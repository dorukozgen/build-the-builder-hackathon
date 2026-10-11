# Card Support (debit, credit, prepaid, virtual, supplementary) — Researcher 06 notes

Date context: research done 2026-10-10. Türkiye is primary; EU/UK/US are given only for comparison. Pages marked "undated" had no visible publication date and were accessed on 2026-10-10. "Snippet" means only the search-result excerpt could be read, not the full page.

Tag legend used on every claim: **[L-TR] / [L-EU] / [L-UK] / [L-US]** law or regulation (by jurisdiction) · **[S]** card-scheme rule or common industry practice · **[B: Bank]** policy of one named bank · **[R]** recommended service practice (my synthesis, no source needed) · **[V]** assumption that needs verification. Values that change from time to time (limits, fees, ratios) are marked **(periodic)**.

Hand-offs: law detail goes to researcher 02 (TR) and 03 (EU/UK/US); fee and interest values to 09; fraud and scams to 10; app, login and OTP-channel faults to 08; complaint routing to 04; tone and vulnerable customers to 11.

---

## 1. Transaction lifecycle in the four-party model (authorization → clearing → settlement; holds; reversal vs refund vs chargeback; offline)

### Takeaway
Card payments are authorized in real time. The issuer then places a hold (TR: *provizyon*, "bekleyen işlem") that reduces the available balance or limit. Clearing and settlement through the acquirer and the scheme happen later. Most "charged twice", "wrong amount" and "refund missing" contacts come from timing or matching gaps between the hold and the cleared item, so the agent's first step is always to separate pending items from posted ones. How long a hold stays valid is set by scheme rules (Visa: 5–30 days depending on the environment). When an unmatched hold is released is issuer practice. Turkish banks publish only typical posting times (1–3 business days), and I found no regulatory deadline for releasing a hold.

