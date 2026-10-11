# 08 — Digital banking access, customer authentication and technical troubleshooting (researcher 08)

Date context: 2026-10-10; all pages accessed 2026-10-10 unless stated. Tags used on statements: **[T1]** law/regulation · **[T2]** common industry practice · **[T3]** individual bank/institution policy (named) · **[T4]** recommended service practice · **[T5]** assumption needing verification. Jurisdiction labels: **TR**, **EU**, **UK**, **US**. "Anecdotal" = forum/complaint-site material used only for customer wording. Legal detail belongs to researchers 02 (TR) and 03 (EU/UK/US); card ops to 06, payments to 07, fraud to 10, communication to 11.

## 1. Turkish authentication models, device binding, credential blocks and recovery flows

### Takeaway
Turkish digital-banking authentication is set by BDDK's 2020 e-banking regulation (BSEBY). The core rules: two independent factors are required for everything, even viewing data. Banks may not send SMS OTPs to customers who have activated the mobile app, except at setup, re-activation, or when the app is unusable. A SIM change or number port is detected through integration with Turkish mobile operators, and the SIM-based factor is then disabled for 90 days unless the change is confirmed. Phone-banking agents may not see customer data before two-factor authentication (2FA), and may never hear PINs or OTPs. Banks implement this with app-bound devices ("cihaz eşleştirme/tanımlama"), push approvals (names differ by bank), and self-service recovery by card + PIN, NFC chip-ID, video call, ATM or branch.

