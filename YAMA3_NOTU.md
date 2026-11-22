# v1.3 yama #3 — "mesaj terminalde yarım kalıyor" + genel hata taraması

Sürüm **v1.3** (v1.4 yok). `__version__ = "1.3"`.
sha256 `46f3ec72fa70b8e24ee150c4d9468c864ccb0c18ba1de8c3405fed58bcb8205f` · 1.078.915 bayt.

## 1) Sorunun gerçek sebebi
Akış halinde (stream) gelen metin, satır tamamlanmadan **olduğu gibi** terminale yazılıyordu. Uzun satırı
terminale bırakınca terminal kendi başına kaydırıyor; dar ekranda (telefon / Termux) satırın devamı
görünmüyor, geri dönen `\r` yüzünden satır kendini yeniden basıyor → *"mesaj yarım kaldı"*.

Ölçtüğüm somut durum: 100 sütunluk terminalde ilk satır **102** hücre, 120 sütunda **125** hücre
oluyordu — çünkü ilk akış satırı `DocMind: ` etiketinin kapladığı 9 hücreyi hesaba katmıyordu.

## 2) Ne değişti
| # | Değişiklik |
|---|---|
| 1 | `_last_wrap_point()` eklendi: satırı son sığan boşluktan böler (ANSI renkleri sütun saymaz). |
| 2 | `stream_assistant_text()` artık **yazmadan önce** sarıyor: tamamlanan satır hemen, yarım satır sadece sığdığı kadar gönderiliyor. |
| 3 | İlk akış satırı `DocMind: ` etiketinden kalan yeri kullanıyor (9 hücre). |
| 4 | `_sanitize_stream_chunk()` SGR renk kodlarını **koruyor**; tek başına `\r`, NUL, C0/C1, sıfır genişlikli boşluk atılıyor. |
| 5 | Banner etiketi (`DocMind v1.3 • OWNER: …`) sığmıyorsa logonun altına, sarılmış olarak basılıyor. |
| 6 | Başlangıç yetki uyarısı ve `/mobil` notu artık ekran genişliğine göre sarılıyor. |
| 7 | Cevap her zaman kendi satırında bitiyor: yarım cümle, `Ctrl+C`, boş yanıt, kapanan boru (`docmind \| head`). |
| 8 | `Ctrl+D` / kapalı stdin: traceback yok — prompt satırı kapanıyor, "Görüşmek üzere" **yeni satırda**. |

## 3) Genel hata taramasında çıkanlar
- **Yol (path):** NUL baytı içeren yol `lstat: embedded null character` diye çökertiyordu → artık net
  `ValueError`; çözülemeyen yol güvenli yedekle dönüyor.
- **Dosya yazma:** atomik yazma ve `/export`, hedef kodlamada karşılığı olmayan karakterde
  `UnicodeEncodeError` atıyordu → `errors="replace"`.
- **i18n:** `aggressive_*` anahtarlarının 10 tanesi yalnızca tr/en/de'de vardı → 14 dilin **hepsinde**
  (her dilde **337** anahtar, hepsi `{}` format denetiminden geçti).
- **Ekip hatası metni:** `t("squad_failed_single").format(err=…)` yerine `t("squad_failed_single", err=…)`
  → ekranda `{err}` değil gerçek hata.
- **`console.newline()`** eklendi: satırı güvenli şekilde bitiren tek yer.

## 4) Doğrulama
| Test | Sonuç |
|---|---|
| `py_compile -W error::SyntaxWarning` | ✓ |
| `python3 DocMind.py --help` (sahip + imza kapıları) | exit **0** |
| Gerçek `ConsoleUI`, 40 sütun, 6.000+ karakter akış | en geniş satır **39/39**, 0 taşma, tüm kelimeler yerinde |
| Aynı test 24 / 80 / 100 / 120 sütun | en geniş satır 20 / 75 / 93 / 114 — hepsi sınırın içinde |
| Tek dev parça (7.200 karakter, hiç `\n` yok) | 240 satır, en geniş 34, 1200/1200 kelime korundu |
| Emoji/CJK: 60× 📱 | 36+36+36+12 = 120 hücre, taşma yok |
| Gerçek CLI, pty, 40 ve 60 sütun (`/help` + `/quit`) | **hiçbir satır** terminalden taşmıyor |
| `/quit` ve `Ctrl+D` çıkışı | tek satırda birleşme yok, traceback yok |
| `t6.py` · `t7.py` · `t8.py` | hepsi yeşil (t7: `failures: none`) |
| `t1`–`t5` (squad / mobil / doküman / gerçek ajan) | exit 0 |

## 5) Nerede
`beyip/docmind-cli` · `main` · commit `64195bb` · release v1.3 asset `DocMind.py` (1.078.915 bayt)
