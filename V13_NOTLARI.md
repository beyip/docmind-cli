# DocMind v1.3 — ne geldi, nasıl kullanılır

## 1) Squad Engine — görev parçalama
Karmaşık bir istek geldiğinde DocMind önce tek soru sorar:

```
Bu işi nasıl yapayım?
  [1] Ekip: görevi parçala, paralel ajanlar çalışsın (plan + isimler)
  [2] Tek ajan: parçalamadan DocMind kendisi yapsın
```

Soru **tek dilde** sorulur: arayüz dili neyse o (14 dilin hepsi). Eskiden Türkçe + İngilizce birlikte
yazıyordu; artık tek dil — `How should I build this?`, `Wie soll ich das umsetzen?`, `¿Cómo quieres que lo
haga?`, `Как это сделать?`, `どのように進めますか？`, `어떻게 진행할까요?` …

[1] seçilirse: DocMind **tepede kalır** → `SQUAD_PLAN.md` yazar → ajanlara isim verir → işleri dağıtır →
canlı akışı gösterir → en sonda kendisi kontrol eder ve kusursuzluk denetimi geçmeden turu kapatmaz.

```
  * DocMind plan ready: 3 agents (Nova/planner, Pixel/ui_builder, Atlas/tester)
  > Nova     map the folder and write the plan
     ... Nova is thinking
  [OK] Nova     finished
  > Pixel    build src/ui.py
     - Pixel writing src/ui.py
  [OK] Pixel    finished
```

Komutlar: `/squad` (canlı panel), `/squad auto`, `/squad off`, `/squad agents 4`.
Her koşu `SQUAD_PLAN.md` + `SQUAD_LOG_<zaman>.json` bırakır.
Sınırlar: ajan başına 10 tur, ekip için 45 alt tur / 15 dakika, ajan başına araç beyaz listesi.

## 2) Arama artık kendiliğinden
"internette ara sonra şunu yap" dersen model `web_search`'ü kendi çağırır, kaynakları okur, sonra işi yapar.
`/search <konu>` **silinmedi** — manuel/doğrulamalı araştırma olarak duruyor.

## 3) Mobil (Termux) desteği
- Otomatik algılama: `TERMUX_VERSION`, `ANDROID_ROOT`, 46 sütundan dar terminaller. Elle: `DOCMIND_MOBILE=1|0`
- Depolama erişimi: `~/storage/shared`, `~/storage/downloads`, `~/storage/dcim`, `/sdcard`, `/storage/emulated/0`
- Bozuk metin sorunu: mobilde otomatik ASCII glif seti, `utf-8` + `errors=replace`, satır tamponu,
  sistem promptunda 44 sütun kuralı. `/mobile` cihaz profilini gösterir.
- Kurulum: `pkg install python` → `termux-setup-storage` → `python DocMind.py`

## 4) Uyarı metni
"bu agent bilgisayarınıza tam yetkilidir" → **"bu agent cihazınıza tam yetkilidir"** (EN/DE/IT/NL dahil).

## 5) Owner satırı = imza
`_DM_OWNER = 'OWNER: DEVRAN E. / BEYİP_'` satırı silinir, boşaltılır, çoğaltılır, kaydırılır; ya da
yazdırma satırı / başlık bloğu bozulursa program **her cihazda exit 90** verir. Doğrulama:
tam 1 kez, sütun 0'da, `_DM_OWNER_SEAL` ile mühürlü, başlık dosyanın ilk baytları.
`DOCMIND_NO_OWNER_CHECK` artık kaçış kapısı değil — kurcalama sayılıyor.

## Doğrulama (bu build üzerinde)
| Test | Sonuç |
|---|---|
| `py_compile` + `--help` kapıları | ✓ exit 0 |
| Owner satırı silindi / boşaltıldı / çoğaltıldı / banner silindi / başlık bozuldu | hepsi **exit 90** ✓ |
| Sahte modelle uçtan uca squad koşusu | 2 ajan, dosyalar yazıldı, plan + log üretildi ✓ |
| Araç beyaz listesi | listede olmayan `write_file` engellendi ✓ |
| Aynı araç çağrısını tekrarlayan ajan | 2 turda kapatıldı (65 değil) ✓ |
| `TERMUX_VERSION` / `COLUMNS=38` | mobil mod algılandı ✓ |
| Prompt katmanları | device satırı + otomatik arama kuralı + `/search` ✓ |
| `/squad`, `/mobile` komutları | çalışıyor, config kaydediliyor ✓ |
| Taze clone + release asset | derleniyor, imza geçiyor, sha256 aynı ✓ |

## 6) Açılış notu — telefondan mı giriyorsun?
Her açılışta, cihazın dilinde tek satır:

```
[i] Telefondan veya tabletten kullanıyorsanız /mobil yazarak mobil modu açın (genişlik, klavye ve glif uyumu).
```

`/mobil` = `/mobile` (aynı komut; yönlendirici, `/help` satırı ve sekme tamamlama hepsinde var).