### Terminology and customer phrasings (TR → EN)
- *şifre / parola* = password (Garanti uses "parola"; QNB "Dijital Şifre"); *şifre bloke / parola bloke oldu* = password locked; *şifremi unuttum / parola al* = forgot password / get password; *geçici şifre* = temporary password; *tek kullanımlık şifre (OTP)*, *SMS şifre*, *Cep Şifre* (Akbank), *Akıllı SMS* (Yapı Kredi), *Mobil Onay Kodu* (İş Bankası) = one-time code; *Mobil Onay / Ziraat Onay / anlık mesaj / bildirimle onay* = push approval; *Dijital onay mesajı* (İş Bankası: approvals sent from branch to app); *cihaz eşleştirme / cihaz eşleşmesi (tokenizasyon) / cihaz tanımlama / Telefon Tanıma / güvenli cihaz* = device binding; *SIM blokesi / SMS Güvenlik Kontrol Listesi / Mobil Onay Kodu blokesi* = SIM-change block on SMS OTP; *numara taşıma* = number porting; *çipli kimlik / yeni tip T.C. kimlik kartı* = chip ID card; *NFC ile okutma* = NFC chip read; *görüntülü görüşme* = video call; *uzaktan kimlik tespiti* = remote ID verification; *kayıtlı cep telefonu* = registered mobile number; *ekran paylaşımı tespit edildi* = screen sharing detected; *planlı kesinti / bakım çalışması* = planned outage/maintenance.
- Realistic customer phrasings (anecdotal, Şikayetvar 2025–2026): "Mobil onay kodu telefonuma hiçbir şekilde ulaşmıyor"; "Telefon değişikliği yaptığım için… mobil onay kodu alamıyorum"; "Numaramı değiştirmedim, yalnızca operatörümü değiştirdim"; "SMS kodu gelmiyor"; "uygulama… beyaz ekranda kalıyor"; "'Bu uygulama telefonunuzda çalışmaz' hatası"; "'ekran paylaşımı tespit edildi' hatası alıyorum"; "yeni cihazımdan giriş yapamıyorum… kod eski telefona gidiyor" — [Şikayetvar İş Bankası](https://www.sikayetvar.com/is-bankasi/mobil-onay-gelmiyor), [Şikayetvar SIM](https://www.sikayetvar.com/kod-gelmiyor/sim-kart-degisikligi), [Şikayetvar DenizBank](https://www.sikayetvar.com/denizbank/ekran-paylasimi), [Şikayetvar Yapı Kredi](https://www.sikayetvar.com/yapi-kredi-bankasi/yapi-kredi-mobil-uygulama-beyaz-ekran-sorunu). Typical short forms an agent should recognise: "SMS gelmiyor", "şifre gelmiyor", "uygulama açılmıyor", "yeni telefona geçtim giriş yapamıyorum", "şifrem bloke oldu", "cihaz tanımlayamıyorum", "NFC okumuyor", "bildirim gelmiyor", "3D şifresi gelmiyor" [T4 list compiled from the above].

### Cited Findings
**Regulation (TR) — BDDK "Bankaların Bilgi Sistemleri ve Elektronik Bankacılık Hizmetleri Hakkında Yönetmelik" (BSEBY), Official Gazette (RG) 15.03.2020 No. 31069.** An amendment (RG 20.06.2020) brought Art. 13, 29, 34(13), 34(15), 37(8), 40 and 42 into force on 01.07.2020 and **all other provisions on 01.01.2021**.
- [TR·T1] Art. 34(1): e-banking needs ≥2 independent factors from different classes (knowledge/possession/biometric), "including transactions with no financial consequence such as viewing customer information". The possession factor must be customer-specific and impossible to copy. Art. 34(2): a chip ID card + PIN/biometric, or an e-signature, satisfies this — [BSEBY RG 15.03.2020](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm); [amendment RG 20.06.2020](https://www.resmigazete.gov.tr/eskiler/2020/06/20200620-1.htm).
- [TR·T1] Art. 34(6): the customer is told about failed attempts at their next login. After a set number of failures extra measures apply, and continued failures block access. **No number is fixed**, so thresholds are bank-specific — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 34(7): a bank "may in no way" send SMS OTPs or verification codes to customers who have **installed and activated** the mobile app, whether for login or for in-session verification. SMS is allowed only at **first installation, activation, re-activation, or when the app is unusable** — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm). BDDK Circular 2023/1 (approved by Board Decision 23.03.2023 No. 10546) adds that SMS must stay exceptional, "not a routine practice". Its reasons: other apps on the same device may read or forward the SMS, and the SMS app is not under the bank's control. It also says the app PIN must be verified online at the bank, not locally — [BDDK Genelge 2023/1](https://www.bddk.org.tr/Mevzuat/DokumanGetir/1171).
- [TR·T1] Art. 34(8): before sending an SMS OTP, the bank must identify customers who changed their SIM card or ported their number, through integration with Turkish mobile operators. Unless the change is confirmed, the SIM-based factor cannot be used **for 90 days from the change**. The bank bears the burden of proof for anything done without 2FA during confirmation — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 34(9): OTPs must be random, long enough, unique and time-limited. Art. 34(10): data printed on ID documents and the mother's maiden name may **never** be used for e-banking authentication. Art. 34(11): the first remote binding of an authenticator needs 2FA. The card PIN may act as the "knowledge" factor only for channel activation, the first password, and a remote password reset done under 2FA. Art. 34(12): customers get access restrictions, daily limits and safe-payee lists, and changing them needs 2FA. Art. 34(14): customers must be able to verify the source of the app. Art. 34(15): controls against compromised devices and "broken or modified" operating systems — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 11(4) (identity and access management; per Art. 3, "user" includes bank customers): block access after a set number of failures; never reveal whether the username or the password was wrong; end or lock idle sessions; refuse, with a warning, a second simultaneous session for the same user unless the information-security officer has approved it. Art. 38(5): errors must not reveal which factor failed — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 38(1): browsers and apps may not remember or auto-send the knowledge factor, and it is verified online. Art. 38(2): after the first factor, and before the session opens, the customer sees a **pre-set welcome message or image** (anti-phishing). Art. 38(3): codes for financial transactions are bound to the amount and payee. Art. 39(1): an app PIN or biometric that unlocks a customer-specific key, verified online, counts as 2FA. Art. 39(2): "a password, PIN or biometric data controlled by the device manufacturer rather than the app" cannot serve as the knowledge or biometric factor. Art. 39(3): one factor plus the bound device is enough for viewing data and for paying safe payees, but full 2FA is needed at the first session and once **90+ days** have passed since the last 2FA session — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 40 (phone banking, in force 01.07.2020) has four rules. (1) Until 2FA, the agent must not be able to see customer data or the customer menu. For lost/stolen/fraud reports the agent may see need-to-know data without authentication. (2) Changes to authentication or **phone information** requested by phone are made through **automated systems without agent involvement or access**. (3) Knowledge factors and OTPs/transaction codes are entered **through automated systems, without agent involvement or access**. (4) Before calling a registered number, the bank checks it is not forwarded — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Art. 37 covers customer information. (2)(ç): planned maintenance expected to interrupt e-banking for **more than 2 hours** must be announced in advance. (3): call-centre menus must put fraud reporting in the main menu, among the first options. (5): internet/mobile banking cannot be opened without the customer's request, and a channel the customer closed reopens only on a new request. (7): if the device or platform cannot show required information, the customer must be pointed to other channels — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T1] Law 7571 (RG 25.12.2025 No. 33118, in force on publication), Art. 30, amends Electronic Communications Law Art. 50. Operators may not register mobile subscriptions with ID documents that lack electronic verification capability, and must confirm identity with the ID plus face/fingerprint biometrics or a verifying password. Art. 33 amends Payment Services Law 6493 Art. 12(3) to allow customer identification "by biometric methods or e-ID-capable identity documents" — [Law 7571](https://www.resmigazete.gov.tr/eskiler/2025/12/20251225-33.htm).
- [TR·T1, government analog] e-Devlet has its own "SIM blokesi" after a SIM change. It can be removed by recovery e-mail, by logging in with mobile signature/e-signature/chip ID, by NFC ID verification, at PTT branches or Türksat offices, or at Nüfusmatik kiosks — [turkiye.gov.tr](https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=355).

**Bank implementations [T3]**
- **Garanti BBVA.** Password: 6 digits, numeric, not guessable (birth date, TCKN, phone), different from the last 3. Obtained with the registered phone + credit card/Paracard PIN, or with the new chip ID over NFC ("Yeni Kimlik Bilgileri ile Parola Al"), by video call if the phone has no NFC, at a branch, or on 444 0 333. Repeated wrong tries can block it; unblock via 444 0 333 or "Parola Yenile/Al" — [Garanti şifre](https://www.garantibbva.com.tr/dijital-bankacilik/nasil-sifre-alinir). Device binding is "cihaz eşleşmesi (tokenizasyon)", managed in *Profil ve Ayarlar > Güvenlik Adımları ve Gizlilik > Güvenlik Ayarları*. Customers are told to **remove the binding before letting anyone else use the device, "even if you keep your SIM"** — [Garanti cihaz](https://www.garantibbva.com.tr/dijital-bankacilik/cihaz-eslesmesi). A SIM block follows an operator change, 4.5G upgrade, porting or number change. It is removed via the app (*Bize Ulaşın > SIM Kart Değişikliği*), by video call (needs a paired device + active password), through the IVR (needs a paired device + card PIN), at an ATM (card + PIN), or at a branch — [Garanti SIM](https://www.garantibbva.com.tr/dijital-bankacilik/sim-kart-degisikligi). The mobile number is updated **only at ATMs and branches**, not in internet banking — [Garanti SSS](https://www.garantibbva.com.tr/sikca-sorulan-sorular/dijital-bankacilik).
- **İş Bankası.** "Telefon Tanıma" (device recognition) allows up to 3 devices per customer, with an optional "only this device" lock. Install and activate it on a new phone. If the phone is lost, call 0850 724 0 724 to cancel. The "Mobil Onay Kodu" (OTP) arrives as SMS, as a SIM-toolkit message (not stored, deleted after OK), or as an in-app "Anlık Mesaj". Internet-branch login can be approved from the İşCep notification ("Onayla") — [İş Bankası güvenlik](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
- **Akbank.** A "güvenli cihaz" (secure device) is verified over **mobile data with Wi-Fi switched off**, or through a "Müşteri İletişim Merkezi beni arasın" callback. Many transactions require it. Akbank İnternet uses a notification to the verified device. Per Akbank, under legislation effective "1 January" SMS "Cep Şifre" can no longer be used for digital-channel transactions — [Akbank güvenli cihaz](https://www.akbank.com/dijital-bankacilik/akilli-cozumler/guvenli-cihaz-tanimlama).
- **Ziraat.** "Ziraat Onay" is the push approval and needs an internet connection plus notification permission. **Uninstalling Ziraat Mobil breaks the link**, and another device needs re-activation. SMS OTPs are valid **3 minutes**. The phone number can be updated, or the SIM block removed, **in the app without logging in** (*Diğer İşlemler > Telefon/SIM Kart İşlemleri*) or at a branch. Customers can restrict access by IP/ISP/domestic/foreign location and by time. Foreign-IP access can be closed; it is opened via a login-screen link, *Profil ve Ayarlar > Erişim Tanımlama*, or the contact centre. The second login screen shows the customer's name (anti-phishing). Real-time transactions cannot be cancelled online — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
- **Yapı Kredi.** After a SIM change "Akıllı SMS" is blocked. Until the block is removed, the customer cannot use internet/mobile login and approvals, 3-D Secure shopping, SMS card-PIN setting, or merchant shopping loans. Removal is instant via the internet branch (automatic redirect after login), the Mobil/World Mobil apps, ATMs or the call centre — [Yapı Kredi SIM](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/sim-kart-degisikligi-yardim).
- **Halkbank.** A SIM change or port puts the customer on the "SMS Güvenlik Kontrol Listesi". Removal options: the app's pre-login *Diğer İşlemler > SIM/SMS bloke kaldır*; ATM menus (debit card "Bana Özel", credit card "Paraf İşlemleri"); Halkbank Dialog 0850 222 0 400 (with Mobil Onay + card PIN or Dijital Parola); or a branch — [Halkbank SIM](https://www.halkbank.com.tr/tr/dijital-bankacilik/guvenlik/sizin-icin-sunduklarimiz/sim-kart-degisikligi).
- **DenizBank.** Since 01.01.2021, active MobilDeniz/DenizKartım users log in to internet banking through a **push to the app**. Customers without the app get SMS OTPs. Paired devices are managed in the app's *Profil ve Ayarlar* menu — [DenizBank güvenlik](https://www.denizbank.com/dijital-bankacilik/guvenlik/mobildeniz-guvenlik-ayarlari).
- **QNB.** The "Dijital Şifre" is obtained in the app. The customer enters card number, 2 of the 3 CVV digits, card PIN and phone number, then a 4-digit SMS code, then answers an IVR callback (press 1). A **5-day temporary password** arrives by SMS. At first login there is another callback, an SMS code, and a new 6-digit password. Holders of the new chip ID without a card can use a video call. Check minimum OS versions in the store listing — [QNB giriş](https://www.qnb.com.tr/724-bankacilik/qnb-mobile-internet-subesine-nasil-giris-yapabilirim/qnb-mobile-nasil-giris-yapabilirim).
- **Enpara (digital-only).** A security code is requested again after: reinstalling, deactivating and reactivating the channel, logging in on another device (and again when returning to the usual one), or another user logging in on the customer's device. If the phone is lost, stolen or in repair, the customer can call to close the mobile channel. A SIM change blocks SMS for internet banking, but **active app users continue**; first-time app users remove the block via "Unuttum". A number change is done in the app or via "Cep telefonu numaram değişti" — [Enpara SSS](https://www.enpara.com/sss).
- **Papara (e-money, comparison; snippet-level only).** Account verification requires NFC ("not possible with non-NFC devices") — [Papara FAQ](https://www.papara.com/faq/hesap-islemleri/hesabimi-nasil-onaylayabilirim). New-device login codes are reported to go to the registered e-mail (anecdotal) — [Şikayetvar Papara](https://www.sikayetvar.com/papara/giris/onay-kodu).

**Night-time extra verification (2025–2026).** Sources disagree on its scope.
- [TR·T3 Garanti BBVA] From 22:00 to 06:00, extra NFC verification applies to: loan, overdraft and cash-advance applications and limit changes; card and virtual-card limit increases; card-to-card FX transfers; and "phone/mail-order and internet shopping". Customers without NFC use "alternative identity methods for the channel". The check cannot be switched off. At ATMs it is completed through prompts sent to the registered phone — [Garanti İşlem Kısıtları](https://www.garantibbva.com.tr/dijital-bankacilik/islem-kisitlari).
- [TR·press] Habertürk (12.11.2025), citing sources: BDDK sent an *instruction* to banks requiring "double verification" for cash advances at night, and "there is no ID-verification requirement as such" — [Habertürk](https://www.haberturk.com/kredi-kartlarina-gece-kisitlamasi-mi-getirildi-iste-yaniti-3837235-ekonomi).
- [TR·press] Yeni Şafak (27.03.2026) instead describes NFC chip-ID checks for IBAN transfers of 20,000 TL or more between 22:00 and 06:00, with a video-call alternative — [Yeni Şafak](https://www.yenisafak.com/galeri/ekonomi/ibanla-para-transferi-islemlerine-yeni-zorunluluk-mu-geliyor-iste-bddk-kararinin-perde-arkasi-4809615).
- The underlying BDDK instruction is not public. The official bank page is the most authoritative source for that bank.

### Inferences
- [T4] The registered mobile number is a security anchor. By law (Art. 40(2)), a phone agent cannot change it by hand. That is why banks route number changes to ATM (card + PIN), branch, NFC/video in-app flows, or automated IVR.
- [T5] Akbank's "1 January" most likely means 01.01.2021, when Art. 34(7) took effect under the June 2020 amendment.
- [T4] "Şifre bloke" (credential lock), "SIM/SMS blokesi" (OTP channel suspended after a SIM change), "cihaz eşleşmesi yok" (unbound device) and account-level freezes are four **different** states with different fixes. An account freeze (e.g., the 48-hour fraud suspension power introduced by Law 7571) belongs to fraud/legal teams (researchers 05/10), not to digital support.

### Gaps
- No public numeric lockout thresholds (e.g., 3 vs 5 wrong passwords) were found on the pages reviewed; bank-specific.
- Whether BSEBY was amended after 2021 (beyond Circular 2023/1) was not verified on a consolidated text; researcher 02 to confirm.
- BTK secondary rules on how SIM *replacement* (as distinct from new subscriptions) is identity-checked after Law 7571 were not found. The operator side of the SIM-change feed (which events count, including eSIM transfers) is not public.
- Push-approval names for Akbank, Yapı Kredi, VakıfBank, QNB and ING internet-banking logins were not confirmed on official pages (ING not researched).

## 2. OTP/SMS delivery failures — causes, checks, alternatives, fraud signal

### Takeaway
In Türkiye most "SMS gelmiyor" contacts trace to three things: (a) a SIM/operator/number change that triggers the bank's SIM block; (b) the code being delivered *in the app*, because SMS is legally off for activated app users; (c) phone-level filtering or signal problems. Bank-side delays or rate limits are a smaller share. Agents must never ask for the code. An unrequested code is a fraud signal, not a technical fault.

### Cited Findings
- [TR·T3 İş Bankası] Codes may be blocked after a SIM or operator change. On iPhone, the customer should check *Ayarlar > Mesajlar > Engellenenler* for the bank's numeric sender (printed as +90472265274); on Android, *Mesajlar > Ayarlar > Spam*. If a phone is defined in İşCep, codes may arrive as in-app notifications (bell icon > *Mesajlar*). Old phones can be removed via *Güvenlik ve Ayarlar > Tanımlı Telefon Yönetimi*. Delivery falls back from in-app message to SIM message to SMS. The NFC unblock is available only for Türk Telekom, Turkcell and Vodafone subscribers; customers on foreign operators are excluded — [İş Bankası](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
- [TR·T3 Ziraat] SMS codes are valid 3 minutes and fail when the phone is off or out of coverage. "If you got a code or info SMS without doing a transaction, call 0850 220 00 00" — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
- [TR·T3 Vodafone TR, search snippet] "If you recently changed operator, number or SIM card, your bank needs a security update" — [Vodafone yardım](https://www.vodafone.com.tr/yardim/ayarlar/sms-mesajlasma/bankalardan-kisa-mesaj-sms-alamiyorum-ne-yapmaliyim) (page body did not render; snippet only).
- [TR·T3 Garanti/Yapı Kredi/Halkbank] SIM-block triggers include 4.5G SIM upgrades and porting even when the **number is unchanged** — [Garanti SIM](https://www.garantibbva.com.tr/dijital-bankacilik/sim-kart-degisikligi), [Yapı Kredi SIM](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/sim-kart-degisikligi-yardim), [Halkbank SIM](https://www.halkbank.com.tr/tr/dijital-bankacilik/guvenlik/sizin-icin-sunduklarimiz/sim-kart-degisikligi).
- [US·standard] NIST SP 800-63B-4 (final, July 2025): OTP over the phone network (PSTN) is the only "restricted" authenticator. Verifiers "SHOULD consider risk indicators (e.g., device swap, SIM change, number porting…)" before using it, and must offer at least one non-restricted alternative — [NIST 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html); [CSRC](https://csrc.nist.gov/pubs/sp/800/63/b/4/final).
- [US·T1-guidance] FFIEC (Aug 2021): one-time codes sent to customers can be intercepted. Institutions should have processes for "changes to established phone numbers or carriers" — [FFIEC via FDIC FIL-55-2021](https://www.fdic.gov/news/financial-institution-letters/2021/fil21055a.pdf).
- [anecdotal] Complaints describe several patterns. Operator change with the same number still triggers the block. The IVR asks for the very code that is not arriving. Repeated phone resets or reinstalls cause "mobil bloke" and trips to the ATM. Masterpass codes fail after a SIM change. Some customers report the block "although I never changed my SIM" — [Şikayetvar İş Bankası](https://www.sikayetvar.com/is-bankasi/mobil-onay-gelmiyor), [Şikayetvar SIM](https://www.sikayetvar.com/kod-gelmiyor/sim-kart-degisikligi). A forum claims a full message inbox or phone storage stops SMS — [Technopat](https://www.technopat.net/sosyal/konu/telefona-3d-secure-onay-kodu-gelmiyor.1994864/) (unverified).

### Inferences
- [T4] Before running phone checks, establish **which code** is involved (login, transaction, 3DS purchase, password reset, card PIN, Masterpass) and whether the app is activated on this phone. Because of Art. 34(7), an "SMS not arriving" complaint from an app user is often a misunderstanding: the approval is waiting in the app.
- [T5] SIM change also covers eSIM conversion or transfer and operator-initiated SIM replacement. That may explain "I never changed my SIM". Verify against the operator feed.
- [T5] Dual-SIM phones (registered number on the inactive line or the data-only SIM), roaming off, Do-Not-Disturb, and operator-level SMS barring are plausible causes. No official Turkish source was found for them.
- [T4] Do not encourage repeated "resend": bank rate limits (unpublished) and the 3-minute validity window can create a loop. A broken IVR path ("enter the code to reach an agent") must offer an OTP-free route to a human for OTP-failure cases.

### Gaps
- Bank-side OTP resend limits and cooldowns are not published.
- Whether operator "reklam/SMS engelleme" services affect OTPs (as opposed to marketing reminders, which Ziraat says need the line opened to promotional SMS) is unconfirmed.

## 3. App, browser and connectivity problems; collecting safe diagnostics

### Takeaway
Most app failures fall into five groups:
- unsupported OS or app version;
- integrity checks (root/jailbreak, beta OS, emulator, remote access);
- network path (VPN or foreign IP, captive Wi-Fi, mobile data needed for operator-based device checks);
- lost binding after a reinstall or reset;
- genuine app or server faults.

On the web, failures come from customer-set access restrictions, outdated browsers, blocked pop-ups, deliberately blocked autofill, and the anti-phishing welcome screen. Agents diagnose using error text, time, device/OS/app version and channel — never credentials or unredacted screenshots.

### Cited Findings
- [TR·T3 QNB] App compatibility follows the store listing (*App Store > Uyumluluk*; *Play Store > Gerekli İşletim Sistemi*). Official stores include Huawei AppGallery — [QNB](https://www.qnb.com.tr/724-bankacilik/qnb-mobile-internet-subesine-nasil-giris-yapabilirim/qnb-mobile-nasil-giris-yapabilirim).
- [anecdotal] An İşCep user on a Huawei P20 Lite got an "Android 9 ve üstü" message. A Samsung J7 user who **deleted the app to update it** then got "Bu uygulama telefonunuzda çalışmaz" and no OTP. Others report login failing after a Xiaomi OS update while working on another phone, white screens during password retrieval, and endless "update" prompts — [Şikayetvar İş Bankası](https://www.sikayetvar.com/is-bankasi/mobil-onay-gelmiyor), [Şikayetvar Xiaomi](https://www.sikayetvar.com/xiaomi/guncelleme-sonrasi-banka-uygulamasina-giris-sorunu), [Şikayetvar Yapı Kredi](https://www.sikayetvar.com/yapi-kredi-bankasi/beyaz-ekran-hatasi-ile-mobil-sifre-alamiyorum-musteri-destegi-yok).
- [TR·T3 Vakıf Katılım, 12.11.2025] Banking apps run root/jailbreak checks at launch and may block, restrict or warn. Rooting can also break secure connections — [Vakıf Katılım](https://www.vakifkatilim.com.tr/tr/hakkimizda/medya-merkezi/blog/detay/jailbreak-ve-rootlama-nedir-cihaz-guvenliginizi-nasil-tehlikeye-atar). [Global·standard] OWASP MASVS-RESILIENCE-1: "The app validates the integrity of the platform" (root/jailbreak, emulator, attestation) — [OWASP MASVS](https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/). [TR·T1] BSEBY Art. 34(15) requires such controls.
- [T3 Expatrio help centre] Its listed causes of a "device security issue" include rooting/jailbreak, VPN/proxy, and beta OS — [Expatrio](https://help.expatrio.com/tr/article/kb-16912353688860) (snippet). [anecdotal] An iOS 26 beta triggered DenizBank's screen-sharing block — [Şikayetvar DenizBank](https://www.sikayetvar.com/denizbank/ekran-paylasimi).
- [TR·T3 Akbank] Device verification runs over 3G/4G with Wi-Fi temporarily off — [Akbank](https://www.akbank.com/dijital-bankacilik/akilli-cozumler/guvenli-cihaz-tanimlama).
- [TR·T3 Ziraat/Garanti] Login can fail because of the customer's own settings: foreign-IP access left closed (Ziraat shows a "Yurtdışı IP… erişimine kapalı" message with an opening link), and IP restrictions or usage-period windows at Garanti. Garanti also notes that a certificate error such as "…bilinmeyen bir yetkili tarafından imzalanmış bir sertifika…" can mean an outdated browser that needs updating — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi), [Garanti SSS](https://www.garantibbva.com.tr/sikca-sorulan-sorular/dijital-bankacilik).
- [Global·T3 Google] Pop-ups can be allowed for a single site in Chrome — [Chrome Help](https://support.google.com/chrome/answer/95472?hl=TR&co=GENIE.Platform%3DDesktop) (snippet).
- [TR·T1] Sessions are terminated or locked after inactivity, and a second concurrent session for the same user is refused with a warning (BSEBY Art. 11(4); no duration is fixed). [EU·T1] Commission Delegated Regulation (EU) 2018/389, Art. 4(3)(d): at most **5 minutes** of inactivity after login — [RTS 2018/389](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389). [US] FFIEC: application time-outs and re-authentication — [FFIEC](https://www.fdic.gov/news/financial-institution-letters/2021/fil21055a.pdf).
- [TR·T3 Ziraat/Enpara] Reinstalling breaks Ziraat Onay. Enpara asks for a security code again after a reinstall — [Ziraat](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi), [Enpara](https://www.enpara.com/sss).

### Inferences
- [T4] Never advise uninstall/reinstall as a first step. A reinstall triggers re-activation, which per Art. 34(7) may need an SMS OTP. If the line is SIM-blocked, or the OS is no longer supported, the customer can lose app access entirely. Check four prerequisites first: OS supported, registered number receiving SMS, no SIM block, and card + PIN or chip ID available.
- [T5] A VPN whose exit node is abroad may look like foreign-IP access and hit foreign-IP blocks.
- [T5] A wrong device clock causes TLS/certificate errors. This is general knowledge, not confirmed by a bank source.
- [T4] Safe diagnostic bundle: channel (app/web), exact error text or code, date/time, device model, OS and app version, network type (Wi-Fi/mobile/VPN/abroad), recent changes (new phone, OS update, SIM/operator change, reinstall), and whether others or other channels are affected. Never collect passwords, PINs, OTPs, CVV, full card numbers, or screenshots showing codes, balances or the URL bar of a suspicious site. If a screenshot is truly needed, use the bank's secure in-app upload, cropped to the error.

### Gaps
- No Turkish bank publishes a supported-browser matrix or a consolidated minimum OS list on the pages reviewed. Store listings change often, so treat them as a periodic check item.

## 4. Biometrics, device changes and screen-sharing / remote-access detection

### Takeaway
Biometric login is a local unlock of a bank key bound to the device. Adding or removing fingerprints or faces, or changing the screen lock, can invalidate it, so the fix is to log in with the password and re-enable biometrics. A new phone always means a new device binding, often with a code or verification step, and the old device should be unbound. Many banks block the app while screen sharing or remote-access tools are active, and Android now warns in that situation. Agents must never ask customers to install remote-access tools or to disable these protections.

### Cited Findings
- [TR·T1] BSEBY Art. 39(1)–(2): a biometric that unlocks a customer-specific key, verified online, counts as 2FA. Device-maker-controlled biometrics cannot themselves be the biometric factor — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [Global·T3 Google, page updated 2026-08-03] On Android, biometric-only keys are by default "irreversibly invalidated when a new biometric is enrolled, or when all existing biometrics are deleted". They are also invalidated when the secure lock screen is disabled or forcibly reset — [Android KeyGenParameterSpec](https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder).
- [US·standard] NIST: "Biometrics SHALL only be used as part of multi-factor authentication with a physical authenticator" — [NIST 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html).
- [TR·T3] Device-change rules by bank:
  - İş Bankası: up to 3 recognised devices; activate on the new phone; cancel lost devices by phone — [İş Bankası](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
  - Ziraat: Ziraat Onay must be re-activated on another device — [Ziraat](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
  - Enpara: a code is required on new or reinstalled devices — [Enpara](https://www.enpara.com/sss).
  - Garanti: unpair before giving the device to anyone — [Garanti](https://www.garantibbva.com.tr/dijital-bankacilik/cihaz-eslesmesi).
  - Akbank: device definitions are removed via the call centre — [Akbank](https://www.akbank.com/dijital-bankacilik/akilli-cozumler/guvenli-cihaz-tanimlama).
- [anecdotal] "I can't log in from my new device; I can't remove the old device definition; the code goes to the old phone" — [Şikayetvar İş Bankası](https://www.sikayetvar.com/is-bankasi/mobil-onay-gelmiyor).
- [anecdotal, DenizBank wording] "Cihazınızdaki başka bir uygulama tarafından ekran paylaşıldığı tespit edilmiştir" and "ekran paylaşımı engellendi" — [Şikayetvar DenizBank](https://www.sikayetvar.com/denizbank/ekran-paylasimi). MobilDeniz also ends the session when "Uzaktan Erişime izin veren uygulama tespit edildi" — [Samsung Community](https://r2.community.samsung.com/t5/Samsung-Members/Denizbank-uygulamas%C4%B1nda-a%C5%9Fa%C4%9F%C4%B1daki-uyar%C4%B1-veriyor-ve-kapat%C4%B1yor/td-p/15400220) (anecdotal).
- [Global·T3 Google, 03.12.2025] Android's in-call protection works as follows. If a user opens a participating financial app while screen sharing **and** on a call with an unsaved number, Android warns, offers to end the call and the sharing, and imposes a **30-second pause**. The UK pilot (2025) was expanded to "most major UK banks", with pilots in Brazil and India — [Google blog](https://blog.google/security/android-expands-pilot-in-call-scam-protection-financial-apps/).
- [TR·T3 Odeabank] "Cihazınıza kimseye uzaktan erişim izni vermeyin" (snippet) — [Odeabank](https://www.odeabank.com.tr/guvenlik/zararli-yazilim-riskine-karsi-guvenlik-onlemleri). [US·T3 Wells Fargo] "Don't give remote access to your devices" (snippet) — [Wells Fargo](https://www.wellsfargo.com/privacy-security/fraud/bank-scams/bank-imposter/). [TR·T3 DenizBank] "No bank official, police, soldier, prosecutor or lawyer will ask for your internet, mobile or card passwords" — [DenizBank](https://www.denizbank.com/dijital-bankacilik/guvenlik/mobildeniz-guvenlik-ayarlari).

### Inferences
- [T4] When biometrics fail after a phone or enrolment change, the safe steps are: log in with the password or PIN, then turn biometrics off and on in the app's security settings. If the app reports a security or binding problem, re-bind through the official flow. Never tell the customer to remove the screen lock or install tools.
- [T4] A screen-sharing or remote-access warning during a live call with a "bank", "police" or "courier" caller is a **fraud trigger**: stop troubleshooting and hand over to fraud (researcher 10). With no caller involved, ask the customer to stop any screen recording, casting or remote-support app *they themselves* installed, then reopen the app. Beta OS builds may produce false positives.

### Gaps
- No official Turkish bank help page confirming screen-sharing or remote-access detection was found; evidence comes from customer-quoted messages. Apple iOS equivalents of Android's in-call protection were not researched.

## 5. Digital onboarding, NFC/video steps, unclear loading states and duplicate submissions

### Takeaway
Remote onboarding in Türkiye is regulated:
- a real-time, uninterrupted video call;
- an NFC chip read of the ID;
- a liveness check;
- a face match against the chip photo;
- checks for coercion.

So most "failed upload / incomplete onboarding" contacts are about NFC reads, lighting or camera, dropped calls, or old-type IDs. For anything involving money, a spinner or timeout means "check status before retrying". Never resubmit blindly.

### Cited Findings
- [TR·T1] BDDK remote-ID regulation (RG 01.04.2021 No. 31441) requires the following:
  - a video call that is real-time, uninterrupted and end-to-end secure (Art. 6(5));
  - an ID showing security features under white light, with photo and signature (Art. 7(1));
  - verification of the chip data by NFC (Art. 7(2)). If NFC fails, at least four visual security features must be checked, **and** the first funds must come from the customer's own account at another bank (Art. 7(3));
  - tilting the ID on camera as instructed (Art. 7(4));
  - liveness detection and deepfake safeguards, plus a biometric face match against the chip photo, or the printed photo if the chip is unreadable (Art. 8(1)–(2));
  - the representative assessing social-engineering or coercion risk (Art. 8(4)).

  Source: [BDDK uzaktan kimlik tespiti](https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm).
- [TR·T3 Garanti] Customers need the new chip ID and a **brightly lit environment**. The NFC read takes data from the chip, a selfie checks liveness, and a representative confirms on video. Old-type IDs are handled by courier visit — [Garanti SSS](https://www.garantibbva.com.tr/sikca-sorulan-sorular/dijital-bankacilik).
- [TR·T1-gov] e-Devlet tips for chip-ID NFC failures: enter the ID details correctly; keep the card and phone still; the antenna position varies by model, so try the middle and upper back; if the chip seems faulty, apply to NVİ (civil registry) — [turkiye.gov.tr](https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=337). [TR·T3 Ziraat] The chip-ID PIN locks after 3 wrong entries, and a new PIN comes from the civil registry office — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
- [TR·T1-equality body] TİHEK decision 2024/115 (08.02.2024) concerned a blind applicant who could not onboard remotely at VakıfBank. TİHEK found discrimination over physical accessibility and fined BDDK and the bank 141,934 TL each. On the digital side it found no violation but issued recommendations, noting the bank was developing voice guidance and that BDDK had allowed third-party assistance — [TİHEK](https://www.tihek.gov.tr/public/images/kararlar/432khm.pdf).
- [TR·T3 Ziraat] Online transactions are real-time and cannot be cancelled online. For an EFT that left the account but did not arrive, obtain the EFT query number — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
- [Global·standards] EMVCo (04.02.2026): in out-of-band (OOB) flows, failures often show up as timeouts, or as the merchant not knowing the challenge succeeded — [EMVCo](https://www.emvco.com/knowledge-hub/emv-3-d-secure-how-merchants-and-issuers-can-enhance-browser-based-out-of-band-authentication/).

### Inferences
- [T4] For NFC failures, have the customer:
  1. remove any thick or metal case;
  2. turn NFC on;
  3. hold the card flat against the upper or middle back without moving;
  4. close other NFC or payment apps;
  5. retry in good light for the selfie.

  If it still fails, offer the bank's alternative (video call, branch, courier) rather than repeated attempts.
- [T4] Duplicate-submission rule: "Check transaction history or status first; if pending, wait; if failed with no debit, retry once; if debited without confirmation, open a payment trace (researcher 07); never re-send on an unknown state."

### Gaps
- Whether the remote-ID regulation was amended after 2021 (TİHEK refers to BDDK changes allowing third-party help) is unverified; researcher 02 to confirm the date and text.

## 6. Push notifications, digital wallets and 3-D Secure

### Takeaway
Push approvals fail mainly on device-side permissions, focus or battery modes, network, and a binding lost after reinstall. Banks offer an in-app "pending approvals" fallback. Apple Pay is not available for Turkish-issued cards (Apple list, Sept 2026), so "wallet" problems in Türkiye usually concern bank-app contactless or wearable payments and Masterpass. 3-D Secure failures cluster around:
- SIM blocks;
- outdated phone numbers;
- cards not enabled, or over the limit, for internet use;
- OOB timeouts;
- the night-time extra verification.

### Cited Findings
- [TR·T3 Ziraat] If no Ziraat Onay notification arrives, check the internet connection and the app's notification permission in *Ayarlar > Uygulamalar* — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi). [TR·T3 İş Bankası] Anlık Mesaj needs the current app version, notifications on, and one login after enablement — [İş Bankası](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
- [Global·T3 Apple] Per-app notifications can be muted for one hour or one day, turned off, delayed by Focus, or bundled into Scheduled Summary. Check *Settings > Notifications* — [Apple 108781](https://support.apple.com/en-us/108781). [Global·T3 Google, updated 2026-08-18] Doze and App Standby defer network access. Apps should use FCM high-priority messages for time-critical notifications — [Android Doze](https://developer.android.com/training/monitoring-device-state/doze-standby).
- [TR·T3 Akbank/Axess] 3-D Secure is approved in the Juzdan app. "Check that Juzdan notification permissions are on before the transaction. If the notification doesn't arrive, approve from *Onay Bekleyen Ödemeler > 3D Secure – Mobil Onaylar*" — [Axess](https://www.axess.com.tr/axess/sayfa/1/7358/3d-secure-juzdan-onay). [TR·T3 Garanti] BonusFlaş users can choose app approval on the 3D screen (snippet) — [Garanti blog](https://www.garantibbva.com.tr/blog/3d-secure-nedir). [TR·T3 İş Bankası] Internet-shopping passwords (TROY GO) can arrive as in-app messages — [İş Bankası](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
- [TR·T3] Card-level limits also cause 3-D Secure failures. Yapı Kredi blocks 3D Secure purchases during a SIM block — [Yapı Kredi SIM](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/sim-kart-degisikligi-yardim). Enpara applies a monthly internet-shopping limit that declines purchases even with funds available — [Enpara SSS](https://www.enpara.com/sss). Garanti lists internet and mail/phone-order shopping under 22:00–06:00 NFC extra verification — [Garanti](https://www.garantibbva.com.tr/dijital-bankacilik/islem-kisitlari). [anecdotal] "gece alışveriş için nfc okutma zorunluluğu" — [Ekşi Sözlük](https://eksisozluk.com/gece-alisveris-icin-nfc-okutma-zorunlulugu--8044737).
- [Global·standards] EMV 3DS exchanges transaction, payment-method and device data so the issuer can authenticate "without adding unnecessary friction" — [EMVCo 3DS](https://www.emvco.com/emv-technologies/3-d-secure/). How the browser-based OOB flow works (EMVCo, 04.02.2026):
  - an iframe appears at checkout;
  - the customer switches to the bank app, then returns and taps "Complete";
  - same-device mobile-browser flows cause timeouts;
  - EMVCo advises countdown timers and telling customers to open the app manually if no push arrives.

  Source: [EMVCo OOB](https://www.emvco.com/knowledge-hub/emv-3-d-secure-how-merchants-and-issuers-can-enhance-browser-based-out-of-band-authentication/).
- [Global·T3 Apple, published 30.09.2026] Apple's list of Apple Pay countries and regions does **not** include Türkiye under Europe or the Middle East — [Apple 102775](https://support.apple.com/en-us/102775). [TR·T3 Akbank] Contactless payment on Samsung watches works from Akbank Mobil: Galaxy Watch4 or later on WearOS, Android 8+, NFC, with Akbank chosen in the watch's NFC payment settings — [Akbank](https://www.akbank.com/dijital-bankacilik/akilli-cozumler/samsung-temassiz-odeme). [anecdotal] Masterpass SMS codes fail after a SIM change — [Şikayetvar SIM](https://www.sikayetvar.com/kod-gelmiyor/sim-kart-degisikligi).

### Inferences
- [T4] Push not received: first open the bank app and look for pending approvals; that resolves many cases without any device changes. Then check notification permission, Focus/DND, battery-saver or "restricted" app status, a connection that is on but captive, and the time window. Then check whether the binding is intact.
- [T4] Customers should not repeat a 3-D Secure attempt more than once or twice. Merchant-side errors (iframe or pop-up blocked, session expired) need a fresh checkout, while issuer-side declines need card support (researcher 06). A 3D code for a purchase the customer did not make goes to fraud.

### Gaps
- Google Wallet and Samsung Wallet availability for Turkish bank cards in 2026 could not be confirmed from official sources. Samsung's "S Wallet" in Türkiye (prepaid Moka card) was seen only in secondary search summaries.

## 7. Scheduled maintenance and outages

### Takeaway
Turkish banks must pre-announce planned maintenance over two hours, and in practice post overnight windows (02:00–05:30) on "Planlı Kesintiler" pages. Agents should confirm any incident from the internal incident channel, give only confirmed facts, offer alternative channels, and never declare "fixed" without confirmation.

### Cited Findings
- [TR·T1] BSEBY Art. 37(2)(ç): advance announcements are required for planned maintenance expected to cause a **>2-hour** e-banking interruption — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).
- [TR·T3 DenizBank] Examples: on 12.06.2026, website work from 02:00 to 04:00 with banking available via MobilDeniz, internet banking and ATMs; on 09.06.2024, internet and mobile banking down from 02:30 to 05:30 — [DenizBank planlı kesintiler](https://www.denizbank.com/dijital-bankacilik/planli-kesintiler) (snippet). [TR·T3 Halkbank] "Between 2:00 and 04:00 ATMs, internet branch and Halkbank Mobil will be unavailable; Halkbank Dialog only for lost/stolen…" — [Halkbank planlı kesintiler](https://www.halkbank.com.tr/tr/dijital-bankacilik/planli-kesintiler) (snippet).
- [UK·T1] FCA BCOBS 7.6.1R: firms publish the number of major operational or security incidents reported to the FCA — [FCA BCOBS 7](https://handbook.fca.org.uk/handbook/bcobs7) (snippet).

### Inferences
- [T4] An agent should treat a problem as bank-wide only if the incident tool or status channel confirms it, or if correlated reports cross a threshold set by IT. Until then, say "we're checking whether there is a wider issue".
- [T4] Customer wording: "Şu anda [kanal]'da yaşanan bir erişim sorununu ekiplerimiz inceliyor; [alternatif kanal] üzerinden işlem yapabilirsiniz. Kesin bir süre veremiyorum; düzeldiğinde [kanal] üzerinden duyurulacak." Never give an ETA that is not published, and never blame the customer's device during a confirmed incident.

### Gaps
- No Turkish bank public real-time status page was found; communication appears to rely on web pages, app banners and social media (not verified per bank).

## 8. Accessibility and usability

### Takeaway
Türkiye already requires accessible internet and mobile banking, screen-reader-compatible SMS OTPs, a password route outside the call centre, a text or video-interpreter channel for hearing-impaired customers, and disability-adapted call-centre authentication. In the EU, the EAA has applied to banking since 28 June 2025, and the EU payment-services package (provisional deal Nov 2025) adds SCA options that do not depend on a smartphone, plus access to human support.

### Cited Findings
- [TR·T1] BDDK "Bankacılık Hizmetlerinin Erişilebilirliğine Dair Yönetmelik" (in force 01.01.2017; existing systems to comply by 01.01.2018):
  - Art. 11(1): internet and mobile banking must meet accessibility standards.
  - Art. 11(2): SMS OTPs must be screen-reader compatible.
  - Art. 12(1): password retrieval and change must also be offered outside the call centre.
  - Art. 12(2): hearing-impaired customers get a secure online text channel or a video sign-language interpreter, including for lost/stolen card reports.
  - Art. 12(3): call-centre authentication is adapted to the disability, with longer keypad-entry time for visually impaired customers.
  - Art. 9: amount SMS after online card payments for visually impaired customers who have told the bank.
  - Contracts, PINs and passwords are available on request in Braille, audio or sign-language video.

  Source: [Erişilebilirlik Yönetmeliği](https://www.aile.gov.tr/eyhgm/mevzuat/ulusal-mevzuat/yonetmelikler/bankacilik-hizmetlerinin-erisilebilirligine-dair-yonetmelik/).
- [EU·T1] The EAA "came into force on June 28, 2025" for banking services. "Identification methods, electronic signatures, security, and payment services" must be "perceivable, operable, understandable and robust", and information may not exceed CEFR level **B2** — [AFM (NL regulator)](https://www.afm.nl/en/sector/themas/dienstverlening-aan-consumenten/toegankelijkheid).
- [EU·T1-pending] A provisional PSR/PSD3 agreement was reached on 27.11.2025. Payment users "must have access to human customer support (not only chatbots)" — [William Fry, 28.11.2025](https://www.williamfry.com/knowledge/psr-psd3-eu-payment-services-legislation-is-agreed/). Every customer must have at least one SCA method "that does not depend on the use of a smartphone" — [EY, 26.09.2025](https://www.ey.com/en_be/technical/financial-services/financial-services-alerts/payment-services-regulation-key-impacts-on-payment-service-providers) (pre-agreement description; final text to verify).

### Inferences
- [T4] Offer accommodations proactively:
  - an extended OTP window or resend;
  - push approval instead of SMS for screen-reader users, or SMS if the app is hard to use;
  - VoiceOver/TalkBack and larger-text guidance;
  - branch, ATM voice-menu or video-interpreter routes;
  - a trusted helper only through the bank's sanctioned process, never by sharing credentials.

  Customers with low digital literacy should get step-by-step guidance and a non-digital alternative.

### Gaps
- The Official Gazette date of the 2017 accessibility regulation was not captured, and the final PSR text and application dates as of Oct 2026 were not verified (researcher 03).

## 9. Safe-troubleshooting rules (never-do list) and official channels

### Takeaway
The safety rules are legal requirements in Türkiye, not just good practice. PINs and OTPs must be entered into automated systems, not given to an agent. Authentication and phone-number changes requested by phone must be handled by automated systems. Customer data stays hidden until 2FA, except for fraud reports. Safety rules override every troubleshooting step.

### Cited Findings
- [TR·T1] BSEBY Art. 40(1)–(4) (see §1) — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm). [US·T1-guidance] FFIEC: threat actors "deceive customer call center… representatives into resetting passwords". Recommended controls: enhanced authentication for resets (OTP to a pre-established device, authenticator app, voice biometrics, secure video chat, call-back to a pre-established number), staff training, and detecting unusual contact methods — [FFIEC](https://www.fdic.gov/news/financial-institution-letters/2021/fil21055a.pdf).
- [TR·T3] Banks tell customers never to share codes:
  - Ziraat: never share codes "including with Bank personnel"; ignore callers asking you to read or key in codes — [Ziraat SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi).
  - QNB: "banka personeli dahil kimseyle paylaşmayın" — [QNB](https://www.qnb.com.tr/724-bankacilik/qnb-mobile-internet-subesine-nasil-giris-yapabilirim/qnb-mobile-nasil-giris-yapabilirim).
  - İş Bankası: don't share codes by "reading the message on the phone" — [İş Bankası](https://www.isbank.com.tr/guvenlik-uygulamalarimiz).
  - Yapı Kredi: ignore anyone requesting information outside its official channels — [Yapı Kredi SIM](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/sim-kart-degisikligi-yardim).
- [UK·T2] Take Five: "We will never text or call you and ask you to share your information or transfer money" — [Take Five](https://www.takefive-stopfraud.org.uk/) (snippet).

### Inferences
- [T4] Never:
  - ask for or accept PINs, passwords, OTPs, CVV, full card numbers or ID-card PINs;
  - have the customer read a code aloud, even when "only for verification";
  - ask the customer to install anything except the official app from App Store, Google Play or AppGallery via the bank's own website link;
  - ask for remote access or screen sharing (AnyDesk, TeamViewer, QuickSupport…);
  - ask the customer to root a phone, disable security or Play Protect, turn off the screen lock, or bypass detection;
  - request screenshots containing codes or credentials;
  - change a registered number or binding outside the bank's automated or strong-verification flow;
  - promise an outcome, an ETA or a refund.

  Direct customers to type the bank URL themselves and confirm their personal welcome image or name on the second login screen.
- [T5] Whether an AI voice or chat agent counts as "görevli" (staff) under Art. 40(3) is a legal question for researcher 02. The conservative design: the AI never receives secrets and routes all secret entry to DTMF/IVR or in-app flows.

### Gaps
- No official UK NCSC page on remote-access scams was fetched (snippet sources only).

## 10. Layered diagnostic methodology, decision trees and issue classification

### Takeaway
Run checks in increasing order of risk:
1. safety screen;
2. scope;
3. customer-side basics;
4. credential and account status (authenticated only);
5. device, OS and app;
6. transaction status;
7. structured escalation.

Classify each case as customer-side, device, authentication, transaction-processing or bank-wide before acting.

### Cited Findings
- [US·T1-guidance] Layered security combines preventive, detective and corrective controls — [FFIEC](https://www.fdic.gov/news/financial-institution-letters/2021/fil21055a.pdf). [TR·T1] Agents may see customer data only after 2FA, except for fraud reports (Art. 40(1)) — [BSEBY](https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm).

### Inferences
**Layers [T4]**
- **L1 Safety/fraud screen (no authentication needed).** Ask whether someone is guiding them on the phone or screen-sharing, whether they received codes or new-device alerts they did not request, whether they shared any code, and whether money is moving. Any yes → fraud handover (Art. 40(1) allows need-to-know access).
- **L2 Scope.** Establish which channel (app/web/IVR/ATM), which device, since when, the exact error text, whether other devices or channels work, and whether the incident board shows a problem.
- **L3 Customer-side basics.** Network, mobile data vs Wi-Fi, VPN, roaming, clock, storage, app or browser update, notification permission, blocked sender — reversible steps only.
- **L4 Credential and account status (requires 2FA; tool permission).** Credential locked, SIM-block flag, device bindings, customer-set access restrictions, channel closed by the customer, account freeze. The agent may *read* status. Resets stay in self-service, automated or branch flows.
- **L5 Device/OS/app.** Supported OS, integrity warnings, reinstall prerequisites, biometric re-enrolment.
- **L6 Transaction status.** Look up the status of any money movement before advising a retry (payments team).
- **L7 Escalation.** Send the diagnostic bundle (§3) to Digital Channels/IT support. Go to the Incident/NOC team when several customers or channels are affected. Fraud/Security handles social engineering, unexpected codes or remote access. Card Ops handles 3DS and wallets. Payments Ops handles debited-not-credited cases. Onboarding/KYC Ops handles the remote-ID flow. Accessibility or complaints routes handle access barriers.

**Classification signals [T4]**
- **Customer-side:** one channel on one network fails; it works on mobile data or after an update.
- **Device:** integrity, root or OS warnings; one phone fails but another works.
- **Authentication:** password, OTP, binding, SIM block or biometric messages; generic "bilgiler hatalı" by design.
- **Transaction-processing:** login works, but a specific payment is pending, declined or debited without credit.
- **Bank-wide:** many customers, several channels, matches the incident board or a maintenance notice.

**Decision tree A — "Giriş yapamıyorum" [T4]**
1. L1 safety screen. If a risk is found, go to fraud and stop.
2. Is there a known incident or maintenance? If yes, use the incident script and offer alternative channels.
3. Which symptom?
   - **App won't open, white screen or crash.** Check OS support and update the app. Check network, VPN and beta OS. Do not reinstall until the prerequisites are met. If several users report it, treat it as a possible incident.
   - **"Bilgiler hatalı", "şifre bloke".** Stop retries. Check customer-set restrictions (time, IP, abroad). Use self-service reset (card + PIN, NFC chip ID, video call, ATM, branch). The agent never resets manually.
   - **Code or approval doesn't arrive.** Go to Tree B.
   - **New phone, "cihaz tanımlı değil".** Use the re-binding flow. Clear any SIM block first. Unbind old or lost devices via the authenticated channel.
   - **Security, root or screen-sharing warning.** If someone is guiding the customer, go to fraud. Otherwise close the sharing or remote tools the customer installed themselves. Never bypass the check.
   - **Abroad.** Check foreign-IP access, roaming, and push approval over data.
4. Is it still failing? Escalate with the diagnostic bundle.

**Decision tree B — "SMS/onay kodu gelmiyor" [T4]**
1. Did the customer start this action themselves? If no, go to fraud; tell them not to share any code.
2. Which code is it, and is the app active on this phone? If the app is active, check in-app pending approvals or messages and notification permission.
3. Was there a recent SIM, operator, eSIM or 4.5G change, or a port? If yes, it is likely a SIM block; use the bank's unblock route (app NFC, ATM card + PIN, IVR, branch).
4. Is the number current? If it changed, use the number-update route (ATM, branch, app with strong verification).
5. Check the phone: signal and airplane mode, roaming, blocked or spam sender, which SIM in a dual-SIM phone, storage, restart.
6. Check the operator: SMS barring or a line problem; contact the operator.
7. Check the bank side: incident or rate limit. Wait out the validity window; do not spam resend.
8. Offer alternatives (push, NFC, ATM, branch, video). If unresolved, escalate with the time, code type, operator and attempt count.

### Gaps
- The escalation team names are generic; each bank's internal routing must be mapped.

## 11. Per-issue handling guidance (19 issues)

### Takeaway
Each card lists: why customers call (and their wording), what to determine, the checks (lowest risk first), the resolution, the never-dos, escalation, and suggested wording. Turkish facts are cited in §§1–9; cards are [T4] unless tagged.

### Cited Findings
- Bank-specific steps referenced below: Garanti, İş Bankası, Akbank, Ziraat, Yapı Kredi, Halkbank, DenizBank, QNB, Enpara — see the §1 sources. Regulatory anchors: BSEBY Art. 34, 37–40; the remote-ID regulation; the accessibility regulation — see §§1, 5, 8.

### Inferences
1. **Login failure** ("giriş yapamıyorum", "hata veriyor"). *Determine:* the channel, the error text, and whether this is credentials, binding, SIM block, restriction, device or incident. *Ask:* "Which message exactly? App or web? Since when? Did anything change (phone, SIM, update)? Are you abroad or on VPN?" *Check:* follow Tree A. *Resolve:* self-service reset or unblock; enable access abroad; update the app or browser. *Never:* ask for the password, or "try again" repeatedly (risks a lock). *Escalate:* digital support if the bundle shows no customer-side cause; incident team if several users are affected. *Say:* "Güvenliğiniz için şifrenizi ya da size gelen kodları benimle paylaşmayın; adım adım birlikte kontrol edelim."
2. **Forgotten username/password** ("müşteri numaramı bilmiyorum", "şifremi unuttum"). *Determine:* whether a customer number or TCKN login is possible (TCKN is accepted at many banks). *Resolve:* the in-app or web "Şifremi unuttum" flow with card + PIN, NFC chip ID or video call (Garanti, QNB), or ATM, branch or IVR. For the customer number, Ziraat points to the internet branch, Ziraat Mobil and its contact centre [T3]; give it only after authentication [T4]. *Never:* reveal the customer number before authentication or set a password for the customer. *Say:* "Yeni şifreyi uygulamadaki 'Şifremi Unuttum' adımından kartınız ve kart şifrenizle ya da çipli kimliğinizle kendiniz belirleyebilirsiniz."
3. **Blocked credentials** ("şifrem bloke oldu"). *Determine:* whether this is the password lock or a different block (SIM, card PIN, ID-card PIN, account freeze). *Check:* the lock status (authenticated). *Resolve:* the self-service reset; ID-card PIN locks go to the civil registry (Ziraat [T3]). *Never:* reveal which factor was wrong (by design, BSEBY), or lift blocks manually outside procedure. *Escalate:* repeated unexplained locks may mean an account-takeover attempt → fraud.
4. **OTP/SMS failure.** Tree B. *Never:* ask for, read back or "verify" a code; treat unexpected codes as fraud. *Say:* "Bu kodu kimseyle, bizimle de paylaşmayın. Bu işlemi siz başlatmadıysanız hemen dolandırıcılık hattına aktarıyorum."
5. **Biometric failure** ("parmak izi/yüz tanıma çalışmıyor"). *Determine:* recent enrolment changes, a new screen lock, an OS update, or a new device. *Resolve:* log in with the password, then turn biometrics off and on in app settings; re-bind if prompted (Android key invalidation [T3 Google]). *Never:* advise removing the screen lock or adding someone else's fingerprint. *Escalate:* if it persists after re-enable on a supported device.
6. **Device registration and device change** ("cihaz tanımlayamıyorum"). *Check:* re-binding prerequisites (SMS reachable or NFC, card + PIN). Akbank verification needs **mobile data, not Wi-Fi** [T3]. İş Bankası allows at most 3 devices [T3]. *Resolve:* the bank flow; remove old devices in the app, or by phone if the device is lost (İş Bankası, Enpara, Akbank [T3]). *Never:* bind on the customer's behalf. *Escalate:* old binding cannot be removed → digital support; unknown devices listed → fraud.
7. **New phone or SIM** ("yeni telefona geçtim", "hat değiştirdim"). *Determine:* whether it is a new device, a new SIM or operator (same number), or a new number. *Resolve:* install from the official store → re-activate. Remove any SIM block via app/ATM/IVR/branch (Garanti, Halkbank, Yapı Kredi, Ziraat, İş Bankası [T3]); a SIM change otherwise disables SMS for 90 days (BSEBY [TR·T1]). Enpara app users stay active [T3]. *Never:* advise wiping the old phone before the new one works. *Say:* "Hat ya da operatör değişikliğinden sonra güvenliğiniz için SMS şifreleri durdurulur; blokeyi [kanal] üzerinden kaldırabilirsiniz."
8. **Mobile-banking activation** ("uygulamayı kuramıyorum/şifre alamıyorum"). *Determine:* whether the customer is new to digital, whether the channel was closed by the customer (a new request is needed, BSEBY 37(5)), and whether they have a card + PIN or chip ID. *Resolve:* the bank's first-password flow; QNB's temporary password is valid 5 days and needs IVR callbacks [T3]. *Never:* activate without the customer's request.
9. **Access after a phone-number change** ("numaram değişti kod eski numaraya gidiyor"). *Resolve:* number update only via ATM or branch (Garanti [T3]), the app's pre-login menu or branch (Ziraat [T3]), or the app route (Enpara [T3]). By phone it must be automated (BSEBY 40(2)). *Never:* key in a new number by hand. *Escalate:* a mismatch persists after an ATM update (anecdotal TEB case) → back-office. *Say:* "Numara değişikliği güvenlik nedeniyle yalnızca ATM, şube veya uygulamadaki doğrulamalı adımla yapılabiliyor."
10. **Crashes, blank screens, loading errors** ("açılmıyor", "beyaz ekranda kalıyor"). *Check:* update the app, restart, check storage and network, check OS support, beta OS, a recent OS update, a "works on other phone?" test. *Resolve:* update; clear cache only per bank guidance; reinstall only once the prerequisites are met. *Escalate:* several reports or one device model → digital/IT with versions. *Never:* suggest third-party "fix" apps or modified APKs.
11. **Browser compatibility** ("internet şubesi açılmıyor"). *Check:* an updated browser, cookies allowed, pop-ups allowed for the bank domain only, extensions off, the URL typed by hand, the personal welcome image or name shown. *Resolve:* update or switch browser; remove restrictions the customer set (IP, time, abroad). *Never:* advise disabling antivirus or certificate warnings. Password autofill is blocked by design (BSEBY 38(1)).
12. **Connectivity.** *Check:* Wi-Fi vs mobile data (captive portals, corporate networks), VPN or proxy, roaming. Push approval needs internet; SMS needs coverage (Ziraat [T3]). *Resolve:* switch network; disable a VPN *the customer chose to use*. *Escalate:* only if failing on multiple networks.
13. **Failed document upload / incomplete onboarding** ("NFC okumuyor", "görüntülü görüşme koptu"). *Resolve:* NFC tips (§5); good lighting and camera permission; restart the session; old-type ID → courier or branch (Garanti [T3]); faulty chip → NVİ. *Never:* accept ID photos over chat or e-mail outside the secure flow. *Escalate:* KYC operations if the application is stuck.
14. **Slow transactions or unclear loading** ("para düştü mü?"). *Resolve:* check status or history before any retry; obtain an EFT query number (Ziraat [T3]); pass debited-not-credited cases to payments (researcher 07). *Never:* say "try again" when the state is unknown. *Say:* "Tekrar denemeden önce işlemin durumunu birlikte kontrol edelim; çift ödeme oluşmasın."
15. **Push-notification failures** ("onay bildirimi gelmiyor"). *Resolve:* open the app and look at pending approvals (Axess/Juzdan, İşCep bell [T3]); check notification permission, Focus/DND, battery or restricted-app settings; re-bind if the app was reinstalled (Ziraat [T3]). *Escalate:* if no device-side cause is found.
16. **Digital-wallet connection problems** ("kart cüzdana eklenmiyor"). *Determine:* which wallet (bank app contactless, watch, Masterpass, foreign Apple Pay). Apple Pay is unavailable for Turkish cards [T3 Apple list]. *Check:* NFC on, the default payment app, OS version, device integrity, card eligibility, SIM block (Masterpass). *Escalate:* card ops (researcher 06). *Never:* promise availability dates.
17. **3-D Secure failures** ("3D şifresi gelmiyor", "ödeme onaylanmadı"). *Determine:* code not received vs declined vs timed out vs night-time NFC step. *Check:* SIM block (Yapı Kredi [T3]); internet shopping on and within limit (Enpara [T3]); the app approval path; pop-up or iframe blocking; time (22:00–06:00, Garanti [T3]). *Never:* help push a purchase through for a third party; unknown 3D codes go to fraud.
18. **Accessibility or usability problems.** *Resolve:* screen reader, larger font or contrast; non-call-centre password routes and adapted IVR timing (TR·T1); text or video-interpreter channels; branch alternatives. *Escalate:* record the barrier for the accessibility or complaints owner. *Say:* "Size en uygun yöntemi birlikte seçelim; isterseniz [alternatif kanal] üzerinden de ilerleyebiliriz."
19. **Maintenance and outages.** *Resolve:* confirm on the incident or maintenance channel; give the published window; offer alternative channels (ATM, other app or channel). *Never:* speculate on the cause, blame the customer, or declare "fixed" without confirmation. *Escalate:* new symptoms to the incident team with a time-stamped count.

### Gaps
- Card wording is not tested with customers; Turkish phrasing should be reviewed by researcher 11.

## Source register
(Accessed 2026-10-10. Publisher; date; jurisdiction; tier.)
1. Bankaların Bilgi Sistemleri ve Elektronik Bankacılık Hizmetleri Hakkında Yönetmelik — BDDK; RG 15.03.2020 No. 31069; TR; regulation — https://www.resmigazete.gov.tr/eskiler/2020/03/20200315-10.htm
2. Amendment setting entry-into-force dates (01.07.2020 / 01.01.2021) — BDDK; RG 20.06.2020; TR; regulation — https://www.resmigazete.gov.tr/eskiler/2020/06/20200620-1.htm
3. Genelge 2023/1 (authentication & transaction security criteria) — BDDK; Board Decision 23.03.2023 No. 10546; TR; regulator circular — https://www.bddk.org.tr/Mevzuat/DokumanGetir/1171
4. Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine… Yönetmelik — BDDK; RG 01.04.2021 No. 31441; TR; regulation — https://www.resmigazete.gov.tr/eskiler/2021/04/20210401-7.htm
5. Bankacılık Hizmetlerinin Erişilebilirliğine Dair Yönetmelik — BDDK (text hosted by Aile ve Sosyal Hizmetler Bakanlığı); in force 01.01.2017; TR; regulation — https://www.aile.gov.tr/eyhgm/mevzuat/ulusal-mevzuat/yonetmelikler/bankacilik-hizmetlerinin-erisilebilirligine-dair-yonetmelik/
6. Law No. 7571 (TCK and other laws amendment; EHK Art. 50, Law 6493 Art. 12) — TBMM; RG 25.12.2025 No. 33118; TR; law — https://www.resmigazete.gov.tr/eskiler/2025/12/20251225-33.htm
7. TİHEK Kurul Kararı 2024/115 — TİHEK; 08.02.2024 (doc. 21.03.2024); TR; equality-body decision — https://www.tihek.gov.tr/public/images/kararlar/432khm.pdf
8. e-Devlet SIM blokesi FAQ — e-Devlet Kapısı; undated; TR; government — https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=355
9. e-Devlet NFC chip-ID FAQ — e-Devlet Kapısı; undated; TR; government — https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=337
10. SIM Kart Değişikliği — Garanti BBVA; undated (© 2026); TR; bank — https://www.garantibbva.com.tr/dijital-bankacilik/sim-kart-degisikligi
11. Cihaz Eşleşmesi — Garanti BBVA; undated (© 2026); TR; bank — https://www.garantibbva.com.tr/dijital-bankacilik/cihaz-eslesmesi
12. İnternet Bankacılığı Şifre Alma — Garanti BBVA; undated (© 2026); TR; bank — https://www.garantibbva.com.tr/dijital-bankacilik/nasil-sifre-alinir
13. Dijital Bankacılık SSS — Garanti BBVA; undated (some legacy content); TR; bank — https://www.garantibbva.com.tr/sikca-sorulan-sorular/dijital-bankacilik
14. İşlem Kısıtları (22:00–06:00 NFC) — Garanti BBVA; undated (© 2026); TR; bank — https://www.garantibbva.com.tr/dijital-bankacilik/islem-kisitlari
15. 3D Secure Nedir (blog; snippet) — Garanti BBVA; undated; TR; bank — https://www.garantibbva.com.tr/blog/3d-secure-nedir
16. Güvenlik Uygulamalarımız — Türkiye İş Bankası; undated; TR; bank — https://www.isbank.com.tr/guvenlik-uygulamalarimiz
17. Güvenli Cihaz Tanımlama — Akbank; undated; TR; bank — https://www.akbank.com/dijital-bankacilik/akilli-cozumler/guvenli-cihaz-tanimlama
18. Samsung Temassız Ödeme — Akbank; undated; TR; bank — https://www.akbank.com/dijital-bankacilik/akilli-cozumler/samsung-temassiz-odeme
19. 3D Secure Juzdan Onay — Axess (Akbank); undated; TR; bank — https://www.axess.com.tr/axess/sayfa/1/7358/3d-secure-juzdan-onay
20. İnternet Bankacılığı SSS — Ziraat Bankası; undated; TR; bank — https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi
21. SIM Kart Değişikliği Yardım — Yapı Kredi; undated; TR; bank — https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/sim-kart-degisikligi-yardim
22. SIM Kart Değişikliği — Halkbank; undated; TR; bank — https://www.halkbank.com.tr/tr/dijital-bankacilik/guvenlik/sizin-icin-sunduklarimiz/sim-kart-degisikligi
23. Planlı Kesintiler (snippet) — Halkbank; undated; TR; bank — https://www.halkbank.com.tr/tr/dijital-bankacilik/planli-kesintiler
24. MobilDeniz Güvenlik Ayarları — DenizBank; undated; TR; bank — https://www.denizbank.com/dijital-bankacilik/guvenlik/mobildeniz-guvenlik-ayarlari
25. Planlı Kesintiler (snippet) — DenizBank; entries 09.06.2024, 12.06.2026; TR; bank — https://www.denizbank.com/dijital-bankacilik/planli-kesintiler
26. QNB Mobil'e Nasıl Giriş Yapabilirim — QNB; undated; TR; bank — https://www.qnb.com.tr/724-bankacilik/qnb-mobile-internet-subesine-nasil-giris-yapabilirim/qnb-mobile-nasil-giris-yapabilirim
27. Enpara SSS — Enpara Bank; undated; TR; bank — https://www.enpara.com/sss
28. Jailbreak ve Rootlama (blog) — Vakıf Katılım; published 12.11.2025; TR; bank — https://www.vakifkatilim.com.tr/tr/hakkimizda/medya-merkezi/blog/detay/jailbreak-ve-rootlama-nedir-cihaz-guvenliginizi-nasil-tehlikeye-atar
29. Zararlı Yazılım Önlemleri (snippet) — Odeabank; undated; TR; bank — https://www.odeabank.com.tr/guvenlik/zararli-yazilim-riskine-karsi-guvenlik-onlemleri
30. Papara FAQ (snippet) — Papara; undated; TR; e-money — https://www.papara.com/faq/hesap-islemleri/hesabimi-nasil-onaylayabilirim
31. Bankalardan SMS alamıyorum (snippet) — Vodafone TR; undated; TR; operator — https://www.vodafone.com.tr/yardim/ayarlar/sms-mesajlasma/bankalardan-kisa-mesaj-sms-alamiyorum-ne-yapmaliyim
32. Kredi kartlarına gece kısıtlaması mı? — Habertürk; 12.11.2025; TR; press — https://www.haberturk.com/kredi-kartlarina-gece-kisitlamasi-mi-getirildi-iste-yaniti-3837235-ekonomi
33. IBAN'la para transferine yeni zorunluluk mu? — Yeni Şafak; 27.03.2026; TR; press — https://www.yenisafak.com/galeri/ekonomi/ibanla-para-transferi-islemlerine-yeni-zorunluluk-mu-geliyor-iste-bddk-kararinin-perde-arkasi-4809615
34. Commission Delegated Regulation (EU) 2018/389 (SCA RTS) — EU; 2018; EU; regulation — https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389
35. European Accessibility Act page — AFM (NL); undated (© 2025); EU; regulator — https://www.afm.nl/en/sector/themas/dienstverlening-aan-consumenten/toegankelijkheid
36. PSR/PSD3 agreed — William Fry; 28.11.2025; EU; law-firm analysis — https://www.williamfry.com/knowledge/psr-psd3-eu-payment-services-legislation-is-agreed/
37. PSR key impacts — EY; 26.09.2025; EU; professional analysis — https://www.ey.com/en_be/technical/financial-services/financial-services-alerts/payment-services-regulation-key-impacts-on-payment-service-providers
38. Authentication and Access to Financial Institution Services and Systems — FFIEC (FDIC FIL-55-2021 attachment); Aug 2021; US; supervisory guidance — https://www.fdic.gov/news/financial-institution-letters/2021/fil21055a.pdf
39. NIST SP 800-63B-4 — NIST; July 2025 (planning note 06.10.2026); US; standard — https://pages.nist.gov/800-63-4/sp800-63b.html ; https://csrc.nist.gov/pubs/sp/800/63/b/4/final
40. BCOBS 7 (snippet) — UK FCA Handbook; current; UK; rule — https://handbook.fca.org.uk/handbook/bcobs7
41. Take Five (snippet) — UK Finance; current; UK; industry campaign — https://www.takefive-stopfraud.org.uk/
42. Bank imposter scams (snippet) — Wells Fargo; undated; US; bank — https://www.wellsfargo.com/privacy-security/fraud/bank-scams/bank-imposter/
43. EMV 3-D Secure — EMVCo; page current 2026; global; standards body — https://www.emvco.com/emv-technologies/3-d-secure/
44. Browser-based OOB authentication — EMVCo; 04.02.2026; global; standards body — https://www.emvco.com/knowledge-hub/emv-3-d-secure-how-merchants-and-issuers-can-enhance-browser-based-out-of-band-authentication/
45. Countries and regions that support Apple Pay — Apple; 30.09.2026; global; vendor — https://support.apple.com/en-us/102775
46. Use notifications on iPhone — Apple; undated (iOS 26 imagery); global; vendor — https://support.apple.com/en-us/108781
47. Doze and App Standby — Google/Android; updated 18.08.2026; global; vendor — https://developer.android.com/training/monitoring-device-state/doze-standby
48. KeyGenParameterSpec.Builder — Google/Android; updated 03.08.2026; global; vendor — https://developer.android.com/reference/android/security/keystore/KeyGenParameterSpec.Builder
49. Android expands in-call scam protection for financial apps — Google; 03.12.2025; UK/BR/IN; vendor — https://blog.google/security/android-expands-pilot-in-call-scam-protection-financial-apps/
50. MASVS-RESILIENCE — OWASP; current; global; security standard — https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/
51. Chrome pop-up help (snippet) — Google; current; global; vendor — https://support.google.com/chrome/answer/95472?hl=TR&co=GENIE.Platform%3DDesktop
52. Expatrio device-security help (snippet) — Expatrio; undated; DE; fintech — https://help.expatrio.com/tr/article/kb-16912353688860
53. Şikayetvar pages (anecdotal; 2025–2026 complaints) — https://www.sikayetvar.com/is-bankasi/mobil-onay-gelmiyor ; https://www.sikayetvar.com/kod-gelmiyor/sim-kart-degisikligi ; https://www.sikayetvar.com/denizbank/ekran-paylasimi ; https://www.sikayetvar.com/yapi-kredi-bankasi/yapi-kredi-mobil-uygulama-beyaz-ekran-sorunu ; https://www.sikayetvar.com/yapi-kredi-bankasi/beyaz-ekran-hatasi-ile-mobil-sifre-alamiyorum-musteri-destegi-yok ; https://www.sikayetvar.com/xiaomi/guncelleme-sonrasi-banka-uygulamasina-giris-sorunu ; https://www.sikayetvar.com/papara/giris/onay-kodu
54. Other anecdotal: Samsung Community (DenizBank remote-access message) — https://r2.community.samsung.com/t5/Samsung-Members/Denizbank-uygulamas%C4%B1nda-a%C5%9Fa%C4%9F%C4%B1daki-uyar%C4%B1-veriyor-ve-kapat%C4%B1yor/td-p/15400220 ; Ekşi Sözlük — https://eksisozluk.com/gece-alisveris-icin-nfc-okutma-zorunlulugu--8044737 ; Technopat — https://www.technopat.net/sosyal/konu/telefona-3d-secure-onay-kodu-gelmiyor.1994864/

## Open questions / unverified items / institution-specific confirmation
- **Night-time (22:00–06:00) extra verification:** the BDDK instruction is unpublished. Official Garanti scope (loans, cash advance, limits, internet/MOTO shopping) conflicts with press claims of IBAN transfers of 20,000 TL or more, and Habertürk reported "no ID requirement". Each bank's scope, thresholds and non-NFC fallbacks need confirmation. Also unclear: whether "internet shopping" means every purchase or enabling the feature.
- **SIM-block mechanics:** which operator events trigger it (eSIM transfer, operator SIM swap, 4.5G upgrade), how "confirmation" ends the 90-day period at each bank, and why customers report blocks without any change.
- **Biometric classification** under BSEBY Art. 39(1)–(2) and Circular 2023/1 (only partially read): how banks treat Face ID/Touch ID; researcher 02.
- **Lockout thresholds,** OTP validity and resend limits, inactivity timeouts, and maximum bound devices per bank (only İş Bankası's 3 devices and Ziraat's 3-minute OTP confirmed).
- **Push-approval names** and internet-login flows for Akbank, Yapı Kredi, VakıfBank, QNB and ING; ING not researched; VakıfBank NFC-only digital onboarding seen only in social-media snippets.
- **Wallets:** Google Wallet and Samsung Wallet status for Turkish cards in 2026; whether any Turkish bank supports Apple Pay through a foreign issuer arrangement.
- **Law 7571 follow-up:** BTK secondary rules on line limits and identity checks at SIM replacement.
- **Regulatory updates:** whether BSEBY, the remote-ID regulation or the accessibility regulation were amended in 2024–2026 (consolidated texts not checked); final EU PSR text, publication and application dates.
- **AI-agent design:** whether an AI agent is a "görevli" under BSEBY Art. 40(3) (secret entry only via automated systems), and what Art. 40(1) means for AI access to customer data before 2FA; researcher 02/12.
- **Institution-specific:** escalation team names, incident-confirmation tools, status-page practices, maintenance windows, and which agent tools can read credential, SIM or binding status — verify against each institution's internal procedure.
