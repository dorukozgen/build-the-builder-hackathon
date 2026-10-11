# 05 — Account Support: Contact Reasons, Root Causes and Safe Handling (Türkiye primary; EU/UK/US comparison)

Researcher 05. Date context: 2026-10-10. All sources accessed 2026-10-10. Turkish laws are cited from consolidated mevzuat.gov.tr PDFs, which list amendments up to the access date. "Undated" means the page shows no date.

**Tags**
- [L-TR] / [L-UK] / [L-US]: law or regulation in that jurisdiction.
- [IND]: common industry practice.
- [BANK: X]: a named bank's own policy.
- [REC]: recommended service practice (my synthesis).
- [VERIFY]: assumption to check against the institution's internal procedure.
- [ANEC]: anecdotal forum wording.
- [AUTH]: the step requires an authenticated customer.
- [HUMAN]: only staff or a specialist team can do this.

Source IDs (S#) are listed in the register at the end.

**Rules that apply to every section**
- **Bank secrecy** [L-TR]: customer data may be shared with a third party only on the customer's own request or instruction. KVKK explicit consent is not enough on its own ([S2 Banking Law art. 73(3)](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)).
- **No tipping-off** [L-TR]: no one may be told that a suspicious-transaction report (şüpheli işlem bildirimi, STR) has been or will be filed. This includes the parties to the transaction and covers every staff member who knows about it ([S8 art. 4(2)](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf); [S9 art. 29](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **What banks never ask for** [BANK: Ziraat]: the bank never asks for passwords, card PINs or SMS OTPs by phone, and never updates customer data via SMS or e-mail links ([S32](https://www.ziraatbank.com.tr/tr/dijital-bankacilik/guvenlik/yaygin-dolandiricilik-turleri)).
- **Agent safety** [REC]: the agent never asks for or accepts a PIN, full password, CVV or OTP, and never asks for remote access to a device. It never reads full account numbers or IBANs to an unverified caller. Where a flow needs a PIN (ATM, IVR keypad), the agent routes the customer to that channel.

---

## 1. Account opening and eligibility (hesap açılışı / müşteri olma)

### Takeaway
In Türkiye, fully remote onboarding is open only to holders of the chip T.C. ID card, through the BDDK video-call plus NFC process. There is also a passport-based route under YUVAM. Everyone else opens in a branch: most foreigners, minors (through a guardian) and anyone whose remote checks fail. If customer due diligence (CDD) cannot be completed, the bank must refuse, and it does not explain risk-based declines.

### Cited Findings
- **How remote onboarding works** [L-TR] (BDDK regulation: RG 1/4/2021 No. 31441, in force 1/5/2021; amended RG 6/4/2022 No. 31801 and RG 25/5/2023 No. 32201; no later amendment in the consolidated text):
  - The applicant first fills a form in the bank's app. A risk assessment can end the process before any video call.
  - Remote ID (uzaktan kimlik tespiti) is then a live, uninterrupted, end-to-end secured video call with trained bank staff ([S1 arts. 4–6](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)).
- **Required ID checks** [L-TR]:
  - The document must be the T.C. Kimlik Kartı, with its chip verified via NFC (yakın alan iletişimi).
  - If NFC fails, at least four visual security features must be checked, and the first money into the account must come from the customer's own account at another bank.
  - Further checks: liveness and biometric face match, serial number read aloud, MRZ and Kimlik Paylaşım Sistemi (KPS, the national ID-data sharing system) match, and an SMS OTP to verify the phone number ([S1 arts. 3(e), 6(7), 7, 8](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)).
- **When the call must end** [L-TR]: weak light, poor image or sound, any inconsistency, or suspected forgery or fraud. Staff must watch for social engineering and for coercion by a third party ([S1 arts. 8(4), 9](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)).
- **After onboarding** [L-TR]: remotely onboarded customers are monitored in a separate risk profile. In a dispute, the bank bears the burden of proof ([S1 art. 11](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)).
- **Other remote routes** [L-TR] ([S1 arts. 4(10), 7/A–7/C, 12/A](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)):
  - YUVAM (2022): citizens abroad and Blue Card holders can onboard with an NFC passport. These accounts can only move money to and from the person's own accounts.
  - 2023: companies can onboard remotely, and disabled applicants may have third-party help on the call.
- **When CDD applies** [L-TR]:
  - Always when a continuous relationship starts, whatever the amount.
  - Identity must be verified before the relationship starts, and the bank must ask about its purpose.
  - Thresholds: occasional transactions 370,000 TL; wire transfers 30,000 TL. These were raised by CK 11845 (RG 7/10/2026) and change periodically ([S9 art. 5](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **What the bank collects** [L-TR] ([S9 art. 6](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)):
  - Data: name, date of birth, nationality, ID type and number, address, signature specimen, job details, and phone/e-mail if available; TCKN for citizens, birthplace for foreigners.
  - Accepted ID for citizens: nüfus cüzdanı or kimlik kartı, driving licence, or passport.
  - Accepted ID for foreigners: passport, residence document, or a ministry-approved ID.
  - Address proof: yerleşim yeri belgesi (residence certificate), a utility bill no older than 3 months, a public document, or another method approved by MASAK (Türkiye's financial intelligence unit).
- **Acting for someone else** [L-TR]: the customer must declare in writing whether they act on someone else's behalf ([S9 art. 17](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **When identity cannot be established** [L-TR]: if identity or purpose cannot be established, the bank must not open the relationship or process the transaction, must not open anonymous accounts, and must assess whether to file an STR ([S9 art. 22](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Foreign nationals** [VERIFY per bank]:
  - Usually need a yabancı kimlik numarası (YKN, foreigner ID number). Some banks open accounts without it if extra documents are provided, sometimes against a deposit ([S41 İTÜ](https://global.itu.edu.tr/tr/uluslararasi-akademisyenler/sozlesmesiz-misafir-arastirmacilar/banka-hesabi)).
  - Wise says: passport plus YKN or tax number; a tax number is needed if there is no residence permit ([S42](https://wise.com/tr/blog/yabancilar-banka-hesabi)).
- **Minors** [L-TR]: majority starts at 18, or earlier on marriage, and a court may declare a 15-year-old an adult. A minor who can understand the act still cannot take on obligations without the legal representative's consent ([S11 TMK arts. 11, 12, 16](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf)).
- **Bank policies for minors**:
  - [BANK: İş Bankası] "İlk İmza" accounts are for ages 12–17, opened in the child's own name on a guardian's instruction. The guardian must be an İş Bankası customer and the contract is signed in a branch. The card is closed to gambling, alcohol and tobacco merchants. "Kumbara" accounts are for ages 0–11 and are run by a parent ([S36](https://www.isbank.com.tr/ilk-imza-hesabi)).
  - [BANK: Enpara] under-18s cannot open accounts themselves; a parent or guardian opens it, and that authority ends at 18 ([S37](https://www.enpara.com/bilgi-bankasi/cocuklar-icin-tasarruf-birikim-hesabi)).
- **US comparison** [L-US]: if refused a checking account, ask which checking-account reporting company was used, get the free report, and dispute errors (CFPB, reviewed 18 Dec 2024) ([S52](https://www.consumerfinance.gov/ask-cfpb/i-was-denied-a-checking-account-because-of-a-report-what-can-i-do-en-1113/)).
- **Real customer complaints** [ANEC] (2026, [S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)):
  - "Hesaba erişememe ve görüntülü görüşme engeli" — can't access the account, video call blocked.
  - "Sahte iş teklifi ve kimliğimle açılan banka hesabı" — a fake job offer, and an account opened in my name.

### Inferences
#### 10-point handling guide
1. **Why they contact:** want to open an account; onboarding is stuck; application declined; foreigner asking about documents; child account; "someone opened an account in my name".
2. **What they experience:** "NFC okunmuyor" (NFC won't read), "görüntülü görüşmeye bağlanamıyorum" (can't connect to the video call), "şubeye başvurunuz" (please apply at a branch).
3. **What they provide:** name, TCKN or YKN, nationality, screenshots, application reference. Do not accept ID images in chat [REC].
4. **What the agent must determine:**
   - which channel they qualify for (chip ID → remote; foreigner or minor → branch);
   - the step where it failed;
   - whether they are already a customer;
   - any third-party involvement.
5. **Clarifying questions:**
   - "Yeni çipli kimlik kartınız mı var?" (Do you have the new chip ID card?)
   - "Telefonunuzda NFC açık mı?" (Is NFC switched on?)
   - "Hangi adımda hata aldınız?" (At which step did you get the error?)
   - "Hesabı kendiniz için mi açıyorsunuz?" (Are you opening the account for yourself?)
6. **Checks:**
   - Application status [AUTH/HUMAN].
   - Technical: lighting, phone case, network, app version.
   - A recent ID renewal or name change can cause a KPS mismatch [VERIFY].
7. **Resolution:**
   - Give retry tips.
   - Offer branch onboarding: citizens bring ID; foreigners bring passport, YKN or tax number, and proof of address [VERIFY].
   - Minors come with their guardian.
8. **Must not:**
   - promise approval or timing;
   - reveal risk or AML reasons;
   - coach the customer on passing the checks;
   - suggest using another person's phone line;
   - ask for the OTP.
9. **Escalate:**
   - identity misuse, coercion or money-mule signals → Fraud/AML (without tipping off);
   - repeated technical failures → Digital onboarding;
   - complaints → Complaints unit.
10. **Wording:**
    - TR: "Başvuru değerlendirme ayrıntılarını paylaşamıyoruz; dilerseniz kimliğinizle şubemizden yüz yüze başvurabilirsiniz."
    - EN: "We can't share details of how applications are assessed, but you can apply in person at a branch with your ID."

### Gaps
- Banks' minimum age for remote onboarding is not public.
- Some secondary sources say foreigners can onboard remotely. This conflicts with the regulation's ID-document definition (T.C. card) [VERIFY].
- No Turkish equivalent of the EU basic-payment-account right was found. The EU directive text (PAD) could not be retrieved.

---

## 2. Updating personal data and contact details (adres, telefon, e-posta)

### Takeaway
Address data in Türkiye comes from MERNİS/AKS (the national population and address registers) via KPS. A phone-number change is the riskiest update. Banks block SMS OTPs after a SIM change (SIM blokesi), and the customer clears the block in the app, at an ATM or at a branch — not on an unauthenticated call.

### Cited Findings
- **Address law** [L-TR]: an address change must be declared within 20 working days, to a population office or a designated institution. The Ministry may share address data with institutions via KPS ([S13 Law 5490 arts. 50–52](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5490.pdf)).
- **Keeping data current** [L-TR]: banks must keep records current and confirm phone and e-mail on a risk basis by contacting the customer through them ([S9 art. 19](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Signature waiver** [L-TR]: from 7/10/2026 (CK 11845), banks may skip the signature specimen for later transactions verified through internet or mobile banking, or by an SMS OTP to a previously verified number. The method must suit the risk and guard against unauthorized users ([S9 art. 16](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Bank channels for changing contact details**:
  - [BANK: QNB] identity, address, e-mail and landline can be changed in internet banking. The mobile number can only be changed at a branch ([S20](https://www.qnb.com.tr/sss/bilgi-guncelleme)).
  - [BANK: Ziraat] the mobile number can be updated and a SIM block removed in Ziraat Mobil before logging in (Diğer İşlemler → Telefon/SIM Kart İşlemleri), or at an ATM or branch ([S19](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi)).
  - [BANK: Garanti BBVA] after a SIM change (operator change, number porting, new number, SIM renewal), OTP SMS messages are blocked "for your security". The block is removed via: an app video call (paired device), IVR (card PIN keyed in), ATM (card + PIN), or branch ([S21](https://www.garantibbva.com.tr/dijital-bankacilik/sim-kart-degisikligi)).
- **e-Devlet SIM block** [GOV]: e-Devlet runs its own SIM block. It is removed via NFC with the ID card, e-signature or mobile signature, a Garanti or Akbank ATM, or PTT ([S22](https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=355)).
- **Real complaint** [ANEC]: a branch typed the wrong address when reissuing a card ([S34](https://www.sikayetvar.com/garanti-bbva/soyadi-degisikligi)).

### Inferences
#### 10-point handling guide
1. **Why:** moved house; new number or SIM; OTPs not arriving; card sent to an old address.
2. **Experience:** "SMS şifresi gelmiyor" (SMS code not arriving), "SIM kart blokesi" (SIM block).
3. **Provide:** the new contact data, often on an unauthenticated line.
4. **Determine:**
   - whether authentication is possible without the old number;
   - signs of a SIM swap;
   - whether MERNİS already has the new address.
5. **Questions:**
   - "Numaranızı taşıdınız mı / SIM kartınız değişti mi?" (Did you port your number or change your SIM?)
   - "Uygulamaya giriş yapabiliyor musunuz?" (Can you log in to the app?)
6. **Checks:** recent contact changes combined with new payees — a takeover pattern [HUMAN][VERIFY].
7. **Resolution:** route to secure self-service (app pre-login flow, ATM) or a branch. Addresses can often be updated digitally or from MERNİS [VERIFY].
8. **Must not:**
   - change a phone number or e-mail on an unauthenticated call;
   - send an OTP to a number the caller has just given;
   - collect a PIN.
9. **Escalate:** "I didn't change my SIM" but OTPs stopped, or a contact change followed by transfers → Fraud, urgently.
10. **Wording:**
    - TR: "Güvenliğiniz için numara değişikliğini telefonda yapamıyoruz; uygulamamızın giriş ekranındaki SIM/telefon işlemlerinden, ATM'den veya şubeden yapabilirsiniz."
    - EN: "For your security we can't change your number by phone. Use the SIM/phone option on the app's login screen, an ATM, or a branch."

### Gaps
- No regulatory "cooling-off" period after a phone or e-mail change was found. Bank-internal holds (for example payee limits) are not public [VERIFY].
- No UK or US primary source on notifying customers of contact changes was gathered.

---

## 3. KYC refresh and document requests (müşteri bilgi güncelleme)

### Takeaway
Banks must keep customer data current and check that activity fits the customer's profile and source of funds. If re-verification fails, the bank must end the relationship. That is why restrictions follow when a customer ignores an update request. Genuine requests arrive only inside the bank's app or branch, never through SMS or e-mail links.

### Cited Findings
- **Ongoing monitoring** [L-TR]: activity is monitored against the customer's job, business, finances, risk profile and source of funds, and records are kept current ([S9 art. 19](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Re-verification** [L-TR]: identity checks are repeated when earlier data is in doubt ([S9 art. 5(1)(e)](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)). If re-verification fails, the relationship ends and the case is assessed for an STR ([S9 art. 22(2)–(3)](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Required data and retention** [L-TR]: job details are a mandatory field ([S9 art. 6](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)). Identity records are kept 8 years after the last transaction ([S8 art. 8](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)).
- **Bank stance on phishing** [BANK: Ziraat] ([S32](https://www.ziraatbank.com.tr/tr/dijital-bankacilik/guvenlik/yaygin-dolandiricilik-turleri)):
  - "Bankamız tarafından kısa mesaj ya da e-posta yoluyla kesinlikle bilgi güncellemesi yapılmamaktadır" — the bank never updates information via SMS or e-mail.
  - Typical phishing lines: "İnternet Bankacılığınızın süresi dolmuştur" (your internet banking has expired), "şüpheli işlemler tespit edilmiştir" (suspicious transactions detected).
- **Real wording** [ANEC] ([S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)):
  - App message: "Dijital Bankacılık kanallarımızdan yararlanmak için lütfen şubenize başvurunuz" (to use digital banking, please visit your branch).
  - Bank reply: "hesabınız inceleniyor" (your account is under review).

### Inferences
#### 10-point handling guide
1. **Why:** an update request arrived; channels were restricted; "is this message real?"
2. **Experience:** "bilgi güncelleme" (information update), "gelir/meslek bilginizi güncelleyin" (update your income/job details), digital channels closed.
3. **Provide:** the message text, the sender, and any link.
4. **Determine:**
   - whether the request is genuine — check the case record [AUTH];
   - which documents are outstanding.
5. **Questions:**
   - "Mesajda bağlantı var mıydı?" (Did the message contain a link?)
   - "Bağlantıya bilgi girdiniz mi?" (Did you enter information through it?) → if yes, start the fraud flow.
6. **Checks:** whether a KYC case is open, and its due date [HUMAN]. Typical documents are ID, proof of address, job or income evidence, and a statement of purpose [IND][VERIFY].
7. **Resolution:** the customer completes the update inside the logged-in app or at a branch. A review follows before channels reopen [VERIFY].
8. **Must not:**
   - validate a request that came through a link;
   - accept documents in unsecured chat;
   - give AML reasons;
   - promise that the restriction will be lifted.
9. **Escalate:**
   - credentials entered on a phishing site → Fraud, urgently;
   - document disputes → KYC operations.
10. **Wording:**
    - TR: "Bilgi güncellemesini SMS/e-posta bağlantısıyla istemeyiz; yalnızca uygulamamıza kendiniz giriş yaparak veya şubemizde güncelleyin."
    - EN: "We never ask for updates through a link. Only update your details after logging in to our app yourself, or at a branch."

### Gaps
- KYC refresh frequency by risk tier, and how long before restrictions apply, are not public.
- No MASAK communiqué from 2024–2026 on periodic refresh was located.

---

## 4. Forgotten account details; finding one's IBAN safely

### Takeaway
Customers should get their IBAN or account number from their own authenticated app or from a statement. The agent never reads full identifiers to an unverified caller. e-Devlet shows which banks hold a citizen's deposits, but not balances or account numbers.

### Cited Findings
- **Where customers find details** [BANK: Ziraat]: account information and balance are in internet banking, Ziraat Mobil and the contact center. Passwords are reset via "Şifremi Unuttum" (I forgot my password) ([S19](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi)).
- **e-Devlet bank finder** [GOV: BDDK]: the e-Devlet service "Mevduat/Katılım Fonu Hesabı Bulunan Banka Sorgulama" ([S16](https://www.bddk.org.tr/Sss/Liste/126)):
  - lists which banks hold a citizen's deposit accounts at domestic branches, including zero-balance and joint accounts;
  - excludes development and investment banks and banks under TMSF (the deposit insurance fund);
  - is updated daily and is not an official document;
  - shows no balances or branches, and cannot be used to query other people.
- **Bank secrecy** [L-TR]: data goes to third parties only on the customer's request or instruction ([S2 art. 73](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)).

### Inferences
#### 10-point handling guide
1. **Why:** need an IBAN for salary or rent; forgot which bank they use; forgot customer number or password.
2. **Experience:** "IBAN'ımı bulamıyorum" (I can't find my IBAN), "müşteri numaramı unuttum" (I forgot my customer number).
3. **Provide:** name and TCKN, plus requests like "just read it to me".
4. **Determine:** authentication level; whether the caller is the account holder; whether they can access the app.
5. **Questions:** "Mobil uygulamaya giriş yapabiliyor musunuz?" (Can you log in to the app?)
6. **Checks:** which channels the customer can use [AUTH].
7. **Resolution:** App → Hesaplarım → IBAN kopyala/paylaş (copy/share IBAN); a statement; a password reset; e-Devlet to find which banks hold accounts.
8. **Must not:**
   - read full numbers to an unverified caller;
   - give details to relatives or employers;
   - ask for the old password or an OTP during a reset.
9. **Escalate:** a third party asking about someone else's account → refuse and log; impersonation → Fraud.
10. **Wording:**
    - TR: "IBAN'ınızı güvenliğiniz için uygulamanızdaki 'Hesaplarım' ekranından görüntüleyip paylaşabilirsiniz."
    - EN: "For your security, please view and share your IBAN from the 'My Accounts' screen in your app."

### Gaps
- Whether a fully authenticated phone channel may give out the IBAN is bank policy [VERIFY].

---

## 5. Inactive, dormant, blocked or closed accounts; time-barred deposits (zamanaşımı → TMSF)

### Takeaway
In Türkiye, a deposit not claimed for 10 years after the owner's last claim, transaction or written instruction becomes time-barred. Unclaimed amounts are transferred to TMSF and booked as TMSF income, and **cannot be refunded** unless the transfer was a mistake. This is unlike the UK and US, where the owner's right to reclaim survives. The agent's value is preventive: tell customers how to stop the clock and check the annual lists.

### Cited Findings
- **The legal rule** [L-TR]: deposits, participation funds, safekeeping items and receivables unclaimed for 10 years are time-barred. If the owner cannot be reached, they become TMSF income after a public announcement ([S2 art. 62](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)).
- **When the 10-year clock starts or stops** [GOV: TMSF] (undated, [S3](https://www.tmsf.org.tr/tr/Tmsf/Mevduat/zamanasimi.sorular)):
  - minors' accounts: from the age of majority;
  - time deposits: from maturity;
  - safe-deposit boxes: from the last rent payment or last opening;
  - accounts blocked by authorities: the clock pauses while the block lasts.
- **Annual notice cycle** [GOV: TMSF] ([S3](https://www.tmsf.org.tr/tr/Tmsf/Mevduat/zamanasimi.sorular)):
  - by end of January: registered letters to holders of amounts of 250 TL or more;
  - from February, for 4 months: lists on banks' websites;
  - by 15 February: a newspaper notice;
  - by end of May: consolidated lists from TMSF and the bank associations;
  - by end of June: items unclaimed by 15 June are transferred.
- **No refunds** [GOV: TMSF]: TMSF income is not refundable except for erroneous transfers. To check an account's fate or claim an erroneous transfer, write to the bank's head office with ID and proof of activity ([S3](https://www.tmsf.org.tr/tr/Tmsf/Mevduat/zamanasimi.sorular)).
- **e-Devlet check** [GOV: e-Devlet]: "Bu Yıl TMSF'ye Devredilecek Hesaplara İlişkin Sorgulama" — accounts due to be transferred to TMSF this year (login required) ([S4](https://www.turkiye.gov.tr/tmsf-zamanasimi-hesaplari-sorgulama)).
- **No account-keeping fees** [L-TR]: no fee may be charged for keeping a deposit account open or ready ([S14 art. 13](https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5)). Inference: inactivity fees are not allowed.
- **UK** [BANK: NatWest]: dormant after 5 years (bank-specific); may be closed at 5 years 9 months; after 15 years the balance may move to Reclaim Fund Ltd, with the right to reclaim intact ([S46](https://www.natwest.com/current-accounts/dormant-accounts.html)). Under the government scheme, Reclaim Fund Ltd takes on firms' liability to repay owners (2 Jun 2025) ([S45](https://www.gov.uk/government/publications/dormant-assets-scheme-strategy)).
- **US** [GOV]: typically 3–5 years without customer-initiated activity under state law, then the bank attempts notice and escheats the funds to the state. Owners claim through state unclaimed-property offices or NAUPA (OCC, reviewed Apr 2021) ([S51](https://helpwithmybank.gov/help-topics/bank-accounts/opening-closing-inactive-bank-accounts/inactive-accounts/inactive-unclaimed.html)).

### Inferences
#### 10-point handling guide
1. **Why:** found an old account; received a warning letter; the money is "gone"; wants to reactivate.
2. **Experience:** "hesabım pasife düştü" (my account went inactive), "TMSF'ye devredilmiş" (it was transferred to TMSF).
3. **Provide:** an old passbook (hesap cüzdanı), the letter, heirs' documents.
4. **Determine:**
   - status: active, inactive, listed, or transferred;
   - date of last customer activity;
   - any pause (block, minority).
5. **Questions:**
   - "Son işlem ne zamandı?" (When was the last transaction?)
   - "Zamanaşımı mektubu aldınız mı?" (Did you receive a time-bar letter?)
   - "Hesap sahibi misiniz, mirasçı mı?" (Are you the account holder or an heir?)
6. **Checks:** account status and presence on the list [AUTH/HUMAN].
7. **Resolution:**
   - Before 15 June, any transaction or written request stops the time-bar.
   - After transfer, only an erroneous transfer can be claimed, by writing to head office.
   - Heirs: see section 13.
8. **Must not:** promise recovery of transferred amounts or imply that TMSF refunds them.
9. **Escalate:** suspected erroneous transfer → head-office time-bar unit [HUMAN].
10. **Wording:**
    - TR: "15 Haziran'a kadar hesabınızda işlem yapmanız veya yazılı talep vermeniz zamanaşımını keser."
    - EN: "Making a transaction or a written request before 15 June stops the time-bar."

### Gaps
- Bank-level "inactive" statuses before 10 years, and how to reactivate, are bank-specific.
- No 2024–2026 amendment to art. 62 was found.

---

## 6. Unexpected restrictions, frozen funds and what can be disclosed

### Takeaway
Most "frozen money" contacts come from one of these: an enforcement-office garnishment (haciz), a tax-office or SGK electronic garnishment (e-haciz), a court injunction (tedbir), an AML or fraud hold, a KYC failure, or a death block. For legal orders the bank only complies. It cannot lift them; the customer must deal with the creditor or the authority. For AML holds, the agent must not confirm any STR, MASAK suspension or investigation.

### Cited Findings
- **Garnishment notices to banks** [L-TR]: an enforcement-office notice (haciz ihbarnamesi) means the bank may pay only the enforcement office, and has 7 days to object ([S5 İİK art. 89](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf)).
- **Salary and pension garnishment** [L-TR]: these can be garnished after the officer sets aside what the debtor and family need. The garnished amount cannot be less than one quarter, and several garnishments are queued in order. Prior agreements waiving exemptions are void ([S5 arts. 83, 83/a](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf)).
- **SGK benefits** [L-TR]: SGK pensions and benefits cannot be garnished except for SGK claims and alimony. Requests are rejected unless the debtor consents (muvafakat) ([S7 Law 5510 art. 93](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5510.pdf)).
- **Tax-office garnishment** [L-TR]: tax offices may serve garnishment notices on banks electronically, including on head offices; banks have 7 days to object ([S6 Law 6183 art. 79](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.6183.pdf)). Customers can see these via e-Devlet: GİB "Banka Hesaplarına Uygulanan Elektronik Haciz Sorgulama" ([S28](https://www.turkiye.gov.tr/gib-intvrg-banka-hesaplarina-uygulanan-elektronik-haciz-sorgulama)).
- **How an e-haciz works in practice** [BANK: Enpara] (undated, [S27](https://www.enpara.com/bilgi-bankasi/e-haciz-nedir)):
  - it usually blocks up to the debt amount;
  - a 7-day payment notice comes first;
  - it lifts when the debt is paid or restructured with the tax office;
  - blocked funds are sent to the tax office;
  - linked cards may be blocked too.
- **MASAK suspension** [L-TR]: MASAK may suspend a transaction for 7 working days on suspicion of laundering or terrorist financing ([S8 art. 19/A](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)).
- **Joint accounts**:
  - [BANK: Ziraat] undeclared shares are treated as equal when a haciz, tedbir or death affects one holder. One holder cannot stop the others' payments by notice alone; a court or enforcement order is needed ([S23](https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf)).
  - [BANK: Akbank] the garnishment targets the debtor's share, but the whole account is often blocked (3 Sep 2025) ([S24](https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay)).
- **UK and US comparison**:
  - [L-UK] tipping-off offences ([S48 POCA s.333A](https://www.legislation.gov.uk/ukpga/2002/29/section/333A)).
  - [L-US] SAR confidentiality ([S49 31 U.S.C. 5318(g)(2)](https://www.law.cornell.edu/uscode/text/31/5318)).
  - [L-US] two months of directly deposited federal benefits are protected from garnishment (CFPB, reviewed 29 Jan 2024) ([S53](https://www.consumerfinance.gov/ask-cfpb/can-a-debt-collector-take-my-social-security-or-va-benefits-en-1157/)).
  - [L-UK] bank-initiated closures: 90 days' notice plus written reasons for new contracts, expected from 28 Apr 2026, with financial-crime carve-outs (announced 28 Apr 2025) [VERIFY commencement] ([S47](https://www.gov.uk/government/news/millions-of-people-and-businesses-protected-against-debanking)).
- **Real wording** [ANEC] ([S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)):
  - "Hesabım açıklama olmadan bloke edildi" (my account was blocked without explanation)
  - "şüpheli işlem gerekçesiyle bloke" (blocked as a suspicious transaction)
  - "Yasadışı bahis şüphesi nedeniyle dijital bankacılık ve kredi kartım bloke edildi" (my digital banking and credit card were blocked on suspicion of illegal betting)
  - "MASAK blokesi" (MASAK block)

**Terminology (TR → EN)**
- **bloke / blokaj**: hold or block — generic.
- **haciz**: attachment or garnishment by an enforcement (icra) office or tax office.
- **e-haciz**: electronic garnishment by a tax office or SGK.
- **ihtiyati haciz**: precautionary attachment.
- **(ihtiyati) tedbir**: court interim injunction.
- **el koyma**: criminal seizure [VERIFY basis].
- **kısıt / kısıtlama**: restriction, usually bank-imposed on channels.
- **işlem erteleme**: MASAK transaction suspension.
- **vefat blokesi**: death block.

### Inferences
#### 10-point handling guide
1. **Why:** a payment failed; available balance lower than balance; channels closed; salary blocked.
2. **Experience:** "Hesabımda haciz var" (there's a garnishment on my account), "maaşımın tamamına bloke konmuş" (my whole salary is blocked), "MASAK blokesi" (MASAK block).
3. **Provide:** amount, dates, SMS texts.
4. **Determine** [AUTH/HUMAN]:
   - the type of hold;
   - for legal orders: the issuing office and file number — these may be disclosed;
   - the amount held;
   - for AML or fraud holds: internal codes only, never disclosed.
5. **Questions:**
   - "Bloke tutarı ne kadar?" (How much is blocked?)
   - "İcra/vergi dairesinden tebligat aldınız mı?" (Did you receive a notice from an enforcement or tax office?)
   - "Maaş/emekli aylığı mı yatıyor?" (Is your salary or pension paid into this account?)
6. **Checks:** order details; whether the funds are salary or pension; joint-account shares.
7. **Resolution:**
   - Haciz: give the office's name and file number; the customer settles with the creditor or office, or objects in court; the office instructs the bank to lift it.
   - e-haciz: pay or restructure with the tax office; check e-Devlet.
   - Pension or salary limits: suggest a lawyer or the enforcement court [VERIFY].
   - KYC hold: complete the update.
   - AML or fraud hold: neutral wording, no timeline guarantee.
8. **Must not:**
   - say the bank can lift a haciz;
   - confirm or deny MASAK involvement or an STR;
   - speculate about reasons;
   - give legal advice;
   - suggest moving funds to avoid holds.
9. **Escalate:**
   - possible calculation errors on legal orders → garnishment operations (haciz birimi) [HUMAN];
   - AML holds → Compliance;
   - fraud holds → Fraud;
   - no money for essentials → vulnerable-customer care (team 11).
10. **Wording:**
    - TR (legal hold): "Bloke, … İcra Dairesi'nin … sayılı dosyasındaki haciz yazısından kaynaklanıyor; bankamız kendisi kaldıramaz, ilgili daire veya alacaklıyla görüşmeniz gerekir."
    - EN (legal hold): "The hold comes from a garnishment order in file … at … Enforcement Office. We can't lift it ourselves; you'll need to speak to that office or the creditor."
    - TR (AML/fraud): "Hesabınızda bir inceleme nedeniyle kısıtlama var; ayrıntı paylaşamıyoruz, talebinizi ilgili birime ilettim."
    - EN (AML/fraud): "There's a restriction because of a review. I can't share details, but I've passed your request to the responsible team."

### Gaps
- Court-of-Cassation (Yargıtay) practice on salary or pension money once deposited, and on advance consents, was not verified.
- The legal basis and duration of bank-initiated fraud holds on receiving accounts was not confirmed.
- The criminal-procedure (CMK) seizure article was not retrieved.

---

## 7. Available vs total balance; unexpected incoming credits; money-mule risk

### Takeaway
A gap between bakiye (balance) and kullanılabilir bakiye (available balance) usually comes from a hold (bloke), a pending card authorization (provizyon) or an overdraft limit (KMH). If unexpected money arrives, the customer must not spend or forward it and should tell the bank, which runs the return. Since 31/7/2026, handing over account access for fraud is explicitly treated as participation in fraud.

### Cited Findings
- **Pending authorizations** [BANK: Türkiye Finans]: a card authorization (provizyon) blocks the amount. A pending authorization (bekleyen/açık provizyon) can last up to two days and is released if cancelled (undated) ([S38](https://www.turkiyefinans.com.tr/tr-tr/blog/sayfalar/provizyon-nedir.aspx)).
- **Keeping mistaken money** [L-TR]: treating mistakenly received property as one's own, without returning it or notifying authorities, is punishable on complaint by up to 1 year in prison or a judicial fine ([S10 TCK art. 160](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5237.pdf)). Whether this applies to bank transfers is a legal question [VERIFY].
- **Lending an account** [L-TR]: new TCK art. 158(4), from Law 7589 (adopted 16/7/2026, in force 31/7/2026). Where a person's part in a fraud is limited to handing over, for unjust benefit, their own or someone else's bank or credit card, or the information or tools needed to use a bank, brokerage, payment-service or crypto account, the penalty is halved. The act is still criminal ([S10](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5237.pdf); [S40](https://www.alomaliye.com/2026/07/31/7589-sayili-kanun-yayimlandi-ozet-ve-sss/)).
- **Return fees** [L-TR]: when an EFT is refunded because of the consumer's own error, only the CBRT (central bank) costs may be charged. Returning a havale (same-bank transfer) carries no fee beyond public or third-party costs ([S14 art. 12(2)](https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5)).
- **Real wording** [ANEC]: the Ekşi Sözlük thread "hesaba yanlış para gelirse ne yapılmalı" (what to do if wrong money lands in your account) ([S35](https://eksisozluk.com/hesaba-yanlis-para-gelirse-ne-yapilmali--7038043)). Accounts opened through fake job offers ([S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)).

### Inferences
#### 10-point handling guide
1. **Why:** money not usable; a stranger's credit arrived; someone asks for it back or onward.
2. **Experience:** "bakiyem var ama kullanamıyorum" (I have a balance but can't use it), "yanlışlıkla para geldi, gönderen geri istiyor" (money arrived by mistake and the sender wants it back).
3. **Provide:** amount, sender, chat messages.
4. **Determine:** holds or authorizations; whether the overdraft is included; whether the credit is genuine, has a recall pending, or is part of a fraud chain.
5. **Questions:**
   - "Parayı başka bir IBAN'a göndermeniz istendi mi?" (Were you asked to send the money to another IBAN?)
   - "Para geldikten sonra transfer yaptınız mı?" (Have you made any transfers since it arrived?)
6. **Checks:** the available-balance breakdown and inbound transfer details [AUTH]; any recall from the sending bank [HUMAN].
7. **Resolution:**
   - Pending authorizations release on their own.
   - Mistaken credits: don't spend; the bank returns the money to the original sender's account (mechanics: team 07).
8. **Must not:** direct payment to any third-party IBAN; accuse the customer; advise keeping the money.
9. **Escalate:** requests to forward money, IBAN-rental offers (IBAN kiralama), or many credits from strangers → Fraud/AML (no tipping-off).
10. **Wording:**
    - TR: "Size ait olmayan bir para geldiyse harcamayın ve kimseye göndermeyin; iadeyi bankamız gönderen bankayla yürütür."
    - EN: "If money that isn't yours arrives, don't spend it or send it on. We'll handle the return with the sending bank."

### Gaps
- No official Turkish bank page on mistaken-credit handling was retrieved. Confirm the recall flow with team 07.

---

## 8. Statements (hesap özeti, hesap hareketleri/dökümü, e-ekstre; visa statements)

### Takeaway
Copies of documents are free for one year after issue, with a reasonable fee after that. Statement requests that need research are free for the first year back. The CBRT's January 2026 instruction allows fees for reference letters, visa and school letters, account research and statements. E-signed, QR-coded statements are increasingly used for visas.

### Cited Findings
- **Copy fees** [L-TR] (CBRT Communiqué 2020/7; RG 7/3/2020 No. 31061; amended 31/12/2020, 9/8/2021, 13/11/2021, 25/11/2023, 22/12/2023): documents given at the time of a transaction are free. Copies are free in the first year after issue, then a proportionate fee after informing the customer ([S14 art. 9(3)–(4)](https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5)).
- **Statement and letter fees** [L-TR] (CBRT Instruction, version 13 Jan 2026):
  - fees are allowed for reference letters, visa and private-school letters, account research and statement provision;
  - instant statement requests that need deposit research are free for the first year back;
  - archive-research fees may differ by channel ([S15](https://www.tcmb.gov.tr/wps/wcm/connect/9fcd654e-65a7-4c42-8292-06ec3846e751/2023-39+say%C4%B1l%C4%B1+FT+Tebli%C4%9Fi+Uygulama+Talimat%C4%B1+-13+Ocak+2026.pdf?MOD=AJPERES)).
- **Retention and complaints** [GOV: BDDK]:
  - documents are kept 10 years ([S17](https://www.bddk.org.tr/Sss/Liste/114));
  - complaints are answered within 1 month (20 days for cards);
  - next steps: the bank associations' consumer arbitration committees (TBB/TKBB Bireysel Müşteri Hakem Heyeti) or BDDK ([S18](https://www.bddk.org.tr/Sss/Liste/111)).
- **E-signed statements** [BANK: Yapı Kredi]: e-signed, QR-coded statements from a branch or the app ("Hesap Hareketleri E-İmzalı Olarak Gönder" → sent by e-mail). Listed "agreed institutions": consulates of Hungary, the UK, Greece and Germany, and the AS VISA and KOSMOS visa centers. Verified by scanning the QR code ([S29](https://www.yapikredi.com.tr/bireysel-bankacilik/odemeler-ve-hizmetler/e-imzali-belge-sorgulama)).

**Terms**
- **hesap özeti**: account statement.
- **hesap hareketleri / dökümü**: transaction history or listing.
- **ekstre**: mainly the card statement.
- **dekont**: transaction receipt.
- **kaşeli-imzalı**: stamped and signed.
- **e-imzalı / QR kodlu**: e-signed / QR-coded.

### Inferences
#### 10-point handling guide
1. **Why:** statement missing or wrong; historical statements for court, tax or divorce; visa.
2. **Experience:** "ekstrem gelmedi" (my statement didn't arrive), "3 aylık kaşeli döküm lazım" (I need a stamped 3-month statement), "vize için ıslak imzalı mı olmalı?" (does it need a wet signature for the visa?).
3. **Provide:** period, account, purpose, receiving institution.
4. **Determine:** whether the period is within 1 year; which channel; whether the recipient needs a wet stamp or accepts e-signed.
5. **Questions:**
   - "Hangi tarih aralığı?" (Which date range?)
   - "Belge hangi kuruma verilecek?" (Which institution is it for?)
   - "Kurum e-imzalı belgeyi kabul ediyor mu?" (Does it accept e-signed documents?)
6. **Checks:** e-statement settings and the e-mail on file [AUTH][VERIFY].
7. **Resolution:** self-service download; e-signed statement; branch stamped copy; archive request with the fee disclosed first.
8. **Must not:** promise consulate acceptance; send to an unverified e-mail; waive fees without authority.
9. **Escalate:** disputed entries → payments or disputes team; old archives → back office [HUMAN].
10. **Wording:**
    - TR: "Son bir yıla ait hareketleriniz ücretsizdir; daha eski dönemler için arşiv ücreti uygulanabilir ve işlem öncesi bildirilir."
    - EN: "The last year is free. Older periods may carry an archive fee, which we'll tell you before processing."

### Gaps
- Bank fee amounts and consulates' current acceptance of e-signed statements were not verified.

---

## 9. Account closure (hesap kapatma)

### Takeaway
Accounts are closed at a branch, or digitally at some banks. The CBRT list of chargeable services has no closure-fee item, and only listed fees may be charged, so closure should be free [VERIFY]. Blockers include a non-zero balance, holds, linked products and the joint-account mandate.

### Cited Findings
- **Channels** [GOV: BDDK]: closure is at branches and, depending on the bank, via internet, mobile or phone. e-Devlet results may lag by a day ([S16](https://www.bddk.org.tr/Sss/Liste/126)).
- **Fees** [L-TR]: only services listed in Ek-1 (the annex of chargeable services) may be charged, plus third-party costs ([S14 art. 6(1)](https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5)). The Ek-1 list in the 2026 instruction has no closure item ([S15](https://www.tcmb.gov.tr/wps/wcm/connect/9fcd654e-65a7-4c42-8292-06ec3846e751/2023-39+say%C4%B1l%C4%B1+FT+Tebli%C4%9Fi+Uygulama+Talimat%C4%B1+-13+Ocak+2026.pdf?MOD=AJPERES)).
- **Loan accounts and safe-deposit boxes** [L-TR] ([S14 arts. 11(7), 14(3)](https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5)):
  - a loan-only account is free and closes automatically on repayment, unless the customer asks otherwise in writing;
  - a safe-deposit box deposit is capped at 1 year's rent and refunded immediately at termination, minus damage or unpaid rent.
- **Joint accounts**:
  - [BANK: Ziraat] in a teselsüllü (either-holder) account any holder can close it alone; a teselsülsüz (joint-signature) account needs all signatures ([S23](https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf)).
  - [BANK: Akbank] a müşterek account needs everyone's consent; a münferit account can be closed by one holder; agree the split of funds first ([S24](https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay)).
- **Real wording** [ANEC]: "Vadesiz hesabımın kapatılmaması" — my current account wasn't closed after an app request ([S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)).

### Inferences
#### 10-point handling guide
1. **Why:** switching banks; unused account; dissatisfied; salary account after a job change; the bank closed the account.
2. **Experience:** "hesabı kapatamıyorum" (I can't close my account), "talebim işleme alınmadı" (my request wasn't processed), "kapatma ücreti kesildi" (I was charged a closure fee).
3. **Provide:** which accounts; where the balance should go.
4. **Determine:**
   - balance, including interest and time-deposit maturity;
   - holds or haciz;
   - linked cards, KMH, loans, automatic payments, investments, safe-deposit box;
   - joint-account type;
   - whether it is a salary account under an employer agreement [VERIFY].
5. **Questions:**
   - "Bağlı otomatik ödeme/kart/KMH var mı?" (Any linked automatic payments, cards or overdraft?)
   - "Bakiye hangi hesaba aktarılsın?" (Which account should the balance go to?)
6. **Checks:** product-linkage view [AUTH].
7. **Resolution:**
   - Move standing orders.
   - Repay the overdraft.
   - Transfer the balance to the customer's own account.
   - Close digitally or at a branch.
   - Give written confirmation.
8. **Must not:**
   - close an account under a legal hold;
   - pay the balance to third parties;
   - mention or charge unlisted fees;
   - close a joint-signature account on one holder's request.
9. **Escalate:**
   - unprocessed requests → back office;
   - fee disputes → Complaints or the Hakem Heyeti;
   - bank-initiated closures → relationship owner or Compliance.
10. **Wording:**
    - TR: "Kapatmadan önce otomatik ödeme talimatlarınızı başka hesaba taşıyın; aksi halde ödemeleriniz gerçekleşmeyebilir."
    - EN: "Please move automatic payments before closing, otherwise they may fail."

### Gaps
- No explicit "no closure fee" line was found in the TBB İzahname (the banking association's fee disclosure) [VERIFY].
- Moving salary accounts under employer promotion agreements was not researched.

---

## 10. Joint accounts, ownership; minors' accounts and guardians

### Takeaway
There are two kinds of Turkish joint account:
- **teselsüllü / münferit ("veya" — "or")**: either holder can act alone; only this type works for ATM and digital use.
- **teselsülsüz / müşterek ("ve" — "and")**: all holders must sign together.

If holders' shares were not declared, they are treated as equal on garnishment or death. Parents and guardians run minors' accounts within the limits of the Civil Code (TMK).

### Cited Findings
- **Either-holder account** [BANK: Ziraat] (teselsüllü):
  - each holder alone may withdraw, give instructions, close the account or move it;
  - the bank has lien and set-off rights over the whole account for any holder's debts;
  - a notice sent to one holder counts for all.
- **Joint-signature account** [BANK: Ziraat] (teselsülsüz): joint signatures only ([S23](https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf)).
- **ATM and digital use** [BANK: İş Bankası]: ATM and digital transfers need a teselsüllü account. Teselsülsüz accounts need all parties at the branch, or their attorneys (blog, 27 Dec 2024) ([S25](https://www.isbank.com.tr/blog/ortak-hesap-nedir)).
- **Tax and death** [BANK: Akbank]: deposit-interest tax is withheld and borne equally by the holders. On a holder's death, the share goes to the heirs and the account may be blocked until the process ends ([S24](https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay)).
- **Minors and guardians** [L-TR] ([S11 TMK arts. 357, 359, 462](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf)):
  - parents may not use for themselves the income from gifts made to a child's savings;
  - the child manages its own earnings;
  - a guardian needs approval for acts such as lending, borrowing and bills of exchange.
- **US comparison** [L-US]: with rights of survivorship the money passes to the survivors; with tenants in common the deceased's share goes to the heirs. Check the account agreement (CFPB, reviewed 28 Aug 2026) ([S50](https://www.consumerfinance.gov/ask-cfpb/what-happens-to-a-bank-account-when-someone-dies-en-1101/)).

### Inferences
#### 10-point handling guide
1. **Why:** add or remove a holder; "my partner emptied the account"; separation; another holder's debt froze the account; a child's limits.
2. **Experience:** "ortağım tüm parayı çekti" (my co-holder withdrew everything), "eşimin borcu yüzünden hesabımız bloke" (our account is blocked because of my spouse's debt).
3. **Provide:** relationship and claimed share.
4. **Determine:** and/or type; declared shares; holds; the caller's role.
5. **Questions:**
   - "Hesap 've' mi 'veya' mı?" (Is it an "and" or an "or" account?)
   - "Hissenizi açılışta bildirdiniz mi?" (Did you declare your share when the account was opened?)
6. **Checks:** mandate and signatories [AUTH/HUMAN].
7. **Resolution:** explain how the mandate works. Changes to holders need all parties at a branch [VERIFY]. Stopping an "or" holder needs a court or enforcement order ([S23](https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf)).
8. **Must not:** disclose one holder's other accounts; take sides; freeze the account at one holder's request.
9. **Escalate:** abuse or coercion → vulnerable-customer team (team 11); legal disputes → Legal.
10. **Wording:**
    - TR: "'Veya' hesapta her sahip tek başına işlem yapabilir; durdurmak için mahkeme veya icra kararı gerekir."
    - EN: "In an 'or' account each holder can act alone. Stopping this needs a court or enforcement order."

### Gaps
- Whether a holder can be removed digitally, and how retail authorized users are handled, is not documented [VERIFY].

---

## 11. Name changes (marriage/divorce) and ID renewal

### Takeaway
Many banks update names automatically from KPS/MERNİS. Some still require a branch visit (anecdotal, 2026). When records don't match, customers see the old surname on transfers, cards printed with the old name, or temporary restrictions.

### Cited Findings
- **Legal basis** [L-TR]: records must be kept current ([S9 art. 19](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)). KPS matching is part of identity checks ([S1 art. 7(7)(d)](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)), and identity data reaches institutions via KPS ([S13 art. 52](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5490.pdf)).
- **e-Devlet surname change** [GOV: e-Devlet]: an online surname-change application exists for married, widowed or divorced women (title only seen) ([S54](https://www.turkiye.gov.tr/nvi-evli-veya-bosanmis-kadinlarin-soyadi-degisikligi-basvurusu)).
- **Real complaints about Garanti BBVA** [ANEC] (2026, [S34](https://www.sikayetvar.com/garanti-bbva/soyadi-degisikligi)):
  - "Diğer tüm müşterisi olduğum bankalar bilgilerimi e-devletten çekerken…" — other banks pulled the data from e-Devlet, this one required a branch visit;
  - transfers showed the old surname;
  - the account was blocked until updated;
  - a new card carried the maiden name.

### Inferences
#### 10-point handling guide
1. **Why:** marriage, divorce, new ID card, name mismatch.
2. **Experience:** "soyadım güncellenmedi" (my surname wasn't updated), "EFT'de eski soyadım görünüyor" (transfers show my old surname), "kartım eski soyadımla geldi" (my card came with my old surname).
3. **Provide:** new name and the date of change.
4. **Determine:** whether KPS has synced; whether cards need reissuing.
5. **Questions:** "Nüfus kaydınız güncellendi mi?" (Has your civil registry record been updated?)
6. **Checks:** name in the core system versus on cards [AUTH/HUMAN].
7. **Resolution:** KPS refresh, or a branch visit with the new ID [VERIFY]; reissue cards; tell payers the new name.
8. **Must not:** change a name on the caller's word without a match in the ID system.
9. **Escalate:** foreign nationals with documents from abroad → branch or back office.
10. **Wording:**
    - TR: "Değişiklik nüfus kaydına işlendiyse sistemimize yansıtıp kartlarınızı yeni adınızla yenileyebiliriz."
    - EN: "Once the change is in the civil registry, we can update our records and reissue your cards."

### Gaps
- No official bank FAQ on name changes was found. Whether KPS sync is automatic or on request is unverified.

---

## 12. Power of attorney (vekaletname), representatives, guardianship

### Takeaway
Banks accept notarized powers of attorney whose wording covers the banking acts requested. The exact criteria are bank-specific. A POA made abroad comes either from a Turkish consulate or from a foreign notary with an Apostille. A guardian (vasi) has legal limits.

### Cited Findings
- **POAs from abroad** [GOV: MFA, NY Consulate 2024] ([S30](https://newyork-bk.mfa.gov.tr/Content/assets/consulate/images/localCache/1/0a75f4a8-8ec7-455d-bac6-50da5cc77502.pdf)):
  - consulates issue POAs;
  - a POA is valid indefinitely unless a term is set;
  - the attorney can obtain copies from Turkish notaries;
  - POAs made before foreign notaries need an Apostille.
- **Verifying representatives** [L-TR]: a representative's identity can be verified from a notarized POA or signature circular (imza sirküleri) that contains ID data ([S9 art. 14](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)). The customer must declare if acting for others ([S9 art. 17](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Joint accounts** [BANK: İş Bankası]: a party absent at joint-account opening can be represented by a notarized POA ([S25](https://www.isbank.com.tr/blog/ortak-hesap-nedir)).
- **POA lookup** [GOV: TNB]: e-Devlet "Kişi Vekaletnameleri Sorgulama" shows POAs held by the notaries' union (TNB) (login required) ([S31](https://www.turkiye.gov.tr/tnb-kisi-vekaletnameleri-sorgulama)).
- **Guardianship limits** [L-TR]: people under legal restriction (kısıtlılar) need their representative's consent. A guardian needs authority approval for lending or borrowing, bills of exchange, and transfers beyond ordinary management ([S11 arts. 16, 462](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf)).

### Inferences
#### 10-point handling guide
1. **Why:** acting for an elderly parent or someone abroad; a POA was refused; guardianship.
2. **Experience:** "vekaletnameyi kabul etmediler" (they didn't accept the power of attorney), "annem için para çekmem lazım" (I need to withdraw money for my mother).
3. **Provide:** POA date, notary, scope.
4. **Determine:**
   - whether the scope covers the requested act;
   - whether it was revoked (azilname);
   - whether the principal has died — the POA then ends [VERIFY];
   - for foreign POAs, whether there is an Apostille;
   - for a guardian, the court decision.
5. **Questions:**
   - "Vekaletnamede banka işlemleri açıkça yazıyor mu?" (Does the POA explicitly cover banking transactions?)
   - "Yurt dışında mı düzenlendi?" (Was it issued abroad?)
6. **Checks:** legal or branch review of the original [HUMAN].
7. **Resolution:** bring the original and both IDs to a branch; get a new POA if the scope is insufficient.
8. **Must not:** act on a POA presented by phone or chat; disclose data before the POA is validated.
9. **Escalate:** suspected financial abuse of a vulnerable principal → vulnerable-customer team and Fraud.
10. **Wording:**
    - TR: "Vekaletnamenin aslıyla şubemize geldiğinizde hukuk birimimiz kapsamını inceler."
    - EN: "Bring the original POA to a branch and our legal team will review its scope."

### Gaps
- Banks' criteria are not public [VERIFY]: whether the POA must be a düzenleme-type (fully notary-drafted) document rather than a signature-certified one, the maximum age of the POA, and the wording required.

---

## 13. Bereavement and deceased customers (vefat, mirasçı işlemleri)

### Takeaway
In Türkiye, heirs need four things:
- a mirasçılık belgesi or veraset ilamı (certificate of inheritance) from a notary or the court of peace;
- an inheritance-tax clearance letter (veraset ve intikal vergisi ilişik kesme yazısı), or acceptance of the bank's 5% withholding instead;
- usually, all heirs acting together, because heirs hold the estate jointly;
- a tax official present if a safe-deposit box is opened.

e-Devlet shows heirs which banks held the deceased's deposits. In the UK, banks are notified separately from Tell Us Once.

### Cited Findings
- **Certificate and joint ownership** [L-TR]: a notary or the court of peace issues the certificate of inheritance ([S11 art. 598](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf)). Heirs own the estate jointly (elbirliği) until it is divided, and a court may appoint a representative ([S11 art. 640](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf)).
- **Tax clearance and withholding** [L-TR]: banks ask for the tax office's certificate before paying heirs. If it is not produced, the bank **may** pay after withholding 5% (inheritance) or 15% (gifts), and must remit the withheld amount to the tax office within a week ([S12 VİVK art. 17](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.7338.pdf)).
- **Safe-deposit boxes** [L-TR]: a deceased holder's box opens only with a tax official present, unless the contents are recorded by a judge ([S12 art. 23](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.7338.pdf)).
- **Inheritance-tax rules for 2026** [GOV: GİB] ([S26](https://www.gib.gov.tr/vergi-konulari/1_bireysel/12_veraset_ve_intikal_vergisi/12)):
  - the return is due within 4 months of the death (6 months if heirs are abroad);
  - attach the certificate of inheritance and the bank's document;
  - filing is mandatory even below the exemption;
  - 2026 exemptions: 2,907,136 TL per child or spouse; 5,817,845 TL for a spouse who is the sole heir;
  - the clearance letter is issued after payment and has no expiry.
- **Heirs' bank lookup** [GOV: BDDK]: e-Devlet "Murise Ait Mevduat/Katılım Fonu Hesabı Bulunan Banka Sorgulama" lists the banks that held the deceased's deposits. It works once the heir's certificate is verified — court certificates issued after 16 Dec 2016, notary certificates after 2 Jun 2021. Balances must be requested from the banks ([S16](https://www.bddk.org.tr/Sss/Liste/126)).
- **Joint accounts on death** [BANK: Ziraat]: shares are deemed equal and the deceased's share is split off. Holders are liable for payments made before the bank learned of the death. Without a tax certificate the bank pays with statutory withholding ([S23](https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf)).
- **UK comparison**:
  - [GOV: UK] Tell Us Once covers government bodies only; banks are contacted separately ([S43](https://www.gov.uk/after-a-death/organisations-you-need-to-contact-and-tell-us-once)).
  - [IND: UK] the Death Notification Service is free and notifies several member firms at once. Firms with a live account reply within 10 working days ([S44](https://www.deathnotificationservice.co.uk/)).
- **US comparison** [L-US]: survivorship vs tenants-in-common rules apply to joint accounts ([S50](https://www.consumerfinance.gov/ask-cfpb/what-happens-to-a-bank-account-when-someone-dies-en-1101/)).

### Inferences
#### 10-point handling guide
1. **Why:** reporting a death; the deceased's card or salary is still active; heirs want funds or information; a joint survivor is blocked.
2. **Experience:** "babam vefat etti, hesapları nasıl kapatırız?" (my father died, how do we close his accounts?), "vefat blokesi konmuş" (a death block was placed), "kasayı açmamız lazım" (we need to open the safe-deposit box).
3. **Provide:** the deceased's name and TCKN, date of death, the caller's relationship.
4. **Determine:**
   - whether the caller is an heir or a co-holder;
   - whether the death is recorded — banks may learn from KPS [VERIFY];
   - products held: deposits, loans, cards, automatic payments, safe-deposit box.
5. **Questions:**
   - "Mirasçılık belgesi aldınız mı?" (Have you obtained the certificate of inheritance?)
   - "Tüm mirasçılar birlikte mi başvuracak?" (Will all heirs apply together?)
6. **Checks:** deceased-accounts unit; a balance letter as at the date of death, for the tax return [HUMAN].
7. **Resolution:**
   1. Obtain the certificate of inheritance.
   2. Get a balance letter from the bank.
   3. File the inheritance-tax return and pay it, or accept the 5% withholding.
   4. All heirs, or their attorneys, attend.
   5. Open the safe-deposit box with a tax official present.
8. **Must not:**
   - disclose balances before heir status is verified;
   - suggest using the deceased's card or app;
   - estimate the tax.
9. **Escalate:**
   - disputes between heirs → Legal;
   - card used after the death → Fraud;
   - distressed caller → bereavement specialist (team 11).
10. **Wording:**
    - TR: "Başınız sağ olsun. Hesap bilgilerini mirasçılık belgesi ibrazından sonra paylaşabiliyoruz; size adım adım neler gerektiğini anlatayım."
    - EN: "I'm very sorry for your loss. We can share account details once a certificate of inheritance is provided. Let me walk you through the steps."

### Gaps
- Paying heirs individually versus jointly is bank- and case-specific [VERIFY].
- How banks learn of deaths is not public.
- UK bank thresholds for releasing funds without probate were not collected.

---

## 14. Business/corporate account basics a retail agent may meet

### Takeaway
A company's identity rests on trade-registry and tax records, its authorized signatories (imza sirküleri, the notarized signature circular) and any beneficial owner above 25%. Since 2023 companies can onboard remotely. Retail agents should identify company requests and route them to commercial or SME banking.

### Cited Findings
- **Company identification** [L-TR]: the bank records title, registry number, tax number, activity, address and contacts, plus the representatives' identity and signatures. It verifies these against registry and GİB (tax authority) documents and the TOBB (chamber union) or registry database ([S9 art. 7](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Instructions and owners** [L-TR]: written instructions can be checked against a notarized signature circular ([S9 art. 7(7)](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)). Owners above 25% are identified as beneficial owners ([S9 art. 17/A](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf)).
- **Remote corporate onboarding** [L-TR]: authority to represent the company is checked against MERSİS (the central trade registry system) and the Trade Registry Gazette. The signature circular is checked by its date and journal number, company data against GİB, and beneficial owners are identified ([S1 arts. 7/A–7/C](https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf)).
- **Corporate internet banking** [BANK: Ziraat]: the customer applies at a branch; the password arrives by SMS ([S19](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi)).

### Inferences
#### 10-point handling guide
1. **Why:** signatory changes; corporate internet-banking roles (maker/approver [VERIFY Turkish terms]); company changes; sole-trader (şahıs firması) and personal accounts mixed up.
2. **Experience:** "şirket yetkilisi değişti" (the company's authorized person changed), "kurumsal internet şubesine giremiyorum" (I can't log in to corporate internet banking).
3. **Provide:** company name, tax number, the caller's role.
4. **Determine:** whether the caller is a signatory; whether the customer is retail or commercial.
5. **Questions:** "Şirket adına imza yetkiniz var mı?" (Are you authorized to sign for the company?)
6. **Checks:** signatory mandate [HUMAN].
7. **Resolution:** route to the commercial/SME channel with the current registry gazette and signature circular [VERIFY].
8. **Must not:** change signatories by phone; disclose company data to non-signatories.
9. **Escalate:** commercial banking or the corporate digital desk; disputes between partners → Legal.
10. **Wording:**
    - TR: "Şirket hesaplarındaki yetki değişiklikleri güncel ticaret sicil gazetesi ve imza sirküleri ile ticari/KOBİ ekibimizce yapılır."
    - EN: "Signatory changes are handled by our commercial/SME team, using the current registry gazette and signature circular."

### Gaps
- Corporate role names and rules for changing them are bank-specific.

---

## 15. Verification and reference letters, proof of funds, tax documents (stopaj), FX documents

### Takeaway
Reference letters, visa and school letters, and account research are chargeable services under the CBRT 2026 instruction. Withholding tax (stopaj) on deposit interest is deducted at source. Its rates are set by Presidential Decision and change often; the current rates were extended to 31/12/2026.

### Cited Findings
- **Letter fees** [L-TR]: fees are allowed for reference, visa and school letters, account research and statements ([S15](https://www.tcmb.gov.tr/wps/wcm/connect/9fcd654e-65a7-4c42-8292-06ec3846e751/2023-39+say%C4%B1l%C4%B1+FT+Tebli%C4%9Fi+Uygulama+Talimat%C4%B1+-13+Ocak+2026.pdf?MOD=AJPERES)). A one-time "borcu yoktur" (no-debt) letter for a loan is free ([S17](https://www.bddk.org.tr/Sss/Liste/114)).
- **Withholding rates** [L-TR, specialist source]: Presidential Decision 11444 (RG 20/6/2026 No. 33286) extended the TL deposit withholding rates to 31/12/2026 ([S39](https://www.yontemymm.com.tr/mali-aciklamalar/2026-041-tl-mevduat-hesaplarinda-uygulanan-stopaj-oranlarinin-suresi-uzatildi)). **These change periodically — verify in the Resmî Gazete before quoting.**

  | Account | Withholding rate |
  |---|---|
  | Demand accounts and terms up to 6 months | 17.5% |
  | Terms up to 1 year | 15% |
  | Terms over 1 year | 10% |

- **Withholding on joint accounts** [BANK: Akbank]: the bank withholds the tax; joint holders bear it equally ([S24](https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay)).

### Inferences
#### 10-point handling guide
1. **Why:** a consulate or employer needs a letter; proof of funds; tax filing; FX transfer documents.
2. **Experience:** "banka referans mektubu" (bank reference letter), "hesap teyit yazısı" (account confirmation letter), "stopaj dökümü" (withholding statement), "vize için bakiye yazısı" (balance letter for a visa).
3. **Provide:** purpose, recipient, language, deadline.
4. **Determine:** document type; fee disclosure; whether TR or EN is needed.
5. **Questions:**
   - "Yazı hangi dilde, kime hitaben?" (Which language, and addressed to whom?)
   - "Belirli tarih itibarıyla bakiye mi gerekiyor?" (Do you need the balance as at a specific date?)
6. **Checks:** account and holders [AUTH].
7. **Resolution:** request at a branch or digitally; interest and withholding listings from internet banking [VERIFY].
8. **Must not:**
   - give tax advice;
   - quote stopaj rates without checking the current Decision;
   - issue letters to third parties without the customer's instruction.
9. **Escalate:** embassy templates and FX-transfer documentation → branch or FX desk [HUMAN].
10. **Wording:**
    - TR: "Referans/vize mektubu ücrete tabi olabilir; ücret işlem öncesi bildirilir."
    - EN: "Reference and visa letters may carry a fee, which we'll confirm before processing."

### Gaps
- FX-account document rules and FX taxes were not researched (teams 07 and 09).
- Bank letter fees were not collected.

---

## 16. Source-of-funds and AML document requests — what the agent can and cannot say

### Takeaway
The agent may say that the bank must understand the purpose of the relationship and where the funds come from, and may list the documents requested. It must never state or imply that an STR has been filed, that MASAK has suspended a transaction, or that there is an investigation.

### Cited Findings
- **Legal duties** [L-TR]:
  - the bank must ask about purpose and nature ([S9 art. 5(3)](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf));
  - it monitors activity against the customer's profile and source of funds ([S9 art. 19](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf));
  - it ends the relationship if re-verification fails ([S9 art. 22](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf));
  - tipping-off is prohibited ([S9 art. 29](https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf); [S8 art. 4(2)](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf));
  - MASAK can suspend a transaction for 7 working days ([S8 art. 19/A](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)).
- **UK and US** [L-UK]/[L-US]: equivalent rules apply ([S48](https://www.legislation.gov.uk/ukpga/2002/29/section/333A); [S49](https://www.law.cornell.edu/uscode/text/31/5318)).
- **Lending an account** [L-TR]: handing over account access for fraud counts as participation in fraud ([S10 TCK 158(4)](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5237.pdf)).
- **Real wording** [ANEC]: customers insist they made no illegal transactions and cite legal betting sites ([S33](https://www.sikayetvar.com/hesap-bloke/supheli-islem)).

### Inferences
#### 10-point handling guide
1. **Why:** the bank requested documents (payslip, sale deed, invoices); channels were restricted after a large inflow.
2. **Experience:** "paranın kaynağını soruyorlar" (they're asking where the money came from), "neden belge istiyorsunuz?" (why do you want documents?), "MASAK mı inceliyor?" (is MASAK investigating?).
3. **Provide:** explanation of the funds.
4. **Determine:** which documents are requested, the deadline and the upload channel [AUTH].
5. **Questions:** "Belgeleri hangi kanaldan iletebilirsiniz?" (Through which channel can you send the documents?)
6. **Checks:** case status only — frontline staff don't see AML detail [HUMAN].
7. **Resolution:** collect documents through a secure channel or at a branch; a specialist team reviews them.
8. **Must not:**
   - confirm or deny MASAK, an STR or an investigation;
   - call it "routine" without knowing;
   - predict the outcome;
   - suggest moving or splitting funds;
   - edit documents.
9. **Escalate:** all AML requests → Compliance/FCC operations; threats or distress → supervisor.
10. **Wording:**
    - TR: "Yasal yükümlülüklerimiz gereği işlemlerin amacı ve fon kaynağına ilişkin bilgi ve belge talep edebiliyoruz. Değerlendirme ilgili birimimizce yapılır; süreç ayrıntısı paylaşamıyoruz."
    - EN: "Under our legal obligations we may ask for information about the purpose of transactions and the source of funds. A specialist team reviews them, and I can't share process details."

### Gaps
- MASAK's 2025–2026 guidance on typologies (illegal betting, account renting) was not retrieved (team 10).

---

## Source register

Access date for all sources: 2026-10-10. "Undated" means no date was shown on the page.

| ID | Title | Publisher | Date | Jur. | URL |
|---|---|---|---|---|---|
| S1 | Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik (consolidated) | BDDK via mevzuat.gov.tr | RG 1/4/2021 No. 31441; amended 6/4/2022 No. 31801, 25/5/2023 No. 32201 | TR | https://www.mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.38568.pdf |
| S2 | 5411 Bankacılık Kanunu (arts. 62, 73) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf |
| S3 | Zamanaşımına İlişkin Sıkça Sorulan Sorular | TMSF | undated | TR | https://www.tmsf.org.tr/tr/Tmsf/Mevduat/zamanasimi.sorular |
| S4 | Bu Yıl TMSF'ye Devredilecek Hesaplara İlişkin Sorgulama | e-Devlet/TMSF | undated (login) | TR | https://www.turkiye.gov.tr/tmsf-zamanasimi-hesaplari-sorgulama |
| S5 | 2004 İcra ve İflas Kanunu (arts. 83, 83/a, 89) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf |
| S6 | 6183 AATUHK (art. 79) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.3.6183.pdf |
| S7 | 5510 SS ve GSS Kanunu (art. 93) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5510.pdf |
| S8 | 5549 Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun (arts. 4, 8, 19/A) | mevzuat.gov.tr | consolidated (to 2024) | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf |
| S9 | Suç Gelirlerinin Aklanmasının ve Terörün Finansmanının Önlenmesine Dair Tedbirler Hakkında Yönetmelik | mevzuat.gov.tr | consolidated incl. CK 9305 (RG 25/12/2024), CK 10945 (RG 13/2/2026), CK 11845 (RG 7/10/2026) | TR | https://www.mevzuat.gov.tr/MevzuatMetin/21.5.200713012.pdf |
| S10 | 5237 Türk Ceza Kanunu (arts. 158(4), 160) | mevzuat.gov.tr | consolidated incl. Law 7589 (in force 31/7/2026) | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5237.pdf |
| S11 | 4721 Türk Medeni Kanunu (arts. 11, 12, 16, 357, 359, 462, 598, 640) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4721.pdf |
| S12 | 7338 Veraset ve İntikal Vergisi Kanunu (arts. 17, 23) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.3.7338.pdf |
| S13 | 5490 Nüfus Hizmetleri Kanunu (arts. 50–52) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5490.pdf |
| S14 | Finansal Tüketicilerden Alınacak Ücretlere İlişkin Usul ve Esaslar Hakkında Tebliğ (2020/7) | TCMB via mevzuat.gov.tr | RG 7/3/2020 No. 31061; last amended RG 22/12/2023 | TR | https://mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=34343&mevzuatTur=Teblig&mevzuatTertip=5 |
| S15 | Tebliğ (2020/7) Uygulama Talimatı | TCMB | version 13 Jan 2026 | TR | https://www.tcmb.gov.tr/wps/wcm/connect/9fcd654e-65a7-4c42-8292-06ec3846e751/2023-39+say%C4%B1l%C4%B1+FT+Tebli%C4%9Fi+Uygulama+Talimat%C4%B1+-13+Ocak+2026.pdf?MOD=AJPERES |
| S16 | SSS: eDevlet Mevduat/Katılım Fonu Hesabı Bulunan Banka Sorgulama | BDDK | undated | TR | https://www.bddk.org.tr/Sss/Liste/126 |
| S17 | SSS: Bireysel Müşterilere İlişkin Ücretler | BDDK | undated | TR | https://www.bddk.org.tr/Sss/Liste/114 |
| S18 | SSS: Kurum ve Banka Uygulamalarına İlişkin Diğer Sorunlar | BDDK | undated | TR | https://www.bddk.org.tr/Sss/Liste/111 |
| S19 | İnternet Bankacılığı SSS | Ziraat Bankası | undated | TR | https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/internet-bankaciligi |
| S20 | Bilgi Güncelleme SSS | QNB | undated | TR | https://www.qnb.com.tr/sss/bilgi-guncelleme |
| S21 | SIM Kart Değişikliği | Garanti BBVA | undated | TR | https://www.garantibbva.com.tr/dijital-bankacilik/sim-kart-degisikligi |
| S22 | SIM blokesi sebebiyle giriş yapamıyorum | e-Devlet | undated | TR | https://www.turkiye.gov.tr/iletisim?hizli=CozumMerkeziV2&nodeId=355 |
| S23 | Teselsüllü Müşterek Hesap Sözleşmesi / Teselsülsüz Küşat Mektubu (ZBFRM-00226/00229) | Ziraat Bankası | undated | TR | https://www.ziraatbank.com.tr/tr/Contracts/MusterekHesapSozlesmeleriveMektubu.pdf |
| S24 | Ortak Hesap Hakkında Bilmeniz Gereken 8 Detay | Akbank (blog) | 3 Sep 2025 | TR | https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay |
| S25 | Ortak Hesap Nedir? | İş Bankası (blog) | 27 Dec 2024 | TR | https://www.isbank.com.tr/blog/ortak-hesap-nedir |
| S26 | Veraset ve İntikal Vergisi | GİB | 2026 figures | TR | https://www.gib.gov.tr/vergi-konulari/1_bireysel/12_veraset_ve_intikal_vergisi/12 |
| S27 | e-Haciz nedir? | Enpara (knowledge base) | undated | TR | https://www.enpara.com/bilgi-bankasi/e-haciz-nedir |
| S28 | Banka Hesaplarına Uygulanan Elektronik Haciz Sorgulama | e-Devlet/GİB | undated (login) | TR | https://www.turkiye.gov.tr/gib-intvrg-banka-hesaplarina-uygulanan-elektronik-haciz-sorgulama |
| S29 | e-İmzalı Hesap Hareketi Sorgulama | Yapı Kredi | undated | TR | https://www.yapikredi.com.tr/bireysel-bankacilik/odemeler-ve-hizmetler/e-imzali-belge-sorgulama |
| S30 | Vekâletname Başvurusu (information sheet) | T.C. New York Başkonsolosluğu (MFA) | 2024 | TR/US | https://newyork-bk.mfa.gov.tr/Content/assets/consulate/images/localCache/1/0a75f4a8-8ec7-455d-bac6-50da5cc77502.pdf |
| S31 | Kişi Vekaletnameleri Sorgulama | e-Devlet/TNB | undated (login) | TR | https://www.turkiye.gov.tr/tnb-kisi-vekaletnameleri-sorgulama |
| S32 | Yaygın Dolandırıcılık Türleri | Ziraat Bankası | undated | TR | https://www.ziraatbank.com.tr/tr/dijital-bankacilik/guvenlik/yaygin-dolandiricilik-turleri |
| S33 | "hesap bloke, şüpheli işlem" listing (anecdotal) | Şikayetvar | entries Sep–Oct 2026 | TR | https://www.sikayetvar.com/hesap-bloke/supheli-islem |
| S34 | Garanti BBVA soyadı değişikliği complaints (anecdotal) | Şikayetvar | 2026 | TR | https://www.sikayetvar.com/garanti-bbva/soyadi-degisikligi |
| S35 | "hesaba yanlış para gelirse ne yapılmalı" (anecdotal; title only) | Ekşi Sözlük | undated | TR | https://eksisozluk.com/hesaba-yanlis-para-gelirse-ne-yapilmali--7038043 |
| S36 | İlk İmza Hesabı | İş Bankası | undated | TR | https://www.isbank.com.tr/ilk-imza-hesabi |
| S37 | Çocuklar için tasarruf hesabı (search extract) | Enpara | undated | TR | https://www.enpara.com/bilgi-bankasi/cocuklar-icin-tasarruf-birikim-hesabi |
| S38 | Provizyon Nedir? | Türkiye Finans (blog) | undated | TR | https://www.turkiyefinans.com.tr/tr-tr/blog/sayfalar/provizyon-nedir.aspx |
| S39 | 2026/041 TL mevduat stopaj oranlarının süresi uzatıldı (CK 11444) | Yöntem YMM (specialist) | Jun 2026 | TR | https://www.yontemymm.com.tr/mali-aciklamalar/2026-041-tl-mevduat-hesaplarinda-uygulanan-stopaj-oranlarinin-suresi-uzatildi |
| S40 | 7589 Sayılı Kanun Yayımlandı – Özet ve SSS | Alomaliye (specialist press) | 31 Jul 2026 | TR | https://www.alomaliye.com/2026/07/31/7589-sayili-kanun-yayimlandi-ozet-ve-sss/ |
| S41 | Banka Hesabı (foreign researchers) | İTÜ Global | undated | TR | https://global.itu.edu.tr/tr/uluslararasi-akademisyenler/sozlesmesiz-misafir-arastirmacilar/banka-hesabi |
| S42 | Yabancıların Banka Hesabı Açması | Wise (secondary) | undated | TR | https://wise.com/tr/blog/yabancilar-banka-hesabi |
| S43 | Organisations you need to contact and Tell Us Once | GOV.UK | undated | UK | https://www.gov.uk/after-a-death/organisations-you-need-to-contact-and-tell-us-once |
| S44 | Death Notification Service | DNS (industry) | undated | UK | https://www.deathnotificationservice.co.uk/ |
| S45 | Dormant Assets Scheme strategy | HM Government | 2 Jun 2025 | UK | https://www.gov.uk/government/publications/dormant-assets-scheme-strategy |
| S46 | Dormant accounts | NatWest | undated | UK | https://www.natwest.com/current-accounts/dormant-accounts.html |
| S47 | Millions of people and businesses protected against debanking | HM Treasury | 28 Apr 2025 | UK | https://www.gov.uk/government/news/millions-of-people-and-businesses-protected-against-debanking |
| S48 | Proceeds of Crime Act 2002 s.333A | legislation.gov.uk | current | UK | https://www.legislation.gov.uk/ukpga/2002/29/section/333A |
| S49 | 31 U.S.C. § 5318(g)(2) | LII/Cornell | current | US | https://www.law.cornell.edu/uscode/text/31/5318 |
| S50 | Joint account when an owner dies | CFPB | reviewed 28 Aug 2026 | US | https://www.consumerfinance.gov/ask-cfpb/what-happens-to-a-bank-account-when-someone-dies-en-1101/ |
| S51 | Inactive/unclaimed accounts | OCC HelpWithMyBank | reviewed Apr 2021 | US | https://helpwithmybank.gov/help-topics/bank-accounts/opening-closing-inactive-bank-accounts/inactive-accounts/inactive-unclaimed.html |
| S52 | Denied a checking account because of a report | CFPB | reviewed 18 Dec 2024 | US | https://www.consumerfinance.gov/ask-cfpb/i-was-denied-a-checking-account-because-of-a-report-what-can-i-do-en-1113/ |
| S53 | Can a debt collector take my Social Security or VA benefits? | CFPB | reviewed 29 Jan 2024 | US | https://www.consumerfinance.gov/ask-cfpb/can-a-debt-collector-take-my-social-security-or-va-benefits-en-1157/ |
| S54 | Evli/Dul veya Boşanmış Kadınların Soyadı Değişikliği Başvurusu (title only) | e-Devlet/NVİ | undated | TR | https://www.turkiye.gov.tr/nvi-evli-veya-bosanmis-kadinlarin-soyadi-degisikligi-basvurusu |

---

## Open questions / unverified items / needs institution-specific confirmation

1. **Very recent changes:**
   - MASAK regulation CK 11845 (RG 7/10/2026): new CDD thresholds and the signature waiver. Confirm when banks implement them.
   - TCK 158(4) (Law 7589, in force 31/7/2026). Confirm with Legal how frontline staff should mention it.
2. **Values that change periodically — re-check before use:**
   - stopaj rates (valid to 31/12/2026);
   - 2026 inheritance-tax exemptions;
   - MASAK thresholds;
   - the TMSF 250 TL notice threshold (not confirmed as current);
   - the CBRT instruction version.
3. **"No closure fee"** is inferred from the Ek-1 list. Confirm in the TBB İzahname and each bank's fee schedule.
4. **Garnishment of salaries and pensions in practice** (1/4 floor, SGK pension consent, Yargıtay practice on salary money once deposited) needs Legal confirmation.
5. **Fraud holds on receiving accounts:** the Turkish legal basis and maximum duration are not established.
6. **Remote onboarding for foreigners:** secondary sources conflict with the BDDK regulation. Confirm with each bank.
7. **After a phone or e-mail change:** cooling-off periods, payee limits and alerts to the old contact are bank-internal. Confirm.
8. **Heirs:** whether payout is individual or joint, and how banks learn of a death, are bank-specific.
9. **Powers of attorney:** acceptance criteria, and the effect of the principal's death or incapacity, need Legal confirmation.
10. **EU Payment Accounts Directive** (basic account right, reasons for refusal): not verified because EUR-Lex blocked retrieval. Defer to team 03.
11. **UK debanking rules (90-day notice):** confirm commencement. Only the April 2025 announcement was verified.
12. **No frequency statistics** were collected or invented. Complaint volumes belong to team 04.
