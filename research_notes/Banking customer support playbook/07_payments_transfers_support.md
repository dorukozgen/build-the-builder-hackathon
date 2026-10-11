# Payments & transfers support (researcher 07): Türkiye (havale, EFT, FAST, Kolay Adres, TR Karekod) and international (SWIFT, SEPA, UK Faster Payments, US ACH/wires): lifecycle, status semantics, troubleshooting, recalls and misdirected payments

Date context: 2026-10-10. Research ran on 2026-10-10. Sources were read in English and Turkish.

Each statement carries a tag:
- **(1)** law or regulation
- **(2)** payment-system or scheme rule, or common industry practice
- **(3)** policy of a named bank
- **(4)** recommended service practice
- **(5)** assumption or item that needs verification
- **[anecdotal]** forum or complaint-site wording, used only to show real customer language

Jurisdiction labels are TR, EU, UK and US. Card refunds belong to researcher 06, fraud and scams to 10, authentication to 08, and legal frameworks to 02 and 03. This file covers them only where a transfer workflow needs them.

---

## 1. Türkiye domestic rails: havale vs EFT vs FAST vs Kolay Adres vs TR Karekod; hours, limits, name checks, delays and returns, fees

### Takeaway
Türkiye has three main ways to move TL between accounts:
- **Havale:** same-institution transfer, 24/7 and instant.
- **EFT:** interbank transfer through TCMB's real-time gross settlement system (RTGS). It runs only on business days. TCMB's systems are open 08:30–17:30 and until 13:00 on half-days, and each bank sets an earlier customer cut-off.
- **FAST:** TCMB's 24/7 instant system. **Since 26 Aug 2026 the per-transaction cap is 300,000 TL**, up from 100,000 TL. Larger transfers must go by EFT.

Kolay Adres (aliases, run by BKM) and FAST-TR Karekod (QR) are overlay services that start ordinary FAST payments. No law requires matching the payee name to the IBAN; payments are executed on the IBAN. Some receiving banks nevertheless return payments whose name does not match.

### Cited Findings

