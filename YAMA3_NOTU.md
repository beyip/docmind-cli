# v1.3 yama #3 — "mesaj terminalde yarım kalıyor" + genel hata taraması

Sürüm **v1.3** (v1.4 yok). `__version__ = "1.3"`.
sha256 `ddf85fe9060af515c78cc99a21ed7aacf5b9f3bdbb7e59f243c3fc9581817c65` · 1,100,585 bayt.

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

## 6) Ek: `/mobil` gerçek anahtar (aynı sürüm, v1.3)
- Telefonda `/mobil` → aç, tekrar `/mobil` → kapat (on/off döngüsü), seçim kalıcı.
- Bilgisayarda `/mobil` → hiçbir şey değişmez, "bu cihaz bilgisayar" der; dar pencere de telefon sayılmaz.
- Açıkken: kompakt düzen, sade glifler, tam ekran altlık yok, prompt `DM:` , modele dar yazma kuralı.
- 46 sütundan dar terminallerde altlık zaten kapalı; boru hattı girişinde cevap prompt satırına yapışmıyor.

**sha256 (bu build):** `ddf85fe9060af515c78cc99a21ed7aacf5b9f3bdbb7e59f243c3fc9581817c65` · test: `t9.py` (telefon + bilgisayar senaryoları) yeşil.

## 7) Açılışta tek cümle (son ek)
- Her açılışta **tek satır**, 14 dilin hepsinde, o anki arayüz dilinde:
  `[i] 📱 Cihazınız otomatik algılandı: telefon/tablet · mobil mod AÇIK. DocMind kendini cihazınıza göre ayarlar.`
- Cihaz **otomatik** algılanır (Termux/Android/iOS), kullanıcı hiçbir şey seçmez; bilgisayarda aynı cümle
  `bilgisayar · mobil mod KAPALI` der. `/mobil` notu telefonda da bilgisayarda da aynı biçimde basılır.

## 8) Mobilde bağlam/maliyet satırı üst üste binmiyor (son düzeltme)
- Sebep: altlık kapalıyken durum satırı **her turdan sonra** yeniden basılıyordu ve kompakt biçim `len()` ile
  ölçülüyordu; telefonda aynı sayılar üst üste yığılıyor, ekrandan uzun satırı terminal alttaki/üstteki
  satırın üzerine sarıyordu.
- Çözüm: durum **tur başına tek satır** — değişmediyse hiç basılmaz, değiştiyse aynı satır yerinde
  güncellenir (`ESC[1A` + `ESC[2K`). Genişlik gerçek sütuna göre ve `_display_width` ile ölçülür; sığmazsa
  2–3 kısa satıra bölünür. `/tokens`, canlı altlık ve REPL hepsi genişliğini geçiriyor.
- Paneller artık 80 sütun varsaymıyor: `=== başlık` satırı sarılıyor, kapanış çizgisi ekranı geçmiyor.

**Doğrulama:** 40 / 32 / 60 sütun gerçek CLI — taşan satır **0**, tekrar eden durum satırı **0**;
`t10.py` (durum satırı testi) 3 genişlikte yeşil; `t1`–`t9` yeşil.