## 7) Paralel çalışma (artık varsayılan)
- Bağımsız ajanlar **aynı anda** (thread) koşar: 3 ajan × 0,3 sn → **0,30 sn** (sırayla 0,90 sn).
- Aynı dosyayı bildiren ajanlar **ayrı dalgalara** ayrılır → aynı dosyaya iki thread asla yazmaz.
- Her ajan kendi kopyasında: kendi context'i, stream tamponu, araç beyaz listesi. Ana context bozulmaz.
- Bir ajan çökerse "failed" olur, dalganın geri kalanı biter.
- Anahtar: `/squad parallel on|off` (varsayılan **on**).
- **Gerçek paralellik:** her alt ajan kendi çalışan kopyasında koşar (kendi context'i, kendi akışı, kendi
  izin kapsamı) ve çalışırken kullanıcıya **soru sormaz** — API çağrıları gerçekten üst üste biner.
  Ölçüm: 3 ajan = **3 eşzamanlı çağrı**, 0,72 sn (sırayla ≥1,05 sn).
- **Dosya sahipliği:** iki ajan aynı dosyayı isterse ilk alan dosyayı **sahiplenir**, diğeri
  `app.py şu anda Nova tarafından düzenleniyor; dokunmadım` notuyla o dosyayı erteler — sessizce ezmez.
- **Ekip bitince son söz DocMind'ın:** birleştirme + doğrulama turunu (review) kendisi koşar; iş sana kalmaz.
- Canlı akış: `~ running 3 agents in parallel, 1 wave(s)` · `▶ wave 1/1: Atlas, Nova, Pixel`

## 8) Yarım kalan mesaj sorunu (yama #3)
- **Sorun:** akış (stream) halinde gelen metin, satır bitmeden terminale tek parça yazılıyordu; terminal
  satırı kendi başına kaydırınca — özellikle dar telefon ekranında — mesajın geri kalanı kayboluyordu.
- **Çözüm:** metin terminale yazılmadan **önce** gerçek genişliğe göre sarılıyor (`_wrap_ansi_line`,
  `_last_wrap_point`). Satır artık terminal tarafından bölünmüyor, mesaj her zaman bittiği yerde bitiyor.
- İlk akış satırı `DocMind: ` etiketinin kalan yerini kullanıyor (eskiden 0. sütundan başlayıp ekranı
  taşırıyordu). Ölçüm: 24/40/80/100/120 sütun — en geniş satır her zaman terminalin içinde.
- Kontrol baytları temizleniyor: tek başına `\r` (satırın kendini yeniden basmasına yol açan şey), NUL,
  sıfır genişlikli boşluk… DocMind'ın kendi renk kodları ise korunuyor (eskiden `[31m` diye düz metin
  olarak sızıyordu).
- Emoji ve CJK karakterler **2 sütun** sayılıyor → kutular, çubuklar, paneller ve araç çıktıları dar
  Termux ekranında da hizalı kalıyor (40 sütunda en geniş satır 38).
- Akış her zaman kendi satırında bitiyor: yarım cümlede, `Ctrl+C` sonrasında, boş cevapta ve
  `docmind | head` gibi kapanan boru hattında da.
- **Genel hata taraması:** `Ctrl+D`/kapalı stdin artık traceback basmıyor; NUL içeren yol net bir hata
  veriyor; dosya yazmaları `UnicodeEncodeError` ile çökmüyor; `aggressive_*` metinleri 14 dilin
  **hepsinde** var (her dilde 337 anahtar); ekip hatası mesajı `{err}` yerine gerçek hatayı yazıyor.

**Sürüm:** hâlâ **v1.3** — yeni sürüm çıkmadı, bu düzeltmeler v1.3'ün içine girdi (v1.4 yok).
`__version__ = "1.3"`, terminal banner'ı da v1.3 yazıyor.

## 9) `/mobil` artık gerçek bir anahtar ve yalnızca telefonda
- **Telefonda:** `/mobil` ilk kullanımda mobil modu **açar** (kompakt düzen, sade glifler, tam ekran
  altlık yok, modele "dar yaz" kuralı), tekrar kullanınca **kapatır**. Seçim `config.json`'a yazılır,
  yeniden açılışta hatırlanır. `/mobil on|off` sabitler, `/mobil status` paneli gösterir.
- **Bilgisayarda:** `/mobil` hiçbir şey değiştirmez; "mobil mod yalnızca telefonda/tablette çalışır" der.
  Dar bir pencere bile telefon sayılmaz. Açılıştaki `/mobil` notu artık yalnızca telefonda basılıyor.
- **46 sütundan dar terminallerde** tam ekran altlık kapanır — telefonda mesajın yarısını yiyordu.
- **Boru hattı girişi** (`printf "/mobil\n" | docmind`): cevap artık `DocMind ❯` satırına yapışmıyor,
  prompt satırı önce kapanıyor.
- **Açılışta tek satır (14 dil):** sistem cihazı kendisi algılar ve tek cümleyle söyler —
  `[i] 📱 Cihazınız otomatik algılandı: telefon/tablet · mobil mod AÇIK. DocMind kendini cihazınıza göre
  ayarlar.` Bilgisayarda aynı cümle `bilgisayar · mobil mod KAPALI` der. Tek dil, tek satır, her açılışta bir kez.