### Cited Findings
- **Parties.** Disputes run between the cardholder's bank (issuer) and the bank the merchant contracts with (acquirer); the issuer asks the merchant's bank for documents [S][B: İş Bankası] — [İş Bankası, Chargeback (08.08.2024)](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir). Once checks finish, a provisioned amount is transferred to the seller's bank and booked as debt on the card [B: Akbank] — [Akbank, Provizyon (10.07.2025)](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek). TROY is a card scheme set up and run by Bankalararası Kart Merkezi (BKM); BKM is owned by Turkish banks with TCMB as majority shareholder [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular).
- **Authorization hold.** When an authorization is approved, the issuer "typically reduces the amount available to the cardholder … commonly known as an authorization hold" [S] — [Visa, Estimated & Incremental Authorization and Reversal Processing (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf).
- **Estimated and incremental authorization (hotels, car rental, fuel, tips).** Under Visa rules any merchant may use an estimated authorization when the final amount is unknown. It must be a genuine estimate, the merchant must tell the cardholder it is an estimate, and it "must not contain incidental spend amounts such as tips or a buffer for damage". If the cardholder spends more, the merchant adds an incremental authorization. If the final amount is lower, the merchant must send a partial reversal [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf).
- **Reversal timing.** If a transaction will not complete, the merchant must reverse the whole authorized amount within 24 hours of knowing that, or at the end of the validity period. If the final amount is below the authorized total, the merchant must reverse the difference within 24 hours of completion [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf).
- **Visa validity windows for estimated authorizations:** lodging, vehicle rental and cruise 30 days; rental merchant categories 10 days; cardholder-initiated card-absent 10 days; card-present 5 days. Incremental authorizations do not extend these windows, and long stays need a fresh authorization. Country-specific timeframes are in the Visa Rules, which prevail over the guide [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf). *Discrepancy:* a secondary summary gives 31 days for lodging and rental ([walletto.eu](https://walletto.eu/authorization-and-reversal-processing-requirements-for-merchants/)); the Visa document (30 days) takes precedence.
- **Fuel.** Automated fuel dispensers use a separate "initial authorization" framework: a capped fixed amount with no incrementals. From April 2025 Visa allows initial authorizations only for fuel dispensers [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf). In the US, a state consumer page says Visa and Mastercard let gas stations hold up to $175 at the pump (periodic) [S][US] — [Georgia AG Consumer Protection (snippet)](https://consumer.georgia.gov/consumer-topics/debit-card-holds).
- **Mastercard.** The rules list "Undefined authorization … Seven calendar days from the authorization approval date" [S] — [Mastercard Transaction Processing Rules (snippet; PDF blocked to download)](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/transaction-processing-rules.pdf). A secondary source says pre-authorizations must clear within 30 calendar days and final authorizations within 7 [S][V] — [PaymentUSA (snippet)](https://paymentusa.com/blog/authorization-hold).
- **Unmatched holds have a cost.** Visa charges a "Misuse of Authorization System" fee on approved authorizations that are neither cleared nor reversed [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf).
- **Türkiye provizyon practice:**
  - A provizyon reduces the available limit but is not debt. It usually posts within 1–3 business days (weekends and holidays excluded) and can take up to a week for suspicious transactions or system errors.
  - Akbank names three kinds: *ön provizyon* (e-commerce, before shipping); *güvenlik provizyonu* (car rental, hotels, online grocery, where the final amount can be lower or higher); and *chargeback provizyonu* (created when a cardholder disputes or a refund is pending).
  - If the final amount is lower, the difference is returned; if higher, more is charged.
  
  [B: Akbank] — [Akbank (10.07.2025)](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek). Other banks: about 1 day, longer when the POS belongs to another bank [B: Halkbank] — [Halkbank blog (snippet)](https://www.halkbank.com.tr/tr/blog/provizyon-nedir); 1–2 days, 1 day when card and POS are at the same bank [B: Vakıf Katılım] — [Vakıf Katılım (snippet)](https://www.vakifkatilim.com.tr/tr/hakkimizda/medya-merkezi/blog/detay/provizyon-ne-demek-provizyon-ne-kadar-surer). An aggregator says holds that never finalize usually drop off within 7–10 days [V] — [HesapKurdu (snippet)](https://www.hesapkurdu.com/kredi-karti/rehber/bekleyen-provizon-iptali-nasil-yapilir).
- **Pending items cannot be disputed.** Items still in provizyon cannot be disputed or cancelled by the bank and do not appear in the dispute menu; the customer waits for them to post, but must call at once if fraud is suspected [B: İş Bankası; Kuveyt Türk] — [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir); [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir). *Discrepancy:* Akbank's blog says a provizyon item can be cancelled through an objection given a valid reason such as loss, theft or fraud ([Akbank](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek)). Treat this as bank-specific.
- **Reversal vs refund vs chargeback.** In a refund the seller returns the money directly; in a chargeback the bank asks the seller's bank for it, with no guarantee. Visa UK notes chargeback "isn't a legal right" in the UK [S][UK] — [Visa UK](https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html). An authorization reversal instead "notif[ies] the issuer that all, or part, of a transaction has been cancelled and that the hold … should be removed" [S] — [Visa (©2024)](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf).
- **Refund posting time.**
  - Kuveyt Türk tells customers to wait 15 days after a cancellation or refund before filing "refund not received" [B: Kuveyt Türk] — [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir).
  - A Turkish travel merchant says card refunds can take up to 7 business days to show [S] — [obilet help (snippet)](https://yardim.obilet.com/hc/tr/articles/5518330172828-%C4%B0adem-hesab%C4%B1ma-yans%C4%B1mad%C4%B1-ne-yapmal%C4%B1y%C4%B1m).
  - An e-money issuer says refunds usually arrive 5–10 business days after the merchant sends them and cannot be tracked before they arrive [S] — [Wise TR help (snippet)](https://wise.com/tr/help/articles/2935785/wise-kart%C4%B1ma-yap%C4%B1lan-bir-iade-ne-kadar-zaman-al%C4%B1r).
- **Offline transactions.** Mastercard rules allow some chip transactions of USD 200 or less (EUR 200 in Europe) to be approved offline by the EMV chip, while magnetic-stripe transactions must always be authorized online by the issuer [S] — [Mastercard TPR (snippet)](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/transaction-processing-rules.pdf). In-flight sales commonly rely on offline approval with floor limits [S] — [PXCom (snippet)](https://pxcom.aero/inflight-payments-must-know/).
- **Record retrieval (TR).** On request, the issuer must provide transaction records within a period suited to the transaction, no longer than 30 days (60 days for transactions abroad) [L-TR] — [Law 5464 Art. 8](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf).

### Inferences
- [R] Diagnostic order: (1) pending or posted? (2) do the pending and posted amounts match? (3) a pending item and a posted one for the same merchant usually means a hold not yet matched, not a double charge; (4) hotel, car rental, fuel and online grocery mean an estimate is expected; (5) for foreign-currency items the FX rate is fixed at clearing (§8).
- [R] Say what *typically* happens; never promise a release date. Release depends on a merchant reversal or on the issuer cleaning up expired holds; a manual release is only possible if the bank allows it [V].
- [R] On debit cards a hold can cause later declines, so warn the customer before travel or a hotel stay.

### Gaps
- No public TCMB or BDDK rule was found on how long a Turkish issuer may keep an uncaptured provizyon. Bank figures are "typical", not commitments.
- BKM's domestic clearing and switching role could not be confirmed from a primary source in this pass.
- Current Mastercard validity windows could not be read from the primary PDF (automated download returned 403).

---

## 2. Declines: categories, diagnosis without exposing fraud logic, customer self-checks

### Takeaway
Most declines come from the issuer: funds or limit, card status, a wrong PIN, CVV or expiry, customer-set controls (closed to e-commerce, abroad or contactless), regulatory closures after missed minimum payments, risk rules, or 3-D Secure failure. A smaller share come from the merchant, acquirer or network. In Türkiye, e-commerce permission is often off by default (a BDDK instruction from 2016–2018), so "kartım internet alışverişine kapalı" is a top cause. The agent should explain the category and the safe fix, never the risk-rule logic.

### Cited Findings
- **Issuer-side causes:** insufficient funds or limit, suspected fraud or unusual activity, wrong CVV or expiry, card reported lost or stolen, account frozen or closed. **Acquirer-side causes:** merchant not set up for the card type, merchant processing limits exceeded, merchant suspended [S] — [Stripe, decline codes](https://stripe.com/resources/more/a-complete-list-of-decline-codes).
- **Common ISO-style response codes:** 05 do not honor · 14 invalid account number · 41/43 lost/stolen pick-up · 51 insufficient funds · 54 expired card · 55 incorrect PIN · 57 not permitted to card · 61 exceeds approval amount · 65 exceeds withdrawal limit · 75 PIN tries exceeded · 91 issuer/switch unavailable · 96 system error · 1A additional customer authentication required [S] — [Stripe](https://stripe.com/resources/more/a-complete-list-of-decline-codes).
- **Visa decline categories:**
  - Category 1: issuer will never approve (e.g., closed account) — do not retry.
  - Category 2: cannot approve at this time — retry later.
  - Category 3: cannot approve with the data given — fix the data and retry.
  - Since April 2022 Visa charges an excessive-reattempt fee for any retry after a category 1, and for retries beyond 15 in 30 days on categories 2 and 3.
  
  [S] — [CardPointe/Fiserv (as of 10/22/2022)](https://support.cardpointe.com/compliance/visa-decline-rules-and-responses/).
- **TROY's public reasons for a decline:** limit used up, card status changed, contactless turned off, or a temporary problem at the issuer [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular).
- **E-commerce closed by default (TR).** Under a BDDK instruction sent on 27 Oct 2016, existing individual credit, debit and supplementary cards whose holders had not consented by 31 Jan 2018 had internet-shopping permission switched off. Virtual cards stay open [L-TR as reported by B: İş Bankası] — [Maximum (İş Bankası)](https://www.maximum.com.tr/kartlarin-internet-alisveris-yetkisi). Ziraat says cards without consent (company and virtual cards excepted) were closed to e-commerce on 01.02.2018 [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Customer self-service controls.** Customers can open or close domestic and abroad e-commerce, cash and POS use and set daily limits in app or internet banking [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Contactless can be toggled under "Kart Ayarları" [B: VakıfBank] — [VakıfBank blog](https://www.vakifbank.com.tr/tr/blog/temassiz-odeme-nedir). E-commerce can also be opened by SMS keywords (İş Bankası "SANALONAY + last 6 digits" to 4402 — [Maximum](https://www.maximum.com.tr/kartlarin-internet-alisveris-yetkisi); Yapı Kredi "YETKI + last 4 digits" to 4944 — [Yapı Kredi (snippet)](https://www.yapikredi.com.tr/bireysel-bankacilik/kartlar/guvenli-alisveris)) [B].
- **New cards ship closed.** Credit cards are sent closed for security and must be activated [B: Garanti BBVA/Bonus] — [Bonus (snippet)](https://www.bonus.com.tr/kredi-karti-kullanima-acmak). Before using a card online or contactless, the customer must first make a chip-and-PIN transaction at an ATM or POS [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Missed minimum payments close the card (regulation as cited by a bank).** Under the 2013 amendment to the BDDK card regulation (RG 08.10.2013, no. 28789), a card whose minimum payment is missed 3 times in a calendar year is closed to cash use, and 3 consecutive misses close it to cash and purchases. Ziraat's own practice is stricter: a single missed or short minimum closes cash advance, two consecutive misses also close purchases, and paying the minimum restores the card [L-TR][B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). *Discrepancy between the regulation summary and the bank's practice; confirm in the Yönetmelik (researcher 02/09).*
- **Limit cuts (TR, 2026).** BDDK board decisions (reported 31.01.2026): where a person's total card limits across banks exceed 400k TL, banks cut unused limits (50% of the unused part for 400–750k, 80% above 750k, based on the statement with the highest spend in the last year) by 15 Feb 2026. All cardholders' limits must be brought in line with income by 1 Jan 2027 [L-TR, press report][V] — [Bigpara/Hürriyet (31.01.2026)](https://bigpara.hurriyet.com.tr/haberler/ekonomi-haberleri/kredilerde-kurallar-degisti-bddkdan-yeni-kararlar_ID1624216/).
- **3-D Secure failures:** see §7. **Card blocks** can also come from security events, overdue payments, suspicious activity or legal orders such as *haciz* [B: Garanti BBVA/Bonus] — [Bonus blog (29.09.2024)](https://www.bonus.com.tr/blog/kredi-karti-blokesi-nasil-kaldirilir).

### Inferences
- [R] Decline triage tree, run in authenticated tools: card status (active, not activated, temporary freeze, lost/stolen, expired, replaced) → channel controls (e-commerce, abroad, contactless, cash) → available balance or limit including holds → regulatory closure (missed minimum) → PIN or CVV attempts → 3DS outcome → risk decline → merchant or network error (no issuer authorization record at all means the request never reached the bank).
- [R] Safe wording for risk declines: "Our security checks stopped this transaction." Offer re-verification or unblocking through the official flow, never name the rule ("over X amount", "new merchant", "country score"). This keeps the response useful without revealing detection logic (see researcher 10).
- [R] Customer self-checks to suggest: card settings in the app (internet, abroad, contactless switches; daily limits), available limit including pending items, expiry date on the card, whether a new card replaced the old one, and whether the 3DS SMS goes to the current phone number.
- [R] If no authorization attempt reached the issuer, the problem is on the merchant, acquirer or network side. The customer should retry with the merchant or use another method, and the bank cannot "approve" it.

### Gaps
- The BDDK 2016 instruction itself was not retrieved; the account above comes from two banks. Researcher 02 should confirm.
- No public figure on decline-reason frequencies in Türkiye was found, and none should be invented.

---

## 3. PIN: lockouts, forgotten PIN, secure reset

### Takeaway
A PIN locks after several consecutive wrong entries; the exact count is set by the issuer. Customers reset or unblock it themselves through official bank channels: mobile app, internet banking, ATM PIN menu, IVR, and some SMS flows. The agent never asks for, hears or confirms a PIN, CVV or OTP, and only points the customer to the official flow.

### Cited Findings
- A PIN block usually follows consecutive wrong entries or a security action by the bank. It is removed by calling the bank, setting a new PIN in the app or internet banking, or using the ATM PIN-renewal menu [B: Garanti BBVA/Bonus] — [Bonus blog (29.09.2024)](https://www.bonus.com.tr/blog/kredi-karti-blokesi-nasil-kaldirilir). Industry response code 75 means "allowable number of PIN entry tries exceeded" [S] — [Stripe](https://stripe.com/resources/more/a-complete-list-of-decline-codes).
- Ziraat lets customers set a PIN at an ATM, in internet or mobile banking, via the call center or by SMS. If the PIN for the credit function is set outside an ATM, the card must first be used at a Ziraat ATM with the new PIN [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Other banks also run SMS PIN flows (e.g., Garanti BBVA to 3340, ING to 2205), and their required fields differ by bank [B] — [Garanti BBVA (snippet)](https://www.garantibbva.com.tr/kartlar/kart-sifresi-alma); [ING (snippet)](https://www.ing.com.tr/tr/sizin-icin/kartlar/kart-sifresi-alma).
- Banks say: never share your PIN with anyone, bank staff included; do not choose easily guessed PINs; banks never ask by phone for the expiry date, CVV or PIN; ignore "helpers" at the ATM who tell you to re-enter your PIN [B: Garanti BBVA] — [Garanti BBVA Güvenli Kart Kullanımı](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi).
- Cardholders are legally required to protect the card and PIN and to tell the issuer immediately about loss, theft or an unauthorized transaction [L-TR] — [Law 5464 Art. 16](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf).
- Under PCI DSS, PINs and PIN blocks, CVV and full track data are "sensitive authentication data" that must never be stored after authorization, even encrypted, and even with customer permission [S] — [PCI SSC Data Storage Do's & Don'ts](https://www.pcisecuritystandards.org/pdfs/pci_fs_data_storage.pdf); [PCI SSC blog FAQ](https://blog.pcisecuritystandards.org/faq-can-cvc-be-stored-for-card-on-file-or-recurring-transactions).

### Inferences
- [R] Safety rule for the AI agent: never collect or echo PIN, CVV/CVC, OTP or 3DS codes, full card number in free text, or passwords. Some bank SMS flows send partial card data to the bank's short code. The agent must not repeat that syntax back with the customer's data or "help fill it in"; it links to the bank's official instruction page.
- [R] Lockout handling: confirm the block from the card status, not from the customer's account of events → send the customer to self-service PIN reset (app or ATM) → if they cannot authenticate digitally, pass to IVR or branch. If several attempts were made and the customer denies making them, treat it as a possible security incident (§5).

### Gaps
- Attempt limits (often 3) and automatic unlock rules (for example a daily reset) were not found on primary pages for the major banks. Mark as institution-specific.

---

## 4. ATM issues: retained card, cash not dispensed, partial dispense, deposits, shared ATMs, fees, abroad

### Takeaway
ATM problems fall into four kinds: card retained (*kart yutma/alıkonma*), cash not dispensed but debited (*para vermedi ama hesaptan düştü*), partial dispense, and a deposit jam or deposit not credited (*para sıkışması*). At the bank's own ATM, the issue is resolved by the bank's ATM reconciliation (cash count, journal). At another bank's ATM it goes through the dispute (*harcama itirazı*) channel and waits on the other bank's investigation under national and international card rules. No public, binding resolution deadline was found.

### Cited Findings
- **Retained card.** If the card is retained at one of the bank's branch ATMs during business hours, the customer collects it from that branch. Otherwise the customer calls at once to close and renew the card, from their own phone, dialing the number themselves, and ignores people offering help [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi). Ziraat sends an SMS with instructions to the registered phone when an ATM retains a card [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Press guidance: getting a retained card back can take 1–2 weeks; at İş Bankası a card retained because of a technical fault is handed back by branch staff after ID verification [press] — [Hürriyet (15.05.2026)](https://www.hurriyet.com.tr/egitim/atm-kartimi-yuttu-ne-yapabilirim-nasil-ve-ne-zaman-geri-alabilirim-ziraat-garanti-vakif-is-halk-ve-yapi-kredi-bankasi-42124420).
- **Cash kept by the ATM (own or other bank).** Customers raise an objection through internet or mobile banking, a branch or the call center. "Resolution of other-bank ATM objections depends on the counterpart bank's review period under national and international card rules" [B: Ziraat] — [Ziraat ATM SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/atm). Cash jams happen especially during deposits, and refunds are requested via the phone branch [B: İş Bankası] — [İş Bankası](https://www.isbank.com.tr/bankamatik-para-sikismasi).
- **Dispute categories exist for ATM cases:** "Nakit tutarı ATM'den alamadım/Eksik aldım" (cash not received or short) [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi). Other-bank ATM problems, short or no cash, and deposits not credited are all disputable, and deposits not credited at other-bank ATMs can only be raised with the dispute form [B: Akbank; DenizBank] — [Akbank](https://www.akbank.com/kartlar/harcama-itirazi); [DenizBank](https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz). Visa has a matching code, 13.9 "Non-Receipt of Cash or Load Transaction Value" [S] — [Chargeflow (2026)](https://www.chargeflow.io/blog/visa-chargeback-reason-codes).
- **Shared ATMs.** Since 1 Oct 2009 Turkish ATM networks (including "Ortak Nokta") merged, so all Visa/Mastercard cards work at every bank's ATMs [B: Halkbank] — [Halkbank Ortak ATM](https://www.halkbank.com.tr/tr/dijital-bankacilik/atm/ortak-atm-platformu). The **"Kamu Ortak ATM"** platform covers VakıfBank, Ziraat Bankası, Halkbank, PTT, Emlak Katılım, Vakıf Katılım and Ziraat Katılım. Members' customers can withdraw, deposit, check balances, pay or check credit cards, and use PIN services free at each other's ATMs [B: VakıfBank] — [VakıfBank Ortak ATM](https://www.vakifbank.com.tr/tr/dijital-bankacilik/atm/ortak-atm). The public banks agreed this in September 2017 [press] — [AA (snippet)](https://www.aa.com.tr/tr/ekonomi/devlet-bankalarinda-ortak-atm-donemi/1195715). Some private banks run their own alliances (e.g., DenizBank, QNB, TEB with limited free transactions) [V] — [HesapKurdu (snippet)](https://www.hesapkurdu.com/uzaktan-musteri-edinimi/rehber/ortak-atm).
- **Fees (TR).** At the customer's own bank, deposits, balance checks and withdrawals within the limit are free. At another bank's ATM a fee may be charged, with the customer's consent at the time of the transaction [L-TR via BDDK FAQ] — [BDDK SSS Ücretler](https://www.bddk.org.tr/Sss/Liste/114). Published bank examples: other-bank withdrawal 1% + 0.91 TL [B: Kuveyt Türk] (periodic; possibly dated) — [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir). Fee values belong to researcher 09.
- **Limits (one bank, periodic):** daily withdrawal 10,000 TL; over-limit withdrawal 7,500 TL (fee applies); QR withdrawal 7,500 TL; deposit 50,000 TL [B: Ziraat] — [Ziraat ATM SSS](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/atm).
- **Abroad.** Only the card's main linked account is reachable at foreign ATMs, and Troy-only cards cannot be used abroad [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). DCC at foreign ATMs: see §8.
- **Anecdotal timelines (not commitments):** "Halkbank 2günde ATM para sayımını…" ([Şikayetvar](https://www.sikayetvar.com/ziraat-bankasi/ziraat-bankasi-ortak-atm-parami-vermedi-hesaptan-dustu)); a forum report of cash returned "3 iş günü içerisinde" ([hukuki.net](https://www.hukuki.net/showthread.php?64249-ATM-de-Kalan-Para)).

### Inferences
- [R] Collect: ATM location or ID (from the receipt or app), bank owning the ATM, date and time, amount requested versus received, card used, transaction type (withdrawal or deposit; card or QR/cardless), whether a receipt or screen error appeared, and whether anyone "helped". **Never** collect the PIN.
- [R] Own-bank ATM: open an ATM reconciliation case (journal plus cash count). Other-bank or abroad ATM: file a dispute (13.9-type) and set expectations of a longer wait. Do not give a fixed number of days unless the bank's internal SLA allows it.
- [R] Retained card plus suspicious circumstances (card trapped, someone nearby, PIN entered on a prompted screen) means block immediately and treat as a security incident (§5, researcher 10).

### Gaps
- No official own-bank ATM reconciliation SLA was found for the major Turkish banks; the 1–7 day figures are anecdotal.
- Whether retained cards are destroyed or kept for collection, and for how long, is bank-specific and was not found in a primary source.

---

## 5. Lost/stolen cards: blocking channels, temporary freeze vs permanent block, replacement, liability

### Takeaway
Block first, investigate later. Turkish banks offer app, IVR and branch blocking, and many offer a temporary freeze (geçici kapatma) that becomes a permanent block plus renewal if not reversed (Garanti BBVA: 24 hours). Turkish liability is set by Law 5464: at most 150 TL for unlawful use in the 24 hours before notification, unless there was gross negligence or intent. The EU, UK and US use different caps.

### Cited Findings
- **Channels.** Close the card in the mobile app or call 444 0 333 and say "kartımı bulamıyorum" or "kartımı çaldırdım". That IVR menu can only close and renew the card, by design. A temporary closure in the app can be reversed within 24 hours; if it is not, the card is automatically renewed and the new card goes to the registered address [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi). Temporary closure is also available in other banks' card settings [B: İş Bankası; Ziraat] — [İş Bankası blog (snippet)](https://www.isbank.com.tr/blog/kart-guvenligi-nasil-saglanir); [Bankkart SSS (snippet)](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- After closing a stolen card used for fraud, Garanti BBVA advises getting a police report and filing a complaint with the prosecutor [B: Garanti BBVA] — [Garanti BBVA dispute page](https://www.garantibbva.com.tr/kartlar/islem-itirazi). For "not me" disputes, banks require the card to be cancelled and renewed [B: Akbank; DenizBank] — [Akbank](https://www.akbank.com/kartlar/harcama-itirazi); [DenizBank](https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz).
- **Replacement fee (TR).** Up to two renewals per calendar year for loss, theft and similar reasons are free [L-TR via BDDK FAQ] — [BDDK SSS](https://www.bddk.org.tr/Sss/Liste/114). Ziraat lists magnetic damage and name change among those reasons [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Liability (TR, Law 5464).**
  - Art. 12: the cardholder is liable for unlawful use in the 24 hours before notification, capped at 150 (Y)TL; the cap does not apply with gross negligence, intent or no notification. Issuers must offer insurance for this 150 TL on request.
  - Art. 15: liability starts on signing and taking possession. The cardholder is not liable for unlawful use in purchases made without a sales slip by remote means or order forms.
  - Art. 16: duty to notify immediately.
  
  [L-TR] — [Law 5464](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf). (The 150 TL figure has not been updated in the consolidated text; whether Law 6493 rules also apply goes to researcher 02.)
- **EU:** the payer bears at most EUR 50, not applicable if the loss was undetectable or caused by the provider [L-EU] — [PSD2 Art. 74(1)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366). Unauthorized transactions must be reported without undue delay and within 13 months of the debit date [L-EU] — [PSD2 Art. 71](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366).
- **UK:** at most £35 [L-UK] — [PSRs 2017 reg. 77](https://www.legislation.gov.uk/uksi/2017/752/regulation/77).
- **US debit (Reg E):** the lesser of $50 if reported within 2 business days of learning of the loss, otherwise up to $500; unauthorized transfers on a statement must be reported within 60 days of transmittal to avoid liability for later transfers [L-US] — [12 CFR 1005.6](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.6). **US credit (Reg Z):** the lesser of $50 [L-US] — [12 CFR 1026.12(b)](https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.12). Visa also has a Zero Liability policy for fraud [S] — [Visa UK](https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html).

### Inferences
- [R] Blocking is a protective action. It should be possible after lighter verification than data disclosure (the Garanti BBVA "close and renew only" fast lane is a good model). Address changes, delivery redirects, unblocking and PIN resets need full strong authentication, because they are classic account-takeover steps.
- [R] Freeze or block decision: if the customer may simply have misplaced the card, offer a temporary freeze and explain the auto-renewal rule. If the card was stolen, or there are unknown transactions, block it permanently, renew it, and open a fraud case.
- [R] Tell customers that recurring merchants and wallet tokens may need updating, or may keep working, after replacement (§6, §11).

### Gaps
- Whether a "temporary closure" in Turkish apps also blocks recurring or merchant-initiated transactions is bank-specific and unverified.
- How the 5464 Art. 12 cap interacts with the 6493 payment-services rules is for researcher 02.

---

## 6. Activation, delivery/couriers, renewal, damaged cards, contactless, digital wallets and tokenization

### Takeaway
Turkish cards are delivered by courier or at a branch and arrive closed for use (activation by a first chip-and-PIN transaction or in the app). The no-PIN contactless limit is 2,500 TL from 15 Jan 2026 (BDDK). Apple Pay is still not available to Turkish-issued cards as of 10 Oct 2026, and Google Wallet appears not to be either (anecdotal only). Phone payments in Türkiye run through banks' own Android NFC/HCE features, and TROY supports these.

### Cited Findings
- **Delivery (law).** Issuers must make sure cards are delivered to the main cardholder; cards for minor supplementary holders go to the main holder; cards may not be issued to anyone who did not request one [L-TR] — [Law 5464 Art. 8](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf).
- **Tracking.** "Kart Gönderim İzleme" shows courier and branch movements and delivery status, and customers can redirect a card already out for delivery to another address [B: VakıfBank] — [Vakıfkart](https://www.vakifkart.com.tr/ayricaliklar/firsatlar/kredi-karti-basvuru-kurye-takip). Ziraat Bankkart can be collected at the branch on application or sent to an address [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Fake-courier scam warning:** never hand a delivered card back to someone claiming to be the courier [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi).
- **Courier complaints (anecdotal):** "5 gündür kartım teslim edilmedi ve sistemde 'adres yetersizliği' ibaresi görünüyor" — [Şikayetvar/Kuryenet](https://www.sikayetvar.com/kuryenet/takip-kredi-karti/takip-numarasi?page=21).
- **Contactless limit.**
  - BDDK raised the no-PIN contactless limit from 1,500 TL (in force since 1 July 2024) to 2,500 TL from 15 Jan 2026. For comparison: UK £100; France, Italy, Spain, Portugal, Greece and Germany €50; no US standard [L-TR via press] — [AA (02.01.2026)](https://www.aa.com.tr/tr/ekonomi/temassiz-kartlarda-sifresiz-islem-limiti-15-ocaktan-itibaren-2-bin-500-lira-olacak/3787754).
  - VakıfBank confirms 2,500 TL for 2026 and adds a cumulative limit of 5,000 TL for consecutive no-PIN taps, after which one chip-and-PIN transaction is required (periodic) [B: VakıfBank] — [VakıfBank](https://www.vakifbank.com.tr/tr/blog/temassiz-odeme-nedir).
  - The first use of a card must be contact plus PIN before contactless works [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Note that some older figures on that page (500 TL, 750 TL) are stale.
  - If a contactless-marked card does not work, the cause may be the terminal or the card's physical condition; contact the issuer [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular).
- **Wallets.** Apple's list of Apple Pay countries does not include Türkiye (checked 2026-10-10) — [Apple Support](https://support.apple.com/en-us/102775). For Google Wallet only anecdotal sources were found ("Google Wallet da Türkiye kartlarına kapalı") — [kartasistanim (snippet)](https://kartasistanim.com/rehber/apple-pay-turkiye); [Technopat (snippet)](https://www.technopat.net/sosyal/konu/google-pay-turkiyede-kullanilabilir-mi.3998624/) [V]. TROY cards can be added to Android phones and wearables with NFC + HCE through the issuer's wallet support [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular). VakıfBank Mobil has "Mobil Temassız Ödeme" for NFC Android phones [B: VakıfBank] — [VakıfBank](https://www.vakifbank.com.tr/tr/blog/temassiz-odeme-nedir). BKM Express is a domestic wallet that pays with an OTP without sharing card data [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Tokens versus the card number.** A network token "remains valid through a card reissue or replacement because the card network refreshes the token in the background" [S] — [ACI Worldwide (snippet)](https://www.aciworldwide.com/network-tokens); the issuer and network can update the token's account data or expiry when the card changes [S] — [Very Good Security (snippet)](https://www.verygoodsecurity.com/blog/posts/what-is-a-network-token).
- **Digital-wallet purchases** are disputed the same way as purchases with the linked card [S][UK] — [Visa UK](https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html).

### Inferences
- [R] "Apple Pay doesn't work with my Turkish card" is an availability issue, not a fault. Offer the bank's own NFC option (Android) or a physical or virtual card. Do not suggest workarounds such as foreign accounts or sideloaded APKs, which some forums do.
- [R] When a card is replaced after fraud, check whether tokens on phones, wearables or at merchants were also suspended. A token that survives replacement can keep a compromised device payment-capable ([V] institution-specific token-lifecycle settings).
- [R] Delivery problems: confirm the address is up to date (5464 Art. 16 requires address changes to be reported within 15 days), check tracking status, and only redirect after strong authentication.

### Gaps
- No primary statement from Google on Türkiye availability was found.
- Renewal timing before expiry (how many weeks ahead), courier ID checks at delivery and how long undelivered cards are kept are not public for most banks.

---

## 7. Online payments: 3-D Secure, card-not-present restrictions, virtual cards

### Takeaway
Turkish e-commerce depends on 3-D Secure, using an SMS OTP or in-app approval. Failures usually come from closed e-commerce permission, an outdated mobile number, an expired or mistyped code, or browser problems. Banks say transactions authenticated with 3DS, PIN or chip usually fail as "I didn't do it" disputes, which is why agents must warn customers never to share OTPs. Virtual cards are free by regulation and open for e-commerce by default.

### Cited Findings
- EMV 3-D Secure sends transaction, payment-method and device data between merchant and issuer so the issuer can authenticate the consumer "without adding unnecessary friction". The specifications in use are v2.2.0–2.3.1.1, and a v2.4.0 draft was under consultation until 1 July 2026 [S] — [EMVCo 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/).
- **Garanti BBVA's 3DS guidance:**
  - The OTP is sent by SMS, and BonusFlaş app approval can replace it.
  - A card closed to internet shopping cannot get a 3DS code.
  - Try another browser if the page fails; confirm the registered mobile number if the SMS does not arrive.
  - Never share the code, and check the merchant and amount shown in the 3DS message.
  
  [B: Garanti BBVA] — [Garanti BBVA (15.08.2023)](https://www.garantibbva.com.tr/blog/3d-secure-nedir); [Güvenli Kart](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi).
- **"Not me" disputes are rejected when the transaction was approved** with a 3DS SMS code, BonusFlaş approval, GarantiPay, BKM Express (no card entry), the card PIN, or the chip or magnetic stripe [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi).
- **Virtual cards (sanal kart).** Banks may not charge an annual fee or a creation or usage fee on virtual credit cards [L-TR via BDDK FAQ] — [BDDK SSS](https://www.bddk.org.tr/Sss/Liste/114). Virtual cards are open for e-commerce by default [B: İş Bankası] — [Maximum](https://www.maximum.com.tr/kartlarin-internet-alisveris-yetkisi). Debit cards also work online at 3DS merchants, and customers can manage domestic and abroad e-commerce restrictions [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Customer wording (anecdotal):** "3D SMS kodu bir türlü gelmiyor", "kartım internet alışverişinde reddediliyor" — [Şikayetvar](https://www.sikayetvar.com/3d/sms-gelmiyor); "kartım alışverişe kapalı" warning — [hesap.com (snippet)](https://hesap.com/hesap-defteri/kredi-karti-internet-alisverisine-nasil-acilir).

### Inferences
- [R] OTP-not-received triage: e-commerce permission → mobile number on file (changing it needs strong authentication and often a branch or other secure channel; researcher 08) → operator or SMS blocking, roaming abroad → code timeout → merchant 3DS page error (try again, another browser). Other causes listed by banks are a wrong or late code and temporary bank system faults — [Vakıf Katılım (snippet)](https://www.vakifkatilim.com.tr/tr/hakkimizda/medya-merkezi/blog/detay/3d-secure-nedir-ve-nasil-calisir). Never ask the customer to read the OTP aloud. If a customer reports getting OTPs they did not request, treat it as a possible compromise (researcher 10).
- [R] Virtual-card questions such as limits, CVV refresh or single-use cards are bank-specific. Send the customer to the app and do not quote features without the institution's documentation.

### Gaps
- Whether Turkish regulation requires 3DS for all domestic e-commerce, and how it handles low-value or merchant-initiated exemptions, was not established here (researcher 02/08).
- Bank-specific virtual-card features (customer-set limits, dynamic CVV) were not verified from primary pages.

---

## 8. International use: travel, Dynamic Currency Conversion (DCC), FX, TROY abroad, country/MCC blocks

### Takeaway
Foreign spending posts in TL at the issuer's conversion rule, typically the rate when the clearing record arrives, so it differs from the pending amount. DCC at a foreign POS or ATM converts at the merchant's rate. Consumers can refuse it: the scheme rules say the choice must be honoured, and the EU requires markup disclosure. Single-brand TROY cards do not work abroad; co-badged TROY cards work wherever the partner scheme is accepted.

### Cited Findings
- **FX conversion.** Schemes send foreign spending in USD, and it is converted into TL at the bank's highest USD rate on the day the record reaches the bank. Customers can instead choose a foreign-currency statement and pay in USD [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Amount differences on foreign transactions can come from exchange-rate movements [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi).
- **DCC (EU).** Under Regulation (EU) 2019/518, whenever DCC is offered at a shop, online or at an ATM, the charges must be disclosed before the transaction in a harmonised way. Card issuers must also send an electronic message after a payment in another EU currency. These rules apply from 19 Apr 2020, and the e-message duty from 19 Apr 2021 [L-EU] — [European Commission statement (Apr 2020)](https://finance.ec.europa.eu/document/download/e19af922-a513-42a2-9bc2-b57baea97449_en?filename=200408-currency-conversion-transparency-requirements-statement_en.pdf).
- **DCC (scheme).** Mastercard: "The cardholder's choice must be honored by all entities that offer DCC" [S] — [Mastercard DCC Guide 2025 (snippet)](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/DCC-Guide-2025-Merchant-Version.pdf). Consumer advice on social media, anecdotal: "Yurt dışında … sakın TRY seçme!" — [Instagram (snippet)](https://www.instagram.com/reel/DZIf_r2uyw1/?hl=en).
- **TROY abroad.** TROY works abroad only where the international scheme shown on the back of the card is accepted, e.g., Discover/Diners Club [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular). Ziraat states that its TROY cards work only domestically [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). *These are consistent once co-badging is taken into account; check the card's brand.*
- **Installments.** Purchases abroad cannot be paid in installments [L-TR, aggregator summary][V] — [HesapKurdu (snippet)](https://www.hesapkurdu.com/kredi-karti/rehber/kredi-kartinda-hangi-harcamalar-taksitlendirilir).
- **Abroad controls.** Customers can set restrictions for cash, POS and e-commerce at home and abroad [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).

### Inferences
- [R] Before travel: check the card brand (TROY single-brand or co-badged, Visa, Mastercard) → abroad usage enabled → limits and holds (hotels, car rental) → a backup card → recommend refusing DCC and choosing local currency. For "the amount on my statement is different", explain the conversion timing and DCC, and file a dispute only for a real processing error.
- [R] Merchant-category and country blocks: tell the customer the transaction is not allowed for that card or country, without detailing sanctions or risk lists. Escalate if the customer insists the block is wrong.

### Gaps
- Foreign-transaction fee (yurt dışı işlem ücreti) levels belong to researcher 09; no primary fee schedule was gathered here.
- No Turkish rule was found that mandates DCC disclosure for Turkish cardholders abroad, beyond the scheme rules.

---

## 9. Credit-card specifics: limits, statement cycle, minimum payment, interest types, installments (taksit), ekstre erteleme, cash advance, overlimit, annual fee, loyalty, supplementary cards

### Takeaway
Law 5464 and BDDK decisions frame Turkish credit cards:
- Limits are income-based and are not raised unless the customer asks.
- Statements are mandatory, and objections are due within 10 days after the due date.
- The minimum payment is 20% or 40% depending on the limit; the threshold rose to 100k TL on 1 Oct 2026.
- Missing the minimum causes regulatory card closures.
- Installments are restricted by sector.
- Banks must offer an annual-fee-free card.
- Supplementary cards sit inside the main card's limit.

Rate and fee values belong to researcher 09.

### Cited Findings
- **Limit (Art. 9).**
  - Issuers set limits from income, scoring and other checks, and may not increase them unless the cardholder asks.
  - Spending over the limit can incur only contractual interest (*akdi faiz*) on the excess.
  - Total limits may not exceed 2× monthly net income in year one and 4× in year two (the Board can change this).
  - Supplementary cards may be issued for third persons, tied to the main card, without exceeding the main limit.
  
  [L-TR] — [Law 5464 Art. 9](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf). For the 2026 limit-alignment decisions see §2 — [Bigpara (31.01.2026)](https://bigpara.hurriyet.com.tr/haberler/ekonomi-haberleri/kredilerde-kurallar-degisti-bddkdan-yeni-kararlar_ID1624216/).
- **Statement and objections (Art. 10–11).** A statement (*hesap özeti/ekstre*) is mandatory. Issuers must answer complaints and objections within 20 days. Credit-card transactions can be objected to within 10 days of the payment due date, giving reasons. If no objection is made in time, the statement becomes final, but the right to sue remains [L-TR] — [Law 5464 Art. 10–11](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf). Customers can change their statement date (*hesap kesim tarihi*) in the app [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Minimum payment (Art. 24).** The minimum can be no less than 20% of the period's debt, and the Board can raise it to 40% or differentiate by cardholder group. If the minimum is not paid, no obligation other than contractual late interest (*gecikme faizi*) may be imposed [L-TR] — [Law 5464 Art. 24](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf). **Current rule (periodic):** 20% for limits up to 100k TL and 40% above, after BDDK raised the threshold from 50k TL [L-TR, press] — [TRT Haber (02.10.2026)](https://www.trthaber.com/haber/ekonomi/kredi-kartlarinda-asgari-odeme-tutari-degisti-958955.html). Secondary sources give this as decision no. 11581 of 01.10.2026 [V] — [HesapKurdu (snippet)](https://www.hesapkurdu.com/kredi-karti/h/asgari-odeme-tutari-hesaplama). If the minimum stays unpaid for 3 months after the due date and is still unpaid 1 month after notice, the credit cards are cancelled and no new card can be issued until the debt is fully paid [L-TR] — [Law 5464 Art. 8](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf).
- **Installment (taksit) limits.** BDDK publishes board decisions changing installment limits, e.g., 17.12.2020-9322, 01.07.2021-9646, 21.12.2021-9993, 05.01.2023-10479, and 05.12.2024-11022 on phone purchases [L-TR] — [BDDK Mevzuat 1210](https://www.bddk.org.tr/Mevzuat/Detay/1210). Aggregator summaries (periodic) [V]:
  - No installments for cosmetics, alcohol, office supplies, telecoms, food and catering, fuel, gift cards, direct marketing, purchases abroad, and printed or bullion jewellery.
  - Capped counts for electronics, clothing and health products.
  - Phone thresholds of 20k TL in one source and 40k TL in a later social-media report.
  
  — [HesapKurdu (snippet)](https://www.hesapkurdu.com/kredi-karti/rehber/kredi-kartinda-hangi-harcamalar-taksitlendirilir); [Instagram (snippet)](https://www.instagram.com/p/DRS0beLDc2p/?hl=en). At the POS, the installment count and amount are shown on screen and the customer confirms with PIN [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular).
- **Deferral and rescheduling products (one bank's October 2026 campaign).** After paying at least the minimum, the customer can defer the remaining "deferrable" amount by 1–4 months or split it into 4–12 installments, at no more than 3.25% interest a month. It cannot be done on the day the minimum is paid, can be cancelled the same day, and early closure follows rules [B: VakıfBank] (periodic) — [Vakıfkart](https://www.vakifkart.com.tr/ayricaliklar/firsatlar/kredi-karti-basvuru-kurye-takip).
- **Cash advance (nakit avans).** For installment cash advances only interest may be charged, no fees [L-TR via BDDK FAQ] — [BDDK SSS](https://www.bddk.org.tr/Sss/Liste/114). For transactions after 28 May 2014 there is a 14-day withdrawal right on installment cash advances [B: VakıfBank] — [Vakıfkart](https://www.vakifkart.com.tr/ayricaliklar/firsatlar/kredi-karti-basvuru-kurye-takip).
- **Annual fee (kart aidatı).** BDDK FAQ:
  - Banks must offer a card type with no annual fee, and a fee-paying card can be switched to a free one with the same limit (which may lack installments or points).
  - The fee may only be charged after the first debiting use; cards with no activity for 180+ days are inactive and are not charged.
  - Increases are capped at prior-year CPI with 30 days' notice and a 15-day right to exit.
  - Supplementary-card fees may be at most 50% of the main card's fee.
  - Fees are governed by the TCMB fee communiqué (in force 7 Mar 2020) and the TBB fee schedule ("izahname"). Fee disputes go to the bank, then TCMB or the TBB/TKBB customer arbitration committees.
  
  [L-TR] — [BDDK SSS](https://www.bddk.org.tr/Sss/Liste/114). The Ministry of Trade notes the no-fee-card requirement [L-TR] — [Ticaret Bakanlığı (snippet)](https://ticaret.gov.tr/haberler/kredi-karti-aidatlarinin-iadesine-iliskin-basin-aciklamasi). An arbitration committee ordered a refund where a bank had not offered a fee-free option [press] — [AA (snippet)](https://www.aa.com.tr/tr/ekonomi/hakem-heyeti-aidatsiz-kredi-karti-secenegi-sunmayan-bankanin-aidati-iadesine-karar-verdi/3041192).
- **Loyalty points (bank-specific).** Ziraat's Jest Lira carries over year to year, but campaign Jest Lira may have an announced expiry [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Akbank Axess cards earn chip-para [B: Akbank] — [Akbank](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek). Garanti BBVA uses the Bonus program and app [B] — [Garanti BBVA](https://www.garantibbva.com.tr/blog/3d-secure-nedir). TROY: points and bonuses are set by the issuer [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular).
- **Supplementary card (ek kart).** Issued at the main holder's request, inside and drawn from the main card's limit, to persons aged 15 or over. Its debts appear on the main card's statement [B: Ziraat] — [Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular). Disputes over supplementary-card transactions must be signed by the supplementary holder [B: Kuveyt Türk; DenizBank] — [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir); [DenizBank](https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz). Turkish statutes have no direct, sufficient provision on the supplementary holder's liability [academic] — [TRDizin abstract (snippet)](https://search.trdizin.gov.tr/en/yayin/detay/220641/kredi-karti-sozlesmelerinde-ek-kart-hamilinin-hukuki-durumu). Secondary sources say the main holder is liable for card debts, while court practice limits the supplementary holder to their own spending [V] — [HesapKurdu (snippet)](https://www.hesapkurdu.com/kredi-karti/rehber/kart-hamili-ne-demek); [epikpartnershukuk (snippet)](https://epikpartnershukuk.com/article.php?aId=358).

### Inferences
- [R] Explain limit versus available limit (*kullanılabilir limit*): available limit = limit − posted debt − pending holds − installment balances not yet billed (installments usually reserve the full purchase amount against the limit) [V: bank-specific].
- [R] Statement-cycle explainer: purchases after the statement date fall into the next statement; *dönem borcu* is the statement balance; *asgari ödeme* is the minimum due; paying only the minimum leaves the rest accruing interest (rates: researcher 09).
- [R] Annual-fee refund requests: check whether a fee-free card was offered, the inactivity rule and first-use timing. The agent may offer a switch to a fee-free card (same limit) if the tool allows, but it must not promise a refund; refunds are a discretionary bank decision or an arbitration outcome.

### Gaps
- The Banka Kartları ve Kredi Kartları Hakkında Yönetmelik text (missed-minimum rules, supplementary-card age, installment rules) was not read directly.
- The full current installment matrix and the text of BDDK decision 11581 were not retrieved.

---

## 10. Disputes and chargebacks (harcama itirazı): process, categories, time limits, what to collect, what not to promise

### Takeaway
The customer files through the issuing bank's app, internet banking, call center or form. The bank judges the claim against Visa, Mastercard or TROY rules and sends it to the merchant's bank. The usual filing window is 120 days from the relevant date under Visa and Mastercard (up to 540 for some codes); TROY says 180 days from the transaction date; Law 5464 sets 10 days after the due date for statement objections. A case can take up to 180 days. Merchant disputes need contact with the merchant first; fraud disputes need the card blocked first.

### Cited Findings
- **Process.** Contact the merchant first (except fraud) → the bank asks for documents → the bank goes to the merchant's bank → if the merchant's documents are missing or insufficient, the amount comes back to the cardholder; if they are sufficient, the dispute can fail. It can take up to 180 days [B: İş Bankası; Kuveyt Türk] — [İş Bankası (08.08.2024)](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir); [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir).
- **Time limits.**
  - 120 days, counted from: the transaction date for fraud; the promised delivery date for goods not received; the delivery date; the date of the cancellation or refund document; hotel check-out; car return. Never more than 540 days [S][B: İş Bankası] — [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir).
  - TROY: at the latest 180 days from the transaction date [S] — [TROY SSS](https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular).
  - Visa: generally 120 days, up to 540 for some codes; merchants have 30 days to respond at each phase [S] — [Chargeflow (2026)](https://www.chargeflow.io/blog/visa-chargeback-reason-codes); Visa UK: "within 120 days of purchase" — [Visa UK](https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html).
  - Garanti BBVA asks customers to file before the payment due date so the claim is not treated as late [B] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi).
  - Law: objections within 10 days of the due date; the bank must answer complaints within 20 days [L-TR] — [Law 5464 Art. 11](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf). Garanti BBVA reviews and replies within 20 days [B] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi).
- **Visa categories:** Fraud (10.x), Authorization (11.x), Processing Errors (12.x), Consumer Disputes (13.x). Code 12.1 (late presentment) was retired in April 2024 and folded into 11.3. Consumer codes include 13.1 not received, 13.3 not as described or defective, 13.5 misrepresentation, 13.6 credit not processed, 13.7 cancelled, 13.9 cash not received at ATM. Processing codes include 12.5 incorrect amount, 12.6.1 duplicate, 12.6.2 paid by other means [S] — [Chargeflow (2026)](https://www.chargeflow.io/blog/visa-chargeback-reason-codes).
- **Turkish bank categories (mirror the scheme codes):**
  - Suspicious or "not me"; lost or stolen card used.
  - Goods or service not received, partial or defective. The product must be returned before a "defective" claim, and Mastercard gambling or forex transactions are excluded from "not received".
  - Cancellation or refund not credited (wait 15 days first).
  - Duplicate; wrong amount; paid by other means.
  - ATM cash short or none.
  
  [B: Garanti BBVA; Kuveyt Türk; DenizBank; Akbank] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi); [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir); [DenizBank](https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz); [Akbank](https://www.akbank.com/kartlar/harcama-itirazi).
- **Checks before disputing.** The billing name may differ from the shop's sign; look at same-day purchases of similar amounts; a deferred payment may have come due; a free trial may have ended [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi).
- **Documents to collect:**
  - Product or service description, invoice or receipt, delivery proof, statements; photos or video of damage; email exchanges and the merchant's refund policy [B: İş Bankası] — [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir).
  - For a written dispute: date, amount, merchant, cardholder or supplementary holder's name and signature, one reason box, supporting documents (credit slip, cancellation number, police report, order number) [B: DenizBank] — [DenizBank](https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz).
- **Provisional credit.** No Turkish bank source states a provisional-credit practice. Akbank describes a "chargeback provizyonu" placed on the disputed amount during review [B: Akbank] — [Akbank](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek). *US comparison:* debit errors must be decided within 10 business days, or up to 45 days if the account is provisionally credited [L-US] — [12 CFR 1005.11](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11); credit-card billing-error notices are due within 60 days of the first statement showing the error [L-US] — [12 CFR 1026.13](https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.13). *UK:* Section 75 (credit purchases of £100–£30,000) runs alongside chargeback, and refused claims can go to the Financial Ombudsman [L-UK] — [Visa UK](https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html).

### Inferences
- [R] Route fraud and merchant disputes differently. **Fraud** ("bilgim dışında"): block and renew → fraud case → dispute → police report advice. **Merchant**: confirm the merchant was contacted (except fraud and clear processing errors) → right category → documents → expected time.
- [R] Never promise the outcome, a temporary credit, a timeline shorter than the bank's rules or "your money will come back". Never tell a customer to stop paying the statement because of a dispute; interest treatment of disputed amounts is bank-specific [V].
- [R] Tell customers early that disputes over 3DS-, PIN- or chip-approved transactions often fail as "not me" claims. Then check for a scam (authorised push or social engineering; researcher 10) rather than filing a weak fraud dispute.

### Gaps
- Mastercard's primary dispute guide was not accessible (403).
- Turkish banks' practice on provisional credit and on interest during disputes is not public.
- The BKM/TROY dispute rulebook is not public.

---

## 11. Recurring card payments and subscriptions: how to stop them

### Takeaway
In Türkiye, bank-held instructions (*otomatik ödeme talimatı*, usually for utility bills) are cancelled at the bank. Card-on-file subscriptions held by merchants have to be cancelled with the merchant; issuer stop services are scheme options and their availability in Türkiye is unverified. The UK gives a statutory right: the issuer must stop a continuous payment authority when asked. Card replacement may not stop recurring payments because of network token and account updates.

### Cited Findings
- **TR bank-held instructions.** An automatic payment instruction lets the bank pay bills (electricity, water, gas, internet, mobile, TV) from the account or credit card on set dates. It is cancelled in the app, internet banking or by phone under "Talimatlarım/Fatura Ödemeleri", or at a branch [B: ING] — [ING blog](https://www.ing.com.tr/tr/sizin-icin/blog/otomatik-fatura-odeme-talimati-hakkinda-bilmeniz-gerekenler). A legal secondary source says the instruction is cancelled in two places, at the bank and at the provider [V] — [kazimceylan.av.tr (snippet)](https://www.kazimceylan.av.tr/otomatik-odeme-iptal-dilekcesi).
- **UK (FCA, 23/06/2025).**
  - The customer can cancel through the business or the card issuer, and the issuer must stop the payments even if the business was not contacted, provided the request comes by the end of the business day before the payment.
  - Later payments are unauthorized and must be refunded immediately.
  - Recurring payments may continue on a new card.
  - Cancelling does not end the contract.
  
  [L-UK] — [FCA](https://www.fca.org.uk/consumers/recurring-card-payments). The FCA has reminded banks of these duties [L-UK] — [FCA press release (snippet)](https://www.fca.org.uk/news/press-releases/fca-reminds-banks-their-obligations-when-cancelling-continuous-payment).
- **Visa Stop Payment Service (VSPS).** Lets issuers stop eligible card-not-present card-on-file payments (recurring or installment) before authorization and clearing. It is optional, covers Visa credentials only, cannot stop transactions already cleared, and is separate from disputes [S] — [Visa Developer VSPS FAQ](https://developer.visa.com/capabilities/visa-stop-payment-service/frequently-asked-questions).
- **Cancelled trials.** Before disputing a recurring charge, check whether a free trial has ended [B: Garanti BBVA] — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi). After cancelling, the customer files "cancelled recurring" or "credit not processed" (Visa 13.7/13.6) [S] — [Chargeflow (2026)](https://www.chargeflow.io/blog/visa-chargeback-reason-codes).
- **Tokens.** A network token is refreshed on reissue, so merchant billing continues [S] — [ACI Worldwide (snippet)](https://www.aciworldwide.com/network-tokens).

### Inferences
- [R] Turkish handling: (1) Is it a bank instruction? Cancel it in the app or with the agent tool. (2) Is it a merchant subscription? Ask the customer to cancel with the merchant and keep proof. (3) If charges continue after cancellation, file a dispute (13.7/13.6-type). (4) If the bank supports a merchant block or stop-payment feature, offer it ([V] availability). (5) Card replacement alone is not a reliable way to stop a subscription.

### Gaps
- No Turkish regulation was found giving an issuer-side right to revoke merchant-held card mandates, comparable to the UK continuous payment authority.
- It was not confirmed whether any Turkish issuer offers VSPS or a Mastercard equivalent to customers.

---

## 12. Contact-reason playbook (10-point cards)

### Takeaway
Fifteen cards follow, each covering: (1) why customers contact, (2) what they experience, (3) what they provide, (4) what to determine, (5) clarifying questions, (6) checks and diagnostics, with **Auth** for the authentication level, (7) resolutions, with **Perm** for tool permission or human team, (8) what must not be promised or done, (9) escalation, (10) wording. Everything here is [R] unless a source is cited, and each card draws on its matching section above.

### Cited Findings
- Safety basis: never request PIN, CVV or OTP; banks do not ask for them by phone — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi); PCI SAD rule — [PCI SSC](https://www.pcisecuritystandards.org/pdfs/pci_fs_data_storage.pdf).

### Inferences

**Global rules [R].** Identify the card by last 4 digits or by selecting it inside an authenticated session; never take the full card number in chat. Read-only status needs standard authentication. Blocking needs minimal verification (protective). Unblocking, address or phone changes, PIN reset, limit changes, fee refunds and disputes need strong authentication plus tool permission. Disputes, fee refunds, manual hold releases and ATM claims are decided by back-office or specialist teams.

**C1 — Pending or "extra" amount, hold not released ("provizyon düşmedi", "iki kere çekilmiş")**
1. Unexpected reduction in available balance or limit; amount differs from the receipt. 2. Duplicate-looking entries; a hotel or rental deposit stuck. 3. Merchant name, date, amounts; sometimes a receipt. 4. Pending versus posted; hold matched or orphaned; estimate expected? 5. "Is the item marked pending (provizyon)?" "Hotel, car rental, fuel or online grocery?" "Has the merchant confirmed a cancellation?" 6. Authorization log, clearing match, merchant category, currency. **Auth:** standard. 7. Explain the hold life cycle and typical posting (Akbank: 1–3 business days); for orphaned holds past the validity window, ask the merchant for a reversal or open a back-office release request [V]. **Perm:** card-ops queue. 8. Do not promise a release date, do not call it a "double charge" before matching, do not open a dispute on a pending item (İş Bankası and Kuveyt Türk policy). 9. Hold past the scheme window, or a posted duplicate → card operations or disputes. 10. TR: "Bu tutar henüz kesinleşmemiş bir provizyon; işyeri işlemi tamamlayınca ya da iptal edince güncellenir. Kesinleştiğinde iki kez yansırsa itiraz başlatabiliriz." EN: "This is a temporary authorization hold, not a final charge…"

**C2 — Card declined (POS, online, abroad)**
1. Purchase failed. 2. Embarrassment, urgency, sometimes abroad. 3. Merchant, time, amount, error text. 4. Which decline family (§2 triage). 5. "Card or phone? Online or in store? In Türkiye or abroad? Did you get an SMS?" 6. Card status, controls, available limit including holds, missed-minimum closure, PIN or CVV counters, 3DS result, whether any authorization reached the bank. **Auth:** standard. 7. Customer-run fixes (open internet or abroad use in the app, use chip and PIN, wait for the limit to free up); verify and unblock if a risk hold applies. **Perm:** risk-unblock tool or fraud team. 8. Do not disclose risk-rule logic or override risk blocks without the required verification. 9. Repeated risk declines or a suspected account takeover → fraud (researcher 10); no issuer record → merchant or acquirer. 10. TR: "Kartınız internet alışverişine kapalı görünüyor; mobil uygulamada Kart Ayarları'ndan açabilirsiniz." / "İşlem güvenlik kontrollerimiz nedeniyle onaylanmadı; kimliğinizi doğruladıktan sonra yardımcı olabilirim."

**C3 — Online payment fails or 3DS code not received**
1. OTP missing, 3DS page error. 2. Checkout stuck, codes rejected. 3. Merchant, time, phone number (do not take the OTP). 4. E-commerce permission, phone on file, code timing, merchant error. 5. "Did you receive any SMS? Is your number up to date? Are you abroad?" 6. 3DS logs, card controls, SMS delivery status. **Auth:** standard; phone-number change needs strong authentication and secure channel (researcher 08). 7. Open the internet permission, update the number via a secure channel, retry with a different browser (Garanti BBVA). **Perm:** controls tool. 8. Never ask for or read back the OTP; do not change the phone number on the call without strong authentication. 9. Customer receives OTPs they did not request → fraud. 10. TR: "Doğrulama kodunu kimseyle, bizimle de paylaşmayın."

**C4 — PIN forgotten or blocked ("şifremi unuttum", "şifre bloke")**
1. Cannot withdraw or pay. 2. "PIN tries exceeded" at ATM or POS. 3. Card and channel used. 4. Lockout versus forgotten; attempts possibly by someone else. 5. "Did you enter it wrongly yourself? Is the card with you?" 6. PIN-try counter, card status. **Auth:** strong for any reset. 7. Self-service PIN set or unblock in the app, ATM, IVR or SMS per the bank's official page (Ziraat: activate a new PIN at a Ziraat ATM). **Perm:** none, or the IVR PIN flow. 8. Never hear, type or confirm a PIN; do not dictate SMS syntax containing card data. 9. Customer denies the wrong attempts → security incident. 10. TR: "Yeni şifrenizi yalnızca mobil uygulamadan veya ATM'den kendiniz belirleyin; şifrenizi hiçbir çalışanımıza söylemeyin."

**C5 — Card retained by ATM ("ATM kartımı yuttu")**
1. Card kept. 2. Stress, possible scam setup. 3. ATM location, bank, time. 4. Own-bank versus other-bank ATM, branch hours, suspicious circumstances. 5. "Was anyone near you or offering help? Did the screen ask for your PIN again?" 6. Card status, ATM incident log. **Auth:** minimal to block. 7. Own branch ATM during business hours → collect from the branch; otherwise block and renew (Garanti BBVA); Ziraat sends SMS instructions. **Perm:** block and renewal tool. 8. Do not promise the card will be returned; tell the customer not to accept bystander help. 9. Signs of trapping or skimming → fraud and ATM security. 10. TR: "Güvenliğiniz için kartınızı hemen kullanıma kapatıp yenisini gönderiyoruz."

**C6 — ATM cash not dispensed, partial dispense or deposit not credited ("ATM para vermedi ama hesaptan düştü", "para sıkıştı")**
1. Debited without cash, or a deposit is missing. 2. Urgent loss of funds. 3. ATM, time, amount, receipt or screen message. 4. Own-bank or other-bank ATM; withdrawal or deposit; card or QR. 5. "How much came out? Which bank's ATM? Was there an error message?" 6. Transaction and journal record, reversal status. **Auth:** standard. 7. Own bank → reconciliation (cash count) case; other bank or abroad → dispute (Ziraat, Akbank, DenizBank, Garanti BBVA categories). **Perm:** ATM-ops or dispute case tool. 8. Do not promise a day count for other-bank cases (they depend on the counterpart bank, per Ziraat); do not promise the full amount before the count. 9. Over the internal SLA or a large amount → ATM operations or complaints. 10. TR: "Kaydınızı oluşturduk; ATM sayımı/karşı banka incelemesi tamamlandığında sonucu SMS ile bildireceğiz."

**C7 — Lost or stolen card, temporary freeze**
1. Card missing. 2. Fear of fraud. 3. When last seen; recent transactions. 4. Freeze or block; any unknown transactions. 5. "Do you see any transactions you don't recognize? Might the card be at home?" 6. Recent authorizations, tokens. **Auth:** minimal to block, strong for redirecting the replacement. 7. Freeze (Garanti BBVA: 24 h, then auto-renewal) or block and renew; fraud case; police-report advice (Garanti BBVA). Liability per 5464 Art. 12. **Perm:** block, renew and fraud-case tools. 8. Do not tell the customer they are "fully covered" (the 150 TL cap does not apply with gross negligence); do not delay the block for sales or retention. 9. Unknown transactions → fraud. 10. TR: "Kartınızı şimdi kalıcı olarak kapattık ve yenisini kayıtlı adresinize gönderiyoruz."

**C8 — Card not arrived, activation, renewal, damaged card**
1. Waiting for a card, or the card does not work. 2. "Courier says insufficient address" (anecdotal). 3. Application date, address. 4. Production or courier status; activation done? 5. "Is your address current? Have you made a first chip-and-PIN transaction?" 6. Tracking, card status, activation flags. **Auth:** strong for an address change or redirect. 7. Redirect (VakıfBank-style), reissue, activate through app or ATM, replace a damaged card (free up to 2 per year per BDDK FAQ). **Perm:** card-ops. 8. Do not give tracking details before authentication; never tell the customer to hand the card back to a "courier" (Garanti BBVA warning). 9. Card shows delivered but not received → fraud check (card intercepted). 10. TR: "Kartınız kuryede görünüyor; adresiniz güncel değilse güvenli doğrulamadan sonra yönlendirme yapabiliriz."

**C9 — Contactless and mobile wallet**
1. Tap fails, PIN requested, Apple Pay unavailable. 2. Confusion about limits. 3. Amount, terminal, device. 4. Over 2,500 TL? Cumulative 5,000 TL reset (VakıfBank)? First chip-and-PIN done? Contactless turned off? 5. "What was the amount? Was the card used with chip and PIN before?" 6. Controls, counters. **Auth:** standard. 7. Explain the limit (BDDK 2,500 TL from 15 Jan 2026); toggle contactless; suggest the bank's Android NFC feature; Apple Pay not supported for Turkish cards (Apple list). **Perm:** controls. 8. Do not recommend unofficial wallet workarounds; do not promise when Apple Pay will arrive. 9. Card or chip fault → replacement. 10. TR: "2.500 TL üzerindeki temassız işlemlerde şifre istenmesi yasal limit gereğidir."

**C10 — Unrecognized transaction (possible fraud)**
1. "Bu harcamayı ben yapmadım." 2. Panic. 3. Merchant name, amount, date. 4. Real fraud versus a merchant descriptor, family member, subscription, trial or deferred payment (Garanti BBVA checks); was it 3DS- or PIN-approved? 5. "Is the card with you? Did you share any code? Could a family member or supplementary card have used it?" 6. Authorization method (3DS, PIN, chip, wallet), device and token, other recent activity. **Auth:** standard; block first. 7. Block and renew → fraud dispute → police report (Garanti BBVA) → handover to researcher 10's scam process if a code was shared. **Perm:** fraud team. 8. Do not promise a refund (3DS- or PIN-approved items "olumsuz sonuçlanmaktadır" per Garanti BBVA); do not reveal the detection logic. 9. Always fraud or card security. 10. TR: "Kartınızı güvenliğiniz için kapatıyorum; itirazınızı kart kuruluşu kurallarına göre inceleyeceğiz, sonucu yazılı olarak ileteceğiz."

**C11 — Merchant dispute and refund not received**
1. Not delivered, defective, wrong amount, duplicate, paid twice, refund missing. 2. Merchant unresponsive. 3. Order, invoice, emails, tracking, refund or cancellation proof. 4. Category; time window (120 days from the relevant date; TROY 180 days); merchant contacted? Refund older than 15 days (Kuveyt Türk)? 5. "When was delivery promised? Did you return the item? Do you have a cancellation number?" 6. Posted status, refund credit search, duplicate match. **Auth:** standard. 7. File in the correct category with documents (İş Bankası, DenizBank lists). **Perm:** dispute team. 8. Do not promise the outcome, a temporary credit or a timeline under 180 days; do not file on pending items. 9. Close to the deadline, high value, or a merchant gone out of business → dispute specialist. 10. TR: "Önce işyerinden iade talep etmenizi öneririz; sonuç alamazsanız belgelerinizle itirazınızı başlatalım. Süreç kart kuruluşu kurallarına göre 180 güne kadar sürebilir."

**C12 — Recurring payment or subscription**
1. Charges continue after cancellation. 2. Repeated debits. 3. Merchant, cancellation proof. 4. Bank instruction or merchant card-on-file; did charges come after cancellation? 5. "Did you set this up as a bank instruction or with the merchant? When did you cancel?" 6. Instruction list; merchant-initiated transaction flags. **Auth:** strong to cancel an instruction. 7. Cancel the bank instruction; merchant cancellation; dispute charges after cancellation (13.7/13.6); merchant block if available [V]. **Perm:** instructions tool, dispute team. 8. Do not claim a new card will surely stop it (tokens update); do not promise UK-style rights in Türkiye. 9. Merchant refuses and charges continue → disputes. 10. TR: "Bankamızdaki otomatik ödeme talimatınızı iptal ettim; işyerindeki aboneliği ise işyeri üzerinden iptal etmeniz gerekiyor."

**C13 — Travel and international use**
1. Going abroad; declined abroad; amount differs. 2. DCC confusion, foreign ATM failure. 3. Countries, dates, card brand. 4. Abroad enabled? TROY single-brand? DCC chosen? 5. "Which card (logo on the back)? Did the terminal offer payment in TL?" 6. Controls, brand, FX posting rule. **Auth:** standard. 7. Enable abroad use; recommend local-currency payment and declining DCC; explain conversion at clearing (Ziraat rule). **Perm:** controls. 8. Do not quote exchange rates as final; do not promise fee waivers. 9. Stranded customer with no card → urgent replacement or emergency process. 10. TR: "Yurt dışında POS 'TL ile ödemek ister misiniz?' diye sorarsa yerel para birimini seçmenizi öneririz."

**C14 — Credit-card account: limit, statement, minimum payment, installments, cash advance**
1. "Limitim neden düştü?", "asgari ne kadar?", "taksit yapılamıyor". 2. Reduced limit, card closed after a missed minimum, no installment option at checkout. 3. Statement or merchant details. 4. 2026 BDDK limit cuts; missed-minimum closure; sector installment ban. 5. "Which statement? Which merchant category?" 6. Limit history, payment history, merchant category. **Auth:** strong. 7. Explain the rule; minimum 20%/40% with the 100k TL threshold; offer ekstre erteleme or taksitlendirme if eligible (bank product). **Perm:** credit or collections (researcher 09). 8. Do not promise limit increases; do not quote rates (researcher 09). 9. Hardship or vulnerability → collections or vulnerable-customer path (researcher 11). 10. TR: "Asgari ödemenin yapılmaması nedeniyle kartınız nakit kullanımına kapatılmış; asgari tutarın ödenmesiyle yeniden açılır."

**C15 — Annual fee refund, supplementary card, loyalty points**
1. "Aidatımı iade edin", "ek kart limiti", "puanlarım silindi". 2. Fee posted, points expired. 3. Card, fee date. 4. Fee-free option offered? Inactivity of 180+ days? Supplementary fee no more than 50%? Point expiry rules. 5. "Do you use installments or points? Would a fee-free card suit you?" 6. Fee history, product. **Auth:** strong. 7. Offer a switch to a fee-free card with the same limit (BDDK FAQ); refund only within delegated authority; give arbitration channel information when asked. **Perm:** fee-refund permission or human. 8. Do not promise a refund; do not argue legality. 9. Formal complaint or arbitration threat → complaints team (researcher 04). 10. TR: "Dilerseniz kartınızı aynı limitle yıllık ücretsiz bir karta dönüştürebiliriz."

### Gaps
- Turkish banks' internal SLAs and their delegated fee-refund authority are not public. Verify against the institution's internal procedure.

---

## 13. Diagnostic matrix (how handling differs by problem domain)

### Takeaway
Classify every card contact into one of seven domains before acting. The domain decides what data to check, who owns the fix, what can safely be said, and the realistic timeline.

### Cited Findings
- Domain behaviours come from §§1–11: holds and reversals ([Visa ©2024](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf)), ATM objections ([Ziraat](https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/atm)), disputes ([İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir)), card status and controls ([Bankkart SSS](https://www.bankkart.com.tr/sikca-sorulan-sorular)).

### Inferences
| Domain | Typical symptoms | Check first | Owner | Safe explanation | Resolution path | Escalate when |
|---|---|---|---|---|---|---|
| Authorization | Declined; pending hold; amount reserved | Auth log, response category, available balance or limit, controls, 3DS | Card ops / risk | "Not approved due to X category" (no rule detail) | Self-fix of controls; verified unblock; retry | Repeated risk declines; ATO signs |
| Settlement / clearing | Posted ≠ pending; apparent duplicate; FX difference | Clearing vs auth match, posting date, FX rule | Card ops | "Final amount set when the merchant completed it" | Explain; dispute if a real error (12.x-type) | Posted duplicate or wrong amount |
| Card status | Not activated, frozen, blocked, expired, closed after missed minimum | Status flags, delinquency, replacement chain | Card ops / collections | "Card is currently closed for…" | Activate, unfreeze, pay minimum, reissue | Legal block (haciz), collections |
| Merchant processing | Refund missing, not delivered, recurring after cancellation | Refund credit search, merchant contact, dates | Customer → merchant → disputes | "Merchant must issue the refund; we can dispute" | Wait 15 days → dispute (13.x) | Deadline near; merchant gone out of business |
| ATM operations | Cash not dispensed or short; deposit jam; card retained | ATM journal, own vs other bank, reversal | ATM ops / reconciliation; disputes | "Count or investigation needed" | Own: reconciliation; Other: dispute (13.9) | Beyond SLA; repeated ATM faults |
| Technical | App or OTP failure, 3DS page error, network outage | Incident status, SMS delivery, versions | Digital support (researcher 08) | "Temporary technical issue" | Retry or alternate channel | Widespread outage |
| Security incident | Unknown transactions, OTPs not requested, retained card plus helper, delivered-not-received | Auth method, device or token, recent changes | Fraud (researcher 10) | "Securing your card now" | Block and renew, fraud case, police advice | Always |

### Gaps
- Mapping each domain to a real Turkish bank's team names and SLAs needs institution data.

---

## 14. Turkish terminology and real customer phrasings

### Takeaway
Agents need the Turkish operational vocabulary and must recognize colloquial complaint phrases. The phrases below are taken from forums and complaint sites and are anecdotal.

### Cited Findings
- **Glossary (sources as cited in sections above):**
  - Provizyon / bekleyen provizyon / açık provizyon = authorization hold / pending / open hold (Akbank; Ekşi).
  - Ön provizyon = pre-authorization; güvenlik provizyonu = estimate hold.
  - Harcama itirazı / ters ibraz = dispute / chargeback.
  - Hesap özeti / ekstre = statement; hesap kesim tarihi = statement date; son ödeme tarihi = payment due date.
  - Dönem borcu = statement balance; asgari ödeme tutarı = minimum payment.
  - Akdi faiz = contractual interest; gecikme faizi = late interest.
  - Taksit / taksitlendirme / sonradan taksitlendirme = installment / post-purchase installment conversion; ekstre erteleme = statement deferral.
  - Nakit avans = cash advance; limit aşımı = overlimit; kullanılabilir limit = available limit.
  - Kart aidatı / yıllık üyelik ücreti = annual fee; aidatsız kart = fee-free card.
  - Ek kart = supplementary card; asıl kart hamili = primary cardholder; sanal kart = virtual card.
  - Banka kartı / bankamatik kartı = debit card; ön ödemeli kart = prepaid card.
  - Temassız = contactless; şifresiz işlem limiti = no-PIN limit.
  - Kart yutma / alıkonma = card retention; para sıkışması = cash jam.
  - Kamu Ortak ATM = public-bank shared ATM network.
  - Kayıp/çalıntı bildirimi = lost/stolen report; geçici kapatma = temporary freeze.
  - İnternet alışverişine kapalı / e-ticaret yetkisi = e-commerce permission off / on; yurt dışı kullanım = usage abroad.
  - 3D Secure şifresi = OTP; Karekod = QR payments (TROY; İş Bankası).
  - Otomatik ödeme talimatı = standing bill-payment instruction; şifre blokesi = PIN lock.
- **Phrasings (anecdotal):**
  - "ATM parayı vermedi ama hesaptan bakiye düştü" — [Şikayetvar PTT](https://www.sikayetvar.com/ptt-bank/para-vermedi-hesaptan-dustu)
  - "Bankamatik paramı vermedi hesaptan düştü" — [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi/ziraat-bankasi-ortak-atm-parami-vermedi-hesaptan-dustu)
  - "3D SMS kodu bir türlü gelmiyor"; "İnternet Alışverişinde Reddediliyor" — [Şikayetvar 3D](https://www.sikayetvar.com/3d/sms-gelmiyor)
  - "iade edilen … ücretimi kartıma yansıtmayıp provizyonda bekletiyorlar" — [Şikayetvar DenizBank](https://www.sikayetvar.com/denizbank/iade/provizyon?page=2)
  - "kredi kartım Kuryenet tarafından bir türlü tarafıma teslim edilmedi" — [Şikayetvar Kuryenet](https://www.sikayetvar.com/kuryenet/kart-takip/kartim?page=8)
  - "kartım alışverişe kapalı" — [hesap.com (snippet)](https://hesap.com/hesap-defteri/kredi-karti-internet-alisverisine-nasil-acilir)
  - "ATM kartımı yuttu" — [Hürriyet](https://www.hurriyet.com.tr/egitim/atm-kartimi-yuttu-ne-yapabilirim-nasil-ve-ne-zaman-geri-alabilirim-ziraat-garanti-vakif-is-halk-ve-yapi-kredi-bankasi-42124420)
  - "Ben yapmadım" (category name) — [Garanti BBVA](https://www.garantibbva.com.tr/kartlar/islem-itirazi)
  - "Kartım bloke oldu" — [Bonus blog](https://www.bonus.com.tr/blog/kredi-karti-blokesi-nasil-kaldirilir)

### Inferences
- [R] Intent detection should map: "düştü/çekildi + vermedi" → C6; "yuttu/kaldı" → C5; "provizyon/bekliyor/iki kere" → C1; "yansımadı/iade" → C11; "ben yapmadım/bilgim dışında" → C10; "kapalı/reddediliyor" → C2/C3.

### Gaps
- No frequency data on these intents was found, and none is given.

---

## Source register

| # | Title | Publisher | URL | Date (pub./updated) | Jurisdiction | Type |
|---|---|---|---|---|---|---|
| 1 | Banka Kartları ve Kredi Kartları Kanunu (5464), consolidated | mevzuat.gov.tr | https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5464.pdf | Enacted 23/2/2006, RG 1/3/2006 no. 26095; amendments incl. 5915 (2009), 7192 (2019), 7247 (2020); accessed 2026-10-10 | TR | Law |
| 2 | Estimated & Incremental Authorization and Reversal Processing | Visa | https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf | ©2024 | Global/US | Scheme |
| 3 | Transaction Processing Rules (snippets only; PDF 403) | Mastercard | https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/transaction-processing-rules.pdf | Undated | Global | Scheme |
| 4 | DCC Performance Guide 2025 (snippet; PDF blocked) | Mastercard | https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/DCC-Guide-2025-Merchant-Version.pdf | 2025 | Global | Scheme |
| 5 | Authorization Hold: Time Limits… (snippet) | PaymentUSA | https://paymentusa.com/blog/authorization-hold | Undated | US | Industry |
| 6 | Provizyon Bekleyen Ödeme Ne Demek? | Akbank | https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek | 10.07.2025 | TR | Bank |
| 7 | Provizyon Nedir? (snippet) | Halkbank | https://www.halkbank.com.tr/tr/blog/provizyon-nedir | Undated | TR | Bank |
| 8 | Provizyon Ne Demek? (snippet) | Vakıf Katılım | https://www.vakifkatilim.com.tr/tr/hakkimizda/medya-merkezi/blog/detay/provizyon-ne-demek-provizyon-ne-kadar-surer | Undated | TR | Bank |
| 9 | Chargeback Nedir? ve Başvurusu Nasıl Yapılır? | İş Bankası | https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir | 08.08.2024 | TR | Bank |
| 10 | İşlem İtirazı – Harcama İtirazı | Garanti BBVA | https://www.garantibbva.com.tr/kartlar/islem-itirazi | Undated (acc. 2026-10-10) | TR | Bank |
| 11 | Harcama İtirazı (Chargeback) Nasıl Yapılır? | Kuveyt Türk | https://www.kuveytturk.com.tr/kendim-icin/kartlar/harcama-itirazi-chargeback-nasil-yapilir | Undated | TR | Bank |
| 12 | Harcama İtiraz | DenizBank | https://www.denizbank.com/kredi-karti/bireysel-bankacilik/harcama-itiraz | Undated | TR | Bank |
| 13 | Kredi kartı ve banka kartı harcama itirazı | Akbank | https://www.akbank.com/kartlar/harcama-itirazi | Undated | TR | Bank |
| 14 | Sıkça Sorulan Sorular | TROY (BKM) | https://www.troyodeme.com/tr/troy-hakkinda/sikca-sorulan-sorular | Undated (acc. 2026-10-10) | TR | Scheme |
| 15 | Bankamatik Para Sıkışması | İş Bankası | https://www.isbank.com.tr/bankamatik-para-sikismasi | Undated | TR | Bank |
| 16 | SSS – ATM | Ziraat Bankası | https://www.ziraatbank.com.tr/tr/sss/dijital-bankacilik/atm | Undated | TR | Bank |
| 17 | Bankkart Sıkça Sorulan Sorular (some figures stale) | Ziraat Bankası | https://www.bankkart.com.tr/sikca-sorulan-sorular | Undated (mixed currency) | TR | Bank |
| 18 | Ortak ATM Platformu (fee figures likely dated) | Halkbank | https://www.halkbank.com.tr/tr/dijital-bankacilik/atm/ortak-atm-platformu | Undated | TR | Bank |
| 19 | Ortak ATM | VakıfBank | https://www.vakifbank.com.tr/tr/dijital-bankacilik/atm/ortak-atm | Undated | TR | Bank |
| 20 | Devlet bankalarında 'ortak ATM' dönemi (snippet) | Anadolu Ajansı | https://www.aa.com.tr/tr/ekonomi/devlet-bankalarinda-ortak-atm-donemi/1195715 | c. 2018 | TR | Press |
| 21 | Bireysel Müşterilere İlişkin Ücretler (SSS) | BDDK | https://www.bddk.org.tr/Sss/Liste/114 | Undated | TR | Regulator FAQ |
| 22 | Mevzuat Detay 1210 (credit and installment board decisions) | BDDK | https://www.bddk.org.tr/Mevzuat/Detay/1210 | Lists decisions to 29.01.2026 | TR | Regulator |
| 23 | Temassız kartlarda şifresiz işlem limiti… 2.500 lira | Anadolu Ajansı | https://www.aa.com.tr/tr/ekonomi/temassiz-kartlarda-sifresiz-islem-limiti-15-ocaktan-itibaren-2-bin-500-lira-olacak/3787754 | 02.01.2026 | TR | Press (reports BDDK letter) |
| 24 | Temassız Ödeme Nedir? | VakıfBank | https://www.vakifbank.com.tr/tr/blog/temassiz-odeme-nedir | 2026 content | TR | Bank |
| 25 | Kredi kartlarında asgari ödeme tutarı değişti | TRT Haber (AA) | https://www.trthaber.com/haber/ekonomi/kredi-kartlarinda-asgari-odeme-tutari-degisti-958955.html | 02.10.2026 | TR | Press (reports BDDK) |
| 26 | Kredilerde kurallar değişti… BDDK'dan yeni kararlar | Bigpara/Hürriyet | https://bigpara.hurriyet.com.tr/haberler/ekonomi-haberleri/kredilerde-kurallar-degisti-bddkdan-yeni-kararlar_ID1624216/ | 31.01.2026 (upd. 01.02.2026) | TR | Press |
| 27 | Atm Kartımı Yuttu… | Hürriyet | https://www.hurriyet.com.tr/egitim/atm-kartimi-yuttu-ne-yapabilirim-nasil-ve-ne-zaman-geri-alabilirim-ziraat-garanti-vakif-is-halk-ve-yapi-kredi-bankasi-42124420 | 15.05.2026 | TR | Press |
| 28 | Güvenli Kart Kullanımı | Garanti BBVA | https://www.garantibbva.com.tr/dijital-bankacilik/guvenli-kart-kullanimi | ©2026 | TR | Bank |
| 29 | Önce Güvenlik: 3D Secure Nedir? | Garanti BBVA | https://www.garantibbva.com.tr/blog/3d-secure-nedir | 15.08.2023 | TR | Bank |
| 30 | Kartların İnternet Alışveriş Yetkisi | Maximum (İş Bankası) | https://www.maximum.com.tr/kartlarin-internet-alisveris-yetkisi | Undated | TR | Bank |
| 31 | Kredi Kartını Kullanıma Açma (snippet) | Bonus (Garanti BBVA) | https://www.bonus.com.tr/kredi-karti-kullanima-acmak | Undated | TR | Bank |
| 32 | Kredi Kartı Blokesi Nasıl Kaldırılır? | Bonus (Garanti BBVA) | https://www.bonus.com.tr/blog/kredi-karti-blokesi-nasil-kaldirilir | 29.09.2024 | TR | Bank |
| 33 | Kart Şifresi Alma (snippets) | Garanti BBVA; ING | https://www.garantibbva.com.tr/kartlar/kart-sifresi-alma ; https://www.ing.com.tr/tr/sizin-icin/kartlar/kart-sifresi-alma | Undated | TR | Bank |
| 34 | Güvenli Alışveriş (snippet) | Yapı Kredi | https://www.yapikredi.com.tr/bireysel-bankacilik/kartlar/guvenli-alisveris | Undated | TR | Bank |
| 35 | Kredi Kartı Başvuru / Kurye Takip | Vakıfkart (VakıfBank) | https://www.vakifkart.com.tr/ayricaliklar/firsatlar/kredi-karti-basvuru-kurye-takip | Oct 2026 content | TR | Bank |
| 36 | Otomatik fatura ödeme talimatı… | ING Türkiye | https://www.ing.com.tr/tr/sizin-icin/blog/otomatik-fatura-odeme-talimati-hakkinda-bilmeniz-gerekenler | Undated | TR | Bank |
| 37 | Countries and regions that support Apple Pay | Apple | https://support.apple.com/en-us/102775 | Accessed 2026-10-10 | Global | Wallet provider |
| 38 | EMV 3-D Secure | EMVCo | https://www.emvco.com/emv-technologies/3-d-secure/ | Accessed 2026-10-10 (lists 2026 items) | Global | Standards body |
| 39 | PCI Data Storage Do's & Don'ts; FAQ on CVC storage | PCI SSC | https://www.pcisecuritystandards.org/pdfs/pci_fs_data_storage.pdf ; https://blog.pcisecuritystandards.org/faq-can-cvc-be-stored-for-card-on-file-or-recurring-transactions | Undated | Global | Standards body |
| 40 | Card decline codes: complete list | Stripe | https://stripe.com/resources/more/a-complete-list-of-decline-codes | Undated | Global | Industry |
| 41 | Visa Decline Rules and Responses | CardPointe (Fiserv) | https://support.cardpointe.com/compliance/visa-decline-rules-and-responses/ | As of 22.10.2022 | US/Global | Industry |
| 42 | Purchase disputes – chargeback | Visa UK | https://www.visa.co.uk/how-you-pay-matters/chargeback-purchase-disputes.html | Undated | UK | Scheme (consumer) |
| 43 | Visa Chargeback Reason Codes (2026 Guide) | Chargeflow | https://www.chargeflow.io/blog/visa-chargeback-reason-codes | 2026 | Global | Industry |
| 44 | Recurring card payments | FCA | https://www.fca.org.uk/consumers/recurring-card-payments | 23/06/2025 | UK | Regulator |
| 45 | Visa Stop Payment Service FAQ | Visa Developer | https://developer.visa.com/capabilities/visa-stop-payment-service/frequently-asked-questions | Undated | Global | Scheme |
| 46 | Directive (EU) 2015/2366 (PSD2) Art. 71, 74 | EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366 | 2015 | EU | Law |
| 47 | Payment Services Regulations 2017, reg. 77 | legislation.gov.uk | https://www.legislation.gov.uk/uksi/2017/752/regulation/77 | 2017 | UK | Law |
| 48 | 12 CFR 1005.6, 1005.11 (Reg E) | eCFR | https://www.ecfr.gov/current/title-12/chapter-X/part-1005 | Current at access | US | Law |
| 49 | 12 CFR 1026.12, 1026.13 (Reg Z) | eCFR | https://www.ecfr.gov/current/title-12/chapter-X/part-1026 | Current at access | US | Law |
| 50 | CBPR2 currency-conversion transparency statement | European Commission | https://finance.ec.europa.eu/document/download/e19af922-a513-42a2-9bc2-b57baea97449_en?filename=200408-currency-conversion-transparency-requirements-statement_en.pdf | April 2020 | EU | Regulator |
| 51 | Debit Card Holds (snippet) | Georgia AG Consumer Protection | https://consumer.georgia.gov/consumer-topics/debit-card-holds | Undated | US | Consumer body |
| 52 | Network tokens (snippets) | ACI Worldwide; Very Good Security | https://www.aciworldwide.com/network-tokens ; https://www.verygoodsecurity.com/blog/posts/what-is-a-network-token | Undated | Global | Industry |
| 53 | Kredi kartı aidatlarının iadesi (snippet) | T.C. Ticaret Bakanlığı | https://ticaret.gov.tr/haberler/kredi-karti-aidatlarinin-iadesine-iliskin-basin-aciklamasi | Undated | TR | Ministry |
| 54 | Hakem heyeti… aidat iadesi (snippet) | Anadolu Ajansı | https://www.aa.com.tr/tr/ekonomi/hakem-heyeti-aidatsiz-kredi-karti-secenegi-sunmayan-bankanin-aidati-iadesine-karar-verdi/3041192 | c. 2023 | TR | Press |
| 55 | Ek kart hamilinin hukuki durumu (abstract) | TRDizin | https://search.trdizin.gov.tr/en/yayin/detay/220641/kredi-karti-sozlesmelerinde-ek-kart-hamilinin-hukuki-durumu | Undated | TR | Academic |
| 56 | Aggregators (taksit, provizyon, ortak ATM, kart hamili) — low authority | HesapKurdu | https://www.hesapkurdu.com/kredi-karti/rehber/kredi-kartinda-hangi-harcamalar-taksitlendirilir (and others cited) | Undated | TR | Aggregator |
| 57 | Refund timing (snippets) | Wise TR; obilet | https://wise.com/tr/help/articles/2935785/wise-kart%C4%B1ma-yap%C4%B1lan-bir-iade-ne-kadar-zaman-al%C4%B1r ; https://yardim.obilet.com/hc/tr/articles/5518330172828 | Undated | TR | EMI / merchant |
| 58 | Complaint wording (anecdotal) | Şikayetvar; Ekşi Sözlük; forums | URLs in §14 | Various | TR | Anecdotal |
| 59 | İş Bankası card-safety blog; Bankkart freeze (snippets) | İş Bankası; Ziraat | https://www.isbank.com.tr/blog/kart-guvenligi-nasil-saglanir | Undated | TR | Bank |
| 60 | Google Wallet/Apple Pay in Türkiye (anecdotal) | kartasistanim; Technopat | https://kartasistanim.com/rehber/apple-pay-turkiye ; https://www.technopat.net/sosyal/konu/google-pay-turkiyede-kullanilabilir-mi.3998624/ | 2026 | TR | Anecdotal |

---

## Open questions, unverified items and items needing institution-specific confirmation

1. **Provizyon release in Türkiye:** no regulatory maximum was found. Confirm each bank's automatic expiry for unmatched holds and whether agents can trigger a manual release.
2. **Mastercard validity windows and dispute time limits:** confirm 30 days for pre-authorizations, 7 days for final or undefined authorizations, and the 120-day dispute window from the current Mastercard rules (PDF access blocked).
3. **BDDK e-commerce closure (2016 instruction, 2018 deadline):** read the primary instruction; confirm whether new cards today are issued closed to e-commerce, abroad use or contactless by rule or by bank choice.
4. **Missed-minimum card closure:** the regulation (3 in a calendar year or 3 consecutive) and Ziraat's practice (1 → cash; 2 consecutive → purchases) differ. Confirm with the Yönetmelik text (researcher 02/09).
5. **Minimum-payment decision 11581 (01.10.2026):** verify the decision number and effective date on bddk.org.tr. Values are periodic.
6. **Installment matrix (sectors, counts, phone thresholds):** the 20k vs 40k TL thresholds conflict across sources. Check the latest BDDK decision.
7. **Contactless:** 2,500 TL is confirmed from 15 Jan 2026. Check for any later 2026 change; confirm the cumulative 5,000 TL rule is industry-wide and not only VakıfBank's.
8. **Liability cap:** 5464 Art. 12 still reads 150 (Y)TL. Confirm whether Law 6493 or the payment-services regulation sets a different consumer cap for cards (researcher 02).
9. **Supplementary-card liability:** confirm contract wording on joint or main-holder liability and the minimum age (Ziraat says 15+).
10. **Disputes in Türkiye:** provisional credit practice, interest treatment of disputed amounts, and BKM/TROY rulebook details are not public.
11. **ATM:** own-bank reconciliation SLA; retained-card custody and destruction policy and timeframes; whether private-bank shared-ATM alliances exist in 2026.
12. **Wallets:** Google Wallet availability for Turkish-issued cards (no primary source); token suspension on card replacement after fraud (bank and token-service settings).
13. **Recurring payments:** whether Turkish issuers offer merchant-level blocks, VSPS or a Mastercard equivalent; no Turkish statutory equivalent to the UK continuous payment authority was found.
14. **PIN attempt limits and unlock rules** per bank; SMS PIN-flow fields differ by bank and must only be referenced through official pages.
15. **Fees** (other-bank ATM, foreign transactions, cash advance): the figures seen (Kuveyt Türk 1% + 0.91 TL; Halkbank 1.15% + 1.04 TL) may be outdated. Hand to researcher 09.
16. **Authentication tiers and tool permissions** in the playbook cards are recommendations. Map them to the institution's actual authentication levels, delegated authorities and team names.