**System mechanics and hours**
- (2, TR) EFT is TCMB's RTGS for TL. The third-generation system has run since 2013, with separate customer and interbank components.
  - Hours: "hafta içi her gün 08.30-17.30… Yarım iş günlerinde ise saat 13.00'e kadar" (weekdays 08:30–17:30, half days until 13:00), except public holidays. TCMB may set different hours for customer payments.
  - Speed: interbank payments settle in under 1 second, and retail payments in about 30 seconds on average.
  - Delays in reaching the customer's account come from the sending and receiving banks' own workflows, so customers must contact those banks.

  — [TCMB EFT/EMKT/FAST page, accessed 2026-10-10](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Odeme+Sistemleri/Turkiyedeki+Odeme+Sistemleri/Elektronik+Fon+Transfer+%28EFT%29+Sistemi); [TCMB Ödemelerin Merkezi](https://odemelerinmerkezi.org/wps/wcm/connect/odeme+sistemleri/tr/tcmb+odeme+sistemleri)
- (2, TR) "Geri Dönülemezlik İlkesi" (irrevocability): payments posted to accounts cannot be cancelled in TCMB systems. "Hatalı ödemeler ancak alıcı banka tarafından iade edilebil[ir]" (erroneous payments can only be returned by the receiving bank), so customers apply to their own bank. — [TCMB EFT page](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Odeme+Sistemleri/Turkiyedeki+Odeme+Sistemleri/Elektronik+Fon+Transfer+%28EFT%29+Sistemi)
- (3, TR) Bank cut-offs differ:
  - İş Bankası: retail EFT on weekdays 08:30–17:00; corporate bulk files until 16:30; half-days 08:30–11:45. Outside these hours customers enter future-dated (ileri tarihli) EFTs. — [İş Bankası EFT](https://www.isbank.com.tr/eft)
  - Ziraat Katılım: 08:30–17:30 arrives the same day, and later orders are processed at the start of the next business day. Some banks offer a "geç EFT" (late window) with a different fee and limit. EFT typically takes minutes to 30 minutes. — [Ziraat Katılım, 2026-04-09](https://www.ziraatkatilim.com.tr/blog/havale-ve-eft-nedir-farklari-islem-saatleri-ve-iptal-sureci)
- (1, TR) Payment Services Regulation (Ödeme Hizmetleri… Yönetmelik, RG 01.12.2021 No. 31676; 2021 text):
  - Art. 58: an order received on a non-business day counts as received the next business day. The PSP may set a daily cut-off. For future-dated or periodic orders, the agreed day is the time of receipt, or the next business day if it is not one.
  - Art. 67: the payer's PSP sends the funds immediately, and at the latest by the end of the next business day. This can be one day longer for orders under a written contract. An agreed longer period may not exceed 4 business days, and other periods can be agreed where one PSP is abroad. The payee's PSP must make funds available by the end of the business day they arrive.

  — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (2, TR) FAST basics:
  - Operated by TCMB and separate from EFT. It runs 7/24, settles in seconds, and the funds are usable at once.
  - "Belirlenen süre aşımı içerisinde tamamlanmayan işlemler ise iptal olmaktadır" (transactions not completed within the timeout are cancelled), and both parties are notified of the result.
  - The pilot started on 18 Dec 2020 and customers got access on 8 Jan 2021.
  - Participants are banks, eligible payment and e-money institutions, and PTT.
  - TL only, and only between *different* institutions; same-institution payments are havale.

  — [TCMB](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Odeme+Sistemleri/Turkiyedeki+Odeme+Sistemleri/Elektronik+Fon+Transfer+%28EFT%29+Sistemi); [FAST SSS](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular)
- (2, TR) FAST limits:
  - Press release 2026-36 (24 Aug 2026): from **26 Aug 2026** transfers and Ödeme İste rise from 100,000 TL to **300,000 TL**, and FAST-TR Karekod merchant payments with dynamic verification rise from 250,000 TL to **300,000 TL**.
  - The FAQ adds a **5,000,000 TL** limit for the FAST Güvenli Ödeme İşlemi (escrow-like secure payment).
  - The limit "gelişen ihtiyaçlara göre revize edilebilmektedir" (can be revised as needs change).

  — [TCMB 2026-36](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2026/DUY2026-36); [FAST SSS](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular); [FAST nedir](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/fast%20nedir)
- (3, TR) Above the FAST limit, standard EFT is needed. — [Ziraat Katılım](https://www.ziraatkatilim.com.tr/blog/havale-ve-eft-nedir-farklari-islem-saatleri-ve-iptal-sureci). **Discrepancy:** the same page's table still shows 100,000 TL. TCMB is authoritative, so treat pre-26-Aug-2026 figures as stale.
- (2, TR) A FAST payment can start from an IBAN plus name/title, a Kolay Adres, a QR code, or the payer accepting an Ödeme İste request. For a wrong FAST payment, "finansal kuruluşunuz ile iletişime geçmeniz gerekmektedir. TCMB'nin iade işlemlerinde herhangi bir rolü bulunmamaktadır" (contact your financial institution; TCMB has no role in returns). — [FAST SSS](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular)
- (2, TR) Kolay Adresleme:
  - Launched in 2020 and operated by BKM.
  - Aliases: mobile number, e-mail, TCKN/YKN, VKN, passport number.
  - "Her kolay adres yalnızca bir hesap için kullanılabilir. Bir kişinin en fazla 5 kolay adres tanımı olabilir." (Each alias maps to one account; a person can hold at most 5.)
  - People register through their own institution. The payer enters only the alias, with no IBAN or name.

  — [FAST – Kolay Adresleme](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/kolay%20adresleme)
- (1/2, TR) Overlay services:
  - **TR Karekod** is the national QR standard under the "TR Karekod İlke ve Kuralları Rehberi" for payments under Law 6493. FAST-TR Karekod is used for person-to-person and merchant payments. A dynamic QR is single-use; a static QR is reusable.
  - **Ödeme İste** (Request to Pay, run by BKM) carries an expiry. The payer can accept or reject, and the creditor can cancel a request until it is accepted. In Models 2 and 4 an accepted request is executed automatically on a later date the creditor sets; billers use this.
  - **Güvenli Ödeme İşlemi** is for second-hand vehicle sales through a notary. Either party can cancel until registration.

  — [FAST SSS](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular); [Karekod](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/karekod); [Güvenli Ödeme](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/guvenli%20odeme)

**Name vs IBAN checks**
- (1, TR) Art. 69(1): a payment made to the identifier given counts as correctly executed. "Müşteri tarafından kimlik tanımlayıcıya ilave bilgiler verilmiş olsa dahi, ödeme hizmeti sağlayıcısı ödeme işleminin sadece kimlik tanımlayıcı ile gerçekleştirilmesinden sorumludur." (Even if the customer gives extra details such as a name, the PSP is responsible only for executing against the identifier.) — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm). A 2026 commentary still cites m.63, 64, 67, 69 and 70 as governing. — [Halil Bakırcı Hukuk, 2026-09-11](https://halilbakirci.av.tr/banka-para-transferini-reddedebilir-mi-odeme-emri-reddi-2026/)
- (1, TR, case law) Yargıtay HGK, E.2017/(19)11-941, K.2021/144, 23.02.2021: a bank has no duty to check the IBAN holder's name against the payee name the payer gave. The facts were a cross-border transfer to a fraudster's IBAN taken from a fake pro-forma invoice. The payer was at fault for not confirming the IBAN, and for repeating the transfer 20 days later without checking.
  - (5) The first-instance court had noted that in practice mismatched payments are "havuza alındığı ve birkaç gün sonra… iade edildiği" (pooled and returned a few days later). This was not the Assembly's holding.

  — [Karamercan Hukuk (decision text)](https://karamercanhukuk.com/yargitay-karari/bankanin-iban-ile-havale-alicisinin-isminin-ayni-olup-olmadigini-kontrol-etme-yukumlulugu-yoktur)
- [anecdotal, TR] Customers report both outcomes: correct IBAN with a wrong name rejected and returned ("IBAN doğru isim yanlış"), and wrong-name EFTs *not* returned. — [Şikayetvar](https://www.sikayetvar.com/vakifbank/eft/iban-dogru-isim-yanlis)
- (3, TR) İş Bankası requires the payee name in full; Turkish IBANs have 26 characters. — [İş Bankası](https://www.isbank.com.tr/eft). Some banking apps show the payee's name once the IBAN is entered, and customers should check it. — [Ziraat Katılım](https://www.ziraatkatilim.com.tr/blog/havale-ve-eft-nedir-farklari-islem-saatleri-ve-iptal-sureci)

**Refusals, holds and delays**
- (1, TR) Art. 63:
  - A PSP may refuse an order only if executing it would breach Law 5549 (AML) or other legislation, the regulation provides otherwise, or there is a justified reason.
  - It must give the reason and how to fix it at the latest by the end of the next business day, unless other laws bar this or there are objective security reasons.
  - A refused order "hiç alınmamış sayılır" (counts as never received).

  — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (5, TR) Transfer-purpose declarations, as reported in the press. The primary MASAK or TBB text was not found.
  - From 1 Jan 2026, transfers of 200,000 TL or more would need a declared purpose: one of 11 categories, or "Diğer" (other) plus at least 20 characters. Documents could be required at 20 million TL or more.
  - Later reports said the threshold became **400,000 TL from 15 Mar 2026**, counting single transfers or same-day totals on internet, mobile and ATM channels. Meaningless or insufficient explanations can mean the transfer is not approved.

  — [CNBC-e, 2025-12-27](https://www.cnbce.com/haberler/para-transferlerinde-yeni-donem-basliyor-masak-duzenlemesiyle-neler-degisecek-g22016); [CNN Türk, 2025-12-27](https://finans.cnnturk.com/finans-haberler/para-transferlerinde-yeni-donem-basliyor-1-ocaktan-itibaren-uyari-zorunlulugu-2377710); [İstiklal, 2026-02-22](https://www.istiklal.com.tr/ekonomi/ibana-para-transferinde-yeni-zorunluluk-limit-degisti-tarih-belli-oldu-1085379h)
- [anecdotal, TR] Common complaints:
  - "güvenlik kısıtına takıldığı için… iptal edildiği, EFT/havale ücretinin de iade edildiği söylendi ancak ana para günlerdir hesab[a dönmedi]" (stopped by a security restriction and cancelled; the fee was refunded but the principal had not come back for days).
  - "para hesabımdan düştü ancak karşı tarafa geçmedi… blokaj uyarısı aldım" (money left my account but never arrived, and I got a block warning).
  - EFTs to wallets, merchants and betting sites showing on the dekont but not credited to the merchant balance.

  — [Şikayetvar "eft hesaba geçmedi"](https://www.sikayetvar.com/eft-hesaba-gecmedi)

**Fees**
- (1/2, TR) Maximum FAST fees are set by TCMB communiqués on fees from financial consumers and commercial customers. Customers should ask their institution for the actual fee. — [FAST SSS](https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular)
- (3, TR, Garanti BBVA, rows updated Jan–Feb 2026, excluding BSMV):

| Transfer type and channel | 0–8,300 TL | 8,300.01–399,000 TL | Above 399,000 TL |
|---|---|---|---|
| FAST, mobile/internet | 7.97 TL | 15.96 TL | — |
| EFT, mobile/internet | 7.97 TL | 15.96 TL | 199.41 TL |
| EFT, branch/call centre | 39.87 TL | 79.76 TL | 797.68 TL |
| Havale, mobile/internet | 3.99 TL | 7.98 TL | 99.71 TL |

  - Transfers funded from a credit card add a 1% cash-advance fee plus interest.
  — [Garanti BBVA fees](https://www.garantibbva.com.tr/urun-ve-hizmet-ucretleri)

**Terminology (Turkish → English gloss)**
- Transfer types and identifiers: *havale* (same-bank transfer), *virman* (between one's own accounts), *EFT* (interbank TL transfer through TCMB), *FAST* (24/7 instant), *Kolay Adres* (alias), *karekod* (QR), *Ödeme İste* (request to pay).
- Documents and parties: *dekont* (transaction receipt), *gönderen/gönderici* (payer), *alıcı* (payee), *açıklama* (payment description), *sorgu/referans numarası* (trace or reference number).
- Timing and instructions: *ileri tarihli* (future-dated), *düzenli ödeme/EFT talimatı* (standing order), *otomatik fatura ödeme talimatı* (automatic bill-payment mandate), *valör* (value date), *mesai saatleri* (business hours), *yarım gün/arife* (half business day).
- Problems and outcomes: *iade* (return or refund), *iptal* (cancellation), *geri alma* (revocation), *mükerrer ödeme* (duplicate payment), *bloke/kısıt* (hold or restriction).
- International and legal: *muhabir banka* (correspondent bank), *masraf OUR/SHA/BEN* (charges option), *kambiyo* (foreign exchange), *BSMV* (banking transaction tax), *sebepsiz zenginleşme* (unjust enrichment), *ihtarname* (formal notice through a notary), *icra takibi* (enforcement proceedings).

### Inferences
- (4) Identify the rail first:
  - Same institution means havale (instant).
  - A different institution at or under 300k TL is usually FAST (7/24).
  - Above 300k TL, or a customer-chosen EFT, runs only in EFT hours.
  - So an evening or weekend "EFT gitmedi" (my EFT didn't go) above the cap is usually a queued order, not a lost payment.
- (4) FAST gives a definite result: completed, or cancelled at timeout. "Completed but the payee says it hasn't arrived" points to the payee's bank, for example a hold or crediting to a wallet or sub-account.
- (4) Under Art. 69 a name mismatch neither guarantees a return nor protects the payer. Never say "the wrong name means it will bounce."
- (5) The FAST cap applies system-wide, so a customer cannot have it raised. Bank channel limits are a separate matter.

### Gaps
- FAST timeout length and return-message mechanics: the "FAST Sistemi İşletim Kuralları" were not reached.
- No official source was found on whether Turkish receiving banks systematically check names and return mismatches.
- No Turkish equivalent of EU VoP or UK CoP was identified as of Oct 2026.
- The primary MASAK/TBB text behind the purpose-declaration rule was not found.
- No authoritative public source was found for new-device or new-payee transfer limits; these appear bank-specific.

---

## 2. Türkiye misdirected transfers ("yanlış IBAN'a para gönderdim")

### Takeaway
Once a transfer is credited, the bank **cannot reverse it on its own**. The payer's bank must take the necessary steps to recover it, and the payee's bank must cooperate. In practice that means a consent-based iade talebi (return request).

If the payee refuses or cannot be reached, the payer can:
- sue for unjust enrichment (TBK 77 and following; time-barred 2 years after learning of the claim and in any case 10 years after the enrichment)
- start enforcement proceedings
- possibly file a criminal complaint (TCK 160)

There are no guaranteed timelines or outcomes.

### Cited Findings
- (1, TR) Art. 69(2)–(4):
  - With a wrong identifier, the PSP is not liable.
  - "Gönderenin ödeme hizmeti sağlayıcısı, hatalı ödeme işlemine konu olan fonları geri almak için gereken işlemleri yapar" (the payer's PSP takes the steps needed to recover the funds). A reasonable, cost-based fee is allowed if the contract provides for it.
  - The payee's PSP "gerekli çabayı gösterir" (makes the necessary effort) in cooperation.
  - If the funds cannot be recovered, then on a **written request** the payer's PSP gives the payer all relevant information and documents it holds for legal action.

  — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (1, TR) Art. 70(4): on request, the payer's PSP investigates non-execution or wrong execution and reports back, and "ücret talep edilemez" (no fee may be charged). — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (3, TR) İş Bankası: a bank-caused erroneous EFT can be returned by the bank, but an EFT sent correctly to the IBAN and payee given is returned only with the payee's consent. — [İş Bankası EFT](https://www.isbank.com.tr/eft)
- (3, TR) Ziraat Katılım's steps:
  1. Call the bank immediately.
  2. "Bankanız alıcının bankasına iade talebi iletecektir" (your bank sends a return request to the payee's bank).
  3. The payee is informed.
  4. If the payee agrees, the money is returned; if not, a legal process for unjust enrichment follows.

  Cancelling an EFT "mümkün olabilir" (may be possible) only while the money has not yet reached the receiving bank. — [Ziraat Katılım](https://www.ziraatkatilim.com.tr/blog/havale-ve-eft-nedir-farklari-islem-saatleri-ve-iptal-sureci)
- (5, TR, law-firm commentary)
  - Banks cannot block or withdraw credited funds on their own; keeping them requires the payee's consent, a court order or an enforcement-office instruction.
  - Banks often decline to reveal the payee's identity, citing the Banking Law or KVKK (data protection).
  - Typical route: a notarised ihtarname (formal notice, 7–15 days), then *ilamsız icra* (enforcement without a judgment) or an unjust-enrichment lawsuit, or a criminal complaint (prosecutors can obtain the payee's identity).

  — [Harbiye Hukuk](https://www.harbiyehukuk.com/iban-ile-gonderilen-para-geri-alinir-mi/)
- (1, TR) TBK 6098:
  - Art. 77: return of enrichment without just cause.
  - Art. 78: a voluntary payment of a non-owed debt can be reclaimed only by proving the payer believed it was owed.
  - Art. 79: a good-faith recipient returns only what remains.
  - Art. 82: time-barred 2 years after learning of the right, and in any case 10 years after the enrichment.

  — [TBK](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6098.pdf)
- (1, TR) TCK 5237 Art. 160: someone who, instead of returning property "hata sonucu ele geçirilen" (obtained by mistake) or notifying the authorities, treats it as their own faces, on complaint, up to 1 year's imprisonment or a judicial fine. — [TCK](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5237.pdf)
- [anecdotal, TR] Customer experiences. Some cases are marked "Çözüldü" (resolved), so outcomes vary.
  - "İade numarası verdiler… birkaç gün içerisinde geri dönüş yapılacağını söylediler. Ancak hâlâ bir ses yok" (they gave me a return reference and said they'd respond in a few days; nothing since).
  - "paramı geri alamayacağım söylendi" (I was told I can't get my money back).
  - "Karşı taraf parayı çoktan çekmiş olabilir" (the other side may already have withdrawn it).
  - Sending to a saved IBAN of a deceased person and expecting it to bounce.
  - An e-money wallet saying "üyelerimize ulaşmamız imkansız" (we cannot contact our members).

  — [Şikayetvar](https://www.sikayetvar.com/yanlis-ibana-para-gonderme)

### Inferences
- (4) Process:
  1. Find the transaction and its status. Not yet sent means cancel. Sent but not credited means a receiving-bank return. Credited means a consent-based iade talebi.
  2. Screen for fraud. Did someone else supply the IBAN? Was there an "IBAN changed" e-mail? Was the customer pressured? If yes, it goes to Fraud.
  3. Lodge the request and give the customer the reference.
  4. Explain that it depends on the payee's consent, the written-request right to documents (Art. 69(4)), and the free investigation (Art. 70(4)).
  5. If refused, point the customer to independent legal advice. The agent gives no legal advice.
- (4) Nothing in Turkish rules sets a deadline for the payee's bank or the payee to respond (compare SEPA's 15 business days), so never promise one.
- (4) When our customer *receives* misdirected money: tell them not to spend it and to tell the bank, which handles the return. They should not send it back themselves, especially to a different account at a stranger's request, which is a scam and mule pattern; route that to Fraud.
- (5) Mention a recovery fee only if it appears in the contract or fee schedule.

### Gaps
- No public internal or TBB-level SLAs exist for iade talebi.
- No data on recovery rates; none should be invented.
- Practice on releasing payee identity under Art. 69(4), versus bank secrecy and KVKK, needs Legal to confirm.

---

## 3. International transfers: SWIFT and ISO 20022, gpi/UETR, correspondents, charges, cut-offs, compliance holds, recalls and returns, FX

### Takeaway
Since **22 Nov 2025**, cross-border Swift payment instructions are ISO 20022 (pacs.008 replaces MT103), with only contingency processing left for MT. The planned November 2026 removal of unstructured addresses was **deferred on 27 Aug 2026**, and Swift said it would announce the new timing by December 2026 at the latest.

gpi gives every payment a UETR and tracking. Swift reports about 60% credited within 30 minutes and almost 100% within 24 hours. Delays come from cut-offs, correspondents, missing cover, documents and sanctions screening.

The charge option (OUR, SHA or BEN) decides who pays, and intermediary fees can reduce what the payee receives. Recalls are *requests*. Once funds are credited they generally need the payee bank and the payee to agree, and FX loss and fees can reduce the amount returned.

### Cited Findings
- (2) "With the coexistence period ending on 22 November 2025… whether you're still using contingency processing or planning ahead for 2026." — [Swift ISO 20022 for FIs](https://www.swift.com/standards/iso-20022/iso-20022-financial-institutions-focus-payments-instructions). MT103/MT202 move to pacs.008/pacs.009. — [Kyriba FAQ](https://www.kyriba.com/resources/faqs/iso-20022-migration-frequently-asked-questions/)
- (2) Swift news, 27 Aug 2026 (updated 21 Sep 2026):
  - "Swift will defer all payments changes" in SR2026, including structured addresses. An update will come "by December, at the latest."
  - Non-payment parts go live on 12 June 2027.
  - The earlier plan had been that after 14 Nov 2026 only structured or hybrid addresses would be accepted.
  - End of coexistence reached "97% adoption rate after the big weekend".

  — [Swift](https://www.swift.com/news-events/news/swift-accepts-community-request-extend-structured-address-migration-iso-20022-payment-messages)
- (2) Swift GPI:
  - "Nearly 60%… credited… within 30 minutes and almost 100% within 24 hours."
  - The Tracker shows "why a payment was rejected".
  - Stop and recall: "the payment is stopped automatically and all other Swift GPI financial institutions in the payment chain are notified."
  - Since 22 Nov 2020, supervised institutions must confirm whether a customer transfer is "credited, on hold, or transferred outside of Swift".

  — [Swift GPI](https://www.swift.com/products/swift-gpi)
- (2/3) Status and reason codes:

  | Code | Meaning |
  |---|---|
  | ACSP (settlement in process) + G000 | Passed to next gpi agent |
  | ACSP + G001 | Passed to a non-gpi agent |
  | ACSP + G002 | May not settle today |
  | ACSP + G003 | Pending documentation |
  | ACSP + G004 | Pending funds |
  | ACSP + G006 | Delivered as non-gpi |
  | RJCT + AC01 / AC03 | Invalid account |
  | RJCT + AC04 | Closed account |
  | RJCT + AC06 | Blocked account |
  | RJCT + AG01 | Transaction forbidden on this account type |
  | RJCT + G004 | Missing cover |

  — [Goldman Sachs Developer](https://developer.gs.com/docs/services/transaction-banking/paymentstatusreasoncodes/)
- (2) Charges are MT103 field 71A, with ISO equivalents:
  - OUR = DEBT: the sender pays and the full amount is "helped" to arrive.
  - SHA = SHAR: deductions possible.
  - BEN = CRED: fees are taken from the amount.

  — [Flywire Help](https://help.flywire.com/hc/en-us/articles/360019759293-What-do-OUR-DEBT-BEN-CRED-and-SHA-SHAR-mean-in-the-fees-section)
- (3, TR) Bank practice:
  - İş Bankası: "masraf türüne (OUR/SHA/BEN) göre ek muhabir banka kesintileri olabilmektedir" (correspondent deductions may apply depending on the charges option); international transfers take 1–2 business days. — [İş Bankası SWIFT](https://www.isbank.com.tr/doviz-transferi-swift)
  - Yapı Kredi: orders before **16:45** on a business day get a value date 2 business days later; later orders can be future-dated. — [Yapı Kredi](https://www.yapikredi.com.tr/bireysel-bankacilik/odemeler-ve-hizmetler/swift-transfer)
  - Garanti BBVA (updated Jan–Feb 2026): outgoing FX transfer commission on mobile is 1,050–2,950 TL including BSMV, and "muhabir bankası masrafı ayrıca tahsil edilebilecektir… alıcının eline geçen tutar… daha düşük olabilir" (correspondent fees may be charged separately, so the payee may receive less). The inquiry/messaging fee is 190.48 TL plus BSMV. Incoming FX from another bank, at the branch, is 0.58% (minimum 1,038.10 TL, maximum 7,685.72 TL). — [Garanti fees](https://www.garantibbva.com.tr/urun-ve-hizmet-ucretleri)
- (1, TR) Art. 46: right after debiting, the payer's PSP must give the reference, payee information, amount, itemised fees, **the FX rate and converted amount**, and the date of receipt or debit. Art. 67(2): where a PSP is abroad, other execution periods can be agreed. — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (1, EU) PSD2 Title IV covers "one-leg" transactions (only one PSP in the EU) for the EU part, apart from listed articles. — [PSD2 Art. 2(4)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- (3, EU/FI) Nordea: "The sanction screening may result in delays in processing individual payments", and the bank may "demand further information on a payment". — [Nordea](https://www.nordea.fi/en/personal/our-services/accounts-payments/nordea-screens-transactions-against-sanctions-lists.html)
- (2, SEPA/Nordic) A positive recall is a return (pacs.004, reason FOCR). The payee bank may charge a fee, and "Currency conversion losses may be included in the Recall fee". — [NPC Clarification Paper v2.0, 2022-12-21](https://www.nordicpaymentscouncil.org/media/mmchrsnz/clarification-paper-rulebooks-v20.pdf). Likewise for SCT Inst: "The amount transferred back can differ from the Original Amount". — [ECB TIPS annex](https://www.ecb.europa.eu/paym/target/tips/governance/pdf/cr/ecb.tipscr210812_TIPS-0012-URD_Annex_1.en.pdf)
- (1, US) A remittance that misses its availability date is not an "error" when the delay comes from fraud screening, extraordinary circumstances, or (under the stated conditions) a wrong account number the sender gave. — [12 CFR 1005.33](https://www.consumerfinance.gov/rules-policy/regulations/1005/33/)
- (1 via press; 5 for the current status, TR) BSMV on FX purchases was cut back to **0.2%** on 30 Sep 2020, after rising to 1% in May 2020. — [Habertürk, 2020-09-30](https://www.haberturk.com/son-dakika-banka-bonosu-doviz-ve-altin-alim-satiminda-vergi-ne-oldu-haberler-2819385-ekonomi). A 2026 content site says 0.2% still applies on purchases only. — [Faturaport (non-authoritative)](https://faturaport.com/blog/vergi/kambiyo-vergisi-bsmv-nedir-2026). Banks apply their own buy/sell rates. — [Yapı Kredi](https://www.yapikredi.com.tr/bireysel-bankacilik/odemeler-ve-hizmetler/swift-transfer)

### Inferences
- (4) For "not arrived", get the UETR, value date and charges option, then read the status:
  - ACCC: credited by the payee bank; the payee should check with that bank.
  - G001 or G006: tracking may stop, so open an investigation.
  - G003: expect a request for information (RFI).
  - RJCT: the money returns, and fees or FX may change the amount.
- (4) Compliance holds: say "additional checks" and pass on the exact request only.
  - (5) AML laws (TR Law 5549 and equivalents) forbid disclosing that a suspicious-transaction report exists. Get Compliance-approved wording.
- (4) For TL→FX transfers, state the bank's selling rate and the conversion time (normally at order entry), fees, BSMV (to verify), and possible correspondent deductions. OUR reduces but may not remove deductions at the payee bank.

### Gaps
- No public industry statistics on recall success; none should be invented.
- MT contingency-processing fees and end date are not confirmed.
- The 2026 BSMV rate is not confirmed from the Resmî Gazete or GİB.
- Whether customers can track by UETR themselves varies by bank.

---

## 4. SEPA: SCT, SCT Inst, Instant Payments Regulation and Verification of Payee, SDD refunds, recall and RFRO

### Takeaway
**SCT** arrives by D+1. **SCT Inst** must complete within **10 seconds**, and if it does not, the payer's account is restored at once. Euro-area PSPs had to receive instant payments from 9 Jan 2025, and send them plus offer free **Verification of Payee (VoP)** from **9 Oct 2025**. Non-euro states follow in 2027.

Recall rules:
- **Recall** covers duplicate or technical errors within **10 business days**, and fraud within **13 months**.
- **RFRO** covers wrong IBAN, wrong amount, or a request without a stated reason, within **13 months**.
- The payee's PSP must answer within **15 business days**.
- Money already credited comes back only with the payee's consent, or where the payee's PSP is legally able to return it.

**SDD**: an unconditional refund within **8 weeks**, and **13 months** for unauthorised transactions.

### Cited Findings
- (1, EU) PSD2 (Directive 2015/2366):
  - Art. 83(1): credited to the payee's PSP by the end of the next business day.
  - Art. 80: irrevocable once received. Direct debits can be revoked until the end of the business day before the debit day, and future-dated orders until the end of the business day before the agreed day. Later revocation needs agreement, plus the payee's agreement for payee-initiated payments.
  - Art. 81: the full amount is transferred.
  - Art. 88: wrong unique identifier. The payer's PSP makes "reasonable efforts to recover", and the payee's PSP cooperates "also by communicating… all relevant information". On written request, the payer gets the information needed for a legal claim, and a fee is allowed if agreed.
  - Art. 89: on request, the PSP will "make immediate efforts to trace the payment transaction", free of charge.

  — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- (2, SEPA) 2025 SCT Rulebook v1.0:
  - Charges follow the shared principle.
  - Returns go back "within three Banking Business Days after Settlement Date."
  - Only the originator's PSP can recall, possibly on the originator's behalf. The windows are 10 business days for "Duplicate sending" and "Technical problems", and 13 months for "Fraudulent originated" transfers.
  - Only one recall is allowed per transaction.
  - The payee's PSP must respond within 15 business days, or it is in breach. After that the originator's PSP can ask for a status update.

  — [EPC SCT Rulebook 2025 (read via search extract)](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2024-11/EPC125-05%202025%20SCT%20Rulebook%20version%201.0.pdf)
- (2, SEPA/Nordic) RFRO:
  - Reasons: wrong IBAN, wrong amount, or "by request of the Originator without any reason specified". The debit date must fall within the 13 months before the request.
  - The payee's PSP must answer within 15 business days. If the payee has not replied, it sends a negative answer, "No response from the Beneficiary".
  - Payees can refuse, dispute the amount, or say they already returned the money.
  - A positive answer is a pacs.004 return. In a recall the payee's PSP can return "if legally possible (or on the basis of an agreement with the Beneficiary)"; an RFRO always needs the payee.
  - A payee can also send the money back with a new transfer (purpose code RRCT).

  — [NPC Clarification Paper](https://www.nordicpaymentscouncil.org/media/mmchrsnz/clarification-paper-rulebooks-v20.pdf)
- (5, SEPA) EPC's March 2026 consultation *proposes* extending the duplicate/technical recall window to 13 months. — [EPC008-26](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2026-03/EPC008-26%20SCT%20Scheme%20Rulebook%20-%20Public%20Consultation%20Document%20on%202026%20Change%20Requests.pdf)
- (1, EU) Instant Payments Regulation (Reg. 2024/886):
  - Art. 5a(4)(c): funds must be available to the payee "within 10 seconds of the time of receipt", and completion confirmed.
  - Art. 5a(5): if there is no confirmation, the payer's PSP "shall immediately restore the payment account of the payer".
  - Art. 5a(6): on request, users can set per-day or per-transaction instant limits and change them at any time. An over-limit order is not executed, and the user is told how to change the limit.
  - Art. 5a(3)(c): non-euro accounts are converted immediately after the order.
  - Art. 5c, VoP: performed before authorisation. A mismatch triggers a warning that funds may go to an account "not held by the payee". An "almost match" shows the real name. It must not stop the payer from authorising (5c(5)) and is free. Non-consumers sending bulk files may opt out. If the PSP fails to verify and the payment goes wrong, it must refund.
  - Recital 22: PSPs are not liable for wrong identifiers "insofar as PSPs correctly perform the service ensuring verification."

  — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400886)
- (1, EU) IPR deadlines, per the ECB:

  | Obligation | Euro area | Non-euro area |
  |---|---|---|
  | Receive instant payments | 9 Jan 2025 | 9 Jan 2027 (non-bank PSPs 9 Apr 2027) |
  | Send instant payments | 9 Oct 2025 | 9 Jul 2027 |
  | Price parity | 9 Jan 2025 | 9 Jan 2027 |
  | VoP | 9 Oct 2025 | 9 Jul 2027 |

  VoP outcomes are "match / close match / no match / other". Sanctions screening covers the PSP's own users at least daily. — [ECB IPR](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.en.html)
- (2, SEPA; industry blogs) The 2025 SCT Inst rulebook removed the €100,000 scheme cap. Under the IPR, PSP limits for SCT Inst may not be lower than for SCT. — [ACI Worldwide](https://www.aciworldwide.com/blog/sepa-instant-payments-whats-new-in-rulebook-2025-and-why-it-matters); [Numeral](https://www.numeral.io/blog/epc-2025-sepa-rulebook-updates)
- (1, EU) Refunds and complaints windows:
  - SDD: "an unconditional right to a refund" within **8 weeks** of the debit. The PSP refunds or justifies refusal within 10 business days, and cannot refuse in the unconditional SDD case (PSD2 Art. 76–77).
  - Unauthorised or incorrectly executed transactions: notify no later than **13 months** after the debit (Art. 71). Unauthorised amounts are refunded by the end of the next business day unless fraud is suspected and reported (Art. 73).

  — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- (5, EU) PSD3/PSR: political agreement on 27 Nov 2025 and final texts in April 2026. Official Journal publication was expected around mid-2026, and the PSR is expected to apply about 18 months later, with wider VoP-related liability at about 24 months. Verify. — [Worldline 2026](https://worldline.com/en/home/main-navigation/resources/blogs/2026/the-scope-and-timeline-are-locked-in-for-psd3-and-psr-what-should-psps-know); [Mondaq](https://webiis08.mondaq.com/ireland/financial-services/1780752/psd3psr-final-compromise-texts-are-published)

### Inferences
- (4) "No match" is a warning, not a block. If the customer proceeds, the PSP is generally not liable for the wrong payee but must still try to recover the money (Art. 88). Record what was displayed.
- (4) Check the execution date before choosing a route. A duplicate past 10 business days falls back to RFRO, which needs the payee's consent.

### Gaps
- EPC PDFs sit behind Cloudflare, so the exact SCT Inst 2025 recall wording comes from secondary extracts.
- No evidence was found that Turkish banks participate in SEPA. Euro transfers from Türkiye likely go through SWIFT (5).

---

## 5. UK Faster Payments, CoP and Credit Payment Recovery; US ACH, Fedwire, RTP/FedNow and the Remittance Rule

### Takeaway
**UK:**
- Faster Payments are near-instant, with a scheme cap of £1m and lower bank limits. They cannot be cancelled once sent.
- Misdirected payments go through the industry **Credit Payment Recovery** process: reasonable efforts by the bank, and the payee's details on written request so the customer can go to court.
- Confirmation of Payee checks names.
- Since 30 Oct 2024, PSPs may delay suspicious outbound payments for up to **4 business days**.

**US:**
- ACH returns use R-codes, generally within 2 banking days, and 60 days for unauthorised consumer debits.
- Originator *reversals* are only for sender errors, within 5 banking days, and never for fraud.
- Fedwire is final and irrevocable. RTP and FedNow allow up to $10m.
- Consumer remittances abroad carry a **30-minute cancellation right** and **180 days** to report errors.

### Cited Findings
- (2, UK) Pay.UK on Faster Payments:
  - Funds are "usually available almost immediately, although they can sometimes take up to two hours".
  - Online payments, including standing orders, must arrive "by the end of the following business day".
  - "once sent Faster Payments cannot be cancelled".
  - Banks follow "the Credit Payment Recovery process".
  - Fewer than 0.1% of accounts cannot receive Faster Payments.

  — [Pay.UK](https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/how-faster-payments-work/)
- (2/3, UK) Individual payments of up to £1 million are possible, but each organisation sets its own limits; for example Access Bank UK's online personal limit is £10,000. — [Pay.UK limits](https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/transaction-limits/)
- (2, UK) CoP launched in 2020, with more than 300 organisations and over 2m checks a day. The PSR mandated its expansion in 2024. It also indicates whether the account is personal or business. — [Pay.UK CoP](https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/)
- (1/regulator guidance, UK) The FCA:
  - For a wrong sort code or account number, the bank "must make a reasonable effort… But it won't be liable". If that fails, the customer can ask for the payee's details "in writing" and go to court.
  - A bank error means a full refund plus charges and interest.
  - A wrong amount must be corrected.

  — [FCA](https://www.fca.org.uk/consumers/making-receiving-payments)
- (3, UK, HSBC UK) Misdirected payments:
  - Customers have 36 months to claim, and the bank acts within 2 working days.
  - With no dispute, the money returns "within 20 working days"; with a dispute, the customer gets the outcome within 20 working days.
  - Payments to closed or invalid accounts "are automatically rejected and returned… a few days".
  - Extra fraud checks can slow a transfer.

  — [HSBC UK](https://www.hsbc.co.uk/current-accounts/online-transfer-mistake/)
- (1, UK) The Payment Services (Amendment) Regulations 2024 apply from 30 Oct 2024. Outbound authorised push payments can be delayed for up to 4 business days on reasonable grounds to suspect fraud, and the payer must be told of the delay, the reason and what is needed. — [FCA FG24/6](https://www.fca.org.uk/publication/finalised-guidance/fg24-6.pdf). The PSR's APP-scam reimbursement started on 7 Oct 2024, capped at £85,000, with an excess of up to £100 (none for vulnerable customers) (lane 10). — [Regulation Tomorrow](https://www.regulationtomorrow.com/2024/10/psr-issues-policy-statement-confirming-maximum-level-of-reimbursement-for-faster-payments-app-scams/)
- (2, UK) The Direct Debit Guarantee gives a "full and immediate refund" for errors. — [directdebit.co.uk](https://directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/). A secondary source says no time limit applies. (5)
- (2, US) Common ACH returns:
  - R01 insufficient funds, R02 closed, R03 no account, R04 invalid, R08 stopped, R09 uncollected: within 2 banking days.
  - R05, R07, R10 (unauthorised or revoked): up to 60 days for consumers.

  — [Plaid](https://plaid.com/resources/ach/ach-return/) (verify against the Nacha Rules)
- (2, US) Nacha on reversals: they are for sender errors only (a duplicate, wrong amount, wrong date or wrong account). A reversal "cannot be used to reverse a fraudulent payment" and must go out within 5 banking days. If funds are gone, the reversal itself is returned. International ACH transactions (IAT) cannot be reversed. — [Nacha, 2026-08-06](https://www.nacha.org/news/second-chance-understanding-ach-reversals)
- (2, US) Timing and limits:
  - From 18 Sep 2026 all non-Same-Day ACH credits must be available by 9 a.m. local time. — [Nacha, 2026-09-01](https://www.nacha.org/news/new-funds-availability-requirements-take-effect-sept-18)
  - Same Day ACH is capped at $1m and rises to $10m on 17 Sep 2027. — [Bloomberg Tax](https://news.bloombergtax.com/payroll/same-day-ach-limit-rising-to-10-million-in-2027)
  - Fedwire is "immediate, final, and irrevocable". — [Federal Reserve](https://www.federalreserve.gov/paymentsystems/fedfunds_coreprinciples.htm)
  - RTP rose to $10m on 9 Feb 2025, and FedNow to $10m in Nov 2025; participants may set lower limits. — [ABA, Dec 2024](https://bankingjournal.aba.com/2024/12/rtp-network-to-raise-individual-transaction-limit-to-10m/); [ABA, 2025-09-15](https://bankingjournal.aba.com/2025/09/fednow-to-raise-transaction-limit-to-10m/)
- (1, US) Reg E Subpart B, the Remittance Rule:
  - It covers transfers over $15. A provider is outside the rule if it made 500 or fewer remittances in both the previous and the current year. — [1005.30](https://www.consumerfinance.gov/rules-policy/regulations/1005/30/)
  - **Cancellation within 30 minutes of payment**, if the funds have not been picked up or deposited. Everything, including fees and, where lawful, taxes, is refunded within 3 business days. Transfers scheduled 3 or more business days ahead are excepted. — [1005.34](https://www.consumerfinance.gov/rules-policy/regulations/1005/34/)
  - Errors must be reported within **180 days** of the disclosed availability date, and the provider decides within **90 days**. Remedies are a refund or resending at no cost.
  - If the sender gave a wrong account number and the stated conditions are met, the provider must "promptly use reasonable efforts to recover" the money. — [1005.33](https://www.consumerfinance.gov/rules-policy/regulations/1005/33/)

### Inferences
- (4) Keep three things apart: a *return* (by the receiving bank), a *reversal* (by the originator, for its own error, ACH only) and a *recall or return request* (consent-based).
- (4) If a US consumer sent money abroad within the last 30 minutes, offer cancellation **immediately**.

### Gaps
- Misdirected-payment positions for P2P apps (Zelle and others) were not researched.
- The Nacha rules were not read in the primary text.
- Fedwire 2026 hours and RTP/FedNow return-request mechanics were not confirmed.

---

## 6. Lifecycle and status semantics; "debited but not received"; minimum investigation data; payment operations vs fraud

### Takeaway
An AI agent must use status words precisely:
- **Rejected:** never executed; the order counts as not received.
- **Returned:** sent back after settlement.
- **Reversed:** the originator or bank is correcting its own error.
- **Recall requested:** not the same as **recalled**.
- **Refunded:** money given back under a right or by a merchant.

"Debited but not received" follows a fixed check sequence. Data collection stays minimal, inside an authenticated session, and never includes credentials. Any payment influenced by a third party goes to Fraud.

### Cited Findings
- (2) ISO/gpi codes (ACSP, ACCC, RJCT) are listed above. — [Goldman Sachs](https://developer.gs.com/docs/services/transaction-banking/paymentstatusreasoncodes/). Universal confirmations report "credited, on hold, or transferred outside of Swift". — [Swift GPI](https://www.swift.com/products/swift-gpi)
- (1, TR) A refused order counts as never received, and the reason is due by D+1 unless legally restricted (Art. 63). The payee bank credits funds the day they arrive (Art. 67(4)). Investigations are free (Art. 70(4)). — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (2, TR) FAST cancels transactions at timeout and notifies both parties. — [TCMB](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Odeme+Sistemleri/Turkiyedeki+Odeme+Sistemleri/Elektronik+Fon+Transfer+%28EFT%29+Sistemi). (1, EU) SCT Inst restores the payer's account when there is no confirmation within 10 seconds. — [Reg. 2024/886 Art. 5a(5)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400886)
- (2, US) Nacha: "A reversal corrects an ACH payment error made by the sender… A return is… sent back because it could not be accepted by the receiving financial institution." — [Nacha](https://www.nacha.org/news/second-chance-understanding-ach-reversals). (2, SEPA) A recall or RFRO request is a camt.056; a positive answer is a pacs.004/FOCR return and a negative one a camt.029. — [NPC](https://www.nordicpaymentscouncil.org/media/mmchrsnz/clarification-paper-rulebooks-v20.pdf)
- (1, TR) Dekont and confirmation content under Art. 46:
  - (2) For the payer: reference and payee information, amount, itemised fees, FX rate and converted amount, and the date of receipt or debit.
  - (3) For the payee: amount, fees, FX rate, and the date funds were made available.
  - (4) This information free of charge at least monthly.
  - (5) Measures so that the counterparty can identify the customer, for example by business name or brand.

  — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- [anecdotal, TR] Customers quote the "EFT sorgu numarası" (EFT inquiry number) and dekont references, and complain "dekontta 'Tamamlandı'… görünmesine rağmen… hesabıma geçmedi" (the dekont says completed but it isn't in my account). — [Şikayetvar](https://www.sikayetvar.com/eft-hesaba-gecmedi)
- (1, TR) KVKK Art. 4(2)(ç): data must be "işlendikleri amaçla bağlantılı, sınırlı ve ölçülü" (relevant, limited and proportionate). — [KVKK 6698](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf). (1, EU) IPR recital 21 requires VoP name disclosure to comply with GDPR. — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400886)
- (1, UK) A delayed outbound payment must be explained to the payer: the delay, the reason and what is needed. — [FCA FG24/6](https://www.fca.org.uk/publication/finalised-guidance/fg24-6.pdf)

### Inferences

#### Status vocabulary (4: map each internal code to one of these)

| Status | TR | Meaning | Agent may say | Must not say |
|---|---|---|---|---|
| Initiated | talimat alındı | Received; not necessarily executed | "Received at [time]." | "It's been sent." |
| Authorised | onaylandı | Customer authenticated and confirmed | "You confirmed it at [time]." | — |
| Pending / scheduled | beklemede, ileri tarihli | Future date, outside EFT hours, limit, compliance or fraud review, or funds check | "Scheduled for [date]" or "Under a standard check; update by [internal SLA]." | The screening reason, unless Compliance has approved it |
| Sent / settled | gönderildi | Left our bank and settled to the payee bank | "Left our bank at [time], reference [x]; the payee bank credits the account." | "It's in their account." |
| Completed / credited | tamamlandı | Payee bank confirmed (FAST result, gpi ACCC) | "The payee bank confirmed crediting at [time]." | — |
| Rejected | reddedildi | Not executed; funds not taken or restored | "Not executed because [reason if disclosable]; funds restored on [date]." | "Returned." |
| Returned | iade edildi / geri döndü | Sent back after settlement | "Came back on [date]; the amount may differ (fees or FX)." | "It never left." |
| Reversed | düzeltme / ters kayıt | Correction of a bank or originator error | "We corrected a processing error." | Use for a consent-based return |
| Return requested | iade talebi iletildi | Request with the payee bank | "Outcome depends on [payee bank / payee consent]." | "Back in X days." |
| Refunded | geri ödeme | Paid back under a right (SDD, unauthorised) or by a merchant or biller | "A refund of [amount] was credited on [date]." | — |

#### "Debited but not received" checks (4)
1. Authenticate the customer, then find the transaction (date, amount, payee).
2. Read the status and the rail.
3. Check timing: the bank's own cut-off (for example 17:00 at İş Bankası) as well as TCMB's 17:30; business day, holiday or half-day; future date; value date.
4. Look for a hold or refusal flag: limit, purpose declaration, fraud or compliance review, insufficient funds.
5. Get the reference: EFT/FAST reference or sorgu number, the UETR, or the SEPA end-to-end ID.
6. Check for a pending return. SEPA returns can take 3 business days; UK closed-account returns take "a few days".
7. If credited: send the dekont and reference and ask the payee to contact their bank (hold, or crediting to a wallet or sub-account).
8. If still unclear: open a free trace (TR Art. 70(4); EU Art. 89) with payment operations. Set an expectation and promise no outcome.

#### Minimum investigation data (4)
- **Collect:** within an authenticated session: date and time, amount, currency, channel, transfer type; the payee's name and bank; the **masked** IBAN (last 4 characters); the description; the dekont or reference/sorgu number; for SWIFT, the UETR, value date and charges option. For incoming funds that are missing, the payer's name and bank, date, amount and reference or UETR, with the payer asking *their* bank for a trace.
- **Never collect:** PIN, password, OTP/SMS codes, CVV/CVC, full card numbers, or remote access to the device.
- **Never disclose:** the payee's identity, except through the written-request or legal routes (TR Art. 69(4); FCA).

#### Routing (4)
- **Payment operations / investigations:** traces, returns, iade talebi, recalls, gpi cases, bank-caused duplicates or wrong amounts.
- **Fraud team, immediately:**
  - The customer followed a third party's instructions: a "bank/police" call, a "safe account", an investment, crypto or marketplace seller, or an IBAN change by e-mail.
  - The customer did not authorise the payment.
  - The app was blocked after the transfer.
  - The customer received unexpected money with a request to send it on.
  - Possible mule activity.
- **Compliance:** RFIs, sanctions holds, MASAK purpose or document requests. The agent relays the request only.
- **Complaints:** dissatisfaction or missed deadlines.
- **Legal:** court or prosecutor orders, and payee-identity requests.

### Gaps
- The mapping from internal status codes to these labels is institution-specific.
- The exact AML/fraud hold wording permitted in Türkiye (the Art. 63(2) exception versus Law 5549 non-disclosure) needs a Compliance-approved script.

---

## 7. Scenario playbooks: missing, delayed, pending, rejected, returned, duplicated, misdirected, incorrect amount, limits, standing orders, direct debits and automatic bill payments, bill-payment failures, dekont, merchant payments (transfer side)

### Takeaway
Most contacts resolve once the agent has identified the rail and its timing rules, read the precise status, and set honest expectations. Recovering money after it is credited depends on consent in every jurisdiction studied: TR Art. 69, EU Art. 88 and RFRO, the UK CRP, US reversals that exclude fraud, and Fedwire finality. Errors made by the bank, by contrast, must be corrected by the bank (TR Art. 70, EU Art. 89, FCA).

### Cited Findings (anchors)
- (1, TR) Art. 64: an order cannot be revoked once received, unless agreed. Direct debits can be revoked until the end of the business day before the debit day; future-dated or periodic orders until the end of the business day before the agreed day. After that, revocation needs agreement, plus the payee's consent for payee-initiated payments, and a cost-capped fee is allowed if contracted. — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (1, TR) Art. 56: a payee-initiated payment authorised without an exact amount, where the amount exceeded what was reasonable, can be refunded on request within **2 months**, and the PSP decides within **10 business days**. A wider direct-debit refund can be *contracted*. There is no unconditional 8-week right as in the EU. — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (1, TR) Art. 54(1): unauthorised or wrongly executed transactions must be notified without delay and within **13 months**, or at any time if the required information was not given. The burden of proof is on the PSP. (2021 text; amounts in Art. 54(4) may have been amended.) Art. 65(1): no deductions from the transferred amount; the order may be refused if the remaining balance cannot cover the fee. — [RG 31676](https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm)
- (3, TR, Kuveyt Türk) Automatic bill payment:
  - Collected on the bill's last payment date.
  - "yeterli bakiye olmaması durumunda tahsilât gerçekleşmez… fatura ödenmemiş sayılır" (with insufficient balance, nothing is collected and the bill counts as unpaid).
  - A duplicate (mükerrer) is a manually paid bill collected again by the instruction, and a refund can be requested.
  - Instructions activate within 1 business day and can be cancelled in the app.
  - If the bank causes the error, the bank covers late fees.

  — [Kuveyt Türk](https://www.kuveytturk.com.tr/kendim-icin/odemeler-ve-hizmetler/odemeler/fatura-odemeleri-ve-talimatlar)
- (3, TR, Garanti BBVA) No fee on automatic-payment-instruction collections. Standing EFT and havale use the same fee tiers as one-off transfers. — [Garanti fees](https://www.garantibbva.com.tr/urun-ve-hizmet-ucretleri)

### Inferences: playbooks (tag 4 unless marked)

Every playbook needs an authenticated session before transaction-specific details are discussed.
- **Tool permissions** are needed to: cancel future-dated or standing orders, lodge an iade talebi, recall or trace, change limits, cancel automatic instructions, and issue a dekont.
- **Human or specialist teams** handle: SWIFT investigations, legal and payee-identity requests, compliance RFIs, fraud, and fee or goodwill refunds (5: confirm per institution).

**7.1 Missing or delayed** ("EFT gitmedi", "para karşıya geçmedi", "hesabımdan düştü ama karşıya geçmedi", "FAST yaptım hesaba geçmedi", "dekontta tamamlandı yazıyor")
- *Why customers contact:* the payee or a merchant has not received the money, or the customer is anxious about a large amount.
- *Determine:* the rail, the timing compared with cut-offs, the status, any hold, refusal or return, and whether the payee is a wallet or merchant sub-account.
- *Ask:*
  - "FAST, EFT, or within our bank?"
  - "Exact time and amount?"
  - "To a person, or to a company, app or wallet?"
  - "Did the screen say completed, or scheduled?"
- *Check:* the section 6 sequence.
- *Resolve:*
  - Queued: explain the timing.
  - Completed: send the dekont and reference, and refer the payee to their bank or the merchant.
  - Not executed: explain why and re-send.
  - Unclear: open a free trace.
- *Never promise:* an arrival time, or that the payee bank will act by a certain time.
- *Escalate:* sent more than 1 business day ago and still not credited (TR Art. 67) → payment ops. App block or fraud flag → Fraud.
- *Wording:*
  - EN: "Your transfer left our bank at 14:05 with reference ###. The receiving bank credits the account; please ask the recipient to quote this reference to their bank. If it's not credited by [time], we'll open a trace at no charge."
  - TR: "Transferiniz 14:05'te ### referansıyla bankamızdan çıkmıştır; hesaba geçirme alıcı bankada yapılır. Alıcının bu referansla bankasına başvurmasını rica ederiz; [saat] itibarıyla geçmediyse ücretsiz araştırma kaydı açacağız."

**7.2 Pending or held** ("işlem beklemede", "güvenlik kısıtına takıldı")
- *Determine:* future date or outside EFT hours; limit; purpose declaration missing or rejected at 400k TL or more (5); fraud or AML review; insufficient funds.
- *Ask:* "Were you asked for a description or documents?" and "Did anyone ask or guide you to make this payment?"
- *Resolve:* explain scheduling; help with a meaningful description or the required documents; hand over to Fraud or Compliance.
  - (1, TR) A refusal reason is due by D+1 unless legally restricted (Art. 63).
  - (1, UK) A fraud delay can last up to 4 business days and must be explained.
- *Never:* speculate about AML matches; coach wording to get through checks; ask for OTPs; promise a release time.
- *Escalate:* any third-party influence → Fraud. Document requests → Compliance.
- *Wording (TR):* "İşleminiz standart bir kontrol nedeniyle beklemede. Sizden istenen bilgi/belge şu: … Süre veya sonuç garantisi veremiyoruz; ilgili ekip sizi bilgilendirecek."

**7.3 Rejected** ("işlem reddedildi", "gerçekleşmedi")
- *Determine:* where it was rejected. In our bank (limit, balance, failed authentication, compliance) means funds were never taken. At the scheme or payee bank it may be a FAST timeout or an ISO RJCT (AC01, AC04, AC06).
- *Resolve:* confirm the funds were not taken or have been restored; explain the fixable cause; re-send with corrected details. For SWIFT RJCT, warn about FX and fees.
- *Never:* call it "returned", or promise that re-sending to the same details will work.
- *Wording (EN):* "The payment wasn't executed, so it counts as never sent; your balance was restored on [date]. The receiving bank reported the account as closed. Please check the details with the recipient."

**7.4 Returned** ("EFT geri döndü")
- *Determine:* the reason (closed or invalid account, name policy, accepted recall) and the date.
- *Resolve:* share the reason if disclosable. For FX transfers, explain that the return converts at the then-current rate and fees may apply. Help re-send.
- *Never:* promise compensation for FX loss unless the bank was at fault. Bank-fault interest and fees go to complaints (TR Art. 70(9)).

**7.5 Duplicate** ("iki kere gönderdim", "mükerrer ödeme", "fatura iki kez ödendi")
- *Determine:* who caused it: (a) the customer re-sent; (b) a bank or technical duplicate; (c) a bill paid manually and by instruction; (d) a merchant charged twice.
- *Resolve:*
  - (a) Treat as misdirected: an iade talebi or recall that needs the payee's consent. EU: a duplicate recall within 10 business days, otherwise RFRO.
  - (b) The bank must correct it (TR Art. 70, EU Art. 89) → payment ops, priority.
  - (c) The biller refunds or credits it; some banks lodge the request (Kuveyt Türk).
  - (d) A merchant refund. Card payments → lane 06.
- *Never:* reverse a credited duplicate on your own, or promise when the biller will refund.

**7.6 Misdirected** (wrong IBAN, Kolay Adres or saved payee). Full process in section 2.
- *Ask:*
  - "Did you type the IBAN or did someone send it to you?"
  - "Do you know the recipient?"
  - "Has anyone contacted you about this payment?"
- *Resolve:* lodge the request; explain that it depends on the payee's consent; explain the Art. 69(4) and 70(4) rights; mention legal options neutrally.
- *Never:* "the bank will get it back"; "a wrong name means it bounces"; any deadline; disclosing the payee's identity.
- *Escalate:* scam signs → Fraud. Written document requests → operations or Legal.
- *Wording:*
  - TR: "Talebinizi alıcı bankaya ilettik. Para alıcı hesaba geçtiği için iade alıcının onayına bağlıdır; bankamız tek taraflı geri alamaz ve süre/sonuç garantisi veremeyiz. İade sağlanamazsa, yazılı talebiniz üzerine hukuki yollara başvurmanız için elimizdeki bilgi ve belgeleri sağlayabiliriz."
  - EN: "We've sent a return request. Because the money has been credited, it can only come back with the recipient's agreement. We can't guarantee the outcome or the timing."

**7.7 Incorrect amount** ("yanlış tutar gönderdim", "eksik geçti")
- *Determine:* the customer typed the wrong amount, the bank executed a different amount, or fees/FX caused a short receipt (SHA/BEN).
- *Resolve:*
  - Customer error: an overpayment needs the payee's consent (EU RFRO "wrong amount"); an underpayment needs a top-up.
  - Bank error: correct it and refund fees and interest (TR Art. 70; FCA).
  - Short receipt: explain charges. OUR reduces deductions but does not guarantee none at the receiving bank.
- *Never:* call SHA deductions a bank error, or promise refunds of intermediary fees.

**7.8 Limits** ("limitim yetmiyor", "FAST 300 bin üstü")
- *Determine:* which limit applies: the system FAST cap of 300k TL (cannot be raised); the bank's channel or daily limit; a temporary security limit (5, bank-specific); or, in the EU, the customer's own instant limit (IPR Art. 5a(6)).
- *Resolve:* above 300k TL, use EFT in business hours. Change bank limits after strong authentication. Explain security limits without explaining how to get round them.
- *Never:* bypass or disable security controls.
- *Escalate:* a limit increase requested with urgency or a third party on the line → Fraud.

**7.9 Scheduled transfers and standing orders** ("düzenli ödeme talimatı çalışmadı", "ileri tarihli EFT'yi iptal")
- *Rules:* a non-business date runs on the next business day (TR Art. 58(3)). Revocation is possible until the end of the business day before (TR Art. 64(4); EU PSD2 Art. 80(4)).
- *Resolve:* cancel or amend if still allowed. If it failed for insufficient funds, re-send manually; retry behaviour depends on the bank (5).
- *Never:* promise automatic retries or a waiver from the payee.

**7.10 Direct debits and automatic bill payment** ("otomatik ödeme talimatı", "fatura ödenmemiş", "talimat iptal")
- *Resolve:*
  - Unpaid for insufficient funds: pay now. Late fees are the biller's matter unless the bank caused the failure (Kuveyt Türk covers those).
  - Cancel: in the app before the business day preceding collection (TR Art. 64(3)).
  - Wrong amount or disputed bill: the biller handles it. EU: an unconditional SDD refund within 8 weeks. UK: the Direct Debit Guarantee.
- *Never:* promise fee waivers or reconnection of a service.

**7.11 Bill-payment failures and duplicate bill payments**
- *Determine:* whether the biller received it (bank confirmation), the timing relative to the due date, and manual plus automatic double payment.
- *Resolve:* provide the dekont as proof. Duplicates are refunded or credited by the biller (3, Kuveyt Türk). A bank-side posting failure goes to operations.

**7.12 Dekont / confirmations** ("dekont istiyorum", "dekont gelmedi")
- *Rights:* (1, TR Art. 46) the reference, amount, fees, FX rate and date, free of charge.
- *Resolve:* deliver it through an authenticated channel: in-app transaction details, or the e-mail address on file.
- *Never:* send it to an unverified address or to third parties.
- *Note:* a dekont proves the money left our bank, not that the payee was credited. This explains many "dekontta tamamlandı" complaints [anecdotal].

**7.13 Merchant payments and refunds, transfer side** ("ödedim siparişim onaylanmadı", "iade IBAN'ıma gelmedi")
- *Resolve:* provide the dekont and reference and refer the customer to the merchant or wallet. A merchant refund by transfer depends on the merchant sending it; check incoming credits by the merchant's reference. Fake shops or "IBAN-only" sellers → Fraud. Card refunds → lane 06.
- (5) There is no chargeback-like scheme right for push transfers in Türkiye; recovery is consent-based or through the courts.

### Gaps
- Bank retry rules for failed standing orders, internal SLAs for traces and iade talebi, and compensation and goodwill rules are not public. Verify against the institution's internal procedure.

---

## 8. Decision table: cancel, recall and reversal requests

### Takeaway
Five factors decide the answer: rail × status × time since initiation × payee consent × fraud involvement. Before execution the bank can usually cancel. After crediting, cooperation from the payee or payee bank is needed, apart from narrow exceptions:
- the US 30-minute remittance cancellation
- ACH reversals for sender errors within 5 banking days
- the EU, UK and contracted TR direct-debit refund rights
- automatic SCT Inst restoration when there is no confirmation

Never imply a recall will succeed.

### Cited Findings
All anchors are cited in sections 1–7: TR Art. 54, 56, 64, 67, 69, 70; TCMB irrevocability and the FAST timeout; PSD2 Art. 76–77, 80, 88; SCT recall and RFRO; IPR Art. 5a(5); Pay.UK; FCA; HSBC UK; Nacha; Fedwire; 12 CFR 1005.33/.34; Swift gpi.

### Inferences: decision table (4)

| Rail | Not yet sent | Sent, not credited | Credited | Time factors | Fraud | Tell the customer |
|---|---|---|---|---|---|---|
| Havale (TR) | Future-dated: cancel until end of the previous business day (Art. 64(4)) | Rare (instant) | Payee consent, else legal route | Act now; legal claim 2y/10y (TBK 82) | Fraud team at once | "Request sent; depends on the recipient's consent" |
| EFT (TR) | Queued or future-dated: cancel before the cut-off | Irrevocable at TCMB; ask the receiving bank to return it | Payee consent, else legal | Payee bank credits same day (Art. 67(4)) | Fraud team; urgent request to the bank | Never "we'll pull it back" |
| FAST / Kolay Adres / QR (TR) | Rarely pending; auto-cancels at timeout | — (seconds) | Payee consent; TCMB has no role | Immediate | Fraud team | "It completed in seconds; we can only request a return" |
| Automatic bill payment / DD (TR) | Revoke until end of the previous business day (Art. 64(3)) | — | Biller refund; Art. 56 (2 months) | 13 months unauthorised (Art. 54) | Disputes or Fraud | "Cancel now; the biller handles bill refunds" |
| SWIFT | Cancel internally before release | gpi Stop and Recall or cancellation request | Payee bank or payee consent; FX loss and fees | Sooner is better; no universal deadline (5) | Fraud recall and team | "Stop/recall requested; no guarantee; the returned amount may differ" |
| SEPA SCT / SCT Inst (EU) | Revocable before receipt; future-dated until the previous business day | Recall: duplicate/technical ≤10 BBD, fraud ≤13 months; SCT Inst auto-restores if no confirmation within 10 s | RFRO ≤13 months, payee consent; response ≤15 BBD | Check execution date | Fraud recall ≤13 months | "The payee bank must answer within 15 business days; outcome not guaranteed" |
| UK Faster Payments | Standing or future-dated: cancel before the bank's cut-off | Cannot be cancelled once sent | CRP: reasonable efforts; payee details on written request | e.g. 2 + 20 working days (HSBC UK) | APP rules, 4-day delay (lane 10) | "We'll contact the receiving bank; recovery not guaranteed" |
| UK Direct Debit | Cancel the mandate | — | Guarantee refund for errors | Time limit: verify (5) | Disputes or Fraud | "Full and immediate refund if taken in error" |
| US ACH | Deletion before transmission (5, bank-specific) | Reversal ≤5 banking days for sender errors, not fraud | Reversal returned if no funds | R10 ≤60 days for consumers | Fraud processes | "We can attempt an error reversal within the window; it may fail" |
| Fedwire / RTP / FedNow (US) | Cancel before release | Final and irrevocable | Request a return (consent) (5) | — | Fraud; urgent bank-to-bank contact | "Final; we can only request a return" |
| US remittance (Reg E Subpart B) | **Cancel ≤30 minutes after payment if not collected; refund ≤3 business days** | Errors: notice ≤180 days; decision ≤90 days | Wrong account from sender: reasonable recovery efforts | 30 min / 180 d / 90 d | Fraud processes | Offer cancellation at once if within 30 minutes |
| Card-funded transfer or card payment | → lane 06 | | | | | |

### Gaps
- RTP/FedNow return requests and ACH pre-transmission deletion are not confirmed from primary sources.
- The time limit on Direct Debit Guarantee claims is not confirmed.
- Bank-specific cut-offs for cancelling future-dated EFTs are not confirmed.

---

## Source register

| # | Title | Publisher | Date | Jurisdiction | URL |
|---|---|---|---|---|---|
| 1 | FAST Sistemi İşlem Tutar Limitinin Artırılması Hakkında Basın Duyurusu (2026-36) | TCMB | 24 Aug 2026 | TR | https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2026/DUY2026-36 |
| 2 | EFT – EMKT – FAST Sistemi | TCMB | Undated; accessed 10 Oct 2026 | TR | https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Odeme+Sistemleri/Turkiyedeki+Odeme+Sistemleri/Elektronik+Fon+Transfer+%28EFT%29+Sistemi |
| 3 | TCMB Ödeme Sistemleri | TCMB Ödemelerin Merkezi | Undated; accessed 10 Oct 2026 | TR | https://odemelerinmerkezi.org/wps/wcm/connect/odeme+sistemleri/tr/tcmb+odeme+sistemleri |
| 4 | FAST Sıkça Sorulan Sorular | TCMB | Undated (shows 300k, so ≥ Aug 2026) | TR | https://fast.tcmb.gov.tr/wps/wcm/connect/fast/sikca%20sorulan%20sorular |
| 5 | FAST: Kolay Adresleme; FAST Nedir; Karekod; Güvenli Ödeme | TCMB | Undated; accessed 10 Oct 2026 | TR | https://fast.tcmb.gov.tr/wps/wcm/connect/fast/kolay%20adresleme (and /fast%20nedir, /karekod, /guvenli%20odeme) |
| 6 | Ödeme Hizmetleri ve Elektronik Para İhracı ile Ödeme Hizmeti Sağlayıcıları Hakkında Yönetmelik (Art. 46, 54, 56, 58, 63–70; original text) | Resmî Gazete No. 31676 | 1 Dec 2021 (amended 2023–2026) | TR | https://www.resmigazete.gov.tr/eskiler/2021/12/20211201-1.htm |
| 7 | Amendments RG 33201 (19 Mar 2026) and RG 33360 (4 Sep 2026), summaries | Alomaliye | 2026 | TR | https://www.alomaliye.com/2026/03/19/odeme-hizmetleri-ve-elektronik-para-ihraci-ile-odeme-hizmeti-saglayicilari-degisiklik/amp/ ; https://www.alomaliye.com/2026/09/04/odeme-hizmetleri-ve-elektronik-para-yonetmeliginde-degisiklik/amp/ |
| 8 | Banka Para Transferini Reddedebilir mi? (2026) | Halil Bakırcı Hukuk | 11 Sep 2026 | TR | https://halilbakirci.av.tr/banka-para-transferini-reddedebilir-mi-odeme-emri-reddi-2026/ |
| 9 | Yargıtay HGK E.2017/(19)11-941 K.2021/144 | Karamercan Hukuk (reproduction) | 23 Feb 2021 | TR | https://karamercanhukuk.com/yargitay-karari/bankanin-iban-ile-havale-alicisinin-isminin-ayni-olup-olmadigini-kontrol-etme-yukumlulugu-yoktur |
| 10 | Havale ve EFT Nedir? … İptal Süreci | Ziraat Katılım | 9 Apr 2026 | TR | https://www.ziraatkatilim.com.tr/blog/havale-ve-eft-nedir-farklari-islem-saatleri-ve-iptal-sureci |
| 11 | EFT; Döviz Transferi (SWIFT) | Türkiye İş Bankası | Undated; accessed 10 Oct 2026 | TR | https://www.isbank.com.tr/eft ; https://www.isbank.com.tr/doviz-transferi-swift |
| 12 | Swift Transfer | Yapı Kredi | Undated; accessed 10 Oct 2026 | TR | https://www.yapikredi.com.tr/bireysel-bankacilik/odemeler-ve-hizmetler/swift-transfer |
| 13 | Ürün ve Hizmet Ücretleri | Garanti BBVA | Rows updated Dec 2025 – May 2026 | TR | https://www.garantibbva.com.tr/urun-ve-hizmet-ucretleri |
| 14 | Fatura Ödemeleri ve Talimatlar | Kuveyt Türk | Undated; accessed 10 Oct 2026 | TR | https://www.kuveytturk.com.tr/kendim-icin/odemeler-ve-hizmetler/odemeler/fatura-odemeleri-ve-talimatlar |
| 15 | Yanlış İban'a Gönderilen Para Geri Alınır mı? | Harbiye Hukuk | Undated; accessed 10 Oct 2026 | TR | https://www.harbiyehukuk.com/iban-ile-gonderilen-para-geri-alinir-mi/ |
| 16 | TBK 6098; TCK 5237; KVKK 6698 (consolidated) | mevzuat.gov.tr | Accessed 10 Oct 2026 | TR | https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6098.pdf ; https://www.mevzuat.gov.tr/mevzuatmetin/1.5.5237.pdf ; https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf |
| 17 | MASAK purpose-declaration news | CNBC-e; CNN Türk; İstiklal | 27 Dec 2025; 27 Dec 2025; 22 Feb 2026 | TR | https://www.cnbce.com/haberler/para-transferlerinde-yeni-donem-basliyor-masak-duzenlemesiyle-neler-degisecek-g22016 ; https://finans.cnnturk.com/finans-haberler/para-transferlerinde-yeni-donem-basliyor-1-ocaktan-itibaren-uyari-zorunlulugu-2377710 ; https://www.istiklal.com.tr/ekonomi/ibana-para-transferinde-yeni-zorunluluk-limit-degisti-tarih-belli-oldu-1085379h |
| 18 | BSMV on FX purchases | Habertürk; Faturaport (non-authoritative) | 30 Sep 2020; 2026 | TR | https://www.haberturk.com/son-dakika-banka-bonosu-doviz-ve-altin-alim-satiminda-vergi-ne-oldu-haberler-2819385-ekonomi ; https://faturaport.com/blog/vergi/kambiyo-vergisi-bsmv-nedir-2026 |
| 19 | Complaints (anecdotal) | Şikayetvar | Sep 2025 – Oct 2026 | TR | https://www.sikayetvar.com/yanlis-ibana-para-gonderme ; https://www.sikayetvar.com/eft-hesaba-gecmedi ; https://www.sikayetvar.com/vakifbank/eft/iban-dogru-isim-yanlis |
| 20 | ISO 20022 for Financial Institutions | Swift | Accessed 10 Oct 2026 | Global | https://www.swift.com/standards/iso-20022/iso-20022-financial-institutions-focus-payments-instructions |
| 21 | Swift accepts community request to extend structured address migration | Swift | 27 Aug 2026 (updated 21 Sep 2026) | Global | https://www.swift.com/news-events/news/swift-accepts-community-request-extend-structured-address-migration-iso-20022-payment-messages |
| 22 | Swift GPI | Swift | Accessed 10 Oct 2026 | Global | https://www.swift.com/products/swift-gpi |
| 23 | Payment Status Reason Codes | Goldman Sachs Developer | Accessed 10 Oct 2026 (search extract) | Global | https://developer.gs.com/docs/services/transaction-banking/paymentstatusreasoncodes/ |
| 24 | ISO 20022 migration FAQ | Kyriba | Accessed 10 Oct 2026 | Global | https://www.kyriba.com/resources/faqs/iso-20022-migration-frequently-asked-questions/ |
| 25 | OUR/DEBT, BEN/CRED, SHA/SHAR | Flywire Help | Accessed 10 Oct 2026 | Global | https://help.flywire.com/hc/en-us/articles/360019759293-What-do-OUR-DEBT-BEN-CRED-and-SHA-SHAR-mean-in-the-fees-section |
| 26 | Nordea screens transactions against sanctions lists | Nordea | Undated | EU/FI | https://www.nordea.fi/en/personal/our-services/accounts-payments/nordea-screens-transactions-against-sanctions-lists.html |
| 27 | Instant Payments Regulation | ECB | Undated; accessed 10 Oct 2026 | EU | https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.en.html |
| 28 | Regulation (EU) 2024/886 | EUR-Lex | OJ 19 Mar 2024 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202400886 |
| 29 | Directive (EU) 2015/2366 (PSD2) | EUR-Lex | OJ 23 Dec 2015 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366 |
| 30 | 2025 SCT Rulebook v1.0 (search extract) | EPC | Effective 5 Oct 2025 | SEPA | https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2024-11/EPC125-05%202025%20SCT%20Rulebook%20version%201.0.pdf |
| 31 | Consultation on 2026 change requests (SCT) | EPC | Mar 2026 | SEPA | https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2026-03/EPC008-26%20SCT%20Scheme%20Rulebook%20-%20Public%20Consultation%20Document%20on%202026%20Change%20Requests.pdf |
| 32 | Clarification Paper NCT/NCT Inst v2.0 (based on EPC131-17) | Nordic Payments Council | 21 Dec 2022 | SEPA/Nordic | https://www.nordicpaymentscouncil.org/media/mmchrsnz/clarification-paper-rulebooks-v20.pdf |
| 33 | SCT Inst rulebook extract (TIPS annex) | ECB | 2021 | SEPA | https://www.ecb.europa.eu/paym/target/tips/governance/pdf/cr/ecb.tipscr210812_TIPS-0012-URD_Annex_1.en.pdf |
| 34 | SCT Inst 2025 changes | ACI Worldwide; Numeral | 2025 | SEPA | https://www.aciworldwide.com/blog/sepa-instant-payments-whats-new-in-rulebook-2025-and-why-it-matters ; https://www.numeral.io/blog/epc-2025-sepa-rulebook-updates |
| 35 | PSD3/PSR timeline | Worldline; Mondaq | 2026 | EU | https://worldline.com/en/home/main-navigation/resources/blogs/2026/the-scope-and-timeline-are-locked-in-for-psd3-and-psr-what-should-psps-know ; https://webiis08.mondaq.com/ireland/financial-services/1780752/psd3psr-final-compromise-texts-are-published |
| 36 | How Faster Payments work; Transaction limits; Confirmation of Payee | Pay.UK | Undated; accessed 10 Oct 2026 | UK | https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/how-faster-payments-work/ ; https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/transaction-limits/ ; https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/ |
| 37 | Making and receiving payments | FCA | Accessed 10 Oct 2026 | UK | https://www.fca.org.uk/consumers/making-receiving-payments |
| 38 | Wrong account transfer guide | HSBC UK | Accessed 10 Oct 2026 | UK | https://www.hsbc.co.uk/current-accounts/online-transfer-mistake/ |
| 39 | FG24/6 | FCA | Late 2024 | UK | https://www.fca.org.uk/publication/finalised-guidance/fg24-6.pdf |
| 40 | PSR APP reimbursement maximum | Regulation Tomorrow | Oct 2024 | UK | https://www.regulationtomorrow.com/2024/10/psr-issues-policy-statement-confirming-maximum-level-of-reimbursement-for-faster-payments-app-scams/ |
| 41 | Direct Debit Guarantee | directdebit.co.uk (Bacs) | Accessed 10 Oct 2026 (search extract) | UK | https://directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/ |
| 42 | Understanding ACH Reversals; New Funds Availability Requirements | Nacha | 6 Aug 2026; 1 Sep 2026 | US | https://www.nacha.org/news/second-chance-understanding-ach-reversals ; https://www.nacha.org/news/new-funds-availability-requirements-take-effect-sept-18 |
| 43 | ACH return codes | Plaid | Accessed 10 Oct 2026 | US | https://plaid.com/resources/ach/ach-return/ |
| 44 | Same-Day ACH limit to $10M (2027) | Bloomberg Tax | 2026 | US | https://news.bloombergtax.com/payroll/same-day-ach-limit-rising-to-10-million-in-2027 |
| 45 | Fedwire core principles | Federal Reserve Board | Accessed 10 Oct 2026 | US | https://www.federalreserve.gov/paymentsystems/fedfunds_coreprinciples.htm |
| 46 | RTP $10M; FedNow $10M | ABA Banking Journal | Dec 2024; 15 Sep 2025 | US | https://bankingjournal.aba.com/2024/12/rtp-network-to-raise-individual-transaction-limit-to-10m/ ; https://bankingjournal.aba.com/2025/09/fednow-to-raise-transaction-limit-to-10m/ |
| 47 | 12 CFR 1005.30 / .33 / .34 | CFPB | Current; accessed 10 Oct 2026 | US | https://www.consumerfinance.gov/rules-policy/regulations/1005/30/ (also /33/, /34/) |

---

## Open questions, unverified items and items needing institution-specific confirmation

1. **MASAK purpose declaration.** Find the primary MASAK or TBB text for the threshold (200k TL from 1 Jan 2026, 400k TL from 15 Mar 2026 per the press), the categories, the 20-character minimum, the document tiers and the bank's rejection behaviour. Confirm with Compliance.
2. **Consolidated Payment Services Regulation.** The 2021 text of Art. 46, 54, 56, 58 and 63–70 was used. Amendments in 2023–2026 may have changed wording or amounts, for example Art. 54(4). Verify against the consolidated version.
3. **FAST operating rules.** The timeout duration, the return messaging, and whether a FAST "iade" message type exists.
4. **Receiving-side name checks at Turkish banks.** Which banks return name mismatches, and how fast. There is no official source and anecdotes conflict.
5. **Bank-specific cut-offs.** EFT cut-offs (İş Bankası 17:00 versus TCMB 17:30), half-day hours (11:45 versus 13:00), late-EFT windows, and cut-offs for cancelling future-dated orders.
6. **New-device, new-payee and night-time transfer limits.** No authoritative public source was found (lane 08/10).
7. **BSMV rate on FX purchases in 2026.** The 0.2% figure is not confirmed from GİB or the Resmî Gazete.
8. **SWIFT.** The new structured-address deadline (by Dec 2026), MT contingency-processing charges and end date, and whether customers can see UETR status themselves.
9. **EPC.** The exact SCT Inst 2025 recall wording, and the outcome of the 2026 proposal to extend duplicate/technical recalls to 13 months.
10. **PSD3/PSR.** Official Journal publication and application dates. The wider VoP liability expected around 2028 could change EU outcomes for misdirected payments.
11. **UK.** The Direct Debit Guarantee time limit; current CRP timelines (HSBC UK's 2 + 20 working days are one bank's figures); and the effect of the PSR merging into the FCA on APP rules.
12. **US.** Nacha return-code timeframes from the primary rules; RTP/FedNow return-request mechanics; Fedwire 2026 hours; and positions on misdirected P2P payments.
13. **Institution-specific items to confirm before deployment:**
    - mapping of internal status codes to labels
    - SLAs for traces, iade talebi and SWIFT investigations
    - fees for recovery, recall and inquiry (for example Garanti's 190.48 TL international inquiry fee)
    - goodwill and compensation rules
    - which actions the AI agent may run itself: cancelling future-dated or standing orders, lodging an iade talebi, changing limits, issuing a dekont
    - Compliance-approved wording for AML and sanctions holds
    - the legal process for Art. 69(4) written requests
14. **Statistics.** No reliable recovery-rate statistics exist for misdirected payments, and none should be invented. Swift's gpi speed figures (~60% within 30 minutes, ~100% within 24 hours) are vendor-reported.
