# ==================================================
# DocMind CLI AI Agent
# Author / Creator: DEVRAN E. / BEYİP_
# Social / Handle: BEYİP_
# License: MIT License
# ==================================================
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 DEVRAN E. / BEYİP_
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
"""DocMind: universal cross-platform (Windows & Linux) terminal AI agent, standard library only.

Creator / Owner: DEVRAN E. / BEYİP_
Run: python DocMind.py   (Windows)  |  python3 DocMind.py   (Linux / macOS)
No packages are downloaded or installed automatically by this file.
"""
from __future__ import annotations

import hashlib as _dm_hashlib
import hmac as _dm_hmac
import os as _dm_os
import re as _dm_re
import sys as _dm_sys
import types as _dm_types
from pathlib import Path as _dm_Path

_DM_OWNER = 'OWNER: DEVRAN E. / BEYİP_'
_DM_OWNER_SEAL = '331d0a8f198cf003c1c0fb9fc09d279aa3d4d2256e016a31bc86d00a89c8b921'
_DM_SOURCE_HASH = 'bcbfc762ddf195324143fb1aa66f93beae6334586e145ca5906b363c3ba95e33'
_DM_SIGNATURE = '18460a56f66f64658b8c00b4b507b20da57b180312916b64f3a9e2835aaa9ed23e9b7c2a93426b7d4455c36d12ca42482641602492ba19c111504158a569506eb1a9edb7293340f4af505f3c669534eca8a2ee9bfb673ff296dfd3ba3385f7b090a19adfe4d8f21b9e923e82ddba24be2f6109ab3d2e59ae82fa278576f5722f938a97cfa6517e17f0360bd7e97886080f4ecaae26d6628ade7fb267727aae943893aa5ab38a16a47bf5e856af9e005d6c5f4d2d32309a3c94ebf2991fe58ff2bff950a55e91eddba7733971faf811fb27ec7e5c0367e8753d4b2e3e147156cd4b5d932bfe221e7733d8ed128e4467f6955ab8442ad7233b38ad4b52ab47569dff81bd92c3df245a895851b06765a4d149467e2e276afc587e07e7d5abd9ad9f20feab28f1fce447d9ca6340d713d493d0c7f8e934bc139460d1cb6692ec6bb79416e5e68e1973cc040737a9311548e4cd68ba735f7bd494e96ee9d1d3d079ceb1d780201b355d02c8e2fd9b3087e085faef2a896311c0c684f2e52635b1365c'
_DM_PUBLIC_N = int('d74101779df580215c069cb8de5be8e6c076ff21846b463da6bbfcfb0428964094825d4c5ed862d615f1764e1d1cee2d78bc9a425d9d9c1bfb4b288135667cc4a282e1bbfcf4909eff8b5e5964613a9469e4a64c64409f7140aa4faabe20e57294cb821e1e49f4b0c66f4583649d02d55d84dda95afeac7d33dbfccde2ccae4c16a141139719f06b4aa06ebf4a3a04f992e21cb952a9c5ce0c6b3b7ae7c5d21e980b1b562d97d5363eb0f8ada97a2b54a5607f91b92a702086f70fba96d34f94d4feb82a8abfe97d2f0ba991b8202a0e3ced9c3e717befc9f5b347ea2e48388027a88f1cff41216f5028fd33072beee1e3ccdee937e5ce278c1a5a320a8d3d20705018d31e621930d62d7dd22b0b84ad25ec4c70d79e2bed27320fa070d3c040873ea8154d5c2519191a22078dd8d529c033eb5c5a7d03a6994da54a41ea043b6546985dda89b9f717ff9f79afe049a519dc516f78eb3bcf8832b2d99ad4854d98fe5531d7472a0bddb1ec564048881bca54225cb283ebe0cfae0c9685afdd11', 16)
_DM_SOURCE_PATH = _dm_Path(__file__).resolve()
_DM_REQUIRED_HEADER = (
    '# ==================================================\n'
    '# DocMind CLI AI Agent\n'
    '# Author / Creator: DEVRAN E. / BEYİP_\n'
    '# Social / Handle: BEYİP_\n'
    '# License: MIT License\n'
    '# ==================================================\n'
).encode('utf-8')
def _dm_attestation_failure(reason=''):
    try:
        msg = (
            '\x1b[1;31m[KORUMA KİLİDİ] DocMind imza / sahip doğrulaması başarısız! '
            '(OWNER: DEVRAN E. / BEYİP_ imzası veya kaynak bütünlüğü silinmiş/değiştirilmiş; kod çalıştırılamaz.)\x1b[0m\n'
        )
        _dm_sys.stderr.write(msg)
        _dm_sys.stderr.flush()
    finally:
        raise SystemExit(90)
def _dm_owner_gate():
    try:
        if not isinstance(_DM_OWNER, str) or 'DEVRAN E.' not in _DM_OWNER or 'BEYİP_' not in _DM_OWNER:
            raise ValueError('Owner identity missing')
        calc_seal = _dm_hashlib.sha256(_DM_OWNER.encode('utf-8')).hexdigest()
        if not _dm_hmac.compare_digest(calc_seal, _DM_OWNER_SEAL):
            raise ValueError('Owner seal mismatch')
        raw = _DM_SOURCE_PATH.read_bytes()
        if not raw.startswith(_DM_REQUIRED_HEADER):
            raise ValueError('Required owner header altered')
        if ("_DM_OWNER = '" + _DM_OWNER + "'").encode('utf-8') not in raw:
            raise ValueError('Owner constant altered in source')
    except Exception:
        _dm_attestation_failure('owner')
def _dm_attestation_data():
    data = _DM_SOURCE_PATH.read_bytes()
    hash_matches = list(_dm_re.finditer(br"(?m)^_DM_SOURCE_HASH = '([0-9a-f]{64})'$", data))
    sig_matches = list(_dm_re.finditer(br"(?m)^_DM_SIGNATURE = '([0-9a-f]{768})'$", data))
    if len(hash_matches) != 1 or len(sig_matches) != 1 or not data.startswith(_DM_REQUIRED_HEADER):
        raise ValueError('Invalid attestation metadata')
    h, s = hash_matches[0], sig_matches[0]
    canonical = bytearray(data)
    canonical[h.start(1):h.end(1)] = b'0' * 64
    canonical[s.start(1):s.end(1)] = b'0' * 768
    return bytes(canonical), h.group(1).decode('ascii'), bytes.fromhex(s.group(1).decode('ascii'))
def _dm_digest_gate():
    try:
        canonical, expected, _signature = _dm_attestation_data()
        digest = _dm_hashlib.sha256(canonical).hexdigest()
        if not _dm_hmac.compare_digest(digest, expected):
            raise ValueError('Digest mismatch')
    except Exception:
        _dm_attestation_failure('digest')
def _dm_signature_gate():
    try:
        canonical, _expected, signature = _dm_attestation_data()
        key_size = (_DM_PUBLIC_N.bit_length() + 7) // 8
        if len(signature) != key_size or int.from_bytes(signature, 'big') >= _DM_PUBLIC_N:
            raise ValueError('Invalid signature size')
        actual = pow(int.from_bytes(signature, 'big'), 65537, _DM_PUBLIC_N).to_bytes(key_size, 'big')
        digest_info = bytes.fromhex('3031300d060960864801650304020105000420') + _dm_hashlib.sha256(canonical).digest()
        pad_len = key_size - len(digest_info) - 3
        if pad_len < 8:
            raise ValueError('Invalid public key')
        expected = bytes.fromhex('0001') + bytes.fromhex('ff') * pad_len + bytes.fromhex('00') + digest_info
        if not _dm_hmac.compare_digest(actual, expected):
            raise ValueError('Signature mismatch')
    except Exception:
        _dm_attestation_failure('signature')
if _dm_os.name == 'nt':
    try:
        import ctypes as _dm_ctypes
        _dm_k32 = _dm_ctypes.windll.kernel32
        for _dm_hid in (-11, -12):
            _dm_h = _dm_k32.GetStdHandle(_dm_hid)
            if _dm_h and _dm_h != -1:
                _dm_m = _dm_ctypes.c_ulong()
                if _dm_k32.GetConsoleMode(_dm_h, _dm_ctypes.byref(_dm_m)):
                    _dm_k32.SetConsoleMode(_dm_h, _dm_m.value | 0x0004)
    except Exception:
        pass
for _dm_stream in (_dm_sys.stdout, _dm_sys.stderr):
    try:
        if hasattr(_dm_stream, 'reconfigure'):
            _dm_stream.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
_dm_owner_gate()
_dm_digest_gate()
_dm_signature_gate()
if __name__ == '__main__':
    print(_DM_OWNER, flush=True)
def _dm_package(name):
    mod = _dm_sys.modules.get(name)
    if mod is None:
        mod = _dm_types.ModuleType(name)
        mod.__package__ = name
        mod.__path__ = []
        _dm_sys.modules[name] = mod
        if "." in name:
            parent, _, leaf = name.rpartition(".")
            setattr(_dm_sys.modules[parent], leaf, mod)
    return mod
def _dm_install(name, factory, is_package=False):
    parent, _, leaf = name.rpartition(".")
    if is_package:
        mod = _dm_package(name)
    else:
        mod = _dm_types.ModuleType(name)
        mod.__package__ = parent
        _dm_sys.modules[name] = mod
        setattr(_dm_sys.modules[parent], leaf, mod)
    mod.__dict__.update(factory())
    return mod
for _package_name in ("docmind", "docmind.i18n", "docmind.core", "docmind.tools", "docmind.ui"):
    _dm_package(_package_name)

# ===== docmind/__init__.py (included source) =====
def _dm_module_00():
 """
 DocMind - Autonomous Cross-Platform Terminal AI Agent
 Creator / Owner: DEVRAN E. / BEYİP_
 """
 __app_name__ = "DocMind"
 __version__ = "1.0"
 __author__ = "DEVRAN E. / BEYİP_"
 __handle__ = "BEYİP_"
 return locals()
_dm_install('docmind', _dm_module_00, True)

# ===== docmind/i18n/locales.py (included source) =====
def _dm_module_01():
 """
 DocMind Multi-Language Dictionary (TR, EN, DE, ES, FR, RU)
 """
 from typing import Dict, List, Tuple
 LANGUAGE_CHOICES: List[Tuple[str, str, str]] = [
   ("tr", "Türkçe", "TR - Türkçe (Varsayılan)"),
   ("en", "English", "EN - English"),
   ("de", "Deutsch", "DE - Deutsch"),
   ("es", "Español", "ES - Español"),
   ("fr", "Français", "FR - Français"),
   ("ru", "Русский", "RU - Русский"),
 ]
 TRANSLATIONS: Dict[str, Dict[str, str]] = {
   "tr": {
     "lang_name": "Türkçe",
     "ai_lang_instruction": "Kullanıcıyla aksi belirtilmedikçe her zaman akıcı, doğal ve anlaşılır TÜRKÇE ile iletişim kur.",
     "welcome_subtitle": "Yeni Nesil Otonom Terminal Yapay Zeka Ajanı",
     "ready_hint": "DocMind hazır! İstediğin görevi yaz, dosyaları düzenlet veya komut çalıştır.",
     "type_help_hint": "Komutlar için /help | Dil için /lang | API için /api | Çıkış için /exit yazın.",
     "prompt_placeholder": "DocMind'a bir görev verin (çok satır için sonuna \\ koyun)...",
     "wiz_title": "DOCMIND İLK KURULUM SİHİRBAZI",
     "wiz_select_lang": "Lütfen kullanmak istediğiniz dili seçin (1-6) [Varsayılan: 1]: ",
     "wiz_lang_saved": "Dil ayarlandı: Türkçe (TR)",
     "wiz_select_provider": "Yapay Zeka API Sağlayıcısını Seçin",
     "wiz_provider_prompt": "Seçiminiz (1-7) [Varsayılan: 1]: ",
     "wiz_select_model": "{provider} için Model Seçin",
     "wiz_custom_model_opt": "Özel model adı gir...",
     "wiz_model_prompt": "Model seçiminiz [Varsayılan: 1]: ",
     "wiz_custom_model_prompt": "Model adını tam olarak yazın (örn. gpt-4o-mini): ",
     "wiz_enter_base_url": "API Base URL girin [Varsayılan: {default}]: ",
     "wiz_enter_api_key": "{provider} API Anahtarınızı (API Key) girin: ",
     "wiz_api_key_optional": "{provider} API Anahtarı (yerel sunucuysa boş bırakabilirsiniz): ",
     "wiz_api_key_empty": "UYARI: API anahtarı boş bırakılamaz! Lütfen geçerli bir API anahtarı girin veya yerel sağlayıcı seçin.",
     "wiz_testing_api": "API bağlantısı ve anahtar doğrulanıyor...",
     "wiz_api_ok": "Harika! {provider} ({model}) bağlantısı başarıyla doğrulandı.",
     "wiz_api_fail_menu": "API doğrulaması sırasında bir sorun oluştu. Ne yapmak istersiniz?",
     "wiz_opt_retry_key": "Yeni API Anahtarı Gir",
     "wiz_opt_change_provider": "Farklı API Sağlayıcısı / Model Seç",
     "wiz_opt_skip_anyway": "Bu Hatayı Geç ve Yine de Kaydet (Sonra /api ile değiştirebilirsiniz)",
     "wiz_select_mode": "Çalışma ve Güvenlik Modunu Seçin",
     "wiz_mode_smart": "Akıllı Onay Modu (Önerilen - Okuma serbest, dosya değiştirme/komutlarda onay sorar)",
     "wiz_mode_auto": "Tam Otomatik Mod (Sınırsız - Onay sormadan tüm işlemleri anında uygular)",
     "wiz_mode_prompt": "Mod seçiminiz (1-2) [Varsayılan: 1]: ",
     "wiz_complete": "Kurulum tamamlandı! Ayarlarınız ~/.docmind-single/config.json dosyasına güvenle kaydedildi.",
     "mode_smart_short": "AKILLI ONAY",
     "mode_auto_short": "TAM OTOMATİK",
     "status_tokens": "Token: {total} (Giriş:{inp} / Çıkış:{out})",
     "status_no_key": "API ANAHTARI YOK (/api yazın)",
     "thinking": "DocMind düşünüyor ve analiz ediyor...",
     "step_counter": "Otonom Adım {step}/{max_steps}",
     "max_steps_reached": "UYARI: Tek seferlik maksimum otonom adım sınırına ({max_steps}) ulaşıldı.",
     "ask_continue_steps": "DocMind çalışmaya devam etsin mi? [E/h]: ",
     "compacting_context": "BİLGİ: Sohbet geçmişi uzadı, token tasarrufu için akıllı özetleme yapılıyor...",
     "context_compacted": "Sohbet geçmişi başarıyla sıkıştırıldı, kesintisiz devam ediliyor.",
     "output_truncated_warn": "UYARI: Modelin tek seferlik yanıt token sınırı dolduğu için yanıt kesildi. Devam etmesi için 'devam et' yazabilirsiniz.",
     "tool_running": "Araç Çalıştırılıyor: {name}",
     "tool_done": "Tamamlandı: {name}",
     "tool_skipped": "Kullanıcı tarafından atlandı: {name}",
     "tool_error_passed": "UYARI: '{name}' aracında sorun oluştu ancak çökmeden atlandı ({err}). DocMind alternatif deneyecek.",
     "perm_title": "İZİN ONAYI GEREKLİ",
     "perm_file_action": "Dosya İşlemi: {action} -> {target}",
     "perm_command_warn": "Terminal Komutu Çalıştırılacak: {cmd}",
     "perm_dangerous_warn": "DİKKAT! KRİTİK / RİSKLİ KOMUT TESPİT EDİLDİ! Lütfen komutu dikkatle kontrol edin!",
     "perm_prompt": "[E]vet çalıştır | [O]tomatik moda geç (bir daha sorma) | [H]ayır atla [Varsayılan: E]: ",
     "perm_dangerous_prompt": "Bu kritik komutu gerçekten çalıştırmak istiyor musunuz? [evet/hayır]: ",
     "perm_switched_auto": "Tam Otomatik Moda geçildi! Tekrar onaylı moda dönmek için /smart yazabilirsiniz.",
     "undo_success": "Son dosya değişikliği geri alındı: {path}",
     "undo_empty": "Geri alınacak bir dosya değişikliği bulunamadı.",
     "err_quota_title": "KRİTİK UYARI: API TOKEN / KREDİ BAKİYESİ BİTTİ!",
     "err_quota_desc": "{provider} hesabınızdaki API kullanım kotası, ücretsiz limit veya kredi bakiyesi tükenmiş görünüyor.\nDetay: {detail}",
     "err_rate_title": "UYARI: API İSTEK / DAKİKALIK TOKEN HIZ LİMİTİ (RATE LIMIT)!",
     "err_rate_desc": "{provider} servisine çok sık istek gönderildi veya dakikalık token sınırı doldu.\nDetay: {detail}",
     "err_auth_title": "UYARI: GEÇERSİZ VEYA YETKİSİZ API ANAHTARI!",
     "err_auth_desc": "{provider} API anahtarınız hatalı, iptal edilmiş veya süresi dolmuş.\nDetay: {detail}",
     "err_context_title": "UYARI: MODEL BAĞLAM (TOKEN) KAPASİTESİ AŞILDI!",
     "err_context_desc": "Gönderilen veri ve geçmiş mesajlar modelin tek seferlik token sınırını aştı. Otomatik sıkıştırma uygulanıyor.\nDetay: {detail}",
     "err_model_title": "UYARI: MODEL BULUNAMADI VEYA ERİŞİMİZ YOK!",
     "err_model_desc": "Seçili model ({model}) bu sağlayıcıda mevcut değil veya hesabınıza açık değil.\nDetay: {detail}",
     "err_server_title": "UYARI: AI SUNUCUSU GEÇİCİ OLARAK YOĞUN / HATALI!",
     "err_server_desc": "{provider} sunucularında geçici bir yoğunluk veya kesinti yaşanıyor.\nDetay: {detail}",
     "err_network_title": "UYARI: İNTERNET / AĞ BAĞLANTI SORUNU!",
     "err_network_desc": "{provider} sunucusuna ulaşılamadı. İnternet bağlantınızı, VPN veya güvenlik duvarını kontrol edin.\nDetay: {detail}",
     "err_tool_title": "UYARI: DOSYA / SİSTEM İŞLEM HATASI (ATLANDI)",
     "err_tool_desc": "İşlem sırasında bir sistem hatası oluştu fakat program durmadı:\nDetay: {detail}",
     "err_unknown_title": "UYARI: BEKLENMEYEN HATA YAKALANDI VE GEÇİLDİ",
     "err_unknown_desc": "İşlem sırasında beklenmeyen bir durum oluştu, sistem güvenli şekilde devam ediyor:\nDetay: {detail}",
     "err_skipped_notice": "Hata güvenli şekilde geçildi. DocMind çalışmaya hazır.",
     "err_retrying_in": "{sec} saniye içinde otomatik tekrar deneniyor (Atlamak için Ctrl+C)...",
     "err_budget_warn_title": "TOKEN KULLANIM UYARISI",
     "err_budget_warn_desc": "Bu oturumda toplam {used} token kullanıldı (Belirlediğiniz uyarı sınırı: {limit}).",
     "rec_title": "KURTARMA SEÇENEKLERİ (Program Kapanmadan Devam Eder)",
     "rec_opt_new_key": "Yeni API Anahtarı Gir ve Devam Et",
     "rec_opt_switch_provider": "Başka AI Sağlayıcısına Geç (Gemini, Groq, OpenRouter, Claude, OpenAI...)",
     "rec_opt_switch_model": "Başka Bir Model Seç ve Devam Et",
     "rec_opt_retry": "Şimdi Tekrar Dene",
     "rec_opt_skip": "Hatayı Geç ve Sohbet Ekranına Dön",
     "rec_choose": "Seçiminiz [Varsayılan: {default}]: ",
     "help_title": "DOCMIND KOMUT REHBERİ",
     "help_body": (
       "  /help              Bu yardım menüsünü gösterir\n"
       "  /setup             Kurulum sihirbazını baştan açar\n"
       "  /api               API sağlayıcısını veya API anahtarını değiştirir\n"
       "  /model             Aktif yapay zeka modelini değiştirir\n"
       "  /lang              Arayüz ve asistan dilini değiştirir (TR, EN, DE, ES, FR, RU)\n"
       "  /auto  (/yolo)     Tam Otomatik Moda geçer (onay sormadan çalıştırır)\n"
       "  /smart             Akıllı Onay Moduna geçer (değişikliklerde onay sorar)\n"
       "  /tokens [limit]    Token istatistiklerini gösterir veya uyarı limiti belirler\n"
       "  /undo              DocMind'ın yaptığı son dosya düzenlemesini geri alır\n"
       "  /tree [yol]        Klasör yapısını ağaç görünümünde listeler\n"
       "  /cd <klasör>       Aktif çalışma dizinini değiştirir\n"
       "  /save [isim]       Sohbet geçmişini kaydeder\n"
       "  /load [isim]       Kaydedilmiş sohbet geçmişini yükler\n"
       "  /doctor            Sistem, ağ ve API sağlık kontrolü yapar\n"
       "  /clear             Ekranı ve mevcut sohbet belleğini temizler\n"
       "  /exit  (/quit)     DocMind'dan güvenli çıkış yapar"
     ),
     "cmd_cleared": "Sohbet geçmişi ve ekran temizlendi.",
     "cmd_saved": "Oturum başarıyla kaydedildi: {path}",
     "cmd_loaded": "Oturum başarıyla yüklendi ({count} mesaj): {path}",
     "cmd_lang_changed": "Dil değiştirildi: {lang}",
     "cmd_mode_changed": "Çalışma modu güncellendi: {mode}",
     "cmd_cd_ok": "Çalışma dizini değiştirildi: {path}",
     "cmd_cd_err": "UYARI: Klasör değiştirilemedi: {err}",
     "cmd_unknown": "Bilinmeyen komut: '{cmd}'. Tüm komutlar için /help yazın.",
     "cmd_exit_bye": "DocMind kapatılıyor. Görüşmek üzere!",
     "ctrl_c_cancelled": "İşlem kullanıcı tarafından durduruldu (Ctrl+C). Sohbete devam edebilirsiniz.",
     "ctrl_c_exit_hint": "Çıkmak için /exit yazın veya tekrar Ctrl+C tuşuna basın.",
     "doctor_title": "DOCMIND SİSTEM & SAĞLIK KONTROLÜ (/doctor)",
     "tokens_report_title": "OTURUM TOKEN VE KULLANIM RAPORU",
   },
   "en": {
     "lang_name": "English",
     "ai_lang_instruction": "Always communicate with the user in clear, natural ENGLISH unless asked otherwise.",
     "welcome_subtitle": "Next-Gen Autonomous Terminal AI Agent",
     "ready_hint": "DocMind is ready! Ask anything, edit files, inspect code, or run commands.",
     "type_help_hint": "Type /help for commands | /lang for language | /api for API settings | /exit to quit.",
     "prompt_placeholder": "Give DocMind a task (end line with \\ for multi-line)...",
     "wiz_title": "DOCMIND INITIAL SETUP WIZARD",
     "wiz_select_lang": "Please select your preferred language (1-6) [Default: 1]: ",
     "wiz_lang_saved": "Language set to: English (EN)",
     "wiz_select_provider": "Select AI API Provider",
     "wiz_provider_prompt": "Your choice (1-7) [Default: 1]: ",
     "wiz_select_model": "Select Model for {provider}",
     "wiz_custom_model_opt": "Enter custom model name...",
     "wiz_model_prompt": "Model choice [Default: 1]: ",
     "wiz_custom_model_prompt": "Enter exact model ID (e.g. gpt-4o-mini): ",
     "wiz_enter_base_url": "Enter API Base URL [Default: {default}]: ",
     "wiz_enter_api_key": "Enter your {provider} API Key: ",
     "wiz_api_key_optional": "{provider} API Key (leave empty if local server requires none): ",
     "wiz_api_key_empty": "WARNING: API key cannot be empty! Please enter a valid key or select a local provider.",
     "wiz_testing_api": "Verifying API connection and key...",
     "wiz_api_ok": "Awesome! {provider} ({model}) connection verified successfully.",
     "wiz_api_fail_menu": "An issue occurred while verifying the API. What would you like to do?",
     "wiz_opt_retry_key": "Enter a New API Key",
     "wiz_opt_change_provider": "Choose Another API Provider / Model",
     "wiz_opt_skip_anyway": "Skip Warning & Save Anyway (You can change later via /api)",
     "wiz_select_mode": "Select Execution & Safety Mode",
     "wiz_mode_smart": "Smart Confirm Mode (Recommended - Free reads, asks before file edits/commands)",
     "wiz_mode_auto": "Full Auto Mode (Unlimited - Executes all file & shell operations immediately)",
     "wiz_mode_prompt": "Mode choice (1-2) [Default: 1]: ",
     "wiz_complete": "Setup complete! Configuration securely saved to ~/.docmind-single/config.json.",
     "mode_smart_short": "SMART CONFIRM",
     "mode_auto_short": "FULL AUTO",
     "status_tokens": "Tokens: {total} (In:{inp} / Out:{out})",
     "status_no_key": "NO API KEY (type /api)",
     "thinking": "DocMind is thinking and analyzing...",
     "step_counter": "Autonomous Step {step}/{max_steps}",
     "max_steps_reached": "WARNING: Reached maximum single-turn autonomous steps ({max_steps}).",
     "ask_continue_steps": "Should DocMind continue working? [Y/n]: ",
     "compacting_context": "INFO: Conversation grew large; running smart context compaction to save tokens...",
     "context_compacted": "Conversation history compacted seamlessly; continuing.",
     "output_truncated_warn": "WARNING: Response hit the single-turn output token limit. Type 'continue' to resume.",
     "tool_running": "Running Tool: {name}",
     "tool_done": "Completed: {name}",
     "tool_skipped": "Skipped by user: {name}",
     "tool_error_passed": "WARNING: Issue in tool '{name}' bypassed safely ({err}). DocMind will adapt.",
     "perm_title": "PERMISSION CONFIRMATION REQUIRED",
     "perm_file_action": "File Operation: {action} -> {target}",
     "perm_command_warn": "Shell Command to Execute: {cmd}",
     "perm_dangerous_warn": "CAUTION! POTENTIALLY DESTRUCTIVE COMMAND DETECTED! Review carefully!",
     "perm_prompt": "[Y]es execute | [A]uto mode (don't ask again) | [N]o skip [Default: Y]: ",
     "perm_dangerous_prompt": "Are you sure you want to execute this critical command? [yes/no]: ",
     "perm_switched_auto": "Switched to Full Auto Mode! Type /smart anytime to re-enable confirmations.",
     "undo_success": "Reverted last file modification: {path}",
     "undo_empty": "No file modifications available to undo.",
     "err_quota_title": "CRITICAL WARNING: API TOKEN / CREDIT QUOTA EXHAUSTED!",
     "err_quota_desc": "Your {provider} API token quota, free tier limit, or billing credit balance is depleted.\nDetail: {detail}",
     "err_rate_title": "WARNING: API RATE LIMIT / TOKENS PER MINUTE EXCEEDED!",
     "err_rate_desc": "Too many requests or per-minute token limit reached on {provider}.\nDetail: {detail}",
     "err_auth_title": "WARNING: INVALID OR EXPIRED API KEY!",
     "err_auth_desc": "Your {provider} API key was rejected, revoked, or expired.\nDetail: {detail}",
     "err_context_title": "WARNING: MODEL CONTEXT TOKEN LIMIT EXCEEDED!",
     "err_context_desc": "Input messages exceeded model context limit. Auto-compacting conversation now.\nDetail: {detail}",
     "err_model_title": "WARNING: MODEL NOT FOUND OR NO ACCESS!",
     "err_model_desc": "Selected model ({model}) does not exist or is unavailable for your account.\nDetail: {detail}",
     "err_server_title": "WARNING: AI SERVER OVERLOADED / TEMPORARY ERROR!",
     "err_server_desc": "{provider} servers experienced temporary overload or downtime.\nDetail: {detail}",
     "err_network_title": "WARNING: NETWORK / INTERNET CONNECTION ISSUE!",
     "err_network_desc": "Could not reach {provider}. Check your internet connection, proxy, or firewall.\nDetail: {detail}",
     "err_tool_title": "WARNING: FILE / SYSTEM OPERATION ERROR (BYPASSED)",
     "err_tool_desc": "A system error occurred during execution and was safely bypassed:\nDetail: {detail}",
     "err_unknown_title": "WARNING: UNEXPECTED ERROR CAUGHT & BYPASSED",
     "err_unknown_desc": "An unexpected issue was caught and safely handled without stopping:\nDetail: {detail}",
     "err_skipped_notice": "Issue bypassed safely. DocMind remains active and ready.",
     "err_retrying_in": "Auto-retrying in {sec}s (Press Ctrl+C to skip wait)...",
     "err_budget_warn_title": "TOKEN BUDGET WARNING",
     "err_budget_warn_desc": "Session used {used} tokens so far (Your warning threshold: {limit}).",
     "rec_title": "RECOVERY OPTIONS (Session Stays Alive)",
     "rec_opt_new_key": "Enter a New API Key & Continue",
     "rec_opt_switch_provider": "Switch AI Provider (Gemini, Groq, OpenRouter, Claude, OpenAI...)",
     "rec_opt_switch_model": "Select Another Model & Continue",
     "rec_opt_retry": "Retry Request Now",
     "rec_opt_skip": "Skip Error & Return to Prompt",
     "rec_choose": "Your choice [Default: {default}]: ",
     "help_title": "DOCMIND COMMAND REFERENCE",
     "help_body": (
       "  /help              Show this command guide\n"
       "  /setup             Re-run the full interactive setup wizard\n"
       "  /api               Change API provider or update API key\n"
       "  /model             Switch active AI model\n"
       "  /lang              Change UI & assistant language (TR, EN, DE, ES, FR, RU)\n"
       "  /auto  (/yolo)     Enable Full Auto Mode (execute without prompts)\n"
       "  /smart             Enable Smart Confirm Mode (ask before changes)\n"
       "  /tokens [limit]    View token usage stats or set token alert limit\n"
       "  /undo              Undo DocMind's most recent file modification\n"
       "  /tree [path]       Display directory tree structure\n"
       "  /cd <dir>          Change current working directory\n"
       "  /save [name]       Save current conversation session\n"
       "  /load [name]       Load a saved conversation session\n"
       "  /doctor            Run system, network & API diagnostics\n"
       "  /clear             Clear screen and reset conversation memory\n"
       "  /exit  (/quit)     Safely exit DocMind"
     ),
     "cmd_cleared": "Conversation memory and screen cleared.",
     "cmd_saved": "Session saved successfully: {path}",
     "cmd_loaded": "Session loaded successfully ({count} messages): {path}",
     "cmd_lang_changed": "Language updated to: {lang}",
     "cmd_mode_changed": "Execution mode updated: {mode}",
     "cmd_cd_ok": "Working directory changed to: {path}",
     "cmd_cd_err": "WARNING: Could not change directory: {err}",
     "cmd_unknown": "Unknown command: '{cmd}'. Type /help for available commands.",
     "cmd_exit_bye": "Closing DocMind. Goodbye!",
     "ctrl_c_cancelled": "Operation cancelled by user (Ctrl+C). Ready for your next instruction.",
     "ctrl_c_exit_hint": "Type /exit or press Ctrl+C again to quit.",
     "doctor_title": "DOCMIND SYSTEM & HEALTH DIAGNOSTICS (/doctor)",
     "tokens_report_title": "SESSION TOKEN & USAGE REPORT",
   },
   "de": {
     "lang_name": "Deutsch",
     "ai_lang_instruction": "Kommuniziere mit dem Benutzer immer auf klarem, natürlichem DEUTSCH, sofern nicht anders gewünscht.",
     "welcome_subtitle": "Autonomer KI-Terminal-Agent der nächsten Generation",
     "ready_hint": "DocMind ist bereit! Stelle Aufgaben, bearbeite Dateien oder führe Befehle aus.",
     "type_help_hint": "/help für Befehle | /lang für Sprache | /api für API | /exit zum Beenden.",
     "prompt_placeholder": "Aufgabe an DocMind eingeben...",
     "wiz_title": "DOCMIND EINRICHTUNGSASSISTENT",
     "wiz_select_lang": "Bitte Sprache wählen (1-6) [Standard: 1]: ",
     "wiz_lang_saved": "Sprache eingestellt: Deutsch (DE)",
     "wiz_select_provider": "KI-API-Anbieter auswählen",
     "wiz_provider_prompt": "Ihre Wahl (1-7) [Standard: 1]: ",
     "wiz_select_model": "Modell für {provider} auswählen",
     "wiz_custom_model_opt": "Eigenen Modellnamen eingeben...",
     "wiz_model_prompt": "Modellwahl [Standard: 1]: ",
     "wiz_custom_model_prompt": "Genaue Modell-ID eingeben: ",
     "wiz_enter_base_url": "API Base-URL eingeben [Standard: {default}]: ",
     "wiz_enter_api_key": "Ihren {provider} API-Schlüssel eingeben: ",
     "wiz_api_key_optional": "{provider} API-Schlüssel (optional bei lokalem Server): ",
     "wiz_api_key_empty": "WARNUNG: API-Schlüssel darf nicht leer sein!",
     "wiz_testing_api": "API-Verbindung und Schlüssel werden geprüft...",
     "wiz_api_ok": "Erfolg! Verbindung zu {provider} ({model}) bestätigt.",
     "wiz_api_fail_menu": "Problem bei der API-Prüfung. Was möchten Sie tun?",
     "wiz_opt_retry_key": "Neuen API-Schlüssel eingeben",
     "wiz_opt_change_provider": "Anderen Anbieter / Modell wählen",
     "wiz_opt_skip_anyway": "Warnung überspringen & trotzdem speichern (/api später nutzbar)",
     "wiz_select_mode": "Sicherheits- & Ausführungsmodus wählen",
     "wiz_mode_smart": "Intelligente Bestätigung (Empfohlen - Lesen frei, fragt vor Änderungen/Befehlen)",
     "wiz_mode_auto": "Vollautomatisch (Führt alle Datei- & Terminal-Aktionen sofort aus)",
     "wiz_mode_prompt": "Moduswahl (1-2) [Standard: 1]: ",
     "wiz_complete": "Einrichtung abgeschlossen! Gespeichert unter ~/.docmind-single/config.json.",
     "mode_smart_short": "BESTÄTIGUNG",
     "mode_auto_short": "VOLLAUTO",
     "status_tokens": "Tokens: {total} (Ein:{inp} / Aus:{out})",
     "status_no_key": "KEIN API-KEY (/api eingeben)",
     "thinking": "DocMind denkt nach und analysiert...",
     "step_counter": "Autonomer Schritt {step}/{max_steps}",
     "max_steps_reached": "WARNUNG: Maximale autonome Schritte ({max_steps}) erreicht.",
     "ask_continue_steps": "Soll DocMind weiterarbeiten? [J/n]: ",
     "compacting_context": "INFO: Verlauf wird zur Token-Einsparung intelligent komprimiert...",
     "context_compacted": "Verlauf erfolgreich komprimiert, fahre fort.",
     "output_truncated_warn": "WARNUNG: Antwort erreichte das Ausgabe-Token-Limit. Tippen Sie 'weiter' zum Fortfahren.",
     "tool_running": "Werkzeug läuft: {name}",
     "tool_done": "Fertig: {name}",
     "tool_skipped": "Vom Benutzer übersprungen: {name}",
     "tool_error_passed": "WARNUNG: Fehler in '{name}' sicher übersprungen ({err}).",
     "perm_title": "BESTÄTIGUNG ERFORDERLICH",
     "perm_file_action": "Dateiaktion: {action} -> {target}",
     "perm_command_warn": "Auszuführender Befehl: {cmd}",
     "perm_dangerous_warn": "ACHTUNG! KRITISCHER BEFEHL ERKANNT! Bitte sorgfältig prüfen!",
     "perm_prompt": "[J]a ausführen | [A]utomatikmodus | [N]ein überspringen [Standard: J]: ",
     "perm_dangerous_prompt": "Diesen kritischen Befehl wirklich ausführen? [yes/no]: ",
     "perm_switched_auto": "Vollautomatischer Modus aktiviert! (/smart zum Zurückwechseln)",
     "undo_success": "Letzte Dateiänderung rückgängig gemacht: {path}",
     "undo_empty": "Keine Dateiänderung zum Rückgängigmachen vorhanden.",
     "err_quota_title": "KRITISCHE WARNUNG: API-TOKEN / GUTHABEN AUFGEBRAUCHT!",
     "err_quota_desc": "Ihr {provider} API-Kontingent oder Guthaben ist erschöpft.\nDetail: {detail}",
     "err_rate_title": "WARNUNG: API-RATENLIMIT ÜBERSCHRITTEN!",
     "err_rate_desc": "Zu viele Anfragen pro Minute bei {provider}.\nDetail: {detail}",
     "err_auth_title": "WARNUNG: UNGÜLTIGER ODER ABGELAUFENER API-SCHLÜSSEL!",
     "err_auth_desc": "Ihr {provider} API-Schlüssel wurde abgelehnt.\nDetail: {detail}",
     "err_context_title": "WARNUNG: KONTEXT-TOKEN-LIMIT ÜBERSCHRITTEN!",
     "err_context_desc": "Kontextlimit erreicht. Automatische Komprimierung startet.\nDetail: {detail}",
     "err_model_title": "WARNUNG: MODELL NICHT GEFUNDEN!",
     "err_model_desc": "Modell ({model}) nicht verfügbar.\nDetail: {detail}",
     "err_server_title": "WARNUNG: KI-SERVER ÜBERLASTET / TEMPORÄRER FEHLER!",
     "err_server_desc": "{provider} meldet vorübergehende Serverprobleme.\nDetail: {detail}",
     "err_network_title": "WARNUNG: NETZWERK- / INTERNETFEHLER!",
     "err_network_desc": "{provider} nicht erreichbar. Bitte Internetverbindung prüfen.\nDetail: {detail}",
     "err_tool_title": "WARNUNG: DATEI- / SYSTEMFEHLER (ÜBERSPRUNGEN)",
     "err_tool_desc": "Systemfehler sicher abgefangen:\nDetail: {detail}",
     "err_unknown_title": "WARNUNG: UNERWARTETER FEHLER ABGEFANGEN",
     "err_unknown_desc": "Fehler wurde abgefangen, Programm läuft weiter:\nDetail: {detail}",
     "err_skipped_notice": "Fehler sicher übersprungen. DocMind ist bereit.",
     "err_retrying_in": "Automatischer Neuversuch in {sec}s (Strg+C zum Überspringen)...",
     "err_budget_warn_title": "TOKEN-BUDGET-WARNUNG",
     "err_budget_warn_desc": "Bisher {used} Tokens verbraucht (Warnschwelle: {limit}).",
     "rec_title": "WIEDERHERSTELLUNGSOPTIONEN",
     "rec_opt_new_key": "Neuen API-Schlüssel eingeben & fortfahren",
     "rec_opt_switch_provider": "KI-Anbieter wechseln",
     "rec_opt_switch_model": "Anderes Modell wählen",
     "rec_opt_retry": "Jetzt erneut versuchen",
     "rec_opt_skip": "Fehler überspringen & zurück zum Chat",
     "rec_choose": "Ihre Wahl [Standard: {default}]: ",
     "help_title": "DOCMIND BEFEHLSÜBERSICHT",
     "help_body": (
       "  /help     Hilfe anzeigen              /setup    Einrichtungsassistent\n"
       "  /api      API-Anbieter/Schlüssel      /model    KI-Modell wechseln\n"
       "  /lang     Sprache ändern              /auto     Vollautomatischer Modus\n"
       "  /smart    Bestätigungsmodus           /tokens   Token-Statistik & Limit\n"
       "  /undo     Letzte Änderung zurück      /tree     Verzeichnisbaum\n"
       "  /cd       Verzeichnis wechseln        /doctor   Systemdiagnose\n"
       "  /save     Sitzung speichern           /load     Sitzung laden\n"
       "  /clear    Verlauf löschen             /exit     Beenden"
     ),
     "cmd_cleared": "Gesprächsverlauf und Bildschirm geleert.",
     "cmd_saved": "Sitzung gespeichert: {path}",
     "cmd_loaded": "Sitzung geladen ({count} Nachrichten): {path}",
     "cmd_lang_changed": "Sprache geändert: {lang}",
     "cmd_mode_changed": "Modus aktualisiert: {mode}",
     "cmd_cd_ok": "Arbeitsverzeichnis geändert: {path}",
     "cmd_cd_err": "WARNUNG: Verzeichniswechsel fehlgeschlagen: {err}",
     "cmd_unknown": "Unbekannter Befehl: '{cmd}'. /help für Hilfe.",
     "cmd_exit_bye": "DocMind wird beendet. Auf Wiedersehen!",
     "ctrl_c_cancelled": "Vorgang abgebrochen (Strg+C). Bereit für neue Eingaben.",
     "ctrl_c_exit_hint": "Tippen Sie /exit oder drücken Sie erneut Strg+C zum Beenden.",
     "doctor_title": "DOCMIND SYSTEMDIAGNOSE (/doctor)",
     "tokens_report_title": "TOKEN- & NUTZUNGSBERICHT",
   },
   "es": {
     "lang_name": "Español",
     "ai_lang_instruction": "Comunícate siempre con el usuario en ESPAÑOL claro y natural, salvo que pida otro idioma.",
     "welcome_subtitle": "Agente IA Autónomo de Terminal de Nueva Generación",
     "ready_hint": "¡DocMind está listo! Pide tareas, edita archivos o ejecuta comandos.",
     "type_help_hint": "Escribe /help para comandos | /lang idioma | /api ajustar API | /exit salir.",
     "prompt_placeholder": "Escribe una tarea para DocMind...",
     "wiz_title": "ASISTENTE DE CONFIGURACIÓN DE DOCMIND",
     "wiz_select_lang": "Seleccione su idioma preferido (1-6) [Por defecto: 1]: ",
     "wiz_lang_saved": "Idioma configurado: Español (ES)",
     "wiz_select_provider": "Seleccione el Proveedor de API de IA",
     "wiz_provider_prompt": "Su elección (1-7) [Por defecto: 1]: ",
     "wiz_select_model": "Seleccione Modelo para {provider}",
     "wiz_custom_model_opt": "Ingresar nombre de modelo personalizado...",
     "wiz_model_prompt": "Elección de modelo [Por defecto: 1]: ",
     "wiz_custom_model_prompt": "Escriba el ID exacto del modelo: ",
     "wiz_enter_base_url": "Ingrese Base URL de la API [Por defecto: {default}]: ",
     "wiz_enter_api_key": "Ingrese su clave API de {provider}: ",
     "wiz_api_key_optional": "Clave API de {provider} (opcional si es servidor local): ",
     "wiz_api_key_empty": "¡ADVERTENCIA: La clave API no puede estar vacía!",
     "wiz_testing_api": "Verificando conexión y clave API...",
     "wiz_api_ok": "¡Excelente! Conexión con {provider} ({model}) verificada.",
     "wiz_api_fail_menu": "Hubo un problema al verificar la API. ¿Qué desea hacer?",
     "wiz_opt_retry_key": "Ingresar nueva clave API",
     "wiz_opt_change_provider": "Elegir otro proveedor / modelo",
     "wiz_opt_skip_anyway": "Omitir advertencia y guardar de todos modos (cambie luego con /api)",
     "wiz_select_mode": "Seleccione Modo de Ejecución y Seguridad",
     "wiz_mode_smart": "Confirmación Inteligente (Recomendado - Pregunta antes de editar/ejecutar)",
     "wiz_mode_auto": "Modo Automático Total (Ejecuta todo sin pedir confirmación)",
     "wiz_mode_prompt": "Elección de modo (1-2) [Por defecto: 1]: ",
     "wiz_complete": "¡Configuración completada! Guardado en ~/.docmind-single/config.json.",
     "mode_smart_short": "CONFIRMACIÓN",
     "mode_auto_short": "AUTO TOTAL",
     "status_tokens": "Tokens: {total} (Ent:{inp} / Sal:{out})",
     "status_no_key": "SIN API KEY (use /api)",
     "thinking": "DocMind está pensando y analizando...",
     "step_counter": "Paso Autónomo {step}/{max_steps}",
     "max_steps_reached": "ADVERTENCIA: Se alcanzó el límite de pasos autónomos ({max_steps}).",
     "ask_continue_steps": "¿Desea que DocMind continúe trabajando? [S/n]: ",
     "compacting_context": "INFO: Compactando historial automáticamente para ahorrar tokens...",
     "context_compacted": "Historial compactado con éxito; continuando.",
     "output_truncated_warn": "ADVERTENCIA: La respuesta alcanzó el límite de tokens de salida. Escriba 'continuar'.",
     "tool_running": "Ejecutando herramienta: {name}",
     "tool_done": "Completado: {name}",
     "tool_skipped": "Omitido por el usuario: {name}",
     "tool_error_passed": "ADVERTENCIA: Error en '{name}' omitido sin fallar ({err}).",
     "perm_title": "CONFIRMACIÓN REQUERIDA",
     "perm_file_action": "Operación de archivo: {action} -> {target}",
     "perm_command_warn": "Comando de terminal a ejecutar: {cmd}",
     "perm_dangerous_warn": "¡ATENCIÓN! ¡COMANDO CRÍTICO O RIESGOSO DETECTADO!",
     "perm_prompt": "[S]í ejecutar | [A]uto modo | [N]o omitir [Por defecto: S]: ",
     "perm_dangerous_prompt": "¿Seguro que desea ejecutar este comando crítico? [yes/no]: ",
     "perm_switched_auto": "¡Modo Automático activado! Escriba /smart para volver a confirmar.",
     "undo_success": "Último cambio de archivo revertido: {path}",
     "undo_empty": "No hay cambios de archivo para deshacer.",
     "err_quota_title": "¡ALERTA CRÍTICA: TOKENS / CRÉDITO DE API AGOTADOS!",
     "err_quota_desc": "Su saldo de créditos o cuota de tokens en {provider} se ha agotado.\nDetalle: {detail}",
     "err_rate_title": "¡ADVERTENCIA: LÍMITE DE VELOCIDAD DE API (RATE LIMIT)!",
     "err_rate_desc": "Demasiadas solicitudes por minuto en {provider}.\nDetalle: {detail}",
     "err_auth_title": "¡ADVERTENCIA: CLAVE API INVÁLIDA O CADUCADA!",
     "err_auth_desc": "Su clave API de {provider} fue rechazada.\nDetalle: {detail}",
     "err_context_title": "¡ADVERTENCIA: LÍMITE DE TOKENS DE CONTEXTO SUPERADO!",
     "err_context_desc": "Compactando historial automáticamente para continuar.\nDetalle: {detail}",
     "err_model_title": "¡ADVERTENCIA: MODELO NO ENCONTRADO O SIN ACCESO!",
     "err_model_desc": "El modelo ({model}) no está disponible.\nDetalle: {detail}",
     "err_server_title": "¡ADVERTENCIA: SERVIDOR IA SOBRECARGADO / ERROR TEMPORAL!",
     "err_server_desc": "Problema temporal en los servidores de {provider}.\nDetalle: {detail}",
     "err_network_title": "¡ADVERTENCIA: PROBLEMA DE CONEXIÓN A INTERNET!",
     "err_network_desc": "No se pudo conectar con {provider}. Verifique su red.\nDetalle: {detail}",
     "err_tool_title": "ADVERTENCIA: ERROR DE SISTEMA/ARCHIVO (OMITIDO)",
     "err_tool_desc": "Se detectó un error pero el programa sigue activo:\nDetalle: {detail}",
     "err_unknown_title": "ADVERTENCIA: ERROR INESPERADO CAPTURADO Y OMITIDO",
     "err_unknown_desc": "El problema fue gestionado de forma segura:\nDetalle: {detail}",
     "err_skipped_notice": "Problema omitido con seguridad. DocMind sigue listo.",
     "err_retrying_in": "Reintentando automáticamente en {sec}s (Ctrl+C para omitir)...",
     "err_budget_warn_title": "AVISO DE CONSUMO DE TOKENS",
     "err_budget_warn_desc": "Se han usado {used} tokens en esta sesión (Límite de aviso: {limit}).",
     "rec_title": "OPCIONES DE RECUPERACIÓN",
     "rec_opt_new_key": "Ingresar nueva clave API y continuar",
     "rec_opt_switch_provider": "Cambiar de proveedor de IA",
     "rec_opt_switch_model": "Seleccionar otro modelo",
     "rec_opt_retry": "Reintentar ahora",
     "rec_opt_skip": "Omitir error y volver al chat",
     "rec_choose": "Su opción [Por defecto: {default}]: ",
     "help_title": "GUÍA DE COMANDOS DE DOCMIND",
     "help_body": (
       "  /help     Mostrar ayuda               /setup    Asistente inicial\n"
       "  /api      Cambiar proveedor/API key   /model    Cambiar modelo IA\n"
       "  /lang     Cambiar idioma              /auto     Modo Automático\n"
       "  /smart    Modo Confirmación           /tokens   Uso y límite de tokens\n"
       "  /undo     Deshacer edición            /tree     Árbol de carpetas\n"
       "  /cd       Cambiar directorio          /doctor   Diagnóstico del sistema\n"
       "  /save     Guardar sesión              /load     Cargar sesión\n"
       "  /clear    Limpiar historial           /exit     Salir"
     ),
     "cmd_cleared": "Historial y pantalla limpiados.",
     "cmd_saved": "Sesión guardada: {path}",
     "cmd_loaded": "Sesión cargada ({count} mensajes): {path}",
     "cmd_lang_changed": "Idioma cambiado a: {lang}",
     "cmd_mode_changed": "Modo actualizado: {mode}",
     "cmd_cd_ok": "Directorio cambiado a: {path}",
     "cmd_cd_err": "ADVERTENCIA: No se pudo cambiar el directorio: {err}",
     "cmd_unknown": "Comando desconocido: '{cmd}'. Escriba /help.",
     "cmd_exit_bye": "Cerrando DocMind. ¡Hasta pronto!",
     "ctrl_c_cancelled": "Operación cancelada (Ctrl+C). Listo para continuar.",
     "ctrl_c_exit_hint": "Escriba /exit o pulse Ctrl+C de nuevo para salir.",
     "doctor_title": "DIAGNÓSTICO DE SALUD DE DOCMIND (/doctor)",
     "tokens_report_title": "INFORME DE TOKENS DE LA SESIÓN",
   },
   "fr": {
     "lang_name": "Français",
     "ai_lang_instruction": "Communique toujours avec l'utilisateur en FRANÇAIS clair et naturel, sauf demande contraire.",
     "welcome_subtitle": "Agent IA Autonome de Terminal Nouvelle Génération",
     "ready_hint": "DocMind est prêt ! Demandez une tâche, modifiez des fichiers ou lancez des commandes.",
     "type_help_hint": "Tapez /help pour l'aide | /lang langue | /api clé API | /exit quitter.",
     "prompt_placeholder": "Confiez une tâche à DocMind...",
     "wiz_title": "ASSISTANT DE CONFIGURATION DOCMIND",
     "wiz_select_lang": "Veuillez choisir votre langue (1-6) [Défaut : 1] : ",
     "wiz_lang_saved": "Langue sélectionnée : Français (FR)",
     "wiz_select_provider": "Choisissez le fournisseur d'API IA",
     "wiz_provider_prompt": "Votre choix (1-7) [Défaut : 1] : ",
     "wiz_select_model": "Choisissez le modèle pour {provider}",
     "wiz_custom_model_opt": "Saisir un nom de modèle personnalisé...",
     "wiz_model_prompt": "Choix du modèle [Défaut : 1] : ",
     "wiz_custom_model_prompt": "Entrez l'identifiant exact du modèle : ",
     "wiz_enter_base_url": "Entrez l'URL de base de l'API [Défaut : {default}] : ",
     "wiz_enter_api_key": "Entrez votre clé API {provider} : ",
     "wiz_api_key_optional": "Clé API {provider} (optionnel pour serveur local) : ",
     "wiz_api_key_empty": "AVERTISSEMENT : La clé API ne peut pas être vide !",
     "wiz_testing_api": "Vérification de la connexion et de la clé API...",
     "wiz_api_ok": "Parfait ! Connexion à {provider} ({model}) vérifiée.",
     "wiz_api_fail_menu": "Un problème est survenu lors de la vérification. Que voulez-vous faire ?",
     "wiz_opt_retry_key": "Saisir une nouvelle clé API",
     "wiz_opt_change_provider": "Choisir un autre fournisseur / modèle",
     "wiz_opt_skip_anyway": "Ignorer l'alerte et enregistrer quand même (/api plus tard)",
     "wiz_select_mode": "Choisissez le mode d'exécution et de sécurité",
     "wiz_mode_smart": "Confirmation Intelligente (Recommandé - Demande avant modifications/commandes)",
     "wiz_mode_auto": "Mode Automatique Complet (Exécute tout immédiatement sans confirmation)",
     "wiz_mode_prompt": "Choix du mode (1-2) [Défaut : 1] : ",
     "wiz_complete": "Configuration terminée ! Enregistré dans ~/.docmind-single/config.json.",
     "mode_smart_short": "CONFIRMATION",
     "mode_auto_short": "AUTO COMPLET",
     "status_tokens": "Tokens : {total} (Ent:{inp} / Sor:{out})",
     "status_no_key": "SANS CLÉ API (/api)",
     "thinking": "DocMind réfléchit et analyse...",
     "step_counter": "Étape autonome {step}/{max_steps}",
     "max_steps_reached": "AVERTISSEMENT : Limite d'étapes autonomes ({max_steps}) atteinte.",
     "ask_continue_steps": "DocMind doit-il continuer ? [O/n] : ",
     "compacting_context": "INFO : Compression intelligente de l'historique pour économiser les tokens...",
     "context_compacted": "Historique compressé avec succès ; reprise en cours.",
     "output_truncated_warn": "AVERTISSEMENT : Limite de tokens de sortie atteinte. Tapez 'continuer' pour poursuivre.",
     "tool_running": "Exécution de l'outil : {name}",
     "tool_done": "Terminé : {name}",
     "tool_skipped": "Ignoré par l'utilisateur : {name}",
     "tool_error_passed": "AVERTISSEMENT : Erreur dans '{name}' ignorée sans plantage ({err}).",
     "perm_title": "CONFIRMATION REQUISE",
     "perm_file_action": "Action fichier : {action} -> {target}",
     "perm_command_warn": "Commande terminal à exécuter : {cmd}",
     "perm_dangerous_warn": "ATTENTION ! COMMANDE CRITIQUE OU RISQUÉE DÉTECTÉE !",
     "perm_prompt": "[O]ui exécuter | Mode [A]uto | [N]on ignorer [Défaut : O] : ",
     "perm_dangerous_prompt": "Voulez-vous vraiment exécuter cette commande critique ? [yes/no] : ",
     "perm_switched_auto": "Mode Automatique activé ! Tapez /smart pour réactiver les confirmations.",
     "undo_success": "Dernière modification annulée : {path}",
     "undo_empty": "Aucune modification de fichier à annuler.",
     "err_quota_title": "ALERTE CRITIQUE : QUOTA DE TOKENS / CRÉDIT API ÉPUISÉ !",
     "err_quota_desc": "Votre quota ou solde de crédits sur {provider} est épuisé.\nDétail : {detail}",
     "err_rate_title": "AVERTISSEMENT : LIMITE DE REQUÊTES API (RATE LIMIT) !",
     "err_rate_desc": "Trop de requêtes envoyées à {provider}.\nDétail : {detail}",
     "err_auth_title": "AVERTISSEMENT : CLÉ API INVALIDE OU EXPIRÉE !",
     "err_auth_desc": "Votre clé API {provider} a été refusée.\nDétail : {detail}",
     "err_context_title": "AVERTISSEMENT : LIMITE DE TOKENS DE CONTEXTE DÉPASSÉE !",
     "err_context_desc": "Compression automatique de la conversation en cours.\nDétail : {detail}",
     "err_model_title": "AVERTISSEMENT : MODÈLE INTROUVABLE OU ACCÈS REFUSÉ !",
     "err_model_desc": "Le modèle ({model}) n'est pas disponible.\nDétail : {detail}",
     "err_server_title": "AVERTISSEMENT : SERVEUR IA SURCHARGÉ / ERREUR TEMPORAIRE !",
     "err_server_desc": "Problème temporaire sur les serveurs {provider}.\nDétail : {detail}",
     "err_network_title": "AVERTISSEMENT : PROBLÈME DE CONNEXION RÉSEAU / INTERNET !",
     "err_network_desc": "Impossible de joindre {provider}. Vérifiez votre connexion.\nDétail : {detail}",
     "err_tool_title": "AVERTISSEMENT : ERREUR FICHIER / SYSTÈME (IGNORÉE)",
     "err_tool_desc": "Une erreur système a été interceptée sans arrêt :\nDétail : {detail}",
     "err_unknown_title": "AVERTISSEMENT : ERREUR INATTENDUE INTERCEPTÉE",
     "err_unknown_desc": "Problème géré en toute sécurité :\nDétail : {detail}",
     "err_skipped_notice": "Erreur ignorée en toute sécurité. DocMind reste prêt.",
     "err_retrying_in": "Nouvelle tentative automatique dans {sec}s (Ctrl+C pour passer)...",
     "err_budget_warn_title": "ALERTE BUDGET TOKENS",
     "err_budget_warn_desc": "{used} tokens utilisés durant cette session (Seuil : {limit}).",
     "rec_title": "OPTIONS DE RÉCUPÉRATION",
     "rec_opt_new_key": "Entrer une nouvelle clé API et continuer",
     "rec_opt_switch_provider": "Changer de fournisseur IA",
     "rec_opt_switch_model": "Choisir un autre modèle",
     "rec_opt_retry": "Réessayer maintenant",
     "rec_opt_skip": "Ignorer l'erreur et revenir au chat",
     "rec_choose": "Votre choix [Défaut : {default}] : ",
     "help_title": "GUIDE DES COMMANDES DOCMIND",
     "help_body": (
       "  /help     Afficher l'aide             /setup    Assistant initial\n"
       "  /api      Changer fournisseur/clé     /model    Changer de modèle\n"
       "  /lang     Changer la langue           /auto     Mode Automatique\n"
       "  /smart    Mode Confirmation           /tokens   Statistiques tokens\n"
       "  /undo     Annuler modification        /tree     Arborescence dossier\n"
       "  /cd       Changer de dossier          /doctor   Diagnostic système\n"
       "  /save     Sauvegarder session         /load     Charger session\n"
       "  /clear    Effacer historique          /exit     Quitter"
     ),
     "cmd_cleared": "Historique et écran effacés.",
     "cmd_saved": "Session sauvegardée : {path}",
     "cmd_loaded": "Session chargée ({count} messages) : {path}",
     "cmd_lang_changed": "Langue modifiée : {lang}",
     "cmd_mode_changed": "Mode mis à jour : {mode}",
     "cmd_cd_ok": "Répertoire courant changé : {path}",
     "cmd_cd_err": "AVERTISSEMENT : Impossible de changer de dossier : {err}",
     "cmd_unknown": "Commande inconnue : '{cmd}'. Tapez /help.",
     "cmd_exit_bye": "Fermeture de DocMind. À bientôt !",
     "ctrl_c_cancelled": "Opération annulée (Ctrl+C). Prêt à continuer.",
     "ctrl_c_exit_hint": "Tapez /exit ou appuyez encore sur Ctrl+C pour quitter.",
     "doctor_title": "DIAGNOSTIC SYSTÈME DOCMIND (/doctor)",
     "tokens_report_title": "RAPPORT DE CONSOMMATION DE TOKENS",
   },
   "ru": {
     "lang_name": "Русский",
     "ai_lang_instruction": "Всегда общайся с пользователем на понятном и естественном РУССКОМ языке, если не указано иное.",
     "welcome_subtitle": "Автономный терминальный ИИ-агент нового поколения",
     "ready_hint": "DocMind готов! Ставьте задачи, редактируйте файлы или выполняйте команды.",
     "type_help_hint": "Введите /help для команд | /lang язык | /api ключ API | /exit выход.",
     "prompt_placeholder": "Введите задачу для DocMind...",
     "wiz_title": "МАСТЕР НАСТРОЙКИ DOCMIND",
     "wiz_select_lang": "Выберите язык интерфейса (1-6) [По умолчанию: 1]: ",
     "wiz_lang_saved": "Язык установлен: Русский (RU)",
     "wiz_select_provider": "Выберите провайдера ИИ API",
     "wiz_provider_prompt": "Ваш выбор (1-7) [По умолчанию: 1]: ",
     "wiz_select_model": "Выберите модель для {provider}",
     "wiz_custom_model_opt": "Ввести своё имя модели...",
     "wiz_model_prompt": "Выбор модели [По умолчанию: 1]: ",
     "wiz_custom_model_prompt": "Введите точный ID модели: ",
     "wiz_enter_base_url": "Введите Base URL API [По умолчанию: {default}]: ",
     "wiz_enter_api_key": "Введите ваш API-ключ {provider}: ",
     "wiz_api_key_optional": "API-ключ {provider} (можно пропустить для локального сервера): ",
     "wiz_api_key_empty": "ВНИМАНИЕ: API-ключ не может быть пустым!",
     "wiz_testing_api": "Проверка соединения и API-ключа...",
     "wiz_api_ok": "Отлично! Подключение к {provider} ({model}) успешно проверено.",
     "wiz_api_fail_menu": "Возникла проблема при проверке API. Что вы хотите сделать?",
     "wiz_opt_retry_key": "Ввести новый API-ключ",
     "wiz_opt_change_provider": "Выбрать другого провайдера / модель",
     "wiz_opt_skip_anyway": "Пропустить предупреждение и сохранить (позже /api)",
     "wiz_select_mode": "Выберите режим безопасности и работы",
     "wiz_mode_smart": "Умное подтверждение (Рекомендуется - спрашивает перед правкой/командами)",
     "wiz_mode_auto": "Полный автомат (Выполняет все действия без запросов)",
     "wiz_mode_prompt": "Выбор режима (1-2) [По умолчанию: 1]: ",
     "wiz_complete": "Настройка завершена! Конфигурация сохранена в ~/.docmind-single/config.json.",
     "mode_smart_short": "ПОДТВЕРЖДЕНИЕ",
     "mode_auto_short": "АВТОМАТ",
     "status_tokens": "Токены: {total} (Вх:{inp} / Вых:{out})",
     "status_no_key": "НЕТ API-КЛЮЧА (/api)",
     "thinking": "DocMind думает и анализирует...",
     "step_counter": "Автономный шаг {step}/{max_steps}",
     "max_steps_reached": "ВНИМАНИЕ: Достигнут лимит автономных шагов ({max_steps}).",
     "ask_continue_steps": "Продолжить выполнение задачи? [Y/n]: ",
     "compacting_context": "ИНФО: Автоматическое сжатие истории для экономии токенов...",
     "context_compacted": "История успешно сжата, продолжаем работу.",
     "output_truncated_warn": "ВНИМАНИЕ: Достигнут лимит выходных токенов ответа. Напишите 'продолжай'.",
     "tool_running": "Запуск инструмента: {name}",
     "tool_done": "Готово: {name}",
     "tool_skipped": "Пропущено пользователем: {name}",
     "tool_error_passed": "ВНИМАНИЕ: Ошибка в '{name}' безопасно пропущена ({err}).",
     "perm_title": "ТРЕБУЕТСЯ ПОДТВЕРЖДЕНИЕ",
     "perm_file_action": "Действие с файлом: {action} -> {target}",
     "perm_command_warn": "Выполнение команды: {cmd}",
     "perm_dangerous_warn": "ОСТОРОЖНО! ОБНАРУЖЕНА ОПАСНАЯ КОМАНДА!",
     "perm_prompt": "[Y] Выполнить | [A]вто-режим | [N] Пропустить [По умолчанию: Y]: ",
     "perm_dangerous_prompt": "Вы уверены, что хотите выполнить эту критическую команду? [yes/no]: ",
     "perm_switched_auto": "Включён полный автоматический режим! (/smart для возврата)",
     "undo_success": "Последнее изменение файла отменено: {path}",
     "undo_empty": "Нет изменений файлов для отмены.",
     "err_quota_title": "КРИТИЧЕСКОЕ ПРЕДУПРЕЖДЕНИЕ: ЗАКОНЧИЛИСЬ ТОКЕНЫ / БАЛАНС API!",
     "err_quota_desc": "Лимит токенов или баланс кредитов {provider} исчерпан.\nДетали: {detail}",
     "err_rate_title": "ВНИМАНИЕ: ПРЕВЫШЕН ЛИМИТ ЗАПРОСОВ API (RATE LIMIT)!",
     "err_rate_desc": "Слишком частые запросы к {provider}.\nДетали: {detail}",
     "err_auth_title": "ВНИМАНИЕ: НЕВЕРНЫЙ ИЛИ ПРОСРОЧЕННЫЙ API-КЛЮЧ!",
     "err_auth_desc": "Ваш API-ключ {provider} отклонён.\nДетали: {detail}",
     "err_context_title": "ВНИМАНИЕ: ПРЕВЫШЕН ЛИМИТ КОНТЕКСТА (ТОКЕНОВ)!",
     "err_context_desc": "Выполняется автоматическое сжатие диалога.\nДетали: {detail}",
     "err_model_title": "ВНИМАНИЕ: МОДЕЛЬ НЕ НАЙДЕНА ИЛИ НЕТ ДОСТУПА!",
     "err_model_desc": "Модель ({model}) недоступна.\nДетали: {detail}",
     "err_server_title": "ВНИМАНИЕ: СЕРВЕР ИИ ПЕРЕГРУЖЕН / ВРЕМЕННАЯ ОШИБКА!",
     "err_server_desc": "Временный сбой на серверах {provider}.\nДетали: {detail}",
     "err_network_title": "ВНИМАНИЕ: ОШИБКА СЕТИ / НЕТ ИНТЕРНЕТА!",
     "err_network_desc": "Не удалось подключиться к {provider}. Проверьте соединение.\nДетали: {detail}",
     "err_tool_title": "ВНИМАНИЕ: ОШИБКА ФАЙЛА / СИСТЕМЫ (ПРОПУЩЕНА)",
     "err_tool_desc": "Системная ошибка перехвачена без остановки программы:\nДетали: {detail}",
     "err_unknown_title": "ВНИМАНИЕ: НЕПРЕДВИДЕННАЯ ОШИБКА ПЕРЕХВАЧЕНА",
     "err_unknown_desc": "Сбой безопасно обработан, работа продолжается:\nДетали: {detail}",
     "err_skipped_notice": "Ошибка безопасно пропущена. DocMind готов к работе.",
     "err_retrying_in": "Повторная попытка через {sec}с (Ctrl+C чтобы пропустить)...",
     "err_budget_warn_title": "ПРЕДУПРЕЖДЕНИЕ О РАСХОДЕ ТОКЕНОВ",
     "err_budget_warn_desc": "Использовано {used} токенов за сессию (Лимит: {limit}).",
     "rec_title": "ВАРИАНТЫ ВОССТАНОВЛЕНИЯ",
     "rec_opt_new_key": "Ввести новый API-ключ и продолжить",
     "rec_opt_switch_provider": "Сменить провайдера ИИ",
     "rec_opt_switch_model": "Выбрать другую модель",
     "rec_opt_retry": "Повторить попытку сейчас",
     "rec_opt_skip": "Пропустить ошибку и вернуться в чат",
     "rec_choose": "Ваш выбор [По умолчанию: {default}]: ",
     "help_title": "СПРАВОЧНИК КОМАНД DOCMIND",
     "help_body": (
       "  /help     Показать справку            /setup    Мастер настройки\n"
       "  /api      Сменить провайдера/ключ     /model    Сменить модель ИИ\n"
       "  /lang     Сменить язык                /auto     Автоматический режим\n"
       "  /smart    Режим подтверждения         /tokens   Статистика токенов\n"
       "  /undo     Отменить правку файла       /tree     Дерево папок\n"
       "  /cd       Сменить рабочую папку       /doctor   Диагностика системы\n"
       "  /save     Сохранить сессию            /load     Загрузить сессию\n"
       "  /clear    Очистить историю            /exit     Выход"
     ),
     "cmd_cleared": "История диалога и экран очищены.",
     "cmd_saved": "Сессия сохранена: {path}",
     "cmd_loaded": "Сессия загружена ({count} сообщений): {path}",
     "cmd_lang_changed": "Язык изменён: {lang}",
     "cmd_mode_changed": "Режим работы обновлён: {mode}",
     "cmd_cd_ok": "Рабочая папка изменена: {path}",
     "cmd_cd_err": "ВНИМАНИЕ: Не удалось сменить папку: {err}",
     "cmd_unknown": "Неизвестная команда: '{cmd}'. Введите /help.",
     "cmd_exit_bye": "Завершение работы DocMind. До встречи!",
     "ctrl_c_cancelled": "Операция прервана пользователем (Ctrl+C). Готов к работе.",
     "ctrl_c_exit_hint": "Введите /exit или нажмите Ctrl+C ещё раз для выхода.",
     "doctor_title": "ДИАГНОСТИКА СИСТЕМЫ DOCMIND (/doctor)",
     "tokens_report_title": "ОТЧЁТ ПО ИСПОЛЬЗОВАНИЮ ТОКЕНОВ",
   },
 }
 _SAFETY_WORDING = {
   "tr": {
     "wiz_secret_notice": "Anahtar yazarken ekranda GÖRÜNÜR; ekranınızı kimseye göstermeyin. Kaydedilirse ~/.docmind-single/config.json içinde ŞİFRELENMEDEN tutulur. Boş Enter mevcut anahtarı korur.",
     "wiz_complete": "Kurulum tamamlandı. API anahtarı şifrelenmeden yerel ayarlarda saklanır.",
     "wiz_mode_smart": "Akıllı Onay (önerilen): değişiklik, komut ve web isteği için onay ister",
     "wiz_mode_auto": "Tam Otomatik (riskli): işlemleri onaysız yapabilir; güvenlik garantisi değildir",
     "perm_prompt": "[E]vet | [O]tomatik moda geç | [H]ayır [Varsayılan: Hayır]: ",
     "perm_sensitive_warning": "HASSAS DOSYA: İçerik şifre veya anahtar içerebilir ve AI sağlayıcısına gönderilebilir. Yalnızca kesinlikle istiyorsanız tam olarak 'evet' yazın.",
     "perm_sensitive_prompt": "Bu hassas işlemi onaylıyor musunuz? [evet/hayır]: ",
   },
   "en": {
     "wiz_secret_notice": "The key is VISIBLE as you type; do not share your screen. If saved, it is stored UNENCRYPTED in ~/.docmind-single/config.json. Enter keeps the current key.",
     "wiz_complete": "Setup complete. API keys are stored unencrypted in local settings.",
     "wiz_mode_smart": "Smart Confirm (recommended): ask before changes, commands and web requests",
     "wiz_mode_auto": "Full Auto (risky): can perform actions without asking; not a security sandbox",
     "perm_prompt": "[Y]es | [A]uto mode | [N]o [Default: No]: ",
     "perm_sensitive_warning": "SENSITIVE: Content may contain credentials and may be sent to the AI provider. Type the full word 'yes' only if you intend this.",
     "perm_sensitive_prompt": "Approve this sensitive action? [yes/no]: ",
   },
   "de": {
     "wiz_secret_notice": "Der Schlüssel ist bei der Eingabe SICHTBAR; zeigen Sie Ihren Bildschirm nicht. Er wird UNVERSCHLÜSSELT in ~/.docmind-single/config.json gespeichert. Enter behält den bisherigen Schlüssel.",
     "wiz_complete": "Einrichtung abgeschlossen. API-Schlüssel werden unverschlüsselt lokal gespeichert.",
     "wiz_mode_smart": "Intelligente Bestätigung (empfohlen): fragt vor Änderungen, Befehlen und Webanfragen",
     "wiz_mode_auto": "Automatisch (riskant): Aktionen ohne Rückfrage; keine Sicherheits-Sandbox",
     "perm_prompt": "[J]a | [A]utomatisch | [N]ein [Standard: Nein]: ",
     "perm_sensitive_warning": "SENSIBEL: Der Inhalt kann Zugangsdaten enthalten und an den KI-Anbieter gesendet werden. Zur Bestätigung 'ja' eingeben.",
     "perm_sensitive_prompt": "Diesen sensiblen Vorgang erlauben? [ja/nein]: ",
   },
   "es": {
     "wiz_secret_notice": "La clave es VISIBLE al escribirla; no compartas la pantalla. Se guarda SIN CIFRAR en ~/.docmind-single/config.json. Enter conserva la clave actual.",
     "wiz_complete": "Configuración completada. Las claves se guardan localmente sin cifrar.",
     "wiz_mode_smart": "Confirmación inteligente (recomendada): pregunta antes de cambios, comandos y web",
     "wiz_mode_auto": "Automático (arriesgado): actúa sin preguntar; no es una sandbox",
     "perm_prompt": "[S]í | [A]utomático | [N]o [Predeterminado: No]: ",
     "perm_sensitive_warning": "SENSIBLE: El contenido puede contener credenciales y enviarse al proveedor de IA. Escriba 'sí' para confirmar.",
     "perm_sensitive_prompt": "¿Permitir esta acción sensible? [sí/no]: ",
   },
   "fr": {
     "wiz_secret_notice": "La clé est VISIBLE pendant la saisie ; ne partagez pas votre écran. Elle est stockée SANS CHIFFREMENT dans ~/.docmind-single/config.json. Entrée conserve la clé actuelle.",
     "wiz_complete": "Configuration terminée. Les clés sont stockées localement sans chiffrement.",
     "wiz_mode_smart": "Confirmation intelligente (recommandée) : demander avant modification, commande et web",
     "wiz_mode_auto": "Automatique (risqué) : agit sans demander ; ce n'est pas un bac à sable",
     "perm_prompt": "[O]ui | [A]uto | [N]on [Défaut : Non] : ",
     "perm_sensitive_warning": "SENSIBLE : Le contenu peut contenir des identifiants et être envoyé au fournisseur IA. Tapez 'oui' pour confirmer.",
     "perm_sensitive_prompt": "Autoriser cette action sensible ? [oui/non] : ",
   },
   "ru": {
     "wiz_secret_notice": "Ключ ВИДЕН при вводе; не показывайте экран. Он хранится БЕЗ ШИФРОВАНИЯ в ~/.docmind-single/config.json. Enter сохраняет текущий ключ.",
     "wiz_complete": "Настройка завершена. API-ключи хранятся локально без шифрования.",
     "wiz_mode_smart": "Умное подтверждение (рекомендуется): спрашивать перед изменениями, командами и веб-запросами",
     "wiz_mode_auto": "Автоматический (опасно): действия без подтверждения; это не песочница",
     "perm_prompt": "[Y] Да | [A] Авто | [N] Нет [По умолчанию: Нет]: ",
     "perm_sensitive_warning": "КОНФИДЕНЦИАЛЬНО: содержимое может включать ключи и отправляться провайдеру ИИ. Для подтверждения введите 'да'.",
     "perm_sensitive_prompt": "Разрешить это конфиденциальное действие? [да/нет]: ",
   },
 }
 for _language, _wording in _SAFETY_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _SIMPLE_HELP = {
   "tr": " /api       Sağlayıcı veya anahtar\n /model     Model değiştir\n /cd YOL    Çalışma klasörü\n /undo      Son dosya değişikliğini geri al\n /clear     Yeni sohbet\n /auto      Otomatik mod (riskli)\n /smart     Onaylı mod\n /reset     Ayarları sıfırla (.json sil) ve kapat\n /exit      Çıkış",
   "en": " /api       Provider or key\n /model     Change model\n /cd PATH   Working folder\n /undo      Undo last file change\n /clear     New chat\n /auto      Automatic mode (risky)\n /smart     Approval mode\n /reset     Reset config (.json) & close terminal\n /exit      Exit",
   "de": " /api       Anbieter oder Schlüssel\n /model     Modell ändern\n /cd PFAD   Arbeitsordner\n /undo      Letzte Dateiänderung rückgängig\n /clear     Neuer Chat\n /auto      Automatik (riskant)\n /smart     Bestätigung\n /reset     Konfiguration löschen & schließen\n /exit      Beenden",
   "es": " /api       Proveedor o clave\n /model     Cambiar modelo\n /cd RUTA   Carpeta de trabajo\n /undo      Deshacer último cambio\n /clear     Nuevo chat\n /auto      Modo automático (riesgo)\n /smart     Confirmación\n /reset     Restablecer config (.json) y cerrar\n /exit      Salir",
   "fr": " /api       Fournisseur ou clé\n /model     Changer de modèle\n /cd CHEMIN Dossier de travail\n /undo      Annuler dernière modification\n /clear     Nouvelle discussion\n /auto      Mode automatique (risqué)\n /smart     Confirmation\n /reset     Réinitialiser config (.json) et fermer\n /exit      Quitter",
   "ru": " /api       Провайдер или ключ\n /model     Изменить модель\n /cd ПУТЬ   Рабочая папка\n /undo      Отменить изменение файла\n /clear     Новый чат\n /auto      Автоматический режим (риск)\n /smart     Подтверждение\n /reset     Сбросить настройки (.json) и закрыть\n /exit      Выход",
 }
 for _language, _help in _SIMPLE_HELP.items():
   TRANSLATIONS[_language]["help_body"] = _help
 TRANSLATIONS["tr"]["welcome_subtitle"] = "Dosyaların ve kodların için yapay zekâ asistanı"
 TRANSLATIONS["en"]["welcome_subtitle"] = "Your assistant for files and code"
 _TERMINAL_TEXT = {
  'tr': {
   'footer_token':'Token','footer_context':'Bağlam','footer_cost':'Maliyet',
   'retry_wait':'Bağlantı veya sunucu sorunu. {seconds} sn sonra tekrar deneniyor (deneme {attempt}). Terminali kapatma; Ctrl+C bu görevi iptal eder.',
   'retry_partial':'Yanıt yarım kaldı; tamamlanmamış araç çağrısı çalıştırılmadı. Tekrar edilen istek ek ücret oluşturabilir.',
   'retry_ok':'Bağlantı düzeldi; görev devam ediyor.',
   'price_usage':'Fiyat: /fiyat GİRİŞ ÇIKIŞ (1 milyon token başına USD); /fiyat auto varsayılana döner.',
   'price_set':'Bu sağlayıcı/model için fiyat kaydedildi: giriş ${inp}, çıkış ${out} / 1 milyon token.',
   'price_reset':'Özel fiyat kaldırıldı.',
   'price_unknown':'Fiyat bilinmiyor; sağlayıcının tarifesini /fiyat ile gir.',
   'price_invalid':'Geçerli, sıfır veya pozitif iki sayı gir: /fiyat 0.15 0.60',
   'context_usage':'Bağlam limiti: /context SAYI; /context auto varsayılana döner.',
   'context_invalid':'Bağlam limiti 1.024 ile 100.000.000 arasında olmalı.',
   'context_set':'Bağlam limiti kaydedildi: {limit}.',
   'context_reset':'Özel bağlam limiti kaldırıldı.',
  },
  'en': {
   'footer_token':'Tokens','footer_context':'Context','footer_cost':'Cost',
   'retry_wait':'Network or server problem. Retrying in {seconds}s (attempt {attempt}). Keep the terminal open; Ctrl+C cancels this task.',
   'retry_partial':'The answer was interrupted; incomplete tool calls were not executed. A retry may incur additional charges.',
   'retry_ok':'Connection restored; continuing the task.',
   'price_usage':'Pricing: /price INPUT OUTPUT (USD per million tokens); /price auto resets.',
   'price_set':'Price saved for this provider/model: input ${inp}, output ${out} per million.',
   'price_reset':'Custom pricing removed.',
   'price_unknown':'Price unknown; enter the provider rate with /price.',
   'price_invalid':'Enter two non-negative numbers: /price 0.15 0.60',
   'context_usage':'Context limit: /context NUMBER; /context auto resets.',
   'context_invalid':'Context limit must be from 1,024 to 100,000,000.',
   'context_set':'Context limit saved: {limit}.',
   'context_reset':'Custom context limit removed.',
  },
  'de': {'footer_token':'Token','footer_context':'Kontext','footer_cost':'Kosten','retry_wait':'Netzwerk- oder Serverproblem. Neuer Versuch in {seconds}s (Versuch {attempt}). Terminal offen lassen; Strg+C bricht ab.','retry_partial':'Antwort unterbrochen; unvollständige Werkzeugaufrufe wurden nicht ausgeführt. Weitere Kosten möglich.','retry_ok':'Verbindung wiederhergestellt; Aufgabe wird fortgesetzt.','price_usage':'Preis: /price EINGABE AUSGABE (USD pro Mio. Token); /price auto setzt zurück.','price_set':'Preis gespeichert: Eingabe ${inp}, Ausgabe ${out} / Mio.','price_reset':'Eigener Preis entfernt.','price_unknown':'Preis unbekannt; mit /price setzen.','price_invalid':'Zwei nichtnegative Zahlen eingeben: /price 0.15 0.60','context_usage':'Kontextlimit: /context ZAHL; /context auto setzt zurück.','context_invalid':'Limit muss zwischen 1024 und 100000000 liegen.','context_set':'Kontextlimit gespeichert: {limit}.','context_reset':'Eigenes Kontextlimit entfernt.'},
  'es': {'footer_token':'Tokens','footer_context':'Contexto','footer_cost':'Coste','retry_wait':'Problema de red o servidor. Reintento en {seconds}s (intento {attempt}). No cierres la terminal; Ctrl+C cancela.','retry_partial':'Respuesta interrumpida; no se ejecutaron llamadas incompletas. El reintento puede generar cargos.','retry_ok':'Conexión restaurada; continuando.','price_usage':'Precio: /price ENTRADA SALIDA (USD por millón); /price auto restablece.','price_set':'Precio guardado: entrada ${inp}, salida ${out} por millón.','price_reset':'Precio personalizado eliminado.','price_unknown':'Precio desconocido; usa /price.','price_invalid':'Introduce dos números no negativos: /price 0.15 0.60','context_usage':'Límite: /context NÚMERO; /context auto restablece.','context_invalid':'El límite debe estar entre 1024 y 100000000.','context_set':'Límite guardado: {limit}.','context_reset':'Límite personalizado eliminado.'},
  'fr': {'footer_token':'Jetons','footer_context':'Contexte','footer_cost':'Coût','retry_wait':'Problème réseau ou serveur. Nouvelle tentative dans {seconds}s (essai {attempt}). Gardez le terminal ouvert ; Ctrl+C annule.','retry_partial':'Réponse interrompue ; aucun appel incomplet exécuté. Une nouvelle tentative peut être facturée.','retry_ok':'Connexion rétablie ; tâche reprise.','price_usage':'Prix : /price ENTRÉE SORTIE (USD par million) ; /price auto réinitialise.','price_set':'Prix enregistré : entrée ${inp}, sortie ${out} par million.','price_reset':'Prix personnalisé supprimé.','price_unknown':'Prix inconnu ; utilisez /price.','price_invalid':'Entrez deux nombres positifs ou nuls : /price 0.15 0.60','context_usage':'Limite : /context NOMBRE ; /context auto réinitialise.','context_invalid':'La limite doit être entre 1024 et 100000000.','context_set':'Limite enregistrée : {limit}.','context_reset':'Limite personnalisée supprimée.'},
  'ru': {'footer_token':'Токены','footer_context':'Контекст','footer_cost':'Стоимость','retry_wait':'Ошибка сети или сервера. Повтор через {seconds}с (попытка {attempt}). Не закрывайте терминал; Ctrl+C отменяет задачу.','retry_partial':'Ответ прерван; неполные вызовы не выполнены. Повтор может повлечь дополнительные расходы.','retry_ok':'Соединение восстановлено; задача продолжается.','price_usage':'Цена: /price ВХОД ВЫХОД (USD за миллион); /price auto сбрасывает.','price_set':'Цена сохранена: вход ${inp}, выход ${out} за миллион.','price_reset':'Своя цена удалена.','price_unknown':'Цена неизвестна; укажите её через /price.','price_invalid':'Введите два неотрицательных числа: /price 0.15 0.60','context_usage':'Лимит: /context ЧИСЛО; /context auto сбрасывает.','context_invalid':'Лимит должен быть от 1024 до 100000000.','context_set':'Лимит сохранён: {limit}.','context_reset':'Свой лимит удалён.'},
 }
 for _language, _strings in _TERMINAL_TEXT.items():
   TRANSLATIONS[_language].update(_strings)
 for _language in TRANSLATIONS:
   TRANSLATIONS[_language]['help_body'] += '\n /tokens    Token / context / cost\n /price     USD per million tokens\n /context   Context limit'
 TRANSLATIONS['tr']['help_body'] = (_SIMPLE_HELP['tr'] + '\n'
   ' /tokens    Token, bağlam ve tahmini maliyet\n /fiyat     Modelin USD fiyatını ayarla\n /context   Bağlam limitini ayarla')
 _STREAM_FALLBACK = {
   'tr':'Akış birkaç kez yarım kaldı; bu oturumda normal yanıt deneniyor. Metin yine kademeli gösterilecek.',
   'en':'The stream repeatedly ended early; retrying without streaming for this session. Text will still be animated.',
   'de':'Der Stream wurde mehrfach unterbrochen; für diese Sitzung wird ohne Streaming fortgefahren.',
   'es':'El flujo se interrumpió varias veces; se intentará sin streaming en esta sesión.',
   'fr':'Le flux a été interrompu plusieurs fois ; nouvel essai sans streaming pour cette session.',
   'ru':'Поток несколько раз прервался; в этой сессии повторяем запрос без потоковой передачи.',
 }
 for _language,_message in _STREAM_FALLBACK.items():
   TRANSLATIONS[_language]['retry_stream_off'] = _message
 TRANSLATIONS['tr']['settings_save_failed'] = 'Ayar kaydedilemedi; yalnızca bu oturumda geçerli olabilir.'
 TRANSLATIONS['en']['settings_save_failed'] = 'Settings could not be saved and may apply only for this session.'
 TRANSLATIONS['de']['settings_save_failed'] = 'Einstellungen konnten nicht gespeichert werden; sie gelten eventuell nur für diese Sitzung.'
 TRANSLATIONS['es']['settings_save_failed'] = 'No se pudieron guardar los ajustes; quizá solo duren esta sesión.'
 TRANSLATIONS['fr']['settings_save_failed'] = 'Paramètres non enregistrés ; ils peuvent ne durer que pour cette session.'
 TRANSLATIONS['ru']['settings_save_failed'] = 'Настройки не сохранены; возможно, они действуют только в этом сеансе.'
 _STAT_LABELS = {
  'tr': ['Sağlayıcı / Model','API isteği','Giriş token','Çıkış token','Toplam token','Bağlam doluluğu','Anlık durum','Maliyet yaklaşık; önbellek, ücretsiz kota, vergi ve yarım kalan istekler sonucu değiştirebilir. Fiyat tablosu 29.10.2026 tarihli; güncel fatura için sağlayıcına bak.','Uyarı sınırı','Bellekteki mesaj'],
  'en': ['Provider / Model','API calls','Input tokens','Output tokens','Total tokens','Context fill','Live status','Estimated cost only; caching, free tiers, tax and interrupted requests can differ. Built-in rates checked 2026-10-29; check your provider bill.','Warning threshold','Messages in memory'],
  'de': ['Anbieter / Modell','API-Anfragen','Eingabe-Token','Ausgabe-Token','Token gesamt','Kontextbelegung','Live-Status','Nur geschätzte Kosten; Cache, Freikontingent, Steuern und unterbrochene Anfragen können abweichen. Tarife: 29.10.2026.','Warnschwelle','Nachrichten im Speicher'],
  'es': ['Proveedor / modelo','Solicitudes API','Tokens de entrada','Tokens de salida','Tokens totales','Uso del contexto','Estado','Coste estimado; caché, nivel gratuito, impuestos y reintentos pueden cambiarlo. Tarifas del 29-10-2026.','Umbral de aviso','Mensajes en memoria'],
  'fr': ['Fournisseur / modèle','Requêtes API','Jetons en entrée','Jetons en sortie','Total de jetons','Contexte utilisé','État','Coût estimé ; cache, gratuité, taxes et interruptions peuvent différer. Tarifs du 29-10-2026.','Seuil d’alerte','Messages en mémoire'],
  'ru': ['Провайдер / модель','Запросы API','Входные токены','Выходные токены','Всего токенов','Заполнение контекста','Состояние','Примерная стоимость; кэш, бесплатный тариф, налоги и прерванные запросы могут отличаться. Тарифы на 29.10.2026.','Порог предупреждения','Сообщений в памяти'],
 }
 for _language,_labels in _STAT_LABELS.items():
   for _index,_label in enumerate(_labels):
     TRANSLATIONS[_language]['stat_'+str(_index)] = _label
 _HISTORY_TEXT = {
   'tr': {
     'history_title':'Sohbet geçmişi',
     'history_choose':'Açmak istediğin sohbet numarası (Enter: iptal): ',
     'history_empty':'Henüz kayıtlı sohbet yok. İlk mesajından sonra otomatik kaydedilir.',
     'history_invalid':'Geçerli bir sohbet numarası gir.',
     'history_cancel':'Sohbet seçimi iptal edildi.',
     'history_loaded':'Sohbet yüklendi: {title}',
     'history_you':'Sen',
     'history_cancelled':'yanıt alınamadı / iptal edildi',
     'history_read_error':'Sohbet geçmişi okunamadı. Dosyayı ve izinleri kontrol et.',
     'history_write_error':'Sohbet geçmişi kaydedilemedi. Disk alanını, sohbet boyutunu ve klasör izinlerini kontrol et.',
     'history_forked':'Bu sohbet başka bir DocMind oturumunda değişmiş; veri kaybını önlemek için devamı ayrı kaydediliyor.',
     'history_privacy':'Sohbetler otomatik sıkıştırılarak kaydedilir; dosyalar şifreli değildir.',
     'history_help':' /history   Kayıtlı sohbetleri aç',
   },
   'en': {
     'history_title':'Conversation history', 'history_choose':'Conversation number (Enter to cancel): ',
     'history_empty':'No saved conversations yet. The first message is saved automatically.',
     'history_invalid':'Enter a valid conversation number.', 'history_cancel':'Conversation selection cancelled.',
     'history_loaded':'Conversation loaded: {title}', 'history_you':'You', 'history_cancelled':'not completed / cancelled',
     'history_read_error':'Could not read conversation history. Check the file and permissions.',
     'history_write_error':'Could not save conversation history. Check its size, disk space and permissions.',
     'history_forked':'Another DocMind session changed this conversation; saving this continuation separately to prevent data loss.',
     'history_privacy':'Conversations are saved automatically in compressed files, not encrypted.',
     'history_help':' /history   Open saved conversations',
   },
   'de': {
     'history_title':'Gesprächsverlauf', 'history_choose':'Gesprächsnummer (Enter: abbrechen): ',
     'history_empty':'Noch keine Gespräche gespeichert. Die erste Nachricht wird automatisch gespeichert.',
     'history_invalid':'Bitte eine gültige Gesprächsnummer eingeben.', 'history_cancel':'Auswahl abgebrochen.',
     'history_loaded':'Gespräch geladen: {title}', 'history_you':'Du', 'history_cancelled':'abgebrochen',
     'history_read_error':'Verlauf konnte nicht gelesen werden. Datei und Berechtigungen prüfen.',
     'history_write_error':'Verlauf konnte nicht gespeichert werden. Größe, Speicherplatz und Berechtigungen prüfen.',
     'history_forked':'Eine andere Sitzung hat dieses Gespräch verändert; Fortsetzung wird separat gespeichert.',
     'history_privacy':'Gespräche werden komprimiert, aber nicht verschlüsselt gespeichert.',
     'history_help':' /history   Gespeicherte Gespräche öffnen',
   },
   'es': {
     'history_title':'Historial de conversaciones', 'history_choose':'Número de conversación (Enter cancela): ',
     'history_empty':'Aún no hay conversaciones guardadas. El primer mensaje se guarda automáticamente.',
     'history_invalid':'Introduce un número válido.', 'history_cancel':'Selección cancelada.',
     'history_loaded':'Conversación cargada: {title}', 'history_you':'Tú', 'history_cancelled':'cancelado',
     'history_read_error':'No se pudo leer el historial. Revisa el archivo y los permisos.',
     'history_write_error':'No se pudo guardar el historial. Revisa el tamaño, el espacio y los permisos.',
     'history_forked':'Otra sesión modificó esta conversación; se guardará una continuación separada.',
     'history_privacy':'Las conversaciones se guardan comprimidas, pero no cifradas.',
     'history_help':' /history   Abrir conversaciones guardadas',
   },
   'fr': {
     'history_title':'Historique des conversations', 'history_choose':'Numéro de conversation (Entrée annule) : ',
     'history_empty':'Aucune conversation enregistrée. Le premier message est sauvegardé automatiquement.',
     'history_invalid':'Entrez un numéro valide.', 'history_cancel':'Sélection annulée.',
     'history_loaded':'Conversation chargée : {title}', 'history_you':'Vous', 'history_cancelled':'annulé',
     'history_read_error':'Impossible de lire l’historique. Vérifiez le fichier et ses permissions.',
     'history_write_error':'Impossible d’enregistrer l’historique. Vérifiez sa taille, l’espace et les permissions.',
     'history_forked':'Une autre session a modifié cette conversation ; la suite est enregistrée séparément.',
     'history_privacy':'Les conversations sont enregistrées compressées, mais non chiffrées.',
     'history_help':' /history   Ouvrir les conversations enregistrées',
   },
   'ru': {
     'history_title':'История разговоров', 'history_choose':'Номер разговора (Enter — отмена): ',
     'history_empty':'Сохранённых разговоров пока нет. Первое сообщение сохраняется автоматически.',
     'history_invalid':'Введите правильный номер.', 'history_cancel':'Выбор отменён.',
     'history_loaded':'Разговор загружен: {title}', 'history_you':'Вы', 'history_cancelled':'отменено',
     'history_read_error':'Не удалось прочитать историю. Проверьте файл и права.',
     'history_write_error':'Не удалось сохранить историю. Проверьте размер, место и права.',
     'history_forked':'Другая сессия изменила разговор; продолжение будет сохранено отдельно.',
     'history_privacy':'Разговоры сохраняются сжатыми, но не зашифрованными.',
     'history_help':' /history   Открыть сохранённые разговоры',
   },
 }
 for _language, _history_strings in _HISTORY_TEXT.items():
   TRANSLATIONS[_language].update(_history_strings)
   TRANSLATIONS[_language]['help_body'] += '\n' + _history_strings['history_help']
 _HISTORY_DELETE = {
  'tr': {'history_delete_hint':'Sohbet silmek için /delete yazın.',
     'history_delete_title':'Sohbet sil',
     'history_delete_warning':'Seçilen sohbet kalıcı olarak silinir; açık sohbetse bellekten de çıkar.',
     'history_delete_choose':'Silinecek sohbet numarası (Enter: iptal): ',
     'history_delete_ok':'Sohbet silindi: {title}',
     'history_delete_active':'Açık sohbet temizlendi; yeni bir sohbet başladı.',
     'history_delete_error':'Sohbet silinemedi. Dosyanın ve klasörün izinlerini kontrol et.',
     'history_delete_help':' /delete    Kayıtlı sohbeti sil'},
  'en': {'history_delete_hint':'Type /delete to delete a conversation.', 'history_delete_title':'Delete conversation',
     'history_delete_warning':'The chosen conversation is permanently deleted; an open one is also cleared from memory.',
     'history_delete_choose':'Conversation number to delete (Enter cancels): ', 'history_delete_ok':'Conversation deleted: {title}',
     'history_delete_active':'The open conversation was cleared; a new one has started.',
     'history_delete_error':'Could not delete the conversation. Check file and directory permissions.',
     'history_delete_help':' /delete    Delete a saved conversation'},
  'de': {'history_delete_hint':'Zum Löschen eines Gesprächs /delete eingeben.', 'history_delete_title':'Gespräch löschen',
     'history_delete_warning':'Das gewählte Gespräch wird dauerhaft gelöscht und bei Bedarf aus dem Speicher entfernt.',
     'history_delete_choose':'Zu löschende Nummer (Enter: abbrechen): ', 'history_delete_ok':'Gespräch gelöscht: {title}',
     'history_delete_active':'Das offene Gespräch wurde geleert; ein neues hat begonnen.',
     'history_delete_error':'Gespräch konnte nicht gelöscht werden. Berechtigungen prüfen.',
     'history_delete_help':' /delete    Gespeichertes Gespräch löschen'},
  'es': {'history_delete_hint':'Escribe /delete para eliminar una conversación.', 'history_delete_title':'Eliminar conversación',
     'history_delete_warning':'La conversación elegida se elimina de forma permanente y, si está abierta, de la memoria.',
     'history_delete_choose':'Número a eliminar (Enter cancela): ', 'history_delete_ok':'Conversación eliminada: {title}',
     'history_delete_active':'Se borró la conversación abierta; comenzó una nueva.',
     'history_delete_error':'No se pudo eliminar. Revisa los permisos del archivo y la carpeta.',
     'history_delete_help':' /delete    Eliminar conversación guardada'},
  'fr': {'history_delete_hint':'Tapez /delete pour supprimer une conversation.', 'history_delete_title':'Supprimer une conversation',
     'history_delete_warning':'La conversation choisie est supprimée définitivement et, si elle est ouverte, de la mémoire.',
     'history_delete_choose':'Numéro à supprimer (Entrée annule) : ', 'history_delete_ok':'Conversation supprimée : {title}',
     'history_delete_active':'La conversation ouverte a été effacée ; une nouvelle a commencé.',
     'history_delete_error':'Impossible de supprimer la conversation. Vérifiez les permissions.',
     'history_delete_help':' /delete    Supprimer une conversation enregistrée'},
  'ru': {'history_delete_hint':'Для удаления разговора введите /delete.', 'history_delete_title':'Удалить разговор',
     'history_delete_warning':'Выбранный разговор удаляется безвозвратно и, если он открыт, из памяти.',
     'history_delete_choose':'Номер для удаления (Enter — отмена): ', 'history_delete_ok':'Разговор удалён: {title}',
     'history_delete_active':'Открытый разговор очищен; начался новый.',
     'history_delete_error':'Не удалось удалить разговор. Проверьте права файла и папки.',
     'history_delete_help':' /delete    Удалить сохранённый разговор'},
 }
 for _language, _delete_strings in _HISTORY_DELETE.items():
   TRANSLATIONS[_language].update(_delete_strings)
   TRANSLATIONS[_language]['help_body'] += '\n' + _delete_strings['history_delete_help']
 _AGENT_RELIABILITY_WORDING = {
   "tr": {
     "auto_syntax_ok": "{path}: otomatik sözdizimi kontrolü başarılı (işlevsel test değildir).",
     "auto_syntax_failed": "{path}: otomatik sözdizimi kontrolü başarısız veya yapılamadı; ayrıntı modele iletildi.",
     "loop_suppressed": "Tekrarlanan başarısız veya reddedilen işlem çalıştırılmadı: {name}",
     "loop_stopped": "Agent tekrara takıldı ve yeni işlem yapmadan durduruldu. Farklı bir yol veya yeni talimat verebilirsiniz.",
     "tool_args_retry": "Model geçersiz araç verisi üretti; işlem yapılmadı. Bir kez daha düzeltilmesi isteniyor (ek API ücreti oluşabilir).",
   },
   "en": {
     "auto_syntax_ok": "{path}: automatic syntax check passed (not a functional test).",
     "auto_syntax_failed": "{path}: automatic syntax check failed or could not run; details were sent to the model.",
     "loop_suppressed": "Repeated failed or declined action was not executed: {name}",
     "loop_stopped": "The agent was stuck repeating itself and stopped without further actions. You can provide a different approach or new instruction.",
     "tool_args_retry": "The model returned invalid tool arguments; nothing was executed. Requesting one correction (an extra API charge may apply).",
   },
   "de": {
     "auto_syntax_ok": "{path}: automatische Syntaxprüfung erfolgreich (kein Funktionstest).",
     "auto_syntax_failed": "{path}: automatische Syntaxprüfung fehlgeschlagen oder nicht möglich; Details wurden an das Modell übermittelt.",
     "loop_suppressed": "Wiederholte fehlgeschlagene oder abgelehnte Aktion nicht ausgeführt: {name}",
     "loop_stopped": "Der Agent wiederholte sich und wurde ohne weitere Aktionen gestoppt. Geben Sie einen anderen Ansatz oder neue Anweisungen ein.",
     "tool_args_retry": "Das Modell lieferte ungültige Werkzeugargumente; nichts wurde ausgeführt. Eine Korrektur wird angefordert (zusätzliche API-Kosten möglich).",
   },
   "es": {
     "auto_syntax_ok": "{path}: comprobación automática de sintaxis correcta (no es una prueba funcional).",
     "auto_syntax_failed": "{path}: la comprobación automática falló o no pudo ejecutarse; se enviaron detalles al modelo.",
     "loop_suppressed": "No se ejecutó la acción fallida o rechazada repetida: {name}",
     "loop_stopped": "El agente quedó repitiéndose y se detuvo sin más acciones. Puede indicar otra estrategia o una nueva instrucción.",
     "tool_args_retry": "El modelo devolvió argumentos inválidos; no se ejecutó nada. Se solicita una corrección (puede tener un coste adicional de API).",
   },
   "fr": {
     "auto_syntax_ok": "{path} : vérification syntaxique automatique réussie (ce n'est pas un test fonctionnel).",
     "auto_syntax_failed": "{path} : vérification syntaxique échouée ou impossible ; les détails ont été transmis au modèle.",
     "loop_suppressed": "Action échouée ou refusée répétée non exécutée : {name}",
     "loop_stopped": "L'agent se répétait et s'est arrêté sans autre action. Vous pouvez fournir une autre approche ou instruction.",
     "tool_args_retry": "Arguments d'outil invalides ; rien n'a été exécuté. Une correction est demandée (coût API supplémentaire possible).",
   },
   "ru": {
     "auto_syntax_ok": "{path}: автоматическая проверка синтаксиса пройдена (это не функциональный тест).",
     "auto_syntax_failed": "{path}: автоматическая проверка синтаксиса не удалась или невозможна; подробности переданы модели.",
     "loop_suppressed": "Повторное неудачное или отклонённое действие не выполнено: {name}",
     "loop_stopped": "Агент зациклился и остановлен без дальнейших действий. Можно предложить другой подход или новую инструкцию.",
     "tool_args_retry": "Модель вернула неверные аргументы; ничего не выполнено. Запрошено одно исправление (возможна дополнительная плата за API).",
   },
 }
 for _language, _wording in _AGENT_RELIABILITY_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _EFFORT_WORDING = {
   'tr': {
     'effort_active': 'Düşünme ayarı: {level}. Desteklenen modellerde kullanılır; yüksek seviye süreyi ve API maliyetini artırabilir. /effort ile değiştirin.',
     'effort_uncontrolled': 'Bu sağlayıcı/model için DocMind özel düşünme parametresi göndermiyor; sağlayıcının kendi ayarı geçerli.',
     'effort_usage': 'Kullanım: /effort max|high|medium|low|default (veya /zeka maksimum|yüksek|orta|düşük|varsayılan).',
     'effort_saved': 'Düşünme ayarı kaydedildi: {level}.',
     'effort_not_saved': 'Düşünme ayarı bu oturumda {level}; ayarlara kaydedilemedi.',
     'effort_help': ' /effort    Düşünme düzeyi ve maliyet',
   },
   'en': {
     'effort_active': 'Reasoning setting: {level}. Used on supported models; high can increase latency and API cost. Change with /effort.',
     'effort_uncontrolled': 'DocMind sends no explicit reasoning parameter for this provider/model; the provider default applies.',
     'effort_usage': 'Usage: /effort max|high|medium|low|default.',
     'effort_saved': 'Reasoning setting saved: {level}.',
     'effort_not_saved': 'Reasoning setting is {level} for this session but could not be saved.',
     'effort_help': ' /effort    Reasoning level and cost',
   },
   'de': {
     'effort_active': 'Denkstufe: {level}. Bei unterstützten Modellen; hoch kann Wartezeit und API-Kosten erhöhen. Ändern mit /effort.',
     'effort_uncontrolled': 'Für diesen Anbieter/dieses Modell wird kein Denkparameter gesendet; der Standard des Anbieters gilt.',
     'effort_usage': 'Nutzung: /effort max|high|medium|low|default.',
     'effort_saved': 'Denkstufe gespeichert: {level}.', 'effort_not_saved': 'Denkstufe ist {level} für diese Sitzung, konnte aber nicht gespeichert werden.',
     'effort_help': ' /effort    Denkstufe und Kosten',
   },
   'es': {
     'effort_active': 'Nivel de razonamiento: {level}. En modelos compatibles, high puede aumentar el tiempo y el coste de API. Cambia con /effort.',
     'effort_uncontrolled': 'DocMind no envía un parámetro de razonamiento para este proveedor/modelo; se usa su valor predeterminado.',
     'effort_usage': 'Uso: /effort max|high|medium|low|default.',
     'effort_saved': 'Nivel de razonamiento guardado: {level}.', 'effort_not_saved': 'El nivel es {level} en esta sesión, pero no pudo guardarse.',
     'effort_help': ' /effort    Razonamiento y coste',
   },
   'fr': {
     'effort_active': 'Niveau de raisonnement : {level}. Sur les modèles compatibles, high peut augmenter le délai et le coût API. Modifier avec /effort.',
     'effort_uncontrolled': 'DocMind n’envoie aucun paramètre de raisonnement pour ce fournisseur/modèle ; son réglage par défaut s’applique.',
     'effort_usage': 'Utilisation : /effort max|high|medium|low|default.',
     'effort_saved': 'Niveau de raisonnement enregistré : {level}.', 'effort_not_saved': 'Le niveau {level} est actif pour cette session, mais n’a pas pu être enregistré.',
     'effort_help': ' /effort    Raisonnement et coût',
   },
   'ru': {
     'effort_active': 'Уровень рассуждений: {level}. На поддерживаемых моделях high может увеличить задержку и стоимость API. Изменить: /effort.',
     'effort_uncontrolled': 'Для этого провайдера/модели DocMind не отправляет параметр рассуждений; действует настройка провайдера.',
     'effort_usage': 'Использование: /effort max|high|medium|low|default.',
     'effort_saved': 'Уровень рассуждений сохранён: {level}.', 'effort_not_saved': 'Уровень {level} действует в этой сессии, но не сохранён.',
     'effort_help': ' /effort    Уровень рассуждений и стоимость',
   },
 }
 _EFFORT_ACTUAL = {
   'tr': 'Bu model için API’ye gönderilecek en yüksek desteklenen düzey: {actual}. Maksimum seviye önemli ölçüde daha fazla zaman ve ücret gerektirebilir.',
   'en': 'Highest supported level sent for this model: {actual}. Maximum may use substantially more time and money.',
   'de': 'Höchste unterstützte Stufe für dieses Modell: {actual}. Maximum kann deutlich mehr Zeit und Kosten verursachen.',
   'es': 'Nivel máximo compatible enviado a este modelo: {actual}. El máximo puede requerir mucho más tiempo y dinero.',
   'fr': 'Niveau maximal pris en charge pour ce modèle : {actual}. Le maximum peut coûter nettement plus de temps et d’argent.',
   'ru': 'Максимальный поддерживаемый уровень для этой модели: {actual}. Максимум может значительно увеличить время и расходы.',
 }
 _EFFORT_FALLBACK = {
   'tr': 'Sağlayıcı düşünme parametresini reddetti. İşlem yapılmadan yeniden deneniyor; bu model/düzey için sağlayıcının varsayılanı kullanılacak. Ek API ücreti oluşabilir.',
   'en': 'The provider rejected the reasoning parameter. Retrying before any action; the provider default will be used for this model/level. Extra API charges may apply.',
   'de': 'Der Anbieter hat den Denkparameter abgelehnt. Vor einer Aktion wird mit Anbieterstandard erneut versucht. Zusätzliche API-Kosten sind möglich.',
   'es': 'El proveedor rechazó el parámetro de razonamiento. Se reintenta antes de actuar usando su valor predeterminado. Puede haber costes adicionales.',
   'fr': 'Le fournisseur a rejeté le paramètre de raisonnement. Nouvelle tentative avant toute action avec son réglage par défaut. Des frais API supplémentaires sont possibles.',
   'ru': 'Провайдер отклонил параметр рассуждений. Повтор до выполнения действий с настройкой провайдера. Возможна дополнительная плата API.',
 }
 _EFFORT_FALLBACK_ACTIVE = {
   'tr': 'Bu oturumda bu model/düzey reddedildi; isteklerde şu anda sağlayıcının varsayılanı kullanılıyor. /effort ile yeniden seçebilirsiniz.',
   'en': 'This model/level was rejected during this session; requests currently use the provider default. Select a level again with /effort.',
   'de': 'Dieses Modell/diese Stufe wurde in dieser Sitzung abgelehnt; Anfragen nutzen derzeit den Anbieterstandard. Mit /effort erneut auswählen.',
   'es': 'Este modelo/nivel fue rechazado en esta sesión; las solicitudes usan el valor predeterminado del proveedor. Elige de nuevo con /effort.',
   'fr': 'Ce modèle/niveau a été rejeté pendant cette session ; les requêtes utilisent le réglage par défaut du fournisseur. Resélectionnez avec /effort.',
   'ru': 'Этот уровень модели был отклонён в текущем сеансе; запросы используют настройку провайдера. Выберите уровень снова через /effort.',
 }
 for _language, _wording in _EFFORT_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
   TRANSLATIONS[_language]['effort_actual'] = _EFFORT_ACTUAL[_language]
   TRANSLATIONS[_language]['effort_fallback'] = _EFFORT_FALLBACK[_language]
   TRANSLATIONS[_language]['effort_fallback_active'] = _EFFORT_FALLBACK_ACTIVE[_language]
   TRANSLATIONS[_language]['help_body'] += '\n' + _wording['effort_help']
 _PROVIDER_DIAGNOSTICS_WORDING = {
   'tr': {
     'compat_fallback': 'Sağlayıcı isteğin bir alanını veya yerel araç biçimini reddetti; uyumlu biçimle yeniden deneniyor. Ek API ücreti oluşabilir.',
     'doctor_connection_ok': '✔ Canlı bağlantı: model yanıt verdi (araç kullanımı ayrıca test edilir).',
     'doctor_tools_skipped': 'Araç test edilmedi. /doctor tools gerçek API ile test eder; ek ücret oluşabilir.',
     'doctor_tools_start': 'Araç şemaları sağlayıcıya gönderiliyor; ek API isteği yapılır, hiçbir araç çalıştırılmaz.',
     'doctor_tools_ok': '✔ Araç çağrısı testi: beklenen deneme çağrısı alındı ({mode}); hiçbir araç çalıştırılmadı.',
     'doctor_tools_inconclusive': '⚠ Araç testi başarısız veya sonuçsuz; model beklenen deneme çağrısını üretmedi. Hiçbir araç çalıştırılmadı.',
     'doctor_tool_native_mode': 'yerel araç API', 'doctor_tool_prompt_mode': 'metin tabanlı uyumluluk',
     'doctor_usage': 'Kullanım: /doctor veya /doctor tools',
     'doctor_tools_help': ' /doctor tools  API ile araç şemalarını sınar; ek ücret oluşabilir',
   },
   'en': {
     'compat_fallback': 'The provider rejected a request field or native tool format; retrying in a compatible form. Extra API charges may apply.',
     'doctor_connection_ok': '✔ Live connection: model responded (tool use is tested separately).',
     'doctor_tools_skipped': 'Tool use not tested. /doctor tools runs a real API test; charges may apply.',
     'doctor_tools_start': 'Sending the agent tool schemas to the provider; an extra API request is made, but no tools are executed.',
     'doctor_tools_ok': '✔ Tool-call test: expected diagnostic call received ({mode}); no tool was executed.',
     'doctor_tools_inconclusive': '⚠ Tool test failed or was inconclusive; the expected diagnostic call was not received. No tool was executed.',
     'doctor_tool_native_mode': 'native tool API', 'doctor_tool_prompt_mode': 'prompt-based compatibility',
     'doctor_usage': 'Usage: /doctor or /doctor tools',
     'doctor_tools_help': ' /doctor tools  Test tool schemas with the API; charges may apply',
   },
   'de': {
     'compat_fallback': 'Der Anbieter hat ein Feld oder das native Werkzeugformat abgelehnt; ein kompatibler Versuch folgt. Zusätzliche API-Kosten sind möglich.',
     'doctor_connection_ok': '✔ Live-Verbindung: Modell hat geantwortet (Werkzeuge werden separat getestet).',
     'doctor_tools_skipped': 'Werkzeuge nicht getestet. /doctor tools nutzt die echte API; Kosten sind möglich.',
     'doctor_tools_start': 'Werkzeugschemas werden an die API gesendet; eine Zusatzanfrage, aber keine Werkzeugausführung.',
     'doctor_tools_ok': '✔ Werkzeugtest: erwarteter Diagnoseaufruf erhalten ({mode}); nichts wurde ausgeführt.',
     'doctor_tools_inconclusive': '⚠ Werkzeugtest fehlgeschlagen oder ohne eindeutiges Ergebnis; nichts wurde ausgeführt.',
     'doctor_tool_native_mode': 'native Werkzeug-API', 'doctor_tool_prompt_mode': 'textbasierte Kompatibilität',
     'doctor_usage': 'Nutzung: /doctor oder /doctor tools',
     'doctor_tools_help': ' /doctor tools  Werkzeugschemas über die API testen; Kosten möglich',
   },
   'es': {
     'compat_fallback': 'El proveedor rechazó un campo o el formato nativo de herramientas; se reintenta con un formato compatible. Puede haber costes adicionales.',
     'doctor_connection_ok': '✔ Conexión real: el modelo respondió (las herramientas se prueban por separado).',
     'doctor_tools_skipped': 'Herramientas sin probar. /doctor tools usa la API real y puede generar costes.',
     'doctor_tools_start': 'Se envían los esquemas a la API; hay una solicitud adicional, pero no se ejecuta ninguna herramienta.',
     'doctor_tools_ok': '✔ Prueba de herramientas: llamada de diagnóstico recibida ({mode}); no se ejecutó ninguna herramienta.',
     'doctor_tools_inconclusive': '⚠ La prueba de herramientas falló o no fue concluyente; no se ejecutó ninguna herramienta.',
     'doctor_tool_native_mode': 'API nativa', 'doctor_tool_prompt_mode': 'compatibilidad basada en texto',
     'doctor_usage': 'Uso: /doctor o /doctor tools',
     'doctor_tools_help': ' /doctor tools  Prueba los esquemas con la API; puede tener coste',
   },
   'fr': {
     'compat_fallback': 'Le fournisseur a refusé un champ ou le format natif des outils ; nouvel essai compatible. Des frais API supplémentaires sont possibles.',
     'doctor_connection_ok': '✔ Connexion réelle : le modèle a répondu (outils testés séparément).',
     'doctor_tools_skipped': 'Outils non testés. /doctor tools utilise la vraie API ; des frais sont possibles.',
     'doctor_tools_start': 'Envoi des schémas à l’API ; requête supplémentaire, mais aucun outil n’est exécuté.',
     'doctor_tools_ok': '✔ Test d’outil : appel de diagnostic reçu ({mode}) ; aucun outil exécuté.',
     'doctor_tools_inconclusive': '⚠ Test d’outil échoué ou non concluant ; aucun outil exécuté.',
     'doctor_tool_native_mode': 'API native', 'doctor_tool_prompt_mode': 'compatibilité par texte',
     'doctor_usage': 'Utilisation : /doctor ou /doctor tools',
     'doctor_tools_help': ' /doctor tools  Tester les schémas via l’API ; frais possibles',
   },
   'ru': {
     'compat_fallback': 'Провайдер отклонил поле или собственный формат инструментов; повтор с совместимым форматом. Возможна дополнительная плата API.',
     'doctor_connection_ok': '✔ Подключение: модель ответила (инструменты проверяются отдельно).',
     'doctor_tools_skipped': 'Инструменты не проверены. /doctor tools обращается к API; возможна плата.',
     'doctor_tools_start': 'Схемы отправляются провайдеру; это дополнительный запрос, но инструменты не выполняются.',
     'doctor_tools_ok': '✔ Проверка инструментов: диагностический вызов получен ({mode}); ничего не выполнено.',
     'doctor_tools_inconclusive': '⚠ Проверка инструментов не удалась или не дала результата; ничего не выполнено.',
     'doctor_tool_native_mode': 'нативный API инструментов', 'doctor_tool_prompt_mode': 'текстовая совместимость',
     'doctor_usage': 'Использование: /doctor или /doctor tools',
     'doctor_tools_help': ' /doctor tools  Проверить схемы через API; возможна плата',
   },
 }
 for _language, _wording in _PROVIDER_DIAGNOSTICS_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
   TRANSLATIONS[_language]['help_body'] += '\n' + _wording['doctor_tools_help']
 _REQUEST_BUDGET_WORDING = {
   'tr': {
     'err_request_budget_title': 'TEK İSTEK TOKEN SINIRINI AŞIYOR',
     'err_request_budget_desc': '{provider} için bu isteğin tamamı dakika başına token bütçesinden büyük; beklemek sorunu çözmez. Mesajı veya geçmişi küçültün, yeni oturum açın ya da farklı model/hesap kullanın. Ayrıntı: {detail}',
     'budget_fallback': 'Sağlayıcının tek istek token sınırı aşıldı. Yalnızca bu isteğin yanıt sınırı {limit} tokene düşürülerek bir kez daha deneniyor; yanıt kısalabilir ve ek API ücreti oluşabilir.',
   },
   'en': {
     'err_request_budget_title': 'SINGLE REQUEST EXCEEDS TOKEN BUDGET',
     'err_request_budget_desc': 'This request is larger than {provider}’s per-minute token budget; waiting cannot fix it. Shorten the message or history, start a new session, or use another model/account. Detail: {detail}',
     'budget_fallback': 'The provider’s single-request token limit was exceeded. Retrying once with this request’s output cap reduced to {limit}; the answer may be shorter and extra API charges may apply.',
   },
   'de': {
     'err_request_budget_title': 'EINZELANFRAGE ÜBERSCHREITET TOKENBUDGET',
     'err_request_budget_desc': 'Diese Anfrage ist größer als das Minutenbudget von {provider}; Warten hilft nicht. Nachricht oder Verlauf kürzen, neue Sitzung oder anderes Modell/Konto nutzen. Details: {detail}',
     'budget_fallback': 'Einzelanfrage überschreitet das Tokenbudget. Ein neuer Versuch mit Ausgabelimit {limit}; die Antwort kann kürzer sein und API-Kosten können entstehen.',
   },
   'es': {
     'err_request_budget_title': 'LA SOLICITUD SUPERA EL LÍMITE DE TOKENS',
     'err_request_budget_desc': 'La solicitud supera el presupuesto por minuto de {provider}; esperar no lo resuelve. Reduce el mensaje o historial, inicia otra sesión o usa otro modelo/cuenta. Detalle: {detail}',
     'budget_fallback': 'La solicitud supera el límite de tokens. Se reintenta una vez con un máximo de salida de {limit}; la respuesta puede ser más corta y generar costes.',
   },
   'fr': {
     'err_request_budget_title': 'LA REQUÊTE DÉPASSE LE BUDGET DE TOKENS',
     'err_request_budget_desc': 'La requête dépasse le budget par minute de {provider} ; attendre ne suffit pas. Réduisez le message ou l’historique, ouvrez une session ou changez de modèle/compte. Détail : {detail}',
     'budget_fallback': 'La requête dépasse le budget de tokens. Un nouvel essai réduit la sortie à {limit} ; la réponse peut être plus courte et des frais peuvent s’appliquer.',
   },
   'ru': {
     'err_request_budget_title': 'ЗАПРОС ПРЕВЫШАЕТ ЛИМИТ ТОКЕНОВ',
     'err_request_budget_desc': 'Запрос больше минутного лимита {provider}; ожидание не поможет. Сократите сообщение или историю, начните новую сессию или смените модель/учётную запись. Детали: {detail}',
     'budget_fallback': 'Запрос превышает лимит токенов. Одна повторная попытка с лимитом ответа {limit}; ответ может стать короче, возможна дополнительная плата.',
   },
 }
 for _language, _wording in _REQUEST_BUDGET_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _PROBE_RETRY = {
   'tr': 'Bağlantı testinde model düşünme sınırına ulaştı ve metin vermedi. Bir kez 1024 token sınırıyla tekrar deneniyor; ilk deneme ücretlenmiş olabilir.',
   'en': 'The model used the connection test budget without returning text. Retrying once with a 1024-token cap; the first attempt may have been billed.',
   'de': 'Das Modell erreichte das Testlimit ohne Text. Ein neuer Versuch mit 1024 Token; der erste kann kostenpflichtig gewesen sein.',
   'es': 'El modelo agotó el límite de prueba sin texto. Se reintenta una vez con 1024 tokens; el primer intento puede tener coste.',
   'fr': 'Le modèle a atteint la limite du test sans texte. Nouvel essai à 1024 tokens ; le premier peut avoir été facturé.',
   'ru': 'Модель исчерпала лимит проверки без текста. Одна повторная попытка с лимитом 1024 токена; первая могла быть платной.',
 }
 for _language, _wording in _PROBE_RETRY.items():
   TRANSLATIONS[_language]['probe_retry'] = _wording
 _EDGE_BLOCK_WORDING = {
   'tr': {
     'err_edge_block_title': 'SAĞLAYICININ GÜVENLİK KATMANI İSTEĞİ ENGELLEDİ (1010)',
     'err_edge_block_desc': '{provider} isteği API’ye ulaşmadan güvenlik katmanında engellenmiş olabilir (HTTP 403 / 1010). Bu hata API anahtarının geçersiz olduğunu göstermez. DocMind’in güncel sürümünü kullanın; sorun sürerse VPN/proxy ve ağınızı kontrol edip sağlayıcı desteğine 403 / 1010 bilgisini iletin. API anahtarınızı paylaşmayın.',
   },
   'en': {
     'err_edge_block_title': 'PROVIDER SECURITY EDGE BLOCKED THE REQUEST (1010)',
     'err_edge_block_desc': 'The {provider} request may have been blocked by a security edge before reaching the API (HTTP 403 / 1010). This does not prove the API key is invalid. Use the latest DocMind; if it persists, check your VPN/proxy and network, and report 403 / 1010 to the provider. Never share your key.',
   },
   'de': {
     'err_edge_block_title': 'SICHERHEITSSCHICHT DES ANBIETERS BLOCKIERT ANFRAGE (1010)',
     'err_edge_block_desc': 'Die Anfrage an {provider} wurde möglicherweise vor der API blockiert (HTTP 403 / 1010). Das belegt keinen ungültigen API-Schlüssel. Nutzen Sie aktuelles DocMind; prüfen Sie bei Fortbestand VPN/Proxy und Netzwerk und melden Sie 403 / 1010 dem Anbieter. Teilen Sie Ihren Schlüssel nicht.',
   },
   'es': {
     'err_edge_block_title': 'LA CAPA DE SEGURIDAD BLOQUEÓ LA SOLICITUD (1010)',
     'err_edge_block_desc': 'La solicitud a {provider} pudo ser bloqueada antes de llegar a la API (HTTP 403 / 1010). Esto no demuestra que la clave sea inválida. Actualiza DocMind; si persiste, revisa la red o VPN/proxy e informa al proveedor de 403 / 1010. No compartas la clave.',
   },
   'fr': {
     'err_edge_block_title': 'LA COUCHE DE SÉCURITÉ A BLOQUÉ LA REQUÊTE (1010)',
     'err_edge_block_desc': 'La requête vers {provider} a pu être bloquée avant l’API (HTTP 403 / 1010). Cela ne prouve pas que la clé est invalide. Utilisez DocMind à jour ; si le problème persiste, vérifiez le réseau ou VPN/proxy et signalez 403 / 1010 au fournisseur. Ne partagez pas votre clé.',
   },
   'ru': {
     'err_edge_block_title': 'ЗАПРОС ЗАБЛОКИРОВАН ЗАЩИТОЙ ПРОВАЙДЕРА (1010)',
     'err_edge_block_desc': 'Запрос к {provider} мог быть заблокирован до API (HTTP 403 / 1010). Это не означает, что ключ недействителен. Обновите DocMind; если ошибка сохраняется, проверьте сеть или VPN/proxy и сообщите провайдеру код 403 / 1010. Не сообщайте API-ключ.',
   },
 }
 for _language, _wording in _EDGE_BLOCK_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _ACCESS_DENIED_WORDING = {
   'tr': {
     'err_access_denied_title': 'SAĞLAYICI ERİŞİMİ REDDETTİ (403)',
     'err_access_denied_desc': '{provider} erişimi reddetti. Hesap/model yetkisi, bölge, ağ veya sağlayıcının güvenlik politikası etkili olabilir; bu kod tek başına anahtarın geçersiz olduğunu kanıtlamaz. Sağlayıcı panelindeki izinleri kontrol edin. Detay: {detail}',
   },
   'en': {
     'err_access_denied_title': 'PROVIDER DENIED ACCESS (403)',
     'err_access_denied_desc': '{provider} denied access. Account or model permissions, region, network, or provider policy may be involved; this status alone does not prove the key is invalid. Check the provider dashboard. Detail: {detail}',
   },
   'de': {
     'err_access_denied_title': 'ANBIETER VERWEIGERT ZUGRIFF (403)',
     'err_access_denied_desc': '{provider} verweigerte den Zugriff. Konto-/Modellberechtigung, Region, Netzwerk oder Sicherheitsrichtlinie können die Ursache sein; der Status allein belegt keinen ungültigen Schlüssel. Details: {detail}',
   },
   'es': {
     'err_access_denied_title': 'EL PROVEEDOR DENEGÓ EL ACCESO (403)',
     'err_access_denied_desc': '{provider} denegó el acceso. Puede deberse a permisos, región, red o políticas; el código por sí solo no demuestra que la clave sea inválida. Detalle: {detail}',
   },
   'fr': {
     'err_access_denied_title': 'ACCÈS REFUSÉ PAR LE FOURNISSEUR (403)',
     'err_access_denied_desc': '{provider} a refusé l’accès. Les autorisations, la région, le réseau ou les règles du fournisseur peuvent être en cause ; ce code seul ne prouve pas que la clé est invalide. Détail : {detail}',
   },
   'ru': {
     'err_access_denied_title': 'ПРОВАЙДЕР ОТКАЗАЛ В ДОСТУПЕ (403)',
     'err_access_denied_desc': '{provider} отказал в доступе. Причиной могут быть права учётной записи или модели, регион, сеть или политика безопасности; сам код не доказывает недействительность ключа. Детали: {detail}',
   },
 }
 for _language, _wording in _ACCESS_DENIED_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _RETRY_RELIABILITY_WORDING = {
  'tr': {'retry_exhausted': '{count} otomatik tekrar başarısız oldu. Ek istekler ücret oluşturabilir; devam etmek sizin seçiminiz.',
     'retry_deferred': 'Sağlayıcı en az {seconds} saniye beklenmesini istedi; otomatik olarak erken tekrar edilmeyecek.',
     'probe_transient_retry': 'Bağlantı testinde geçici hata: {seconds} sn sonra yeniden deneniyor ({attempt}/2). Ek API ücreti oluşabilir.'},
  'en': {'retry_exhausted': '{count} automatic retries failed. Further requests may incur charges; continuing is your choice.',
     'retry_deferred': 'The provider requested a wait of at least {seconds}s; no early automatic retry will be made.',
     'probe_transient_retry': 'Temporary connection-test error: retrying in {seconds}s ({attempt}/2). Additional API charges may apply.'},
  'de': {'retry_exhausted': '{count} automatische Versuche fehlgeschlagen. Weitere Anfragen können Kosten verursachen; Sie entscheiden.',
     'retry_deferred': 'Der Anbieter verlangt mindestens {seconds}s Wartezeit; kein vorzeitiger automatischer Versuch.',
     'probe_transient_retry': 'Vorübergehender Verbindungsfehler: neuer Test in {seconds}s ({attempt}/2); Kosten möglich.'},
  'es': {'retry_exhausted': 'Fallaron {count} reintentos automáticos. Más solicitudes pueden generar costes; decide si continúas.',
     'retry_deferred': 'El proveedor pide esperar al menos {seconds}s; no se reintentará antes automáticamente.',
     'probe_transient_retry': 'Error temporal de conexión: reintento en {seconds}s ({attempt}/2); puede tener coste.'},
  'fr': {'retry_exhausted': '{count} tentatives automatiques ont échoué. Les requêtes suivantes peuvent être facturées ; à vous de décider.',
     'retry_deferred': 'Le fournisseur demande au moins {seconds}s ; aucun nouvel essai automatique prématuré.',
     'probe_transient_retry': 'Erreur temporaire de connexion : nouvel essai dans {seconds}s ({attempt}/2) ; frais possibles.'},
  'ru': {'retry_exhausted': '{count} автоматических попыток не удались. Дальнейшие запросы могут быть платными; решение за вами.',
     'retry_deferred': 'Провайдер просит подождать не менее {seconds} с; преждевременного повтора не будет.',
     'probe_transient_retry': 'Временная ошибка подключения: повтор через {seconds} с ({attempt}/2); возможна плата.'},
 }
 for _language, _wording in _RETRY_RELIABILITY_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 for _language, _message in {
  'tr': '{name} ertelendi: önceki işlem başarısız veya reddedildi; agent sonucu değerlendirip yeniden planlayacak.',
  'en': '{name} deferred: an earlier action failed or was declined; the agent will reassess.',
  'de': '{name} verschoben: Eine vorherige Aktion schlug fehl oder wurde abgelehnt; der Agent plant neu.',
  'es': '{name} aplazado: una acción anterior falló o fue rechazada; el agente reevaluará.',
  'fr': '{name} reporté : une action précédente a échoué ou a été refusée ; l’agent réévaluera.',
  'ru': '{name} отложено: предыдущее действие не удалось или отклонено; агент пересмотрит план.',
 }.items():
   TRANSLATIONS[_language]['batch_deferred'] = _message
 _USAGE_CLARITY_WORDING = {
  'tr': {'footer_incomplete':'eksik', 'footer_unknown':'bilinmiyor', 'footer_calculating':'hesaplanıyor',
     'usage_incomplete_detail':'Eksik maliyet verisi: {count} istek; bunların {interrupted} tanesi kesildi veya hata verdi. Kullanım/fiyat bilgisi gelmeyebilir. Gösterilen tutar yalnızca bilinen kısmın tahminidir. Dar ekranda * işareti eksik veya devam eden veriyi gösterir.',
     'usage_complete_detail':'Kullanım ve fiyat verisi eksik olan istek yok. Dar ekranda * devam eden veriyi gösterebilir.'},
  'en': {'footer_incomplete':'incomplete', 'footer_unknown':'unknown', 'footer_calculating':'calculating',
     'usage_incomplete_detail':'Missing cost data for {count} request(s); {interrupted} were interrupted or failed. Usage or pricing may be unavailable. The amount shown estimates only the known part. On narrow screens * means incomplete or ongoing data.',
     'usage_complete_detail':'No requests are missing usage or pricing. On narrow screens * can indicate an ongoing response.'},
  'de': {'footer_incomplete':'unvollst.', 'footer_unknown':'unbekannt', 'footer_calculating':'berechne',
     'usage_incomplete_detail':'Kosten für {count} Anfragen fehlen; {interrupted} wurden unterbrochen oder scheiterten. Nutzungs- oder Preisdaten können fehlen. Angezeigt wird nur der bekannte Anteil. * bedeutet unvollständige oder laufende Daten.',
     'usage_complete_detail':'Keine Anfrage hat fehlende Nutzungs- oder Preisdaten. * kann laufende Daten anzeigen.'},
  'es': {'footer_incomplete':'incompleto', 'footer_unknown':'desconocido', 'footer_calculating':'calculando',
     'usage_incomplete_detail':'Faltan costes de {count} solicitudes; {interrupted} se interrumpieron o fallaron. Pueden faltar datos o precios. El importe solo estima la parte conocida. * indica datos incompletos o en curso.',
     'usage_complete_detail':'No faltan datos de uso o precio. * puede indicar una respuesta en curso.'},
  'fr': {'footer_incomplete':'incomplet', 'footer_unknown':'inconnu', 'footer_calculating':'calcul',
     'usage_incomplete_detail':'Coût manquant pour {count} requêtes ; {interrupted} ont échoué ou été interrompues. Les données ou tarifs peuvent manquer. Le montant estime seulement la partie connue. * indique des données incomplètes ou en cours.',
     'usage_complete_detail':'Aucune requête ne manque de données ou de tarif. * peut indiquer une réponse en cours.'},
  'ru': {'footer_incomplete':'неполно', 'footer_unknown':'неизвестно', 'footer_calculating':'подсчёт',
     'usage_incomplete_detail':'Нет данных о стоимости для {count} запросов; {interrupted} прерваны или завершились ошибкой. Данные или цена могут отсутствовать. Показана оценка только известной части. * означает неполные или текущие данные.',
     'usage_complete_detail':'Нет запросов с отсутствующими данными или ценой. * может обозначать текущий ответ.'},
 }
 for _language, _wording in _USAGE_CLARITY_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 _DOCTOR_ALL_WORDING = {
  'tr': {'doctor_usage':'Kullanım: /doctor, /doctor tools veya /doctor all',
     'doctor_all_help':' /doctor all  Kayıtlı sağlayıcılarla ücretli olabilecek bağlantı testi',
     'doctor_all_title':'Tüm yapılandırılmış sağlayıcıları test et',
     'doctor_all_none':'Test edilecek kayıtlı sağlayıcı anahtarı yok. /api ile sağlayıcı ekleyin.',
     'doctor_all_intro':'Aşağıdaki modellere gerçek API istekleri gönderilir; ek ücret oluşabilir. Aktif olmayan sağlayıcılarda varsayılan model denenir. Her sağlayıcı için kendi anahtarı ve gösterilen sunucu kullanılır; ayarlar değiştirilmez.',
     'doctor_all_confirm':'Testlere devam edilsin mi? (evet/hayır; Enter: hayır): ',
     'doctor_all_cancelled':'Test iptal edildi; hiçbir istek gönderilmedi.',
     'doctor_all_checking':'{provider} bağlantısı test ediliyor', 'doctor_all_ok':'model yanıt verdi',
     'doctor_all_failed':'test başarısız', 'doctor_all_skipped':'Atlanan (yapılandırılmamış): {names}',
     'doctor_all_tool_note':'Bu yalnızca bağlantı testidir. Aktif modelin araç uyumluluğu için /doctor tools kullanın; ek ücret oluşabilir.'},
  'en': {'doctor_usage':'Usage: /doctor, /doctor tools or /doctor all',
     'doctor_all_help':' /doctor all  Test configured providers; charges may apply',
     'doctor_all_title':'Test configured providers', 'doctor_all_none':'No configured provider credentials to test. Use /api.',
     'doctor_all_intro':'Real API requests are sent to the models below and may incur charges. Inactive providers use their default model. Each provider uses its own credential and the displayed destination; settings are unchanged.',
     'doctor_all_confirm':'Proceed with tests? (yes/no; Enter: no): ', 'doctor_all_cancelled':'Cancelled; no request was sent.',
     'doctor_all_checking':'Testing {provider} connection', 'doctor_all_ok':'model responded',
     'doctor_all_failed':'test failed', 'doctor_all_skipped':'Skipped (not configured): {names}',
     'doctor_all_tool_note':'Connection test only. Use /doctor tools for the active model; additional charges may apply.'},
  'de': {'doctor_usage':'Nutzung: /doctor, /doctor tools oder /doctor all', 'doctor_all_help':' /doctor all  Konfigurierte Anbieter prüfen; Kosten möglich',
     'doctor_all_title':'Konfigurierte Anbieter prüfen', 'doctor_all_none':'Keine Zugangsdaten zum Prüfen. /api verwenden.',
     'doctor_all_intro':'Echte API-Anfragen an die folgenden Modelle können Kosten verursachen. Inaktive Anbieter nutzen ihr Standardmodell. Jeder Anbieter nutzt seinen eigenen Schlüssel und das angezeigte Ziel; Einstellungen bleiben unverändert.',
     'doctor_all_confirm':'Tests starten? (ja/nein; Enter: nein): ', 'doctor_all_cancelled':'Abgebrochen; keine Anfrage gesendet.',
     'doctor_all_checking':'Verbindung zu {provider} wird geprüft', 'doctor_all_ok':'Modell hat geantwortet',
     'doctor_all_failed':'Test fehlgeschlagen', 'doctor_all_skipped':'Übersprungen (nicht konfiguriert): {names}',
     'doctor_all_tool_note':'Nur Verbindungstest. /doctor tools prüft das aktive Modell; Kosten möglich.'},
  'es': {'doctor_usage':'Uso: /doctor, /doctor tools o /doctor all', 'doctor_all_help':' /doctor all  Prueba proveedores configurados; puede tener coste',
     'doctor_all_title':'Probar proveedores configurados', 'doctor_all_none':'No hay credenciales configuradas. Usa /api.',
     'doctor_all_intro':'Se enviarán solicitudes reales a estos modelos; pueden generar costes. Los proveedores inactivos usan su modelo predeterminado. Cada proveedor usa su clave y el destino mostrado; no se cambian ajustes.',
     'doctor_all_confirm':'¿Continuar? (sí/no; Enter: no): ', 'doctor_all_cancelled':'Cancelado; no se envió ninguna solicitud.',
     'doctor_all_checking':'Probando conexión con {provider}', 'doctor_all_ok':'el modelo respondió',
     'doctor_all_failed':'prueba fallida', 'doctor_all_skipped':'Omitidos (sin configurar): {names}',
     'doctor_all_tool_note':'Solo prueba la conexión. /doctor tools prueba el modelo activo y puede tener coste.'},
  'fr': {'doctor_usage':'Utilisation : /doctor, /doctor tools ou /doctor all', 'doctor_all_help':' /doctor all  Tester les fournisseurs configurés ; frais possibles',
     'doctor_all_title':'Tester les fournisseurs configurés', 'doctor_all_none':'Aucun identifiant configuré. Utilisez /api.',
     'doctor_all_intro':'Des requêtes API réelles seront envoyées aux modèles suivants et peuvent être facturées. Les fournisseurs inactifs utilisent leur modèle par défaut. Chaque fournisseur utilise sa propre clé et la destination affichée ; les paramètres restent inchangés.',
     'doctor_all_confirm':'Continuer ? (oui/non ; Entrée : non) : ', 'doctor_all_cancelled':'Annulé ; aucune requête envoyée.',
     'doctor_all_checking':'Test de connexion à {provider}', 'doctor_all_ok':'le modèle a répondu',
     'doctor_all_failed':'échec du test', 'doctor_all_skipped':'Ignorés (non configurés) : {names}',
     'doctor_all_tool_note':'Test de connexion uniquement. /doctor tools teste le modèle actif ; frais possibles.'},
  'ru': {'doctor_usage':'Использование: /doctor, /doctor tools или /doctor all', 'doctor_all_help':' /doctor all  Проверить настроенных провайдеров; возможна плата',
     'doctor_all_title':'Проверка настроенных провайдеров', 'doctor_all_none':'Нет настроенных ключей. Используйте /api.',
     'doctor_all_intro':'Будут отправлены реальные API-запросы указанным моделям; возможна плата. Для неактивных провайдеров берётся модель по умолчанию. Для каждого провайдера используются свой ключ и указанный адрес; настройки не меняются.',
     'doctor_all_confirm':'Продолжить? (да/нет; Enter: нет): ', 'doctor_all_cancelled':'Отменено; запросы не отправлены.',
     'doctor_all_checking':'Проверка подключения к {provider}', 'doctor_all_ok':'модель ответила',
     'doctor_all_failed':'ошибка проверки', 'doctor_all_skipped':'Пропущены (не настроены): {names}',
     'doctor_all_tool_note':'Только проверка подключения. /doctor tools проверяет активную модель; возможна плата.'},
 }
 for _language, _wording in _DOCTOR_ALL_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
   TRANSLATIONS[_language]['help_body'] += '\n' + _wording['doctor_all_help']
 for _language, _message in {
  'tr': 'Claude bağlamı değiştiğinden eski imzalı düşünce blokları yeni isteğe eklenmedi; sohbet metni ve araç sonuçları korundu.',
  'en': 'Claude context changed, so older signed thinking blocks were omitted; conversation text and tool results were retained.',
  'de': 'Claude-Kontext geändert: ältere signierte Denkblöcke wurden ausgelassen; Gesprächstext und Werkzeugergebnisse bleiben erhalten.',
  'es': 'Cambió el contexto de Claude: se omitieron bloques de razonamiento firmados; se conservaron texto y resultados de herramientas.',
  'fr': 'Le contexte Claude a changé : les anciens blocs de réflexion signés sont omis ; le texte et les résultats sont conservés.',
  'ru': 'Контекст Claude изменился: старые подписанные блоки рассуждений исключены; текст и результаты инструментов сохранены.',
 }.items():
   TRANSLATIONS[_language]['thinking_rebase'] = _message
 for _language, _message in {
  'tr': 'Maliyet bildirilmiş olsa da {count} isteğin token verisi eksik. Dar ekranda * eksik veriyi gösterir.',
  'en': 'Cost may be reported, but token data is missing for {count} request(s). On narrow screens * marks incomplete data.',
  'de': 'Die Kosten wurden ggf. gemeldet, aber für {count} Anfragen fehlen Tokendaten. * markiert unvollständige Daten.',
  'es': 'Puede haberse informado el coste, pero faltan tokens de {count} solicitudes. * indica datos incompletos.',
  'fr': 'Le coût peut être fourni, mais les tokens de {count} requêtes manquent. * signale des données incomplètes.',
  'ru': 'Стоимость может быть указана, но данные токенов отсутствуют для {count} запросов. * означает неполные данные.',
 }.items():
   TRANSLATIONS[_language]['usage_tokens_missing_detail'] = _message
 _UNIVERSAL_AGENT_WORDING = {
   "tr": {
     "startup_authority_warn": (
       "⚠ UYARI: AGENT BİLGİSAYARINIZA TAM YETKİLİDİR — Tüm sürücüleri, klasörleri ve dosyaları "
       "görebilir, açabilir, düzenleyebilir ve (izninizle) terminal/sistem kodu çalıştırabilir. "
       "Dikkatli kullanın; doğabilecek işlemlerden sorumluluk kabul edilmez."
     ),
     "term_perm_title": "TERMİNAL / KOD ÇALIŞTIRMA İZNİ GEREKLİ",
     "term_perm_header": "TERMİNAL / KOD ÇALIŞTIRMA İZNİ GEREKLİ",
     "term_perm_denied": "Terminal / kod çalıştırma izni kullanıcı tarafından reddedildi.",
     "term_used_status": "Durum",
     "term_triage_manual": "⚠ ŞİFRE / YETKİ GEREKLİ: Bu komut şifre veya yönetici izni istediği için kullanıcı tarafından çalıştırılmalıdır.",
     "term_triage_autofix": "↻ Hata algılandı — DocMind hatayı analiz edip düzeltme yolunu değerlendiriyor...",
     "ask_user_header": "DOCMIND SORUSU / HEDEF SİSTEM SEÇİMİ",
     "ask_user_prompt": "Seçiminiz (numara veya açıklama yazın, varsayılan={default}): ",
     "term_perm_shell": "Kabuk / Ortam",
     "term_perm_cwd": "Çalışma Klasörü",
     "term_perm_code": "ÇALIŞTIRILACAK KOD",
     "term_perm_prompt": "Bu terminal/sistem kodunu çalıştırmak için izin veriyor musunuz? [E]vet / [H]ayır: ",
     "term_perm_reprompt": "Lütfen onay için 'e' (evet) veya iptal için 'h' (hayır) yazın: ",
     "term_used_header": "TERMİNAL KULLANILDI",
     "term_used_code": "KULLANILAN KOD",
     "term_used_shell": "Kabuk / Ortam",
     "term_used_cwd": "Çalışma Klasörü",
     "term_used_ok": "Başarılı (Çıkış Kodu: {code}, {elapsed:.2f} sn)",
     "term_used_err": "Hata / Çıkış Kodu: {code} ({elapsed:.2f} sn)",
     "term_used_output": "Çıktı",
     "conn_auto_heal": "Bağlantı kesintisi algılandı; oturum korunarak otomatik yeniden bağlanılıyor ({attempt}/{max_attempts})...",
   },
   "en": {
     "startup_authority_warn": (
       "⚠ WARNING: THIS AGENT HAS FULL SYSTEM ACCESS — It can view, open, and edit any drive, folder, "
       "or file on your computer and execute terminal/system commands (with your permission). "
       "Use carefully; no liability is accepted."
     ),
     "term_perm_title": "TERMINAL / CODE EXECUTION PERMISSION REQUIRED",
     "term_perm_header": "TERMINAL / CODE EXECUTION PERMISSION REQUIRED",
     "term_perm_denied": "Terminal / code execution declined by user.",
     "term_used_status": "Status",
     "term_triage_manual": "⚠ PASSWORT / ADMIN ERFORDERLICH: Dieser Befehl muss vom Benutzer selbst ausgeführt werden.",
     "term_triage_autofix": "↻ Fehler erkannt — DocMind analysiert eine Korrektur...",
     "ask_user_header": "DOCMIND-FRAGE / ZIELSYSTEM",
     "ask_user_prompt": "Ihre Wahl (Nummer oder Text, Standard={default}): ",
     "term_triage_manual": "⚠ PASSWORD / ADMIN REQUIRED: This command requires interactive credentials/elevation and must be run by the user.",
     "term_triage_autofix": "↻ Error detected — DocMind is analyzing the failure to self-correct...",
     "ask_user_header": "DOCMIND QUESTION / TARGET PLATFORM CHOICE",
     "ask_user_prompt": "Your choice (enter number or custom text, default={default}): ",
     "term_perm_shell": "Shell / Runtime",
     "term_perm_cwd": "Working Directory",
     "term_perm_code": "CODE TO EXECUTE",
     "term_perm_prompt": "Allow this terminal/system command to execute on your computer? [Y]es / [N]o: ",
     "term_perm_reprompt": "Please type 'y' (yes) to approve or 'n' (no) to decline: ",
     "term_used_header": "TERMINAL USED (TERMİNAL KULLANILDI)",
     "term_used_code": "CODE USED (KULLANILAN KOD)",
     "term_used_shell": "Shell / Runtime",
     "term_perm_cwd_lbl": "Working Directory",
     "term_used_cwd": "Working Directory",
     "term_used_ok": "Completed (Exit Code: {code}, {elapsed:.2f}s)",
     "term_used_err": "Failed / Exit Code: {code} ({elapsed:.2f}s)",
     "term_used_output": "Output",
     "conn_auto_heal": "Connection drop detected; auto-reconnecting without losing context ({attempt}/{max_attempts})...",
   },
   "de": {
     "startup_authority_warn": (
       "⚠ WARNUNG: DIESER AGENT HAT VOLLZUGRIFF AUF IHREN COMPUTER — Alle Laufwerke, Ordner und Dateien "
       "sind sichtbar/bearbeitbar und Terminal-Code kann (mit Ihrer Erlaubnis) ausgeführt werden. "
       "Vorsichtig verwenden; keine Haftung."
     ),
     "term_perm_title": "TERMINAL-AUSFÜHRUNGSGENEHMIGUNG ERFORDERLICH",
     "term_perm_header": "TERMINAL-AUSFÜHRUNGSGENEHMIGUNG ERFORDERLICH",
     "term_perm_denied": "Terminal-Ausführung vom Benutzer abgelehnt.",
     "term_triage_manual": "⚠ PASSWORT / ADMIN ERFORDERLICH: Dieser Befehl muss vom Benutzer selbst ausgeführt werden.",
     "term_triage_autofix": "↻ Fehler erkannt — DocMind analysiert eine Korrektur...",
     "ask_user_header": "DOCMIND-FRAGE / ZIELSYSTEM",
     "ask_user_prompt": "Ihre Wahl (Nummer oder Text, Standard={default}): ",
     "term_used_status": "Status",
     "term_perm_shell": "Shell / Umgebung",
     "term_perm_cwd": "Arbeitsverzeichnis",
     "term_perm_code": "AUSZUFÜHRENDER CODE",
     "term_perm_prompt": "Diesen Terminal-Befehl auf Ihrem Computer ausführen? [J]a / [N]ein: ",
     "term_perm_reprompt": "Bitte 'j' (ja) oder 'n' (nein) eingeben: ",
     "term_used_header": "TERMINAL VERWENDET",
     "term_used_code": "VERWENDETER CODE",
     "term_used_shell": "Shell / Umgebung",
     "term_used_cwd": "Arbeitsverzeichnis",
     "term_used_ok": "Erfolgreich (Exit-Code: {code}, {elapsed:.2f}s)",
     "term_used_err": "Fehler / Exit-Code: {code} ({elapsed:.2f}s)",
     "term_used_output": "Ausgabe",
     "conn_auto_heal": "Verbindungsabbruch erkannt; automatische Wiederverbindung ({attempt}/{max_attempts})...",
   },
   "es": {
     "startup_authority_warn": (
       "⚠ ADVERTENCIA: ESTE AGENTE TIENE ACCESO TOTAL A SU COMPUTADORA — Puede ver, abrir y editar cualquier "
       "disco, carpeta o archivo y ejecutar código en terminal (con su permiso). Úselo con precaución; "
       "no se acepta responsabilidad."
     ),
     "term_perm_title": "PERMISO REQUERIDO PARA EJECUTAR EN TERMINAL",
     "term_perm_header": "PERMISO REQUERIDO PARA EJECUTAR EN TERMINAL",
     "term_perm_denied": "Ejecución en terminal rechazada por el usuario.",
     "term_used_status": "Estado",
     "term_triage_manual": "⚠ CONTRASEÑA / ADMIN REQUERIDO: Este comando debe ser ejecutado directamente por el usuario.",
     "term_triage_autofix": "↻ Error detectado — DocMind está analizando cómo corregirlo...",
     "ask_user_header": "PREGUNTA DE DOCMIND / SISTEMA OBJETIVO",
     "ask_user_prompt": "Su elección (número o texto, predeterminado={default}): ",
     "term_perm_shell": "Shell / Entorno",
     "term_perm_cwd": "Carpeta de trabajo",
     "term_perm_code": "CÓDIGO A EJECUTAR",
     "term_perm_prompt": "¿Permite ejecutar este comando en su computadora? [S]í / [N]o: ",
     "term_perm_reprompt": "Escriba 's' (sí) o 'n' (no): ",
     "term_used_header": "TERMINAL UTILIZADA",
     "term_used_code": "CÓDIGO UTILIZADO",
     "term_used_shell": "Shell / Entorno",
     "term_used_cwd": "Carpeta de trabajo",
     "term_used_ok": "Completado (Código: {code}, {elapsed:.2f}s)",
     "term_used_err": "Error / Código: {code} ({elapsed:.2f}s)",
     "term_used_output": "Salida",
     "conn_auto_heal": "Corte de conexión detectado; reconectando automáticamente ({attempt}/{max_attempts})...",
   },
   "fr": {
     "startup_authority_warn": (
       "⚠ AVERTISSEMENT : CET AGENT DISPOSE D'UN ACCÈS COMPLET À VOTRE ORDINATEUR — Il peut voir, ouvrir "
       "et modifier tous les fichiers/dossiers et exécuter du code terminal (avec votre autorisation). "
       "Utilisez avec prudence ; aucune responsabilité acceptée."
     ),
     "term_perm_title": "AUTORISATION D'EXÉCUTION TERMINAL REQUISE",
     "term_perm_header": "AUTORISATION D'EXÉCUTION TERMINAL REQUISE",
     "term_perm_denied": "Exécution dans le terminal refusée par l'utilisateur.",
     "term_used_status": "Statut",
     "term_triage_manual": "⚠ MOT DE PASSE / ADMIN REQUIS : Cette commande doit être exécutée par l'utilisateur.",
     "term_triage_autofix": "↻ Erreur détectée — DocMind analyse une correction...",
     "ask_user_header": "QUESTION DOCMIND / SYSTÈME CIBLE",
     "ask_user_prompt": "Votre choix (numéro ou texte, défaut={default}) : ",
     "term_perm_shell": "Shell / Environnement",
     "term_perm_cwd": "Dossier de travail",
     "term_perm_code": "CODE À EXÉCUTER",
     "term_perm_prompt": "Autoriser l'exécution de cette commande sur votre ordinateur ? [O]ui / [N]on : ",
     "term_perm_reprompt": "Veuillez saisir 'o' (oui) ou 'n' (non) : ",
     "term_used_header": "TERMINAL UTILISÉ",
     "term_used_code": "CODE UTILISÉ",
     "term_used_shell": "Shell / Environnement",
     "term_used_cwd": "Dossier de travail",
     "term_used_ok": "Réussi (Code : {code}, {elapsed:.2f}s)",
     "term_used_err": "Erreur / Code : {code} ({elapsed:.2f}s)",
     "term_used_output": "Sortie",
     "conn_auto_heal": "Coupure réseau détectée ; reconnexion automatique ({attempt}/{max_attempts})...",
   },
   "ru": {
     "startup_authority_warn": (
       "⚠ ВНИМАНИЕ: АГЕНТ ИМЕЕТ ПОЛНЫЙ ДОСТУП К КОМПЬЮТЕРУ — Может просматривать, открывать и изменять "
       "любые диски, папки и файлы, а также выполнять команды терминала (с вашего разрешения). "
       "Используйте осторожно; ответственность не принимается."
     ),
     "term_perm_title": "ТРЕБУЕТСЯ РАЗРЕШЕНИЕ НА ВЫПОЛНЕНИЕ КОДА В ТЕРМИНАЛЕ",
     "term_perm_header": "ТРЕБУЕТСЯ РАЗРЕШЕНИЕ НА ВЫПОЛНЕНИЕ КОДА В ТЕРМИНАЛЕ",
     "term_perm_denied": "Выполнение команды отклонено пользователем.",
     "term_used_status": "Статус",
     "term_triage_manual": "⚠ ТРЕБУЕТСЯ ПАРОЛЬ / ПРАВА АДМИНИСТРАТОРА: Эту команду должен выполнить сам пользователь.",
     "term_triage_autofix": "↻ Обнаружена ошибка — DocMind анализирует способ исправления...",
     "ask_user_header": "ВОПРОС DOCMIND / ВЫБОР СИСТЕМЫ",
     "ask_user_prompt": "Ваш выбор (номер или текст, по умолчанию={default}): ",
     "term_perm_shell": "Оболочка / Среда",
     "term_perm_cwd": "Рабочая папка",
     "term_perm_code": "КОД ДЛЯ ВЫПОЛНЕНИЯ",
     "term_perm_prompt": "Разрешить выполнение этой команды на вашем компьютере? [Д]а / [Н]ет: ",
     "term_perm_reprompt": "Введите 'y'/'д' (да) или 'n'/'н' (нет): ",
     "term_used_header": "ИСПОЛЬЗОВАН ТЕРМИНАЛ",
     "term_used_code": "ИСПОЛЬЗОВАННЫЙ КОД",
     "term_used_shell": "Оболочка / Среда",
     "term_used_cwd": "Рабочая папка",
     "term_used_ok": "Успешно (Код выхода: {code}, {elapsed:.2f}с)",
     "term_used_err": "Ошибка / Код выхода: {code} ({elapsed:.2f}с)",
     "term_used_output": "Вывод",
     "conn_auto_heal": "Обрыв соединения; автоматическое переподключение ({attempt}/{max_attempts})...",
   },
 }
 for _language, _wording in _UNIVERSAL_AGENT_WORDING.items():
   TRANSLATIONS[_language].update(_wording)
 return locals()
_dm_install('docmind.i18n.locales', _dm_module_01, False)

# ===== docmind/i18n/__init__.py (included source) =====
def _dm_module_02():
 """
 DocMind Internationalization (i18n) Engine
 Safe, zero-crash translation lookup with fallback chain: active_lang -> tr -> en -> key.
 """
 from typing import Any
 from docmind.i18n.locales import LANGUAGE_CHOICES, TRANSLATIONS
 class Translator:
   def __init__(self, lang: str = "tr") -> None:
     self._lang = lang if lang in TRANSLATIONS else "tr"
   @property
   def lang(self) -> str:
     return self._lang
   def set_lang(self, lang: str) -> str:
     code = (lang or "").strip().lower()
     if code in TRANSLATIONS:
       self._lang = code
     return self._lang
   def get(self, key: str, **kwargs: Any) -> str:
     template = (
       TRANSLATIONS.get(self._lang, {}).get(key)
       or TRANSLATIONS.get("tr", {}).get(key)
       or TRANSLATIONS.get("en", {}).get(key)
       or key
     )
     if kwargs:
       try:
         return template.format(**kwargs)
       except Exception:
         safe = template
         for k, v in kwargs.items():
           safe = safe.replace("{" + str(k) + "}", str(v))
         return safe
     return template
 i18n = Translator("tr")
 def t(key: str, **kwargs: Any) -> str:
   return i18n.get(key, **kwargs)
 __all__ = ["Translator", "i18n", "t", "LANGUAGE_CHOICES", "TRANSLATIONS"]
 return locals()
_dm_install('docmind.i18n', _dm_module_02, True)

# ===== docmind/config.py (included source) =====
def _dm_module_03():
 """
 DocMind Configuration & Session Persistence Manager
 Fault-tolerant JSON config with multi-provider API key memory and secure permissions.
 """
 import json
 import os
 import shutil
 import stat
 import tempfile
 from dataclasses import dataclass, field, asdict
 from pathlib import Path
 from typing import Any, Dict, List, Optional
 from docmind.i18n import i18n
 @dataclass(frozen=True)
 class ProviderSpec:
   id: str
   name: str
   protocol: str
   default_base_url: str
   models: List[str]
   env_vars: List[str]
   key_optional: bool = False
   context_window: int = 128_000
 PROVIDERS: List[ProviderSpec] = [
   ProviderSpec(
     id="anthropic",
     name="Anthropic (Claude)",
     protocol="anthropic",
     default_base_url="https://api.anthropic.com/v1",
     models=[
       "claude-sonnet-5-5",
       "claude-haiku-5-5",
       "claude-opus-5-5",
       "claude-sonnet-4-5-20250929",
     ],
     env_vars=["ANTHROPIC_API_KEY"],
     context_window=200_000,
   ),
   ProviderSpec(
     id="openai",
     name="OpenAI (ChatGPT)",
     protocol="openai",
     default_base_url="https://api.openai.com/v1",
     models=[
       "gpt-5.4-mini",
       "gpt-5.6-terra",
       "gpt-5.6-sol",
       "gpt-4.1-mini",
     ],
     env_vars=["OPENAI_API_KEY"],
     context_window=128_000,
   ),
   ProviderSpec(
     id="gemini",
     name="Google Gemini",
     protocol="gemini",
     default_base_url="https://generativelanguage.googleapis.com/v1beta",
     models=[
       "gemini-3.5-flash-lite",
       "gemini-3.8-flash",
       "gemini-3.6-flash",
       "gemini-2.5-flash",
     ],
     env_vars=["GEMINI_API_KEY", "GOOGLE_API_KEY"],
     context_window=1_000_000,
   ),
   ProviderSpec(
     id="groq",
     name="Groq (Ultra-Fast)",
     protocol="openai",
     default_base_url="https://api.groq.com/openai/v1",
     models=[
       "openai/gpt-oss-120b",
       "openai/gpt-oss-20b",
       "qwen/qwen3.8-27b",
     ],
     env_vars=["GROQ_API_KEY"],
     context_window=128_000,
   ),
   ProviderSpec(
     id="openrouter",
     name="OpenRouter (Multi-Model)",
     protocol="openai",
     default_base_url="https://openrouter.ai/api/v1",
     models=[
       "anthropic/claude-sonnet-5.5",
       "google/gemini-3.8-flash",
       "openai/gpt-5.4-mini",
       "deepseek/deepseek-chat",
     ],
     env_vars=["OPENROUTER_API_KEY"],
     context_window=128_000,
   ),
   ProviderSpec(
     id="deepseek",
     name="DeepSeek AI",
     protocol="openai",
     default_base_url="https://api.deepseek.com",
     models=[
       "deepseek-flash",
       "deepseek-v4-pro",
       "deepseek-chat",
       "deepseek-reasoner",
     ],
     env_vars=["DEEPSEEK_API_KEY"],
     context_window=64_000,
   ),
   ProviderSpec(
     id="custom",
     name="Custom / Local API (Ollama, LM Studio, vLLM)",
     protocol="openai",
     default_base_url="http://localhost:11434/v1",
     models=[
       "qwen2.5-coder:14b",
       "llama3.2",
       "deepseek-r1:14b",
     ],
     env_vars=["CUSTOM_API_KEY"],
     key_optional=True,
     context_window=64_000,
   ),
 ]
 PROVIDER_MAP: Dict[str, ProviderSpec] = {p.id: p for p in PROVIDERS}
 def get_provider_spec(provider_id: str) -> ProviderSpec:
   return PROVIDER_MAP.get(provider_id, PROVIDERS[0])
 def clean_api_key(raw: str) -> str:
   """Strip accidental quotes, whitespace, or 'Bearer ' prefixes from pasted keys."""
   if not raw:
     return ""
   cleaned = str(raw).strip()
   for _ in range(4):
     value = cleaned.strip().strip("\"'").strip()
     if len(value) > 6 and value[:6].lower() == "bearer" and value[6].isspace():
       value = value[6:].strip()
     if value == cleaned:
       break
     cleaned = value
   return cleaned
 @dataclass
 class DocMindConfig:
   language: str = "tr"
   provider: str = "anthropic"
   model: str = "claude-sonnet-5-5"
   api_keys: Dict[str, str] = field(default_factory=dict)
   base_urls: Dict[str, str] = field(default_factory=dict)
   permission_mode: str = "smart"
   max_steps_per_turn: int = 65
   max_output_tokens: int = 12288
   reasoning_effort: str = "high"
   temperature: float = 0.2
   token_warning_limit: int = 0
   price_overrides: Dict[str, List[float]] = field(default_factory=dict)
   context_overrides: Dict[str, int] = field(default_factory=dict)
   setup_completed: bool = False
   def get_api_key(self, provider_id: Optional[str] = None) -> str:
     pid = provider_id or self.provider
     stored = clean_api_key(self.api_keys.get(pid, ""))
     if stored:
       return stored
     universal = clean_api_key(os.environ.get("DOCMIND_API_KEY", ""))
     if universal:
       return universal
     spec = get_provider_spec(pid)
     for env_name in spec.env_vars:
       val = clean_api_key(os.environ.get(env_name, ""))
       if val:
         return val
     return ""
   def set_api_key(self, key: str, provider_id: Optional[str] = None) -> None:
     pid = provider_id or self.provider
     self.api_keys[pid] = clean_api_key(key)
   def get_base_url(self, provider_id: Optional[str] = None) -> str:
     pid = provider_id or self.provider
     custom_url = self.base_urls.get(pid, "").strip()
     if custom_url:
       return custom_url.rstrip("/")
     return get_provider_spec(pid).default_base_url.rstrip("/")
   def set_base_url(self, url: str, provider_id: Optional[str] = None) -> None:
     pid = provider_id or self.provider
     if url and url.strip():
       self.base_urls[pid] = url.strip().rstrip("/")
   def has_valid_credentials(self) -> bool:
     spec = get_provider_spec(self.provider)
     if spec.key_optional:
       return True
     return bool(self.get_api_key(self.provider))
 class ConfigManager:
   def __init__(self, home_dir: Optional[Path] = None) -> None:
     env_home = os.environ.get("DOCMIND_HOME", "").strip()
     if home_dir is not None:
       self.home_dir = Path(home_dir)
     elif env_home:
       self.home_dir = Path(env_home).expanduser()
     else:
       self.home_dir = Path.home() / ".docmind-single"
     self.config_path = self.home_dir / "config.json"
     self.sessions_dir = self.home_dir / "sessions"
     self.logs_dir = self.home_dir / "logs"
     self.ensure_dirs()
     self.config = self.load()
   def ensure_dirs(self) -> None:
     for d in (self.home_dir, self.sessions_dir, self.logs_dir):
       try:
         d.mkdir(mode=0o700, parents=True, exist_ok=True)
         if os.name != "nt" and not d.is_symlink():
           os.chmod(d, 0o700)
       except OSError:
         pass
   def load(self) -> DocMindConfig:
     if not self.config_path.exists():
       cfg = DocMindConfig()
       i18n.set_lang(cfg.language)
       return cfg
     try:
       raw = self.config_path.read_text(encoding="utf-8")
       data: Dict[str, Any] = json.loads(raw)
       valid_fields = {f for f in DocMindConfig.__dataclass_fields__}
       filtered = {k: v for k, v in data.items() if k in valid_fields}
       cfg = DocMindConfig(**filtered)
       if cfg.provider not in PROVIDER_MAP:
         cfg.provider = "anthropic"
       if cfg.permission_mode not in ("smart", "auto"):
         cfg.permission_mode = "smart"
       if cfg.reasoning_effort not in ("max", "high", "medium", "low", "default"):
         cfg.reasoning_effort = "high"
       i18n.set_lang(cfg.language)
       return cfg
     except Exception:
       try:
         backup = self.config_path.with_suffix(".json.bak")
         shutil.copy2(self.config_path, backup)
         if os.name != "nt":
           os.chmod(backup, 0o600)
       except Exception:
         pass
       cfg = DocMindConfig()
       i18n.set_lang(cfg.language)
       return cfg
   def save(self, cfg: Optional[DocMindConfig] = None) -> bool:
     if cfg is not None:
       self.config = cfg
     i18n.set_lang(self.config.language)
     self.ensure_dirs()
     tmp_name = None
     try:
       fd, tmp_name = tempfile.mkstemp(prefix=".config-", suffix=".tmp", dir=str(self.home_dir))
       with os.fdopen(fd, "w", encoding="utf-8") as f:
         json.dump(asdict(self.config), f, indent=2, ensure_ascii=False)
         f.flush()
         os.fsync(f.fileno())
       os.replace(tmp_name, self.config_path)
       if os.name != "nt":
         os.chmod(self.config_path, 0o600)
       return True
     except (OSError, TypeError, ValueError):
       return False
     finally:
       if tmp_name:
         try:
           os.unlink(tmp_name)
         except FileNotFoundError:
           pass
         except OSError:
           pass
   def log_error(self, context: str, detail: str) -> None:
     """Append a redacted diagnostic; do not intentionally log configured keys."""
     try:
       from datetime import datetime
       from docmind.core.errors import mask_secrets
       self.ensure_dirs()
       safe = str(detail)
       secrets = list(self.config.api_keys.values())
       secrets += [os.environ.get("DOCMIND_API_KEY", "")]
       for spec in PROVIDERS:
         secrets.extend(os.environ.get(var, "") for var in spec.env_vars)
       for secret in sorted({clean_api_key(x) for x in secrets if x}, key=len, reverse=True):
         if secret:
           safe = safe.replace(secret, "[REDACTED]")
       safe = mask_secrets(safe).replace("\n", " ").replace("\r", " ")
       log_file = self.logs_dir / "docmind.log"
       ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
       if hasattr(os, "O_NOFOLLOW"):
         flags |= os.O_NOFOLLOW
       fd = os.open(str(log_file), flags, 0o600)
       with os.fdopen(fd, "a", encoding="utf-8") as fh:
         fh.write(f"[{ts}] [{context}] {safe}\n")
       if os.name != "nt":
         os.chmod(log_file, 0o600)
     except Exception:
       pass
 return locals()
_dm_install('docmind.config', _dm_module_03, False)

# ===== docmind/core/errors.py (included source) =====
def _dm_module_04():
 """
 DocMind Universal Error Classifier, Token/Quota Alerting & Resilience Engine.
 Guarantees that EVERY API, token, network, file, or runtime error produces a clear
 localized alert box and NEVER crashes the application.
 """
 import json
 import math
 import random
 import re
 from datetime import datetime, timezone
 from email.utils import parsedate_to_datetime
 from dataclasses import dataclass
 from enum import Enum
 from typing import Any, Optional, Tuple
 from docmind.i18n import t
 class ErrorCategory(str, Enum):
   QUOTA_EXHAUSTED = "quota_exhausted"
   RATE_LIMITED = "rate_limited"
   REQUEST_TOO_LARGE = "request_too_large"
   AUTH_INVALID = "auth_invalid"
   EDGE_BLOCKED = "edge_blocked"
   ACCESS_DENIED = "access_denied"
   CONTEXT_OVERFLOW = "context_overflow"
   MODEL_UNAVAILABLE = "model_unavailable"
   SERVER_OVERLOAD = "server_overload"
   NETWORK_ERROR = "network_error"
   TOOL_ERROR = "tool_error"
   UNKNOWN_ERROR = "unknown_error"
 @dataclass
 class DocMindAlert:
   category: ErrorCategory
   title: str
   description: str
   raw_detail: str
   status_code: Optional[int] = None
   retry_after: Optional[float] = None
   auto_retryable: bool = False
   suggest_key_change: bool = False
   suggest_model_change: bool = False
   suggest_compact: bool = False
   retry_exhausted: bool = False
 class DocMindAPIException(Exception):
   """Structured exception raised by provider adapters and caught by the resilience engine."""
   def __init__(
     self,
     message: str,
     status_code: Optional[int] = None,
     response_body: str = "",
     retry_after: Optional[float] = None,
     provider_name: str = "AI",
     model_name: str = "",
   ) -> None:
     super().__init__(message)
     self.message = message
     self.status_code = status_code
     self.response_body = response_body
     self.retry_after = retry_after
     self.provider_name = provider_name
     self.model_name = model_name
 def mask_secrets(text: str) -> str:
   """Mask API keys if an upstream error message ever echoes them."""
   if not text:
     return ""
   masked = re.sub(r"(sk-[a-zA-Z0-9_\-]{6})[a-zA-Z0-9_\-]{8,}", r"\1***", text)
   masked = re.sub(r"(AIza[a-zA-Z0-9_\-]{5})[a-zA-Z0-9_\-]{8,}", r"\1***", masked)
   masked = re.sub(r"(gsk_[a-zA-Z0-9_\-]{5})[a-zA-Z0-9_\-]{8,}", r"\1***", masked)
   return masked
 def extract_api_error_message(body: str, fallback: str = "") -> Tuple[str, str]:
   """
     Extract (human_message, error_code_or_type) from OpenAI, Anthropic, Gemini,
     OpenRouter, Groq, or DeepSeek JSON error payloads.
     """
   if not body:
     return (mask_secrets(fallback or "Unknown API error"), "")
   try:
     parsed: Any = json.loads(body)
     if isinstance(parsed, list) and parsed:
       parsed = parsed[0]
     if isinstance(parsed, dict):
       err = parsed.get("error")
       if isinstance(err, dict):
         msg = str(err.get("message") or err.get("status") or fallback)
         code = str(err.get("code") or err.get("type") or err.get("status") or "")
         metadata = err.get("metadata")
         if isinstance(metadata, dict) and metadata.get("raw"):
           msg = f"{msg} ({metadata.get('raw')})"
         return (mask_secrets(msg), code.lower())
       if isinstance(err, str):
         return (mask_secrets(err), str(parsed.get("type", "")).lower())
       if "message" in parsed:
         return (mask_secrets(str(parsed["message"])), str(parsed.get("code", "")).lower())
   except Exception:
     pass
   clean = body.strip()
   if len(clean) > 400:
     clean = clean[:400] + "..."
   return (mask_secrets(clean or fallback), "")
 QUOTA_KEYWORDS = (
   "insufficient_quota",
   "exceeded your current quota",
   "credit balance is too low",
   "insufficient credits",
   "insufficient balance",
   "billing_hard_limit",
   "billing_not_active",
   "out of credits",
   "payment required",
   "spend limit",
   "monthly limit",
   "account balance",
   "requests per day",
   "tokens per day",
   "daily quota",
   "limit: 0",
   "check your plan and billing",
 )
 CONTEXT_KEYWORDS = (
   "context_length_exceeded",
   "maximum context length",
   "prompt is too long",
   "input token count",
   "reduce the length",
   "too many tokens",
   "max_tokens_exceeded",
   "request too large",
   "context window",
 )
 AUTH_KEYWORDS = (
   "invalid_api_key",
   "authentication_error",
   "api_key_invalid",
   "api key not valid",
   "incorrect api key",
   "unauthorized",
   "permission_denied",
   "invalid x-api-key",
   "invalid authentication",
 )
 MODEL_KEYWORDS = (
   "model_not_found",
   "does not exist or you do not have access",
   "not found for api version",
   "model is not supported",
   "unknown model",
   "decommissioned",
 )
 def parse_retry_after(value: Any, now: Optional[datetime] = None) -> Optional[float]:
   """Parse RFC Retry-After seconds or HTTP-date, rejecting invalid/unsafe values."""
   if value is None:
     return None
   text = str(value).strip()
   if not text:
     return None
   try:
     seconds = float(text)
     if math.isfinite(seconds) and seconds >= 0:
       return seconds
     return None
   except (ValueError, OverflowError):
     pass
   try:
     future = parsedate_to_datetime(text)
     if future.tzinfo is None:
       future = future.replace(tzinfo=timezone.utc)
     current = now or datetime.now(timezone.utc)
     if current.tzinfo is None:
       current = current.replace(tzinfo=timezone.utc)
     return max(0.0, (future - current).total_seconds())
   except (TypeError, ValueError, IndexError, OverflowError):
     return None
 def retry_delay(attempt: int, minimum: Optional[float] = None, max_wait: float = 120.0) -> Optional[float]:
   """Fast-recovering exponential backoff with jitter; respects Retry-After."""
   floor = parse_retry_after(minimum)
   if floor is not None and floor > max_wait:
     return None
   schedule = (1.0, 2.0, 3.8, 7.2, 14.0, 25.0, 40.0)
   idx = min(max(0, attempt - 1), len(schedule) - 1)
   base = schedule[idx]
   delay = base + random.uniform(0.05, min(0.85, base * 0.2))
   return max(delay, floor or 0.0)
 def request_token_ceiling(detail: str, status: Optional[int]) -> Optional[Tuple[int, int]]:
   """Parse an explicit per-request TPM/OTPM ceiling, not a transient 429.

     A request with Requested > Limit can never fit by waiting. Unrecognized
     formats remain unknown; we never guess a provider's account limits.
     """
   text = str(detail or "").lower()
   if status not in (413, 429) or not any(x in text for x in ("tokens per minute", "tokens per min", "(tpm)", "(otpm)")):
     return None
   found_limit = re.search(r"\blimit\s*[:=]?\s*([0-9][0-9,]*)", text)
   found_requested = re.search(r"\brequested\s*[:=]?\s*([0-9][0-9,]*)", text)
   if not found_limit or not found_requested:
     return None
   try:
     limit = int(found_limit.group(1).replace(",", ""))
     requested = int(found_requested.group(1).replace(",", ""))
   except ValueError:
     return None
   return (limit, requested) if 0 < limit < requested <= 1_000_000_000 else None
 def classify_exception(
   exc: BaseException,
   provider_name: str = "AI",
   model_name: str = "",
 ) -> DocMindAlert:
   """
     Convert ANY exception (DocMindAPIException, network error, OS error, etc.)
     into a localized, actionable DocMindAlert.
     """
   if isinstance(exc, DocMindAPIException):
     status = exc.status_code
     prov = exc.provider_name or provider_name
     mod = exc.model_name or model_name
     msg, err_code = extract_api_error_message(exc.response_body, exc.message)
     combined = f"{msg} {err_code}".lower()
     edge_detail = (str(exc.message) + " " + str(exc.response_body or "")).lower()
     edge_1010 = ("browser_signature_banned" in edge_detail or
           bool(re.search(r"\berror[\s_\-]*code[\s\"':=]*1010\b", edge_detail)))
     if status == 403 and edge_1010:
       return DocMindAlert(
         category=ErrorCategory.EDGE_BLOCKED,
         title=t("err_edge_block_title"),
         description=t("err_edge_block_desc", provider=prov),
         raw_detail=msg, status_code=status, auto_retryable=False,
         suggest_key_change=False,
       )
     if request_token_ceiling(msg + " " + (exc.response_body or ""), status):
       return DocMindAlert(
         category=ErrorCategory.REQUEST_TOO_LARGE,
         title=t("err_request_budget_title"),
         description=t("err_request_budget_desc", provider=prov, detail=msg),
         raw_detail=msg, status_code=status, auto_retryable=False,
         suggest_model_change=True,
       )
     if (status == 402 or any(k in combined for k in QUOTA_KEYWORDS) or
         "enforced_spend_limit_reached" in str(exc.response_body or "").lower()):
       return DocMindAlert(
         category=ErrorCategory.QUOTA_EXHAUSTED,
         title=t("err_quota_title"),
         description=t("err_quota_desc", provider=prov, detail=msg),
         raw_detail=msg,
         status_code=status,
         auto_retryable=False,
         suggest_key_change=True,
       )
     explicit_auth = any(k in combined for k in AUTH_KEYWORDS if k != "permission_denied")
     if status == 403 and not explicit_auth and not any(k in combined for k in MODEL_KEYWORDS):
       return DocMindAlert(
         category=ErrorCategory.ACCESS_DENIED,
         title=t("err_access_denied_title"),
         description=t("err_access_denied_desc", provider=prov, detail=msg),
         raw_detail=msg, status_code=status, auto_retryable=False,
       )
     if status in (401, 403) or any(k in combined for k in AUTH_KEYWORDS):
       if status == 403 and any(k in combined for k in MODEL_KEYWORDS):
         return DocMindAlert(
           category=ErrorCategory.MODEL_UNAVAILABLE,
           title=t("err_model_title"),
           description=t("err_model_desc", model=mod, detail=msg),
           raw_detail=msg,
           status_code=status,
           suggest_model_change=True,
         )
       return DocMindAlert(
         category=ErrorCategory.AUTH_INVALID,
         title=t("err_auth_title"),
         description=t("err_auth_desc", provider=prov, detail=msg),
         raw_detail=msg,
         status_code=status,
         suggest_key_change=True,
       )
     if (status in (400, 413) or status is None) and any(k in combined for k in CONTEXT_KEYWORDS):
       return DocMindAlert(
         category=ErrorCategory.CONTEXT_OVERFLOW,
         title=t("err_context_title"),
         description=t("err_context_desc", detail=msg),
         raw_detail=msg,
         status_code=status,
         suggest_compact=True,
       )
     if status == 404 or any(k in combined for k in MODEL_KEYWORDS):
       return DocMindAlert(
         category=ErrorCategory.MODEL_UNAVAILABLE,
         title=t("err_model_title"),
         description=t("err_model_desc", model=mod, detail=msg),
         raw_detail=msg,
         status_code=status,
         suggest_model_change=True,
       )
     if status == 429 or "rate_limit" in combined or "resource_exhausted" in combined or "too many requests" in combined:
       retry_sec = parse_retry_after(exc.retry_after)
       if retry_sec is None:
         detail = combined + " " + str(exc.response_body or "").lower()
         m = re.search(r'retry(?: in| after)\s+([0-9]+(?:\.[0-9]+)?)\s*s', detail)
         if not m:
           m = re.search(r'["\']retrydelay["\']\s*:\s*["\']([0-9]+(?:\.[0-9]+)?)s', detail)
         retry_sec = float(m.group(1)) if m else None
       return DocMindAlert(
         category=ErrorCategory.RATE_LIMITED,
         title=t("err_rate_title"),
         description=t("err_rate_desc", provider=prov, detail=msg),
         raw_detail=msg,
         status_code=status,
         retry_after=retry_sec if retry_sec is not None else 5.0,
         auto_retryable=True,
         suggest_key_change=False,
       )
     if (status and status >= 500) or "overloaded" in combined or "server_error" in combined:
       return DocMindAlert(
         category=ErrorCategory.SERVER_OVERLOAD,
         title=t("err_server_title"),
         description=t("err_server_desc", provider=prov, detail=msg),
         raw_detail=msg,
         status_code=status,
         retry_after=parse_retry_after(exc.retry_after) if exc.retry_after is not None else 3.0,
         auto_retryable=True,
       )
     transient_markers = (
       "stream ended before", "incomplete streamed", "incompleteread",
       "remotedisconnected", "connection reset", "connection aborted",
       "broken pipe", "timed out", "timeout", "unexpected eof",
       "eof occurred in violation", "ssl", "bad status line", "urlopen error",
       "temporarily unavailable", "network is unreachable", "bad gateway",
     )
     if status is None or status in (408, 425, 499) or any(m in combined for m in transient_markers):
       return DocMindAlert(
         category=ErrorCategory.NETWORK_ERROR,
         title=t("err_network_title"),
         description=t("err_network_desc", provider=prov, detail=msg),
         raw_detail=msg,
         status_code=status,
         retry_after=1.0,
         auto_retryable=True,
       )
     return DocMindAlert(
       category=ErrorCategory.UNKNOWN_ERROR,
       title=t("err_unknown_title"),
       description=t("err_unknown_desc", detail=f"[HTTP {status}] {msg}"),
       raw_detail=msg,
       status_code=status,
     )
   err_name = type(exc).__name__
   detail = mask_secrets(f"{err_name}: {exc}")
   if isinstance(exc, (ConnectionError, TimeoutError)) or any(
     w in detail.lower() for w in (
       "urlopen error", "timed out", "timeout", "name or service not known",
       "ssl", "connection", "incompleteread", "remotedisconnected",
       "broken pipe", "eof", "reset by peer", "temporary failure",
     )
   ):
     return DocMindAlert(
       category=ErrorCategory.NETWORK_ERROR,
       title=t("err_network_title"),
       description=t("err_network_desc", provider=provider_name, detail=detail),
       raw_detail=detail,
       auto_retryable=True,
     )
   if isinstance(exc, (OSError, PermissionError, FileNotFoundError)):
     return DocMindAlert(
       category=ErrorCategory.TOOL_ERROR,
       title=t("err_tool_title"),
       description=t("err_tool_desc", detail=detail),
       raw_detail=detail,
     )
   return DocMindAlert(
     category=ErrorCategory.UNKNOWN_ERROR,
     title=t("err_unknown_title"),
     description=t("err_unknown_desc", detail=detail),
     raw_detail=detail,
   )
 return locals()
_dm_install('docmind.core.errors', _dm_module_04, False)

# ===== docmind/tools/backup.py (included source) =====
def _dm_module_05():
 """
 DocMind Reversible File Snapshot Manager (/undo & AI self-rollback support)
 """
 from dataclasses import dataclass
 from datetime import datetime
 from pathlib import Path
 from typing import List, Optional, Tuple
 @dataclass
 class FileSnapshot:
   path: Path
   existed: bool
   previous_bytes: Optional[bytes]
   timestamp: str = ""
 class UndoManager:
   def __init__(self, max_history: int = 50) -> None:
     self._stack: List[FileSnapshot] = []
     self._max_history = max_history
   def record_before_modify(self, path: Path) -> None:
     try:
       target = path.resolve()
       stamp = datetime.now().strftime("%H:%M:%S")
       if target.exists() and target.is_file():
         if target.stat().st_size <= 10 * 1024 * 1024:
           data = target.read_bytes()
           self._push(FileSnapshot(path=target, existed=True, previous_bytes=data, timestamp=stamp))
       elif not target.exists():
         self._push(FileSnapshot(path=target, existed=False, previous_bytes=None, timestamp=stamp))
     except Exception:
       pass
   def _push(self, snap: FileSnapshot) -> None:
     self._stack.append(snap)
     if len(self._stack) > self._max_history:
       self._stack.pop(0)
   def _apply_snapshot(self, snap: FileSnapshot) -> Tuple[Path, str]:
     if snap.existed and snap.previous_bytes is not None:
       snap.path.parent.mkdir(parents=True, exist_ok=True)
       snap.path.write_bytes(snap.previous_bytes)
       return snap.path, "restored previous content"
     if not snap.existed and snap.path.exists() and snap.path.is_file():
       snap.path.unlink()
       return snap.path, "removed newly created file"
     return snap.path, "restored state"
   def undo_last(self) -> Optional[Path]:
     if not self._stack:
       return None
     snap = self._stack.pop()
     restored_path, _ = self._apply_snapshot(snap)
     return restored_path
   def undo_for_path(self, target: Path) -> Optional[Tuple[Path, str]]:
     resolved = target.resolve()
     for idx in range(len(self._stack) - 1, -1, -1):
       if self._stack[idx].path == resolved:
         snap = self._stack.pop(idx)
         return self._apply_snapshot(snap)
     return None
   def recent_paths(self, limit: int = 10) -> List[str]:
     out: List[str] = []
     for snap in reversed(self._stack[-limit:]):
       kind = "modified" if snap.existed else "created"
       out.append(f"{snap.timestamp} [{kind}] {snap.path}")
     return out
 return locals()
_dm_install('docmind.tools.backup', _dm_module_05, False)

# ===== docmind/tools/filesystem.py (included source) =====
def _dm_module_06():
 """
 DocMind Universal Cross-Platform Filesystem & Document Tools (Windows / Linux / macOS)
 Full computer-wide file reading (text, UTF-16, CP1254, DOCX, XLSX, PPTX, ODT/ODS/ODP,
 PDF, SQLite, ZIP/TAR, binary metadata), atomic writing, surgical editing with UndoManager,
 directory navigation, drive & special-folder discovery, and archive management.
 """
 import ctypes
 import difflib
 import os
 import posixpath
 import re
 import shutil
 import sqlite3
 import stat
 import string
 import tarfile
 import tempfile
 import xml.etree.ElementTree as ET
 import zipfile
 import zlib
 from pathlib import Path
 from typing import Any, Callable, Dict, List, Optional, Tuple
 from docmind.tools.backup import UndoManager
 ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1254", "cp1252", "latin-1")
 IGNORED_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", ".mypy_cache", ".pytest_cache"}
 def format_size(num_bytes: int) -> str:
   val = float(max(0, num_bytes))
   for unit in ("B", "KB", "MB", "GB", "TB"):
     if val < 1024.0 or unit == "TB":
       return f"{int(val)} {unit}" if unit == "B" else f"{val:.1f} {unit}"
     val /= 1024.0
   return f"{num_bytes} B"
 def _xdg_user_dirs(home: Path) -> Dict[str, Path]:
   out: Dict[str, Path] = {}
   cfg = home / ".config" / "user-dirs.dirs"
   if not cfg.is_file():
     return out
   try:
     text = cfg.read_text(encoding="utf-8", errors="ignore")
     for m in re.finditer(r'^XDG_([A-Z]+)_DIR="([^"]+)"', text, flags=re.MULTILINE):
       key, val = m.group(1).lower(), m.group(2)
       val = val.replace("$HOME", str(home))
       out[key] = Path(val)
   except Exception:
     pass
   return out
 def get_special_folders() -> Dict[str, Path]:
   """Discover real OS special folders across Windows (incl. OneDrive), Linux (incl. XDG), and macOS."""
   home = Path.home()
   folders: Dict[str, Path] = {"home": home, "temp": Path(tempfile.gettempdir())}
   xdg = _xdg_user_dirs(home) if os.name != "nt" else {}
   onedrive = os.environ.get("OneDrive") or os.environ.get("OneDriveConsumer") or os.environ.get("OneDriveCommercial")
   candidates = {
     "desktop": [
       Path(onedrive) / "Desktop" if onedrive else None,
       Path(onedrive) / "Masaüstü" if onedrive else None,
       xdg.get("desktop"),
       home / "Desktop",
       home / "Masaüstü",
     ],
     "downloads": [
       xdg.get("download"),
       home / "Downloads",
       home / "İndirilenler",
       home / "Indirilenler",
     ],
     "documents": [
       Path(onedrive) / "Documents" if onedrive else None,
       Path(onedrive) / "Belgeler" if onedrive else None,
       xdg.get("documents"),
       home / "Documents",
       home / "Belgeler",
     ],
     "pictures": [
       Path(onedrive) / "Pictures" if onedrive else None,
       xdg.get("pictures"),
       home / "Pictures",
       home / "Resimler",
     ],
     "music": [xdg.get("music"), home / "Music", home / "Müzik"],
     "videos": [xdg.get("videos"), home / "Videos", home / "Videolar"],
   }
   for key, opts in candidates.items():
     chosen = None
     for c in opts:
       if c is not None and c.exists():
         chosen = c
         break
     if chosen is None:
       chosen = next((c for c in opts if c is not None), home / key.capitalize())
     folders[key] = chosen
   if os.name == "nt":
     for env_key, name in (("APPDATA", "appdata"), ("LOCALAPPDATA", "localappdata"), ("PROGRAMFILES", "programfiles")):
       val = os.environ.get(env_key)
       if val:
         folders[name] = Path(val)
   return folders
 def list_mounted_roots() -> List[Dict[str, Any]]:
   """Return available drives/roots across Windows (A:..Z:) and Linux/macOS mount points."""
   roots: List[Dict[str, Any]] = []
   if os.name == "nt":
     bitmask = 0
     try:
       bitmask = ctypes.windll.kernel32.GetLogicalDrives()
     except Exception:
       pass
     for idx, letter in enumerate(string.ascii_uppercase):
       drive = f"{letter}:\\"
       present = bool(bitmask & (1 << idx)) if bitmask else os.path.exists(drive)
       if present:
         info: Dict[str, Any] = {"root": drive}
         try:
           usage = shutil.disk_usage(drive)
           info["total_gb"] = round(usage.total / (1024 ** 3), 2)
           info["free_gb"] = round(usage.free / (1024 ** 3), 2)
         except OSError:
           pass
         roots.append(info)
   else:
     seen = set()
     candidates = ["/"]
     for base in ("/mnt", "/media", "/Volumes", "/run/media"):
       p = Path(base)
       if p.is_dir():
         try:
           for child in sorted(p.iterdir()):
             if child.is_dir():
               candidates.append(str(child))
         except OSError:
           pass
     for c in candidates:
       try:
         rp = str(Path(c).resolve())
         if rp in seen and c != "/":
           continue
         seen.add(rp)
         usage = shutil.disk_usage(c)
         roots.append({
           "root": c,
           "total_gb": round(usage.total / (1024 ** 3), 2),
           "free_gb": round(usage.free / (1024 ** 3), 2),
         })
       except OSError:
         continue
   return roots
 _FOLDER_ALIASES = {
   "desktop": "desktop", "masaustu": "desktop", "masaüstü": "desktop",
   "downloads": "downloads", "indirilenler": "downloads", "i̇ndirilenler": "downloads",
   "documents": "documents", "belgeler": "documents", "belgelerim": "documents",
   "pictures": "pictures", "resimler": "pictures",
   "music": "music", "müzik": "music", "muzik": "music",
   "videos": "videos", "videolar": "videos",
   "home": "home", "ev": "home",
   "temp": "temp", "tmp": "temp",
 }
 _TR_NORM_MAP = str.maketrans("şığüöçŞİĞÜÖÇI", "siguocsiguoci")
 def _norm_name(name: str) -> str:
   return name.translate(_TR_NORM_MAP).lower().replace("_", "").replace("-", "").replace(" ", "")
 def suggest_similar_paths(missing_target: Path, cwd: Path, max_suggestions: int = 5) -> List[str]:
   """Find closely named files/folders when an open/read/edit target was not found."""
   wanted_name = missing_target.name
   wanted_norm = _norm_name(wanted_name)
   wanted_stem = _norm_name(missing_target.stem)
   search_dirs: List[Path] = []
   for candidate_dir in (
     missing_target.parent,
     missing_target.parent.parent if missing_target.parent != missing_target else None,
     cwd,
     *get_special_folders().values(),
   ):
     if candidate_dir is not None:
       try:
         rp = candidate_dir.resolve()
         if rp.is_dir() and rp not in search_dirs:
           search_dirs.append(rp)
       except OSError:
         continue
   scored: List[Tuple[float, str]] = []
   seen_paths = set()
   for sdir in search_dirs[:8]:
     try:
       for idx, entry in enumerate(sdir.iterdir()):
         if idx > 400:
           break
         ep = str(entry)
         if ep in seen_paths:
           continue
         seen_paths.add(ep)
         enorm = _norm_name(entry.name)
         estem = _norm_name(entry.stem)
         ratio = max(
           difflib.SequenceMatcher(None, wanted_norm, enorm).ratio(),
           difflib.SequenceMatcher(None, wanted_stem, estem).ratio() if wanted_stem else 0.0,
         )
         if wanted_norm and (wanted_norm in enorm or enorm in wanted_norm):
           ratio = max(ratio, 0.82)
         if ratio >= 0.52:
           scored.append((ratio, ep))
     except OSError:
       continue
   scored.sort(key=lambda item: item[0], reverse=True)
   return [p for _, p in scored[:max_suggestions]]
 def _missing_path_message(prefix: str, target: Path, cwd: Path) -> str:
   suggestions = suggest_similar_paths(target, cwd)
   msg = f"{prefix}: {target}"
   if suggestions:
     msg += "\n[SELF-RECOVERY HINT] Similar existing path(s) found — check if you meant one of these and retry:\n"
     msg += "\n".join(f"  - {s}" for s in suggestions)
   else:
     parent = target.parent
     if parent.exists() and parent.is_dir():
       msg += f"\n[SELF-RECOVERY HINT] Parent directory '{parent}' exists; call list_directory or search_files on it to inspect exact filenames."
     else:
       msg += f"\n[SELF-RECOVERY HINT] Parent directory '{parent}' also does not exist; use search_files or list_system_drives to locate the right path."
   return msg
 def _closest_edit_snippet(content: str, old_text: str) -> str:
   """Locate the closest matching lines in `content` so the agent can immediately fix a failed edit_file."""
   src_lines = content.splitlines()
   needle_lines = [ln.strip() for ln in old_text.splitlines() if ln.strip()]
   if not src_lines or not needle_lines:
     return ""
   first_needle = needle_lines[0]
   best_score = 0.0
   best_idx = 0
   for idx, line in enumerate(src_lines[:4000]):
     score = difflib.SequenceMatcher(None, first_needle, line.strip()).ratio()
     if score > best_score:
       best_score = score
       best_idx = idx
   if best_score < 0.45:
     return ""
   start = max(0, best_idx - 2)
   end = min(len(src_lines), best_idx + max(len(needle_lines), 3) + 2)
   snippet = "\n".join(f"  {i + 1:5d} | {src_lines[i]}" for i in range(start, end))
   return f"\n[SELF-RECOVERY HINT] Closest lines in file (lines {start + 1}-{end}):\n{snippet}"
 def resolve_user_path(raw_path: str, base_cwd: Path) -> Path:
   """Resolve any Windows or Linux path including ~, %ENV%, $ENV, /c/Users/..., and Desktop/Masaüstü aliases."""
   s = (raw_path or ".").strip()
   if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
     s = s[1:-1].strip()
   if not s or s == ".":
     return base_cwd.resolve()
   s = re.sub(r"%([A-Za-z_][A-Za-z0-9_]*)%", lambda m: os.environ.get(m.group(1), m.group(0)), s)
   s = os.path.expandvars(os.path.expanduser(s))
   if os.name == "nt":
     m_drive = re.match(r"^/([a-zA-Z])(/.*)?$", s)
     if m_drive:
       rest = (m_drive.group(2) or "\\").replace("/", "\\")
       s = f"{m_drive.group(1).upper()}:{rest}"
     elif re.match(r"^[a-zA-Z]:$", s):
       s = s + "\\"
   norm_slash = s.replace("\\", "/")
   first_seg, sep, remainder = norm_slash.partition("/")
   alias_key = _FOLDER_ALIASES.get(first_seg.lower())
   if alias_key and not (base_cwd / s).exists():
     special = get_special_folders().get(alias_key)
     if special is not None:
       candidate = special / remainder if (sep and remainder) else special
       return Path(os.path.abspath(str(candidate)))
   p = Path(s)
   if not p.is_absolute():
     p = base_cwd / p
   try:
     return p.resolve()
   except OSError:
     return Path(os.path.abspath(str(p)))
 def read_text_resilient(path: Path) -> Tuple[str, str]:
   """Read text file supporting UTF-8, UTF-8-BOM, UTF-16 LE/BE, Turkish CP1254, and Latin-1."""
   raw = path.read_bytes()
   if not raw:
     return "", "utf-8"
   if raw.startswith(b"\xff\xfe"):
     return raw.decode("utf-16-le", errors="replace"), "utf-16-le"
   if raw.startswith(b"\xfe\xff"):
     return raw.decode("utf-16-be", errors="replace"), "utf-16-be"
   sample = raw[:4096]
   if b"\x00" in sample:
     even_nulls = sum(1 for b in sample[0::2] if b == 0)
     odd_nulls = sum(1 for b in sample[1::2] if b == 0)
     half = max(1, len(sample) // 2)
     if odd_nulls / half > 0.35 and even_nulls / half < 0.05:
       return raw.decode("utf-16-le", errors="replace"), "utf-16-le"
     if even_nulls / half > 0.35 and odd_nulls / half < 0.05:
       return raw.decode("utf-16-be", errors="replace"), "utf-16-be"
     raise ValueError(f"Binary file detected ({format_size(len(raw))}).")
   for enc in ENCODINGS_TO_TRY:
     try:
       return raw.decode(enc), enc
     except UnicodeDecodeError:
       continue
   return raw.decode("utf-8", errors="replace"), "utf-8-replace"
 def _extract_docx(path: Path) -> str:
   with zipfile.ZipFile(path, "r") as zf:
     xml_bytes = zf.read("word/document.xml")
   root = ET.fromstring(xml_bytes)
   paragraphs: List[str] = []
   for p in root.iter():
     if p.tag.endswith("}p"):
       texts = [t_el.text for t_el in p.iter() if t_el.tag.endswith("}t") and t_el.text]
       if texts:
         paragraphs.append("".join(texts))
   return "\n".join(paragraphs) or "(Empty DOCX document)"
 def _extract_xlsx(path: Path) -> str:
   with zipfile.ZipFile(path, "r") as zf:
     shared: List[str] = []
     if "xl/sharedStrings.xml" in zf.namelist():
       s_root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
       for si in s_root.iter():
         if si.tag.endswith("}si"):
           shared.append("".join(t_el.text or "" for t_el in si.iter() if t_el.tag.endswith("}t")))
     sheets = sorted(n for n in zf.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml"))
     out: List[str] = []
     for idx, sh in enumerate(sheets, 1):
       out.append(f"=== Sheet {idx} ({posixpath.basename(sh)}) ===")
       sh_root = ET.fromstring(zf.read(sh))
       rows_count = 0
       for row in sh_root.iter():
         if row.tag.endswith("}row"):
           vals: List[str] = []
           for c in row:
             if not c.tag.endswith("}c"):
               continue
             ctype = c.attrib.get("t", "")
             v_text = ""
             for ch in c:
               if ch.tag.endswith("}v") and ch.text is not None:
                 v_text = ch.text
               elif ch.tag.endswith("}is"):
                 v_text = "".join(t_el.text or "" for t_el in ch.iter() if t_el.tag.endswith("}t"))
             if ctype == "s" and v_text.isdigit() and int(v_text) < len(shared):
               v_text = shared[int(v_text)]
             vals.append(v_text)
           if any(vals):
             out.append("\t".join(vals))
             rows_count += 1
             if rows_count >= 500:
               out.append("... (sheet truncated at 500 rows)")
               break
     return "\n".join(out) or "(Empty XLSX workbook)"
 def _extract_pptx(path: Path) -> str:
   with zipfile.ZipFile(path, "r") as zf:
     slides = sorted(n for n in zf.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
     out: List[str] = []
     for idx, sl in enumerate(slides, 1):
       root = ET.fromstring(zf.read(sl))
       texts = [el.text.strip() for el in root.iter() if el.tag.endswith("}t") and el.text and el.text.strip()]
       out.append(f"=== Slide {idx} ===\n" + ("\n".join(texts) if texts else "(no text)"))
     return "\n\n".join(out) or "(Empty PPTX presentation)"
 def _extract_odf(path: Path) -> str:
   with zipfile.ZipFile(path, "r") as zf:
     root = ET.fromstring(zf.read("content.xml"))
   lines = ["".join(el.itertext()).strip() for el in root.iter() if el.tag.endswith(("}p", "}h"))]
   return "\n".join(ln for ln in lines if ln) or "(Empty OpenDocument file)"
 def _extract_pdf_stdlib(path: Path) -> str:
   raw = path.read_bytes()
   chunks: List[str] = []
   for m in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", raw, flags=re.DOTALL):
     stream_data = m.group(1)
     decomp = None
     for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS):
       try:
         decomp = zlib.decompress(stream_data, wbits)
         break
       except Exception:
         continue
     buf = decomp if decomp is not None else stream_data
     if b"BT" not in buf and b"Tj" not in buf and b"TJ" not in buf:
       continue
     for tm in re.finditer(rb"\(([^()\\]*(?:\\.[^()\\]*)*)\)\s*Tj", buf):
       txt = tm.group(1).replace(b"\\(", b"(").replace(b"\\)", b")").replace(b"\\n", b"\n")
       chunks.append(txt.decode("latin-1", errors="ignore"))
     for arr in re.finditer(rb"\[(.*?)\]\s*TJ", buf, flags=re.DOTALL):
       parts = [
         p.group(1).replace(b"\\(", b"(").replace(b"\\)", b")").decode("latin-1", errors="ignore")
         for p in re.finditer(rb"\(([^()\\]*(?:\\.[^()\\]*)*)\)", arr.group(1))
       ]
       if parts:
         chunks.append("".join(parts))
     if sum(len(c) for c in chunks) > 120_000:
       break
   joined = re.sub(r"[ \t]+", " ", "\n".join(chunks)).strip()
   if joined:
     return f"[PDF Text Extraction ({format_size(len(raw))})]\n{joined}"
   return (
     f"[PDF Binary File ({format_size(len(raw))})]\n"
     "Compressed/CID-encoded or scanned PDF stream could not be decoded purely via stdlib regex. "
     "You can inspect it further via python_eval or system tools if needed."
   )
 def _extract_sqlite(path: Path) -> str:
   uri = f"file:{path.as_posix()}?mode=ro"
   conn = sqlite3.connect(uri, uri=True)
   try:
     cur = conn.cursor()
     tables = cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
     out = [f"[SQLite Database: {path.name} ({len(tables)} tables)]"]
     for tname, tsql in tables[:30]:
       out.append(f"\n--- Table: {tname} ---\nSchema: {tsql}")
       try:
         cnt = cur.execute(f'SELECT COUNT(*) FROM "{tname}"').fetchone()[0]
         rows = cur.execute(f'SELECT * FROM "{tname}" LIMIT 10').fetchall()
         cols = [d[0] for d in cur.description] if cur.description else []
         out.append(f"Rows: {cnt} | Columns: {cols}")
         for r in rows:
           out.append(f"  {r}")
       except Exception as exc:
         out.append(f"  (Preview error: {exc})")
     return "\n".join(out)
   finally:
     conn.close()
 def _extract_archive_listing(path: Path) -> str:
   low = path.name.lower()
   if zipfile.is_zipfile(path):
     with zipfile.ZipFile(path, "r") as zf:
       infos = zf.infolist()
       lines = [f"[ZIP Archive: {path.name} — {len(infos)} entries]"]
       for info in infos[:200]:
         lines.append(f"  {info.filename} ({format_size(info.file_size)})")
       if len(infos) > 200:
         lines.append(f"  ... and {len(infos) - 200} more entries")
       return "\n".join(lines)
   if low.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz")):
     with tarfile.open(path, "r:*") as tf:
       members = tf.getmembers()
       lines = [f"[TAR Archive: {path.name} — {len(members)} entries]"]
       for m in members[:200]:
         lines.append(f"  {m.name} ({format_size(m.size)})")
       if len(members) > 200:
         lines.append(f"  ... and {len(members) - 200} more entries")
       return "\n".join(lines)
   return ""
 def _describe_binary(path: Path) -> str:
   size = path.stat().st_size
   with path.open("rb") as f:
     head = f.read(64)
   kind = "Binary file"
   if head.startswith(b"\x89PNG\r\n\x1a\n") and len(head) >= 24:
     w = int.from_bytes(head[16:20], "big")
     h = int.from_bytes(head[20:24], "big")
     kind = f"PNG Image ({w}x{h} px)"
   elif head.startswith(b"\xff\xd8\xff"):
     kind = "JPEG Image"
   elif head.startswith((b"GIF87a", b"GIF89a")):
     kind = "GIF Image"
   elif head.startswith(b"MZ"):
     kind = "Windows PE Executable / DLL"
   elif head.startswith(b"\x7fELF"):
     kind = "Linux ELF Executable / Shared Library"
   hex_preview = " ".join(f"{b:02x}" for b in head[:32])
   return (
     f"[{kind}]\nPath: {path}\nSize: {format_size(size)} ({size:,} bytes)\n"
     f"Header (32B hex): {hex_preview}\n"
     "(Use open_path to open it in the user's desktop app, or python_eval to process binary bytes.)"
   )
 def _atomic_write_text(target: Path, content: str, encoding: str) -> None:
   previous_mode = None
   if target.exists():
     previous_mode = stat.S_IMODE(target.stat().st_mode)
   target.parent.mkdir(parents=True, exist_ok=True)
   fd, name = tempfile.mkstemp(prefix=".docmind-write-", suffix=".tmp", dir=str(target.parent))
   try:
     with os.fdopen(fd, "w", encoding=encoding, newline="") as stream:
       stream.write(content)
       stream.flush()
       os.fsync(stream.fileno())
     if previous_mode is not None and os.name != "nt":
       os.chmod(name, previous_mode)
     os.replace(name, target)
   finally:
     try:
       os.unlink(name)
     except FileNotFoundError:
       pass
 def tool_read_file(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   raw_path = str(args.get("path", "")).strip()
   if not raw_path:
     return False, "Error: 'path' parameter is required."
   target = resolve_user_path(raw_path, cwd)
   if not target.exists():
     return False, _missing_path_message("File not found", target, cwd)
   if target.is_dir():
     return False, f"Path is a directory, not a file: {target}. Use list_directory instead."
   size = target.stat().st_size
   ext = target.suffix.lower()
   low_name = target.name.lower()
   offset = max(1, int(args.get("offset") or args.get("start_line") or 1))
   if "end_line" in args and args.get("end_line"):
     limit = max(1, min(1500, int(args["end_line"]) - offset + 1))
   else:
     limit = max(1, min(1500, int(args.get("limit", 400) or 400)))
   if size <= 64 * 1024 * 1024:
     try:
       extracted: Optional[str] = None
       fmt_label = ""
       if ext == ".docx":
         extracted, fmt_label = _extract_docx(target), "DOCX"
       elif ext == ".xlsx":
         extracted, fmt_label = _extract_xlsx(target), "XLSX"
       elif ext == ".pptx":
         extracted, fmt_label = _extract_pptx(target), "PPTX"
       elif ext in (".odt", ".ods", ".odp"):
         extracted, fmt_label = _extract_odf(target), ext.upper().lstrip(".")
       elif ext == ".pdf":
         extracted, fmt_label = _extract_pdf_stdlib(target), "PDF"
       elif ext in (".sqlite", ".sqlite3", ".db"):
         extracted, fmt_label = _extract_sqlite(target), "SQLite"
       elif ext in (".zip", ".jar", ".apk", ".whl") or low_name.endswith((".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz")):
         extracted, fmt_label = _extract_archive_listing(target), "Archive"
       if extracted is not None:
         lines = extracted.splitlines()
         total_lines = len(lines)
         end_idx = min(total_lines, offset - 1 + limit)
         selected = lines[offset - 1 : end_idx]
         numbered = [f"{i:5d} | {ln}" for i, ln in enumerate(selected, start=offset)]
         header = f"File: {target} ({fmt_label}, {total_lines} extracted lines, {format_size(size)}) [Lines {offset}-{end_idx}]"
         footer = f"\n... ({total_lines - end_idx} more lines. Pass offset={end_idx + 1} to read further.)" if end_idx < total_lines else ""
         return True, header + "\n" + "\n".join(numbered) + footer
     except Exception:
       pass
   if size > 15 * 1024 * 1024:
     return True, _describe_binary(target) + "\nNote: File > 15 MB; use grep_search or python_eval to inspect slices."
   try:
     content, enc = read_text_resilient(target)
   except ValueError:
     return True, _describe_binary(target)
   lines = content.splitlines()
   total_lines = len(lines)
   start_idx = offset - 1
   end_idx = min(total_lines, start_idx + limit)
   selected = lines[start_idx:end_idx]
   numbered = [f"{i:5d} | {line}" for i, line in enumerate(selected, start=offset)]
   header = f"File: {target} ({total_lines} lines, {format_size(size)}, encoding={enc}) [Showing lines {offset}-{end_idx}]"
   footer = f"\n... ({total_lines - end_idx} more lines. Pass offset={end_idx + 1} to read further.)" if end_idx < total_lines else ""
   return True, header + "\n" + "\n".join(numbered) + footer
 def tool_write_file(
   args: Dict[str, Any],
   cwd: Path,
   undo_mgr: UndoManager,
 ) -> Tuple[bool, str, Optional[Tuple[str, str, str]]]:
   raw_path = str(args.get("path", "")).strip()
   content = str(args.get("content", ""))
   if not raw_path:
     return False, "Error: 'path' parameter is required.", None
   target = resolve_user_path(raw_path, cwd)
   old_text = ""
   if target.exists() and target.is_file():
     try:
       old_text, _ = read_text_resilient(target)
     except Exception:
       old_text = ""
   undo_mgr.record_before_modify(target)
   _atomic_write_text(target, content, encoding="utf-8")
   line_count = len(content.splitlines())
   diff_info = (str(target), old_text, content)
   return True, f"Successfully wrote {line_count} lines ({format_size(len(content.encode('utf-8')))}) to {target}", diff_info
 def _fuzzy_line_replace(full_text: str, old_text: str, new_text: str) -> Optional[str]:
   src_lines = full_text.splitlines(keepends=True)
   raw_needle_lines = old_text.splitlines()
   n = len(raw_needle_lines)
   if n == 0 or n > len(src_lines):
     return None
   target_stripped = [ln.strip() for ln in raw_needle_lines]
   if not any(target_stripped) and n > 1:
     return None
   matches: List[int] = []
   for i in range(len(src_lines) - n + 1):
     if [src_lines[i + j].strip() for j in range(n)] == target_stripped:
       matches.append(i)
   if len(matches) != 1:
     return None
   idx = matches[0]
   ending = "\r\n" if src_lines[idx].endswith("\r\n") else "\n"
   replacement_chunk = new_text
   if replacement_chunk and not replacement_chunk.endswith(("\n", "\r\n")) and src_lines[idx + n - 1].endswith(("\n", "\r\n")):
     replacement_chunk += ending
   return "".join(src_lines[:idx]) + replacement_chunk + "".join(src_lines[idx + n :])
 def tool_edit_file(
   args: Dict[str, Any],
   cwd: Path,
   undo_mgr: UndoManager,
 ) -> Tuple[bool, str, Optional[Tuple[str, str, str]]]:
   raw_path = str(args.get("path", "")).strip()
   old_text = str(args.get("old_text") if "old_text" in args else args.get("old_string", ""))
   new_text = str(args.get("new_text") if "new_text" in args else args.get("new_string", ""))
   replace_all = bool(args.get("replace_all", False))
   if not raw_path:
     return False, "Error: 'path' is required.", None
   if not old_text:
     return False, "Error: 'old_text' cannot be empty.", None
   target = resolve_user_path(raw_path, cwd)
   if not target.exists() or not target.is_file():
     return False, _missing_path_message("File does not exist", target, cwd), None
   content, enc = read_text_resilient(target)
   count = content.count(old_text)
   if count == 0:
     fuzzy_updated = _fuzzy_line_replace(content, old_text, new_text)
     if fuzzy_updated is None:
       return False, f"Could not find 'old_text' in {target}. Verify exact lines and retry.{_closest_edit_snippet(content, old_text)}", None
     updated = fuzzy_updated
     replaced_count = 1
   elif count > 1 and not replace_all:
     return False, f"'old_text' matched {count} times in {target}. Include more surrounding context lines or set replace_all=true.", None
   else:
     updated = content.replace(old_text, new_text) if replace_all else content.replace(old_text, new_text, 1)
     replaced_count = count if replace_all else 1
   undo_mgr.record_before_modify(target)
   write_enc = enc if enc in ("utf-8", "utf-8-sig", "cp1254", "utf-16-le", "utf-16-be") else "utf-8"
   _atomic_write_text(target, updated, encoding=write_enc)
   return True, f"Edited {target} ({replaced_count} replacement(s) applied).", (str(target), content, updated)
 def tool_multi_edit(
   args: Dict[str, Any],
   cwd: Path,
   undo_mgr: UndoManager,
 ) -> Tuple[bool, str, Optional[Tuple[str, str, str]]]:
   raw_path = str(args.get("path", "")).strip()
   edits = args.get("edits") or []
   if not raw_path or not isinstance(edits, list) or not edits:
     return False, "Error: 'path' and a non-empty list of 'edits' are required.", None
   target = resolve_user_path(raw_path, cwd)
   if not target.exists() or not target.is_file():
     return False, _missing_path_message("File does not exist", target, cwd), None
   original, enc = read_text_resilient(target)
   working = original
   for idx, item in enumerate(edits, start=1):
     if not isinstance(item, dict):
       return False, f"Edit #{idx} must be an object with old_text and new_text.", None
     o_txt = str(item.get("old_text") if "old_text" in item else item.get("old_string", ""))
     n_txt = str(item.get("new_text") if "new_text" in item else item.get("new_string", ""))
     if not o_txt:
       return False, f"Edit #{idx} has empty old_text.", None
     matches = working.count(o_txt)
     if matches > 1 and not item.get("replace_all"):
       return False, f"Edit #{idx} is ambiguous ({matches} matches). Include more surrounding context.", None
     if matches >= 1:
       working = working.replace(o_txt, n_txt) if item.get("replace_all") else working.replace(o_txt, n_txt, 1)
     else:
       fuzzy = _fuzzy_line_replace(working, o_txt, n_txt)
       if fuzzy is None:
         return False, f"Edit #{idx} failed: could not locate old_text in {target}.{_closest_edit_snippet(working, o_txt)}", None
       working = fuzzy
   undo_mgr.record_before_modify(target)
   write_enc = enc if enc in ("utf-8", "utf-8-sig", "cp1254", "utf-16-le", "utf-16-be") else "utf-8"
   _atomic_write_text(target, working, encoding=write_enc)
   return True, f"Applied {len(edits)} edits atomically to {target}.", (str(target), original, working)
 def tool_delete_path(
   args: Dict[str, Any],
   cwd: Path,
   undo_mgr: UndoManager,
 ) -> Tuple[bool, str]:
   raw_path = str(args.get("path", "")).strip()
   if not raw_path:
     return False, "Error: 'path' is required."
   target = resolve_user_path(raw_path, cwd)
   if target.is_symlink():
     target.unlink()
     return True, f"Deleted symbolic link: {target}"
   if not target.exists():
     return False, f"Path does not exist: {target}"
   if target in (Path(target.anchor), Path("/"), Path.home().resolve()):
     return False, f"Safety lock: Refusing to delete protected root directory {target}."
   if target.is_file():
     undo_mgr.record_before_modify(target)
     target.unlink()
     return True, f"Deleted file: {target}"
   shutil.rmtree(target)
   return True, f"Deleted directory recursively: {target}"
 def tool_move_or_copy(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   src_raw = str(args.get("source", "")).strip()
   dst_raw = str(args.get("destination", "")).strip()
   op = str(args.get("operation", "move")).strip().lower()
   if not src_raw or not dst_raw:
     return False, "Error: Both 'source' and 'destination' paths are required."
   if op not in ("copy", "move"):
     return False, "Error: operation must be 'copy' or 'move'."
   src = resolve_user_path(src_raw, cwd)
   dst = resolve_user_path(dst_raw, cwd)
   if not src.exists() and not src.is_symlink():
     return False, f"Source path not found: {src}"
   if dst.exists() and dst.is_dir():
     dst = dst / src.name
   if not src.is_symlink() and src.resolve() in (Path(src.anchor), Path("/"), Path.home().resolve()):
     return False, f"Safety lock: refusing to move/copy a protected root directory: {src}"
   dst.parent.mkdir(parents=True, exist_ok=True)
   if op == "copy":
     if src.is_dir():
       shutil.copytree(src, dst, dirs_exist_ok=True, symlinks=True)
     else:
       shutil.copy2(src, dst)
     return True, f"Copied {src} -> {dst}"
   shutil.move(str(src), str(dst))
   return True, f"Moved {src} -> {dst}"
 def render_directory_tree(
   root: Path,
   max_depth: int = 2,
   show_hidden: bool = True,
   max_entries: int = 300,
 ) -> str:
   lines: List[str] = [f"📂 {root}"]
   counter = [0]
   def _walk(curr: Path, prefix: str, depth: int) -> None:
     if depth > max_depth or counter[0] >= max_entries:
       return
     try:
       entries = sorted(curr.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
     except PermissionError:
       lines.append(f"{prefix}└── [Permission Denied]")
       return
     except OSError as exc:
       lines.append(f"{prefix}└── [OS Error: {exc}]")
       return
     filtered: List[Path] = []
     for e in entries:
       if not show_hidden and e.name.startswith("."):
         continue
       if depth > 1 and e.is_dir() and e.name in IGNORED_DIRS:
         continue
       filtered.append(e)
     for idx, entry in enumerate(filtered):
       if counter[0] >= max_entries:
         lines.append(f"{prefix}└── ... (truncated at {max_entries} items)")
         return
       counter[0] += 1
       is_last = idx == len(filtered) - 1
       connector = "└── " if is_last else "├── "
       if entry.is_symlink():
         lines.append(f"{prefix}{connector}🔗 {entry.name}")
       elif entry.is_dir():
         lines.append(f"{prefix}{connector}📁 {entry.name}/")
         extension = "    " if is_last else "│   "
         if depth < max_depth:
           _walk(entry, prefix + extension, depth + 1)
       else:
         try:
           sz = format_size(entry.stat().st_size)
         except OSError:
           sz = "?"
         lines.append(f"{prefix}{connector}📄 {entry.name} ({sz})")
   _walk(root, "", 1)
   return "\n".join(lines)
 def tool_list_directory(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   raw_path = str(args.get("path", ".") or ".")
   recursive = bool(args.get("recursive", False))
   show_hidden = bool(args.get("show_hidden", args.get("include_hidden", True)))
   max_depth = max(1, min(5, int(args.get("max_depth", 2 if recursive else 1) or 1)))
   target = resolve_user_path(raw_path, cwd)
   if not target.exists():
     return False, _missing_path_message("Directory does not exist", target, cwd)
   if not target.is_dir():
     return False, f"Path is not a directory: {target}"
   return True, render_directory_tree(target, max_depth=max_depth if recursive else 1, show_hidden=show_hidden)
 def tool_change_directory(
   args: Dict[str, Any],
   cwd: Path,
   set_cwd_fn: Callable[[Path], None],
 ) -> Tuple[bool, str]:
   raw_path = str(args.get("path", "")).strip()
   if not raw_path:
     return False, "Error: 'path' is required."
   target = resolve_user_path(raw_path, cwd)
   if not target.exists():
     return False, _missing_path_message("Directory does not exist", target, cwd)
   if not target.is_dir():
     return False, f"Path is not a directory: {target}"
   set_cwd_fn(target)
   return True, f"Active working directory changed to: {target}"
 def tool_list_system_drives() -> Tuple[bool, str]:
   roots = list_mounted_roots()
   folders = get_special_folders()
   lines = ["=== System Drives / Mounted Filesystems ==="]
   for r in roots:
     if "total_gb" in r:
       lines.append(f"  - {r['root']}  (Free: {r['free_gb']} GB / Total: {r['total_gb']} GB)")
     else:
       lines.append(f"  - {r['root']}")
   lines.append("\n=== User Special Folders ===")
   for name, p in folders.items():
     status = "exists" if p.exists() else "not created"
     lines.append(f"  - {name}: {p} ({status})")
   return True, "\n".join(lines)
 def tool_archive(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   action = str(args.get("action", "list")).strip().lower()
   arch_raw = str(args.get("archive_path", "")).strip()
   if not arch_raw:
     return False, "Error: 'archive_path' is required."
   arch = resolve_user_path(arch_raw, cwd)
   if action == "list":
     if not arch.exists():
       return False, f"Archive not found: {arch}"
     listing = _extract_archive_listing(arch)
     return (True, listing) if listing else (False, f"Unsupported archive format: {arch}")
   if action == "extract":
     if not arch.exists():
       return False, f"Archive not found: {arch}"
     out_raw = str(args.get("output_dir") or "").strip()
     dest = resolve_user_path(out_raw, cwd) if out_raw else arch.parent / arch.stem
     dest.mkdir(parents=True, exist_ok=True)
     dest_resolved = dest.resolve()
     if zipfile.is_zipfile(arch):
       with zipfile.ZipFile(arch, "r") as zf:
         for member in zf.infolist():
           target_p = (dest_resolved / member.filename).resolve()
           if not target_p.is_relative_to(dest_resolved):
             return False, f"Blocked Zip-Slip path traversal entry: {member.filename}"
         zf.extractall(dest_resolved)
       return True, f"Extracted ZIP archive {arch} -> {dest_resolved}"
     with tarfile.open(arch, "r:*") as tf:
       safe_members = []
       for m in tf.getmembers():
         if m.issym() or m.islnk():
           continue
         target_p = (dest_resolved / m.name).resolve()
         if not target_p.is_relative_to(dest_resolved):
           return False, f"Blocked Tar-Slip path traversal entry: {m.name}"
         safe_members.append(m)
       tf.extractall(dest_resolved, members=safe_members)
     return True, f"Extracted TAR archive {arch} -> {dest_resolved}"
   if action == "create":
     raw_targets = args.get("target_paths") or []
     if not isinstance(raw_targets, list) or not raw_targets:
       return False, "Error: 'target_paths' list is required when action='create'."
     arch.parent.mkdir(parents=True, exist_ok=True)
     low = arch.name.lower()
     if low.endswith((".tar.gz", ".tgz", ".tar")):
       mode = "w:gz" if low.endswith((".gz", ".tgz")) else "w"
       with tarfile.open(arch, mode) as tf:
         for rt in raw_targets:
           tp = resolve_user_path(str(rt), cwd)
           if not tp.exists():
             return False, f"Source path not found: {tp}"
           tf.add(tp, arcname=tp.name)
       return True, f"Created TAR archive {arch} ({format_size(arch.stat().st_size)})"
     with zipfile.ZipFile(arch, "w", compression=zipfile.ZIP_DEFLATED) as zf:
       for rt in raw_targets:
         tp = resolve_user_path(str(rt), cwd)
         if not tp.exists():
           return False, f"Source path not found: {tp}"
         if tp.is_file():
           zf.write(tp, arcname=tp.name)
         else:
           for root_d, _, files in os.walk(tp):
             for fn in files:
               full_f = Path(root_d) / fn
               zf.write(full_f, arcname=str(full_f.relative_to(tp.parent)))
     return True, f"Created ZIP archive {arch} ({format_size(arch.stat().st_size)})"
   return False, f"Unsupported archive action '{action}'. Use 'list', 'extract', or 'create'."
 def tool_undo_file_change(args: Dict[str, Any], cwd: Path, undo_mgr: UndoManager) -> Tuple[bool, str]:
   """Revert the most recent file write/edit/delete, or revert a specific file path."""
   raw_path = str(args.get("path") or "").strip()
   if raw_path:
     target = resolve_user_path(raw_path, cwd)
     res = undo_mgr.undo_for_path(target)
     if res is None:
       recent = undo_mgr.recent_paths()
       hint = ("\nTracked snapshots:\n  " + "\n  ".join(recent)) if recent else "\nNo snapshots recorded yet."
       return False, f"No undo snapshot found for {target}.{hint}"
     restored_path, action = res
     return True, f"Successfully rolled back {restored_path} ({action})."
   restored = undo_mgr.undo_last()
   if restored is None:
     return False, "No file changes available in undo history to roll back."
   return True, f"Successfully rolled back most recent file change: {restored}"
 return locals()
_dm_install('docmind.tools.filesystem', _dm_module_06, False)

# ===== docmind/core/safety.py (included source) =====
def _dm_module_07():
 """
 Heuristic credential-vault & SSRF guard.
 Full computer-wide filesystem access IS enabled across all drives and folders
 (Desktop, Downloads, Documents, C:\\, D:\\, /home, /etc, /opt, etc.); only private
 cryptographic keys / credential stores and localhost SSRF URLs trigger extra consent.
 """
 import ipaddress
 import re
 import urllib.parse
 from pathlib import Path
 from typing import Any, Dict
 from docmind.tools.filesystem import resolve_user_path
 _VAULT_DIRS = {".ssh", ".aws", ".gnupg", ".kube", ".docmind", ".docmind-single", ".azure"}
 _VAULT_FILES = {
   ".git-credentials", ".netrc", "credentials.json", "secrets.json",
   "id_rsa", "id_ed25519", "id_ecdsa", "id_dsa",
 }
 DANGEROUS_COMMAND_PATTERNS = [
   r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\s+/(?:\s|$|\*)",
   r"\bmkfs(?:\.[a-z0-9]+)?\b",
   r"\bdd\s+if=.*\bof=/dev/(?:sd|nvme|hd|vd)",
   r":\(\)\s*\{\s*:\|:\s*&\s*\}\s*;",
   r"\bformat\s+[a-zA-Z]:",
   r"\bdiskpart\b",
   r"\bdel\s+/[fFsS].*[cC]:\\",
   r"\brd\s+/[sS]\s+/[qQ]\s+[cC]:\\",
   r"\bremove-item\b.*[cC]:\\\*\s+-recurse",
 ]
 def is_catastrophic_command(cmd: str) -> bool:
   if not cmd:
     return False
   lowered = cmd.strip().lower()
   return any(re.search(pat, lowered) for pat in DANGEROUS_COMMAND_PATTERNS)
 def sensitive_path(raw: str, cwd: Path) -> bool:
   """Return True ONLY for private key/credential vaults (never blocks normal computer folders)."""
   if not raw:
     return False
   try:
     raw_path = Path(raw).expanduser()
     resolved = resolve_user_path(raw, cwd)
     for p in (raw_path, resolved):
       parts = [part.lower() for part in p.parts]
       base = p.name.lower()
       if any(part in _VAULT_DIRS for part in parts):
         return True
       if ".config" in parts and any(x in parts for x in ("gcloud", "gh")):
         return True
       if base in _VAULT_FILES or base.startswith(("id_rsa.", "id_ed25519.")):
         return True
       if base.endswith((".pem", ".key", ".p12", ".pfx", ".kdbx")):
         return True
   except (OSError, ValueError):
     return False
   return False
 def sensitive_tool_action(name: str, args: Dict[str, Any], cwd: Path) -> bool:
   """Check if a tool call touches a private credential vault or internal loopback SSRF target."""
   for key in ("path", "source", "destination", "archive_path", "output_dir"):
     if key in args and args.get(key) and sensitive_path(str(args[key]), cwd):
       return True
   if name == "web_fetch":
     try:
       host = (urllib.parse.urlsplit(str(args.get("url", ""))).hostname or "").lower()
       if host in ("localhost", "localhost.localdomain") or host.endswith(".local"):
         return True
       try:
         addr = ipaddress.ip_address(host)
         return not addr.is_global
       except ValueError:
         pass
     except ValueError:
       return True
   return False
 return locals()
_dm_install('docmind.core.safety', _dm_module_07, False)

# ===== docmind/tools/search.py (included source) =====
def _dm_module_08():
 """
 DocMind Code & File Search Tools
 Fast recursive filename glob search and content regex grep search.
 """
 import fnmatch
 import os
 import re
 from pathlib import Path
 from typing import Any, Dict, List, Tuple
 from docmind.tools.filesystem import IGNORED_DIRS, format_size, read_text_resilient, resolve_user_path
 from docmind.core.safety import sensitive_path
 def tool_search_files(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   pattern = str(args.get("pattern", "*") or "*").strip()
   raw_path = str(args.get("path", ".") or ".")
   include_hidden = bool(args.get("include_hidden", False))
   max_results = max(1, min(300, int(args.get("max_results", 100) or 100)))
   root = resolve_user_path(raw_path, cwd)
   if not root.exists():
     return False, f"Search directory not found: {root}"
   matches: List[str] = []
   for dirpath, dirnames, filenames in os.walk(root):
     dirnames[:] = [
       d
       for d in dirnames
       if d not in IGNORED_DIRS and (include_hidden or not d.startswith("."))
       and not sensitive_path(str(Path(dirpath) / d), cwd)
     ]
     for fname in filenames:
       if not include_hidden and fname.startswith("."):
         continue
       full_path = Path(dirpath) / fname
       if sensitive_path(str(full_path), cwd):
         continue
       rel_str = str(full_path.relative_to(root)) if full_path != root else fname
       if fnmatch.fnmatch(fname.lower(), pattern.lower()) or fnmatch.fnmatch(rel_str.lower(), pattern.lower()):
         try:
           sz = format_size(full_path.stat().st_size)
         except OSError:
           sz = "?"
         matches.append(f"{rel_str}  ({sz})")
         if len(matches) >= max_results:
           break
     if len(matches) >= max_results:
       break
   if not matches:
     return True, f"No files matching '{pattern}' found under {root}."
   header = f"Found {len(matches)} file(s) matching '{pattern}' in {root}:"
   return True, header + "\n" + "\n".join(matches)
 def tool_grep_search(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   query = str(args.get("query", "")).strip()
   if not query:
     return False, "Error: 'query' parameter is required."
   raw_path = str(args.get("path", ".") or ".")
   file_pattern = str(args.get("file_pattern", "*") or "*")
   case_sensitive = bool(args.get("case_sensitive", False))
   max_matches = max(1, min(200, int(args.get("max_matches", 80) or 80)))
   flags = 0 if case_sensitive else re.IGNORECASE
   try:
     regex = re.compile(query, flags)
   except re.error:
     regex = re.compile(re.escape(query), flags)
   root = resolve_user_path(raw_path, cwd)
   if not root.exists():
     return False, f"Path not found: {root}"
   results: List[str] = []
   def _scan_file(fpath: Path, display_name: str) -> None:
     try:
       if fpath.stat().st_size > 2 * 1024 * 1024:
         return
       text, _ = read_text_resilient(fpath)
     except Exception:
       return
     for lineno, line in enumerate(text.splitlines(), start=1):
       if regex.search(line):
         snippet = line.strip()
         if len(snippet) > 180:
           snippet = snippet[:177] + "..."
         results.append(f"{display_name}:{lineno}: {snippet}")
         if len(results) >= max_matches:
           return
   if root.is_file():
     _scan_file(root, root.name)
   else:
     for dirpath, dirnames, filenames in os.walk(root):
       dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS and not d.startswith(".")
              and not sensitive_path(str(Path(dirpath) / d), cwd)]
       for fname in filenames:
         if fname.startswith("."):
           continue
         if file_pattern != "*" and not fnmatch.fnmatch(fname.lower(), file_pattern.lower()):
           continue
         fp = Path(dirpath) / fname
         if fp.is_symlink() or sensitive_path(str(fp), cwd):
           continue
         rel = str(fp.relative_to(root))
         _scan_file(fp, rel)
         if len(results) >= max_matches:
           break
       if len(results) >= max_matches:
         break
   if not results:
     return True, f"No matches found for '{query}' in {root}."
   header = f"Grep matches for '{query}' ({len(results)} hit(s)):"
   return True, header + "\n" + "\n".join(results)
 return locals()
_dm_install('docmind.tools.search', _dm_module_08, False)

# ===== docmind/tools/project.py (included source) =====
def _dm_module_09():
 """Bounded, read-only project discovery and multi-language non-executing syntax checks."""
 import ast
 import json
 import os
 import shutil
 import subprocess
 import sys
 import xml.etree.ElementTree as ET
 from collections import Counter
 from pathlib import Path
 from typing import Any, Dict, List, Tuple
 from docmind.core.safety import sensitive_path
 from docmind.tools.filesystem import resolve_user_path
 _SKIP_DIRS = {
   ".git", ".hg", ".svn", ".cache", ".venv", "venv", "__pycache__",
   "node_modules", "vendor", "dist", "build", "target", "out", "coverage",
   ".next", ".pytest_cache", ".mypy_cache", ".tox", ".gradle", ".dart_tool",
 }
 _LANGUAGE_EXTENSIONS = {
   ".py": "Python", ".pyi": "Python", ".js": "JavaScript", ".jsx": "JavaScript",
   ".mjs": "JavaScript", ".cjs": "JavaScript", ".ts": "TypeScript", ".tsx": "TypeScript",
   ".go": "Go", ".rs": "Rust", ".c": "C", ".h": "C/C++", ".cc": "C++", ".cpp": "C++",
   ".hpp": "C++", ".java": "Java", ".kt": "Kotlin", ".kts": "Kotlin", ".cs": "C#",
   ".fs": "F#", ".rb": "Ruby", ".php": "PHP", ".swift": "Swift", ".dart": "Dart",
   ".ex": "Elixir", ".exs": "Elixir", ".erl": "Erlang", ".hs": "Haskell", ".lua": "Lua",
   ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell", ".ps1": "PowerShell",
   ".html": "HTML", ".htm": "HTML", ".css": "CSS", ".scss": "SCSS", ".vue": "Vue",
   ".svelte": "Svelte", ".sql": "SQL", ".r": "R", ".jl": "Julia", ".gd": "GDScript",
 }
 _MANIFESTS = {
   "agents.md", "readme.md", "pyproject.toml", "requirements.txt", "setup.py", "setup.cfg",
   "pytest.ini", "tox.ini", "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
   "bun.lock", "bun.lockb", "cargo.toml", "cargo.lock", "go.mod", "go.sum", "gemfile",
   "gemfile.lock", "pom.xml", "build.gradle", "build.gradle.kts", "gradlew", "composer.json",
   "mix.exs", "pubspec.yaml", "makefile", "cmakelists.txt", "dockerfile", "docker-compose.yml",
   "compose.yaml", "deno.json", "deno.jsonc", "tsconfig.json", "vite.config.ts", "vite.config.js",
   "pkgbuild",
 }
 def tool_project_overview(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   """Summarize a bounded project tree; never execute a project command."""
   root = resolve_user_path(str(args.get("path") or "."), cwd)
   if not root.exists() or not root.is_dir():
     return False, f"Project directory not found: {root}"
   depth_limit = max(1, min(5, int(args.get("max_depth", 3) or 3)))
   limit = max(50, min(1800, int(args.get("max_files", 900) or 900)))
   max_directories = max(25, min(900, limit // 2))
   files: List[str] = []
   manifests: List[str] = []
   pkg_paths: List[Path] = []
   languages: Counter = Counter()
   truncated = False
   directories_truncated = False
   directories_seen = 0
   walk_errors: List[str] = []
   def record_error(exc: OSError) -> None:
     if len(walk_errors) < 3:
       walk_errors.append(str(exc))
   for dirpath, dirs, names in os.walk(root, topdown=True, followlinks=False, onerror=record_error):
     directories_seen += 1
     if directories_seen > max_directories:
       directories_truncated = True
       break
     base = Path(dirpath)
     depth = len(base.relative_to(root).parts)
     selected_dirs: List[str] = []
     for name in sorted(dirs, key=str.lower):
       if (
         depth >= depth_limit
         or name.lower() in _SKIP_DIRS
         or name.startswith(".")
         or (base / name).is_symlink()
         or sensitive_path(str(base / name), cwd)
       ):
         continue
       if len(selected_dirs) >= max_directories - directories_seen:
         directories_truncated = True
         break
       selected_dirs.append(name)
     dirs[:] = selected_dirs
     for name in sorted(names, key=str.lower):
       path = base / name
       if name.startswith(".") or path.is_symlink() or sensitive_path(str(path), cwd):
         continue
       rel = str(path.relative_to(root)).replace(os.sep, "/")
       files.append(rel)
       low = name.lower()
       language = _LANGUAGE_EXTENSIONS.get(path.suffix.lower())
       if language:
         languages[language] += 1
       if low in _MANIFESTS or low.endswith((".sln", ".csproj")):
         manifests.append(rel)
       if low == "package.json" and len(pkg_paths) < 8:
         pkg_paths.append(path)
       if len(files) >= limit:
         truncated = True
         break
     if truncated:
       break
   output = [
     f"Project: {root}",
     f"Files scanned: {len(files)}" + (" (bounded; more may exist)" if truncated or directories_truncated else ""),
     f"Directories visited: {min(directories_seen, max_directories)} (maximum {max_directories}; depth {depth_limit})",
     "Languages by file count: " + (", ".join(f"{name}={count}" for name, count in languages.most_common(16)) or "not detected"),
     "Project markers: " + (", ".join(manifests[:35]) if manifests else "none detected"),
   ]
   for package in pkg_paths:
     try:
       with package.open("rb") as stream:
         package_data = stream.read(256 * 1024 + 1)
       if len(package_data) > 256 * 1024:
         continue
       parsed = json.loads(package_data.decode("utf-8-sig"))
       if not isinstance(parsed, dict):
         continue
       scripts = parsed.get("scripts") if isinstance(parsed.get("scripts"), dict) else {}
       dependencies = {}
       for key in ("dependencies", "devDependencies"):
         part = parsed.get(key)
         if isinstance(part, dict):
           dependencies.update(part)
       script_names = [str(k)[:60] for k in scripts.keys() if isinstance(k, str)][:20]
       known = (
         "react", "next", "vue", "svelte", "vite", "express", "fastify",
         "typescript", "jest", "vitest", "playwright", "@angular/core",
       )
       frameworks = [name for name in known if name in dependencies]
       if script_names or frameworks:
         rel = str(package.relative_to(root)).replace(os.sep, "/")
         output.append(
           f"{rel}: script names=" + (", ".join(script_names) or "none")
           + "; recognized dependencies=" + (", ".join(frameworks) or "none")
         )
     except (OSError, ValueError, UnicodeError):
       pass
   output.append("Sample paths: " + (", ".join(files[:45]) if files else "(empty)"))
   if walk_errors:
     output.append(f"Warning: {len(walk_errors)} directory access error(s); listing may be incomplete.")
   return True, "\n".join(output)
 def _line_context_around(data_bytes: bytes, lineno: int) -> str:
   if not lineno or lineno < 1:
     return ""
   lines = data_bytes.decode("utf-8", errors="replace").splitlines()
   if not lines:
     return ""
   start = max(0, lineno - 3)
   end = min(len(lines), lineno + 2)
   out = ["\nCode context around syntax error:"]
   for idx in range(start, end):
     marker = ">>" if (idx + 1) == lineno else "  "
     out.append(f"  {marker} {idx + 1:5d} | {lines[idx]}")
   return "\n".join(out)
 def tool_check_syntax(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   """Validate Python, JSON, TOML, XML/SVG, Shell (.sh), or JS (.js/.mjs) syntax without executing user logic."""
   raw_path = str(args.get("path", "")).strip()
   if not raw_path:
     return False, "Error: path is required."
   path = resolve_user_path(raw_path, cwd)
   if not path.is_file():
     return False, f"File not found or not a regular file: {path}"
   size = path.stat().st_size
   if size > 4 * 1024 * 1024:
     return False, f"Syntax check skipped: file exceeds 4 MiB: {path}"
   language = str(args.get("language") or "").strip().lower()
   if not language:
     language = {
       ".py": "python", ".pyi": "python",
       ".json": "json", ".ipynb": "json",
       ".toml": "toml",
       ".xml": "xml", ".svg": "xml", ".plist": "xml", ".csproj": "xml",
       ".sh": "shell", ".bash": "shell",
       ".js": "javascript", ".mjs": "javascript", ".cjs": "javascript",
     }.get(path.suffix.lower(), "")
   data = path.read_bytes()
   try:
     if language in ("python", "py"):
       ast.parse(data, filename=str(path))
       detail = f"Python {sys.version_info.major}.{sys.version_info.minor} AST syntax valid."
     elif language == "json":
       def reject_constant(value: str):
         raise ValueError("Non-standard JSON constant: " + value)
       json.loads(data.decode("utf-8-sig"), parse_constant=reject_constant)
       detail = "Strict JSON syntax valid."
     elif language == "toml":
       try:
         import tomllib
         tomllib.loads(data.decode("utf-8-sig"))
         detail = "TOML syntax valid."
       except ImportError:
         return False, "TOML parsing requires Python 3.11+."
     elif language == "xml":
       ET.fromstring(data.decode("utf-8-sig"))
       detail = "XML structure well-formed."
     elif language == "shell":
       bash_bin = shutil.which("bash") or shutil.which("sh")
       if not bash_bin:
         return True, f"No POSIX shell parser installed to check {path.name}; skipped."
       pr = subprocess.run([bash_bin, "-n", str(path)], capture_output=True, text=True, timeout=8, stdin=subprocess.DEVNULL)
       if pr.returncode != 0:
         err_txt = (pr.stderr or pr.stdout).strip()
         return False, f"Shell syntax check FAILED for {path}:\n{err_txt}\n[SELF-RECOVERY] Fix the shell syntax error with edit_file or undo_file_change."
       detail = f"Shell syntax checked cleanly with '{Path(bash_bin).name} -n' (not executed)."
     elif language == "javascript":
       node_bin = shutil.which("node")
       if not node_bin:
         return True, f"Node.js not installed to syntax-check {path.name}; skipped."
       pr = subprocess.run([node_bin, "--check", str(path)], capture_output=True, text=True, timeout=8, stdin=subprocess.DEVNULL)
       if pr.returncode != 0:
         err_txt = (pr.stderr or pr.stdout).strip()
         return False, f"JavaScript syntax check FAILED for {path}:\n{err_txt}\n[SELF-RECOVERY] Fix the syntax error with edit_file or undo_file_change."
       detail = "JavaScript syntax checked cleanly with 'node --check' (not executed)."
     else:
       return False, f"No built-in syntax parser for '{path.suffix}'; use language-appropriate tooling."
   except (SyntaxError, UnicodeError, ValueError, ET.ParseError) as exc:
     lineno = getattr(exc, "lineno", 0) or (exc.position[0] if isinstance(exc, ET.ParseError) and hasattr(exc, "position") else 0)
     if isinstance(exc, SyntaxError):
       detail = f"{exc.msg} (line {exc.lineno or '?'}, column {exc.offset or '?'})"
     elif isinstance(exc, json.JSONDecodeError):
       detail = f"{exc.msg} (line {exc.lineno}, column {exc.colno})"
     else:
       detail = str(exc)[:300]
     ctx = _line_context_around(data, int(lineno or 0))
     return (
       False,
       f"Syntax check FAILED for {path}: {detail}.{ctx}\n"
       "[SELF-RECOVERY] Go back and fix the broken lines using edit_file, or revert via undo_file_change.",
     )
   return True, f"Syntax check passed for {path}. {detail}"
 return locals()
_dm_install('docmind.tools.project', _dm_module_09, False)

# ===== docmind/tools/terminal.py (included source) =====
def _dm_module_10():
 """
 DocMind Universal Cross-Platform Terminal, Python, Desktop Open & Process Tools
 Works seamlessly across Windows (PowerShell 7 / Windows PowerShell / CMD / Git Bash / WSL)
 and Linux / macOS (Bash / Zsh / POSIX sh), with clean process-tree termination and UTF-8 decoding.
 """
 import ctypes
 import os
 import platform
 import shutil
 import signal
 import subprocess
 import sys
 import time
 from pathlib import Path
 from typing import Any, Dict, List, Optional, Tuple
 from docmind.core.errors import mask_secrets
 import re
 from docmind.tools.filesystem import get_special_folders, list_mounted_roots, resolve_user_path, suggest_similar_paths
 def _child_environment() -> Dict[str, str]:
   env = dict(os.environ)
   env["PYTHONIOENCODING"] = "utf-8"
   env["PYTHONUTF8"] = "1"
   return env
 def _truncate_output(text: str, max_chars: int = 24000) -> str:
   if len(text) <= max_chars:
     return text
   half = max_chars // 2
   return text[:half] + f"\n\n... [Output truncated: {len(text) - max_chars:,} chars omitted] ...\n\n" + text[-half:]
 _OS_PROFILE_CACHE: List[Dict[str, Any]] = []
 def detect_os_profile() -> Dict[str, Any]:
   """Detect exact OS & Linux distro (e.g. Arch Linux, Ubuntu, Fedora, Windows 11/10, macOS) + package managers."""
   if _OS_PROFILE_CACHE:
     return dict(_OS_PROFILE_CACHE[0])
   sys_name = platform.system()
   arch = platform.machine() or "unknown"
   os_family = "Linux"
   pretty_name = f"{sys_name} {platform.release()}"
   distro_id = sys_name.lower()
   distro_like = ""
   is_wsl = False
   if os.name == "nt":
     os_family = "Windows"
     distro_id = "windows"
     try:
       ver = sys.getwindowsversion()
       win_ed = "Windows 11" if ver.build >= 22000 else f"Windows {platform.release()}"
       pretty_name = f"{win_ed} (Build {ver.build})"
     except Exception:
       pretty_name = f"Windows {platform.release()}"
   elif sys.platform == "darwin":
     os_family = "macOS"
     distro_id = "macos"
     mac_v = platform.mac_ver()[0] or platform.release()
     pretty_name = f"macOS {mac_v}"
   else:
     os_family = "Linux"
     try:
       proc_ver = Path("/proc/version").read_text(encoding="utf-8", errors="ignore").lower()
       if "microsoft" in proc_ver or "wsl" in proc_ver:
         is_wsl = True
     except Exception:
       pass
     os_rel_data: Dict[str, str] = {}
     for rel_file in (Path("/etc/os-release"), Path("/usr/lib/os-release")):
       if rel_file.is_file():
         try:
           for ln in rel_file.read_text(encoding="utf-8", errors="ignore").splitlines():
             if "=" in ln and not ln.lstrip().startswith("#"):
               k, v = ln.split("=", 1)
               os_rel_data[k.strip()] = v.strip().strip('"').strip("'")
           break
         except Exception:
           pass
     if os_rel_data:
       distro_id = os_rel_data.get("ID", "linux").lower()
       distro_like = os_rel_data.get("ID_LIKE", "").lower()
       pretty_name = os_rel_data.get("PRETTY_NAME") or os_rel_data.get("NAME") or pretty_name
     elif Path("/etc/arch-release").is_file():
       distro_id = "arch"
       pretty_name = "Arch Linux"
     elif Path("/etc/debian_version").is_file():
       distro_id = "debian"
       pretty_name = "Debian GNU/Linux"
     elif Path("/etc/fedora-release").is_file():
       distro_id = "fedora"
       pretty_name = Path("/etc/fedora-release").read_text(encoding="utf-8", errors="ignore").strip()
     if Path("/etc/arch-release").is_file() and "arch" not in distro_id and "arch" not in distro_like:
       distro_like = (distro_like + " arch").strip()
     if is_wsl:
       pretty_name = f"{pretty_name} (WSL)"
   pkg_candidates = (
     ("pacman", "pacman"), ("paru", "paru (AUR)"), ("yay", "yay (AUR)"),
     ("apt", "apt"), ("dnf", "dnf"), ("zypper", "zypper"), ("apk", "apk"),
     ("xbps-install", "xbps"), ("emerge", "emerge"), ("nix-env", "nix"),
     ("winget", "winget"), ("choco", "choco"), ("scoop", "scoop"),
     ("brew", "brew"), ("flatpak", "flatpak"), ("snap", "snap"),
   )
   pkg_managers = [label for binary, label in pkg_candidates if shutil.which(binary)]
   dev_tools = [t_bin for t_bin in ("git", "python3", "pip", "uv", "node", "npm", "cargo", "go", "gcc", "docker") if shutil.which(t_bin)]
   desktop_env = (
     os.environ.get("XDG_CURRENT_DESKTOP")
     or os.environ.get("DESKTOP_SESSION")
     or ("Wayland" if os.environ.get("WAYLAND_DISPLAY") else ("X11" if os.environ.get("DISPLAY") else ("Windows Desktop" if os.name == "nt" else "CLI/Headless")))
   )
   profile = {
     "os_family": os_family,
     "pretty_name": pretty_name,
     "distro_id": distro_id,
     "distro_like": distro_like,
     "arch": arch,
     "is_arch": distro_id == "arch" or "arch" in distro_like.split(),
     "is_debian": distro_id in ("debian", "ubuntu", "linuxmint", "pop", "kali") or "debian" in distro_like,
     "is_fedora": distro_id in ("fedora", "rhel", "rocky", "almalinux") or "fedora" in distro_like,
     "is_wsl": is_wsl,
     "pkg_managers": pkg_managers,
     "dev_tools": dev_tools,
     "desktop": desktop_env,
   }
   _OS_PROFILE_CACHE.append(profile)
   return dict(profile)
 _AUTH_OR_ADMIN_PATTERNS = (
   r"sudo:\s*(?:a terminal is required|no tty present|password is required)",
   r"\[sudo\]\s*password",
   r"password for\s+\S+:",
   r"enter passphrase",
   r"authentication is required",
   r"authentication failure",
   r"polkit-agent-helper",
   r"pkexec",
   r"must be run as root",
   r"you cannot perform this operation unless you are root",
   r"are you root\?",
   r"only root can",
   r"permission denied.*(?:/etc/|/usr/|/var/lib/pacman|/var/lib/dpkg|/boot/|/sys/)",
   r"error:\s*you cannot perform this operation unless you are root",
   r"e:\s*could not open lock file\s+/var/lib/(?:dpkg|apt)",
   r"requested operation requires elevation",
   r"requires elevation",
   r"run as administrator",
   r"yönetici olarak",
   r"access is denied\.\s*$",
   r"sistem hatası 5\b|system error 5\b|0x80070005",
 )
 def diagnose_execution_failure(
   code_text: str,
   stdout_s: str,
   stderr_s: str,
   exit_code: int,
   shell_label: str,
 ) -> Dict[str, Any]:
   """
     Classify a failed terminal/Python execution so the agent knows whether:
     - USER_MUST_RUN: requires sudo/root/admin password or interactive credential input (cannot be fixed by agent; explain to user!)
     - AGENT_CAN_FIX: syntax/flag/path/package/code mistake that the agent CAN fix, re-request permission for, and retry!
     """
   combined = f"{stdout_s}\n{stderr_s}".strip()
   low = combined.lower()
   cmd_low = code_text.strip().lower()
   os_prof = detect_os_profile()
   needs_manual = any(re.search(pat, low, flags=re.MULTILINE) for pat in _AUTH_OR_ADMIN_PATTERNS)
   if not needs_manual and re.match(r"^\s*sudo\b", cmd_low) and exit_code != 0 and (
     "password" in low or "parola" in low or "tty" in low or "not allowed" in low or not low
   ):
     needs_manual = True
   if not needs_manual and os_prof["is_arch"] and re.search(r"\bpacman\s+-[SUTR]", code_text) and "root" in low:
     needs_manual = True
   if needs_manual:
     return {
       "triage": "USER_MUST_RUN",
       "requires_user_action": True,
       "summary_key": "term_triage_manual",
       "guidance": (
         "[ERROR TRIAGE: USER_MUST_RUN_MANUALLY — DO NOT RETRY THIS PRIVILEGED/PASSWORD COMMAND]\n"
         "Reason: This operation requires an interactive password (sudo/root/passphrase) or Administrator/UAC elevation, "
         "which cannot be entered inside a non-interactive agent subprocess.\n"
         "Required Agent Action: DO NOT re-run this privileged command yourself. Clearly explain to the user WHY it could not "
         "run automatically (password/admin privilege needed) and give them the exact command tailored to their OS "
         f"({os_prof['pretty_name']}) so they can run it directly in their own terminal."
       ),
     }
   hints: List[str] = []
   if exit_code == 127 or "command not found" in low or "is not recognized as an internal or external command" in low or "commandnotfoundexception" in low:
     pkgs = ", ".join(os_prof["pkg_managers"]) or "none"
     hints.append(
       f"Command/binary was not found on {os_prof['pretty_name']}. "
       f"Check available alternatives (installed dev tools: {', '.join(os_prof['dev_tools']) or 'python'}, "
       f"package managers: {pkgs}) or solve it directly via Python (`python_eval`) / built-in DocMind tools."
     )
   if "no such file or directory" in low or "cannot find path" in low or "sistem belirtilen yolu bulamıyor" in low:
     hints.append("A file or directory path in the command was wrong. Verify exact paths with `list_directory` or `search_files` first.")
   if "invalid option" in low or "unrecognized arguments" in low or "unknown option" in low or "unexpected token" in low or "syntax error" in low:
     hints.append(f"Command syntax or flags were invalid for shell '{shell_label}' on {os_prof['pretty_name']}. Rewrite with valid syntax/flags.")
   if "modulenotfounderror" in low or "importerror" in low:
     hints.append("A Python module is missing. Prefer Python standard library, or ask permission to install it in a venv/user environment if appropriate.")
   if not hints:
     hints.append(f"Inspect the exit code ({exit_code}) and stderr output carefully to determine if a corrected command or Python/tool approach will solve it.")
   return {
     "triage": "AGENT_CAN_FIX",
     "requires_user_action": False,
     "summary_key": "term_triage_autofix",
     "guidance": (
       "[ERROR TRIAGE: AGENT_SELF_REPAIR_POSSIBLE]\n"
       + " ".join(hints) + "\n"
       "Required Agent Action: Decide honestly whether you can fix this. "
       "• If YES: fix the command/code/path, request user permission again via `run_command` / `python_eval` (or use file tools), and verify the fix.\n"
       "• If NO (external blocker, missing hardware/service, or requires manual user login/secret): explain clearly to the user what failed and how they can resolve it."
     ),
   }
 def detect_available_shells() -> Dict[str, str]:
   """Detect all usable shells on Windows, Linux, or macOS."""
   shells: Dict[str, str] = {}
   if os.name == "nt":
     for name in ("pwsh", "powershell", "cmd"):
       found = shutil.which(name)
       if found:
         shells["powershell" if name in ("pwsh", "powershell") and "powershell" not in shells else name] = found
     git_bash_candidates = [
       Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "bin" / "bash.exe",
       Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Git" / "bin" / "bash.exe",
       Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Git" / "bin" / "bash.exe",
       Path(r"C:\msys64\usr\bin\bash.exe"),
     ]
     for cand in git_bash_candidates:
       if cand.is_file():
         shells["bash"] = str(cand)
         break
     if "bash" not in shells:
       w_bash = shutil.which("bash")
       if w_bash:
         if "system32" in w_bash.lower():
           try:
             pr = subprocess.run([w_bash, "-c", "echo ok"], capture_output=True, timeout=2)
             if pr.returncode == 0:
               shells["bash"] = w_bash
           except Exception:
             pass
         else:
           shells["bash"] = w_bash
   else:
     for name in ("bash", "zsh", "sh", "pwsh"):
       found = shutil.which(name)
       if found:
         shells[name] = found
   return shells
 def resolve_shell_invocation(requested_shell: str = "auto", command: str = "") -> Tuple[List[str], str]:
   """Build exact cross-platform subprocess argv and human-readable shell label."""
   req = (requested_shell or "auto").strip().lower()
   os_prof = detect_os_profile()
   shells = detect_available_shells()
   if os.name == "nt":
     if req == "bash":
       bash_bin = shells.get("bash")
       if not bash_bin:
         raise RuntimeError("Bash is not installed on this Windows machine. Use shell='powershell' or shell='cmd'.")
       return [bash_bin, "-c", command], f"bash ({bash_bin})"
     if req == "cmd":
       cmd_bin = shells.get("cmd") or os.environ.get("COMSPEC", "cmd.exe")
       wrapped = f"chcp 65001 >nul & {command}"
       return [cmd_bin, "/d", "/s", "/c", wrapped], f"cmd ({cmd_bin})"
     ps_bin = shells.get("pwsh") or shells.get("powershell")
     if ps_bin:
       utf8_prefix = (
         "[Console]::InputEncoding = [Console]::OutputEncoding = "
         "$OutputEncoding = [System.Text.UTF8Encoding]::new($false); "
       )
       return (
         [ps_bin, "-NoLogo", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", utf8_prefix + command],
         f"powershell ({ps_bin})",
       )
     cmd_bin = shells.get("cmd") or os.environ.get("COMSPEC", "cmd.exe")
     return [cmd_bin, "/d", "/s", "/c", f"chcp 65001 >nul & {command}"], f"cmd ({cmd_bin})"
   if req in ("powershell", "pwsh") and shells.get("pwsh"):
     ps_bin = shells["pwsh"]
     return [ps_bin, "-NoLogo", "-NoProfile", "-NonInteractive", "-Command", command], f"pwsh ({ps_bin})"
   if req == "sh":
     sh_bin = shells.get("sh", "/bin/sh")
     return [sh_bin, "-c", command], f"sh ({sh_bin})"
   bash_bin = shells.get("bash")
   if bash_bin:
     return [bash_bin, "-c", command], f"bash ({bash_bin})"
   sh_bin = shells.get("sh", "/bin/sh")
   return [sh_bin, "-c", command], f"sh ({sh_bin})"
 def _kill_process_tree(proc: subprocess.Popen) -> None:
   try:
     if os.name == "nt":
       subprocess.run(
         ["taskkill", "/F", "/T", "/PID", str(proc.pid)],
         capture_output=True,
         timeout=5,
       )
     else:
       os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
   except Exception:
     try:
       proc.kill()
     except Exception:
       pass
 def _decode_stream(raw: bytes) -> str:
   if not raw:
     return ""
   for enc in ("utf-8", "cp1254", "cp857", "cp1252"):
     try:
       return raw.decode(enc)
     except UnicodeDecodeError:
       continue
   return raw.decode("utf-8", errors="replace")
 def run_command_detailed(
   command: str,
   cwd: Path,
   timeout: int = 90,
   workdir: Optional[str] = None,
   shell: str = "auto",
 ) -> Dict[str, Any]:
   """Execute a terminal command across Windows or Linux and return structured execution telemetry."""
   exec_cwd = resolve_user_path(workdir, cwd) if workdir else cwd
   if not exec_cwd.exists() or not exec_cwd.is_dir():
     return {
       "ok": False,
       "exit_code": -1,
       "elapsed": 0.0,
       "shell": shell,
       "cwd": str(exec_cwd),
       "stdout": "",
       "stderr": f"Working directory does not exist: {exec_cwd}",
       "formatted": f"Error: Working directory does not exist: {exec_cwd}",
     }
   argv, shell_label = resolve_shell_invocation(shell, command)
   timeout_s = max(2, min(600, int(timeout or 90)))
   popen_kwargs: Dict[str, Any] = {
     "cwd": str(exec_cwd),
     "env": _child_environment(),
     "stdin": subprocess.DEVNULL,
     "stdout": subprocess.PIPE,
     "stderr": subprocess.PIPE,
   }
   if os.name == "nt":
     popen_kwargs["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
   else:
     popen_kwargs["start_new_session"] = True
   t0 = time.monotonic()
   proc = subprocess.Popen(argv, **popen_kwargs)
   try:
     out_b, err_b = proc.communicate(timeout=timeout_s)
     elapsed = time.monotonic() - t0
     rc = proc.returncode if proc.returncode is not None else 0
   except subprocess.TimeoutExpired:
     _kill_process_tree(proc)
     try:
       out_b, err_b = proc.communicate(timeout=2)
     except Exception:
       out_b, err_b = b"", b""
     elapsed = time.monotonic() - t0
     stdout_s = mask_secrets(_truncate_output(_decode_stream(out_b)))
     stderr_s = mask_secrets(_truncate_output(_decode_stream(err_b)))
     msg = f"[TIMEOUT] Command exceeded {timeout_s}s limit in {shell_label}.\nSTDOUT:\n{stdout_s}\nSTDERR:\n{stderr_s}".strip()
     return {
       "ok": False,
       "exit_code": -9,
       "elapsed": elapsed,
       "shell": shell_label,
       "cwd": str(exec_cwd),
       "stdout": stdout_s,
       "stderr": stderr_s or f"Timed out after {timeout_s}s",
       "formatted": msg,
     }
   stdout_s = mask_secrets(_truncate_output(_decode_stream(out_b)))
   stderr_s = mask_secrets(_truncate_output(_decode_stream(err_b)))
   parts = [
     f"Command: {mask_secrets(command)}",
     f"Shell: {shell_label}",
     f"Working Directory: {exec_cwd}",
     f"Exit Code: {rc} ({elapsed:.2f}s)",
   ]
   if stdout_s.strip():
     parts.append(f"--- STDOUT ---\n{stdout_s.rstrip()}")
   if stderr_s.strip():
     parts.append(f"--- STDERR ---\n{stderr_s.rstrip()}")
   if not stdout_s.strip() and not stderr_s.strip():
     parts.append("(Command completed with no stdout/stderr output)")
   triage_info = None
   if rc != 0:
     triage_info = diagnose_execution_failure(command, stdout_s, stderr_s, rc, shell_label)
     parts.append(triage_info["guidance"])
   return {
     "ok": rc == 0,
     "exit_code": rc,
     "elapsed": elapsed,
     "shell": shell_label,
     "cwd": str(exec_cwd),
     "stdout": stdout_s,
     "stderr": stderr_s,
     "triage": triage_info,
     "formatted": "\n".join(parts),
   }
 def run_python_detailed(code: str, cwd: Path, timeout: int = 45) -> Dict[str, Any]:
   timeout_s = max(2, min(300, int(timeout or 45)))
   py_label = f"python ({sys.executable})"
   popen_kwargs: Dict[str, Any] = {
     "cwd": str(cwd),
     "env": _child_environment(),
     "stdin": subprocess.DEVNULL,
     "stdout": subprocess.PIPE,
     "stderr": subprocess.PIPE,
   }
   if os.name == "nt":
     popen_kwargs["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
   else:
     popen_kwargs["start_new_session"] = True
   t0 = time.monotonic()
   proc = subprocess.Popen([sys.executable, "-c", code], **popen_kwargs)
   try:
     out_b, err_b = proc.communicate(timeout=timeout_s)
     elapsed = time.monotonic() - t0
     rc = proc.returncode if proc.returncode is not None else 0
   except subprocess.TimeoutExpired:
     _kill_process_tree(proc)
     try:
       out_b, err_b = proc.communicate(timeout=2)
     except Exception:
       out_b, err_b = b"", b""
     elapsed = time.monotonic() - t0
     stdout_s = mask_secrets(_truncate_output(_decode_stream(out_b)))
     stderr_s = mask_secrets(_truncate_output(_decode_stream(err_b)))
     return {
       "ok": False,
       "exit_code": -9,
       "elapsed": elapsed,
       "shell": py_label,
       "cwd": str(cwd),
       "stdout": stdout_s,
       "stderr": stderr_s or f"Timed out after {timeout_s}s",
       "formatted": f"[TIMEOUT] Python snippet exceeded {timeout_s}s.\n{stdout_s}\n{stderr_s}".strip(),
     }
   stdout_s = mask_secrets(_truncate_output(_decode_stream(out_b)))
   stderr_s = mask_secrets(_truncate_output(_decode_stream(err_b)))
   parts = [f"Python ({sys.version.split()[0]}) Exit Code: {rc} ({elapsed:.2f}s)"]
   if stdout_s.strip():
     parts.append(f"--- STDOUT ---\n{stdout_s.rstrip()}")
   if stderr_s.strip():
     parts.append(f"--- STDERR ---\n{stderr_s.rstrip()}")
   if not stdout_s.strip() and not stderr_s.strip():
     parts.append("(Python snippet finished with no printed output)")
   triage_info = None
   if rc != 0:
     triage_info = diagnose_execution_failure(code, stdout_s, stderr_s, rc, py_label)
     parts.append(triage_info["guidance"])
   return {
     "ok": rc == 0,
     "exit_code": rc,
     "elapsed": elapsed,
     "shell": py_label,
     "cwd": str(cwd),
     "stdout": stdout_s,
     "stderr": stderr_s,
     "triage": triage_info,
     "formatted": "\n".join(parts),
   }
 def tool_run_command(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   cmd = str(args.get("command", "")).strip()
   if not cmd:
     return False, "Error: 'command' is required."
   res = run_command_detailed(
     command=cmd,
     cwd=cwd,
     timeout=int(args.get("timeout", 90) or 90),
     workdir=str(args["workdir"]) if args.get("workdir") else (str(args["cwd"]) if args.get("cwd") else None),
     shell=str(args.get("shell") or "auto"),
   )
   return bool(res["ok"]), str(res["formatted"])
 def tool_python_eval(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   code = str(args.get("code", ""))
   if not code.strip():
     return False, "Error: 'code' is required."
   res = run_python_detailed(code=code, cwd=cwd, timeout=int(args.get("timeout", 45) or 45))
   return bool(res["ok"]), str(res["formatted"])
 def tool_open_path(args: Dict[str, Any], cwd: Path) -> Tuple[bool, str]:
   """Open a file, folder, URL, or application in the native OS desktop environment."""
   raw = str(args.get("target") or args.get("path") or "").strip()
   if not raw:
     return False, "Error: 'target' is required."
   is_url = raw.lower().startswith(("http://", "https://", "mailto:"))
   target_str = raw
   if not is_url:
     resolved = resolve_user_path(raw, cwd)
     if resolved.exists():
       target_str = str(resolved)
     elif shutil.which(raw):
       target_str = shutil.which(raw) or raw
     else:
       similar = suggest_similar_paths(resolved, cwd)
       hint = ("\n[SELF-RECOVERY HINT] Similar existing paths:\n  - " + "\n  - ".join(similar)) if similar else ""
       return False, f"Target file, folder, or application not found: {raw} (resolved: {resolved}){hint}"
   try:
     if os.name == "nt":
       os.startfile(target_str)
       return True, f"Opened on Windows desktop: {target_str}"
     if sys.platform == "darwin":
       subprocess.Popen(
         ["open", target_str],
         stdin=subprocess.DEVNULL,
         stdout=subprocess.DEVNULL,
         stderr=subprocess.DEVNULL,
         start_new_session=True,
       )
       return True, f"Opened on macOS: {target_str}"
     if not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
       return False, f"No graphical desktop session (DISPLAY/WAYLAND_DISPLAY) detected to open: {target_str}"
     opener = shutil.which("xdg-open") or shutil.which("gio")
     if not opener:
       return False, "Neither 'xdg-open' nor 'gio' is installed on this Linux system."
     cmd = [opener, "open", target_str] if opener.endswith("gio") else [opener, target_str]
     subprocess.Popen(
       cmd,
       stdin=subprocess.DEVNULL,
       stdout=subprocess.DEVNULL,
       stderr=subprocess.DEVNULL,
       start_new_session=True,
     )
     return True, f"Opened in Linux desktop session: {target_str}"
   except Exception as exc:
     return False, f"Failed to open '{target_str}': {exc}"
 def tool_find_processes(args: Dict[str, Any]) -> Tuple[bool, str]:
   """List or filter running processes across Windows and Linux/macOS without shell interpolation."""
   query = str(args.get("query") or "").strip().lower()
   limit = max(5, min(250, int(args.get("limit", 60) or 60)))
   try:
     if os.name == "nt":
       pr = subprocess.run(
         ["tasklist", "/FO", "CSV", "/NH"],
         capture_output=True,
         timeout=10,
         stdin=subprocess.DEVNULL,
       )
       lines = _decode_stream(pr.stdout).splitlines()
     else:
       ps_cmd = ["ps", "-eo", "pid,pcpu,pmem,comm,args"] if sys.platform != "darwin" else ["ps", "-axo", "pid,pcpu,pmem,comm"]
       pr = subprocess.run(
         ps_cmd,
         capture_output=True,
         timeout=10,
         stdin=subprocess.DEVNULL,
       )
       lines = _decode_stream(pr.stdout).splitlines()
     if query:
       matched = [ln for ln in lines if query in ln.lower()]
     else:
       matched = lines
     shown = matched[:limit]
     if not shown:
       return True, f"No running processes matched query '{query}'."
     header = f"Running processes ({len(shown)} shown of {len(matched)} matched):"
     return True, header + "\n" + "\n".join(shown)
   except Exception as exc:
     return False, f"Failed to enumerate processes: {exc}"
 def _get_ram_summary() -> str:
   try:
     if os.name == "nt":
       class MEMORYSTATUSEX(ctypes.Structure):
         _fields_ = [
           ("dwLength", ctypes.c_ulong),
           ("dwMemoryLoad", ctypes.c_ulong),
           ("ullTotalPhys", ctypes.c_ulonglong),
           ("ullAvailPhys", ctypes.c_ulonglong),
           ("ullTotalPageFile", ctypes.c_ulonglong),
           ("ullAvailPageFile", ctypes.c_ulonglong),
           ("ullTotalVirtual", ctypes.c_ulonglong),
           ("ullAvailVirtual", ctypes.c_ulonglong),
           ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
         ]
       stat_mem = MEMORYSTATUSEX()
       stat_mem.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
       if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat_mem)):
         tot = stat_mem.ullTotalPhys / (1024 ** 3)
         avail = stat_mem.ullAvailPhys / (1024 ** 3)
         return f"{avail:.1f} GB available / {tot:.1f} GB total ({stat_mem.dwMemoryLoad}% used)"
     elif Path("/proc/meminfo").is_file():
       mem_txt = Path("/proc/meminfo").read_text(encoding="utf-8", errors="ignore")
       vals: Dict[str, int] = {}
       for ln in mem_txt.splitlines():
         parts = ln.split(":")
         if len(parts) == 2:
           num = parts[1].strip().split()[0]
           if num.isdigit():
             vals[parts[0].strip()] = int(num)
       if "MemTotal" in vals:
         tot = vals["MemTotal"] / (1024 ** 2)
         avail = vals.get("MemAvailable", vals.get("MemFree", 0)) / (1024 ** 2)
         return f"{avail:.1f} GB available / {tot:.1f} GB total"
   except Exception:
     pass
   return "unknown"
 def tool_system_info(cwd: Path) -> Tuple[bool, str]:
   shells = detect_available_shells()
   roots = list_mounted_roots()
   folders = get_special_folders()
   user_name = os.environ.get("USERNAME") or os.environ.get("USER") or "unknown"
   info_lines = [
     f"OS / Distro: {os_prof['pretty_name']} [Family: {os_prof['os_family']}, ID: {os_prof['distro_id']}]",
     f"Kernel / Version: {platform.system()} {platform.release()} ({platform.version()})",
     f"Desktop / Session: {os_prof['desktop']}",
     "Package Managers: " + (", ".join(os_prof["pkg_managers"]) or "none detected"),
     "Installed Dev Tools: " + (", ".join(os_prof["dev_tools"]) or "python"),
     f"Architecture: {platform.machine()} | CPU Cores: {os.cpu_count()}",
     f"RAM: {_get_ram_summary()}",
     f"User: {user_name} | Host: {platform.node()}",
     f"Python: {sys.version.split()[0]} ({sys.executable})",
     f"Active Working Directory: {cwd}",
     "Available Shells: " + (", ".join(f"{k}={v}" for k, v in shells.items()) or "none"),
     "Mounted Drives / Roots: " + (
       ", ".join(f"{r['root']} ({r.get('free_gb', '?')}GB free/{r.get('total_gb', '?')}GB)" for r in roots) or "unknown"
     ),
     "Special Folders: " + ", ".join(f"{k}={v}" for k, v in folders.items()),
   ]
   return True, "\n".join(info_lines)
 return locals()
_dm_install('docmind.tools.terminal', _dm_module_10, False)

# ===== docmind/tools/web.py (included source) =====
def _dm_module_11():
 """Bounded web fetches. Remote content is untrusted; redirects are not followed."""
 import html
 import json
 import re
 import urllib.error
 import urllib.parse
 import urllib.request
 from typing import Any, Dict, Tuple
 HAS_HTTPX = False
 MAX_DOWNLOAD_BYTES = 1024 * 1024
 class _NoRedirect(urllib.request.HTTPRedirectHandler):
   def redirect_request(self, req, fp, code, msg, headers, newurl):
     return None
 def _strip_html(raw_html: str) -> str:
   cleaned = re.sub(r"(?is)<(script|style|noscript).*?>.*?</\1>", " ", raw_html)
   cleaned = re.sub(r"(?i)<br\s*/?>", "\n", cleaned)
   cleaned = re.sub(r"(?i)</(p|div|h[1-6]|li|tr|section|article)>", "\n", cleaned)
   cleaned = re.sub(r"(?s)<[^>]+>", " ", cleaned)
   cleaned = html.unescape(cleaned)
   lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in cleaned.splitlines()]
   return "\n".join(ln for ln in lines if ln)
 def tool_web_fetch(args: Dict[str, Any]) -> Tuple[bool, str]:
   url = str(args.get("url", "")).strip()
   try:
     parsed = urllib.parse.urlsplit(url)
     if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username is not None or parsed.password is not None:
       return False, "Error: an http(s) URL without embedded credentials is required."
     _ = parsed.port
   except ValueError:
     return False, "Error: invalid URL."
   max_chars = max(500, min(30000, int(args.get("max_chars", 12000) or 12000)))
   headers = {"User-Agent": "DocMind-AI-Agent/1.0"}
   data = bytearray()
   req = urllib.request.Request(url, headers=headers, method="GET")
   try:
     with urllib.request.build_opener(_NoRedirect()).open(req, timeout=20.0) as resp:
       status = resp.status
       ctype = (resp.headers.get("Content-Type") or "").lower()
       data.extend(resp.read(MAX_DOWNLOAD_BYTES + 1))
       if len(data) > MAX_DOWNLOAD_BYTES:
         return False, "Web response exceeds the 1 MiB safety limit."
   except urllib.error.HTTPError as exc:
     if 300 <= exc.code < 400:
       return False, f"URL: {url} (HTTP {exc.code}); redirects are disabled."
     status, ctype = exc.code, (exc.headers.get("Content-Type") or "").lower()
     data.extend(exc.read(MAX_DOWNLOAD_BYTES + 1))
     if len(data) > MAX_DOWNLOAD_BYTES:
       return False, "Web response exceeds the 1 MiB safety limit."
   raw_text = data.decode("utf-8", errors="replace")
   if "json" in ctype:
     try:
       body = json.dumps(json.loads(raw_text), indent=2, ensure_ascii=False)
     except ValueError:
       body = raw_text
   elif "html" in ctype or "<html" in raw_text[:500].lower():
     body = _strip_html(raw_text)
   else:
     body = raw_text
   if len(body) > max_chars:
     body = body[:max_chars] + f"\n\n... [Truncated at {max_chars} chars]"
   return (status < 400), f"URL: {url} (HTTP {status})\nUNTRUSTED WEB CONTENT:\n\n{body}"
 return locals()
_dm_install('docmind.tools.web', _dm_module_11, False)

# ===== docmind/core/context.py (included source) =====
def _dm_module_12():
 """
 DocMind Conversation Context, Token Tracker & Auto-Compaction Engine
 Allows unlimited continuous sessions by intelligently truncating bulky historical
 tool outputs and compacting older turns without breaking tool_call/tool_result pairs.
 """
 import json
 import os
 from pathlib import Path
 from typing import Any, Callable, Dict, List, Optional
 def _clip_summary(value: Any, limit: int) -> str:
   text = ' '.join(str(value or '').split())
   if len(text) <= limit:
     return text
   front = max(1, limit * 3 // 4)
   return text[:front] + ' …[omitted]… ' + text[-max(1, limit - front - 13):]
 def _summarize_older_groups(groups: List[List[Dict[str, Any]]]) -> str:
   """Keep the opening goal and newest older turns; do not invent tool success."""
   header = '[Earlier Conversation Summary - Auto-Compacted; lossy, not a full transcript]'
   users = [m for group in groups for m in group if m.get('role') == 'user']
   opening = _clip_summary(users[0].get('content', '') if users else '', 1500)
   label = 'Prior lossy summary' if opening.startswith('[Earlier Conversation Summary') else 'Opening user request'
   lines = [header, f'{label}: {opening}', 'Recent earlier turns and tool outcomes (older details may be omitted):']
   for group in groups[-10:]:
     events: List[str] = []
     results = {str(m.get('tool_call_id', '')): m for m in group if m.get('role') == 'tool'}
     for m in group:
       role = m.get('role')
       if role == 'user':
         text = str(m.get('content', ''))
         if not text.startswith('[Earlier Conversation Summary'):
           events.append('User: ' + _clip_summary(text, 280))
       elif role == 'assistant':
         for tc in (m.get('tool_calls') or [])[-6:]:
           args = tc.get('arguments') if isinstance(tc.get('arguments'), dict) else {}
           target = next((str(args[k]) for k in ('path', 'source', 'command', 'url') if args.get(k)), '')
           result = results.get(str(tc.get('id', '')))
           if result is None:
             state = 'NO RESULT; execution not confirmed'
             detail = ''
           else:
             state = 'FAILED OR DECLINED' if result.get('is_error') else 'TOOL REPORTED SUCCESS'
             result_text = str(result.get('content', ''))
             if 'Automatic, non-executing syntax check:' in result_text:
               if 'Syntax check failed' in result_text:
                 state += '; AUTOMATIC SYNTAX FAILED'
               elif 'Syntax check passed' in result_text:
                 state += '; AUTOMATIC SYNTAX PASSED (NOT FUNCTIONAL TEST)'
             elif 'Automatic syntax check skipped' in result_text:
               state += '; AUTOMATIC SYNTAX SKIPPED'
             detail = _clip_summary(result_text, 130)
           events.append('Tool ' + _clip_summary(tc.get('name', '?'), 40) +
                  ((' [' + _clip_summary(target, 100) + ']') if target else '') +
                  ': ' + state + ((' — ' + detail) if detail else ''))
         if m.get('content'):
           events.append('Assistant said (not independent proof): ' + _clip_summary(m['content'], 180))
     if events:
       lines.append('- ' + ' | '.join(events[-9:]))
   text = '\n'.join(lines)
   if len(text) > 8500:
     text = '\n'.join(lines[:3]) + '\n...[some earlier events omitted]...\n' + text[-6000:]
   return text
 class ConversationContext:
   def __init__(self) -> None:
     self.messages: List[Dict[str, Any]] = []
     self.total_input_tokens: int = 0
     self.total_output_tokens: int = 0
     self.last_input_tokens: int = 0
     self.last_context_estimate: int = 0
     self.api_calls: int = 0
     self.budget_warned: bool = False
     self.on_append: Optional[Callable[[Dict[str, Any]], None]] = None
   @property
   def total_tokens(self) -> int:
     return self.total_input_tokens + self.total_output_tokens
   def record_usage(self, input_tokens: int, output_tokens: int, update_context: bool = True) -> None:
     if update_context:
       self.last_context_estimate = self.estimate_tokens()
       if input_tokens > 0:
         self.last_input_tokens = input_tokens
       else:
         self.last_input_tokens = self.estimate_tokens()
     self.total_input_tokens += max(0, input_tokens)
     self.total_output_tokens += max(0, output_tokens)
     self.api_calls += 1
   def estimate_tokens(self) -> int:
     """Fast heuristic token estimator (~4 chars per token)."""
     chars = 0
     for m in self.messages:
       chars += len(str(m.get("content", "")))
       if (m.get("provider_data") or {}).get("provider") == "deepseek":
         chars += len(str(m.get("thought", "")))
       for tc in m.get("tool_calls", []):
         chars += len(str(tc.get("name", ""))) + len(json.dumps(tc.get("arguments", {})))
     return max(1, chars // 4)
   def current_context_estimate(self) -> int:
     if not self.messages:
       return 0
     current = self.estimate_tokens()
     if self.last_input_tokens:
       current = max(current, self.last_input_tokens + max(0, current - self.last_context_estimate))
     return current
   def _append(self, message: Dict[str, Any]) -> None:
     self.messages.append(message)
     if self.on_append:
       self.on_append(message)
   def add_user(self, content: str) -> None:
     self._append({"role": "user", "content": content})
   def add_assistant(
     self,
     content: str,
     tool_calls: Optional[List[Dict[str, Any]]] = None,
     thought: str = "",
     provider_data: Optional[Dict[str, Any]] = None,
   ) -> None:
     entry: Dict[str, Any] = {"role": "assistant", "content": content}
     if tool_calls:
       entry["tool_calls"] = tool_calls
     if thought:
       entry["thought"] = thought
     if provider_data:
       entry["provider_data"] = provider_data
     self._append(entry)
   def add_tool_result(
     self,
     tool_call_id: str,
     name: str,
     content: str,
     is_error: bool = False,
   ) -> None:
     self._append(
       {
         "role": "tool",
         "tool_call_id": tool_call_id,
         "name": name,
         "content": content,
         "is_error": is_error,
       }
     )
   def clear(self) -> None:
     self.messages.clear()
     self.last_input_tokens = 0
     self.last_context_estimate = 0
   def needs_compaction(self, context_window: int) -> bool:
     threshold = int(context_window * 0.78)
     est = self.current_context_estimate()
     return est >= threshold and len(self.messages) > 6
   def compact(self, keep_recent_groups: int = 4) -> bool:
     """
         Safely compact older conversation turns while preserving valid
         (user -> assistant -> tool_result) atomic turn boundaries.
         """
     keep_recent_groups = max(1, int(keep_recent_groups))
     if len(self.messages) <= 4:
       shrunk = False
       for m in self.messages:
         if m.get("role") == "tool" and len(str(m.get("content", ""))) > 4000:
           txt = str(m["content"])
           m["content"] = txt[:1800] + "\n...[compacted middle]...\n" + txt[-1200:]
           shrunk = True
       if shrunk:
         self.last_input_tokens = self.estimate_tokens()
         self.last_context_estimate = self.last_input_tokens
       return shrunk
     groups: List[List[Dict[str, Any]]] = []
     current: List[Dict[str, Any]] = []
     for m in self.messages:
       if m["role"] == "user" and current:
         groups.append(current)
         current = [m]
       else:
         current.append(m)
     if current:
       groups.append(current)
     if len(groups) <= keep_recent_groups:
       shrunk = False
       for grp in groups[:-1]:
         for m in grp:
           if m.get("role") == "tool" and len(str(m.get("content", ""))) > 2500:
             txt = str(m["content"])
             m["content"] = txt[:1200] + "\n...[compacted]...\n" + txt[-800:]
             shrunk = True
       if not shrunk and groups:
         for m in groups[-1]:
           if m.get("role") == "tool" and len(str(m.get("content", ""))) > 4000:
             txt = str(m["content"])
             m["content"] = txt[:1800] + "\n...[compacted middle; re-read if needed]...\n" + txt[-1200:]
             shrunk = True
       if shrunk:
         self.last_input_tokens = self.estimate_tokens()
         self.last_context_estimate = self.last_input_tokens
       return shrunk
     older_groups = groups[:-keep_recent_groups]
     recent_groups = groups[-keep_recent_groups:]
     summary_text = _summarize_older_groups(older_groups)
     compacted_messages: List[Dict[str, Any]] = [
       {"role": "user", "content": summary_text},
       {"role": "assistant", "content": "Understood. I have the context from our earlier steps and am ready to continue."},
     ]
     for grp in recent_groups:
       for m in grp:
         if m.get("role") == "tool" and len(str(m.get("content", ""))) > 12000:
           txt = str(m["content"])
           m = dict(m)
           m["content"] = txt[:6000] + "\n...[truncated]...\n" + txt[-4000:]
         compacted_messages.append(m)
     self.messages = compacted_messages
     self.last_input_tokens = self.estimate_tokens()
     self.last_context_estimate = self.last_input_tokens
     return True
   def save_to_file(self, path: Path) -> None:
     path.parent.mkdir(parents=True, exist_ok=True)
     payload = {
       "total_input_tokens": self.total_input_tokens,
       "total_output_tokens": self.total_output_tokens,
       "api_calls": self.api_calls,
       "messages": self.messages,
     }
     flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
     if hasattr(os, "O_NOFOLLOW"):
       flags |= os.O_NOFOLLOW
     fd = os.open(str(path), flags, 0o600)
     with os.fdopen(fd, "w", encoding="utf-8") as f:
       json.dump(payload, f, indent=2, ensure_ascii=False)
     if os.name != "nt":
       os.chmod(path, 0o600)
   def load_from_file(self, path: Path) -> int:
     raw = json.loads(path.read_text(encoding="utf-8"))
     msgs = raw.get("messages", [])
     if isinstance(msgs, list):
       self.messages = msgs
     self.total_input_tokens = int(raw.get("total_input_tokens", 0))
     self.total_output_tokens = int(raw.get("total_output_tokens", 0))
     self.api_calls = int(raw.get("api_calls", 0))
     return len(self.messages)
 return locals()
_dm_install('docmind.core.context', _dm_module_12, False)

# ===== docmind/core/history.py (included source) =====
def _dm_module_13():
 """Private-by-default, compressed automatic conversation history.

 Each conversation is a single gzip-compressed JSON file. Writes replace the
 same file atomically; older snapshots are not accumulated. Compression is not
 encryption. Nothing from the provider configuration is intentionally stored.
 """
 import copy
 import gzip
 import json
 import os
 import re
 import stat
 import tempfile
 import uuid
 from datetime import datetime, timezone
 from pathlib import Path
 from typing import Any, Callable, Dict, List, Optional
 _ID_RE = re.compile(r"^[0-9a-f]{32}$")
 _HEADER_BYTES = 4096
 _MAX_JSON_BYTES = 128 * 1024 * 1024
 def _now() -> str:
   return datetime.now(timezone.utc).isoformat(timespec="seconds")
 class ConversationHistory:
   def __init__(self, home: Path, on_error: Optional[Callable[[Exception], None]] = None,
         on_fork: Optional[Callable[[], None]] = None) -> None:
     self.directory = Path(home) / "history"
     self.on_error = on_error
     self.on_fork = on_fork
     self._warned = False
     self.new_session()
   def new_session(self, seed: Optional[List[Dict[str, Any]]] = None) -> None:
     self.session_id: Optional[str] = None
     self.created_at = ""
     self.title = ""
     self.records: List[Dict[str, Any]] = copy.deepcopy(seed or [])
     self._expected_stamp: Optional[tuple] = None
   def _ensure_dir(self) -> None:
     if self.directory.is_symlink():
       raise OSError("History directory must not be a symbolic link")
     self.directory.mkdir(mode=0o700, parents=True, exist_ok=True)
     if os.name != "nt":
       os.chmod(self.directory, 0o700)
   def _path(self, session_id: str) -> Path:
     if not _ID_RE.fullmatch(str(session_id)):
       raise ValueError("Invalid history ID")
     return self.directory / (session_id + ".json.gz")
   @staticmethod
   def _stamp(path: Path) -> Optional[tuple]:
     try:
       st = os.stat(str(path), follow_symlinks=False)
       return (st.st_mtime_ns, st.st_size, st.st_ino)
     except FileNotFoundError:
       return None
   def _activate(self) -> None:
     if self.session_id is None:
       self.session_id = uuid.uuid4().hex
       self.created_at = _now()
       for msg in self.records:
         if msg.get("role") == "user" and str(msg.get("content", "")).strip():
           self.title = " ".join(str(msg["content"]).split())[:72]
           break
       if not self.title:
         self.title = "DocMind"
   def append(self, message: Dict[str, Any]) -> None:
     self.records.append(copy.deepcopy(message))
     if self.session_id is None and message.get("role") != "user":
       return
     self._activate()
     self._safe_save()
   def mark_last_user_cancelled(self) -> None:
     for msg in reversed(self.records):
       if msg.get("role") == "user":
         msg["_history_cancelled"] = True
         self._safe_save()
         return
       if msg.get("role") == "assistant" and not msg.get("_history_incomplete"):
         return
   def record_partial(self, text: str) -> None:
     if not text or self.session_id is None:
       return
     self.records.append({"role": "assistant", "content": text, "_history_incomplete": True})
     self._safe_save()
   def _safe_save(self) -> bool:
     if self.session_id is None:
       return True
     try:
       self._write()
       self._warned = False
       return True
     except Exception as exc:
       if not self._warned and self.on_error:
         self._warned = True
         self.on_error(exc)
       return False
   def _write(self) -> None:
     self._ensure_dir()
     assert self.session_id is not None
     path = self._path(self.session_id)
     current = self._stamp(path)
     if current != self._expected_stamp:
       self.session_id = uuid.uuid4().hex
       self.created_at = _now()
       self._expected_stamp = None
       path = self._path(self.session_id)
       if self.on_fork:
         self.on_fork()
     payload = {
       "format": "docmind-conversation",
       "version": 1,
       "id": self.session_id,
       "title": self.title,
       "created_at": self.created_at,
       "updated_at": _now(),
       "messages": self.records,
     }
     raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
     if len(raw) > _MAX_JSON_BYTES:
       raise ValueError("Conversation history exceeds the safe 128 MiB limit")
     tmp = None
     try:
       fd, tmp = tempfile.mkstemp(prefix=".history-", suffix=".tmp", dir=str(self.directory))
       with os.fdopen(fd, "wb") as out:
         with gzip.GzipFile(fileobj=out, mode="wb", compresslevel=6, mtime=0) as gz:
           gz.write(raw)
         out.flush()
         os.fsync(out.fileno())
       os.replace(tmp, path)
       if os.name != "nt":
         os.chmod(path, 0o600)
       self._expected_stamp = self._stamp(path)
     finally:
       if tmp:
         try:
           os.unlink(tmp)
         except OSError:
           pass
   def _read_gzip(self, path: Path, limit: int) -> bytes:
     if path.is_symlink():
       raise OSError("Refusing symbolic-link history file")
     flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
     fd = os.open(str(path), flags)
     with os.fdopen(fd, "rb") as raw:
       with gzip.GzipFile(fileobj=raw, mode="rb") as gz:
         return gz.read(limit)
   def list_sessions(self) -> List[Dict[str, Any]]:
     if not self.directory.exists():
       return []
     if self.directory.is_symlink():
       raise OSError("History directory must not be a symbolic link")
     found: List[Dict[str, Any]] = []
     for path in self.directory.glob("*.json.gz"):
       session_id = path.name[:-8]
       if not _ID_RE.fullmatch(session_id) or path.is_symlink():
         continue
       try:
         prefix = self._read_gzip(path, _HEADER_BYTES)
         marker = prefix.find(b',"messages":')
         if marker < 0:
           continue
         header = json.loads(prefix[:marker] + b"}")
         if header.get("format") != "docmind-conversation" or header.get("id") != session_id:
           continue
         stamp = self._stamp(path)
         if stamp is None:
           continue
         found.append({"id": session_id, "title": str(header.get("title") or "DocMind")[:72],
                "updated_at": str(header.get("updated_at") or ""), "stamp": stamp[0]})
       except (OSError, EOFError, ValueError, TypeError, UnicodeError, json.JSONDecodeError):
         continue
     return sorted(found, key=lambda row: (row["stamp"], row["id"]), reverse=True)
   def delete(self, session_id: str) -> bool:
     """Delete exactly one selected history file; return whether it was active."""
     if self.directory.is_symlink():
       raise OSError("History directory must not be a symbolic link")
     path = self._path(session_id)
     if path.is_symlink():
       raise OSError("Refusing symbolic-link history file")
     if (os.stat in os.supports_dir_fd and os.unlink in os.supports_dir_fd
         and hasattr(os, "O_DIRECTORY") and hasattr(os, "O_NOFOLLOW")):
       fd = os.open(str(self.directory), os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
       try:
         info = os.stat(path.name, dir_fd=fd, follow_symlinks=False)
         if not stat.S_ISREG(info.st_mode):
           raise OSError("History entry is not a regular file")
         os.unlink(path.name, dir_fd=fd)
       finally:
         os.close(fd)
     else:
       if path.is_symlink() or not path.is_file():
         raise OSError("History entry is not a regular file")
       path.unlink()
     was_active = self.session_id == session_id
     if was_active:
       self.new_session()
     return was_active
   def load(self, session_id: str) -> List[Dict[str, Any]]:
     path = self._path(session_id)
     before = self._stamp(path)
     raw = self._read_gzip(path, _MAX_JSON_BYTES + 1)
     after = self._stamp(path)
     if before != after:
       raise OSError("Conversation changed while it was being loaded")
     if len(raw) > _MAX_JSON_BYTES:
       raise ValueError("History file is too large to load safely")
     payload = json.loads(raw.decode("utf-8"))
     if not isinstance(payload, dict) or payload.get("format") != "docmind-conversation" or payload.get("id") != session_id:
       raise ValueError("Invalid history file")
     records = payload.get("messages")
     if not isinstance(records, list) or not all(isinstance(m, dict) and m.get("role") in ("user", "assistant", "tool") for m in records):
       raise ValueError("Invalid history messages")
     self.session_id = session_id
     self.created_at = str(payload.get("created_at") or _now())
     self.title = str(payload.get("title") or "DocMind")[:72]
     self.records = copy.deepcopy(records)
     self._expected_stamp = after
     for last in reversed(self.records):
       if last.get("_history_incomplete"):
         continue
       if last.get("role") == "user" and not last.get("_history_cancelled"):
         last["_history_cancelled"] = True
       break
     return self.restored_messages()
   def restored_messages(self) -> List[Dict[str, Any]]:
     return [{k: copy.deepcopy(v) for k, v in m.items() if not k.startswith("_history_")}
         for m in self.records if not m.get("_history_cancelled") and not m.get("_history_incomplete")]
 return locals()
_dm_install('docmind.core.history', _dm_module_13, False)

# ===== docmind/core/usage.py (included source) =====
def _dm_module_14():
 """Transparent session usage and rough cost estimates (USD, never a bill).

 Built-in ordinary text prices were checked against vendor pages on 2026-10-29.
 Overrides apply to the provider/model pair. Unknown prices remain unknown.
 Prices exclude caching adjustments, taxes, free tiers and other billed services.
 """
 from datetime import date, datetime, timezone
 from typing import Any, Dict, List, Optional, Tuple
 from docmind.config import DocMindConfig, get_provider_spec
 PRICE_PER_MILLION: Dict[Tuple[str, str], Tuple[float, float]] = {
   ('anthropic','claude-sonnet-5-5'): (2.0,10.0),
   ('anthropic','claude-opus-5-5'): (4.0,20.0),
   ('anthropic','claude-sonnet-4-5-20250929'): (3.0,15.0),
   ('openai','gpt-5.4-mini'): (0.75,4.50),
   ('openai','gpt-5.4-mini-2026-03-17'): (0.75,4.50),
   ('openai','gpt-5.6-terra'): (2.0,12.0),
   ('openai','gpt-5.6-sol'): (4.0,20.0),
   ('openai','gpt-4.1-mini'): (0.40,1.60),
   ('gemini','gemini-3.5-flash-lite'): (0.30,2.50),
   ('gemini','gemini-2.5-flash'): (0.30,2.50),
   ('groq','openai/gpt-oss-120b'): (0.15,0.60),
   ('groq','openai/gpt-oss-20b'): (0.075,0.30),
   ('groq','qwen/qwen3.8-27b'): (0.80,4.0),
   ('deepseek','deepseek-flash'): (0.30,1.20),
   ('deepseek','deepseek-v4-flash'): (0.30,1.20),
   ('deepseek','deepseek-v4-pro'): (1.32,3.96),
 }
 CONTEXT_LIMITS: Dict[Tuple[str, str], int] = {
   ('anthropic','claude-sonnet-5-5'):1_000_000,
   ('anthropic','claude-opus-5-5'):1_000_000,
   ('anthropic','claude-haiku-5-5'):1_000_000,
   ('openai','gpt-5.4-mini'):400_000,
   ('openai','gpt-5.4-mini-2026-03-17'):400_000,
   ('openai','gpt-5.6-terra'):1_050_000,
   ('groq','openai/gpt-oss-120b'):131_072,
   ('groq','openai/gpt-oss-20b'):131_072,
   ('groq','qwen/qwen3.8-27b'):131_072,
   ('gemini','gemini-3.5-flash-lite'):1_048_576,
   ('gemini','gemini-3.8-flash'):1_048_576,
   ('gemini','gemini-3.6-flash'):1_048_576,
   ('gemini','gemini-2.5-flash'):1_048_576,
   ('deepseek','deepseek-flash'):1_000_000,
   ('deepseek','deepseek-v4-flash'):1_000_000,
   ('deepseek','deepseek-v4-pro'):1_000_000,
 }
 def model_key(provider: str, model: str) -> str:
   return str(provider).lower().strip() + ':' + str(model).lower().strip()
 def prices_for(cfg: DocMindConfig, provider: str, model: str, input_tokens: int = 0,
        day: Optional[date] = None, moment: Optional[datetime] = None) -> Optional[Tuple[float, float]]:
   key = model_key(provider,model)
   overrides = getattr(cfg, 'price_overrides', {})
   raw = overrides.get(key) if isinstance(overrides, dict) else None
   if isinstance(raw, (list, tuple)) and len(raw)==2:
     try:
       a,b=float(raw[0]),float(raw[1])
       if 0 <= a < 1e9 and 0 <= b < 1e9:
         return a,b
     except (TypeError,ValueError):
       pass
   if (provider,model) == ('anthropic','claude-haiku-5-5'):
     return (0.50,2.50) if input_tokens > 100_000 else (0.10,0.50)
   if provider=='gemini' and model in ('gemini-3.8-flash','gemini-3.6-flash'):
     return (0.75,3.75) if (day or date.today()) < date(2027,1,1) else (1.50,7.50)
   rate=PRICE_PER_MILLION.get((provider,model))
   if rate and provider=='deepseek':
     now=moment or datetime.now(timezone.utc)
     if now.tzinfo is None:now=now.replace(tzinfo=timezone.utc)
     now=now.astimezone(timezone.utc)
     peak=now.weekday()<5 and (1 <= now.hour < 4 or 6 <= now.hour < 10)
     if not peak:return rate[0]/2,rate[1]/2
   if rate and provider=='openai' and model in ('gpt-5.6-terra','gpt-5.6-sol') and input_tokens>272_000:
     return rate[0]*2,rate[1]*1.5
   return rate
 def context_limit_for(cfg: DocMindConfig) -> Tuple[int, bool]:
   key=model_key(cfg.provider,cfg.model)
   overrides=getattr(cfg,'context_overrides',{})
   override=overrides.get(key) if isinstance(overrides,dict) else None
   if isinstance(override,int) and not isinstance(override,bool) and 1024 <= override <= 100_000_000:
     return override, True
   known=CONTEXT_LIMITS.get((cfg.provider,cfg.model))
   if known:
     return known, True
   return get_provider_spec(cfg.provider).context_window, False
 class UsageTracker:
   """Tracks each successful call separately across model changes."""
   def __init__(self) -> None:
     self.events: List[Dict[str, Any]]=[]
     self.interrupted_attempts=0
     self.live_chars=0
   def mark_interrupted(self) -> None:
     self.interrupted_attempts += 1
     self.live_chars=0
   def record(self,provider:str,model:str,input_tokens:int,output_tokens:int,
        reported_cost:Optional[float]=None, usage_complete:Optional[bool]=None) -> None:
     self.events.append({'provider':provider,'model':model,'input':max(0,input_tokens),
               'output':max(0,output_tokens),'cost':reported_cost,
               'usage_complete':usage_complete,'date':date.today(),
               'timestamp':datetime.now(timezone.utc)})
     self.live_chars=0
   def summary(self,cfg:DocMindConfig) -> Dict[str, Any]:
     known_cost=0.0; missing_cost=0;missing_tokens=0;known_cost_calls=0
     for event in self.events:
       inp,out=event['input'],event['output']
       complete=event.get('usage_complete')
       if complete is None:
         complete=bool(inp or out)
       if not complete:
         missing_tokens+=1
       cost=event.get('cost')
       if isinstance(cost,(int,float)) and not isinstance(cost,bool) and 0<=cost<1e12:
         known_cost+=float(cost);known_cost_calls+=1;continue
       rates=prices_for(cfg,event['provider'],event['model'],inp,event['date'],event['timestamp'])
       if rates is None:
         missing_cost+=1
       else:
         if inp or out or complete:
           known_cost+=(inp*rates[0]+out*rates[1])/1_000_000
           known_cost_calls+=1
         if not complete:
           missing_cost+=1
     return {'cost':known_cost,'missing_cost':missing_cost+self.interrupted_attempts,
         'missing_tokens':missing_tokens+self.interrupted_attempts,'known_cost_calls':known_cost_calls,
         'live_tokens':(self.live_chars+3)//4 if self.live_chars else 0}
 return locals()
_dm_install('docmind.core.usage', _dm_module_14, False)

# ===== docmind/core/streaming.py (included source) =====
def _dm_module_15():
 """Resilient Keep-Alive HTTP/TLS Pool & Bounded SSE Streaming for Anthropic, OpenAI, and Gemini.

 Network I/O uses only Python's standard library, upgraded with:
 - Persistent HTTP/1.1 TLS Keep-Alive connection pooling (thread-safe)
 - OS-level TCP Keep-Alive probes on Windows (SIO_KEEPALIVE_VALS), Linux, and macOS
 - Instant transparent reconnect when a remote server closes an idle pooled socket
 - Safe HTTPS redirect handling without cross-origin credential leakage
 - Forgiving SSE completion when finish_reason/stop_reason + valid JSON already arrived
 """
 import gzip
 import http.client
 import json
 import os
 import socket
 import ssl
 import threading
 import time
 import urllib.error
 import urllib.parse
 import urllib.request
 import zlib
 from collections import OrderedDict
 from typing import Any, Callable, Dict, List, Optional, Tuple
 from docmind import __version__
 from docmind.core.errors import DocMindAPIException, parse_retry_after
 def identified_headers(headers: Dict[str, str]) -> Dict[str, str]:
   """Identify DocMind on every API request while enabling HTTP Keep-Alive."""
   result = dict(headers)
   lower_keys = {str(name).lower() for name in result}
   if "user-agent" not in lower_keys:
     result["User-Agent"] = "DocMind/" + __version__
   if "connection" not in lower_keys:
     result["Connection"] = "keep-alive"
   return result
 MAX_STREAM_BYTES = 8 * 1024 * 1024
 class _NoRedirect(urllib.request.HTTPRedirectHandler):
   def redirect_request(self, req, fp, code, msg, headers, newurl):
     return None
 def _configure_tcp_keepalive(sock: Optional[socket.socket]) -> None:
   """Enable TCP_NODELAY and aggressive kernel TCP keepalive probes to prevent NAT/Wi-Fi/Cloudflare drops."""
   if sock is None:
     return
   try:
     sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
   except OSError:
     pass
   try:
     sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
   except OSError:
     return
   try:
     if os.name == "nt" and hasattr(sock, "ioctl") and hasattr(socket, "SIO_KEEPALIVE_VALS"):
       sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 12000, 5000))
     else:
       if hasattr(socket, "TCP_KEEPIDLE"):
         sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 12)
       elif hasattr(socket, "TCP_KEEPALIVE"):
         sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPALIVE, 12)
       if hasattr(socket, "TCP_KEEPINTVL"):
         sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 5)
       if hasattr(socket, "TCP_KEEPCNT"):
         sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 4)
   except OSError:
     pass
 def _connect_fast_socket(host: str, port: int, timeout: float) -> socket.socket:
   """IPv4-preferred multi-address connector to avoid broken ISP IPv6 blackholes and DNS stalls."""
   infos = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
   if not infos:
     raise OSError(f"DNS resolution returned no addresses for {host}:{port}")
   infos_sorted = sorted(infos, key=lambda item: 0 if item[0] == socket.AF_INET else 1)
   last_err: Optional[BaseException] = None
   per_addr_timeout = max(3.5, min(float(timeout), 8.0)) if len(infos_sorted) > 1 else max(4.0, float(timeout))
   for af, socktype, proto, _canon, sa in infos_sorted:
     s: Optional[socket.socket] = None
     try:
       s = socket.socket(af, socktype, proto)
       s.settimeout(per_addr_timeout)
       _configure_tcp_keepalive(s)
       s.connect(sa)
       s.settimeout(timeout)
       return s
     except BaseException as exc:
       last_err = exc
       if s is not None:
         try:
           s.close()
         except Exception:
           pass
   if last_err is not None:
     raise last_err
   raise OSError(f"Unable to connect to {host}:{port}")
 class _ResilientHTTPConnection(http.client.HTTPConnection):
   def connect(self) -> None:
     self.sock = _connect_fast_socket(self.host, self.port, self.timeout or 20.0)
     if self._tunnel_host:
       self._tunnel()
 class _ResilientHTTPSConnection(http.client.HTTPSConnection):
   def connect(self) -> None:
     raw_sock = _connect_fast_socket(self.host, self.port, self.timeout or 20.0)
     if self._tunnel_host:
       self.sock = raw_sock
       self._tunnel()
       server_host = self._tunnel_host
     else:
       server_host = self.host
     self.sock = self._context.wrap_socket(raw_sock, server_hostname=server_host)
     _configure_tcp_keepalive(self.sock)
 def _is_socket_alive(conn: http.client.HTTPConnection) -> bool:
   """Detect sockets silently closed (FIN/RST) by Cloudflare/API gateways while idle in pool."""
   sock = getattr(conn, "sock", None)
   if sock is None:
     return False
   try:
     if sock.fileno() < 0:
       return False
     import select as _sel
     readable, _, broken = _sel.select([sock], [], [sock], 0.0)
     if broken or readable:
       return False
     return True
   except Exception:
     return False
 def _should_use_env_proxy(scheme: str, host: str) -> bool:
   try:
     proxies = urllib.request.getproxies()
     if scheme.lower() not in proxies:
       return False
     if urllib.request.proxy_bypass(host):
       return False
     return True
   except Exception:
     return False
 class KeepAlivePool:
   """Thread-safe stdlib HTTP/1.1 + TLS Keep-Alive connection pool with dead-socket pruning."""
   MAX_IDLE_PER_ORIGIN = 4
   IDLE_TTL_SECONDS = 18.0
   def __init__(self) -> None:
     self._lock = threading.Lock()
     self._idle: Dict[Tuple[str, str, int], List[Tuple[float, http.client.HTTPConnection]]] = {}
     ctx = ssl.create_default_context()
     if hasattr(ssl, "OP_IGNORE_UNEXPECTED_EOF"):
       ctx.options |= ssl.OP_IGNORE_UNEXPECTED_EOF
     self._ssl_ctx = ctx
   def _origin_key(self, parsed: urllib.parse.SplitResult) -> Tuple[str, str, int]:
     scheme = parsed.scheme.lower()
     host = (parsed.hostname or "").lower()
     port = parsed.port or (443 if scheme == "https" else 80)
     return (scheme, host, port)
   def drop_origin(self, url: str) -> None:
     """Purge all pooled sockets for an origin after any network/stream hiccup."""
     try:
       key = self._origin_key(urllib.parse.urlsplit(url))
     except Exception:
       return
     with self._lock:
       stale_list = self._idle.pop(key, [])
     for _, conn in stale_list:
       try:
         conn.close()
       except Exception:
         pass
   def _checkout(self, key: Tuple[str, str, int], connect_timeout: float) -> Tuple[http.client.HTTPConnection, bool]:
     now = time.monotonic()
     with self._lock:
       bucket = self._idle.get(key) or []
       while bucket:
         ts, conn = bucket.pop()
         if (now - ts) <= self.IDLE_TTL_SECONDS and _is_socket_alive(conn):
           return conn, True
         try:
           conn.close()
         except Exception:
           pass
     scheme, host, port = key
     if scheme == "https":
       conn = _ResilientHTTPSConnection(host, port, timeout=connect_timeout, context=self._ssl_ctx)
     else:
       conn = _ResilientHTTPConnection(host, port, timeout=connect_timeout)
     return conn, False
   def release(self, key: Tuple[str, str, int], conn: Optional[http.client.HTTPConnection], reusable: bool) -> None:
     if conn is None:
       return
     if not reusable or not _is_socket_alive(conn):
       try:
         conn.close()
       except Exception:
         pass
       return
     with self._lock:
       bucket = self._idle.setdefault(key, [])
       if len(bucket) >= self.MAX_IDLE_PER_ORIGIN:
         _, oldest = bucket.pop(0)
         try:
           oldest.close()
         except Exception:
           pass
       bucket.append((time.monotonic(), conn))
   def open_request(
     self,
     url: str,
     headers: Dict[str, str],
     body: bytes,
     timeout: float,
     validate_url: Optional[Callable[[str], None]] = None,
   ) -> Tuple[Any, Callable[[bool], None]]:
     current_url = url
     current_headers = identified_headers(headers)
     connect_timeout = max(6.0, min(18.0, float(timeout)))
     read_timeout = max(float(timeout), 45.0)
     for _hop in range(4):
       parsed = urllib.parse.urlsplit(current_url)
       if validate_url is not None:
         base_no_query = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))
         validate_url(base_no_query)
       scheme = parsed.scheme.lower()
       host = parsed.hostname or ""
       if _should_use_env_proxy(scheme, host):
         req = urllib.request.Request(current_url, data=body, headers=current_headers, method="POST")
         resp = urllib.request.build_opener(_NoRedirect()).open(req, timeout=read_timeout)
         return resp, (lambda _ok: resp.close())
       key = self._origin_key(parsed)
       path_and_query = (parsed.path or "/") + (("?" + parsed.query) if parsed.query else "")
       last_stale_exc: Optional[BaseException] = None
       for attempt_idx in range(3):
         conn, was_reused = self._checkout(key, connect_timeout)
         try:
           if getattr(conn, "sock", None) is None:
             conn.connect()
           _configure_tcp_keepalive(getattr(conn, "sock", None))
           if getattr(conn, "sock", None) is not None:
             conn.sock.settimeout(read_timeout)
           conn.request("POST", path_and_query, body=body, headers=current_headers)
           resp = conn.getresponse()
           break
         except (
           http.client.RemoteDisconnected,
           http.client.BadStatusLine,
           http.client.CannotSendRequest,
           http.client.ResponseNotReady,
           BrokenPipeError,
           ConnectionResetError,
           ConnectionAbortedError,
           TimeoutError,
           socket.timeout,
           ssl.SSLError,
           OSError,
         ) as exc:
           self.release(key, conn, False)
           last_stale_exc = exc
           if was_reused or attempt_idx < 2:
             if not was_reused:
               time.sleep(0.25 * (attempt_idx + 1))
             continue
           raise
         except BaseException:
           self.release(key, conn, False)
           raise
       else:
         if last_stale_exc is not None:
           raise last_stale_exc
       if resp.status in (301, 302, 307, 308):
         loc = resp.getheader("Location") or ""
         try:
           resp.read(4096)
         except Exception:
           pass
         self.release(key, conn, not resp.will_close)
         if not loc:
           raise urllib.error.HTTPError(current_url, resp.status, resp.reason, resp.headers, None)
         next_url = urllib.parse.urljoin(current_url, loc)
         next_parsed = urllib.parse.urlsplit(next_url)
         if (next_parsed.hostname or "").lower() != host.lower():
           current_headers = {
             k: v for k, v in current_headers.items()
             if k.lower() not in ("authorization", "x-api-key", "x-goog-api-key")
           }
         current_url = next_url
         continue
       if resp.status >= 400:
         try:
           err_bytes = resp.read(16384)
         except Exception:
           err_bytes = b""
         self.release(key, conn, False)
         import io
         raise urllib.error.HTTPError(
           current_url, resp.status, resp.reason, resp.headers, io.BytesIO(err_bytes)
         )
       def _finish(reusable: bool, _k=key, _c=conn, _r=resp) -> None:
         can_keep = bool(reusable and not getattr(_r, "will_close", True))
         self.release(_k, _c, can_keep)
       return resp, _finish
     raise urllib.error.URLError("Too many HTTP redirects")
 KEEPALIVE_POOL = KeepAlivePool()
 def _decode_content_encoding(raw: bytes, content_encoding: str) -> bytes:
   enc = (content_encoding or "").strip().lower()
   if enc == "gzip":
     return gzip.decompress(raw)
   if enc == "deflate":
     try:
       return zlib.decompress(raw)
     except zlib.error:
       return zlib.decompress(raw, -zlib.MAX_WBITS)
   return raw
 def _merge_extra(target: dict, incoming: dict) -> None:
   """Keep provider-specific opaque metadata, including tool signatures."""
   for key, value in incoming.items():
     if isinstance(value, dict) and isinstance(target.get(key), dict):
       _merge_extra(target[key], value)
     else:
       target[key] = value
 class _OpenAIAccumulator:
   def __init__(self, emit: Callable[[str], None]):
     self.emit = emit
     self.text: List[str] = []
     self.reasoning: List[str] = []
     self.reasoning_key = "reasoning"
     self.tools: Dict[int, dict] = OrderedDict()
     self.details: List[dict] = []
     self.usage: dict = {}
     self.finish = None
     self.done = False
     self.seen = False
   def feed(self, data: dict) -> None:
     self.seen = True
     if isinstance(data.get("usage"), dict):
       self.usage = data["usage"]
     if isinstance((data.get("x_groq") or {}).get("usage"), dict):
       self.usage = data["x_groq"]["usage"]
     choices = data.get("choices") or []
     if not choices:
       return
     choice = choices[0]
     delta = choice.get("delta") or {}
     if choice.get("finish_reason"):
       self.finish = choice["finish_reason"]
     text = delta.get("content")
     if isinstance(text, str) and text:
       self.text.append(text)
       self.emit(text)
     for key in ("reasoning_content", "reasoning"):
       if isinstance(delta.get(key), str):
         self.reasoning_key = key
         self.reasoning.append(delta[key])
         break
     for detail in delta.get("reasoning_details") or []:
       if not isinstance(detail, dict):
         continue
       dtype, idx, detail_id = detail.get("type"), detail.get("index"), detail.get("id")
       saved = None
       if dtype in ("reasoning.text", "reasoning.summary"):
         for prior in reversed(self.details):
           if prior.get("type") != dtype:
             continue
           if idx is not None and prior.get("index") is not None and prior["index"] != idx:
             continue
           if detail_id and prior.get("id") and detail_id != prior["id"]:
             continue
           if prior.get("signature") and (prior.get("text") or prior.get("summary")):
             break
           saved = prior
           break
       if saved is None:
         saved = {}
         self.details.append(saved)
       for field, value in detail.items():
         if field in ("text", "summary") and isinstance(value, str):
           saved[field] = str(saved.get(field) or "") + value
         elif value is not None:
           saved[field] = value
     for raw in delta.get("tool_calls") or []:
       if not isinstance(raw, dict):
         continue
       idx = raw.get("index", 0)
       if not isinstance(idx, int):
         raise ValueError("Invalid tool call index")
       tool = self.tools.setdefault(idx, {"id": "", "type": "function", "function": {"name": "", "arguments": ""}})
       for key, value in raw.items():
         if key in ("index", "function"):
           continue
         if isinstance(value, dict) and isinstance(tool.get(key), dict):
           _merge_extra(tool[key], value)
         elif value is not None:
           tool[key] = value
       fn = raw.get("function") or {}
       if isinstance(fn, dict):
         for key, value in fn.items():
           if key in ("name", "arguments") and isinstance(value, str):
             prior = tool["function"].get(key, "")
             if key == "name" and prior and value == prior:
               continue
             tool["function"][key] = prior + value
           elif value is not None:
             tool["function"][key] = value
   def result(self) -> dict:
     if not self.seen or (not self.done and not self.finish):
       raise ValueError("Stream ended before the final completion marker")
     calls = [self.tools[k] for k in sorted(self.tools)]
     for call in calls:
       fn = call.get("function") or {}
       if not fn.get("name"):
         raise ValueError("Incomplete streamed tool name")
       raw_args = (fn.get("arguments") or "").strip()
       if raw_args:
         try:
           args = json.loads(raw_args)
         except (ValueError, TypeError) as exc:
           raise ValueError("Incomplete streamed tool arguments") from exc
         if not isinstance(args, dict):
           raise ValueError("Streamed tool arguments must be a JSON object")
     msg: dict = {"role": "assistant", "content": "".join(self.text)}
     if calls:
       msg["tool_calls"] = calls
     if self.reasoning:
       msg[self.reasoning_key] = "".join(self.reasoning)
     if self.details:
       msg["reasoning_details"] = list(self.details)
     return {"choices": [{"message": msg, "finish_reason": self.finish or "stop"}], "usage": self.usage}
 class _AnthropicAccumulator:
   def __init__(self, emit: Callable[[str], None]):
     self.emit = emit
     self.blocks: Dict[int, dict] = OrderedDict()
     self.inputs: Dict[int, List[str]] = {}
     self.usage: dict = {}
     self.stop = None
     self.done = False
     self.seen = False
   def feed(self, data: dict) -> None:
     self.seen = True
     typ = data.get("type")
     if typ == "message_start":
       self.usage.update((data.get("message") or {}).get("usage") or {})
     elif typ == "content_block_start":
       idx = data.get("index")
       if not isinstance(idx, int):
         raise ValueError("Invalid content block index")
       block = dict(data.get("content_block") or {})
       self.blocks[idx] = block
       if block.get("type") == "text" and block.get("text"):
         self.emit(str(block["text"]))
     elif typ == "content_block_delta":
       idx = data.get("index")
       if idx not in self.blocks:
         raise ValueError("Delta for missing content block")
       block = self.blocks[idx]
       delta = data.get("delta") or {}
       dtype = delta.get("type")
       if dtype == "text_delta":
         piece = str(delta.get("text") or "")
         block["text"] = str(block.get("text") or "") + piece
         if piece:
           self.emit(piece)
       elif dtype == "input_json_delta":
         self.inputs.setdefault(idx, []).append(str(delta.get("partial_json") or ""))
       elif dtype == "thinking_delta":
         block["thinking"] = str(block.get("thinking") or "") + str(delta.get("thinking") or "")
       elif dtype == "signature_delta":
         block["signature"] = str(block.get("signature") or "") + str(delta.get("signature") or "")
       elif dtype == "citations_delta" and delta.get("citation"):
         block.setdefault("citations", []).append(delta["citation"])
     elif typ == "message_delta":
       self.stop = (data.get("delta") or {}).get("stop_reason") or self.stop
       self.usage.update(data.get("usage") or {})
     elif typ == "message_stop":
       self.done = True
   def result(self) -> dict:
     if not self.seen or (not self.done and not self.stop):
       raise ValueError("Anthropic stream ended before message_stop")
     for idx, chunks in self.inputs.items():
       joined = "".join(chunks).strip()
       if not joined:
         self.blocks[idx]["input"] = {}
         continue
       try:
         value = json.loads(joined)
       except (ValueError, TypeError) as exc:
         raise ValueError("Incomplete streamed tool arguments") from exc
       if not isinstance(value, dict):
         raise ValueError("Streamed tool arguments must be a JSON object")
       self.blocks[idx]["input"] = value
     for block in self.blocks.values():
       if block.get("type") == "tool_use" and (not block.get("name") or not isinstance(block.get("input", {}), dict)):
         raise ValueError("Incomplete streamed tool call")
     return {"content": [self.blocks[k] for k in sorted(self.blocks)], "stop_reason": self.stop or "end_turn", "usage": self.usage}
 class _GeminiAccumulator:
   def __init__(self, emit: Callable[[str], None]):
     self.emit = emit
     self.parts: List[dict] = []
     self.usage: dict = {}
     self.finish = None
     self.feedback: dict = {}
     self.seen = False
   def feed(self, data: dict) -> None:
     self.seen = True
     if isinstance(data.get("usageMetadata"), dict):
       self.usage = data["usageMetadata"]
     if isinstance(data.get("promptFeedback"), dict):
       self.feedback = data["promptFeedback"]
     candidates = data.get("candidates") or []
     if not candidates:
       return
     cand = candidates[0]
     if cand.get("finishReason"):
       self.finish = cand["finishReason"]
     for part in ((cand.get("content") or {}).get("parts") or []):
       if not isinstance(part, dict) or not part:
         continue
       if set(part) == {"text"} and not part["text"]:
         continue
       saved = dict(part)
       text = saved.get("text")
       if isinstance(text, str) and text and not saved.get("thought"):
         self.emit(text)
       if (
         self.parts
         and isinstance(text, str)
         and set(saved).issubset({"text", "thought"})
         and set(self.parts[-1]).issubset({"text", "thought"})
         and bool(saved.get("thought")) == bool(self.parts[-1].get("thought"))
       ):
         self.parts[-1]["text"] = str(self.parts[-1].get("text") or "") + text
       else:
         self.parts.append(saved)
   def result(self) -> dict:
     if not self.seen or (not self.finish and not self.feedback.get("blockReason")):
       raise ValueError("Gemini stream ended before finishReason")
     for part in self.parts:
       if "functionCall" in part:
         fc = part["functionCall"]
         if not isinstance(fc, dict) or not fc.get("name") or not isinstance(fc.get("args", {}), dict):
           raise ValueError("Incomplete streamed function call")
     if self.feedback.get("blockReason") and not self.parts:
       return {"candidates": [], "promptFeedback": self.feedback, "usageMetadata": self.usage}
     return {"candidates": [{"content": {"role": "model", "parts": self.parts}, "finishReason": self.finish}], "usageMetadata": self.usage}
 def stream_json(
   url: str,
   headers: Dict[str, str],
   payload: Dict[str, Any],
   timeout: float,
   provider_name: str,
   model_name: str,
   protocol: str,
   emit: Callable[[str], None],
   validate: Callable[[str], None],
   redact: Callable[[str, Dict[str, str]], str],
 ) -> dict:
   """Stream an SSE request over the persistent Keep-Alive pool with strict tool safety."""
   parsed = urllib.parse.urlsplit(url)
   if parsed.query and not (protocol == "gemini" and parsed.query == "alt=sse"):
     raise DocMindAPIException("Invalid stream URL query", status_code=400, provider_name=provider_name, model_name=model_name)
   validate(urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", parsed.fragment)))
   accum_type = {"openai": _OpenAIAccumulator, "anthropic": _AnthropicAccumulator, "gemini": _GeminiAccumulator}[protocol]
   accepted = [False]
   def safe_emit(text: str) -> None:
     if text:
       accepted[0] = True
       emit(text)
   accum = accum_type(safe_emit)
   request_headers = identified_headers(headers)
   request_headers["Accept"] = "text/event-stream"
   body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
   def fail(message: Any, status: Optional[int] = None, response: str = "", retry: Optional[float] = None) -> DocMindAPIException:
     error = DocMindAPIException(
       redact(str(message), headers),
       status_code=status,
       response_body=redact(str(response)[:16384], headers),
       retry_after=retry,
       provider_name=provider_name,
       model_name=model_name,
     )
     error.emitted_text = accepted[0]
     error.partial_stream = accepted[0]
     error.stream_interrupted = bool(getattr(accum, "seen", False))
     return error
   done_cb: Optional[Callable[[bool], None]] = None
   stream_clean = False
   try:
     response, done_cb = KEEPALIVE_POOL.open_request(url, request_headers, body, timeout=timeout, validate_url=validate)
     ctype = (response.headers.get("Content-Type") or "").lower()
     cenc = response.headers.get("Content-Encoding") or ""
     if "text/event-stream" not in ctype:
       raw = response.read(MAX_STREAM_BYTES + 1)
       if len(raw) > MAX_STREAM_BYTES:
         raise fail("API response exceeded 8 MiB", response.status)
       raw = _decode_content_encoding(raw, cenc)
       stream_clean = True
       try:
         result = json.loads(raw.decode("utf-8"))
       except (UnicodeError, ValueError) as exc:
         raise fail("Invalid streaming response", response.status) from exc
       if not isinstance(result, dict):
         raise fail("Unexpected API response", response.status)
       return result
     total = 0
     pending: List[str] = []
     def process_event() -> None:
       if not pending:
         return
       value = "\n".join(pending)
       pending.clear()
       if value == "[DONE]":
         if hasattr(accum, "done"):
           accum.done = True
         return
       try:
         data = json.loads(value)
       except ValueError as exc:
         raise fail("Invalid event in API stream") from exc
       if not isinstance(data, dict):
         raise fail("Invalid event in API stream")
       if isinstance(data.get("error"), dict):
         err = data["error"]
         code = err.get("status") if isinstance(err.get("status"), int) else err.get("code")
         code = code if isinstance(code, int) and not isinstance(code, bool) else None
         raise fail(str(err.get("message") or "API stream error"), code, json.dumps(data))
       accum.feed(data)
     eof_exc: Optional[BaseException] = None
     while True:
       try:
         raw_line = response.readline(MAX_STREAM_BYTES + 1)
       except http.client.IncompleteRead as inc_exc:
         eof_exc = inc_exc
         partial_bytes = getattr(inc_exc, "partial", b"") or b""
         if partial_bytes:
           for sub_raw in partial_bytes.splitlines():
             sub_line = sub_raw.decode("utf-8", errors="ignore").rstrip("\r\n")
             if not sub_line:
               process_event()
             elif sub_line.startswith("data:"):
               pending.append(sub_line[5:].lstrip(" "))
         break
       except (
         http.client.RemoteDisconnected,
         ConnectionResetError,
         ConnectionAbortedError,
         BrokenPipeError,
         ssl.SSLError,
         TimeoutError,
         socket.timeout,
         OSError,
       ) as sock_exc:
         eof_exc = sock_exc
         break
       if not raw_line:
         break
       total += len(raw_line)
       if total > MAX_STREAM_BYTES:
         raise fail("API stream exceeded 8 MiB")
       try:
         line = raw_line.decode("utf-8").rstrip("\r\n")
       except UnicodeError as exc:
         raise fail("Invalid UTF-8 in API stream") from exc
       if not line:
         process_event()
       elif line.startswith("data:"):
         pending.append(line[5:].lstrip(" "))
     try:
       process_event()
     except Exception:
       if eof_exc is None:
         raise
     stream_clean = eof_exc is None
     if eof_exc is not None:
       try:
         return accum.result()
       except Exception:
         KEEPALIVE_POOL.drop_origin(url)
         raise fail(f"{type(eof_exc).__name__}: {eof_exc}") from eof_exc
     try:
       return accum.result()
     except (TypeError, ValueError) as exc:
       stream_clean = False
       raise fail(str(exc)) from exc
   except urllib.error.HTTPError as exc:
     try:
       details = exc.read(16384).decode("utf-8", errors="replace")
     except Exception:
       details = ""
     retry_header = exc.headers.get("Retry-After") if exc.headers else None
     retry = parse_retry_after(retry_header)
     raise fail(str(exc), exc.code, details, retry) from exc
   except DocMindAPIException:
     raise
   except Exception as exc:
     raise fail(f"{type(exc).__name__}: {exc}") from exc
   finally:
     if done_cb is not None:
       try:
         done_cb(stream_clean)
       except Exception:
         pass
 return locals()
_dm_install('docmind.core.streaming', _dm_module_15, False)

# ===== docmind/core/providers.py (included source) =====
def _dm_module_16():
 """
 DocMind Unified Multi-Provider AI Client
 Supports Anthropic (Claude), OpenAI, Google Gemini, Groq, OpenRouter, DeepSeek,
 and Custom/Local OpenAI-compatible servers (Ollama, LM Studio, vLLM).
 Includes strict native tool argument validation and prompt-based tool fallback.
 """
 import json
 import hashlib
 import ipaddress
 import re
 import time
 import urllib.parse
 import urllib.error
 import urllib.request
 import uuid
 from dataclasses import dataclass, field
 from typing import Any, Callable, Dict, List, Optional, Tuple
 from docmind.config import DocMindConfig, get_provider_spec
 from docmind.core.errors import DocMindAPIException, classify_exception, parse_retry_after, request_token_ceiling, retry_delay
 from docmind.core.streaming import KEEPALIVE_POOL, _decode_content_encoding, identified_headers, stream_json
 HAS_HTTPX = False
 @dataclass
 class ToolCall:
   id: str
   name: str
   arguments: Dict[str, Any]
   metadata: Dict[str, Any] = field(default_factory=dict)
 @dataclass
 class ModelResponse:
   text: str = ""
   thought: str = ""
   tool_calls: List[ToolCall] = field(default_factory=list)
   stop_reason: str = "stop"
   input_tokens: int = 0
   output_tokens: int = 0
   reported_cost_usd: Optional[float] = None
   usage_complete: Optional[bool] = None
   provider_data: Dict[str, Any] = field(default_factory=dict)
   @property
   def total_tokens(self) -> int:
     return self.input_tokens + self.output_tokens
 def _complete_usage(usage: Any, required: Tuple[str, ...]) -> bool:
   if not isinstance(usage, dict):
     return False
   for key in required:
     value = usage.get(key)
     if value is None or isinstance(value, bool):
       return False
     try:
       if int(value) < 0:
         return False
     except (TypeError, ValueError, OverflowError):
       return False
   return True
 def _usage_int(usage: Dict[str, Any], key: str) -> int:
   value = usage.get(key, 0)
   if isinstance(value, bool):
     return 0
   try:
     return max(0, int(value))
   except (TypeError, ValueError, OverflowError):
     return 0
 def heal_json_arguments(raw: Any) -> Dict[str, Any]:
   """Safely parse tool arguments even if an LLM emits slightly malformed JSON."""
   if isinstance(raw, dict):
     return raw
   if not raw or not isinstance(raw, str):
     return {}
   s = raw.strip()
   if not s:
     return {}
   try:
     parsed = json.loads(s)
     return parsed if isinstance(parsed, dict) else {"value": parsed}
   except Exception:
     pass
   s_clean = re.sub(r"^```(?:json)?\s*|\s*```$", "", s, flags=re.IGNORECASE | re.DOTALL).strip()
   s_clean = re.sub(r",\s*([}\]])", r"\1", s_clean)
   try:
     parsed = json.loads(s_clean)
     return parsed if isinstance(parsed, dict) else {"value": parsed}
   except Exception:
     return {}
 def reasoning_control_for(provider: str, model: str) -> str:
   """Return a known direct-API effort protocol, otherwise leave server defaults.

     Deliberately whitelist documented model families; an OpenAI-compatible
     gateway or similarly named unsupported model must not receive new fields.
     """
   name = str(model or '').lower()
   if name.startswith('models/'):
     name = name[len('models/'):]
   def matches(ids: Tuple[str, ...]) -> bool:
     return any(name == item or name.startswith(item + '-') for item in ids)
   if provider == 'openai' and (name == 'gpt-5.6' or matches(('gpt-5.4-mini', 'gpt-5.6-terra', 'gpt-5.6-sol'))):
     return 'openai'
   if provider == 'anthropic' and matches(('claude-sonnet-5-5', 'claude-opus-5-5', 'claude-haiku-5-5',
                        'claude-sonnet-4-6', 'claude-opus-4-6')):
     return 'anthropic'
   if provider == 'gemini' and matches(('gemini-3.5-flash-lite', 'gemini-3.6-flash', 'gemini-3.8-flash')):
     return 'gemini'
   if provider == 'groq' and name in ('openai/gpt-oss-20b', 'openai/gpt-oss-120b', 'qwen/qwen3.8-27b'):
     return 'groq'
   if provider == 'deepseek' and name in ('deepseek-flash', 'deepseek-v4-pro'):
     return 'deepseek'
   return ''
 def reasoning_effort_for(cfg: DocMindConfig) -> str:
   """Map the user's level to a documented value for the selected model."""
   value = getattr(cfg, 'reasoning_effort', 'high')
   kind = reasoning_control_for(cfg.provider, cfg.model)
   if not kind or value == 'default':
     return ''
   if value in ('low', 'medium', 'high'):
     return 'high' if kind == 'deepseek' and value == 'medium' else value
   if value == 'max':
     if kind in ('anthropic', 'deepseek'):
       return 'max'
     if kind == 'openai':
       model = str(cfg.model).lower()
       if model.startswith('models/'):
         model = model[len('models/'):]
       return 'max' if model.startswith('gpt-5.6') else 'xhigh'
     return 'high'
   return ''
 def _native_tool_arguments(raw: Any, provider_name: str, model_name: str) -> Dict[str, Any]:
   """Parse tool arguments safely; accept empty string/None as {} for parameterless tools."""
   if raw is None:
     return {}
   if isinstance(raw, dict):
     return raw
   if isinstance(raw, str):
     s = raw.strip()
     if not s:
       return {}
     try:
       parsed = json.loads(s)
       if isinstance(parsed, dict):
         return parsed
     except ValueError:
       s_clean = re.sub(r"^```(?:json)?\s*|\s*```$", "", s, flags=re.IGNORECASE | re.DOTALL).strip()
       s_clean = re.sub(r",\s*([}\]])", r"\1", s_clean)
       if s_clean.startswith("{") and s_clean.endswith("}"):
         try:
           parsed = json.loads(s_clean)
           if isinstance(parsed, dict):
             return parsed
         except ValueError:
           pass
   exc = DocMindAPIException(
     "The model returned invalid or incomplete tool arguments; no tool was executed.",
     status_code=200, provider_name=provider_name, model_name=model_name,
   )
   exc.invalid_tool_arguments = True
   raise exc
 def _clean_gemini_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
   """Remove JSON Schema fields rejected by Gemini's OpenAPI subset."""
   disallowed = {"additionalProperties", "$schema", "default", "title"}
   cleaned: Dict[str, Any] = {}
   for k, v in schema.items():
     if k in disallowed:
       continue
     if isinstance(v, dict):
       cleaned[k] = _clean_gemini_schema(v)
     elif isinstance(v, list):
       cleaned[k] = [_clean_gemini_schema(i) if isinstance(i, dict) else i for i in v]
     else:
       cleaned[k] = v
   return cleaned
 PROMPT_TOOL_REGEX = re.compile(r"<docmind_tool>\s*(\{.*?\})\s*</docmind_tool>", re.DOTALL)
 def _build_prompt_tool_instructions(tools: List[Dict[str, Any]]) -> str:
   """Fallback tool instructions for models without native tool-calling API support."""
   lines = [
     "\n\n## TOOL CALLING FORMAT",
     "To use a tool, output ONLY a block in this exact XML+JSON format:",
     '<docmind_tool>{"name": "tool_name", "arguments": {"param": "value"}}</docmind_tool>',
     "Available tools:",
   ]
   for tool in tools:
     lines.append(f"- {tool['name']}: {tool['description']} | Schema: {json.dumps(tool['parameters'])}")
   return "\n".join(lines)
 def _extract_prompt_tool_calls(text: str, provider_name: str = "AI", model_name: str = "") -> Tuple[str, List[ToolCall]]:
   calls: List[ToolCall] = []
   matches = list(PROMPT_TOOL_REGEX.finditer(text))
   if text.count("<docmind_tool>") != len(matches) or text.count("</docmind_tool>") != len(matches):
     _native_tool_arguments(None, provider_name, model_name)
   for match in matches:
     obj = heal_json_arguments(match.group(1))
     name = obj.get("name")
     if not isinstance(name, str) or not name.strip() or "arguments" not in obj:
       _native_tool_arguments(None, provider_name, model_name)
     args = _native_tool_arguments(obj["arguments"], provider_name, model_name)
     calls.append(ToolCall(id=f"call_{uuid.uuid4().hex[:10]}", name=name.strip(), arguments=args))
   cleaned_text = PROMPT_TOOL_REGEX.sub("", text).strip()
   return cleaned_text, calls
 class _NoRedirect(urllib.request.HTTPRedirectHandler):
   def redirect_request(self, req, fp, code, msg, headers, newurl):
     return None
 def _validate_api_url(url: str) -> None:
   """Require HTTPS except for an explicit loopback endpoint, without URL credentials."""
   try:
     parsed = urllib.parse.urlsplit(url)
     host = (parsed.hostname or "").lower().rstrip(".")
     _ = parsed.port
     if not host or parsed.username is not None or parsed.password is not None or parsed.query or parsed.fragment:
       raise ValueError("Invalid host or embedded credentials, query, or fragment")
     if parsed.scheme == "https":
       return
     if parsed.scheme == "http":
       try:
         local = host == "localhost" or ipaddress.ip_address(host).is_loopback
       except ValueError:
         local = host == "localhost"
       if local:
         return
     raise ValueError("HTTPS is required except for localhost / loopback")
   except (TypeError, ValueError) as exc:
     raise DocMindAPIException(
       "Güvensiz veya geçersiz API adresi: HTTPS kullanın; HTTP sadece localhost için kullanılabilir.",
       status_code=400,
     ) from exc
 def _redact_known_keys(text: str, headers: Dict[str, str]) -> str:
   result = str(text or "")
   for name, value in headers.items():
     if name.lower() in ("authorization", "x-api-key", "x-goog-api-key") and value:
       result = result.replace(value, "[REDACTED]")
       token = value[7:].strip() if value.lower().startswith("bearer ") else value
       if token:
         result = result.replace(token, "[REDACTED]")
   return result
 class HttpClient:
   """TLS-verified Keep-Alive HTTP JSON client with stale-socket auto-reconnect."""
   MAX_RESPONSE_BYTES = 8 * 1024 * 1024
   @staticmethod
   def post_json(
     url: str,
     headers: Dict[str, str],
     payload: Dict[str, Any],
     timeout: float = 180.0,
     provider_name: str = "AI",
     model_name: str = "",
   ) -> Dict[str, Any]:
     try:
       _validate_api_url(url)
     except DocMindAPIException as exc:
       exc.provider_name = provider_name
       exc.model_name = model_name
       raise
     headers = identified_headers(headers)
     if not any(str(name).lower() == "accept" for name in headers):
       headers["Accept"] = "application/json"
     if not any(str(name).lower() == "accept-encoding" for name in headers):
       headers["Accept-Encoding"] = "gzip, deflate"
     body_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
     def make_error(message: str, status: Optional[int] = None, body: str = "", retry: Optional[float] = None) -> DocMindAPIException:
       return DocMindAPIException(
         message=_redact_known_keys(message, headers), status_code=status,
         response_body=_redact_known_keys(body[:16384], headers), retry_after=retry,
         provider_name=provider_name, model_name=model_name,
       )
     def decode_json(raw: bytes, status: int, content_encoding: str = "") -> Dict[str, Any]:
       if len(raw) > HttpClient.MAX_RESPONSE_BYTES:
         raise make_error("API response exceeded 8 MiB", status)
       try:
         decoded_bytes = _decode_content_encoding(raw, content_encoding)
         data = json.loads(decoded_bytes.decode("utf-8"))
         if not isinstance(data, dict):
           raise ValueError("JSON root must be an object")
         return data
       except (UnicodeError, ValueError, OSError) as exc:
         raise make_error(f"Invalid JSON response: {exc}", status) from exc
     done_cb: Optional[Callable[[bool], None]] = None
     clean_ok = False
     try:
       resp, done_cb = KEEPALIVE_POOL.open_request(
         url, headers, body_bytes, timeout=timeout, validate_url=_validate_api_url
       )
       raw = resp.read(HttpClient.MAX_RESPONSE_BYTES + 1)
       cenc = resp.headers.get("Content-Encoding") or ""
       clean_ok = len(raw) <= HttpClient.MAX_RESPONSE_BYTES
       return decode_json(raw, resp.status, cenc)
     except urllib.error.HTTPError as exc:
       try:
         err_body = exc.read(16384).decode("utf-8", errors="replace")
       except Exception:
         err_body = ""
       retry_hdr = exc.headers.get("Retry-After") if exc.headers else None
       retry_sec = parse_retry_after(retry_hdr)
       raise make_error(str(exc), exc.code, err_body, retry_sec) from exc
     except DocMindAPIException:
       raise
     except Exception as exc:
       raise make_error(f"{type(exc).__name__}: {exc}") from exc
     finally:
       if done_cb is not None:
         try:
           done_cb(clean_ok)
         except Exception:
           pass
 def _anthropic_prefix_binding(system: str, tools: List[Dict[str, Any]], messages: List[Dict[str, Any]]) -> str:
   """Fingerprint the request prefix without storing its contents or credentials."""
   canonical = json.dumps({"system": system, "tools": tools, "messages": messages},
              ensure_ascii=False, sort_keys=True, separators=(",", ":"))
   return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
 def _anthropic_bound_model(model: str) -> bool:
   name = str(model or "").lower()
   return name.startswith(("claude-sonnet-5-5", "claude-opus-5-5", "claude-haiku-5-5",
               "claude-fable-5-1", "claude-mythos-5-1"))
 def _strip_anthropic_thinking(messages: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], bool]:
   """Drop only signed thinking blocks; leave text, tool calls/results intact."""
   output = []
   removed = False
   for message in messages:
     updated = dict(message)
     content = updated.get("content")
     if updated.get("role") == "assistant" and isinstance(content, list):
       filtered = [block for block in content if not (isinstance(block, dict) and
             block.get("type") in ("thinking", "redacted_thinking"))]
       removed = removed or len(filtered) != len(content)
       updated["content"] = filtered
     if updated.get("content"):
       output.append(updated)
   return output, removed
 class ProviderClient:
   """Unified adapter across Anthropic, OpenAI-compatible, and Google Gemini APIs."""
   def __init__(self, cfg: DocMindConfig, on_text: Optional[Callable[[str], None]] = None,
         on_effort_fallback: Optional[Callable[[], None]] = None) -> None:
     self.cfg = cfg
     self.on_text = on_text
     self.on_effort_fallback = on_effort_fallback
     self.last_verification_response: Optional[ModelResponse] = None
     self.last_tool_test_response: Optional[ModelResponse] = None
     self._prompt_tool_fallback = False
     self._unsupported_effort_keys = set()
     self._unsupported_reasoning_format = set()
     self._token_limit_overrides: Dict[tuple, str] = {}
     self.on_compat_fallback: Optional[Callable[[], None]] = None
     self.on_budget_fallback: Optional[Callable[[int], None]] = None
     self.on_probe_retry: Optional[Callable[[], None]] = None
     self.on_connection_retry: Optional[Callable[[int, float], None]] = None
     self.on_probe_interrupted: Optional[Callable[[], None]] = None
     self.on_thinking_rebase: Optional[Callable[[], None]] = None
     self._warned_thinking_rebase = False
   def _effort_key(self) -> tuple:
     return (self.cfg.provider, self.cfg.model, self.cfg.get_base_url(), self.cfg.reasoning_effort)
   def requested_reasoning_effort(self) -> str:
     return '' if self._effort_key() in self._unsupported_effort_keys else reasoning_effort_for(self.cfg)
   def _endpoint_key(self) -> tuple:
     return (self.cfg.provider, self.cfg.model, self.cfg.get_base_url())
   def _adapt_rejected_openai_parameter(self, exc: DocMindAPIException, payload: Dict[str, Any]) -> bool:
     """Retry one explicitly rejected optional field, before any streamed output.

         Never infer capabilities from 401/403/429, ambiguous errors, or an
         incomplete stream. Each token-cap alternative is tried at most once.
         """
     if exc.status_code not in (400, 422) or getattr(exc, "partial_stream", False):
       return False
     text = (str(exc) + " " + (exc.response_body or "")).lower()
     compact = re.sub(r"[^a-z0-9]+", "", text)
     rejected = any(marker in text for marker in (
       "unknown", "unrecognized", "unsupported", "not supported", "not allowed",
       "not permitted", "unexpected", "extra fields", "use max_completion_tokens instead",
       "use max_tokens instead", "does not support"))
     if not rejected:
       return False
     key = self._endpoint_key()
     changed = False
     if "reasoning_format" in payload and "reasoningformat" in compact and key not in self._unsupported_reasoning_format:
       self._unsupported_reasoning_format.add(key)
       changed = True
     elif key not in self._token_limit_overrides:
       for current, alternate in (("max_completion_tokens", "max_tokens"), ("max_tokens", "max_completion_tokens")):
         if current in payload and current.replace("_", "") in compact and any(w in text for w in ("unsupported", "unrecognized", "unknown", "instead")):
           self._token_limit_overrides[key] = alternate
           changed = True
           break
     if not changed and any(k in payload for k in ("max_tokens", "max_completion_tokens")):
       if any(w in text for w in ("max_tokens", "max_completion_tokens")) and any(w in text for w in ("range", "maximum", "at most", "less than", "exceed", "invalid")):
         if self.cfg.max_output_tokens > 8192:
           self.cfg.max_output_tokens = 8192
           changed = True
         elif self.cfg.max_output_tokens > 4096:
           self.cfg.max_output_tokens = 4096
           changed = True
     if changed and self.on_compat_fallback:
       self.on_compat_fallback()
     return changed
   def _disable_rejected_effort(self, exc: DocMindAPIException) -> bool:
     if (exc.status_code not in (400, 422) or getattr(exc, 'partial_stream', False) or
         not self.requested_reasoning_effort()):
       return False
     kind = reasoning_control_for(self.cfg.provider, self.cfg.model)
     text = (str(exc) + ' ' + (exc.response_body or '')).lower()
     compact = re.sub(r'[^a-z0-9]+', '', text)
     fields = {
       'openai': ('reasoningeffort',), 'groq': ('reasoningeffort',), 'deepseek': ('reasoningeffort',),
       'gemini': ('thinkingconfig', 'thinkinglevel'),
       'anthropic': ('outputconfig', 'thinking'),
     }.get(kind, ())
     rejection = ('unknown', 'unrecognized', 'unsupported', 'not supported', 'not allowed',
           'not permitted', 'invalid argument', 'invalid value', 'extra fields', 'unexpected')
     if not any(field in compact for field in fields) or not any(term in text for term in rejection):
       return False
     self._unsupported_effort_keys.add(self._effort_key())
     if self.on_effort_fallback:
       self.on_effort_fallback()
     return True
   def _is_transient_transport_drop(self, exc: DocMindAPIException) -> bool:
     """True if exc is a socket/SSL/EOF/gateway hiccup safe to retry silently before text was printed."""
     if getattr(exc, "emitted_text", False) or getattr(exc, "partial_stream", False):
       return False
     st = exc.status_code
     if st in (408, 425, 499, 500, 502, 503, 504, 520, 521, 522, 523, 524, 529):
       return True
     if st is not None:
       return False
     msg = (str(exc) + " " + (exc.response_body or "")).lower()
     return any(k in msg for k in (
       "remotedisconnected", "incompleteread", "connectionreset", "connection reset",
       "brokenpipe", "broken pipe", "connectionaborted", "ssleoferror", "ssl",
       "timed out", "timeout", "urlopen error", "stream ended before",
       "incomplete streamed", "unexpected eof", "badstatusline",
     ))
   def _request_json(self, url: str, headers: Dict[str, str], payload: Dict[str, Any],
            timeout: float, provider_name: str, protocol: str,
            allow_stream: bool = True) -> Dict[str, Any]:
     eff_timeout = max(timeout, 180.0) if timeout >= 100.0 else timeout
     def _post_with_micro_retry() -> Dict[str, Any]:
       for micro in range(4):
         try:
           return HttpClient.post_json(url, headers, payload, eff_timeout, provider_name, self.cfg.model)
         except DocMindAPIException as post_exc:
           KEEPALIVE_POOL.drop_origin(url)
           if micro < 3 and self._is_transient_transport_drop(post_exc):
             time.sleep(0.35 * (micro + 1))
             continue
           raise
       return HttpClient.post_json(url, headers, payload, eff_timeout, provider_name, self.cfg.model)
     if not self.on_text or not allow_stream:
       return _post_with_micro_retry()
     stream_url = url
     stream_payload = dict(payload)
     if protocol == "gemini":
       stream_url = url.replace(":generateContent", ":streamGenerateContent") + "?alt=sse"
     else:
       stream_payload["stream"] = True
       if self.cfg.provider in ("openai", "groq"):
         stream_payload["stream_options"] = {"include_usage": True}
     def unsupported_stream(exc: DocMindAPIException) -> bool:
       detail = (exc.response_body or "").lower()
       unsupported = "stream" in detail and any(x in detail for x in
         ("unsupported", "not supported", "unknown", "unrecognized", "extra fields", "not permitted", "not allowed", "not implemented"))
       return (exc.status_code in (400, 404, 405, 422, 501) and unsupported and
           not getattr(exc, "partial_stream", False))
     for micro in range(2):
       try:
         return stream_json(stream_url, headers, stream_payload, eff_timeout, provider_name,
                  self.cfg.model, protocol, self.on_text, _validate_api_url, _redact_known_keys)
       except DocMindAPIException as exc:
         KEEPALIVE_POOL.drop_origin(stream_url)
         if unsupported_stream(exc) and "stream_options" in (exc.response_body or "").lower() and "stream_options" in stream_payload:
           stream_payload.pop("stream_options", None)
           continue
         if unsupported_stream(exc):
           return _post_with_micro_retry()
         if self._is_transient_transport_drop(exc):
           if micro == 0:
             time.sleep(0.35)
             continue
           return _post_with_micro_retry()
         raise
     return _post_with_micro_retry()
   def generate(
     self,
     system_prompt: str,
     messages: List[Dict[str, Any]],
     tools: Optional[List[Dict[str, Any]]] = None,
     timeout: float = 180.0,
   ) -> ModelResponse:
     _dm_digest_gate()
     _dm_signature_gate()
     spec = get_provider_spec(self.cfg.provider)
     api_key = self.cfg.get_api_key()
     if not api_key and not spec.key_optional:
       raise DocMindAPIException(
         message="API key is missing. Run /api or /setup to configure.",
         status_code=401,
         response_body='{"error":{"type":"authentication_error","message":"Missing API key"}}',
         provider_name=spec.name,
         model_name=self.cfg.model,
       )
     try:
       if spec.protocol == "anthropic":
         result = self._call_anthropic(spec.name, api_key, system_prompt, messages, tools or [], timeout)
       elif spec.protocol == "gemini":
         result = self._call_gemini(spec.name, api_key, system_prompt, messages, tools or [], timeout)
       else:
         result = self._call_openai(spec.name, api_key, system_prompt, messages, tools or [], timeout)
       seen_ids = set()
       for call in result.tool_calls:
         if (not isinstance(call.id, str) or not call.id.strip() or call.id in seen_ids or
             not isinstance(call.name, str) or not call.name.strip()):
           exc = DocMindAPIException("Invalid or duplicate tool call identity; no tool was executed.",
                        status_code=200, provider_name=spec.name, model_name=self.cfg.model)
           exc.invalid_tool_arguments = True
           raise exc
         seen_ids.add(call.id)
       return result
     except DocMindAPIException as exc:
       secret_headers = {"Authorization": "Bearer " + api_key} if api_key else {}
       exc.message = _redact_known_keys(exc.message, secret_headers)
       exc.args = (exc.message,)
       exc.response_body = _redact_known_keys(exc.response_body, secret_headers)
       if self._disable_rejected_effort(exc):
         return self.generate(system_prompt, messages, tools, timeout)
       raise
     except Exception as exc:
       secret_headers = {"Authorization": "Bearer " + api_key} if api_key else {}
       detail = _redact_known_keys(str(exc), secret_headers)
       raise DocMindAPIException(
         "Invalid or unexpected provider response: " + detail, status_code=200,
         provider_name=spec.name, model_name=self.cfg.model,
       ) from None
   def _probe_generate(self, system_prompt: str, messages: List[Dict[str, Any]],
             tools: List[Dict[str, Any]], timeout: float) -> ModelResponse:
     """Retry a short setup/diagnostic request only on bounded transient failures."""
     retries = 0
     while True:
       try:
         return self.generate(system_prompt, messages, tools=tools, timeout=timeout)
       except KeyboardInterrupt:
         if self.on_probe_interrupted:
           self.on_probe_interrupted()
         raise
       except DocMindAPIException as exc:
         alert = classify_exception(exc, get_provider_spec(self.cfg.provider).name, self.cfg.model)
         delay = retry_delay(retries + 1, alert.retry_after, max_wait=8.0)
         if (not alert.auto_retryable or getattr(exc, "partial_stream", False) or
             retries >= 2 or delay is None):
           raise
         retries += 1
         if self.on_connection_retry:
           self.on_connection_retry(retries, delay)
         time.sleep(delay)
   def verify_connection(self, timeout: float = 25.0) -> Tuple[bool, Optional[DocMindAPIException]]:
     """Lightweight live API check during Setup Wizard or /doctor."""
     self.last_verification_response = None
     try:
       test_msgs = [{"role": "user", "content": "Reply with OK."}]
       saved_max = self.cfg.max_output_tokens
       saved_effort = self.cfg.reasoning_effort
       saved_callback = self.on_text
       try:
         self.cfg.max_output_tokens = 512
         self.cfg.reasoning_effort = "low"
         self.on_text = None
         try:
           response = self._probe_generate("Reply briefly.", test_msgs, tools=[], timeout=timeout)
         except DocMindAPIException as exc:
           if not getattr(exc, "empty_output_limit", False):
             raise
           if self.on_probe_retry:
             self.on_probe_retry()
           self.cfg.max_output_tokens = 1024
           response = self._probe_generate("Reply briefly.", test_msgs, tools=[], timeout=timeout)
         self.last_verification_response = response
       finally:
         self.cfg.max_output_tokens = saved_max
         self.cfg.reasoning_effort = saved_effort
         self.on_text = saved_callback
       if not response.text.strip():
         raise DocMindAPIException(
           "The model returned no text during the connection test. Check model access or try another model.",
           status_code=200, provider_name=get_provider_spec(self.cfg.provider).name,
           model_name=self.cfg.model,
         )
       return True, None
     except DocMindAPIException as exc:
       return False, exc
     except Exception as exc:
       wrapped = DocMindAPIException(
         message=_redact_known_keys(str(exc), {"Authorization": "Bearer " + self.cfg.get_api_key()}),
         status_code=None,
         provider_name=get_provider_spec(self.cfg.provider).name,
         model_name=self.cfg.model,
       )
       return False, wrapped
   def verify_tool_connection(self, registered_tools: List[Dict[str, Any]], timeout: float = 35.0) -> Tuple[bool, Optional[DocMindAPIException]]:
     """Ask for a harmless diagnostic call; NEVER execute the returned call.

         Include the real agent schemas so this catches provider schema rejection,
         but the response, including any unexpected tool calls, is inspection-only.
         A missing probe call is inconclusive rather than proof of no tool support.
         """
     self.last_tool_test_response = None
     probe = {
       "name": "docmind_probe",
       "description": "Diagnostic only. Request this function with marker ping; the client will not execute it.",
       "parameters": {"type": "object", "properties": {"marker": {"type": "string"}}, "required": ["marker"]},
     }
     saved_max = self.cfg.max_output_tokens
     saved_effort = self.cfg.reasoning_effort
     saved_callback = self.on_text
     try:
       self.cfg.max_output_tokens = min(saved_max, 1024)
       self.cfg.reasoning_effort = "low"
       self.on_text = None
       response = self._probe_generate(
         "For this diagnostic, request the docmind_probe function exactly once with marker ping. "
         "Do not request any other function. The client only inspects the request and executes nothing.",
         [{"role": "user", "content": "Request docmind_probe with marker ping."}],
         tools=[probe] + list(registered_tools), timeout=timeout,
       )
       self.last_tool_test_response = response
       calls = response.tool_calls
       ok = (len(calls) == 1 and calls[0].name == "docmind_probe" and
          calls[0].arguments == {"marker": "ping"})
       return ok, None
     except DocMindAPIException as exc:
       return False, exc
     except Exception as exc:
       headers = {"Authorization": "Bearer " + self.cfg.get_api_key()}
       return False, DocMindAPIException(
         message=_redact_known_keys(str(exc), headers), status_code=None,
         provider_name=get_provider_spec(self.cfg.provider).name, model_name=self.cfg.model,
       )
     finally:
       self.cfg.max_output_tokens = saved_max
       self.cfg.reasoning_effort = saved_effort
       self.on_text = saved_callback
   def _call_anthropic(
     self,
     provider_name: str,
     api_key: str,
     system_prompt: str,
     messages: List[Dict[str, Any]],
     tools: List[Dict[str, Any]],
     timeout: float,
   ) -> ModelResponse:
     url = f"{self.cfg.get_base_url()}/messages"
     headers = {
       "x-api-key": api_key,
       "anthropic-version": "2023-06-01",
       "content-type": "application/json",
     }
     anth_tools = [{"name": item["name"], "description": item["description"],
            "input_schema": item["parameters"]} for item in tools]
     anth_msgs: List[Dict[str, Any]] = []
     rebased = False
     for m in messages:
       role = m["role"]
       if role == "user":
         anth_msgs.append({"role": "user", "content": str(m.get("content", ""))})
       elif role == "assistant":
         meta = m.get("provider_data") or {}
         saved_blocks = meta.get("blocks") if meta.get("provider") == "anthropic" and meta.get("model") == self.cfg.model else None
         blocks: List[Dict[str, Any]] = list(saved_blocks) if isinstance(saved_blocks, list) else []
         if blocks and _anthropic_bound_model(self.cfg.model):
           has_thinking = any(isinstance(block, dict) and block.get("type") in
                    ("thinking", "redacted_thinking") for block in blocks)
           if has_thinking:
             expected = meta.get("binding_prefix")
             actual = _anthropic_prefix_binding(system_prompt, anth_tools, anth_msgs)
             if not isinstance(expected, str) or expected != actual:
               blocks = [block for block in blocks if not (isinstance(block, dict) and
                    block.get("type") in ("thinking", "redacted_thinking"))]
               rebased = True
         if not blocks:
           if m.get("content"):
             blocks.append({"type": "text", "text": str(m["content"])})
           for tc in m.get("tool_calls", []):
             blocks.append({"type": "tool_use", "id": tc["id"], "name": tc["name"], "input": tc["arguments"]})
         if blocks:
           anth_msgs.append({"role": "assistant", "content": blocks})
       elif role == "tool":
         result_block = {
           "type": "tool_result",
           "tool_use_id": m["tool_call_id"],
           "content": str(m.get("content", "")),
           "is_error": bool(m.get("is_error", False)),
         }
         if anth_msgs and anth_msgs[-1]["role"] == "user" and isinstance(anth_msgs[-1]["content"], list):
           anth_msgs[-1]["content"].append(result_block)
         else:
           anth_msgs.append({"role": "user", "content": [result_block]})
     payload: Dict[str, Any] = {
       "model": self.cfg.model,
       "max_tokens": min(self.cfg.max_output_tokens, 8192),
       "system": system_prompt,
       "messages": anth_msgs,
     }
     effort = self.requested_reasoning_effort()
     if effort and reasoning_control_for(self.cfg.provider, self.cfg.model) == "anthropic":
       payload["thinking"] = {"type": "adaptive"}
       payload["output_config"] = {"effort": effort}
     if tools:
       payload["tools"] = anth_tools
       payload["tool_choice"] = {"type": "auto"}
     if rebased and not self._warned_thinking_rebase:
       self._warned_thinking_rebase = True
       if self.on_thinking_rebase:
         self.on_thinking_rebase()
     try:
       data = self._request_json(url, headers, payload, timeout, provider_name, "anthropic")
     except DocMindAPIException as exc:
       detail = (str(exc) + " " + (exc.response_body or "")).lower()
       mismatch = (exc.status_code == 400 and not getattr(exc, "partial_stream", False) and
             "thinking" in detail and "signature" in detail and
             ("bound to a different conversation" in detail or "prefix mismatch" in detail))
       stripped, removed = _strip_anthropic_thinking(payload["messages"]) if mismatch else ([], False)
       if mismatch and removed:
         payload = dict(payload)
         payload["messages"] = stripped
         if self.on_compat_fallback:
           self.on_compat_fallback()
         data = self._request_json(url, headers, payload, timeout, provider_name, "anthropic")
       elif (exc.status_code == 400 and "max_tokens" in (exc.response_body or "") and
           payload["max_tokens"] > 4096 and not getattr(exc, "partial_stream", False)):
         payload["max_tokens"] = 4096
         data = self._request_json(url, headers, payload, timeout, provider_name, "anthropic")
       else:
         raise
     text_parts: List[str] = []
     thought_parts: List[str] = []
     tool_calls: List[ToolCall] = []
     for block in data.get("content", []):
       btype = block.get("type")
       if btype == "text":
         text_parts.append(block.get("text", ""))
       elif btype == "thinking":
         thought_parts.append(block.get("thinking", ""))
       elif btype == "tool_use":
         tool_calls.append(
           ToolCall(
             id=block.get("id") or f"toolu_{uuid.uuid4().hex[:10]}",
             name=block.get("name", ""),
             arguments=_native_tool_arguments(block.get("input", {}), provider_name, self.cfg.model),
           )
         )
     raw_stop = data.get("stop_reason", "end_turn")
     if tool_calls and str(raw_stop).lower() in ("max_tokens", "refusal", "error"):
       raise DocMindAPIException("The response was cut off or refused; no tool was executed (stop: " + str(raw_stop) + ").",
                    status_code=200, provider_name=provider_name, model_name=self.cfg.model)
     if not any(text_parts) and not tool_calls:
       error = DocMindAPIException("Model returned an empty response (stop: " + str(raw_stop) + ").", status_code=200,
                     provider_name=provider_name, model_name=self.cfg.model)
       error.empty_output_limit = str(raw_stop).lower() == "max_tokens"
       raise error
     stop_reason = "tool_use" if tool_calls else ("max_tokens" if raw_stop == "max_tokens" else "stop")
     usage = data.get("usage") or {}
     if not isinstance(usage, dict):
       usage = {}
     return ModelResponse(
       text="".join(text_parts),
       thought="\n".join(thought_parts).strip(),
       tool_calls=tool_calls,
       stop_reason=stop_reason,
       input_tokens=(_usage_int(usage, "input_tokens") + _usage_int(usage, "cache_read_input_tokens")
              + _usage_int(usage, "cache_creation_input_tokens")),
       output_tokens=_usage_int(usage, "output_tokens"),
       usage_complete=_complete_usage(usage, ("input_tokens", "output_tokens")),
       provider_data={"provider": "anthropic", "model": self.cfg.model, "blocks": data.get("content", []),
              "binding_prefix": _anthropic_prefix_binding(system_prompt, anth_tools, payload["messages"])},
     )
   def _call_openai(
     self,
     provider_name: str,
     api_key: str,
     system_prompt: str,
     messages: List[Dict[str, Any]],
     tools: List[Dict[str, Any]],
     timeout: float,
   ) -> ModelResponse:
     url = f"{self.cfg.get_base_url()}/chat/completions"
     headers: Dict[str, str] = {"Content-Type": "application/json"}
     if api_key:
       headers["Authorization"] = f"Bearer {api_key}"
     if self.cfg.provider == "openrouter":
       headers["HTTP-Referer"] = "https://github.com/beyip/docmind-cli"
       headers["X-Title"] = "DocMind Terminal AI Agent"
     use_prompt_tools = self._prompt_tool_fallback and bool(tools)
     effective_system = (
       system_prompt + _build_prompt_tool_instructions(tools) if use_prompt_tools else system_prompt
     )
     oai_msgs: List[Dict[str, Any]] = [{"role": "system", "content": effective_system}]
     for m in messages:
       role = m["role"]
       if role == "user":
         oai_msgs.append({"role": "user", "content": str(m.get("content", ""))})
       elif role == "assistant":
         tcs = m.get("tool_calls", [])
         if tcs and not use_prompt_tools:
           msg_obj: Dict[str, Any] = {
             "role": "assistant",
             "content": m.get("content") or "",
             "tool_calls": [
               {
                 "id": tc["id"],
                 "type": "function",
                 "function": {
                   "name": tc["name"],
                   "arguments": json.dumps(tc["arguments"], ensure_ascii=False),
                 },
               }
               for tc in tcs
             ],
           }
           saved = m.get("provider_data") or {}
           if self.cfg.provider == "deepseek":
             msg_obj["reasoning_content"] = (m.get("thought") or "") if saved.get("provider") == "deepseek" else ""
           elif m.get("thought") and "reasoner" in self.cfg.model.lower():
             msg_obj["reasoning_content"] = m["thought"]
           if self.cfg.provider == "openrouter" and saved.get("provider") == "openrouter" and saved.get("model") == self.cfg.model:
             if isinstance(saved.get("reasoning_details"), list):
               msg_obj["reasoning_details"] = saved["reasoning_details"]
             elif saved.get("reasoning"):
               msg_obj["reasoning"] = saved["reasoning"]
             if isinstance(saved.get("raw_tool_calls"), list):
               msg_obj["tool_calls"] = saved["raw_tool_calls"]
           oai_msgs.append(msg_obj)
         else:
           content_str = str(m.get("content", ""))
           if tcs and use_prompt_tools:
             for tc in tcs:
               content_str += (
                 f'\n<docmind_tool>{json.dumps({"name": tc["name"], "arguments": tc["arguments"]})}</docmind_tool>'
               )
           plain_msg: Dict[str, Any] = {"role": "assistant", "content": content_str}
           saved = m.get("provider_data") or {}
           if self.cfg.provider == "deepseek":
             plain_msg["reasoning_content"] = (m.get("thought") or "") if saved.get("provider") == "deepseek" else ""
           if self.cfg.provider == "openrouter" and saved.get("provider") == "openrouter" and saved.get("model") == self.cfg.model:
             if isinstance(saved.get("reasoning_details"), list):
               plain_msg["reasoning_details"] = saved["reasoning_details"]
             elif saved.get("reasoning"):
               plain_msg["reasoning"] = saved["reasoning"]
           oai_msgs.append(plain_msg)
       elif role == "tool":
         if use_prompt_tools:
           oai_msgs.append(
             {
               "role": "user",
               "content": f"[Tool Result ({m.get('name', 'tool')})]:\n{m.get('content', '')}",
             }
           )
         else:
           oai_msgs.append(
             {
               "role": "tool",
               "tool_call_id": m["tool_call_id"],
               "content": str(m.get("content", "")),
             }
           )
     model_lower = self.cfg.model.lower()
     is_openai_reasoning = self.cfg.provider == "openai" and (
       bool(re.match(r"^o[0-9]+(?:-|$)", model_lower)) or model_lower.startswith("gpt-5")
     )
     is_groq_qwen = self.cfg.provider == "groq" and model_lower == "qwen/qwen3.8-27b"
     payload: Dict[str, Any] = {"model": self.cfg.model, "messages": oai_msgs}
     output_limit = min(self.cfg.max_output_tokens, 4096) if self.cfg.provider == "groq" else self.cfg.max_output_tokens
     cap_field = "max_completion_tokens" if (is_openai_reasoning or self.cfg.provider == "groq") else "max_tokens"
     cap_field = self._token_limit_overrides.get(self._endpoint_key(), cap_field)
     payload[cap_field] = output_limit
     if is_groq_qwen and self._endpoint_key() not in self._unsupported_reasoning_format:
       payload["reasoning_format"] = "parsed"
     effort = self.requested_reasoning_effort()
     if effort and reasoning_control_for(self.cfg.provider, self.cfg.model) in ("openai", "groq", "deepseek"):
       payload["reasoning_effort"] = effort
     if tools and not use_prompt_tools:
       payload["tools"] = [
         {
           "type": "function",
           "function": {
             "name": t_def["name"],
             "description": t_def["description"],
             "parameters": t_def["parameters"],
           },
         }
         for t_def in tools
       ]
       payload["tool_choice"] = "auto"
     try:
       data = self._request_json(url, headers, payload, timeout, provider_name, "openai", allow_stream=not use_prompt_tools)
     except DocMindAPIException as exc:
       ceiling = request_token_ceiling(str(exc) + " " + (exc.response_body or ""), exc.status_code)
       adjusted_limit = None
       if self.cfg.provider == "groq" and ceiling and not getattr(exc, "partial_stream", False):
         limit, requested = ceiling
         margin = min(256, max(32, int(limit * 0.02)))
         candidate = output_limit - (requested - limit) - margin
         if 512 <= candidate < output_limit:
           adjusted_limit = candidate
       if adjusted_limit is not None:
         retry_payload = dict(payload)
         retry_payload[cap_field] = adjusted_limit
         if self.on_budget_fallback:
           self.on_budget_fallback(adjusted_limit)
         data = self._request_json(url, headers, retry_payload, timeout, provider_name, "openai", allow_stream=not use_prompt_tools)
       elif self._adapt_rejected_openai_parameter(exc, payload):
         return self._call_openai(provider_name, api_key, system_prompt, messages, tools, timeout)
       else:
         body_low = (exc.response_body or "").lower()
         if (
           tools
           and not use_prompt_tools
           and not getattr(exc, "partial_stream", False)
           and exc.status_code in (400, 404, 422)
           and any(w in body_low for w in ("tool", "function call", "function calling"))
           and any(w in body_low for w in ("does not support", "not supported", "unsupported", "not available for this model"))
         ):
           self._prompt_tool_fallback = True
           if self.on_compat_fallback:
             self.on_compat_fallback()
           return self._call_openai(provider_name, api_key, system_prompt, messages, tools, timeout)
         raise
     choices = data.get("choices") or []
     if not choices:
       raise DocMindAPIException("The model returned no answer or tool call.", status_code=200,
                    provider_name=provider_name, model_name=self.cfg.model)
     choice = choices[0]
     msg = choice.get("message") or {}
     content_text = str(msg.get("content") or "")
     thought_text = str(msg.get("reasoning_content") or msg.get("reasoning") or "")
     tool_calls: List[ToolCall] = []
     for raw_tc in msg.get("tool_calls") or []:
       fn = raw_tc.get("function") or {}
       tool_calls.append(
         ToolCall(
           id=raw_tc.get("id") or f"call_{uuid.uuid4().hex[:10]}",
           name=fn.get("name", ""),
           arguments=_native_tool_arguments(fn.get("arguments"), provider_name, self.cfg.model),
         )
       )
     if not tool_calls and "<docmind_tool>" in content_text:
       content_text, tool_calls = _extract_prompt_tool_calls(content_text, provider_name, self.cfg.model)
     finish = choice.get("finish_reason") or "stop"
     if str(finish).lower() == "error" and not tool_calls:
       error = DocMindAPIException("Provider ended the response with an error; partial text is not a completed answer.",
                     status_code=200, provider_name=provider_name, model_name=self.cfg.model)
       error.partial_stream = bool(self.on_text and content_text)
       raise error
     if tool_calls and str(finish).lower() in ("length", "max_tokens", "content_filter", "error"):
       raise DocMindAPIException("The response was cut off or filtered; no tool was executed (finish: " + str(finish) + ").",
                    status_code=200, provider_name=provider_name, model_name=self.cfg.model)
     if not content_text.strip() and not tool_calls:
       error = DocMindAPIException("Model returned an empty response (finish: " + str(finish) + ").", status_code=200,
                     provider_name=provider_name, model_name=self.cfg.model)
       error.empty_output_limit = str(finish).lower() in ("length", "max_tokens")
       raise error
     stop_reason = "tool_use" if tool_calls else ("max_tokens" if finish == "length" else "stop")
     usage = data.get("usage") or (data.get("x_groq") or {}).get("usage") or {}
     if not isinstance(usage, dict):
       usage = {}
     return ModelResponse(
       text=content_text,
       thought=thought_text,
       tool_calls=tool_calls,
       stop_reason=stop_reason,
       input_tokens=_usage_int(usage, "prompt_tokens"),
       output_tokens=_usage_int(usage, "completion_tokens"),
       usage_complete=_complete_usage(usage, ("prompt_tokens", "completion_tokens")),
       reported_cost_usd=(float(usage['cost']) if self.cfg.provider == 'openrouter'
                and isinstance(usage.get('cost'), (int, float))
                and not isinstance(usage.get('cost'), bool)
                and 0 <= usage['cost'] < 1e12 else None),
       provider_data=({
         "provider": "openrouter", "model": self.cfg.model,
         "reasoning_details": msg.get("reasoning_details"),
         "reasoning": msg.get("reasoning"),
         "raw_tool_calls": msg.get("tool_calls"),
       } if self.cfg.provider == "openrouter" else
        {"provider": "deepseek", "model": self.cfg.model} if self.cfg.provider == "deepseek" else {}),
     )
   def _call_gemini(
     self,
     provider_name: str,
     api_key: str,
     system_prompt: str,
     messages: List[Dict[str, Any]],
     tools: List[Dict[str, Any]],
     timeout: float,
   ) -> ModelResponse:
     model_id = self.cfg.model
     if model_id.startswith("models/"):
       model_id = model_id[len("models/") :]
     model_id = urllib.parse.quote(model_id, safe="-_.")
     url = f"{self.cfg.get_base_url()}/models/{model_id}:generateContent"
     headers = {
       "x-goog-api-key": api_key,
       "Content-Type": "application/json",
     }
     contents: List[Dict[str, Any]] = []
     gemini_call_ids: Dict[str, str] = {}
     for m in messages:
       role = m["role"]
       if role == "user":
         contents.append({"role": "user", "parts": [{"text": str(m.get("content", ""))}]})
       elif role == "assistant":
         provider_data = m.get("provider_data") or {}
         saved_parts = provider_data.get("parts") if provider_data.get("provider") == "gemini" and provider_data.get("model") == self.cfg.model else None
         parts: List[Dict[str, Any]] = list(saved_parts) if isinstance(saved_parts, list) else []
         for tc in m.get("tool_calls", []):
           meta = tc.get("metadata") or {}
           if meta.get("gemini_id"):
             gemini_call_ids[tc["id"]] = meta["gemini_id"]
         if not parts:
           if m.get("content"):
             parts.append({"text": str(m["content"])})
           for tc in m.get("tool_calls", []):
             fc_part: Dict[str, Any] = {"functionCall": {"name": tc["name"], "args": tc["arguments"]}}
             meta = tc.get("metadata") or {}
             if meta.get("thoughtSignature"):
               fc_part["thoughtSignature"] = meta["thoughtSignature"]
             if meta.get("gemini_id"):
               fc_part["functionCall"]["id"] = meta["gemini_id"]
             parts.append(fc_part)
         if parts:
           contents.append({"role": "model", "parts": parts})
       elif role == "tool":
         fr_part = {
           "functionResponse": {
             "name": m.get("name", "tool"),
             "response": {"result": str(m.get("content", ""))},
           }
         }
         call_id = gemini_call_ids.get(m.get("tool_call_id", ""))
         if call_id:
           fr_part["functionResponse"]["id"] = call_id
         if (
           contents
           and contents[-1]["role"] == "user"
           and contents[-1]["parts"]
           and "functionResponse" in contents[-1]["parts"][0]
         ):
           contents[-1]["parts"].append(fr_part)
         else:
           contents.append({"role": "user", "parts": [fr_part]})
     payload: Dict[str, Any] = {
       "systemInstruction": {"parts": [{"text": system_prompt}]},
       "contents": contents,
       "generationConfig": {
         "maxOutputTokens": self.cfg.max_output_tokens,
       },
     }
     effort = self.requested_reasoning_effort()
     if effort and reasoning_control_for(self.cfg.provider, self.cfg.model) == "gemini":
       payload["generationConfig"]["thinkingConfig"] = {"thinkingLevel": effort}
     if tools:
       declarations = []
       for t_def in tools:
         schema = _clean_gemini_schema(t_def["parameters"])
         declaration = {"name": t_def["name"], "description": t_def["description"]}
         if not (schema.get("type", "").lower() == "object" and
             schema.get("properties") == {} and not schema.get("required")):
           declaration["parameters"] = schema
         declarations.append(declaration)
       payload["tools"] = [{"functionDeclarations": declarations}]
       payload["toolConfig"] = {"functionCallingConfig": {"mode": "AUTO"}}
     try:
       data = self._request_json(url, headers, payload, timeout, provider_name, "gemini")
     except DocMindAPIException as exc:
       if self._disable_rejected_effort(exc):
         payload["generationConfig"].pop("thinkingConfig", None)
         data = self._request_json(url, headers, payload, timeout, provider_name, "gemini")
       else:
         raise
     candidates = data.get("candidates") or []
     if not candidates:
       block_reason = (data.get("promptFeedback") or {}).get("blockReason", "")
       if block_reason:
         raise DocMindAPIException(
           f"Gemini did not generate a response (blocked: {block_reason}).",
           status_code=200, provider_name=provider_name, model_name=self.cfg.model,
         )
       raise DocMindAPIException("Gemini returned no answer or tool call.", status_code=200,
                    provider_name=provider_name, model_name=self.cfg.model)
     cand = candidates[0]
     parts_out = (cand.get("content") or {}).get("parts") or []
     text_parts: List[str] = []
     thought_parts: List[str] = []
     tool_calls: List[ToolCall] = []
     for part in parts_out:
       if part.get("thought") is True and "text" in part:
         thought_parts.append(str(part["text"]))
       elif "text" in part:
         text_parts.append(str(part["text"]))
       elif "functionCall" in part:
         fc = part["functionCall"]
         meta: Dict[str, Any] = {}
         if "thoughtSignature" in part:
           meta["thoughtSignature"] = part["thoughtSignature"]
         if fc.get("id"):
           meta["gemini_id"] = str(fc["id"])
         tool_calls.append(
           ToolCall(
             id=str(fc.get("id") or f"gem_{uuid.uuid4().hex[:10]}"),
             name=fc.get("name", ""),
             arguments=_native_tool_arguments(fc.get("args", {}), provider_name, self.cfg.model),
             metadata=meta,
           )
         )
     finish = cand.get("finishReason", "STOP")
     if tool_calls and str(finish).upper() not in ("STOP", "TOOL_USE"): 
       raise DocMindAPIException("The response was cut off or filtered; no tool was executed (finish: " + str(finish) + ").",
                    status_code=200, provider_name=provider_name, model_name=self.cfg.model)
     if not any(text_parts) and not tool_calls:
       error = DocMindAPIException("Gemini returned an empty response (finish: " + str(finish) + ").", status_code=200,
                     provider_name=provider_name, model_name=self.cfg.model)
       if str(finish).upper() == "MALFORMED_FUNCTION_CALL":
         error.invalid_tool_arguments = True
       error.empty_output_limit = str(finish).upper() == "MAX_TOKENS"
       raise error
     stop_reason = "tool_use" if tool_calls else ("max_tokens" if finish == "MAX_TOKENS" else "stop")
     usage = data.get("usageMetadata") or {}
     if not isinstance(usage, dict):
       usage = {}
     return ModelResponse(
       text="".join(text_parts),
       thought="".join(thought_parts).strip(),
       tool_calls=tool_calls,
       stop_reason=stop_reason,
       input_tokens=_usage_int(usage, "promptTokenCount"),
       output_tokens=_usage_int(usage, "candidatesTokenCount") + _usage_int(usage, "thoughtsTokenCount"),
       usage_complete=_complete_usage(usage, ("promptTokenCount", "candidatesTokenCount")),
       provider_data={"provider": "gemini", "model": self.cfg.model, "parts": parts_out},
     )
 return locals()
_dm_install('docmind.core.providers', _dm_module_16, False)

# ===== docmind/ui/activity.py (included source) =====
def _dm_module_17():
 """Clear, localised progress labels for real tool operations."""
 import os
 import re
 import shutil
 import urllib.parse
 from typing import Any, Dict
 from docmind.core.errors import mask_secrets
 from docmind.i18n import i18n
 _LABELS = {
   "tr": {
     "project_overview": ("Proje inceleme isteği", "Proje incelendi"),
     "check_syntax": ("Sözdizimi kontrolü isteği", "Sözdizimi kontrolü tamamlandı"),
     "read_file": ("Dosya okuma isteği", "Dosya okundu"),
     "write_file": ("Dosya yazma isteği", "Dosya yazıldı"),
     "edit_file": ("Dosya düzenleme isteği", "Dosya düzenlendi"),
     "multi_edit": ("Dosya düzenleme isteği", "Dosya düzenlendi"),
     "delete_path": ("Silme isteği", "Silindi"),
     "move_or_copy": ("Taşıma / kopyalama isteği", "Taşıma / kopyalama tamamlandı"),
     "list_directory": ("Klasörü inceleme isteği", "Klasör incelendi"),
     "change_directory": ("Klasör değiştirme isteği", "Aktif klasör değiştirildi"),
     "list_system_drives": ("Sistem sürücüleri isteği", "Sürücüler ve özel klasörler listelendi"),
     "archive_tool": ("Arşiv işlemi isteği", "Arşiv işlemi tamamlandı"),
     "undo_file_change": ("Değişikliği geri alma isteği", "Dosya önceki haline döndürüldü"),
     "ask_user": ("Kullanıcı tercihi soruluyor", "Kullanıcı tercihi alındı"),
     "search_files": ("Dosya arama isteği", "Dosya araması tamamlandı"),
     "grep_search": ("İçerik arama isteği", "İçerik araması tamamlandı"),
     "run_command": ("Terminal komutu isteği", "TERMİNAL KULLANILDI"),
     "python_eval": ("Python kodu çalıştırma isteği", "TERMİNAL KULLANILDI (Python)"),
     "open_path": ("Dosya / uygulama açma isteği", "Sistemde açıldı"),
     "find_processes": ("Çalışan işlemler isteği", "Çalışan işlemler incelendi"),
     "system_info": ("Sistem bilgisi isteği", "Sistem bilgisi alındı"),
     "web_fetch": ("Web sayfası isteği", "Web sayfası okundu"),
     "unknown": ("İşlem isteği", "İşlem tamamlandı"),
     "failed": "İşlem başarısız",
     "skipped": "Kullanıcı izin vermedi (iptal edildi)",
     "bash": "TERMİNAL KULLANILDI (Bash)",
   },
   "en": {
     "project_overview": ("Project inspection requested", "Project inspected"),
     "check_syntax": ("Syntax check requested", "Syntax check completed"),
     "read_file": ("File read requested", "File read"),
     "write_file": ("File write requested", "File written"),
     "edit_file": ("File edit requested", "File edited"),
     "multi_edit": ("File edit requested", "File edited"),
     "delete_path": ("Deletion requested", "Deleted"),
     "move_or_copy": ("Move / copy requested", "Move / copy completed"),
     "list_directory": ("Folder inspection requested", "Folder inspected"),
     "change_directory": ("Directory change requested", "Working directory changed"),
     "list_system_drives": ("Drives inspection requested", "Drives & folders listed"),
     "archive_tool": ("Archive action requested", "Archive action completed"),
     "undo_file_change": ("Rollback requested", "File rolled back to previous state"),
     "ask_user": ("Asking user preference", "User preference received"),
     "search_files": ("File search requested", "File search completed"),
     "grep_search": ("Content search requested", "Content search completed"),
     "run_command": ("Terminal command requested", "TERMINAL USED"),
     "python_eval": ("Python execution requested", "TERMINAL USED (Python)"),
     "open_path": ("Desktop open requested", "Opened on system"),
     "find_processes": ("Process scan requested", "Running processes inspected"),
     "system_info": ("System information requested", "System information collected"),
     "web_fetch": ("Web request", "Web page read"),
     "unknown": ("Action requested", "Action completed"),
     "failed": "Action failed",
     "skipped": "Action declined by user",
     "bash": "TERMINAL USED (Bash)",
   },
   "de": {
     "project_overview": ("Projektprüfung angefordert", "Projekt geprüft"),
     "check_syntax": ("Syntaxprüfung angefordert", "Syntaxprüfung abgeschlossen"),
     "read_file": ("Datei lesen angefordert", "Datei gelesen"),
     "write_file": ("Datei schreiben angefordert", "Datei geschrieben"),
     "edit_file": ("Datei ändern angefordert", "Datei geändert"),
     "multi_edit": ("Datei ändern angefordert", "Datei geändert"),
     "delete_path": ("Löschen angefordert", "Gelöscht"),
     "move_or_copy": ("Verschieben / Kopieren angefordert", "Verschieben / Kopieren abgeschlossen"),
     "list_directory": ("Ordnerprüfung angefordert", "Ordner geprüft"),
     "change_directory": ("Ordnerwechsel angefordert", "Ordner gewechselt"),
     "list_system_drives": ("Laufwerke angefordert", "Laufwerke aufgelistet"),
     "archive_tool": ("Archivaktion angefordert", "Archivaktion abgeschlossen"),
     "undo_file_change": ("Rückgängig angefordert", "Datei wiederhergestellt"),
     "ask_user": ("Benutzerfrage", "Antwort erhalten"),
     "search_files": ("Dateisuche angefordert", "Dateisuche abgeschlossen"),
     "grep_search": ("Inhaltssuche angefordert", "Inhaltssuche abgeschlossen"),
     "run_command": ("Befehl angefordert", "TERMINAL VERWENDET"),
     "python_eval": ("Python-Ausführung angefordert", "TERMINAL VERWENDET (Python)"),
     "open_path": ("Öffnen angefordert", "Geöffnet"),
     "find_processes": ("Prozesssuche angefordert", "Prozesse geprüft"),
     "system_info": ("Systeminformationen angefordert", "Systeminformationen gelesen"),
     "web_fetch": ("Webanfrage", "Webseite gelesen"),
     "unknown": ("Aktion angefordert", "Aktion abgeschlossen"),
     "failed": "Aktion fehlgeschlagen",
     "skipped": "Aktion abgelehnt",
     "bash": "TERMINAL VERWENDET (Bash)",
   },
   "es": {
     "project_overview": ("Inspección del proyecto solicitada", "Proyecto inspeccionado"),
     "check_syntax": ("Comprobación de sintaxis solicitada", "Comprobación de sintaxis completada"),
     "read_file": ("Lectura de archivo solicitada", "Archivo leído"),
     "write_file": ("Escritura de archivo solicitada", "Archivo escrito"),
     "edit_file": ("Edición de archivo solicitada", "Archivo editado"),
     "multi_edit": ("Edición de archivo solicitada", "Archivo editado"),
     "delete_path": ("Eliminación solicitada", "Eliminado"),
     "move_or_copy": ("Movimiento / copia solicitada", "Movimiento / copia completada"),
     "list_directory": ("Inspección de carpeta solicitada", "Carpeta inspeccionada"),
     "change_directory": ("Cambio de carpeta solicitado", "Carpeta cambiada"),
     "list_system_drives": ("Unidades del sistema solicitadas", "Unidades listadas"),
     "archive_tool": ("Acción de archivo comprimido solicitada", "Archivo comprimido procesado"),
     "undo_file_change": ("Reversión solicitada", "Archivo restaurado"),
     "ask_user": ("Consultando al usuario", "Respuesta recibida"),
     "search_files": ("Búsqueda solicitada", "Búsqueda de archivos completada"),
     "grep_search": ("Búsqueda de contenido solicitada", "Búsqueda de contenido completada"),
     "run_command": ("Comando solicitado", "TERMINAL UTILIZADA"),
     "python_eval": ("Ejecución de Python solicitada", "TERMINAL UTILIZADA (Python)"),
     "open_path": ("Apertura solicitada", "Abierto en el sistema"),
     "find_processes": ("Procesos solicitados", "Procesos inspeccionados"),
     "system_info": ("Información del sistema solicitada", "Información del sistema obtenida"),
     "web_fetch": ("Solicitud web", "Página web leída"),
     "unknown": ("Acción solicitada", "Acción completada"),
     "failed": "Acción fallida",
     "skipped": "Acción rechazada",
     "bash": "TERMINAL UTILIZADA (Bash)",
   },
   "fr": {
     "project_overview": ("Inspection du projet demandée", "Projet inspecté"),
     "check_syntax": ("Vérification syntaxique demandée", "Vérification syntaxique terminée"),
     "read_file": ("Lecture du fichier demandée", "Fichier lu"),
     "write_file": ("Écriture du fichier demandée", "Fichier écrit"),
     "edit_file": ("Modification du fichier demandée", "Fichier modifié"),
     "multi_edit": ("Modification du fichier demandée", "Fichier modifié"),
     "delete_path": ("Suppression demandée", "Supprimé"),
     "move_or_copy": ("Déplacement / copie demandé", "Déplacement / copie terminé"),
     "list_directory": ("Inspection du dossier demandée", "Dossier inspecté"),
     "change_directory": ("Changement de dossier demandé", "Dossier modifié"),
     "list_system_drives": ("Disques demandés", "Disques listés"),
     "archive_tool": ("Archive demandée", "Archive traitée"),
     "undo_file_change": ("Annulation demandée", "Fichier restauré"),
     "ask_user": ("Question à l'utilisateur", "Réponse reçue"),
     "search_files": ("Recherche de fichiers demandée", "Recherche de fichiers terminée"),
     "grep_search": ("Recherche de contenu demandée", "Recherche de contenu terminée"),
     "run_command": ("Commande demandée", "TERMINAL UTILISÉ"),
     "python_eval": ("Exécution Python demandée", "TERMINAL UTILISÉ (Python)"),
     "open_path": ("Ouverture demandée", "Ouvert sur le système"),
     "find_processes": ("Processus demandés", "Processus inspectés"),
     "system_info": ("Informations système demandées", "Informations système obtenues"),
     "web_fetch": ("Requête web", "Page web lue"),
     "unknown": ("Action demandée", "Action terminée"),
     "failed": "Échec de l’action",
     "skipped": "Action refusée",
     "bash": "TERMINAL UTILISÉ (Bash)",
   },
   "ru": {
     "project_overview": ("Запрос проверки проекта", "Проект проверен"),
     "check_syntax": ("Запрос проверки синтаксиса", "Проверка синтаксиса завершена"),
     "read_file": ("Запрос чтения файла", "Файл прочитан"),
     "write_file": ("Запрос записи файла", "Файл записан"),
     "edit_file": ("Запрос изменения файла", "Файл изменён"),
     "multi_edit": ("Запрос изменения файла", "Файл изменён"),
     "delete_path": ("Запрос удаления", "Удалено"),
     "move_or_copy": ("Запрос перемещения / копирования", "Перемещение / копирование завершено"),
     "list_directory": ("Запрос просмотра папки", "Папка просмотрена"),
     "change_directory": ("Запрос смены папки", "Рабочая папка изменена"),
     "list_system_drives": ("Запрос дисков системы", "Диски перечислены"),
     "archive_tool": ("Запрос архивации", "Операция с архивом завершена"),
     "undo_file_change": ("Запрос отката файла", "Файл восстановлен"),
     "ask_user": ("Вопрос пользователю", "Ответ получен"),
     "search_files": ("Запрос поиска файлов", "Поиск файлов завершён"),
     "grep_search": ("Запрос поиска содержимого", "Поиск содержимого завершён"),
     "run_command": ("Запрос команды терминала", "ИСПОЛЬЗОВАН ТЕРМИНАЛ"),
     "python_eval": ("Запрос запуска Python", "ИСПОЛЬЗОВАН ТЕРМИНАЛ (Python)"),
     "open_path": ("Запрос открытия", "Открыто в системе"),
     "find_processes": ("Запрос процессов", "Процессы проверены"),
     "system_info": ("Запрос сведений о системе", "Сведения о системе получены"),
     "web_fetch": ("Веб-запрос", "Веб-страница прочитана"),
     "unknown": ("Запрос действия", "Действие завершено"),
     "failed": "Ошибка действия",
     "skipped": "Действие отклонено",
     "bash": "ИСПОЛЬЗОВАН ТЕРМИНАЛ (Bash)",
   },
 }
 def _safe(value: Any) -> str:
   text = str(value or "").replace("\n", " ").replace("\r", " ")
   text = re.sub(r"[\x00-\x1f\x7f-\x9f]", lambda m: "\\x%02x" % ord(m.group(0)), text)
   text = mask_secrets(text)
   return text[:117] + "…" if len(text) > 120 else text
 def describe_activity(name: str, args: Dict[str, Any], stage: str = "pending") -> str:
   words = _LABELS.get(i18n.lang, _LABELS["en"])
   if stage == "failed":
     label = words["failed"]
   elif stage == "skipped":
     label = words["skipped"]
   else:
     labels = words.get(name, words["unknown"])
     label = labels[1 if stage == "done" else 0]
     if name == "run_command" and stage == "done" and os.name != "nt" and shutil.which("bash"):
       label = words["bash"]
   subject = ""
   if name in {
     "read_file", "write_file", "edit_file", "multi_edit", "delete_path",
     "list_directory", "change_directory", "search_files", "grep_search",
     "project_overview", "check_syntax", "undo_file_change",
   }:
     subject = str(args.get("path") or ".")
   elif name == "open_path":
     subject = str(args.get("target") or args.get("path") or "")
   elif name == "archive_tool":
     subject = str(args.get("archive_path") or "")
   elif name == "find_processes":
     subject = str(args.get("query") or "all")
   elif name == "move_or_copy":
     subject = str(args.get("source") or "") + " → " + str(args.get("destination") or "")
   elif name == "run_command":
     subject = str(args.get("command") or "")
   elif name == "python_eval":
     subject = str(args.get("code") or "")[:80]
   elif name == "web_fetch":
     try:
       u = urllib.parse.urlsplit(str(args.get("url") or ""))
       subject = urllib.parse.urlunsplit((u.scheme, u.netloc, u.path, "…" if u.query else "", ""))
     except ValueError:
       subject = ""
   return label + (" · " + _safe(subject) if subject else "")
 return locals()
_dm_install('docmind.ui.activity', _dm_module_17, False)

# ===== docmind/ui/terminal_view.py (included source) =====
def _dm_module_18():
 """Dependency-free terminal animations, Windows/Linux ANSI color support, and pinned footer.
 No graphical window, no Python package installation, and no shell interpolation.
 """
 import collections
 import ctypes
 import os
 import re
 import shutil
 import sys
 import threading
 import time
 import unicodedata
 from contextlib import contextmanager
 from typing import Callable, Deque, Optional, Tuple
 def enable_windows_ansi() -> bool:
   """Enable Virtual Terminal ANSI escape sequences on Windows 10/11 CMD & PowerShell."""
   if os.name != "nt":
     return True
   try:
     kernel32 = ctypes.windll.kernel32
     ok_any = False
     for std_id in (-11, -12):
       handle = kernel32.GetStdHandle(std_id)
       if handle and handle != -1:
         mode = ctypes.c_ulong()
         if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
           if kernel32.SetConsoleMode(handle, mode.value | 0x0004):
             ok_any = True
     return ok_any or bool(os.environ.get("WT_SESSION") or os.environ.get("ANSICON") or os.environ.get("TERM_PROGRAM"))
   except Exception:
     return bool(os.environ.get("WT_SESSION") or os.environ.get("TERM_PROGRAM"))
 def _terminal_width(text: str, limit: int) -> str:
   used = 0
   out = []
   for ch in text:
     width = 0 if unicodedata.combining(ch) else (2 if unicodedata.east_asian_width(ch) in "WF" else 1)
     if used + width > limit:
       break
     out.append(ch)
     used += width
   return "".join(out)
 class TerminalView:
   def __init__(self, is_tty: bool) -> None:
     self.is_tty = is_tty
     win_vt = enable_windows_ansi() if (is_tty and os.name == "nt") else False
     if os.name == "nt":
       self.ansi = bool(is_tty and win_vt and os.environ.get("WT_SESSION"))
       self.color = bool(is_tty and win_vt and not os.environ.get("NO_COLOR"))
     else:
       posix_term_ok = os.environ.get("TERM", "xterm") != "dumb"
       self.ansi = bool(is_tty and posix_term_ok)
       self.color = bool(self.ansi and not os.environ.get("NO_COLOR"))
     self.lock = threading.RLock()
     self._footer: Optional[Callable[[], str]] = None
     self._compact_footer: Optional[Callable[[int], str]] = None
     self._footer_active = False
     self._rows = 0
     self._last_footer = 0.0
     self._spin_event: Optional[threading.Event] = None
     self._spin_thread: Optional[threading.Thread] = None
     self._typing_cond = threading.Condition()
     self._typing_queue: Deque[Tuple[str, Optional[str]]] = collections.deque()
     self._typing_chars = 0
     self._typing_thread: Optional[threading.Thread] = None
     self._typing_done = False
     self._typing_fast = False
     self._typing_abort = False
     self._typing_emitted = 0
   def _write(self, text: str) -> None:
     with self.lock:
       sys.stdout.write(text)
       sys.stdout.flush()
   def _size(self) -> Tuple[int, int]:
     size = shutil.get_terminal_size(fallback=(80, 24))
     return max(1, size.lines), max(1, size.columns)
   def start_footer(self, status: Callable[[], str], compact: Optional[Callable[[int], str]] = None) -> bool:
     self._footer = status
     self._compact_footer = compact
     rows, cols = self._size()
     if not self.ansi or rows < 8 or cols < 30:
       return False
     with self.lock:
       self._rows = rows
       self._footer_active = True
       sys.stdout.write(f"\x1b[1;{rows-1}r\x1b[{rows-1};1H")
       self._draw_footer_locked(force=True)
       sys.stdout.flush()
     return True
   def _draw_footer_locked(self, force: bool = False) -> None:
     if self._footer is None or not self.ansi:
       return
     rows, cols = self._size()
     if rows < 8 or cols < 30:
       if self._footer_active:
         sys.stdout.write("\x1b7\x1b[r\x1b8")
         self._footer_active = False
       return
     if not self._footer_active:
       self._rows = rows
       self._footer_active = True
       force = True
       sys.stdout.write(f"\x1b7\x1b[1;{rows-1}r\x1b8")
     now = time.monotonic()
     if not force and now - self._last_footer < 0.20:
       return
     if rows != self._rows:
       self._rows = rows
       sys.stdout.write(f"\x1b7\x1b[1;{rows-1}r\x1b8")
     try:
       line = str(self._footer())
       if self._compact_footer and len(line) > cols - 1:
         line = str(self._compact_footer(cols - 1))
     except Exception:
       line = "DocMind"
     line = re.sub(r"[\x00-\x1f\x7f-\x9f]", " ", line)
     line = _terminal_width(line, max(1, cols - 1))
     sys.stdout.write(f"\x1b7\x1b[{rows};1H\x1b[2K\x1b[2m{line}\x1b[0m\x1b8")
     self._last_footer = now
   def update_footer(self, force: bool = False) -> None:
     with self.lock:
       self._draw_footer_locked(force)
       if self.ansi:
         sys.stdout.flush()
   def stop_footer(self) -> None:
     with self.lock:
       if self._footer_active:
         rows, _ = self._size()
         sys.stdout.write(f"\x1b7\x1b[{rows};1H\x1b[2K\x1b[r\x1b8\n")
         sys.stdout.flush()
         self._footer_active = False
   @property
   def footer_active(self) -> bool:
     return self._footer_active
   def start_spinner(self, message: str) -> None:
     self.stop_spinner()
     if not self.is_tty:
       return
     if not self.ansi:
       self._write("… " + message + "\n")
       return
     event = threading.Event()
     self._spin_event = event
     def animate() -> None:
       frames = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
       idx = 0
       while not event.is_set():
         with self.lock:
           _, cols = self._size()
           label = _terminal_width(frames[idx % len(frames)] + " " + message.replace("\n", " "), max(1, cols - 1))
           if self.color:
             label = "\x1b[36m" + label + "\x1b[0m"
           sys.stdout.write("\r\x1b[2K" + label)
           self._draw_footer_locked()
           sys.stdout.flush()
         idx += 1
         event.wait(0.10)
     self._spin_thread = threading.Thread(target=animate, name="DocMind spinner", daemon=True)
     self._spin_thread.start()
   def stop_spinner(self) -> None:
     event, thread = self._spin_event, self._spin_thread
     self._spin_event = None
     self._spin_thread = None
     if event:
       event.set()
     if thread and thread is not threading.current_thread():
       thread.join(timeout=1)
     if thread and self.ansi:
       self._write("\r\x1b[2K")
   def start_typing(self) -> None:
     self.stop_spinner()
     if self._typing_thread:
       self.finish_typing(True)
     with self._typing_cond:
       self._typing_queue.clear()
       self._typing_chars = 0
       self._typing_done = False
       self._typing_fast = False
       self._typing_abort = False
       self._typing_emitted = 0
     self._write("\n" + ("\x1b[1;36mDocMind\x1b[0m: " if self.color else "DocMind: "))
     def animate() -> None:
       while True:
         with self._typing_cond:
           while not self._typing_queue and not self._typing_done and not self._typing_abort:
             self._typing_cond.wait(0.20)
             if not self._typing_queue and not self._typing_done:
               self.update_footer()
           if self._typing_abort:
             return
           if not self._typing_queue and self._typing_done:
             return
           pending = self._typing_chars
           emitted = self._typing_emitted
           width = 5 if emitted < 240 else (18 if emitted < 1200 else 50)
           if pending > 2500:
             width = max(width, 140)
           if pending > 12000:
             width = max(width, 600)
           if self._typing_fast:
             width = max(width, pending)
           pieces = []
           remaining = width
           while self._typing_queue and remaining > 0:
             part, style = self._typing_queue.popleft()
             take = part[:remaining]
             rest = part[remaining:]
             pieces.append((take, style))
             self._typing_chars -= len(take)
             remaining -= len(take)
             if rest:
               self._typing_queue.appendleft((rest, style))
           emitted_now = sum(len(part) for part, _ in pieces)
           self._typing_emitted += emitted_now
           fast = self._typing_fast
         if pieces:
           with self.lock:
             for part, style in pieces:
               if self.color and style:
                 sys.stdout.write("\x1b[" + style + "m" + part + "\x1b[0m")
               else:
                 sys.stdout.write(part)
             self._draw_footer_locked()
             sys.stdout.flush()
         if not fast:
           time.sleep(0.018)
     self._typing_thread = threading.Thread(target=animate, name="DocMind typing", daemon=True)
     self._typing_thread.start()
   def append_typing(self, text: str, style: Optional[str] = None) -> None:
     with self._typing_cond:
       self._typing_queue.append((text, style))
       self._typing_chars += len(text)
       self._typing_cond.notify()
   def finish_typing(self, fast: bool = False) -> None:
     thread = self._typing_thread
     if not thread:
       return
     with self._typing_cond:
       self._typing_fast = fast
       self._typing_done = True
       self._typing_cond.notify_all()
     try:
       while thread.is_alive():
         thread.join(0.10)
     except KeyboardInterrupt:
       with self._typing_cond:
         self._typing_abort = True
         self._typing_cond.notify_all()
       thread.join(0.5)
       self._typing_thread = None
       self._write("\n")
       raise
     self._typing_thread = None
     self._write("\n\n")
     self.update_footer(force=True)
   @contextmanager
   def spinner(self, message: str):
     self.start_spinner(message)
     try:
       yield
     finally:
       self.stop_spinner()
 return locals()
_dm_install('docmind.ui.terminal_view', _dm_module_18, False)

# ===== docmind/ui/syntax.py (included source) =====
def _dm_module_19():
 """Small streaming, language-agnostic syntax colouring for fenced code.

 No external syntax package is required. Text is never interpreted as terminal
 escapes: the caller sanitizes it, and this module returns plain text plus an
 optional trusted SGR style. The lexer is intentionally lightweight.
 """
 import re
 from typing import Callable, List, Optional, Tuple
 KEYWORDS = set((
   "and as assert async await break case catch class const continue def default "
   "defer del do else elif enum except export extends false False final finally "
   "fn for from func function global go if impl import in interface is let match "
   "mod mut namespace new nil None not null or package pass private protected pub "
   "public raise return self static struct super switch this throw true True try "
   "type typeof undefined use using var void while with yield SELECT FROM WHERE "
   "JOIN INSERT UPDATE DELETE CREATE TABLE VALUES ORDER BY GROUP LIMIT"
 ).split())
 BUILTINS = set(("print len range str int float bool list dict set tuple super open "
         "console Math JSON Array Object Promise String Number" ).split())
 TOKEN_RE = re.compile(
   r'''(?P<string>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`)'''
   r'''|(?P<comment>\#.*|//.*|--.*)'''
   r'''|(?P<number>\b(?:0[xX][0-9a-fA-F]+|\d+(?:\.\d+)?)\b)'''
   r'''|(?P<word>\b[A-Za-z_][A-Za-z_0-9]*\b)'''
 )
 class StreamSyntaxHighlighter:
   """Emit text immediately except code lines, which are coloured on newline."""
   def __init__(self, emit: Callable[[str, Optional[str]], None]):
     self.emit = emit
     self.in_code = False
     self.language = ""
     self.fence_char = ""
     self._prefix: Optional[str] = ""
     self._fence: Optional[str] = None
     self._code = ""
     self._out: List[Tuple[List[str], Optional[str]]] = []
   def _push(self, text: str, style: Optional[str] = None) -> None:
     if not text:
       return
     if self._out and self._out[-1][1] == style:
       self._out[-1][0].append(text)
     else:
       self._out.append(([text], style))
   def _flush_out(self) -> None:
     out, self._out = self._out, []
     for parts, style in out:
       self.emit("".join(parts), style)
   def _highlight(self, line: str) -> None:
     position = 0
     for match in TOKEN_RE.finditer(line):
       self._push(line[position:match.start()])
       token = match.group(0)
       kind = match.lastgroup
       style = None
       if kind == "string":
         style = "32"
       elif kind == "comment":
         style = "2;37"
       elif kind == "number":
         style = "33"
       elif kind == "word" and token in KEYWORDS:
         style = "1;35"
       elif kind == "word" and token in BUILTINS:
         style = "36"
       self._push(token, style)
       position = match.end()
     self._push(line[position:])
   def _ordinary(self, text: str) -> None:
     if not self.in_code:
       self._push(text)
       return
     for ch in text:
       if ch == "\n":
         self._highlight(self._code)
         self._code = ""
         self._push("\n")
       else:
         self._code += ch
         if len(self._code) >= 512:
           self._highlight(self._code)
           self._code = ""
   def feed(self, text: str) -> None:
     for ch in text:
       if self._fence is not None:
         self._fence += ch
         if ch == "\n" or len(self._fence) >= 256:
           line = self._fence
           self._push(line, "2;36")
           self._fence = None
           if self.in_code:
             self.in_code = False
             self.language = ""
             self.fence_char = ""
           else:
             stripped = line.lstrip()
             self.fence_char = stripped[:1]
             self.language = stripped[3:].strip().split(maxsplit=1)[0] if stripped[3:].strip() else ""
             self.in_code = True
           self._prefix = "" if ch == "\n" else None
         continue
       if self._prefix is not None:
         self._prefix += ch
         stripped = self._prefix.lstrip(" ")
         indent = len(self._prefix) - len(stripped)
         if indent <= 3 and not stripped:
           continue
         if indent <= 3 and stripped and stripped[0] in "`~":
           marker = stripped[0]
           if all(c == marker for c in stripped) and len(stripped) < 3:
             continue
           if stripped.startswith(marker * 3) and (not self.in_code or marker == self.fence_char):
             self._fence = self._prefix
             self._prefix = None
             continue
         pending = self._prefix
         self._prefix = None
         self._ordinary(pending)
         if pending.endswith("\n"):
           self._prefix = ""
         continue
       self._ordinary(ch)
       if ch == "\n":
         self._prefix = ""
     self._flush_out()
   def finish(self) -> None:
     if self._fence is not None:
       self._push(self._fence, "2;36")
       self._fence = None
     if self._prefix:
       self._ordinary(self._prefix)
     self._prefix = None
     if self._code:
       self._highlight(self._code)
       self._code = ""
     self._flush_out()
 return locals()
_dm_install('docmind.ui.syntax', _dm_module_19, False)

# ===== docmind/ui/console.py (included source) =====
def _dm_module_20():
 """
 DocMind Dual-Engine Terminal UI (Rich + Pure ANSI Fallback)
 Provides Claude-Code-grade terminal rendering, syntax-highlighted diffs,
 animated spinners, status bars, and high-visibility warning panels.
 """
 import difflib
 import os
 import re
 import sys
 from contextlib import contextmanager
 from pathlib import Path
 from typing import Any, Callable, Dict, Iterator, List, Optional
 from docmind import __version__
 from docmind.config import DocMindConfig, get_provider_spec
 from docmind.core.errors import DocMindAlert, ErrorCategory, mask_secrets
 from docmind.i18n import t
 from docmind.ui.activity import describe_activity
 from docmind.ui.terminal_view import TerminalView
 from docmind.ui.syntax import StreamSyntaxHighlighter
 for _stream in (sys.stdout, sys.stderr):
   try:
     if hasattr(_stream, "reconfigure"):
       _stream.reconfigure(encoding="utf-8", errors="replace")
   except Exception:
     pass
 HAS_RICH = False
 HAS_PROMPT_TOOLKIT = False
 def _visible_controls(value: Any) -> str:
   """Render terminal control bytes visibly instead of letting data move the cursor."""
   return re.sub(r"[\x00-\x08\x0b-\x1f\x7f-\x9f]", lambda m: "\\x%02x" % ord(m.group(0)), str(value))
 SLASH_COMMANDS = [
   "/help",
   "/setup",
   "/api",
   "/model",
   "/lang",
   "/auto",
   "/yolo",
   "/smart",
   "/tokens",
   "/history",
   "/delete",
   "/fiyat",
   "/context",
   "/undo",
   "/tree",
   "/cd",
   "/save",
   "/load",
   "/doctor",
   "/clear",
   "/reset",
   "/exit",
   "/quit",
 ]
 class ConsoleUI:
   def __init__(self, history_file: Optional[Path] = None, input_fn: Optional[Callable[[str], str]] = None) -> None:
     self._input_fn = input_fn
     self.is_tty = bool(sys.stdin and sys.stdin.isatty() and sys.stdout and sys.stdout.isatty())
     self.rich_console = Console(highlight=False) if HAS_RICH else None
     self._prompt_session: Any = None
     self._tool_counter = 0
     self._current_tool_args: Dict[str, Any] = {}
     self._stream_active = False
     self._syntax_highlighter = None
     self._waiting_notice = False
     self.view = TerminalView(self.is_tty)
     if self.is_tty and self._input_fn is None and os.name != "nt":
       try:
         import readline
       except ImportError:
         pass
     if HAS_PROMPT_TOOLKIT and self.is_tty and self._input_fn is None:
       try:
         hist = InMemoryHistory()
         completer = WordCompleter(SLASH_COMMANDS, ignore_case=True, sentence=False)
         self._prompt_session = PromptSession(history=hist, completer=completer)
       except Exception:
         self._prompt_session = None
   def clear(self) -> None:
     try:
       if self.rich_console and self.is_tty:
         self.rich_console.clear()
       else:
         os.system("cls" if os.name == "nt" else "clear")
     except Exception:
       print("\n" * 3)
     _dm_owner_gate()
     print(_DM_OWNER, flush=True)
   def _paint(self, text: str, style: str) -> str:
     return "\x1b[" + style + "m" + text + "\x1b[0m" if self.view.color else text
   def print_startup_authority_warning(self) -> None:
     """Display a compact red warning immediately on startup about full system access."""
     msg = _visible_controls(t("startup_authority_warn"))
     use_red = not os.environ.get("NO_COLOR") and (
       self.view.color or os.name != "nt" or bool(os.environ.get("WT_SESSION") or os.environ.get("TERM"))
     )
     if use_red:
       print(f"\x1b[1;31m  {msg}\x1b[0m", flush=True)
     else:
       print(f"  {msg}", flush=True)
   def print_terminal_permission_box(
     self,
     shell_name: str,
     cwd_str: str,
     code_str: str,
     dangerous: bool = False,
   ) -> None:
     """Render a clear approval box BEFORE running any terminal command or Python code."""
     self.view.stop_spinner()
     safe_shell = _visible_controls(shell_name)
     safe_cwd = _visible_controls(cwd_str)
     safe_code = _visible_controls(mask_secrets(code_str))
     border_col = "1;31" if dangerous else "1;33"
     line_col = "31" if dangerous else "33"
     title = _visible_controls(t("term_perm_header"))
     bar = "─" * 64
     print()
     print(self._paint(f"╭─── 🔐 {title} ", border_col) + self._paint(bar[: max(4, 58 - len(title))] + "╮", line_col))
     print(self._paint("│ ", line_col) + self._paint(f"{t('term_perm_shell'):<18}: ", "1;36") + safe_shell)
     print(self._paint("│ ", line_col) + self._paint(f"{t('term_perm_cwd'):<18}: ", "1;36") + safe_cwd)
     code_lines = safe_code.splitlines() or [safe_code]
     if len(code_lines) == 1:
       print(self._paint("│ ", line_col) + self._paint(f"{t('term_perm_code'):<18}: ", "1;33") + self._paint(code_lines[0], "1;37"))
     else:
       print(self._paint("│ ", line_col) + self._paint(f"{t('term_perm_code')}:", "1;33"))
       for cl in code_lines[:25]:
         print(self._paint("│   ", line_col) + self._paint(cl, "1;37"))
       if len(code_lines) > 25:
         print(self._paint("│   ", line_col) + f"... (+{len(code_lines) - 25} lines)")
     print(self._paint("╰" + bar + "╯", line_col), flush=True)
   def prompt_user_choice(
     self,
     question: str,
     options: List[str],
     default_index: int = 1,
   ) -> str:
     """Display an interactive numbered question box (e.g. target OS choice) and return user's answer."""
     self.view.stop_spinner()
     header = _visible_controls(t("ask_user_header"))
     safe_q = _visible_controls(question.strip())
     clean_opts = [_visible_controls(str(o).strip()) for o in options if str(o).strip()]
     bar = "─" * 64
     print()
     print(self._paint(f"╭─── 💬 {header} ", "1;36") + self._paint(bar[: max(4, 58 - len(header))] + "╮", "36"))
     for qline in safe_q.splitlines():
       print(self._paint("│ ", "36") + self._paint(qline, "1;37"))
     if clean_opts:
       print(self._paint("│", "36"))
       def_idx = max(1, min(len(clean_opts), int(default_index or 1)))
       for idx, opt in enumerate(clean_opts, 1):
         star = " ★" if idx == def_idx else ""
         print(self._paint("│   ", "36") + self._paint(f"[{idx}] ", "1;33") + opt + self._paint(star, "1;32"))
     else:
       def_idx = 1
     print(self._paint("╰" + bar + "╯", "36"), flush=True)
     prompt_txt = t("ask_user_prompt", default=def_idx) if clean_opts else "❯ "
     try:
       raw = self.ask(prompt_txt).strip()
     except (KeyboardInterrupt, EOFError):
       print()
       return clean_opts[def_idx - 1] if clean_opts else ""
     if not raw and clean_opts:
       chosen = clean_opts[def_idx - 1]
       self.info(f"→ {chosen}")
       return chosen
     if raw.isdigit() and clean_opts:
       num = int(raw)
       if 1 <= num <= len(clean_opts):
         chosen = clean_opts[num - 1]
         self.info(f"→ {chosen}")
         return chosen
     return raw
   def print_terminal_used(
     self,
     shell_name: str,
     cwd_str: str,
     code_str: str,
     ok: bool,
     exit_code: int,
     elapsed: float,
     preview: str = "",
     triage_note: str = "",
   ) -> None:
     """Prominently notify the user that the terminal was used and show KULLANILAN KOD."""
     self.view.stop_spinner()
     safe_shell = _visible_controls(shell_name)
     safe_cwd = _visible_controls(cwd_str)
     safe_code = _visible_controls(mask_secrets(code_str))
     header = _visible_controls(t("term_used_header"))
     code_lbl = _visible_controls(t("term_used_code"))
     status_lbl = _visible_controls(t("term_used_status"))
     out_lbl = _visible_controls(t("term_used_output"))
     border_col = "1;32" if ok else "1;31"
     line_col = "36" if ok else "31"
     bar = "━" * 64
     status_txt = (
       f"✔ OK (exit={exit_code}, {elapsed:.2f}s)"
       if ok
       else f"✖ EXIT={exit_code} ({elapsed:.2f}s)"
     )
     print()
     print(self._paint(f"┏━━━ 💻 {header} ", border_col) + self._paint(bar[: max(4, 58 - len(header))] + "┓", line_col))
     print(self._paint("┃ ", line_col) + self._paint(f"{t('term_perm_shell'):<17}: ", "36") + safe_shell)
     print(self._paint("┃ ", line_col) + self._paint(f"{t('term_perm_cwd'):<17}: ", "36") + safe_cwd)
     code_lines = safe_code.splitlines() or [safe_code]
     if len(code_lines) == 1:
       print(self._paint("┃ ", line_col) + self._paint(f"{code_lbl:<17}: ", "1;33") + self._paint(code_lines[0], "1;37"))
     else:
       print(self._paint("┃ ", line_col) + self._paint(f"{code_lbl} :", "1;33"))
       for cl in code_lines[:20]:
         print(self._paint("┃   ", line_col) + self._paint(cl, "1;37"))
       if len(code_lines) > 20:
         print(self._paint("┃   ", line_col) + f"... (+{len(code_lines) - 20} lines)")
     print(self._paint("┃ ", line_col) + self._paint(f"{status_lbl:<17}: ", "36") + self._paint(status_txt, border_col))
     if preview and preview.strip():
       clean_prev = _visible_controls(mask_secrets(preview.strip()))
       prev_lines = clean_prev.splitlines()
       print(self._paint("┃ ", line_col) + self._paint(f"{out_lbl}:", "2"))
       for pl in prev_lines[:10]:
         print(self._paint("┃   ", line_col) + pl[:160])
       if len(prev_lines) > 10:
         print(self._paint("┃   ", line_col) + self._paint(f"... (+{len(prev_lines) - 10} satır / lines)", "2"))
     if triage_note:
       note_col = "1;33" if "↻" in triage_note else "1;31"
       print(self._paint("┃ ", line_col) + self._paint(_visible_controls(triage_note), note_col))
     print(self._paint("┗" + bar + "┛", line_col), flush=True)
   def print_banner(self) -> None:
     _dm_owner_gate()
     _dm_signature_gate()
     if not self.view.color or self.view._size()[1] < 30:
       print(f"\nDocMind v1.0  •  {_DM_OWNER}\n")
       return
     pixels = (
       "......PP......", ".....P..P.....", ".....PPPP.....",
       "...TTTPPTTT...", ".PTTTTTTTTTTP.", "PTTDDDDDDDDTTP",
       "PTTDDTDDTDDTTP", "PTTDDTDDTDDTTP", ".PTDDDDDDDDTP.",
       "..TTTTTTTTTT..", "...TTTTPPTT...", "....TTT..TT...",
     )
     palette = {"T": 37, "P": 99, "D": 17}
     print()
     for i in range(0, len(pixels), 2):
       cells = []
       for upper, lower in zip(pixels[i], pixels[i+1]):
         if upper == "." and lower == ".":
           cells.append(" ")
         elif upper == ".":
           cells.append(f"\x1b[38;5;{palette[lower]}m▄\x1b[0m")
         elif lower == ".":
           cells.append(f"\x1b[38;5;{palette[upper]}m▀\x1b[0m")
         else:
           cells.append(f"\x1b[38;5;{palette[upper]};48;5;{palette[lower]}m▀\x1b[0m")
       label = ("  " + self._paint("DocMind v1.0", "1;36") + self._paint("  •  DEVRAN E. / BEYİP_", "1;35")) if i == 4 else ""
       print("  " + "".join(cells) + label)
     print()
   @contextmanager
   def live_footer(self, get_status: Callable[[], str], compact_status=None):
     active = self.view.start_footer(get_status, compact_status)
     try:
       yield active
     finally:
       self.view.stop_spinner()
       self.view.stop_footer()
   def refresh_footer(self) -> None:
     self.view.update_footer(force=True)
   def show_inline_status(self, status: str) -> None:
     if not self.view.footer_active:
       print("  " + _visible_controls(status), flush=True)
   def print_status_bar(
     self,
     cfg: DocMindConfig,
     total_tokens: int = 0,
     input_tokens: int = 0,
     output_tokens: int = 0,
     cwd: Optional[Path] = None,
   ) -> None:
     spec = get_provider_spec(cfg.provider)
     mode_label = t("mode_auto_short") if cfg.permission_mode == "auto" else t("mode_smart_short")
     mode_color = "bright_magenta" if cfg.permission_mode == "auto" else "bright_green"
     key_ok = cfg.has_valid_credentials()
     prov_part = f"{spec.name} • {cfg.model}" if key_ok else f"{spec.name} • {t('status_no_key')}"
     tok_part = t("status_tokens", total=f"{total_tokens:,}", inp=f"{input_tokens:,}", out=f"{output_tokens:,}")
     active_cwd = str(cwd or Path.cwd())
     if len(active_cwd) > 48:
       active_cwd = "..." + active_cwd[-45:]
     if self.rich_console:
       line = (
         f"[bold cyan]⚡ {prov_part}[/bold cyan]  │  "
         f"[{mode_color}]🛡️ {mode_label}[/{mode_color}]  │  "
         f"[bright_yellow]🌐 {cfg.language.upper()}[/bright_yellow]  │  "
         f"[bright_blue]🪙 {tok_part}[/bright_blue]  │  "
         f"[dim]📂 {active_cwd}[/dim]"
       )
       self.rich_console.print(Panel(line, border_style="dim cyan", box=box.SQUARE, padding=(0, 1)))
     else:
       print(f"[ {prov_part} | {mode_label} | {cfg.language.upper()} | {tok_part} | {active_cwd} ]")
   def info(self, msg: str) -> None:
     msg = _visible_controls(msg)
     if self.rich_console:
       self.rich_console.print(Text("ℹ ", style="bright_cyan") + Text(msg))
     else:
       print(self._paint(f"[i] {msg}", "36"))
   def success(self, msg: str) -> None:
     msg = _visible_controls(msg)
     if self.rich_console:
       self.rich_console.print(Text("✔ ", style="bold bright_green") + Text(msg, style="green"))
     else:
       print(self._paint(f"[OK] {msg}", "32"))
   def warn(self, msg: str) -> None:
     msg = _visible_controls(msg)
     if self.rich_console:
       self.rich_console.print(Text("⚠ ", style="bold bright_yellow") + Text(msg, style="bright_yellow"))
     else:
       print(self._paint(f"[!] {msg}", "33"))
   def print_alert(self, alert: DocMindAlert) -> None:
     """Render a prominent, color-coded alert box for token exhaustion, API, network, or tool errors."""
     critical_cats = {ErrorCategory.QUOTA_EXHAUSTED, ErrorCategory.AUTH_INVALID}
     is_critical = alert.category in critical_cats
     border = "bold bright_red" if is_critical else "bold bright_yellow"
     icon = "🚨" if is_critical else "⚠️"
     if self.rich_console:
       body = Text()
       body.append(_visible_controls(alert.description))
       if alert.status_code:
         body.append(f"\n[HTTP Status: {alert.status_code}]", style="dim")
       panel = Panel(
         body,
         title=f"[{border}]{icon} {alert.title}[/{border}]",
         border_style=border,
         box=box.DOUBLE if is_critical else box.ROUNDED,
         padding=(1, 2),
       )
       self.rich_console.print(panel)
     else:
       sep = "!" * 68 if is_critical else "-" * 68
       color = "1;31" if is_critical else "1;33"
       print("\n" + self._paint(sep, color))
       print(self._paint(f"{icon} {_visible_controls(alert.title)}", color))
       print(_visible_controls(alert.description))
       if alert.status_code:
         print(f"[HTTP Status: {alert.status_code}]")
       print(self._paint(sep, color) + "\n")
   def print_panel(self, title: str, body: str, style: str = "cyan") -> None:
     title, body = _visible_controls(title), _visible_controls(body)
     if self.rich_console:
       self.rich_console.print(
         Panel(Text(body), title=Text(title, style=f"bold {style}"), border_style=style, box=box.ROUNDED, padding=(0, 2))
       )
     else:
       head = self._paint(f"=== {title} ===", "1;36")
       print(f"\n{head}\n{body}\n" + self._paint("=" * (len(title) + 8), "36"))
   def begin_turn(self) -> None:
     self._tool_counter = 0
     self._waiting_notice = False
   def stream_assistant_text(self, text: str) -> None:
     safe = _visible_controls(text)
     if not self._stream_active:
       self._stream_active = True
       self.view.start_typing()
       self._syntax_highlighter = StreamSyntaxHighlighter(self.view.append_typing) if self.view.color else None
     if self._syntax_highlighter:
       self._syntax_highlighter.feed(safe)
     else:
       self.view.append_typing(safe)
   def finish_streamed_message(self, fast: bool = False) -> None:
     if self._stream_active:
       try:
         if self._syntax_highlighter:
           self._syntax_highlighter.finish()
         self.view.finish_typing(fast=fast)
       finally:
         self._syntax_highlighter = None
         self._stream_active = False
   def print_assistant_message(self, content: str, thought: str = "") -> None:
     if not content or not content.strip():
       return
     if self.is_tty:
       self.stream_assistant_text(content)
       self.finish_streamed_message()
     else:
       print(f"\nDocMind: {_visible_controls(content)}\n")
   def print_history_message(self, label: str, content: str, cancelled: bool = False) -> None:
     suffix = " (" + t("history_cancelled") + ")" if cancelled else ""
     caption = self._paint(_visible_controls(label) + suffix, "1;36" if label == "DocMind" else "1;35")
     safe = _visible_controls(content)
     print(f"\n{caption}: ", end="")
     if label == "DocMind" and self.view.color:
       def emit(text: str, style: Optional[str]) -> None:
         print(self._paint(text, style) if style else text, end="")
       highlighter = StreamSyntaxHighlighter(emit)
       highlighter.feed(safe)
       highlighter.finish()
       print()
     else:
       print(safe)
   def print_tool_start(self, tool_name: str, args: Dict[str, Any]) -> None:
     self._tool_counter += 1
     self._current_tool_args = dict(args)
     label = describe_activity(tool_name, args, "pending")
     line = f"  {self._tool_counter}. … {label}"
     if self.rich_console:
       self.rich_console.print(Text(line, style="dim"))
     else:
       print(line, flush=True)
   def print_tool_result(self, tool_name: str, ok: bool, summary: str) -> None:
     skipped = not ok and str(summary) == t("tool_skipped", name=tool_name)
     stage = "done" if ok else ("skipped" if skipped else "failed")
     label = describe_activity(tool_name, self._current_tool_args, stage)
     line = f"     {'✓' if ok else '–' if skipped else '⚠'} {label}"
     if self.rich_console:
       self.rich_console.print(Text(line, style="green" if ok else "yellow"))
     else:
       print(self._paint(line, "32" if ok else "33" if skipped else "31"), flush=True)
     if not ok and not skipped and summary:
       first = _visible_controls(str(summary).strip().splitlines()[0])[:240]
       print("     " + first, flush=True)
   def print_diff(self, path: str, old_text: str, new_text: str, max_lines: int = 40) -> None:
     lines = difflib.unified_diff(old_text.splitlines(), new_text.splitlines(), lineterm="")
     added = removed = 0
     for line in lines:
       if line.startswith("+") and not line.startswith("+++"):
         added += 1
       elif line.startswith("-") and not line.startswith("---"):
         removed += 1
     if added or removed:
       print(f"       +{added} / -{removed}", flush=True)
   @contextmanager
   def spinner(self, message: Optional[str] = None) -> Iterator[None]:
     msg = _visible_controls(message or t("thinking"))
     with self.view.spinner(msg):
       yield
   def ask_secret(self, prompt_text: str = "") -> str:
     """Read a credential visibly, bypassing readline and prompt-toolkit history.

         The terminal's ordinary echo displays characters; input is not recorded
         as a chat message or placed in the app's line-editing history. Screen
         recordings and anyone watching can see the key, as warned by the wizard.
         """
     if self._input_fn is not None:
       return self._input_fn(prompt_text)
     if not sys.stdin or not sys.stdin.isatty():
       raise RuntimeError("API key input requires a terminal; use a provider API-key environment variable instead.")
     old_settings = None
     try:
       if os.name == "posix":
         try:
           import termios
           old_settings = termios.tcgetattr(sys.stdin.fileno())
           if not old_settings[3] & termios.ECHO:
             visible_settings = list(old_settings)
             visible_settings[3] |= termios.ECHO
             termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, visible_settings)
         except (ImportError, OSError, ValueError):
           old_settings = None
       sys.stdout.write(prompt_text)
       sys.stdout.flush()
       line = sys.stdin.readline()
       if line == "":
         raise EOFError
       return line.rstrip("\r\n")
     finally:
       if old_settings is not None:
         try:
           termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, old_settings)
         except (OSError, ValueError):
           pass
   def ask(self, prompt_text: str = "", allow_multiline: bool = False) -> str:
     """Read input safely with multi-line backslash continuation and zero crash on EOF."""
     if self._input_fn is not None:
       return self._input_fn(prompt_text)
     lines: List[str] = []
     current_prompt = prompt_text
     while True:
       if self._prompt_session is not None and allow_multiline:
         line = self._prompt_session.prompt(HTML("<b><ansicyan>DocMind</ansicyan> <ansibrightgreen>❯</ansibrightgreen></b> "))
       else:
         if self.rich_console and not allow_multiline and prompt_text:
           self.rich_console.print(f"[bold bright_cyan]{current_prompt}[/bold bright_cyan]", end="")
           line = input("")
         else:
           line = input(current_prompt or "DocMind > ")
       if allow_multiline and line.endswith("\\"):
         lines.append(line[:-1])
         current_prompt = "... "
         continue
       lines.append(line)
       break
     return "\n".join(lines)
 return locals()
_dm_install('docmind.ui.console', _dm_module_20, False)

# ===== docmind/core/permissions.py (included source) =====
def _dm_module_21():
 """
 DocMind Smart Permission & Mandatory Terminal Consent Guard
 - Read-only & navigation tools execute seamlessly across the entire computer.
 - Terminal & Python execution (run_command, python_eval) ALWAYS ask explicit user
   approval BEFORE running (even in 'auto' mode) and show the exact command/code.
 - Catastrophic OS destruction patterns require typing the full confirmation word.
 """
 from typing import Optional
 from docmind.config import ConfigManager
 from docmind.core.safety import is_catastrophic_command
 from docmind.i18n import i18n, t
 from docmind.ui.console import ConsoleUI
 READ_ONLY_TOOLS = {
   "read_file",
   "list_directory",
   "change_directory",
   "list_system_drives",
   "search_files",
   "grep_search",
   "project_overview",
   "check_syntax",
   "system_info",
   "find_processes",
   "ask_user",
 }
 TERMINAL_TOOLS = {"run_command", "python_eval"}
 _YES_TOKENS = {"e", "evet", "onay", "tamam", "y", "yes", "j", "ja", "s", "si", "sí", "o", "oui", "д", "да", "1"}
 _NO_TOKENS = {"h", "hayir", "hayır", "iptal", "red", "n", "no", "nein", "non", "нет", "0", "skip"}
 _FULL_YES_WORDS = {"evet", "yes", "onay", "ja", "si", "sí", "oui", "да"}
 class PermissionManager:
   def __init__(self, config_mgr: ConfigManager, ui: ConsoleUI, non_interactive: bool = False) -> None:
     self.config_mgr = config_mgr
     self.ui = ui
     self.non_interactive = non_interactive
   @property
   def mode(self) -> str:
     return self.config_mgr.config.permission_mode
   def set_mode(self, mode: str) -> None:
     clean = "auto" if mode == "auto" else "smart"
     self.config_mgr.config.permission_mode = clean
     self.config_mgr.save()
   def check_terminal_permission(
     self,
     tool_name: str,
     code_text: str,
     shell_label: str,
     cwd_str: str,
   ) -> bool:
     """
         Mandatory pre-execution user consent BEFORE running any terminal command or Python snippet.
         """
     dangerous = is_catastrophic_command(code_text)
     if self.non_interactive:
       if dangerous:
         self.ui.warn("Blocked catastrophic command in non-interactive mode.")
         return False
       return True
     self.ui.print_terminal_permission_box(
       shell_name=shell_label,
       cwd_str=cwd_str,
       code_str=code_text,
       dangerous=dangerous,
     )
     if dangerous:
       self.ui.warn(t("perm_dangerous_warn"))
     is_real_tty = bool(getattr(self.ui, "is_tty", False) and getattr(self.ui, "_input_fn", None) is None)
     max_tries = 3 if is_real_tty else 1
     for attempt in range(max_tries):
       try:
         prompt_lbl = t("perm_dangerous_prompt") if dangerous else t("term_perm_prompt")
         raw = self.ui.ask(prompt_lbl).replace("İ", "i").replace("I", "ı").strip().lower().replace("\u0307", "")
       except (KeyboardInterrupt, EOFError):
         print()
         self.ui.warn(t("term_perm_denied"))
         return False
       if not raw:
         if attempt + 1 < max_tries:
           self.ui.warn(t("term_perm_reprompt"))
           continue
         self.ui.warn(t("term_perm_denied"))
         return False
       if dangerous:
         if raw in _FULL_YES_WORDS:
           return True
         if raw in _NO_TOKENS:
           self.ui.warn(t("term_perm_denied"))
           return False
         if attempt + 1 < max_tries:
           self.ui.warn(t("perm_dangerous_prompt"))
           continue
         self.ui.warn(t("term_perm_denied"))
         return False
       if raw in _YES_TOKENS:
         return True
       if raw in _NO_TOKENS:
         self.ui.warn(t("term_perm_denied"))
         return False
       if attempt + 1 < max_tries:
         self.ui.warn(t("term_perm_reprompt"))
         continue
     self.ui.warn(t("term_perm_denied"))
     return False
   def check_tool_permission(
     self,
     tool_name: str,
     action_summary: str,
     command_text: Optional[str] = None,
     sensitive: bool = False,
   ) -> bool:
     """
         Return True if execution is approved, False if user skipped.
         """
     if sensitive:
       if self.non_interactive:
         return False
       self.ui.print_panel(t("perm_title"), f"{t('perm_sensitive_warning')}\n\n{action_summary}", style="bright_red")
       try:
         raw = self.ui.ask(t("perm_sensitive_prompt")).replace("İ", "i").replace("I", "ı").strip().lower().replace("\u0307", "")
       except (KeyboardInterrupt, EOFError):
         return False
       return raw in _FULL_YES_WORDS
     if tool_name in TERMINAL_TOOLS:
       return self.check_terminal_permission(
         tool_name=tool_name,
         code_text=command_text or action_summary,
         shell_label=tool_name,
         cwd_str=".",
       )
     if tool_name in READ_ONLY_TOOLS:
       return True
     if self.mode == "auto" or self.non_interactive:
       return True
     detail = (action_summary + "\n\n" + t("perm_command_warn", cmd=command_text)) if command_text else action_summary
     self.ui.print_panel(t("perm_title"), detail, style="yellow")
     try:
       raw = self.ui.ask(t("perm_prompt")).replace("İ", "i").replace("I", "ı").strip().lower().replace("\u0307", "")
     except (KeyboardInterrupt, EOFError):
       print()
       return False
     if raw == "":
       return False
     lang = i18n.lang
     auto_tokens = {"a", "auto", "yolo", "otomatik", "авто"}
     if lang == "tr":
       auto_tokens.add("o")
     if raw in auto_tokens:
       self.set_mode("auto")
       self.ui.success(t("perm_switched_auto"))
       return True
     if raw in _NO_TOKENS:
       return False
     if raw in _YES_TOKENS:
       return True
     return False
 return locals()
_dm_install('docmind.core.permissions', _dm_module_21, False)

# ===== docmind/tools/registry.py (included source) =====
def _dm_module_22():
 """
 DocMind Central Tool Registry & Universal Cross-Platform Dispatcher
 Provides 20 JSON Schemas for full computer access (Windows & Linux), enforces
 mandatory pre-execution user consent for terminal/code execution, displays
 'TERMİNAL KULLANILDI' & 'KULLANILAN KOD : ...', renders unified diffs, and
 safely handles all errors so the agent loop never crashes.
 """
 from dataclasses import dataclass
 import json
 from pathlib import Path
 import sys
 from typing import Any, Dict, List
 from docmind.config import ConfigManager
 from docmind.core.errors import classify_exception, mask_secrets
 from docmind.core.permissions import PermissionManager
 from docmind.core.safety import sensitive_tool_action
 from docmind.i18n import t
 from docmind.tools.backup import UndoManager
 from docmind.tools.filesystem import (
   resolve_user_path,
   tool_archive,
   tool_change_directory,
   tool_delete_path,
   tool_edit_file,
   tool_list_directory,
   tool_list_system_drives,
   tool_move_or_copy,
   tool_multi_edit,
   tool_read_file,
   tool_undo_file_change,
   tool_write_file,
 )
 from docmind.tools.project import tool_check_syntax, tool_project_overview
 from docmind.tools.search import tool_grep_search, tool_search_files
 from docmind.tools.terminal import (
   resolve_shell_invocation,
   run_command_detailed,
   run_python_detailed,
   tool_find_processes,
   tool_open_path,
   tool_system_info,
 )
 from docmind.tools.web import tool_web_fetch
 from docmind.ui.console import ConsoleUI
 @dataclass
 class ToolExecutionResult:
   ok: bool
   output: str
   skipped: bool = False
   invalid_args: bool = False
 TOOL_SCHEMAS: List[Dict[str, Any]] = [
   {
     "name": "read_file",
     "description": (
       "ONLY use when the user asks to read/inspect/edit a specific file or document. NEVER call proactively on CWD files during greetings or general questions. Read any file anywhere on the computer (supports absolute paths, ~, %USERPROFILE%, Desktop/Masaüstü, "
       "Downloads/İndirilenler, Documents/Belgeler, C:\\..., /etc/..., etc.). Automatically decodes UTF-8/UTF-16/CP1254 "
       "text & code, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), OpenDocument (.odt/.ods/.odp), PDF (.pdf), "
       "SQLite (.sqlite/.db), archives (.zip/.tar.gz), and binary/image metadata."
     ),
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "File path anywhere on the computer."},
         "offset": {"type": "integer", "description": "1-based starting line number (default 1)."},
         "limit": {"type": "integer", "description": "Maximum number of lines to return (default 400)."},
       },
       "required": ["path"],
     },
   },
   {
     "name": "write_file",
     "description": "Create a new file or overwrite an existing file anywhere on the computer. Automatically creates parent folders.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "Target file path."},
         "content": {"type": "string", "description": "Complete text content to write."},
       },
       "required": ["path", "content"],
     },
   },
   {
     "name": "edit_file",
     "description": "Surgically edit an existing file anywhere on the computer by replacing old_text with new_text.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "File path to edit."},
         "old_text": {"type": "string", "description": "Exact existing lines/block to find."},
         "new_text": {"type": "string", "description": "Replacement lines/block."},
         "replace_all": {"type": "boolean", "description": "Replace every occurrence if true (default false)."},
       },
       "required": ["path", "old_text", "new_text"],
     },
   },
   {
     "name": "multi_edit",
     "description": "Apply multiple sequential old_text -> new_text edits to a single file atomically.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "File path to edit."},
         "edits": {
           "type": "array",
           "description": "Ordered list of {old_text, new_text} edit operations.",
           "items": {
             "type": "object",
             "properties": {
               "old_text": {"type": "string"},
               "new_text": {"type": "string"},
             },
             "required": ["old_text", "new_text"],
           },
         },
       },
       "required": ["path", "edits"],
     },
   },
   {
     "name": "delete_path",
     "description": "Delete a file or directory anywhere on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "File or folder path to delete."},
       },
       "required": ["path"],
     },
   },
   {
     "name": "move_or_copy",
     "description": "Move, rename, or copy a file or directory anywhere on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "source": {"type": "string", "description": "Source file or directory path."},
         "destination": {"type": "string", "description": "Destination file or directory path."},
         "operation": {
           "type": "string",
           "enum": ["move", "copy"],
           "description": "'move' (rename/relocate) or 'copy'.",
         },
       },
       "required": ["source", "destination", "operation"],
     },
   },
   {
     "name": "list_directory",
     "description": "ONLY use when the user asks what is inside a folder/project or when locating a requested file. NEVER call for general chat/questions. List files and folders inside any directory on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "Directory path to inspect (default '.')."},
         "recursive": {"type": "boolean", "description": "Recurse into subdirectories if true."},
         "max_depth": {"type": "integer", "description": "Max tree depth (1-5)."},
         "show_hidden": {"type": "boolean", "description": "Show dotfiles/hidden items (default true)."},
       },
     },
   },
   {
     "name": "change_directory",
     "description": "Change the active working directory (cd) to any folder on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "Target directory path (absolute, relative, ~, Desktop, Downloads, etc.)."},
       },
       "required": ["path"],
     },
   },
   {
     "name": "list_system_drives",
     "description": "List all disk drives / mounted filesystems (with free & total GB) and user special folders (Desktop, Downloads, Documents, Home, Temp).",
     "parameters": {
       "type": "object",
       "properties": {},
     },
   },
   {
     "name": "archive_tool",
     "description": "List, extract, or create .zip and .tar.gz archives anywhere on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "action": {"type": "string", "enum": ["list", "extract", "create"], "description": "Archive operation."},
         "archive_path": {"type": "string", "description": "Path to the .zip or .tar.gz archive."},
         "target_paths": {
           "type": "array",
           "items": {"type": "string"},
           "description": "Files/folders to pack when action='create'.",
         },
         "output_dir": {"type": "string", "description": "Destination folder when action='extract'."},
       },
       "required": ["action", "archive_path"],
     },
   },
   {
     "name": "search_files",
     "description": "Find files by glob pattern (e.g. '*.pdf', '*rapor*', '*.py') inside any folder or drive on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "pattern": {"type": "string", "description": "Filename glob pattern, e.g. '*.py' or '*fatura*'."},
         "path": {"type": "string", "description": "Root directory to search from (default '.')."},
         "include_hidden": {"type": "boolean", "description": "Include hidden files/folders if true."},
         "max_results": {"type": "integer", "description": "Maximum results (default 100)."},
       },
       "required": ["pattern"],
     },
   },
   {
     "name": "grep_search",
     "description": "Search file contents using regex or literal text inside any file or folder on the computer.",
     "parameters": {
       "type": "object",
       "properties": {
         "query": {"type": "string", "description": "Regex or text string to search for."},
         "path": {"type": "string", "description": "Directory or file path to search in (default '.')."},
         "file_pattern": {"type": "string", "description": "Optional filename glob filter, e.g. '*.py'."},
         "case_sensitive": {"type": "boolean", "description": "Case-sensitive search if true."},
         "max_matches": {"type": "integer", "description": "Maximum matches (default 80)."},
       },
       "required": ["query"],
     },
   },
   {
     "name": "project_overview",
     "description": "ONLY use when the user explicitly asks to analyze or summarize a project folder/codebase. NEVER call for simple questions or chat.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "Directory path (default '.')."},
         "max_depth": {"type": "integer", "description": "Maximum directory depth (1-5)."},
       },
     },
   },
   {
     "name": "check_syntax",
     "description": "Non-executing syntax check for Python (.py), JSON (.json), or TOML (.toml) files.",
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "File path to syntax-check."},
         "language": {"type": "string", "description": "Optional language override ('python', 'json', 'toml')."},
       },
       "required": ["path"],
     },
   },
   {
     "name": "run_command",
     "description": (
       "Execute a terminal command on the user's OS (Bash/sh on Linux/macOS, PowerShell/CMD on Windows). Use whenever the user chooses/asks to run a command, print output in terminal, run Python/shell snippets, test/build code, or inspect live system state. Do NOT use for casual greetings or pure file reads already handled by read_file. Always asks user approval before executing."
     ),
     "parameters": {
       "type": "object",
       "properties": {
         "command": {"type": "string", "description": "Exact terminal command for the current OS/shell."},
         "shell": {
           "type": "string",
           "enum": ["auto", "bash", "powershell", "cmd", "sh"],
           "description": "Shell to use: 'auto' (Bash on Linux/macOS, PowerShell on Windows), or 'bash', 'powershell', 'cmd', 'sh'.",
         },
         "workdir": {"type": "string", "description": "Optional working directory for this command."},
         "timeout": {"type": "integer", "description": "Timeout in seconds (default 90, max 600)."},
       },
       "required": ["command"],
     },
   },
   {
     "name": "python_eval",
     "description": (
       "Execute a Python 3 snippet/code on the user's computer and return real stdout/stderr. Use whenever the user asks/chooses to run Python code (including printing Hello World, calculations, scripts, or verifications). Do NOT call during casual greetings or when the user chose explanation-only mode. Always asks user approval before executing."
     ),
     "parameters": {
       "type": "object",
       "properties": {
         "code": {"type": "string", "description": "Python 3 code to execute."},
         "timeout": {"type": "integer", "description": "Timeout in seconds (default 45, max 300)."},
       },
       "required": ["code"],
     },
   },
   {
     "name": "open_path",
     "description": "Open any file, folder, application, or URL in the user's desktop OS (Windows Explorer/Start, Linux xdg-open, macOS open).",
     "parameters": {
       "type": "object",
       "properties": {
         "target": {"type": "string", "description": "File path, folder path, application name, or URL to open."},
       },
       "required": ["target"],
     },
   },
   {
     "name": "find_processes",
     "description": "List or filter currently running processes on Windows or Linux/macOS.",
     "parameters": {
       "type": "object",
       "properties": {
         "query": {"type": "string", "description": "Optional process name or PID filter (e.g. 'python', 'chrome', 'node')."},
         "limit": {"type": "integer", "description": "Maximum rows to return (default 60)."},
       },
     },
   },
   {
     "name": "system_info",
     "description": "Inspect OS version, CPU/RAM, Python runtime, available shells (Bash/PowerShell/CMD), mounted drives, and special folders.",
     "parameters": {
       "type": "object",
       "properties": {},
     },
   },
   {
     "name": "undo_file_change",
     "description": (
       "Roll back / revert a broken or unwanted file modification (write_file, edit_file, multi_edit, or file deletion) "
       "using DocMind's snapshot history. Pass 'path' to revert a specific file, or omit 'path' to undo the latest file change."
     ),
     "parameters": {
       "type": "object",
       "properties": {
         "path": {"type": "string", "description": "Optional specific file path to restore to its previous snapshot."},
       },
     },
   },
   {
     "name": "ask_user",
     "description": (
       "Ask the user an interactive question with numbered choices directly in the terminal and receive their immediate answer. "
       "ALWAYS use this BEFORE writing platform-specific scripts/code/commands when the target OS was not explicitly specified "
       "(e.g. 'İşletim sisteminiz Arch Linux (Linux) olarak algılandı; buna uyumlu yapacağım. Başka bir sistem ister misiniz yoksa evrensel mi olsun?')."
     ),
     "parameters": {
       "type": "object",
       "properties": {
         "question": {"type": "string", "description": "Clear question to show the user in their language."},
         "options": {
           "type": "array",
           "items": {"type": "string"},
           "description": "2 to 5 concise choices (option 1 is default if user presses Enter).",
         },
         "default_index": {"type": "integer", "description": "1-based default option index (default 1)."},
       },
       "required": ["question"],
     },
   },
   {
     "name": "web_fetch",
     "description": "Fetch and extract readable text/JSON from an HTTP/HTTPS URL.",
     "parameters": {
       "type": "object",
       "properties": {
         "url": {"type": "string", "description": "Full http:// or https:// URL."},
         "max_chars": {"type": "integer", "description": "Maximum characters to return (default 12000)."},
       },
       "required": ["url"],
     },
   },
 ]
 def _validate_arguments(name: str, args: Any) -> str:
   """Validate tool call arguments against schema before asking permission or executing."""
   definition = next((item for item in TOOL_SCHEMAS if item["name"] == name), None)
   if definition is None:
     return "Unknown tool: " + str(name)
   def check(value: Any, schema: Dict[str, Any], location: str) -> str:
     kind = schema.get("type")
     expected = {
       "object": lambda v: isinstance(v, dict),
       "array": lambda v: isinstance(v, list),
       "string": lambda v: isinstance(v, str),
       "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
       "boolean": lambda v: isinstance(v, bool),
     }
     if kind in expected and not expected[kind](value):
       return f"{location} must be {kind}"
     if "enum" in schema and value not in schema["enum"]:
       return f"{location} must be one of: " + ", ".join(map(str, schema["enum"]))
     if kind == "object":
       for key in schema.get("required", []):
         if key not in value:
           return f"{location}.{key} is required"
       for key, prop in schema.get("properties", {}).items():
         if key in value and value[key] is not None:
           issue = check(value[key], prop, f"{location}.{key}")
           if issue:
             return issue
     elif kind == "array":
       for idx, item in enumerate(value):
         issue = check(item, schema.get("items", {}), f"{location}[{idx}]")
         if issue:
           return issue
     return ""
   return check(args, definition["parameters"], "arguments")
 class ToolRegistry:
   def __init__(
     self,
     config_mgr: ConfigManager,
     ui: ConsoleUI,
     perm_mgr: PermissionManager,
     undo_mgr: UndoManager,
   ) -> None:
     self.config_mgr = config_mgr
     self.ui = ui
     self.perm_mgr = perm_mgr
     self.undo_mgr = undo_mgr
     self.cwd: Path = Path.cwd().resolve()
   def set_cwd(self, new_cwd: Path) -> None:
     self.cwd = new_cwd.resolve()
   def get_schemas(self) -> List[Dict[str, Any]]:
     return TOOL_SCHEMAS
   def _describe_action(self, name: str, args: Dict[str, Any]) -> str:
     if name in ("write_file", "edit_file", "multi_edit", "delete_path"):
       detail = t("perm_file_action", action=name, target=args.get("path", ""))
       if name != "delete_path":
         detail += "\n\n" + json.dumps(args, ensure_ascii=False, indent=2)[:1600]
       return detail
     if name == "move_or_copy":
       op = args.get("operation", "move")
       return t("perm_file_action", action=op, target=f"{args.get('source', '')} -> {args.get('destination', '')}")
     if name == "archive_tool":
       return f"Archive ({args.get('action', '')}): {args.get('archive_path', '')}"
     if name == "open_path":
       return f"Open on desktop: {args.get('target', '')}"
     if name == "web_fetch":
       return f"Web request: {args.get('url', '')}"
     return f"{name}({args})"
   def execute(self, name: str, args: Dict[str, Any]) -> ToolExecutionResult:
     """
         Validate arguments, enforce mandatory terminal consent & transparent reporting,
         execute cross-platform tools, show diffs, and catch any exception cleanly.
         """
     safe_args = args if isinstance(args, dict) else {}
     if name == "edit_file" and isinstance(safe_args, dict):
       if "old_string" in safe_args and "old_text" not in safe_args:
         safe_args = dict(safe_args, old_text=safe_args["old_string"])
       if "new_string" in safe_args and "new_text" not in safe_args:
         safe_args = dict(safe_args, new_text=safe_args["new_string"])
     elif name == "read_file" and isinstance(safe_args, dict) and "start_line" in safe_args and "offset" not in safe_args:
       s_ln = int(safe_args.get("start_line") or 1)
       e_ln = int(safe_args.get("end_line") or (s_ln + 399))
       safe_args = dict(safe_args, offset=s_ln, limit=max(1, e_ln - s_ln + 1))
     self.ui.print_tool_start(name, safe_args)
     try:
       issue = _validate_arguments(name, safe_args)
       if issue:
         out = f"Tool '{name}' was not executed: invalid arguments ({issue}). Correct the call and try again."
         self.ui.print_tool_result(name, False, out)
         return ToolExecutionResult(ok=False, output=out, invalid_args=True)
       if name == "run_command":
         cmd_str = str(safe_args["command"])
         shell_req = str(safe_args.get("shell") or "auto")
         wdir_raw = safe_args.get("workdir")
         exec_dir = resolve_user_path(str(wdir_raw), self.cwd) if wdir_raw else self.cwd
         try:
           _, shell_label = resolve_shell_invocation(shell_req, cmd_str)
         except Exception as shell_exc:
           err_txt = str(shell_exc)
           self.ui.print_tool_result(name, False, err_txt)
           return ToolExecutionResult(ok=False, output=err_txt)
         approved = self.perm_mgr.check_terminal_permission(
           tool_name="run_command",
           code_text=cmd_str,
           shell_label=shell_label,
           cwd_str=str(exec_dir),
         )
         if not approved:
           skip_msg = t("tool_skipped", name=name)
           self.ui.print_tool_result(name, False, skip_msg)
           return ToolExecutionResult(
             ok=False,
             output=f"Terminal command '{cmd_str}' was declined by the user. Respect the refusal and ask or use a non-terminal alternative.",
             skipped=True,
           )
         res = run_command_detailed(
           command=cmd_str,
           cwd=self.cwd,
           timeout=int(safe_args.get("timeout", 90) or 90),
           workdir=str(wdir_raw) if wdir_raw else None,
           shell=shell_req,
         )
         preview = res.get("stdout") or res.get("stderr") or ""
         if res.get("stdout") and res.get("stderr"):
           preview = f"{res['stdout'].rstrip()}\n[STDERR]\n{res['stderr'].rstrip()}"
         triage_obj = res.get("triage")
         triage_txt = t(triage_obj["summary_key"]) if isinstance(triage_obj, dict) and triage_obj.get("summary_key") else ""
         self.ui.print_terminal_used(
           shell_name=str(res.get("shell") or shell_label),
           cwd_str=str(res.get("cwd") or exec_dir),
           code_str=cmd_str,
           ok=bool(res.get("ok")),
           exit_code=int(res.get("exit_code", -1)),
           elapsed=float(res.get("elapsed", 0.0)),
           preview=preview,
           triage_note=triage_txt,
         )
         ok = bool(res.get("ok"))
         out = str(res.get("formatted") or "")
         self.ui.print_tool_result(name, ok, out)
         return ToolExecutionResult(ok=ok, output=out)
       if name == "python_eval":
         code_str = str(safe_args["code"])
         py_label = f"python ({sys.executable})"
         approved = self.perm_mgr.check_terminal_permission(
           tool_name="python_eval",
           code_text=code_str,
           shell_label=py_label,
           cwd_str=str(self.cwd),
         )
         if not approved:
           skip_msg = t("tool_skipped", name=name)
           self.ui.print_tool_result(name, False, skip_msg)
           return ToolExecutionResult(
             ok=False,
             output="Python code execution was declined by the user. Respect the refusal and ask how to proceed.",
             skipped=True,
           )
         res = run_python_detailed(
           code=code_str,
           cwd=self.cwd,
           timeout=int(safe_args.get("timeout", 45) or 45),
         )
         preview = res.get("stdout") or res.get("stderr") or ""
         if res.get("stdout") and res.get("stderr"):
           preview = f"{res['stdout'].rstrip()}\n[STDERR]\n{res['stderr'].rstrip()}"
         triage_obj = res.get("triage")
         triage_txt = t(triage_obj["summary_key"]) if isinstance(triage_obj, dict) and triage_obj.get("summary_key") else ""
         self.ui.print_terminal_used(
           shell_name=str(res.get("shell") or py_label),
           cwd_str=str(res.get("cwd") or self.cwd),
           code_str=code_str,
           ok=bool(res.get("ok")),
           exit_code=int(res.get("exit_code", -1)),
           elapsed=float(res.get("elapsed", 0.0)),
           preview=preview,
           triage_note=triage_txt,
         )
         ok = bool(res.get("ok"))
         out = str(res.get("formatted") or "")
         self.ui.print_tool_result(name, ok, out)
         return ToolExecutionResult(ok=ok, output=out)
       action_desc = self._describe_action(name, safe_args)
       if name in (
         "read_file", "write_file", "edit_file", "multi_edit", "delete_path",
         "list_directory", "change_directory", "search_files", "grep_search",
         "project_overview", "check_syntax",
       ):
         p_arg = str(safe_args.get("path", "."))
         try:
           action_desc += f"\nResolved path: {resolve_user_path(p_arg, self.cwd)}"
         except (OSError, ValueError):
           pass
       approved = self.perm_mgr.check_tool_permission(
         name,
         action_desc,
         command_text=None,
         sensitive=sensitive_tool_action(name, safe_args, self.cwd),
       )
       if not approved:
         skip_msg = t("tool_skipped", name=name)
         self.ui.print_tool_result(name, False, skip_msg)
         return ToolExecutionResult(
           ok=False,
           output=f"Action '{name}' was declined/skipped by the user. Ask how they prefer to proceed.",
           skipped=True,
         )
       diff_payload = None
       if name == "read_file":
         ok, out = tool_read_file(safe_args, self.cwd)
       elif name == "write_file":
         ok, out, diff_payload = tool_write_file(safe_args, self.cwd, self.undo_mgr)
       elif name == "edit_file":
         ok, out, diff_payload = tool_edit_file(safe_args, self.cwd, self.undo_mgr)
       elif name == "multi_edit":
         ok, out, diff_payload = tool_multi_edit(safe_args, self.cwd, self.undo_mgr)
       elif name == "delete_path":
         ok, out = tool_delete_path(safe_args, self.cwd, self.undo_mgr)
       elif name == "move_or_copy":
         ok, out = tool_move_or_copy(safe_args, self.cwd)
       elif name == "list_directory":
         ok, out = tool_list_directory(safe_args, self.cwd)
       elif name == "change_directory":
         ok, out = tool_change_directory(safe_args, self.cwd, self.set_cwd)
       elif name == "list_system_drives":
         ok, out = tool_list_system_drives()
       elif name == "archive_tool":
         ok, out = tool_archive(safe_args, self.cwd)
       elif name == "search_files":
         ok, out = tool_search_files(safe_args, self.cwd)
       elif name == "grep_search":
         ok, out = tool_grep_search(safe_args, self.cwd)
       elif name == "project_overview":
         ok, out = tool_project_overview(safe_args, self.cwd)
       elif name == "check_syntax":
         ok, out = tool_check_syntax(safe_args, self.cwd)
       elif name == "open_path":
         ok, out = tool_open_path(safe_args, self.cwd)
       elif name == "find_processes":
         ok, out = tool_find_processes(safe_args)
       elif name == "undo_file_change":
         ok, out = tool_undo_file_change(safe_args, self.cwd, self.undo_mgr)
       elif name == "ask_user":
         q_str = str(safe_args.get("question", "")).strip()
         opts = [str(x) for x in (safe_args.get("options") or [])]
         def_idx = int(safe_args.get("default_index", 1) or 1)
         if self.perm_mgr.non_interactive:
           chosen = opts[max(0, min(len(opts) - 1, def_idx - 1))] if opts else "default"
           ok, out = True, f"User response (non-interactive default): {chosen}"
         else:
           ans = self.ui.prompt_user_choice(q_str, opts, def_idx)
           ok, out = True, f"User selected / answered: {ans}"
       elif name == "system_info":
         ok, out = tool_system_info(self.cwd)
       elif name == "web_fetch":
         ok, out = tool_web_fetch(safe_args)
       else:
         ok = False
         out = f"Unknown tool '{name}'. Available tools: {', '.join(s['name'] for s in TOOL_SCHEMAS)}"
       if diff_payload is not None and ok:
         fpath, before_txt, after_txt = diff_payload
         self.ui.print_diff(fpath, before_txt, after_txt)
       if ok and name in ("write_file", "edit_file", "multi_edit"):
         raw_path = str(safe_args.get("path", ""))
         if Path(raw_path).suffix.lower() in (
           ".py", ".pyi", ".json", ".toml", ".xml", ".svg", ".sh", ".bash", ".js", ".mjs", ".cjs"
         ):
           check_args = {"path": raw_path}
           if not sensitive_tool_action("check_syntax", check_args, self.cwd):
             try:
               check_ok, check_out = tool_check_syntax(check_args, self.cwd)
               out += "\nAutomatic syntax check: " + check_out
               if check_ok:
                 self.ui.info(t("auto_syntax_ok", path=raw_path))
               else:
                 self.ui.warn(t("auto_syntax_failed", path=raw_path))
                 out += (
                   "\n[ACTION REQUIRED: SYNTAX ERROR INTRODUCED] "
                   "Immediately go back and fix the syntax error in this file using edit_file, "
                   "or revert to the clean snapshot via undo_file_change!"
                 )
             except Exception:
               pass
       self.ui.print_tool_result(name, ok, out)
       return ToolExecutionResult(ok=ok, output=out)
     except KeyboardInterrupt:
       self.ui.print_tool_result(name, False, t("ctrl_c_cancelled"))
       raise
     except Exception as exc:
       self.config_mgr.log_error(f"tool:{name}", repr(exc))
       alert = classify_exception(exc)
       self.ui.print_alert(alert)
       detail = mask_secrets(str(exc))
       for secret in self.config_mgr.config.api_keys.values():
         if secret:
           detail = detail.replace(secret, "[REDACTED]")
       warn_note = t("tool_error_passed", name=name, err=detail)
       self.ui.warn(warn_note)
       self.ui.print_tool_result(name, False, f"{type(exc).__name__}: {detail}")
       return ToolExecutionResult(
         ok=False,
         output=f"Tool '{name}' encountered an error ({type(exc).__name__}: {detail}). Adapt and try an alternative approach.",
       )
 return locals()
_dm_install('docmind.tools.registry', _dm_module_22, False)

# ===== docmind/ui/wizard.py (included source) =====
def _dm_module_23():
 """
 DocMind Interactive Setup & Configuration Wizard
 Handles first-launch onboarding (Language -> Provider -> Model -> API Key -> Mode)
 and mid-session API/model/language hot-swapping without losing conversation context.
 """
 from docmind.config import PROVIDERS, ConfigManager, clean_api_key, get_provider_spec
 from docmind.core.errors import classify_exception
 from docmind.core.providers import ProviderClient
 from docmind.i18n import LANGUAGE_CHOICES, i18n, t
 from docmind.ui.console import ConsoleUI
 class SetupWizard:
   def __init__(self, config_mgr: ConfigManager, ui: ConsoleUI, on_usage=None, on_unknown_usage=None) -> None:
     self.config_mgr = config_mgr
     self.ui = ui
     self.on_usage = on_usage
     self.on_unknown_usage = on_unknown_usage
   def select_language(self) -> str:
     lines = []
     for idx, (code, native_name, label) in enumerate(LANGUAGE_CHOICES, start=1):
       marker = " *" if code == self.config_mgr.config.language else ""
       lines.append(f"  [{idx}] {label}{marker}")
     self.ui.print_panel("🌐 Language / Dil Seçimi", "\n".join(lines), style="bright_cyan")
     raw = self.ui.ask(t("wiz_select_lang")).strip()
     choice_idx = 0
     if raw.isdigit():
       val = int(raw)
       if 1 <= val <= len(LANGUAGE_CHOICES):
         choice_idx = val - 1
     elif raw.lower() in {c[0] for c in LANGUAGE_CHOICES}:
       for i, c in enumerate(LANGUAGE_CHOICES):
         if c[0] == raw.lower():
           choice_idx = i
           break
     selected_code = LANGUAGE_CHOICES[choice_idx][0]
     self.config_mgr.config.language = selected_code
     i18n.set_lang(selected_code)
     self.config_mgr.save()
     self.ui.success(t("wiz_lang_saved"))
     return selected_code
   def select_provider(self) -> str:
     by_id = {spec.id: spec for spec in PROVIDERS}
     order = ["gemini", "anthropic", "openai", "groq", "openrouter", "deepseek", "custom"]
     choices = [by_id[key] for key in order]
     lines = []
     for idx, spec in enumerate(choices, 1):
       name = spec.name
       if spec.id == "custom":
         name = {
           "tr": "Başka / Özel / Yerel (OpenAI uyumlu)",
           "en": "Other / Custom / Local (OpenAI-compatible)",
           "de": "Andere / Benutzerdefiniert / Lokal (OpenAI-kompatibel)",
           "es": "Otro / Personalizado / Local (compatible con OpenAI)",
           "fr": "Autre / Personnalisé / Local (compatible OpenAI)",
           "ru": "Другой / Особый / Локальный (совместим с OpenAI)",
         }.get(i18n.lang, "Other / Custom / Local")
       current = " *" if spec.id == self.config_mgr.config.provider else ""
       lines.append(f"  [{idx}] {name}{current}")
     self.ui.print_panel(f"🤖 {t('wiz_select_provider')}", "\n".join(lines), style="bright_cyan")
     raw = self.ui.ask(t("wiz_provider_prompt")).strip()
     chosen = choices[0]
     if raw.isdigit() and 1 <= int(raw) <= len(choices):
       chosen = choices[int(raw) - 1]
     elif raw:
       chosen = next((spec for spec in choices if spec.id == raw.lower()), choices[0])
     self.config_mgr.config.provider = chosen.id
     if chosen.id == "custom":
       self.select_model()
     else:
       self.config_mgr.config.model = chosen.models[0]
     self.config_mgr.save()
     return chosen.id
   def select_model(self) -> str:
     spec = get_provider_spec(self.config_mgr.config.provider)
     if spec.id == "custom":
       labels = {
         "tr": "Model adı (isteğe bağlı; boş bırakırsanız default-model): ",
         "en": "Model name (optional; blank uses default-model): ",
         "de": "Modellname (optional; leer = default-model): ",
         "es": "Nombre del modelo (opcional; vacío = default-model): ",
         "fr": "Nom du modèle (facultatif ; vide = default-model) : ",
         "ru": "Название модели (необязательно; пусто = default-model): ",
       }
       chosen_model = self.ui.ask(labels.get(i18n.lang, labels["en"])).strip() or "default-model"
     else:
       lines = []
       for idx, m_name in enumerate(spec.models, start=1):
         current = " *" if m_name == self.config_mgr.config.model else ""
         lines.append(f"  [{idx}] {m_name}{current}")
       custom_num = len(spec.models) + 1
       lines.append(f"  [{custom_num}] {t('wiz_custom_model_opt')}")
       self.ui.print_panel(f"🧠 {t('wiz_select_model', provider=spec.name)}", "\n".join(lines), style="bright_cyan")
       raw = self.ui.ask(t("wiz_model_prompt")).strip()
       if raw.isdigit():
         num = int(raw)
         if 1 <= num <= len(spec.models):
           chosen_model = spec.models[num - 1]
         elif num == custom_num:
           chosen_model = self.ui.ask(t("wiz_custom_model_prompt")).strip() or spec.models[0]
         else:
           chosen_model = spec.models[0]
       elif raw:
         chosen_model = raw
       else:
         chosen_model = spec.models[0]
     self.config_mgr.config.model = chosen_model
     self.config_mgr.save()
     return chosen_model
   def prompt_api_key_and_verify(self) -> bool:
     """Read a visible key and offer model/provider changes or a retry on failure."""
     ask_key = True
     ask_custom_url = True
     while True:
       spec = get_provider_spec(self.config_mgr.config.provider)
       existing = self.config_mgr.config.get_api_key(spec.id)
       if ask_key:
         prompt_lbl = (
           t("wiz_api_key_optional", provider=spec.name)
           if spec.key_optional else t("wiz_enter_api_key", provider=spec.name)
         )
         self.ui.info(t("wiz_secret_notice"))
         entered = clean_api_key(self.ui.ask_secret(prompt_lbl))
         if entered:
           self.config_mgr.config.set_api_key(entered, spec.id)
         elif not existing and not spec.key_optional:
           self.ui.warn(t("wiz_api_key_empty"))
           menu = (
             f"  [1] {t('wiz_opt_retry_key')}\n"
             f"  [2] {t('wiz_opt_change_provider')}\n"
             f"  [5] {t('wiz_opt_skip_anyway')}"
           )
           self.ui.print_panel(t("wiz_api_fail_menu"), menu, style="yellow")
           sub = self.ui.ask(t("rec_choose", default="1")).strip() or "1"
           if sub == "2":
             self.select_provider()
             ask_custom_url = True
           elif sub in ("3", "5"):
             self.config_mgr.save()
             return False
           continue
       if spec.id == "custom" and ask_custom_url:
         current_url = self.config_mgr.config.get_base_url("custom")
         entered_url = self.ui.ask(t("wiz_enter_base_url", default=current_url)).strip()
         self.config_mgr.config.set_base_url(entered_url or current_url, "custom")
         ask_custom_url = False
       self.config_mgr.save()
       def retry_notice(key, **values):
         if self.on_unknown_usage:
           self.on_unknown_usage()
         self.ui.warn(t(key, **values))
       client = ProviderClient(self.config_mgr.config, on_effort_fallback=lambda: retry_notice("effort_fallback"))
       client.on_compat_fallback = lambda: retry_notice("compat_fallback")
       client.on_budget_fallback = lambda limit: retry_notice("budget_fallback", limit=limit)
       client.on_probe_retry = lambda: retry_notice("probe_retry")
       client.on_probe_interrupted = self.on_unknown_usage
       client.on_connection_retry = lambda attempt, delay: retry_notice(
         "probe_transient_retry", attempt=attempt, seconds=int(delay + 0.999))
       with self.ui.spinner(t("wiz_testing_api")):
         ok, api_err = client.verify_connection(timeout=30.0)
       if self.on_usage and client.last_verification_response is not None:
         self.on_usage(client.last_verification_response)
       elif not ok and self.on_unknown_usage:
         self.on_unknown_usage()
       if ok:
         self.ui.success(t("wiz_api_ok", provider=spec.name, model=self.config_mgr.config.model))
         self.ui.info(t("doctor_tools_skipped"))
         return True
       if api_err is not None:
         self.ui.print_alert(classify_exception(api_err, provider_name=spec.name, model_name=self.config_mgr.config.model))
       menu = (
         f"  [1] 🔑 {t('wiz_opt_retry_key')}\n"
         f"  [2] 🔄 {t('wiz_opt_change_provider')}\n"
         f"  [3] 🧠 {t('rec_opt_switch_model')}\n"
         f"  [4] 🔁 {t('rec_opt_retry')}\n"
         f"  [5] ⏭️  {t('wiz_opt_skip_anyway')}"
       )
       self.ui.print_panel(t("wiz_api_fail_menu"), menu, style="yellow")
       choice = self.ui.ask(t("rec_choose", default="1")).strip() or "1"
       if choice == "2":
         self.select_provider()
         ask_custom_url = True
         ask_key = True
       elif choice == "3":
         self.select_model()
         ask_key = False
       elif choice == "4":
         ask_key = False
       elif choice == "5":
         self.ui.info(t("err_skipped_notice"))
         return False
       else:
         ask_key = True
   def select_permission_mode(self) -> str:
     lines = [
       f"  [1] 🛡️  {t('wiz_mode_smart')}",
       f"  [2] 🚀 {t('wiz_mode_auto')}",
     ]
     self.ui.print_panel(t("wiz_select_mode"), "\n".join(lines), style="bright_cyan")
     raw = self.ui.ask(t("wiz_mode_prompt")).strip()
     mode = "auto" if raw == "2" else "smart"
     self.config_mgr.config.permission_mode = mode
     self.config_mgr.save()
     return mode
   def run_full_setup(self, skip_language: bool = False) -> None:
     self.ui.print_panel(f"✨ {t('wiz_title')}", t("welcome_subtitle"), style="bright_magenta")
     previous_setup_state = self.config_mgr.config.setup_completed
     try:
       if not skip_language:
         self.select_language()
       self.select_provider()
       self.prompt_api_key_and_verify()
       self.config_mgr.config.setup_completed = True
       self.config_mgr.save()
       self.ui.success(t("wiz_complete"))
     except (KeyboardInterrupt, EOFError):
       print()
       self.config_mgr.config.setup_completed = previous_setup_state
       self.config_mgr.save()
       self.ui.warn(t("ctrl_c_cancelled"))
 return locals()
_dm_install('docmind.ui.wizard', _dm_module_23, False)

# ===== docmind/core/agent.py (included source) =====
def _dm_module_24():
 """
 DocMind Autonomous Agent Engine
 Implements the ReAct + Native Function Calling agent loop with dynamic environment
 awareness, auto-compaction, token exhaustion detection, and interactive self-healing.
 """
 import os
 import hashlib
 import json
 import math
 from itertools import islice
 import platform
 import sys
 import time
 from datetime import datetime
 from pathlib import Path
 from typing import Any, Dict, List, Optional
 from docmind.config import ConfigManager, get_provider_spec
 from docmind.i18n import t
 from docmind.tools.backup import UndoManager
 from docmind.tools.filesystem import get_special_folders, list_mounted_roots
 from docmind.tools.terminal import detect_available_shells, detect_os_profile
 from docmind.tools.registry import ToolExecutionResult, ToolRegistry
 from docmind.ui.console import ConsoleUI
 from docmind.ui.wizard import SetupWizard
 from docmind.core.context import ConversationContext
 from docmind.core.history import ConversationHistory
 from docmind.core.usage import UsageTracker, context_limit_for
 from docmind.core.errors import DocMindAlert, ErrorCategory, classify_exception, retry_delay
 from docmind.core.permissions import PermissionManager, READ_ONLY_TOOLS
 import re
 from docmind.core.providers import ModelResponse, ProviderClient
 from docmind.core.streaming import KEEPALIVE_POOL
 _TR_ASCII_MAP = str.maketrans("çğıöşü", "cgiosu")
 def _tr_fold(text: str) -> str:
   return (text or "").replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "")
 def _ascii_fold(text: str) -> str:
   return _tr_fold(text).translate(_TR_ASCII_MAP)
 _PURE_CHAT_EXACT = {
   "merhaba", "selam", "selamlar", "slm", "sa", "as", "selamun aleykum",
   "gunaydin", "iyi gunler", "iyi aksamlar", "iyi geceler", "merhabalar",
   "nasilsin", "naber", "ne haber", "iyi misin", "keyifler nasil",
   "tesekkurler", "tesekkur ederim", "sag ol", "sagol", "eyvallah",
   "tamam", "tamamdir", "ok", "okay", "peki", "anladim", "harika", "super", "guzel",
   "kimsin", "sen kimsin", "adin ne", "nesin sen", "ne yapabilirsin", "neler yapabilirsin",
   "hi", "hello", "hey", "yo", "good morning", "good evening", "how are you", "whats up",
   "thanks", "thank you", "thx", "who are you", "what is your name", "what can you do",
   "hallo", "hola", "bonjour", "salut", "привет", "здравствуйте", "спасибо",
 }
 _ACTION_CUES_ASCII_RE = re.compile(
   r"(?:"
   r"[/\\~]|\b[a-z]:|"
   r"\.(?:py|js|ts|tsx|jsx|json|md|txt|pdf|docx?|xlsx?|pptx?|odt|ods|odp|zip|tar|gz|sh|bat|ps1|cmd|html?|css|sql|db|sqlite|ya?ml|toml|ini|cfg|conf|log|csv|xml|c|cpp|h|rs|go|java|kt|cs|php|rb)\b|"
   r"\b(?:dosya|klasor|dizin|masaust|indirilen|belge|disk|surucu|"
   r"olustur|duzenle|degistir|guncelle|kaldir|kopyala|adlandir|arsiv|cikar|"
   r"listele|incele|analiz|ozetle|kontrol|duzelt|onar|"
   r"calistir|kostur|baslat|durdur|yukle|indir|derle|test|yazdir|"
   r"terminal|konsol|komut|kabuk|shell|bash|powershell|pwsh|cmd|script|betik|"
   r"pyt?hon|pyrthon|pyhton|phyton|piton|node|npm|pip|git|java|gcc|cargo|go\b|"
   r"print|echo|hello world|merhaba dunya|ekrana|"
   r"proje|repo|uygulama|program|bot|oyun|kod|"
   r"sistem|islem|process|ram\b|cpu\b|bellek|port\b|wifi|paket|pacman|apt\b|dnf\b|winget|brew\b|"
   r"hazirla|tasarla|oku|ac\b|yaz|ekle|sil|tasi|ara|bul|tara|kur|geri al|arac|"
   r"file|folder|directory|path|desktop|download|document|drive|"
   r"read|open|write|create|save|edit|modify|update|delete|remove|move|copy|rename|extract|"
   r"search|find|grep|list|inspect|analyze|summarize|check|fix|debug|undo|"
   r"run|execute|start|stop|kill|install|build|compile|project|app|tool|system|memory|network|fetch|url|https?)"
   r")"
 )
 _TERMINAL_CANDIDATE_RE = re.compile(
   r"\b(?:"
   r"terminal|konsol|komut|kabuk|shell|bash|powershell|pwsh|cmd|"
   r"calistir|kostur|yazdir|print|echo|hello\s+world|merhaba\s+dunya|ekrana\s+yaz|"
   r"pyt?hon|pyrthon|pyhton|phyton|piton|"
   r"run\b|execute\b|compile|derle|test\s+et|testleri|paket\s+kur|pip\s+install|npm\s+run|git\s+"
   r")"
 )
 _PURE_CONCEPT_QUESTION_RE = re.compile(
   r"^(?:nedir|ne\s+demek|farki\s+ne|nasil\s+calisir|what\s+is|what\s+are|why\s+is|explain\s+what)\b|"
   r"\b(?:nedir|ne\s+demek|ne\s+ise\s+yarar)\s*\??$"
 )
 def _should_expose_tools(user_input: str, messages: List[Dict[str, Any]]) -> bool:
   """Only suppress tools on unmistakable greetings / small talk; keep tools available for all real tasks!"""
   raw = (user_input or "").strip()
   if not raw:
     return False
   folded = _ascii_fold(raw)
   norm = re.sub(r"[^\w\s]+", " ", folded, flags=re.UNICODE)
   norm = re.sub(r"\s+", " ", norm).strip()
   if norm in _PURE_CHAT_EXACT:
     return False
   if _ACTION_CUES_ASCII_RE.search(folded):
     return True
   recent_msgs = messages[-4:] if len(messages) >= 4 else messages
   for m in recent_msgs:
     if m.get("role") == "tool" or m.get("tool_calls"):
       return True
     if m.get("role") == "assistant" and "?" in str(m.get("content") or ""):
       return True
   if re.fullmatch(r"[0-9\s+\-*/()%.,=^?]+(?:kac|eder|yapiyor|yapar|equals|what is)?[0-9\s?]*", folded):
     return False
   if len(norm.split()) <= 4 and _PURE_CONCEPT_QUESTION_RE.search(norm):
     return False
   if len(norm.split()) <= 3:
     return False
   return True
 def _is_explain_or_execute_candidate(user_input: str) -> bool:
   """
   Detect requests involving terminal/command/code execution or printing in terminal
   where the agent should ask the user: [1] Explain how to do it vs [2] Run it myself!
   """
   raw = (user_input or "").strip()
   if not raw or raw.startswith("/"):
     return False
   folded = _ascii_fold(raw)
   norm = re.sub(r"[^\w\s]+", " ", folded, flags=re.UNICODE)
   norm = re.sub(r"\s+", " ", norm).strip()
   if norm in _PURE_CHAT_EXACT or _PURE_CONCEPT_QUESTION_RE.search(norm):
     return False
   # Pure file read/summarize without terminal/execution cues should directly read the file
   file_read_only = bool(re.search(r"\b(?:ozetle|oku\b|icerigini|read\b|summarize)\b", folded)) and not bool(
     re.search(r"\b(?:terminal|calistir|kostur|yazdir|print|echo|bash|powershell|cmd)\b", folded)
   )
   if file_read_only:
     return False
   return bool(_TERMINAL_CANDIDATE_RE.search(folded))
 def _tool_fingerprint(name: str, arguments: Any) -> str:
   try:
     encoded = json.dumps([name, arguments], ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str)
   except (TypeError, ValueError):
     encoded = repr((name, arguments))
   return hashlib.sha256(encoded.encode('utf-8', errors='replace')).hexdigest()
 class DocMindAgent:
   def __init__(
     self,
     config_mgr: ConfigManager,
     ui: ConsoleUI,
     non_interactive: bool = False,
   ) -> None:
     self.config_mgr = config_mgr
     self.ui = ui
     self.non_interactive = non_interactive
     self.perm_mgr = PermissionManager(config_mgr, ui, non_interactive=non_interactive)
     self.undo_mgr = UndoManager()
     self.tools = ToolRegistry(config_mgr, ui, self.perm_mgr, self.undo_mgr)
     self.context = ConversationContext()
     self.history = ConversationHistory(config_mgr.home_dir, self._history_error, self._history_fork)
     self.context.on_append = self.history.append
     self.usage = UsageTracker()
     self.wizard = SetupWizard(config_mgr, ui, on_usage=self.record_verification_usage,
                  on_unknown_usage=self.usage.mark_interrupted)
     self._streamed_text = False
     self._streamed_chunks: List[str] = []
     self._turn_system_prompt: Optional[str] = None
     self._turn_exec_mode: str = "auto"
     self.refresh_client()
   def _history_error(self, exc: Exception) -> None:
     self.config_mgr.log_error("history.write", repr(exc))
     self.ui.warn(t("history_write_error"))
   def _history_fork(self) -> None:
     self.ui.warn(t("history_forked"))
   def record_verification_usage(self, resp: ModelResponse, provider: Optional[str] = None,
                  model: Optional[str] = None) -> None:
     self.context.record_usage(resp.input_tokens, resp.output_tokens, update_context=False)
     self.usage.record(provider or self.config_mgr.config.provider, model or self.config_mgr.config.model,
              resp.input_tokens, resp.output_tokens, resp.reported_cost_usd, resp.usage_complete)
     refresh = getattr(self.ui, "refresh_footer", None)
     if refresh:refresh()
   def _receive_stream_text(self, text: str) -> None:
     self._streamed_text = self._streamed_text or bool(text)
     self._streamed_chunks.append(text)
     self.usage.live_chars += len(text)
     callback = getattr(self.ui, "stream_assistant_text", None)
     if callback:
       callback(text)
   def _finish_streamed_message(self, fast: bool = False) -> None:
     if self._streamed_text:
       callback = getattr(self.ui, "finish_streamed_message", None)
       if callback:
         try:
           callback(fast=fast)
         except TypeError:
           callback()
   def status_text(self, width: Optional[int] = None) -> str:
     cfg = self.config_mgr.config
     stats = self.usage.summary(cfg)
     total = f"{self.context.total_tokens:,}"
     if stats['missing_tokens']:
       total += " (" + t("footer_incomplete") + ")"
     if stats['live_tokens']:
       total += " +~" + f"{stats['live_tokens']:,}"
     limit, verified = context_limit_for(cfg)
     estimated = self.context.current_context_estimate()
     estimated += stats['live_tokens']
     pct = (estimated / max(limit, 1)) * 100.0
     limit_label = f"{limit:,}" + ("?" if not verified else "")
     if stats['missing_cost'] and not stats['known_cost_calls']:
       cost = t("footer_unknown")
     else:
       amount = stats['cost']
       decimals = 6 if amount < .01 else (4 if amount < 1 else 2)
       cost = "~$" + f"{amount:.{decimals}f}"
       if stats['missing_cost']:
         cost += " (" + t("footer_incomplete") + ")"
       elif stats['live_tokens']:
         cost += " (" + t("footer_calculating") + ")"
     full = (f"{t('footer_token')}: {total}  |  {t('footer_context')}: ~{estimated:,}/{limit_label} ({pct:.1f}%)"
         f"  |  {t('footer_cost')}: {cost}")
     if width is None or len(full) <= width:
       return full
     number = self.context.total_tokens + stats['live_tokens']
     if number >= 1_000_000_000:
       short_num = f"{number/1_000_000_000:.1f}B"
     elif number >= 1_000_000:
       short_num = f"{number/1_000_000:.1f}M"
     elif number >= 10_000:
       short_num = f"{number/1_000:.1f}k"
     else:
       short_num = f"{number:,}"
     if stats['live_tokens']:
       short_num = "~" + short_num
     if stats['missing_tokens']:
       short_num += "*"
     if stats['missing_cost'] and not stats['known_cost_calls']:
       short_cost = t("footer_unknown")
     else:
       short_cost = "~$" + f"{stats['cost']:.3g}"
       if stats['missing_cost']:
         short_cost += " (" + t("footer_incomplete") + ")"
       elif stats['live_tokens']:
         short_cost += " (" + t("footer_calculating") + ")"
     percent = f"{pct:.1f}" if pct < 1000 else ">999"
     compact = f"T:{short_num} C:{percent}% {short_cost}"
     if len(compact) > width:
       percent = f"{pct:.0f}" if pct < 1000 else ">999"
       short_cost = t("footer_unknown") if stats['missing_cost'] and not stats['known_cost_calls'] else (
         "~$" + f"{stats['cost']:.2g}" + ("*" if stats['missing_cost'] or stats['live_tokens'] else ""))
       compact = f"T:{short_num} C:{percent}% {short_cost}"
     return compact
   def refresh_client(self) -> None:
     supports_stream = bool(getattr(self.ui, "is_tty", False) and
                callable(getattr(self.ui, "stream_assistant_text", None)) and
                not self.non_interactive)
     def retry_notice(key, **values):
       self.usage.mark_interrupted()
       self.ui.warn(t(key, **values))
     self.client = ProviderClient(self.config_mgr.config, self._receive_stream_text if supports_stream else None,
                   on_effort_fallback=lambda: retry_notice("effort_fallback"))
     self.client.on_compat_fallback = lambda: retry_notice("compat_fallback")
     self.client.on_budget_fallback = lambda limit: retry_notice("budget_fallback", limit=limit)
     self.client.on_probe_retry = lambda: retry_notice("probe_retry")
     self.client.on_connection_retry = lambda attempt, delay: retry_notice(
       "probe_transient_retry", attempt=attempt, seconds=int(delay + 0.999))
     self.client.on_probe_interrupted = self.usage.mark_interrupted
     self.client.on_thinking_rebase = lambda: self.ui.info(t("thinking_rebase"))
   def build_system_prompt(self) -> str:
     cwd = self.tools.cwd
     try:
       os_prof = detect_os_profile()
     except Exception:
       os_prof = {
         "os_family": "Windows" if os.name == "nt" else "Linux",
         "pretty_name": f"{platform.system()} {platform.release()}",
         "distro_id": platform.system().lower(),
         "pkg_managers": [],
         "dev_tools": [],
         "desktop": "unknown",
       }
     try:
       folders = get_special_folders()
       folders_str = ", ".join(f"{k}={v}" for k, v in folders.items())
     except Exception:
       folders_str = str(Path.home())
     try:
       roots = list_mounted_roots()
       drives_str = ", ".join(
         f"{r['root']} ({r.get('free_gb', '?')}GB free/{r.get('total_gb', '?')}GB)"
         if "total_gb" in r else str(r["root"])
         for r in roots
       ) or "/"
     except Exception:
       drives_str = "/"
     try:
       shells = detect_available_shells()
       shells_str = ", ".join(f"{k}={v}" for k, v in shells.items()) or "default"
     except Exception:
       shells_str = "default"
     now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
     lang_rule = t("ai_lang_instruction")
     pretty_os = os_prof.get("pretty_name", platform.system())
     os_family = os_prof.get("os_family", platform.system())
     pkg_str = ", ".join(os_prof.get("pkg_managers") or []) or "none detected"
     dev_str = ", ".join(os_prof.get("dev_tools") or []) or "python"
     mode_desc = (
       "Full Auto for file operations (terminal/Python commands STILL ask explicit user permission first)"
       if self.config_mgr.config.permission_mode == "auto"
       else "Smart Confirm (read/search/navigation tools are automatic; file-write and terminal tools ask user approval)"
     )
     return (
       "You are DocMind (created by DEVRAN E. / BEYİP_), an intelligent, self-correcting, OS-aware AI assistant "
       "and software engineering agent.\n\n"
       f"## LANGUAGE RULE\n{lang_rule}\n\n"
       "## RULE #0 — SMART TOOL & TERMINAL DECISION RULES (CRITICAL!)\n"
       "- **GREETINGS & PURE GENERAL KNOWLEDGE -> ZERO TOOLS**: For greetings ('merhaba', 'nasılsın'), casual chat, conceptual definitions "
       "('OOP nedir?'), translations, or general questions unrelated to the computer, call **ZERO TOOLS** and answer directly.\n"
       "- **NEVER BROWSE CWD FILES UNPROMPTED**: Do NOT open or list random files (`read_file`, `list_directory`, `project_overview`) unless the "
       "user actually asks about files, folders, documents, or a project. Prefer native file tools over terminal commands for reading/searching files.\n"
       "- **TERMINAL / CODE REQUESTS -> 2-OPTION CHOICE (EXPLAIN vs. EXECUTE)**:\n"
       "  • When `CURRENT_USER_CHOICE` is set at the bottom of this prompt, obey it strictly (either explain-only with zero tools, or immediately execute via `run_command` / `python_eval`).\n"
       "  • If `CURRENT_USER_CHOICE` is NOT set and the user asks something that could EITHER be explained OR executed in the terminal (e.g. running a command, printing output with Python/shell, checking a live system metric, running a task), "
       "FIRST call `ask_user` with 2 choices (in the user's language): `[1] Nasıl yapılacağını anlatayım` vs `[2] Ben terminal kullanarak çalıştırayım`, then strictly follow their choice!\n\n"
       "## LIVE COMPUTER & DISTRO ENVIRONMENT\n"
       f"- Date/Time: {now_str}\n"
       f"- Exact OS / Distro: {pretty_os} (Family: {os_family}, ID: {os_prof.get('distro_id', 'unknown')}, Arch: {platform.machine()})\n"
       f"- Desktop / Display Session: {os_prof.get('desktop', 'unknown')}\n"
       f"- Installed Package Managers: {pkg_str}\n"
       f"- Installed Dev Tools: {dev_str}\n"
       f"- Python Runtime: {sys.version.split()[0]} ({sys.executable})\n"
       f"- Active Working Directory (CWD): {cwd}\n"
       f"- Mounted Drives / Roots: {drives_str}\n"
       f"- User Special Folders: {folders_str}\n"
       f"- Available Shells for run_command: {shells_str}\n"
       f"- Permission Mode: {mode_desc}\n\n"
       "## MANDATORY OPERATING RULES WHEN TOOLS ARE NEEDED\n"
       "1. **OS & Distro Mastery + Target OS Confirmation Before Writing Files/Scripts**:\n"
       f"   - You know the user's exact system is **{pretty_os} ({os_family})** with package managers [{pkg_str}]. "
       "Always tailor system commands to this exact OS/distro (e.g., `pacman` on Arch Linux, `apt` on Debian/Ubuntu, `dnf` on Fedora, PowerShell/`winget` on Windows).\n"
       "   - When the user asks you to build/save a platform-dependent script, program, or tool — unless they already specified the target OS — "
       f"FIRST call `ask_user` to confirm whether they want it tailored to **{pretty_os} ({os_family})**, **cross-platform (Windows + Linux)**, or another OS.\n\n"
       "2. **Self-Reflection, Error Triage & Rollback Loop**:\n"
       "   - **When `run_command` or `python_eval` FAILS**:\n"
       "     • **Case A — Requires User Password / `sudo` / `root` / Administrator (`USER_MUST_RUN_MANUALLY`)**: "
       "DO NOT retry privileged/password commands! Explain clearly why elevation is required and provide the exact ready-to-copy command for the user to run in their own terminal.\n"
       "     • **Case B — Fixable by Agent (`AGENT_SELF_REPAIR_POSSIBLE`)**: Fix the command/code, request approval via `run_command` / `python_eval`, and verify the result.\n"
       "   - **When opening/editing a file fails**: Use `[SELF-RECOVERY HINT]` or `search_files` to resolve wrong paths; if `Automatic syntax check` fails after an edit, immediately repair it with `edit_file` or revert cleanly via `undo_file_change`.\n\n"
       "3. **Full Computer Access When Requested & Security**:\n"
       "   - When the user DOES ask about files/drives/documents ('masaüstündeki pdfi özetle', 'indirilenlerdeki zipi çıkar', 'D diskine bak'), use native tools directly across any path or drive (`read_file` supports text/code, `.docx`, `.xlsx`, `.pptx`, `.odt`/`.ods`/`.odp`, `.pdf`, `.sqlite`, `.zip`/`.tar.gz`).\n"
       "   - Never fabricate tool outputs when performing system tasks. Respect user permission denials immediately. Never exfiltrate credentials or private keys."
     )
   def _sleep_interruptible(self, seconds: float, attempt: int = 1) -> bool:
     """Wait without closing the terminal; Ctrl+C cancels only this task."""
     wait = max(1, math.ceil(seconds))
     self.ui.warn(t("retry_wait", seconds=wait, attempt=attempt))
     try:
       with self.ui.spinner(t("retry_wait", seconds=wait, attempt=attempt)):
         deadline = time.monotonic() + wait
         while time.monotonic() < deadline:
           time.sleep(min(.2, max(0, deadline - time.monotonic())))
       return True
     except KeyboardInterrupt:
       print()
       self.ui.warn(t("ctrl_c_cancelled"))
       return False
   def _interactive_recovery(self, alert: DocMindAlert) -> str:
     """
         Show recovery options when API quota/tokens run out, key is invalid, model is missing,
         or network fails. Returns action: 'retry' | 'skip'.
         """
     if self.non_interactive:
       self.ui.info(t("err_skipped_notice"))
       return "skip"
     default_opt = "5" if alert.retry_exhausted else ("1" if alert.suggest_key_change else ("3" if alert.suggest_model_change else "4"))
     menu_lines = [
       f"  [1] 🔑 {t('rec_opt_new_key')}",
       f"  [2] 🔄 {t('rec_opt_switch_provider')}",
       f"  [3] 🧠 {t('rec_opt_switch_model')}",
       f"  [4] 🔁 {t('rec_opt_retry')}",
       f"  [5] ⏭️  {t('rec_opt_skip')}",
     ]
     self.ui.print_panel(f"🛠️ {t('rec_title')}", "\n".join(menu_lines), style="bright_yellow")
     try:
       choice = self.ui.ask(t("rec_choose", default=default_opt)).strip() or default_opt
     except (KeyboardInterrupt, EOFError):
       print()
       return "skip"
     if choice == "1":
       spec = get_provider_spec(self.config_mgr.config.provider)
       self.ui.info(t("wiz_secret_notice"))
       new_key = self.ui.ask_secret(t("wiz_enter_api_key", provider=spec.name)).strip()
       if new_key:
         self.config_mgr.config.set_api_key(new_key, spec.id)
         self.config_mgr.save()
         self.refresh_client()
         return "retry"
       return "skip"
     if choice == "2":
       self.wizard.select_provider()
       self.wizard.prompt_api_key_and_verify()
       self.refresh_client()
       return "retry"
     if choice == "3":
       self.wizard.select_model()
       self.refresh_client()
       return "retry"
     if choice == "4":
       return "retry"
     self.ui.info(t("err_skipped_notice"))
     return "skip"
   def _generate_resilient(self) -> Optional[ModelResponse]:
     """
         Execute an LLM API call wrapped in full error classification, auto-compaction,
         rate-limit backoff, token exhaustion alerting, and interactive hot-swap recovery.
         """
     auto_retries = 0
     incomplete_streams = 0
     compaction_attempted = False
     invalid_tool_retried = False
     while True:
       spec = get_provider_spec(self.config_mgr.config.provider)
       context_limit, _ = context_limit_for(self.config_mgr.config)
       if self.context.needs_compaction(context_limit):
         self.ui.info(t("compacting_context"))
         if self.context.compact():
           self.ui.success(t("context_compacted"))
       sys_prompt = self._turn_system_prompt or self.build_system_prompt()
       if invalid_tool_retried and spec.protocol != "anthropic":
         sys_prompt += ("\n\nThe previous response contained malformed tool arguments and was not executed. "
                "Return a complete JSON object matching the tool schema, or answer without a tool.")
       last_user_msg = ""
       for _m in reversed(self.context.messages):
         if _m.get("role") == "user":
           last_user_msg = str(_m.get("content") or "")
           break
       if self._turn_exec_mode == "explain":
         tool_schemas = []
       elif self._turn_exec_mode == "execute":
         tool_schemas = self.tools.get_schemas()
       else:
         has_tool_turn_already = bool(self.context.messages and self.context.messages[-1].get("role") == "tool")
         expose_tools = has_tool_turn_already or _should_expose_tools(last_user_msg, self.context.messages[:-1])
         tool_schemas = self.tools.get_schemas() if expose_tools else []
       try:
         self._streamed_text = False
         self._streamed_chunks = []
         with self.ui.spinner(t("thinking")):
           resp = self.client.generate(
             system_prompt=sys_prompt,
             messages=self.context.messages,
             tools=tool_schemas,
           )
         if auto_retries:
           self._finish_streamed_message(fast=bool(resp.tool_calls))
           self.ui.success(t("retry_ok"))
         return resp
       except KeyboardInterrupt:
         self.usage.mark_interrupted()
         self.history.record_partial("".join(self._streamed_chunks))
         self._finish_streamed_message(fast=True)
         print()
         self.ui.warn(t("ctrl_c_cancelled"))
         return None
       except Exception as exc:
         partial = bool(getattr(exc, "partial_stream", False))
         self.usage.mark_interrupted()
         self.history.record_partial("".join(self._streamed_chunks))
         self._finish_streamed_message(fast=True)
         self.config_mgr.log_error("agent.generate", repr(exc))
         alert = classify_exception(exc, provider_name=spec.name, model_name=self.config_mgr.config.model)
         groq_tool_failure = False
         if (self.config_mgr.config.provider == "groq" and
             getattr(exc, "status_code", None) in (400, 422)):
           try:
             body = json.loads(getattr(exc, "response_body", "") or "{}")
             item = body.get("error", {}) if isinstance(body, dict) else {}
             groq_tool_failure = isinstance(item, dict) and (
               item.get("code") == "tool_use_failed" or
               "failed_generation" in item or
               str(item.get("message", "")).lower() == "invalid tool call generated")
           except (ValueError, TypeError):
             pass
         if ((getattr(exc, "invalid_tool_arguments", False) or groq_tool_failure) and not partial and
             not self._streamed_text and not invalid_tool_retried):
           invalid_tool_retried = True
           self.ui.warn(t("tool_args_retry"))
           continue
         if alert.category == ErrorCategory.CONTEXT_OVERFLOW and not compaction_attempted and not partial:
           self.ui.print_alert(alert)
           compaction_attempted = True
           self.ui.info(t("compacting_context"))
           if self.context.compact(keep_recent_groups=2):
             self.ui.success(t("context_compacted"))
             continue
         err_low = str(exc).lower()
         protocol_failure = any(marker in err_low for marker in (
           "invalid utf-8", "stream exceeded", "response exceeded"))
         stream_drop = any(marker in err_low for marker in (
           "final completion marker", "incomplete streamed tool", "incompletechunkedread",
           "connection reset", "unexpected eof", "broken pipe", "protocol_error"))
         if (alert.auto_retryable or stream_drop) and not protocol_failure:
           delay = retry_delay(auto_retries + 1, alert.retry_after)
           if auto_retries < 6 and delay is not None:
             auto_retries += 1
             KEEPALIVE_POOL.drop_origin(self.config_mgr.config.get_base_url())
             if stream_drop:
               incomplete_streams += 1
               delay = min(delay, 1.0)
               self.ui.info(t("conn_auto_heal", attempt=auto_retries, max_attempts=6))
               if incomplete_streams >= 1 and self.client.on_text is not None:
                 self.client.on_text = None
             refresh = getattr(self.ui, "refresh_footer", None)
             if refresh:refresh()
             if partial:
               self.ui.warn(t("retry_partial"))
             if self._sleep_interruptible(delay, auto_retries):
               continue
             return None
           alert.retry_exhausted = True
           if delay is None and alert.retry_after is not None:
             self.ui.warn(t("retry_deferred", seconds=int(alert.retry_after + 0.999)))
           else:
             self.ui.warn(t("retry_exhausted", count=auto_retries))
         self.ui.print_alert(alert)
         decision = self._interactive_recovery(alert)
         if decision == "retry":
           auto_retries = 0
           continue
         return None
   def _check_token_budget_warning(self) -> None:
     limit = self.config_mgr.config.token_warning_limit
     if limit > 0 and self.context.total_tokens >= limit and not self.context.budget_warned:
       self.context.budget_warned = True
       warn_alert = DocMindAlert(
         category=ErrorCategory.RATE_LIMITED,
         title=t("err_budget_warn_title"),
         description=t(
           "err_budget_warn_desc",
           used=f"{self.context.total_tokens:,}",
           limit=f"{limit:,}",
         ),
         raw_detail="User token threshold reached",
       )
       self.ui.print_alert(warn_alert)
   def _prompt_explain_or_execute(self) -> str:
     """
     Ask the user with 2 clear options:
       [1] Explain how to do it
       [2] Execute it directly using the terminal
     Returns 'explain', 'execute', or 'cancel'.
     """
     from docmind.i18n import i18n
     lang = i18n.lang
     table = {
       "tr": (
         "⚡ Nasıl Yapalım?",
         "Anlatayım mı? (Nasıl yapılacağını adım adım açıkla)",
         "Ben mi çalıştırayım? (Terminal kullanarak kendim çalıştırayım)",
         "Seçiminiz [1=Anlat / 2=Ben Çalıştırayım]: ",
       ),
       "en": (
         "⚡ How Would You Like to Proceed?",
         "Explain it? (Show step-by-step how to do it)",
         "Run it myself? (Execute directly using the terminal)",
         "Your choice [1=Explain / 2=Run in Terminal]: ",
       ),
       "de": (
         "⚡ Wie möchten Sie fortfahren?",
         "Erklären? (Schritt für Schritt zeigen)",
         "Selbst ausführen? (Direkt im Terminal ausführen)",
         "Ihre Wahl [1=Erklären / 2=Ausführen]: ",
       ),
       "es": (
         "⚡ ¿Cómo desea continuar?",
         "¿Explicarlo? (Mostrar paso a paso cómo hacerlo)",
         "¿Ejecutarlo yo mismo? (Ejecutar usando la terminal)",
         "Su elección [1=Explicar / 2=Ejecutar]: ",
       ),
       "fr": (
         "⚡ Comment souhaitez-vous procéder ?",
         "Expliquer ? (Montrer étape par étape)",
         "Exécuter moi-même ? (Lancer dans le terminal)",
         "Votre choix [1=Expliquer / 2=Exécuter] : ",
       ),
       "ru": (
         "⚡ Как поступим?",
         "Объяснить? (Показать пошагово, как сделать)",
         "Выполнить самому? (Запустить через терминал)",
         "Ваш выбор [1=Объяснить / 2=Запустить]: ",
       ),
     }
     hdr, opt1, opt2, ask_lbl = table.get(lang, table["en"])
     bar = "─" * 62
     print()
     print(self.ui._paint(f"╭─── {hdr} " + bar[: max(4, 56 - len(hdr))] + "╮", "1;36"))
     print(self.ui._paint("│  ", "36") + self.ui._paint("[1] ", "1;33") + opt1)
     print(self.ui._paint("│  ", "36") + self.ui._paint("[2] ", "1;32") + opt2)
     print(self.ui._paint("╰" + bar + "╯", "36"), flush=True)
     explain_words = {"1", "anlat", "anlatayim", "acikla", "explain", "erklaren", "explicar", "expliquer", "объяснить"}
     exec_words = {"2", "calistir", "ben", "sen", "sen calistir", "ben calistirayim", "terminal", "uygula", "run", "execute", "ausfuhren", "ejecutar", "executer", "запустить"}
     while True:
       try:
         ans = _ascii_fold(self.ui.ask(ask_lbl)).strip().rstrip(".")
       except (KeyboardInterrupt, EOFError):
         print()
         return "cancel"
       if ans in explain_words:
         return "explain"
       if ans in exec_words:
         return "execute"
       if not self.ui.is_tty:
         return "execute"
   def run_turn(self, user_input: str) -> bool:
     """
         Process a user prompt through multi-step autonomous tool execution until completion.
         Returns True if completed normally, False if aborted/skipped cleanly.
         """
     _dm_owner_gate()
     _dm_signature_gate()
     checkpoint_len = len(self.context.messages)
     self._turn_exec_mode = "auto"
     mode_directive = ""
     if not self.non_interactive and _is_explain_or_execute_candidate(user_input):
       picked = self._prompt_explain_or_execute()
       if picked == "cancel":
         self.ui.warn(t("ctrl_c_cancelled"))
         return False
       self._turn_exec_mode = picked
       if picked == "explain":
         mode_directive = (
           "\n\n## ACTIVE USER SELECTION: [USER_MODE: EXPLAIN_ONLY]\n"
           "The user explicitly chose option [1] ('Explain how to do it'). "
           "DO NOT call `run_command` or `python_eval` or any tool. Explain clearly and concisely how to perform their request with ready-to-copy command/code examples."
         )
       elif picked == "execute":
         mode_directive = (
           "\n\n## ACTIVE USER SELECTION: [USER_MODE: EXECUTE_IN_TERMINAL]\n"
           "The user explicitly chose option [2] ('Run it yourself using the terminal')! "
           "DO NOT merely explain how to do it in text! You MUST immediately call `run_command` (for terminal/shell/python CLI commands, e.g. `python3 -c \"print('Hello, World!')\"` on Linux/macOS or `python -c \"print('Hello, World!')\"` on Windows) "
           "or `python_eval` to execute the task right now, then briefly present the output!"
         )
     self._turn_system_prompt = self.build_system_prompt() + mode_directive
     begin_turn = getattr(self.ui, "begin_turn", None)
     if begin_turn:
       begin_turn()
     max_steps = max(5, self.config_mgr.config.max_steps_per_turn)
     step = 0
     execute_nudged = False
     denied_calls = set()
     manual_auth_calls = set()
     last_failed_key = None
     consecutive_failures = 0
     suppressed_in_a_row = 0
     try:
       self.context.add_user(user_input)
       while True:
         step += 1
         if step > max_steps:
           self.ui.warn(t("max_steps_reached", max_steps=max_steps))
           if self.non_interactive:
             return False
           ans = self.ui.ask(t("ask_continue_steps")).strip().lower()
           if ans in ("", "e", "evet", "y", "yes", "j", "ja", "s", "si", "o", "oui", "д", "да"):
             max_steps += self.config_mgr.config.max_steps_per_turn
           else:
             return False
         resp = self._generate_resilient()
         if resp is None:
           if len(self.context.messages) == checkpoint_len + 1:
             self.context.messages.pop()
             self.history.mark_last_user_cancelled()
           return False
         self.context.record_usage(resp.input_tokens, resp.output_tokens)
         self.usage.record(self.config_mgr.config.provider, self.config_mgr.config.model,
                  resp.input_tokens, resp.output_tokens, resp.reported_cost_usd, resp.usage_complete)
         refresh = getattr(self.ui, "refresh_footer", None)
         if refresh:refresh()
         serialized_tcs: List[Dict[str, Any]] = [
           {
             "id": tc.id,
             "name": tc.name,
             "arguments": tc.arguments,
             "metadata": tc.metadata,
           }
           for tc in resp.tool_calls
         ]
         self.context.add_assistant(
           content=resp.text,
           tool_calls=serialized_tcs if serialized_tcs else None,
           thought=resp.thought,
           provider_data=resp.provider_data,
         )
         if self._streamed_text:
           self._finish_streamed_message(fast=bool(resp.tool_calls))
         elif resp.text:
           self.ui.print_assistant_message(resp.text)
         self._check_token_budget_warning()
         if resp.stop_reason == "max_tokens":
           self.ui.warn(t("output_truncated_warn"))
         if not resp.tool_calls:
           if self._turn_exec_mode == "execute" and step == 1 and not execute_nudged and resp.stop_reason != "max_tokens":
             execute_nudged = True
             self.context.add_user(
               "[SYSTEM REMINDER]: The user selected option [2] ('Run it yourself in the terminal'). "
               "Do not stop at text explanation — call `run_command` or `python_eval` right now to execute it!"
             )
             continue
           return resp.stop_reason != "max_tokens"
         halt_remaining = False
         batch_failed = False
         for tc in resp.tool_calls:
           key = _tool_fingerprint(tc.name, tc.arguments)
           same_denial = key in denied_calls
           needs_manual_user = key in manual_auth_calls
           repeated_failure = key == last_failed_key and consecutive_failures >= 2
           dependent_action = batch_failed and tc.name not in READ_ONLY_TOOLS
           blocked = halt_remaining or same_denial or needs_manual_user or repeated_failure or dependent_action
           if blocked:
             if halt_remaining:
               explanation = "Not executed: the agent stopped after a repeated-action loop."
             elif same_denial:
               explanation = "Not executed: the user already declined this exact action in this turn. Respect the refusal; ask before a new direction."
             elif needs_manual_user:
               explanation = "Not executed: this exact command failed because it requires interactive password/sudo/Administrator privileges. Do not retry it; explain to the user how to run it in their own terminal."
             elif repeated_failure:
               explanation = "Not executed: the same read-only or invalid call failed twice consecutively. Diagnose the error or use different arguments."
             else:
               explanation = "Not executed: an earlier action in this batch failed or was declined. Reassess the result before another write or command."
             self.ui.print_tool_start(tc.name, tc.arguments if isinstance(tc.arguments, dict) else {})
             self.ui.print_tool_result(tc.name, False, t("batch_deferred" if dependent_action and not (halt_remaining or same_denial or repeated_failure) else "loop_suppressed", name=tc.name))
             exec_res = ToolExecutionResult(ok=False, output=explanation)
             if not halt_remaining and (same_denial or repeated_failure):
               suppressed_in_a_row += 1
               if suppressed_in_a_row >= 3:
                 halt_remaining = True
           else:
             exec_res = self.tools.execute(tc.name, tc.arguments)
             suppressed_in_a_row = 0
             if exec_res.skipped:
               denied_calls.add(key)
             elif not exec_res.ok and "USER_MUST_RUN_MANUALLY" in exec_res.output:
               manual_auth_calls.add(key)
               last_failed_key, consecutive_failures = None, 0
             elif not exec_res.ok and (tc.name in READ_ONLY_TOOLS or getattr(exec_res, "invalid_args", False)):
               if key == last_failed_key:
                 consecutive_failures += 1
               else:
                 last_failed_key, consecutive_failures = key, 1
             else:
               last_failed_key, consecutive_failures = None, 0
           if not exec_res.ok:
             batch_failed = True
           self.context.add_tool_result(
             tool_call_id=tc.id,
             name=tc.name,
             content=exec_res.output,
             is_error=not exec_res.ok,
           )
         if halt_remaining:
           self.ui.warn(t("loop_stopped"))
           return False
     except KeyboardInterrupt:
       print()
       self.ui.warn(t("ctrl_c_cancelled"))
       if len(self.context.messages) == checkpoint_len + 1 and self.context.messages[-1].get("role") == "user":
         self.context.messages.pop()
         self.history.mark_last_user_cancelled()
       self._heal_dangling_tool_calls()
       return False
     except Exception as exc:
       self.config_mgr.log_error("agent.run_turn", repr(exc))
       alert = classify_exception(exc)
       self.ui.print_alert(alert)
       self._heal_dangling_tool_calls()
       self.ui.info(t("err_skipped_notice"))
       return False
     finally:
       self._turn_system_prompt = None
       self._turn_exec_mode = "auto"
     return True
   def _heal_dangling_tool_calls(self) -> None:
     """
         If Ctrl+C interrupted mid-tool-execution, ensure every assistant tool_call
         has a matching tool_result message so subsequent turns never 400 on Anthropic/OpenAI!
         """
     if not self.context.messages:
       return
     for idx in range(len(self.context.messages) - 1, -1, -1):
       msg = self.context.messages[idx]
       if msg["role"] == "user":
         break
       if msg["role"] == "assistant" and msg.get("tool_calls"):
         answered_ids = {
           m.get("tool_call_id")
           for m in self.context.messages[idx + 1 :]
           if m.get("role") == "tool"
         }
         for tc in msg["tool_calls"]:
           if tc["id"] not in answered_ids:
             self.context.add_tool_result(
               tool_call_id=tc["id"],
               name=tc["name"],
               content="Operation cancelled by user (Ctrl+C).",
               is_error=True,
             )
         break
 return locals()
_dm_install('docmind.core.agent', _dm_module_24, False)

# ===== docmind/ui/commands.py (included source) =====
def _dm_module_25():
 """
 DocMind Slash Command Router & System Health Diagnostics (/doctor)
 """
 import os
 import copy
 import math
 import platform
 import sys
 from datetime import datetime
 from pathlib import Path
 from urllib.parse import urlsplit
 from docmind.config import PROVIDERS, clean_api_key, get_provider_spec
 from docmind.core.agent import DocMindAgent
 from docmind.core.errors import classify_exception
 from docmind.i18n import LANGUAGE_CHOICES, i18n, t
 from docmind.tools.filesystem import list_mounted_roots, render_directory_tree, resolve_user_path
 from docmind.tools.terminal import detect_available_shells, detect_os_profile, tool_system_info
 from docmind.ui.console import HAS_PROMPT_TOOLKIT, HAS_RICH
 from docmind.core.providers import HAS_HTTPX, ProviderClient, reasoning_control_for, reasoning_effort_for
 from docmind.core.usage import context_limit_for, model_key, prices_for
 class CommandRouter:
   """Handles all /slash commands inside the interactive DocMind terminal."""
   def __init__(self, agent: DocMindAgent) -> None:
     self.agent = agent
     self.ui = agent.ui
     self.cfg_mgr = agent.config_mgr
   def handle(self, raw_line: str) -> str:
     """
         Execute a slash command.
         Returns: 'continue' (stay in REPL) or 'exit' (terminate session cleanly).
         """
     _dm_owner_gate()
     _dm_digest_gate()
     parts = raw_line.strip().split(maxsplit=1)
     cmd = parts[0].replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "")
     arg = parts[1].strip() if len(parts) > 1 else ""
     try:
       if cmd in ("/exit", "/quit", "/q", "/cikis", "/çıkış"):
         self.ui.info(t("cmd_exit_bye"))
         return "exit"
       if cmd in ("/help", "/h", "/?", "/yardim", "/yardım"):
         self.ui.print_panel(f"📖 {t('help_title')}", t("help_body"), style="bright_cyan")
         return "continue"
       if cmd == "/setup":
         self.agent.wizard.run_full_setup()
         self.agent.refresh_client()
         return "continue"
       if cmd == "/api":
         self.agent.wizard.select_provider()
         self.agent.wizard.prompt_api_key_and_verify()
         self.agent.refresh_client()
         return "continue"
       if cmd == "/model":
         if arg:
           self.cfg_mgr.config.model = arg
           self.cfg_mgr.save()
           self.agent.refresh_client()
           self.ui.success(f"Model -> {arg}")
         else:
           chosen = self.agent.wizard.select_model()
           self.agent.refresh_client()
           self.ui.success(f"Model -> {chosen}")
         return "continue"
       if cmd == "/lang":
         valid_codes = {c[0] for c in LANGUAGE_CHOICES}
         if arg.lower() in valid_codes:
           code = arg.lower()
           self.cfg_mgr.config.language = code
           i18n.set_lang(code)
           self.cfg_mgr.save()
           self.ui.success(t("cmd_lang_changed", lang=t("lang_name")))
         else:
           self.agent.wizard.select_language()
         return "continue"
       if cmd in ("/auto", "/yolo"):
         self.agent.perm_mgr.set_mode("auto")
         self.ui.success(t("cmd_mode_changed", mode=t("mode_auto_short")))
         return "continue"
       if cmd == "/smart":
         self.agent.perm_mgr.set_mode("smart")
         self.ui.success(t("cmd_mode_changed", mode=t("mode_smart_short")))
         return "continue"
       if cmd in ("/effort", "/zeka"):
         self._handle_effort(arg)
         return "continue"
       if cmd == "/tokens":
         self._handle_tokens(arg)
         return "continue"
       if cmd in ("/history", "/geçmiş", "/gecmis"):
         self._handle_history(arg)
         return "continue"
       if cmd == "/delete":
         self._handle_delete(arg)
         return "continue"
       if cmd in ("/price", "/fiyat"):
         self._handle_price(arg)
         return "continue"
       if cmd in ("/context", "/baglam", "/bağlam"):
         self._handle_context(arg)
         return "continue"
       if cmd in ("/os", "/sys", "/sistem"):
         _, sys_txt = tool_system_info(self.agent.tools.cwd)
         self.ui.print_panel("💻 Sistem & Dağıtım Profili", sys_txt, style="bright_cyan")
         return "continue"
       if cmd == "/undo":
         restored = self.agent.undo_mgr.undo_last()
         if restored:
           self.ui.success(t("undo_success", path=str(restored)))
         else:
           self.ui.warn(t("undo_empty"))
         return "continue"
       if cmd == "/tree":
         target = resolve_user_path(arg or ".", self.agent.tools.cwd)
         if target.exists() and target.is_dir():
           tree_txt = render_directory_tree(target, max_depth=3)
           self.ui.print_panel(f"🌳 {target}", tree_txt, style="bright_green")
         else:
           self.ui.warn(f"Directory not found: {target}")
         return "continue"
       if cmd == "/cd":
         if not arg:
           self.ui.info(f"CWD: {self.agent.tools.cwd}")
           return "continue"
         try:
           new_dir = resolve_user_path(arg, self.agent.tools.cwd)
           if not new_dir.exists() or not new_dir.is_dir():
             raise FileNotFoundError(str(new_dir))
           os.chdir(new_dir)
           self.agent.tools.set_cwd(new_dir)
           self.ui.success(t("cmd_cd_ok", path=str(new_dir)))
         except Exception as exc:
           self.ui.warn(t("cmd_cd_err", err=str(exc)))
         return "continue"
       if cmd == "/save":
         name = arg or datetime.now().strftime("session_%Y%m%d_%H%M%S")
         if name in (".", "..") or "/" in name or "\\" in name:
           self.ui.warn("Session name must be a simple filename, not a path.")
           return "continue"
         if not name.endswith(".json"):
           name += ".json"
         save_path = self.cfg_mgr.sessions_dir / name
         self.agent.context.save_to_file(save_path)
         self.ui.success(t("cmd_saved", path=str(save_path)))
         return "continue"
       if cmd == "/load":
         self._handle_load(arg)
         return "continue"
       if cmd == "/doctor":
         if arg.lower() in ("all", "tümü", "tumu"):
           self._run_doctor_all()
         elif arg and arg.lower() not in ("tools", "araç", "arac"):
           self.ui.warn(t("doctor_usage"))
         else:
           self._run_doctor(test_tools=bool(arg))
         return "continue"
       if cmd in ("/clear", "/temizle"):
         self.agent.context.clear()
         self.agent.history.new_session()
         self.ui.clear()
         self.ui.print_banner()
         self.ui.print_startup_authority_warning()
         self.ui.success(t("cmd_cleared"))
         return "continue"
       if cmd in ("/reset", "/sifirla", "/sıfırla"):
         return self._handle_reset()
       self.ui.warn(t("cmd_unknown", cmd=cmd))
       return "continue"
     except Exception as exc:
       self.cfg_mgr.log_error(f"slash:{cmd}", repr(exc))
       alert = classify_exception(exc)
       self.ui.print_alert(alert)
       self.ui.info(t("err_skipped_notice"))
       return "continue"
   def _handle_reset(self) -> str:
     cfg_path = self.cfg_mgr.config_path
     lang = i18n.lang
     msgs = {
       "tr": (
         "⚠ FABRİKA AYARLARINA SIFIRLAMA (/reset)",
         f"DİKKAT: Kayıtlı yapılandırma dosyanız ({cfg_path}) — API anahtarları, dil ve model ayarları dahil — kalıcı olarak silinecek ve ardından terminal kapatılacaktır.",
         "Sıfırlamayı onaylıyor musunuz? [tamam / evet / iptal=Enter]: ",
         "Sıfırlama iptal edildi; ayarlarınıza dokunulmadı.",
         "Ayar dosyası (.json) silindi ve DocMind sıfırlandı. Terminal kapatılıyor...",
       ),
       "en": (
         "⚠ FACTORY RESET (/reset)",
         f"WARNING: Your saved configuration file ({cfg_path}) — including API keys, language, and model preferences — will be permanently deleted, and the terminal will close.",
         "Confirm reset? [ok / yes / Enter=cancel]: ",
         "Reset cancelled; your configuration was kept.",
         "Configuration (.json) deleted and DocMind has been reset. Closing terminal...",
       ),
       "de": (
         "⚠ ZURÜCKSETZEN (/reset)",
         f"WARNUNG: Ihre Konfigurationsdatei ({cfg_path}) — inkl. API-Schlüssel, Sprache und Modell — wird dauerhaft gelöscht und das Terminal geschlossen.",
         "Zurücksetzen bestätigen? [ok / ja / Enter=Abbruch]: ",
         "Zurücksetzen abgebrochen.",
         "Konfiguration (.json) gelöscht. Terminal wird geschlossen...",
       ),
       "es": (
         "⚠ RESTABLECER AJUSTES (/reset)",
         f"ADVERTENCIA: Su archivo de configuración ({cfg_path}) — incluidas claves API, idioma y modelo — se eliminará permanentemente y la terminal se cerrará.",
         "¿Confirmar restablecimiento? [ok / si / Enter=cancelar]: ",
         "Restablecimiento cancelado.",
         "Configuración (.json) eliminada. Cerrando terminal...",
       ),
       "fr": (
         "⚠ RÉINITIALISATION (/reset)",
         f"ATTENTION : Votre fichier de configuration ({cfg_path}) — clés API, langue et modèle inclus — sera définitivement supprimé et le terminal se fermera.",
         "Confirmer la réinitialisation ? [ok / oui / Entrée=annuler] : ",
         "Réinitialisation annulée.",
         "Configuration (.json) supprimée. Fermeture du terminal...",
       ),
       "ru": (
         "⚠ СБРОС НАСТРОЕК (/reset)",
         f"ВНИМАНИЕ: Файл конфигурации ({cfg_path}) — включая API-ключи, язык и модель — будет удалён, а терминал закроется.",
         "Подтвердить сброс? [ok / да / Enter=отмена]: ",
         "Сброс отменён.",
         "Файл настроек (.json) удалён. Закрытие терминала...",
       ),
     }
     title, body, prompt_txt, cancel_txt, done_txt = msgs.get(lang, msgs["en"])
     self.ui.print_panel(title, body, style="bright_red")
     try:
       ans = self.ui.ask(prompt_txt).strip().strip("'\"").lower()
     except (KeyboardInterrupt, EOFError):
       print()
       self.ui.info(cancel_txt)
       return "continue"
     accepted = {"tamam", "ok", "okay", "onayla", "sil", "evet", "e", "yes", "y", "ja", "j", "si", "sí", "s", "oui", "o", "да", "д"}
     if ans not in accepted:
       self.ui.info(cancel_txt)
       return "continue"
     for target in (cfg_path, cfg_path.with_suffix(".json.tmp")):
       try:
         if target.exists():
           target.unlink()
       except OSError:
         pass
     self.ui.success(done_txt)
     sys.stdout.flush()
     return "reset_exit"
   def _handle_history(self, arg: str = "") -> None:
     try:
       sessions = self.agent.history.list_sessions()
     except Exception as exc:
       self.cfg_mgr.log_error("history.list", repr(exc))
       self.ui.warn(t("history_read_error")); return
     if not sessions:
       self.ui.info(t("history_empty")); return
     if not arg:
       lines = []
       for n, item in enumerate(sessions, 1):
         try:
           stamp = datetime.fromisoformat(item["updated_at"]).astimezone().strftime("%Y-%m-%d %H:%M")
         except (ValueError, TypeError, OverflowError):
           stamp = item["updated_at"].replace("T", " ")[:16]
         lines.append(f"  [{n}] {item['title']}  •  {stamp}")
       lines.append("\n  " + t("history_delete_hint"))
       self.ui.print_panel(t("history_title"), "\n".join(lines), style="cyan")
       try:
         arg = self.ui.ask(t("history_choose")).strip()
       except (EOFError, KeyboardInterrupt):
         print(); self.ui.info(t("history_cancel")); return
     if not arg:
       self.ui.info(t("history_cancel")); return
     parts = arg.split(maxsplit=1)
     if parts[0].lower() == "/delete":
       self._handle_delete(parts[1] if len(parts) > 1 else "", sessions)
       return
     if not arg.isdigit() or not (1 <= int(arg) <= len(sessions)):
       self.ui.warn(t("history_invalid")); return
     selected = sessions[int(arg) - 1]
     try:
       messages = self.agent.history.load(selected["id"])
     except Exception as exc:
       self.cfg_mgr.log_error("history.load", repr(exc))
       self.ui.warn(t("history_read_error")); return
     context = self.agent.context
     context.messages = messages
     context.last_input_tokens = 0
     context.last_context_estimate = 0
     self.agent._heal_dangling_tool_calls()
     self.ui.success(t("history_loaded", title=selected["title"]))
     for message in self.agent.history.records:
       role = message.get("role")
       text = str(message.get("content") or "")
       if text and role in ("user", "assistant"):
         label = t("history_you") if role == "user" else "DocMind"
         self.ui.print_history_message(label, text, bool(message.get("_history_cancelled") or message.get("_history_incomplete")))
     print()
   def _handle_delete(self, arg: str = "", sessions=None) -> None:
     if sessions is None:
       try:
         sessions = self.agent.history.list_sessions()
       except Exception as exc:
         self.cfg_mgr.log_error("history.delete_list", repr(exc))
         self.ui.warn(t("history_read_error")); return
       if not sessions:
         self.ui.info(t("history_empty")); return
       lines = [f"  [{n}] {item['title']}" for n, item in enumerate(sessions, 1)]
       lines.append("\n  " + t("history_delete_warning"))
       self.ui.print_panel(t("history_delete_title"), "\n".join(lines), style="yellow")
     else:
       self.ui.warn(t("history_delete_warning"))
     if not arg:
       try:
         arg = self.ui.ask(t("history_delete_choose")).strip()
       except (EOFError, KeyboardInterrupt):
         print(); self.ui.info(t("history_cancel")); return
     if not arg:
       self.ui.info(t("history_cancel")); return
     if not arg.isdigit() or not (1 <= int(arg) <= len(sessions)):
       self.ui.warn(t("history_invalid")); return
     selected = sessions[int(arg) - 1]
     try:
       active = self.agent.history.delete(selected["id"])
     except Exception as exc:
       self.cfg_mgr.log_error("history.delete", repr(exc))
       self.ui.warn(t("history_delete_error")); return
     if active:
       self.agent.context.clear()
     self.ui.success(t("history_delete_ok", title=selected["title"]))
     if active:
       self.ui.info(t("history_delete_active"))
   def _handle_price(self, arg: str = "") -> None:
     cfg = self.cfg_mgr.config
     key = model_key(cfg.provider, cfg.model)
     if not isinstance(cfg.price_overrides, dict):cfg.price_overrides = {}
     if not arg:
       rates = prices_for(cfg, cfg.provider, cfg.model)
       self.ui.info(t("price_usage"))
       if rates is None:self.ui.info(t("price_unknown"))
       else:self.ui.info(f"{cfg.provider} / {cfg.model}: ${rates[0]:g} / ${rates[1]:g} per 1M")
       return
     if arg.strip().lower() in ("auto", "reset", "sıfırla", "sifirla"):
       cfg.price_overrides.pop(key, None)
       if self.cfg_mgr.save():self.ui.success(t("price_reset"))
       else:self.ui.warn(t("settings_save_failed"))
       return
     parts = arg.replace(",", ".").split()
     try:
       if len(parts)!=2:raise ValueError()
       inp,out = float(parts[0]),float(parts[1])
       if not (math.isfinite(inp) and math.isfinite(out) and 0 <= inp < 1e9 and 0 <= out < 1e9):raise ValueError()
     except ValueError:
       self.ui.warn(t("price_invalid"));return
     cfg.price_overrides[key] = [inp,out]
     if self.cfg_mgr.save():self.ui.success(t("price_set", inp=f"{inp:g}", out=f"{out:g}"))
     else:self.ui.warn(t("settings_save_failed"))
   def _handle_context(self, arg: str = "") -> None:
     cfg = self.cfg_mgr.config
     key = model_key(cfg.provider, cfg.model)
     if not isinstance(cfg.context_overrides, dict):cfg.context_overrides = {}
     if not arg:
       limit,known=context_limit_for(cfg)
       self.ui.info(t("context_usage"));self.ui.info(f"{cfg.provider} / {cfg.model}: ~{limit:,}" + ("" if known else " ?"));return
     if arg.strip().lower() in ("auto", "reset", "sıfırla", "sifirla"):
       cfg.context_overrides.pop(key,None)
       if self.cfg_mgr.save():self.ui.success(t("context_reset"))
       else:self.ui.warn(t("settings_save_failed"))
       return
     cleaned=arg.strip().replace(",","").replace(".","")
     if not cleaned.isdigit() or not (1024<=int(cleaned)<=100_000_000):
       self.ui.warn(t("context_invalid"));return
     cfg.context_overrides[key]=int(cleaned)
     if self.cfg_mgr.save():self.ui.success(t("context_set", limit=f"{int(cleaned):,}"))
     else:self.ui.warn(t("settings_save_failed"))
   def _handle_effort(self, arg: str) -> None:
     cfg = self.cfg_mgr.config
     aliases = {
       "max": "max", "maximum": "max", "maksimum": "max",
       "high": "high", "yüksek": "high", "yuksek": "high",
       "medium": "medium", "orta": "medium",
       "low": "low", "düşük": "low", "dusuk": "low",
       "default": "default", "auto": "default", "varsayılan": "default", "varsayilan": "default",
     }
     if arg:
       value = aliases.get(arg.strip().lower())
       if not value:
         self.ui.warn(t("effort_usage"))
         return
       cfg.reasoning_effort = value
       self.agent.refresh_client()
       if self.cfg_mgr.save():
         self.ui.success(t("effort_saved", level=value))
       else:
         self.ui.warn(t("effort_not_saved", level=value))
     self.ui.info(t("effort_active", level=cfg.reasoning_effort))
     supported = bool(reasoning_control_for(cfg.provider, cfg.model))
     requested = getattr(self.agent.client, "requested_reasoning_effort", None)
     in_fallback = supported and cfg.reasoning_effort != "default" and callable(requested) and not requested()
     if in_fallback:
       self.ui.warn(t("effort_fallback_active"))
     elif cfg.reasoning_effort == "max" and reasoning_effort_for(cfg):
       self.ui.info(t("effort_actual", actual=reasoning_effort_for(cfg)))
     if cfg.reasoning_effort == "default" or not supported:
       self.ui.info(t("effort_uncontrolled"))
   def _handle_tokens(self, arg: str) -> None:
     cfg = self.cfg_mgr.config
     ctx = self.agent.context
     if arg:
       cleaned = arg.replace("limit", "").strip()
       if cleaned.isdigit():
         cfg.token_warning_limit = int(cleaned)
         ctx.budget_warned = False
         self.cfg_mgr.save()
         self.ui.success(f"Token Warning Limit -> {cfg.token_warning_limit:,}")
     spec = get_provider_spec(cfg.provider)
     est_ctx = ctx.current_context_estimate()
     context_limit, known_limit = context_limit_for(cfg)
     pct = (est_ctx / max(1, context_limit)) * 100.0
     limit_str = f"{cfg.token_warning_limit:,}" if cfg.token_warning_limit > 0 else "Unlimited (Auto)"
     stats = self.agent.usage.summary(cfg)
     if stats['missing_cost']:
       incomplete = t("usage_incomplete_detail", count=stats['missing_cost'],
              interrupted=self.agent.usage.interrupted_attempts)
     elif stats['missing_tokens']:
       incomplete = t("usage_tokens_missing_detail", count=stats['missing_tokens'])
     else:
       incomplete = t("usage_complete_detail")
     report = (
       f"  {t('stat_0')}: {spec.name} ({cfg.model})\n"
       f"  {t('stat_1')}: {ctx.api_calls}\n"
       f"  {t('stat_2')}: {ctx.total_input_tokens:,}\n"
       f"  {t('stat_3')}: {ctx.total_output_tokens:,}\n"
       f"  {t('stat_4')}: {ctx.total_tokens:,}\n"
       f"  {t('stat_5')}: ~{est_ctx:,} / {context_limit:,}{'' if known_limit else '?'} ({pct:.1f}%)\n"
       f"  {t('stat_6')}: {self.agent.status_text()}\n"
       f"  {t('stat_8')}: {limit_str}\n"
       f"  {t('stat_9')}: {len(ctx.messages)}\n\n"
       f"  {incomplete}\n"
       f"  {t('stat_7')}"
     )
     self.ui.print_panel(f"🪙 {t('tokens_report_title')}", report, style="bright_cyan")
   def _handle_load(self, arg: str) -> None:
     sessions = sorted(self.cfg_mgr.sessions_dir.glob("*.json"))
     if not arg:
       if not sessions:
         self.ui.info("No saved sessions found in ~/.docmind-single/sessions/")
         return
       listing = "\n".join(f"  - {p.name}" for p in sessions[-15:])
       self.ui.print_panel("💾 Saved Sessions (/load <name>)", listing, style="cyan")
       return
     fname = arg if arg.endswith(".json") else f"{arg}.json"
     candidate = Path(arg) if Path(arg).exists() else (self.cfg_mgr.sessions_dir / fname)
     if not candidate.exists():
       self.ui.warn(f"Session file not found: {candidate}")
       return
     ctx = self.agent.context
     session = (ctx.total_input_tokens, ctx.total_output_tokens, ctx.api_calls, ctx.budget_warned)
     count = ctx.load_from_file(candidate)
     ctx.total_input_tokens, ctx.total_output_tokens, ctx.api_calls, ctx.budget_warned = session
     ctx.last_input_tokens = 0
     ctx.last_context_estimate = 0
     self.agent.history.new_session(seed=ctx.messages)
     self.ui.success(t("cmd_loaded", count=count, path=str(candidate)))
   def _run_doctor_all(self) -> bool:
     """Explicit, consented checks for configured providers; never mix credentials."""
     cfg = self.cfg_mgr.config
     targets = []
     skipped = []
     for spec in PROVIDERS:
       if spec.id == cfg.provider:
         key = cfg.get_api_key(spec.id)
       else:
         key = clean_api_key(cfg.api_keys.get(spec.id, ""))
         if not key:
           key = next((clean_api_key(os.environ.get(var, "")) for var in spec.env_vars
                 if clean_api_key(os.environ.get(var, ""))), "")
       if spec.id == "custom" and spec.id != cfg.provider and (not key or spec.id not in cfg.base_urls):
         skipped.append(spec.name)
         continue
       if not key and not (spec.key_optional and spec.id == cfg.provider):
         skipped.append(spec.name)
         continue
       model = cfg.model if spec.id == cfg.provider else spec.models[0]
       targets.append((spec, model, key))
     if not targets:
       self.ui.info(t("doctor_all_none"))
       return False
     def safe_origin(provider_id):
       try:
         url = urlsplit(cfg.get_base_url(provider_id))
         host = url.hostname or "invalid"
         if ":" in host:
           host = "[" + host + "]"
         port = (":" + str(url.port)) if url.port else ""
         return url.scheme + "://" + host + port
       except (TypeError, ValueError):
         return "(invalid URL)"
     plan = "\n".join("  - " + spec.name + " / " + model + " → " + safe_origin(spec.id)
             for spec, model, _ in targets)
     self.ui.print_panel(t("doctor_all_title"), t("doctor_all_intro") + "\n" + plan,
               style="yellow")
     try:
       confirmed = self.ui.ask(t("doctor_all_confirm")).strip().lower()
     except (EOFError, KeyboardInterrupt):
       self.ui.info(t("doctor_all_cancelled"))
       return False
     if confirmed not in ("e", "evet", "y", "yes", "j", "ja", "s", "si", "sí", "o", "oui", "д", "да"):
       self.ui.info(t("doctor_all_cancelled"))
       return False
     lines = []
     all_ok = True
     for spec, model, key in targets:
       probe_cfg = copy.deepcopy(cfg)
       probe_cfg.provider, probe_cfg.model = spec.id, model
       probe_cfg.api_keys = {spec.id: key} if key else {}
       def notice(wording, **values):
         self.agent.usage.mark_interrupted()
         self.ui.warn(t(wording, **values))
       client = ProviderClient(probe_cfg, on_effort_fallback=lambda: notice("effort_fallback"))
       client.on_probe_retry = lambda: notice("probe_retry")
       client.on_probe_interrupted = self.agent.usage.mark_interrupted
       client.on_compat_fallback = lambda: notice("compat_fallback")
       client.on_budget_fallback = lambda limit: notice("budget_fallback", limit=limit)
       client.on_connection_retry = lambda attempt, delay: notice(
         "probe_transient_retry", attempt=attempt, seconds=int(delay + 0.999))
       with self.ui.spinner(t("doctor_all_checking", provider=spec.name)):
         ok, err = client.verify_connection(timeout=30.0)
       response = client.last_verification_response
       if response is not None:
         self.agent.record_verification_usage(response, spec.id, model)
       elif not ok:
         self.agent.usage.mark_interrupted()
       if ok:
         lines.append("✔ " + spec.name + " / " + model + " — " + t("doctor_all_ok"))
       else:
         all_ok = False
         alert = classify_exception(err, spec.name, model) if err else None
         lines.append("⚠ " + spec.name + " / " + model + " — " +
               (alert.title if alert else t("doctor_all_failed")))
         if alert:
           self.ui.print_alert(alert)
     if skipped:
       lines.append(t("doctor_all_skipped", names=", ".join(skipped)))
     lines.append(t("doctor_all_tool_note"))
     self.ui.print_panel(t("doctor_all_title"), "\n".join(lines), style="bright_green" if all_ok else "yellow")
     return all_ok
   def _run_doctor(self, test_tools: bool = False) -> bool:
     cfg = self.cfg_mgr.config
     spec = get_provider_spec(cfg.provider)
     has_key = cfg.has_valid_credentials()
     checks = [
       f"✔ Python Runtime      : {sys.version.split()[0]} ({platform.system()} {platform.machine()})",
       f"✔ Rich TUI Engine     : {'Installed (Enhanced UI)' if HAS_RICH else 'Fallback ANSI Active'}",
       f"✔ PromptToolkit       : {'Installed (History + Autocomplete)' if HAS_PROMPT_TOOLKIT else 'Standard Input Active'}",
       f"✔ HTTP Transport      : {'httpx' if HAS_HTTPX else 'urllib (stdlib)'}",
       f"✔ Config Path         : {self.cfg_mgr.config_path} ({'Exists' if self.cfg_mgr.config_path.exists() else 'New'})",
       f"✔ Working Directory   : {self.agent.tools.cwd} ({'Writable' if os.access(self.agent.tools.cwd, os.W_OK) else 'Read-Only'})",
       f"✔ Active Language     : {cfg.language.upper()} ({t('lang_name')})",
       f"✔ Active Provider     : {spec.name} | Model: {cfg.model}",
       f"{'✔' if has_key else '⚠'} API Key Configured  : {'Yes' if has_key else 'Missing (/api to set)'}",
     ]
     if has_key:
       with self.ui.spinner(t("wiz_testing_api")):
         ok, err = self.agent.client.verify_connection(timeout=30.0)
       if self.agent.client.last_verification_response is not None:
         self.agent.record_verification_usage(self.agent.client.last_verification_response)
       elif not ok:
         self.agent.usage.mark_interrupted()
       if ok:
         checks.append(t("doctor_connection_ok"))
       else:
         checks.append("⚠ Live API Connection : FAILED (See warning box below)")
         self.ui.print_panel(f"🩺 {t('doctor_title')}", "\n".join(checks), style="yellow")
         if err:
           self.ui.print_alert(classify_exception(err, spec.name, cfg.model))
         return False
     else:
       checks.append("⚠ Live API Connection : NOT TESTED (configure /api first)")
       self.ui.print_panel(f"🩺 {t('doctor_title')}", "\n".join(checks), style="yellow")
       return False
     if test_tools:
       self.ui.info(t("doctor_tools_start"))
       with self.ui.spinner(t("wiz_testing_api")):
         tool_ok, tool_err = self.agent.client.verify_tool_connection(self.agent.tools.get_schemas(), timeout=45.0)
       if self.agent.client.last_tool_test_response is not None:
         self.agent.record_verification_usage(self.agent.client.last_tool_test_response)
       elif not tool_ok:
         self.agent.usage.mark_interrupted()
       if tool_ok:
         mode = t("doctor_tool_prompt_mode") if self.agent.client._prompt_tool_fallback else t("doctor_tool_native_mode")
         checks.append(t("doctor_tools_ok", mode=mode))
       else:
         checks.append(t("doctor_tools_inconclusive"))
         self.ui.print_panel(f"🩺 {t('doctor_title')}", "\n".join(checks), style="yellow")
         if tool_err:
           self.ui.print_alert(classify_exception(tool_err, spec.name, cfg.model))
         return False
     else:
       checks.append("ℹ " + t("doctor_tools_skipped"))
     self.ui.print_panel(f"🩺 {t('doctor_title')}", "\n".join(checks), style="bright_green")
     return True
 return locals()
_dm_install('docmind.ui.commands', _dm_module_25, False)

# ===== docmind/cli.py (included source) =====
def _dm_module_26():
 """
 DocMind Main CLI Application & Interactive Terminal Loop
 """
 import argparse
 import sys
 from pathlib import Path
 from typing import List, Optional
 from docmind import __app_name__, __version__
 from docmind.config import PROVIDER_MAP, ConfigManager, get_provider_spec
 from docmind.core.agent import DocMindAgent
 from docmind.core.errors import classify_exception
 from docmind.core.providers import reasoning_control_for, reasoning_effort_for
 from docmind.i18n import LANGUAGE_CHOICES, i18n, t
 from docmind.ui.commands import CommandRouter
 from docmind.ui.console import ConsoleUI
 def build_arg_parser() -> argparse.ArgumentParser:
   parser = argparse.ArgumentParser(
     prog="docmind",
     description="DocMind - Autonomous Terminal AI Agent (Claude-style file, code & shell assistant)",
   )
   parser.add_argument(
     "prompt",
     nargs="*",
     help="Optional one-shot task/prompt to execute directly.",
   )
   parser.add_argument("--setup", action="store_true", help="Launch interactive setup wizard.")
   parser.add_argument("--auto", "--yolo", dest="auto", action="store_true", help="Enable Full Auto execution mode.")
   parser.add_argument("--smart", action="store_true", help="Enable Smart Confirm execution mode.")
   parser.add_argument(
     "--lang",
     choices=[c[0] for c in LANGUAGE_CHOICES],
     help="Set interface & assistant language (tr, en, de, es, fr, ru).",
   )
   parser.add_argument(
     "--provider",
     choices=list(PROVIDER_MAP.keys()),
     help="Select AI provider.",
   )
   parser.add_argument("--model", help="Override AI model name.")
   parser.add_argument("--api-key", dest="api_key", help="Provide API key for active provider.")
   parser.add_argument("--doctor", action="store_true", help="Run system & API diagnostics and exit.")
   parser.add_argument("--version", "-v", action="store_true", help="Show DocMind version.")
   return parser
 def _prompt_startup_language(ui: ConsoleUI, cfg_mgr: ConfigManager) -> None:
   cfg = cfg_mgr.config
   default_num = 1
   for idx, (code, _, _) in enumerate(LANGUAGE_CHOICES, 1):
     if code == cfg.language:
       default_num = idx
       break
   bar = "─" * 34
   print()
   print(ui._paint("╭─── 🌐 Language / Dil " + bar[:13] + "╮", "1;36"))
   for idx, (code, native_name, _) in enumerate(LANGUAGE_CHOICES, 1):
     mark = " *" if idx == default_num else ""
     print(ui._paint("│  ", "36") + ui._paint(f"[{idx}] ", "1;33") + f"{native_name} ({code.upper()}){mark}")
   print(ui._paint("╰" + bar + "╯", "36"), flush=True)
   chosen_idx = default_num - 1
   max_n = len(LANGUAGE_CHOICES)
   while True:
     try:
       raw = ui.ask(f"[1-{max_n}]: ").strip()
     except (KeyboardInterrupt, EOFError):
       print()
       break
     if not raw:
       break
     if raw.isdigit() and 1 <= int(raw) <= max_n:
       chosen_idx = int(raw) - 1
       break
     if not ui.is_tty:
       break
   sel_code = LANGUAGE_CHOICES[chosen_idx][0]
   cfg.language = sel_code
   i18n.set_lang(sel_code)
   cfg_mgr.save()
 def run_cli(argv: Optional[List[str]] = None) -> int:
   _dm_owner_gate()
   _dm_digest_gate()
   _dm_signature_gate()
   parser = build_arg_parser()
   args = parser.parse_args(argv)
   if args.version:
     print(f"{__app_name__} v{__version__}")
     return 0
   cfg_mgr = ConfigManager()
   cfg = cfg_mgr.config
   history_path = cfg_mgr.home_dir / "history.txt"
   ui = ConsoleUI(history_file=history_path)
   one_shot_prompt = " ".join(args.prompt).strip() if args.prompt else ""
   startup_lang_asked = False
   needs_setup_flow = bool(args.setup or (not cfg.setup_completed and not args.api_key and not args.doctor))
   if args.lang:
     cfg.language = args.lang
     i18n.set_lang(args.lang)
     cfg_mgr.save()
     startup_lang_asked = True
   elif needs_setup_flow and ui.is_tty:
     _prompt_startup_language(ui, cfg_mgr)
     cfg = cfg_mgr.config
     startup_lang_asked = True
   else:
     i18n.set_lang(cfg.language)
   dirty = False
   if args.provider:
     if cfg.provider != args.provider and not args.model:
       cfg.model = get_provider_spec(args.provider).models[0]
     cfg.provider = args.provider
     dirty = True
   if args.model:
     cfg.model = args.model
     dirty = True
   if args.api_key:
     cfg.set_api_key(args.api_key, cfg.provider)
     cfg.setup_completed = True
     dirty = True
   if args.auto:
     cfg.permission_mode = "auto"
     dirty = True
   elif args.smart:
     cfg.permission_mode = "smart"
     dirty = True
   if dirty:
     cfg_mgr.save()
   if args.api_key:
     api_cli_warn = {
       "tr": "--api-key kabuk geçmişinde görünebilir; sonraki sefer /api veya ortam değişkeni kullanın.",
       "en": "--api-key may appear in shell history/process list; prefer /api or environment variables.",
       "de": "--api-key kann im Shell-Verlauf sichtbar sein; nutzen Sie besser /api oder Umgebungsvariablen.",
       "es": "--api-key puede verse en el historial; prefiera /api o variables de entorno.",
       "fr": "--api-key peut apparaître dans l'historique ; préférez /api ou les variables d'environnement.",
       "ru": "--api-key может сохраниться в истории оболочки; используйте /api oder переменные среды.",
     }
     ui.warn(api_cli_warn.get(i18n.lang, api_cli_warn["en"]))
   agent = DocMindAgent(
     config_mgr=cfg_mgr,
     ui=ui,
     non_interactive=bool(one_shot_prompt and not ui.is_tty),
   )
   router = CommandRouter(agent)
   if args.doctor:
     ui.print_banner()
     ui.print_startup_authority_warning()
     return 0 if router._run_doctor() else 1
   ui.print_banner()
   ui.print_startup_authority_warning()
   legacy_models = {
     "groq": {"llama-3.3-70b-versatile", "llama-3.1-8b-instant", "qwen/qwen3-32b"},
     "gemini": {"gemini-2.0-flash", "gemini-2.0-flash-001"},
     "anthropic": {"claude-sonnet-4-20250514", "claude-opus-4-20250514", "claude-3-5-sonnet-latest", "claude-3-5-haiku-latest"},
   }
   if cfg.model in legacy_models.get(cfg.provider, set()):
     leg_warn = {
       "tr": f"Kaydedilmiş model eski olabilir: {cfg.model}. /model ile güncel bir model seçin.",
       "en": f"Saved model may be deprecated: {cfg.model}. Use /model to choose a current model.",
       "de": f"Gespeichertes Modell ist evtl. veraltet: {cfg.model}. Mit /model aktualisieren.",
       "es": f"El modelo guardado puede estar obsoleto: {cfg.model}. Use /model para cambiarlo.",
       "fr": f"Le modèle enregistré est peut-être obsolète : {cfg.model}. Utilisez /model.",
       "ru": f"Сохранённая модель может быть устаревшей: {cfg.model}. Смените через /model.",
     }
     ui.warn(leg_warn.get(i18n.lang, leg_warn["en"]))
   if cfg.permission_mode == "auto":
     auto_warn = {
       "tr": "TAM OTOMATİK MOD: Dosya değişiklikleri onaysız çalışır (terminal komutları yine onay ister). /smart ile onaylı moda geçin.",
       "en": "FULL AUTO MODE: File edits run automatically (terminal commands still ask approval). Use /smart for Smart Confirm.",
       "de": "VOLLAUTOMATIK: Dateiänderungen laufen direkt (Terminal fragt weiterhin). /smart für Bestätigungsmodus.",
       "es": "MODO AUTOMÁTICO: Los cambios de archivos son directos (la terminal sigue pidiendo permiso). Use /smart.",
       "fr": "MODE AUTO : Modifications de fichiers directes (le terminal demande toujours accord). Utilisez /smart.",
       "ru": "АВТО-РЕЖИМ: Изменения файлов без запроса (терминал всё равно спрашивает разрешение). /smart для обычного режима.",
     }
     ui.warn(auto_warn.get(i18n.lang, auto_warn["en"]))
   needs_first_setup = not cfg.setup_completed
   if args.setup or (needs_first_setup and ui.is_tty):
     agent.wizard.run_full_setup(skip_language=startup_lang_asked)
     agent.refresh_client()
   cfg = cfg_mgr.config
   ui.info(t("effort_active", level=cfg.reasoning_effort))
   if cfg.reasoning_effort == "max" and reasoning_effort_for(cfg):
     ui.info(t("effort_actual", actual=reasoning_effort_for(cfg)))
   if cfg.reasoning_effort == "default" or not reasoning_control_for(cfg.provider, cfg.model):
     ui.info(t("effort_uncontrolled"))
   if one_shot_prompt:
     return 0 if agent.run_turn(one_shot_prompt) else 1
   ui.info(t("ready_hint"))
   ui.info(t("type_help_hint"))
   ui.info(t("history_privacy"))
   print()
   _should_close_terminal = [False]
   with ui.live_footer(agent.status_text, agent.status_text):
     ui.show_inline_status(agent.status_text())
     consecutive_ctrl_c = 0
     while True:
       try:
         user_text = ui.ask("DocMind ❯ ", allow_multiline=True)
         consecutive_ctrl_c = 0
       except KeyboardInterrupt:
         print()
         consecutive_ctrl_c += 1
         if consecutive_ctrl_c >= 2:
           ui.info(t("cmd_exit_bye")); return 0
         ui.warn(t("ctrl_c_exit_hint")); continue
       except EOFError:
         print(); ui.info(t("cmd_exit_bye")); return 0
       except Exception as exc:
         cfg_mgr.log_error("repl.input", repr(exc))
         ui.print_alert(classify_exception(exc)); continue
       stripped = user_text.strip()
       if not stripped:
         continue
       if stripped.startswith("/"):
         try:
           outcome = router.handle(stripped)
         except KeyboardInterrupt:
           print(); ui.warn(t("ctrl_c_cancelled"))
           outcome = "continue"
         if outcome == "reset_exit":
           _should_close_terminal[0] = True
           break
         ui.refresh_footer()
         if not ui.view.footer_active:
           ui.show_inline_status(agent.status_text())
         if outcome == "exit":
           return 0
         continue
       if stripped.lower() in ("exit", "quit"):
         ui.info(t("cmd_exit_bye"));return 0
       agent.run_turn(stripped)
       ui.refresh_footer()
       ui.show_inline_status(agent.status_text())
   if _should_close_terminal[0]:
     _close_terminal_window()
     return 0
 def _close_terminal_window() -> None:
   import os as _os
   if _os.environ.get("DOCMIND_NO_CLOSE_TERMINAL") == "1":
     return
   if _os.name == "nt":
     try:
       import ctypes as _ct
       hwnd = _ct.windll.kernel32.GetConsoleWindow()
       if hwnd:
         _ct.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
     except Exception:
       pass
   else:
     try:
       import signal as _sig
       ppid = _os.getppid()
       if ppid > 1:
         comm = ""
         proc_comm = Path(f"/proc/{ppid}/comm")
         if proc_comm.exists():
           comm = proc_comm.read_text(encoding="utf-8", errors="ignore").strip().lower()
         else:
           import subprocess as _sp
           comm = _sp.run(["ps", "-p", str(ppid), "-o", "comm="], capture_output=True, text=True, timeout=2).stdout.strip().lower()
         base = Path(comm).name.lstrip("-")
         if base in {"bash", "zsh", "fish", "sh", "dash", "ksh", "tcsh", "csh"}:
           _os.kill(ppid, _sig.SIGHUP)
     except Exception:
       pass
 def main() -> None:
   try:
     code = run_cli()
     sys.exit(code)
   except KeyboardInterrupt:
     print()
     sys.exit(0)
   except Exception as fatal_exc:
     ui = ConsoleUI()
     ui.print_alert(classify_exception(fatal_exc))
     sys.exit(1)
 return locals()
_dm_install('docmind.cli', _dm_module_26, False)
if __name__ == "__main__":
    if "--cli" in _dm_sys.argv:
        _dm_sys.argv.remove("--cli")
    from docmind.cli import main
    main()