- **Durum satırı üst üste binmiyor:** altlık kapalıyken (mobil mod / 46 sütundan dar terminal) bağlam ve
  maliyet **tek satır** olarak gösterilir; sayılar değişmediyse yeniden basılmaz, değiştiyse aynı satır
  yerinde güncellenir. Sığmazsa iki-üç kısa satıra bölünür — hiçbir zaman terminal tarafından üstteki
  satırın üzerine sarılmaz. Paneller de 80 sütun varsaymıyor (`/tokens` başlığı ve çizgisi ekrana uyuyor).

## 10) Mobilde iç içe girme bitti (yama #7)

> "/mobile yazdıktan sonra mobilde iç içe giriyor."

**Sebep 1 — altlık kendini geri açıyordu.** Mobil modda altlık kurulmuyordu ama her turdan sonra çalışan
yeniden çizim yalnız "8 satır / 30 sütun var mı" diye bakıp `_footer_active = True` yapıyor ve satırı
ekranın **son satırına** basıyordu. Bir sonraki mesaj o satıra yazıldığı için `DocMind ❯ /quit0` ve durum
satırının bir üst satırın içine girmesi görülüyordu.

**Sebep 2 — durum satırı silinmiyordu.** `T:… C:… ~$…` çizildikten sonra mesaj/panel/soru/akış yazılırken
temizlenmiyor, yeni metin onun üzerine geliyordu.

**Çözüm:**
- `_footer_allowed()` tek karar noktası: mobil mod, ANSI olmayan terminal, <8 satır veya <46 sütun → **False**.
  `start_footer()` ve her yeniden çizim bunu kullanıyor; izin yoksa altlık **sökülüyor**, yeniden kurulmuyor.
- `clear_inline_status()`: durum satırı kaç satır çizdiğini hatırlıyor ve yalnız o satırları siliyor
  (`ESC[<n>A` + `ESC[J`); prompt satırına asla dokunmuyor. `info/success/warn/panel/alert/ask/stream/geçmiş`
  hepsi yazmadan önce çağırıyor.
- `_at_line_start` + `_ensure_line_start()`: prompt veya akış satırın sahibiyken bayrak kapalı, giriş dönünce
  açılıyor; eksik satır sonu otomatik yazılıyor → cevap artık `DocMind ❯` satırı içinde başlamıyor.
- Satır içi durum yalnız gerçek TTY'de çiziliyor.

**Kanıt (pty ekran emülatörü, `screen_check.py`):** ANSI imleç hareketleri, `ESC[J/K`, kaydırma bölgesi
`ESC[r` uygulanıp ekran gerçekten çiziliyor ve üzerine yazılan hücreler sayılıyor.

| Senaryo | Üzerine yazılan karakter |
|---|---|
| Telefon 40×24 | **0** |
| Telefon 32×24 | **0** |
| Telefon 40×24 (`/quit` olmadan) | **0** |
| Bilgisayar 80×24 (altlık açık) | **0** |
| Bilgisayar 40×24 · 100×24 | **0** |

Prompt satırı yalnız `DocMind ❯ /mobil status`; `[i]`/`[OK]`/panel/durum satırı hepsi kendi satırında.
`py_compile -W error::SyntaxWarning` ✓ · `--help` kapıları **exit 0** · `t1`–`t10` yeşil.
**sha256:** `b993155a7e4830eda84321ac6a4bcfb73036f78663c8d8de6925f2b8be489086` · 1.103.438 bayt.

## 11) Telefonda altlık tamamen kapalı (yama #8) — fotoğraftaki hâl

Fotoğrafta `/mobil` **yazılmamıştı**, yani mobil mod kapalıydı; o durumda tam ekran altlık hâlâ açıktı.
Altlık mutlak satır numaralarıyla çiziliyor (`ESC[<satır>;1H`, `ESC[r`), telefonda ise klavye açılınca ekran
yüksekliği değişiyor ve Termux bunu her zaman bildirmiyor → satır, prompt'un/mesajın olduğu yere yazılıyordu
(`DocMind > | Context: -0/1,048,576 (0.0%)`).

- `_footer_allowed()` artık donanıma bakıyor: telefon/tablet, mobil mod, ANSI yok, <12 satır, <46 sütun → kapalı.
- `start_footer()` kararı boyut okumadan önce veriyor; izin yoksa kaydırma bölgesi hiç kurulmuyor.
- REPL'deki altlık temizliği telefonda da çalışıyor.
- Telefonda durum satırı, üzerine yazı olduysa yerinde yeniden yazılmıyor; temiz satırda basılıyor.

**Kanıt (`screen_timeline.py`, adım adım ekran ızgarası):** telefon 56×12 + `/hlp` + `/quit` → **0**
üzerine yazılan karakter (önce 92); klavye açılması (20→12 satır) **0**; klavye kapanması (12→20) **0**;
telefon 40/32/56 sütun ve bilgisayar 80/100 sütun **0**. `t1`–`t10` yeşil.
**sha256:** `fb9a2a188f29380da0c79a8e03f3eb566e5092e40448d3e03ebb29fdd9c42d32` · 1.104.523 bayt.
