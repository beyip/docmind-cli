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

**sha256 (yama #6 build):** `ddf85fe9060af515c78cc99a21ed7aacf5b9f3bdbb7e59f243c3fc9581817c65` · test: `t9.py` (telefon + bilgisayar senaryoları) yeşil. (Güncel build için §9.)

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

## 9) Mobilde hiçbir şey birbirinin üzerine yazmıyor (yama #7)

**Şikâyet:** "`/mobile` yazdıktan sonra mobilde iç içe giriyor." Yani mesajlar birbirinin, durum satırının
ve prompt'un üzerine basılıyor.

### Gerçek sebep (iki tane)
1. **Altlık geri geliyordu.** Mobil modda `start_footer()` altlığı kurmuyor, ama her komut/turdan sonra
   çalışan yeniden çizim (`_draw_footer_locked()`) yalnızca "8 satır ve 30 sütun var mı?" diye bakıyordu.
   Sonuç: `self._footer_active = True` + kaydırma bölgesi yeniden kuruluyor ve satır **ekranın son
   satırına** boyanıyordu. Bir sonraki mesaj o satıra yazıldığı için ekranda `DocMind ❯ /quit0` ve
   `T:0 C:0.0% ~$0` metninin bir üst satırın içinde görünmesi ortaya çıkıyordu.
2. **Durum satırı yerinde kalıyordu.** Satır çizildikten sonra mesaj/panel/soru yazılırken silinmiyordu,
   bu yüzden yeni metin onun üzerine geliyordu.

### Çözüm
| # | Değişiklik |
|---|---|
| 1 | Tek karar noktası: `_footer_allowed()` — mobil modda, ANSI olmayan terminalde, 8 satırdan az veya 46 sütundan dar ekranda **False**. |
| 2 | `start_footer()` ve **her** yeniden çizim bu kararı kullanıyor; izin yoksa altlık **sökülüyor** (`ESC7 ESC[r ESC8`), yeniden kurulmuyor. |
| 3 | `_inline_status_rows_drawn` + `_inline_status_live`: durum satırı kaç satır çizdiğini hatırlıyor. |
| 4 | `clear_inline_status()` yalnız kendi çizdiği satırları siliyor (`ESC[<n>A ESC[J`); prompt satırına dokunmuyor. |
| 5 | `info` / `success` / `warn` / `print_panel` / `print_alert` / `ask` / `stream_assistant_text` / geçmiş yazımı hepsi önce durum satırını siliyor. |
| 6 | `_at_line_start` + `_ensure_line_start()`: prompt veya akış satırın sahibiyken bayrak `False`, giriş dönünce/mesaj bitince `True`; eksik satır sonu yazılıyor. Cevap artık `DocMind ❯` içinde başlamıyor. |
| 7 | Satır içi durum yalnız gerçek TTY'de çiziliyor (boruya yazarken kirlilik yok). |

### Doğrulama — gerçek terminal ızgarası (pty ekran emülatörü)
`screen_check.py` gerçek bir pty açar, `/mobil`, `/mobil status` ve `/quit` komutlarını yazar, ANSI kodlarını
(imleç hareketi, `ESC[J`/`ESC[K`, kaydırma bölgesi `ESC[r`, kaydet/geri yükle) uygulayıp **ekranı** çizer ve
üzerine yazılan hücreleri sayar. (Basit `len()` kontrolü bu hatayı görmüyordu.)

| Senaryo | Üzerine yazılan karakter |
|---|---|
| Telefon 40×24 (`PHONE=1`) | **0** |
| Telefon 32×24 | **0** |
| Telefon 40×24, `/quit` olmadan | **0** |
| Bilgisayar 80×24 (tam ekran altlık açık) | **0** |
| Bilgisayar 40×24 / 100×24 | **0** |

Ekranda her metin kendi satırında; prompt satırı yalnız `DocMind ❯ /mobil status`; durum satırı ve `[OK]`
satırı başka bir satıra taşmıyor. Ek olarak `py_compile -W error::SyntaxWarning` ✓, `--help` kapıları
**exit 0**, `t1`–`t10` yeşil.

**sha256 (bu build):** `b993155a7e4830eda84321ac6a4bcfb73036f78663c8d8de6925f2b8be489086` · 1.103.438 bayt.

## 10) Telefonda altlık yok — `/mobil` yazılmadan önce de (yama #8)

**Kullanıcının fotoğrafı:** telefon, `/mobil` **henüz yazılmamış** (panoda `mobile mode OFF`), alt satırda
`DocMind > | Context: -0/1,048,576 (0.0%)` — yani durum satırı prompt satırının **içine** basılmış ve
`Unknown command` satırı da yazıyla iç içe. Önceki iki yamadan sonra hâlâ görülen hâl buydu.

### Gerçek sebep
Altlık (footer) kendini **mutlak satır numaralarıyla** çiziyor: `ESC[<satır>;1H`, `ESC[1;<satır-1>r`,
`ESC[2K`. Telefonda ekranın gerçek yüksekliği klavye açılıp kapanınca sürekli değişiyor ve Termux bunu her
zaman bildirmiyor. `/mobil` yazılmadığı sürece mobil mod **kapalı** olduğu için altlık serbest kalıyordu ve
satır, mesajın/prompt'un olduğu yere yazılıyordu. Mobil modu açtığımız senaryolarda (yama #7) bu yüzden
görünmüyordu; telefonda varsayılan hâl ise **kapalı**.

### Çözüm
| # | Değişiklik |
|---|---|
| 1 | `_footer_allowed()` artık **donanıma** bakıyor: telefon/tablet (`_DM_PHONE_DEVICE`), mobil mod, ANSI olmayan terminal, <12 satır veya <46 sütun → **False**. Telefon `/mobil` yazılmadan da altlık almıyor. |
| 2 | `start_footer()` kararı **boyut okumadan önce** veriyor; izin yoksa geri çağrıları bırakıp dönüyor → telefonda kaydırma bölgesi hiç kurulmuyor. |
| 3 | REPL'deki "kalmış altlığı kaldır" temizliği artık telefonda da çalışıyor (yalnız mobil modda değil). |
| 4 | Satır içi durum satırı telefonda, çizildikten sonra ekrana bir şey yazıldıysa **yerinde yeniden yazmıyor**; temiz satırı bekliyor. |

### Doğrulama (pty, adım adım ekran ızgarası — `screen_timeline.py`)
Fotoğraftaki durum birebir kuruldu: telefon (`TERMUX_VERSION`), 56×12, `/hlp` (fotoğraftaki `/hl31` gibi hatalı
komut), `/quit`.

| Senaryo | Üzerine yazılan karakter |
|---|---|
| Telefon 56×12, `/mobil` **yazılmadan**, `/hlp` → `/quit` | **0** (önce: 92) |
| Telefon 56×20 iken klavye açılıyor → 56×12 | **0** |
| Telefon 56×12 iken klavye kapanıyor → 56×20 | **0** |
| Telefon 40×24 · 32×24 · 56×24 (mobil mod açık) | **0** |
| Bilgisayar 80×24 · 100×24 (altlık açık) | **0** |

Ekranda prompt satırı yalnız `DocMind ❯ /hlp`; `[!]` ve `[i]` satırları kendi satırında; durum satırı
`T:0 C:0.0% ~$0` prompt'un içine girmiyor. `py_compile -W error::SyntaxWarning` ✓, `--help` kapıları **exit 0**,
`t1`–`t10` yeşil.

**sha256 (bu build):** `fb9a2a188f29380da0c79a8e03f3eb566e5092e40448d3e03ebb29fdd9c42d32` · 1.104.523 bayt.
