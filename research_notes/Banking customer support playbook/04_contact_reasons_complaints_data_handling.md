# 04 — Why bank customers contact us, what they complain about, and how complaints are handled (research notes, as of 10 Oct 2026)

Researcher 04. Scope: contact-reason/intent taxonomy, complaint frequency data, complaint-handling operations. Türkiye is primary; EU/UK/US are for comparison. Legal deadlines and ombudsman rules get only short notes here because researchers 02 and 03 cover them in depth.

**Tag legend (used throughout):** [L] law/regulation · [IP] common industry practice · [BP:Bank] an individual bank's policy · [RP] recommended service practice · [V] assumption that needs verification. Jurisdiction tags: TR / EU / UK / US / Global.
**Example-utterance provenance tags:** [B77] BANKING77 training set · [CLINC] CLINC150 · [Bitext] Bitext retail-banking dataset · [SV] Şikayetvar complaint title or body excerpt (anecdotal, real users; titles appear to be platform-normalised) · [brief] phrasing supplied in the research brief (realistic, but its origin is not verified) · [C] I constructed it for augmentation or evaluation. [C] phrases were not observed in data and must never be presented as real customer quotes.

---

## KQ1. Public banking intent taxonomies, and a hierarchical taxonomy with an urgency level for each intent

### Takeaway
The three public datasets each cover only part of a real Turkish retail bank's contact mix. BANKING77 is fine-grained but written for a neobank/e-money app. CLINC150 has only 15 banking + 15 credit-card intents. Bitext has 26 broad intents. A usable routing taxonomy has to combine these with the categories regulators and bank associations use in their complaint statistics (BDDK, TBB, CFPB, FCA/FOS), which add loans, garnishment, fraud, fees, restructuring and "other authority" cases. On top of the primary intent, each contact needs four independent flags: urgency, complaint, dispute and vulnerability.

### Cited Findings
- **BANKING77 (Casanueva et al., 2020).** 13,083 "customer service queries labeled with 77 intents" in a single banking domain; split 10,003 train / 3,080 test; licence CC BY 4.0 — [arXiv 2003.04807](https://arxiv.org/abs/2003.04807); [HF dataset card](https://huggingface.co/datasets/PolyAI/banking77). The paper says the intents are fine-grained and partly overlapping (its example: "reverted top-up vs. failed top-up"). Average utterance length is 12 words, against 7 for HWU64 and 8 for CLINC150 — [arXiv 2003.04807](https://arxiv.org/abs/2003.04807).
- The BANKING77 dataset card says "[More Information Needed]" for both data collection and source producers, so the provenance of the utterances is undocumented — [HF card](https://huggingface.co/datasets/PolyAI/banking77).
- The full list of BANKING77 labels is in `categories.json` — [PolyAI GitHub](https://github.com/PolyAI-LDN/task-specific-datasets). The labels lean toward card/e-money apps: top-ups (`top_up_failed`, `top_up_reverted`, `pending_top_up`), virtual and disposable cards, `apple_pay_or_google_pay`, `exchange_via_app`, `fiat_currency_support`, identity checks (`verify_my_identity`, `unable_to_verify_identity`, `why_verify_identity`, `verify_source_of_funds`). It also has many "where is my money" labels (`pending_transfer`, `transfer_not_received_by_recipient`, `balance_not_updated_after_bank_transfer`, `balance_not_updated_after_cheque_or_cash_deposit`, `Refund_not_showing_up`, `pending_card_payment`, `pending_cash_withdrawal`) and unauthorised-activity labels (`card_payment_not_recognised`, `cash_withdrawal_not_recognised`, `direct_debit_payment_not_recognised`, `compromised_card`). There are no loan, mortgage, garnishment or complaint-escalation intents.
- In my count of the downloaded train file, examples per intent range from 35 to 187, so the training set is imbalanced — [train.csv, PolyAI GitHub](https://github.com/PolyAI-LDN/task-specific-datasets).
- **BANKING77 label noise.** Ying & Thomas (2022) estimate that more than 1,400 of the 10,003 training utterances (14%) may be mislabelled. Removing them raised F1 by 4.5% (supervised) and Adjusted Rand Index by 8% (unsupervised) — ["Label Errors in BANKING77", ACL Anthology, Insights workshop 2022](https://aclanthology.org/2022.insights-1.19/).
- **CLINC150 (Larson et al., EMNLP 2019).** 150 intents in 10 domains plus out-of-scope samples. It was built by crowdsourcing: workers paraphrased seed phrases or answered scenarios — [oos-eval README](https://github.com/clinc/oos-eval); [ACL Anthology D19-1131](https://aclanthology.org/D19-1131/).
  - Banking domain (15): `freeze_account, routing, pin_change, bill_due, pay_bill, account_blocked, interest_rate, min_payment, bill_balance, transfer, order_checks, balance, spending_history, transactions, report_fraud`.
  - Credit-card domain (15): `replacement_card_duration, expiration_date, damaged_card, improve_credit_score, report_lost_card, card_declined, credit_limit_change, apr, redeem_rewards, credit_limit, rewards_balance, application_status, credit_score, new_card, international_fees`.
  - Source: [domains.json](https://raw.githubusercontent.com/clinc/oos-eval/master/data/domains.json).
  - Its out-of-scope class is useful for teaching the agent to say "not my remit".
- **Bitext retail banking (vendor dataset, 2024).** "Hybrid synthetic"; 26 intents in 9 categories; 25,545 Q/A pairs, about 1,000 per intent; licence CDLA-Sharing 1.0 — [HF card](https://huggingface.co/datasets/bitext/Bitext-retail-banking-llm-chatbot-training-dataset).
  - Categories: ACCOUNT, ATM (`dispute_ATM_withdrawal`, `recover_swallowed_card`), CARD (`activate_card`, `activate_card_international_usage`, `block_card`, `cancel_card`, `check_card_annual_fee`, …), CONTACT (`customer_service`, `human_agent`), FEES, FIND, LOAN, PASSWORD, TRANSFER.
  - Its utterances carry language-variation tags: colloquial, offensive, typos, abbreviations. A "Y – code switching" tag is defined but listed as "not in use in this Dataset".
- **Complaint category schemes used by authorities**, which work as de facto taxonomies:
  - **BDDK 2025 topic scheme** (re-based in 2025): "Başka Kurumun/Kuruluşun Görev Alanına Giren" (another body's remit), Deposits/Participation funds, Bank & credit cards, Alternative distribution channels, Deferral/restructuring, Fraud, Enforcement (icra) issues, Commercial customer, Credit/card application and limit, Credit score/record amnesty/blacklist, Non-bank institutions, Savings-finance companies, Consumer loans, Overdraft (KMH), Information/document requests (to institutions and to BDDK), Whistleblowing (ihbar), Non-specific, Banking for persons with disabilities — [BDDK Faaliyet Raporu 2025, Tablo 16](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527).
  - **TBB topic scheme** for complaints made directly to banks: Loans, Bank & credit cards (includes loss/theft/fraud notifications and spending disputes), Alternative distribution channels, KMH, Insurance, Deposits (includes safe-deposit boxes and money/value transfers), Bills & other payments, Investment products — [TBB Bireysel Müşteri Hakem Heyeti 2024 Faaliyet Raporu](https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf).
  - **CFPB product → issue → sub-issue tree**, e.g., Checking/savings → "Managing an account" → "Deposits and withdrawals" — [CFPB complaint API, 2025 query](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Checking%20or%20savings%20account).
- **What one Turkish bank's chatbot offers as top topics** (Garanti BBVA site assistant, accessed 10 Oct 2026) [BP:Garanti BBVA]:
  - becoming a customer; loans (calculate instalment, documents)
  - accounts (IBAN, e-time deposit, deposit rates)
  - retiree salary promotion ("Emekli maaş promosyon tutarı ne kadar?", "3 yıllık maaş taahhütüm ne zaman doluyor?")
  - investment ("1 Dolar kaç TL?", "Altın Hesabı açmak istiyorum")
  - limits (daily ATM withdrawal limit, card limit increase, transfer limit increase)
  - Source: [Garanti BBVA page](https://www.garantibbva.com.tr/musteri-deneyimi/tbb-bireysel-musteri-hakem-heyeti).
- **Turkish regulation already ranks some intents by urgency** [L][TR]. The BDDK call-centre regulation (RG 20.05.2020/31132) requires:
  - lost/stolen and suspicious transactions as the **first IVR option**, with priority connection to an agent;
  - a 20-second answer threshold for those calls (30 s for others), and a monthly service level of ≥90% for lost/stolen/suspicious calls (≥80% for others);
  - card-cancellation requests taken without redirecting the customer to another channel;
  - callers aged 60+ offered a direct option to reach an agent with no recognition step.
  - Source: [Resmî Gazete 20.05.2020](https://www.resmigazete.gov.tr/eskiler/2020/05/20200520-9.htm).

### Inferences
- **Design principle.** Use a multi-head label instead of one flat intent:
  - `intent` (one primary, optional secondary)
  - `urgency` (P1–P4)
  - `complaint_flag` (any dissatisfaction)
  - `dispute_flag` (the customer challenges a specific transaction or decision, which can start statutory or scheme clocks)
  - `vulnerability_flag` (team 11)
  - `authority_signpost` (the issue belongs to another institution)

  The datasets support the intent head. The definitions in KQ5 support the flags.
- **Urgency scale** [RP]:
  - **P1 – critical.** Money or credentials at risk now: fraud in progress, lost/stolen card or phone, scam being coached, account takeover. Immediate human or fraud path, 24/7.
  - **P2 – urgent.** Customer cannot access or locate money, or a deadline is imminent: transfer missing, card retained, ATM debit without cash, hold/garnishment, OTP not arriving, login locked, salary not credited, payment due.
  - **P3 – standard.** Service requests, non-fraud disputes, fees, documents, credit decisions, complaints about service.
  - **P4 – routine/informational.** Rates, balances, branch/ATM, campaign information.
  - Two rules on top of the scale: (a) urgency is raised by vulnerability, repeat contact, an overdue complaint, or a mention of regulator, legal action or media; (b) a complaint flag never lowers urgency.
- Because BANKING77 is noisy (about 14%), skewed toward neobanks, and its provenance is undocumented, use it for **coverage and stress tests of fine-grained distinctions** (pending vs failed vs reverted), not as the main training set for a Turkish retail bank. The anchors from BDDK/TBB categories and Şikayetvar wording should drive Turkish coverage.

### Synthesised routing taxonomy (domain → intent → sub-intents)
Owner teams are generic; verify against the institution's internal procedure. Urgency is the default and changes with context. Anchors point to the evidence for each intent.

| ID | Domain → intent (sub-intents) | What it covers | EN example(s) | TR example(s) | Urg. | Typical owner | Evidence anchors |
|---|---|---|---|---|---|---|---|
| A1 | Security → unrecognised card transaction (CNP/CP, recurring, merchant-descriptor confusion) | Customer sees a card debit they don't recognise | "I see a payment on my statement for a place I didn't make a purchase at." [B77] | "Kartımdan bilmediğim bir harcama var" [brief]; "İzinsiz 7.370 TL Harcama Ve Uzayan İtiraz Süreci" [SV] | P1 | Fraud ops (24/7) → card disputes (harcama itirazı / chargeback, "ters ibraz") | B77 card_payment_not_recognised; CFPB "charged for something you did not purchase" 4,547 (2025); EBA: unauthorised transactions = top payment-services complaint reason |
| A2 | Security → unauthorised account debit / cash withdrawal / direct debit | Money left the account without consent | "I didn't withdraw cash but I see that transaction on my app" [B77] | "Hesabımdan habersiz para çekilmiş" [brief] | P1 | Fraud ops | B77 cash_withdrawal_not_recognised, direct_debit_payment_not_recognised; CFPB "Transaction was not authorized" 7,978 (checking, 2025) |
| A3 | Security → scam victim (APP/"safe account", impersonation, investment, betting) | Customer authorised a payment after being deceived | "I was tricked into moving my savings to a 'safe' account" [C] | "Beni banka görevlisi diye aradılar, parayı gönderdim" [C] | P1 | Fraud ops + vulnerability handling | FOS: 18,900 of 32,900 current-account complaints = fraud & scams (2025/26); Şikayetvar: bank-staff impersonation asking for "onay kodu" |
| A4 | Security → "is this message/call really from you?" | Verify bank contact / phishing check | "Got a text saying my account is locked—is it from you?" [C] | "Bankadan aradılar, kod istediler, bu sizden mi?" [C] | P2 (P1 if a code or credentials were shared) | L1 with fraud script → Fraud ops | Şikayetvar 2025: "dava/icra SMS" scams 11,368 (+162%); Ziraat "Sahte Faizsiz Kredi Aramasıyla Mağduriyet" [SV] |
| A5 | Security → lost/stolen card | Block and replace | "Could you assist me in finding my lost card?" [B77 paper] | "Kartımı kaybettim, hemen kapatın" [C] | P1 | Card ops / fraud (first IVR option in TR) | B77 lost_or_stolen_card; CLINC report_lost_card; Bitext block_card; TR call-centre reg. art. 6(4) |
| A6 | Security → lost/stolen phone, SIM swap, device compromise | App/OTP channel at risk | "Someone stole my phone, what is my next step?" [B77] | "Telefonum çalındı, mobil bankacılığımı kapatın" [C] | P1 | Digital security / fraud | B77 lost_or_stolen_phone |
| A7 | Security → suspicious login / account takeover | Unknown login, changed details | "I got a login alert that wasn't me" [C] | "Benim yapmadığım bir giriş bildirimi geldi" [C] | P1 | Fraud / digital security | EBA: phishing → manipulated app/software token |
| B1 | Cards → card retained by ATM | Card swallowed or captured | "I didn't get my card back from the ATM." [B77] | "Kartım ATM'de kaldı" [brief]; "Banka Kartımı Yuttu" [SV] | P2 | Card ops / ATM ops | B77 card_swallowed; Bitext recover_swallowed_card |
| B2 | Cards → card declined / not working (POS, online, contactless, abroad) | Authorisation failures | "I tried to used my card in a shop and the transaction was declined." [B77] | "Kartım geçmiyor" [C]; "Kredi Kartım Tam Ödemeye Rağmen Açılmadı" [SV] | P2 if travelling or stranded, else P3 | Card ops / authorisation | B77 declined_card_payment, card_not_working; CLINC card_declined; CFPB "Can't use card to make purchases" 2,029 |
| B3 | Cards → PIN blocked / PIN change | Card PIN locked or forgotten (not internet password) | "I tried entering my pin several times incorrectly." [B77] | "Şifrem bloke oldu" [brief] (ask which password) | P2/P3 | IVR self-service / card ops | B77 pin_blocked, change_pin; CLINC pin_change |
| B4 | Cards → delivery / courier status | New or replacement card not arrived | "My card hasn't arrived." [B77] | "Kartım hâlâ gelmedi, kurye ne zaman getirir?" [C] | P3 | Card ops / courier vendor | B77 card_arrival, card_delivery_estimate |
| B5 | Cards → activation, replacement, expiry, damaged | Lifecycle requests | "My card is about to expire" [C] | "Kartımın süresi doluyor, yenisi gelecek mi?" [C] | P3/P4 | Card ops | CLINC damaged_card, replacement_card_duration, expiration_date; B77 activate_my_card |
| B6 | Cards → limit change (increase/decrease) | Limit requests | "Can I raise my credit limit?" [C] | "Kart limitimi artırmak istiyorum" [BP: Garanti chatbot] | P3 | Credit / cards | CLINC credit_limit_change; CFPB 942 "won't increase or decrease your credit limit"; TR: limit-decrease answer within 7 days (İş Bankası table) |
| B7 | Cards → cancel card | Cancellation (retention must not obstruct) | "Cancel my credit card" [C] | "Kartımı iptal ettirmek istiyorum" [C] | P3 | Card ops | TR call-centre reg. art. 6(5); İş Bankası: 7 days |
| B8 | Cards → annual fee refund / fee objection | Kart aidatı | "I want my annual card fee refunded" [C] | "Kart aidatı iadesi istiyorum" [brief]; "Yıllık Kart Aidatı Haksız Kesildi Ve İade Talebi" [SV] | P3 + complaint | Cards / fees; external: Tüketici Hakem Heyeti | THH 2025: "kredi kartı üyelik ücreti" = 3.97% of all 907,515 applications |
| B9 | Cards → merchant dispute, non-fraud (refund not posted, double charge, goods not received, wrong amount) | Chargeback-type disputes | "I was charged too many times for one transaction." [B77] | "İade yapıldı dendi ama kartıma yansımadı" [C] | P3 + dispute | Card disputes | CFPB "isn't resolving a dispute about a purchase" 14,758; B77 Refund_not_showing_up, transaction_charged_twice |
| B10 | Cards → usage abroad / FX rate / international fees | Travel enablement, FX questions | "Can I use my card abroad?" [C] | "Kartımı yurt dışı kullanımına açar mısınız?" [C] | P3 (P2 if abroad and stranded) | Card ops | Bitext activate_card_international_usage; B77 card_payment_wrong_exchange_rate; CLINC international_fees |
| B11 | Cards → digital wallet / virtual / contactless | Tokenised cards | "Apple Pay isn't working" [C] | "Temassız çalışmıyor" [C] | P3 | Card ops / digital | B77 apple_pay_or_google_pay, virtual_card_not_working, contactless_not_working |
| B12 | Cards → statement interest/fees, payment problem, minimum payment | Credit-card billing | "Why was I charged interest?" [C] | "Ekstremde anlamadığım faiz var" [C] | P3 (P2 near due date) | Cards | CFPB "Problem with fees" 4,676; "Charged too much interest" 2,410; "Problem during payment process" 3,926 |
| C1 | Payments → outgoing transfer not received by recipient (EFT/FAST/havale/SWIFT) | "Where is my money" for sends | "Why isn't the recipient seeing the transaction? I just sent the money." [B77] | "EFT gitmedi" / "Gönderdiğim para karşıya geçmedi" [brief]; "gönderdiğim para ne alıcı hesaba geçti ne de kendi hesabıma geri döndü" [SV] | P2 | Payments ops | B77 transfer_not_received_by_recipient, pending_transfer; CFPB money transfer "Other transaction problem" 63.6% |
| C2 | Payments → incoming money not credited (salary, benefit, transfer) | Inbound missing | "I do not see the money I transferred into this account" [B77] | "Maaşım hesabıma geçmedi" [C]; "Sosyal Yardım Ödemelerinin Hesaba Yansımaması" [SV] | P2 | Payments ops | B77 balance_not_updated_after_bank_transfer |
| C3 | Payments → transfer held for security review | Bank-side hold or verification | "My transfer is on hold—why?" [C] | "Güvenlik Onayı Bekleyen 120 Bin TL'lik EFT İşlemi Bloke" [SV] | P2 | Fraud / payments ops | — |
| C4 | Payments → wrong recipient / recall / cancel transfer | Misdirected payment | "I submitted a transaction but it was for the incorrect account." [B77] | "Yanlış IBAN'a para gönderdim, geri alabilir miyim?" [C]; "Yanlış Alıcı İsmi Nedeniyle 92.700 TL EFT Parası Geri Ödenmedi" [SV] | P2 | Payments ops | B77 cancel_transfer |
| C5 | Payments → failed/declined transfer, beneficiary not allowed | Rejections | "Why did the bank reject my transfer?" [B77] | "Havale yapamıyorum, hata veriyor" [C] | P2/P3 | Payments ops / digital | B77 failed_transfer, declined_transfer, beneficiary_not_allowed |
| C6 | Payments → limits, fees, timing information | Info | "How long does a transfer take?" [C] | "Para transfer limitimi artırmak istiyorum" [BP: Garanti chatbot] | P4 | L0/L1 | B77 transfer_timing, transfer_fee_charged |
| C7 | Payments → bills, auto-pay, standing orders, direct debits | Recurring payments | "My bill autopay didn't go through" [C] | "Otomatik fatura talimatım çalışmamış" [C] | P3 | Payments ops | CLINC pay_bill, bill_due; FOS direct debits 391, standing orders 48 |
| D1 | Accounts → "my money disappeared" (unexplained debit/balance drop) | Symptom-level umbrella → disambiguate (see KQ4 map) | "Where is my money that I transfered?!" [B77] | "Param kayboldu" [brief] | P2 (P1 if fraud signs) | L1 triage | See KQ4 symptom map |
| D2 | Accounts → balance, transactions, spending history | Information | "What's my balance?" [C] | "Hesap hareketlerimi görmek istiyorum" [C] | P4 | L0 | CLINC balance, transactions, spending_history |
| D3 | Accounts → hold/restriction ("bloke") | Funds unavailable | "My account is frozen" [C] | "Hesabıma bloke konmuş" [brief]; "Hesabımdaki Parayı Kullanamıyorum!" [SV] | P2 | Depends: legal-holds unit / fraud / compliance / branch | CLINC account_blocked, freeze_account |
| D4 | Accounts → garnishment ("haciz", e-haciz, icra) | Enforcement attachment | "There's a garnishment on my account" [C] | "Haciz gelmiş" [brief]; "Emekli Maaşına Haksız Bloke Ve Transfer Engeli" [SV] | P2 | Legal / garnishment ops | BDDK 2025 "İcraya İlişkin Sorunlar" 10,926 (4.7%) |
| D5 | Accounts → onboarding / KYC / identity verification / source of funds | Opening and refresh | "What's wrong with my ID? I can't verify it." [B77] | "Kimlik doğrulamam onaylanmıyor" [C] | P3 | Onboarding / KYC ops | B77 verify_my_identity, unable_to_verify_identity, verify_source_of_funds; CFPB "Unable to open an account" 2,673 |
| D6 | Accounts → customer wants to close account | Exit | "I want to terminate my account" [B77] | "TEB Bankası'ndaki açık hesaplarımı kapatmak istiyorum ancak … bağlanamıyorum" [SV] | P3 | Account ops / branch | CFPB "Can't close your account" 1,450 (checking), 1,193 (cards) |
| D7 | Accounts → bank closed/restricted my account (de-risking), funds from closed account | Exit by the bank | "You closed my account and kept my money" [C] | "Hesabım banka tarafından kapatıldı, param ne olacak?" [C] | P2 | Compliance / account ops | CFPB "Company closed your account" 5,051 (checking); "Funds not received from closed account" 3,470; EBA: account closing = most common payment-account complaint reason |
| D8 | Accounts → overdraft (KMH / "ek hesap") interest, fees, limits | Overdraft | "Why was I charged overdraft fees?" [C] | "KMH faizi neden bu kadar yüksek?" [C] | P3 | Retail credit / accounts | CFPB overdrafts 9,814 (checking); FCA overdrafts 26,456 (2025 H2); BDDK KMH 3,197 |
| D9 | Accounts → ATM cash issues (not dispensed / wrong amount / deposit not credited) | Cash events | "I only got $20 after trying to withdraw $100" [B77] | "ATM'den Para Alındı Ama Hesaba Yatırılmadı" [SV]; "ATM para vermedi ama hesaptan düştü" [C] | P2 + dispute | ATM ops / reconciliation | B77 wrong_amount_of_cash_received; TKBB ATM complaints 230 (16.7%, 2025); US Reg E: incorrect amount from terminal = "error" |
| D10 | Accounts → update personal details (phone, address, e-mail) | Data maintenance | "How do I change my address?" [C] | "Mobil Bankacılık Erişimi Telefon Numarası Güncellenememesi" [SV] | P3 (P2 if it blocks OTP) | Account ops / branch | B77 edit_personal_details |
| D11 | Accounts → documents (statement, account-confirmation/reference letter, interest/tax certificate) | Paperwork | "I need a bank reference letter" [C] | "Hesap dökümü / banka referans mektubu istiyorum" [C] | P4 (P3 if deadline) | Ops / branch | BDDK "Kuruluşlardan Bilgi/Belge Talepleri" 3,099 (2025) |
| E1 | Digital → OTP/SMS not received (incl. "SIM bloke" after SIM change, wrong number on file) | Authentication channel | "I'm not getting the verification code" [C] | "SMS gelmiyor" [brief]; "Şifre SMS gelmiyor", "Doğrulama kodu gelmiyor" [SV] | P2 | Digital support | Şikayetvar topic pages; never ask for the code |
| E2 | Digital → login locked / forgotten password / internet-banking password blocked | Access | "I can't remember what my password is" [B77] | "Şifre giriş yapamıyorum", "Şifre bloke" [SV] | P2 | Digital support | B77 passcode_forgotten; Bitext get_password |
| E3 | Digital → app/web error or outage | Technical failure | "The app keeps crashing" [C] | "Uygulama hata veriyor, açılmıyor" [C]; "Sistem arızası" [SV topic] | P2 if widespread (incident) | IT / digital support; major-incident process | TBB: ADC = 22% of 3.68m direct complaints (2024); BDDK ADC 23,761 (2025) |
| E4 | Digital → new device / device binding / app activation | Device lifecycle | "New phone, app won't log in" [C] | "Yeni telefona geçtim, uygulama açılmıyor" [C] | P3 | Digital support | — |
| F1 | Credit → application status / why rejected | Decision explanation | "Why was my loan application denied?" [C] | "Kredi başvurum neden reddedildi" [brief]; "Kredi Başvurum Açıklamasız Reddedildi" [SV] | P3 | Credit / underwriting | CLINC application_status; CFPB "Application denied" 1,750 |
| F2 | Credit → restructuring / deferral (öteleme/yapılandırma), hardship | Financial difficulty | "I can't pay my card this month" [C] | "Kredi kartı borcumu yapılandırmak istiyorum" [C] | P2 + vulnerability check | Collections / credit | BDDK 2025: 18,638 (8.0%), doubled after Board Decision 11240 |
| F3 | Credit → repayment, instalments, early payoff, payoff amount | Servicing | "How much to pay off my loan?" [C] | "Erken Kapatılan Taksitli Nakit Avanslara Yansıtılan Açıklanamayan Borçlar" [SV] | P3 | Loan servicing | Bitext check_loan_payments |
| F4 | Credit → collections conduct complaint | Calls, threats, wrong debt | "Collectors keep calling me" [C] | "Avukat Ve Şube Çalışanlarının Tehdit Ve Kanunsuz Para Blokajı İddiaları" [SV] | P2 + complaint | Collections QA / complaints | CFPB debt collection: 40.8% "attempts to collect debt not owed" |
| F5 | Credit → credit report / KKB-Findeks error, blacklist, record amnesty | Bureau data | "My credit report is wrong" [C] | "Findeks'te Hatalı Gecikme Kaydı Kredi Kullanımını Engelliyor" [SV] | P3 | Credit ops (bureau reporting) | BDDK "Kredi Notu/Sicil Affı/Kara Liste" 6,863 |
| F6 | Credit → lien/pledge release after payoff (rehin/ipotek fekki) | Post-closure | "Loan is paid, lien still on my car" [C] | "Kapanan Taşıt Kredisi Rehini Hâlâ Kaldırılmadı" [SV] | P3 (P2 if a sale is pending) | Loan ops | — |
| G1 | Fees → unexpected fee/charge on account or statement | Fee objection | "In my statement, I got a £1 extra fee." [B77] | "Hesabımdan habersiz ücret kesilmiş" [C] | P3 + complaint likely | Fees / product ops | B77 extra_charge_on_statement; EBA: fees = 2nd payment-services complaint reason |
| G2 | Fees → fee schedule information | Info | "How much is an EFT fee?" [C] | "EFT ücreti ne kadar?" [C] | P4 | L0 | Bitext check_fees |
| G3 | Fees → unrequested tied product / insurance premium deduction | Bancassurance | "I was charged for insurance I never agreed to" [C] | "Hesabından Onaysız Hayat Sigortası Kesintisi Ve İade Talebi" [SV] | P3 + complaint | Bancassurance ops | TBB: insurance 1% of direct complaints; TBB insurance committee customer-favour rate 64% (2024) |
| H1 | Life events → bereavement / estate (vefat, veraset) | Deceased customer's accounts | "My father passed away; what do I do with his accounts?" [C] | "Babam vefat etti, hesapları için ne yapmam gerekiyor?" [C] | P2 (sensitive) | Bereavement/estates team or branch | FCA: good practice routes bereavement chatbot queries to a human; FOS "Executorships or Trusteeships" 30 |
| H2 | Third parties → power of attorney / representative / guardian | Acting for someone else | "I have power of attorney for my mother" [C] | "Annem adına vekaletnameyle işlem yapmak istiyorum" [C] | P3 | Ops / legal | TBB/TKBB rules exclude third-party complaints without a POA |
| I1 | Products → rates, deposits, product information | Info / sales | "What's your deposit rate?" [C] | "Vadeli mevduat faiz oranları nelerdir?" [BP: Garanti chatbot] | P4 | L0 / sales | CLINC interest_rate, apr |
| I2 | Products → FX and gold accounts | Rates, conversions, gold account issues | "What's the exchange rate?" [C] | "1 Dolar kaç TL?" [BP: Garanti chatbot]; "Altın Hesabından İzinsiz Kesinti" [SV] | P4/P3 | Treasury / branch | B77 exchange_rate; TKBB "Döviz/Kıymetli Maden" category |
| I3 | Products → investment products | Brokerage / funds | "My fund order didn't execute" [C] | "Fon alım talimatım gerçekleşmedi" [C] | P3 | Investment ops; external route TSPB (TR) | İş Bankası: capital-markets disputes → TSPB within 60 days |
| J1 | Rewards → points/cashback (bonus, puan, chip-para, etc.) | Loyalty | "My rewards points are missing" [C] | "Kredi Kartı Yetkisiz Jest Lira Kesintileri" [SV] | P4/P3 | Card rewards ops | CLINC rewards_balance, redeem_rewards; CFPB "Problem with rewards" 1,929 |
| J2 | Rewards → salary/pension promotion (maaş/emekli promosyonu), commitment period, transfer restrictions | TR-specific | — | "3 yıllık maaş taahhütüm ne zaman doluyor?" [BP: Garanti chatbot] | P3 | Retail products / branch | Ziraat #Promosyon complaints [SV] |
| J3 | Campaigns → advertised terms not honoured | Marketing | "I didn't get the promised bonus" [C] | "Kampanya puanım yüklenmedi" [C] | P3 + complaint | Marketing ops | CFPB "Didn't receive advertised or promotional terms" 1,797 |
| K1 | Service → request a human | Escalate out of automation | "Let me talk to a person" [C] | "Müşteri temsilcisine bağlanmak istiyorum" [brief]; "Müşteri temsilcisine bağlanamıyorum" [SV] | Inherits underlying intent; never block | Routing | Bitext human_agent; Gartner: 87% say a human option is essential |
| K2 | Service → new complaint about service/staff/process | Dissatisfaction | "This is terrible, i want to delete my account" [B77] | "Gişe Personelinin Hassas Durumda Empati Eksikliği" [SV] | P3 + complaint | Complaints unit | CFPB "Problem with customer service" 887 (cards) |
| K3 | Service → complaint status / follow-up / overdue | Case tracking | "Nobody has told me the result of my dispute" [C] | "Referans numaram var, şikayetim hâlâ sonuçlanmadı" [C] | P3 (P2 if overdue or repeat) | Case owner | CFPB "Was not notified of investigation status or results" 7,959 (cards) |
| K4 | Service → how to escalate externally (Hakem Heyeti, BDDK, THH, FOS, CFPB) | Signposting | "How do I go to the ombudsman?" [C] | "Hakem Heyeti'ne nasıl başvururum?" [C] | P3 | Complaints unit | TBB: 22% of applications rejected for procedural gaps |
| K5 | Service → callback not received / broken promise | Failure demand | "You said you'd call me back" [C] | "Beni arayacaktınız, kimse aramadı" [C] | P3 + complaint | Case owner | Şikayetvar "yanıt alınamaması" titles |
| K6 | Service → complaint about chatbot/IVR/automation | Automation friction | "Your bot keeps looping" [C] | "Sistem sürekli 'ürününüz bulunmamaktadır' diyor" [SV snippet] | P3 + complaint | Digital CX | Gartner 2026 |
| L1 | Data protection → KVKK/GDPR data-subject request (copy, correction, deletion, call recording) | Privacy rights | "I want a copy of my call recording" [C] | "Görüşmemin ses kaydını istiyorum" [C] | P3 (statutory clock) | DPO / KVKK office | KVKK art. 13 (30 days, free) [V/02]; KVKK Board decision 2023/1050 (bank and call-recording transcript) |
| L2 | Marketing → opt-out of commercial messages | Consent | "Stop sending me promo SMS" [C] | "Reklam SMS'i göndermeyin" [C] | P4 (3-business-day clock in TR) | Marketing ops | İş Bankası table citing the e-message regulation |
| L3 | Accessibility / disability adjustments | Reasonable adjustments | "I'm visually impaired; can you send it in another format?" [C] | "Görme engelliyim, işlem için yardım istiyorum" [C] | P3 | Accessibility lead / branch | BDDK "Engelli Kişilerin Bankacılık İşlemleri" 212 (2025) |
| M1 | Out of scope → belongs to another institution | Signpost (insurance, capital markets, telco, e-commerce merchant, state) | "My insurer won't pay" [C] | "Sigorta şirketi hasarı ödemiyor" [C] | P4 | L1 signposting | BDDK top category: 21.8% of 2025 applications were in another body's remit |
| M2 | Commercial/SME customer issues | Business banking | "Our POS settlement is late" [C] | "Üye işyeri ödememiz gecikti" [C] | P3 | Commercial desk | BDDK "Ticari Müşteri" 10,154 (2025, ×1.78); FOS business current accounts 4,091; merchant services 774 |

### Gaps
- No published vendor banking intent libraries (Google, Amazon, Kore.ai, IBM etc.) were retrieved, so they could not be checked. Bitext is the only vendor library verified here.
- I found no public Turkish-language banking intent dataset. Turkish examples come from complaint platforms (anecdotal) and from constructed phrases.
- The urgency levels are my design [RP]. They are not found in any standard, except that TR regulation gives explicit priority to lost/stolen/suspicious-transaction calls.

---

## KQ2. What official complaint datasets show (US, UK, EU, Türkiye)

### Takeaway
Wherever complaints are counted, **cards and current/deposit accounts dominate**:
- TR: 66% of 3.68m complaints made directly to Turkish banks in 2024 were about bank and credit cards.
- UK: current accounts + credit cards = 82.8% of UK banking complaints in 2025 H2.
- **Fraud/scams** is the biggest single theme in ombudsman and supervisory data: FOS current accounts (57%), EBA top issue, and fraud is a top-6 BDDK topic.

US CFPB volumes are swamped by credit reporting (88% in 2025). Outside credit reporting, debt collection, credit cards, money transfer and checking/savings lead. Türkiye shows spikes driven by regulation (restructuring applications doubled in 2025).

### Cited Findings

**US — CFPB Consumer Complaint Database** (queried by API on 10 Oct 2026; calendar 2025 = date_received ≥ 2025-01-01 and < 2026-01-01; `date_received_max` is exclusive per the [API spec](https://github.com/cfpb/ccdb5-api))
- 2025 total: **5,452,094** complaints — [CFPB API 2025](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0).
  - Credit reporting/other personal consumer reports: 4,818,215 (**88.4%**)
  - Debt collection: 283,827 (5.2%)
  - Credit card: 90,157 (1.65%)
  - Money transfer/virtual currency/money service: 84,708 (1.55%)
  - Checking/savings: 84,348 (1.55%)
  - Mortgage: 24,735 (0.45%)
  - Student loan: 21,325; vehicle loan/lease: 20,823; payday/title/personal/advance loans: 13,167; prepaid: 6,516; debt/credit management: 4,273
  - Excluding credit reporting (633,879): debt collection 44.8%, credit card 14.2%, money transfer 13.4%, checking/savings 13.3% (my calculation from the same query).
- **Checking/savings 2025 (84,348)** — [CFPB API, checking/savings](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Checking%20or%20savings%20account)

  | Issue | Count | Share of product | Sub-issues (share of the issue) |
  |---|---|---|---|
  | Managing an account | 45,046 | 53.4% | Deposits and withdrawals 17,421 (38.7%); Problem using a debit/ATM card 9,809 (21.8%); Funds not handled or disbursed as instructed 5,227 (11.6%); Banking errors 4,264 (9.5%); Problem accessing account 3,404 (7.6%); Problem making or receiving payments 2,744 (6.1%) |
  | Problem caused by your funds being low | 11,945 | 14.2% | Overdrafts and overdraft fees 9,814 |
  | Closing an account | 10,194 | 12.1% | Company closed your account 5,051; Funds not received from closed account 3,470; Can't close your account 1,450 |
  | Problem with a lender or other company charging your account | 9,635 | 11.4% | Transaction was not authorized 7,978 |
  | Opening an account | 6,974 | 8.3% | Unable to open 2,673; Opened without consent 2,571 |

  Company response: closed with explanation 84.5%, monetary relief 10.6%, non-monetary relief 4.8%.
- **Credit card 2025 (90,157)** — [CFPB API, credit card](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Credit%20card)

  | Issue | Count | Share of product | Notable sub-issues |
  |---|---|---|---|
  | Problem with a purchase shown on your statement | 19,857 | 22.0% | Company isn't resolving a dispute about a purchase 14,758; Charged for something you did not purchase 4,547 |
  | Incorrect information on your report | 13,760 | 15.3% | — |
  | Getting a credit card | 10,830 | 12.0% | Card opened without consent 7,817; Application denied 1,750 |
  | Problem with a company's investigation into an existing problem | 10,131 | 11.2% | **Was not notified of investigation status or results 7,959** |
  | Other features/terms/problems | 8,438 | 9.4% | Rewards 1,929; Customer service 887 |
  | Fees or interest | 7,854 | 8.7% | — |
  | Closing your account | 6,233 | 6.9% | Company closed your account 5,040 |
  | Problem when making payments | 4,602 | 5.1% | — |
  | Advertising/marketing | 3,112 | 3.5% | — |
  | Trouble using your card | 3,030 | 3.4% | — |
  | Struggling to pay your bill | 1,237 | 1.4% | — |

- **Money transfer/virtual currency 2025 (84,708)** — [CFPB API, money transfer](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Money%20transfer%2C%20virtual%20currency%2C%20or%20money%20service)
  - Other transaction problem 53,903 (63.6%)
  - Fraud or scam 11,196 (13.2%)
  - Unauthorized transactions or other transaction problem 5,773 (6.8%)
  - Trouble accessing funds in mobile/digital wallet 3,059 (3.6%)
  - Money not available when promised 2,434 (2.9%)
  - No sub-issues are recorded for this product.
  - Sub-products: domestic transfer 68.3%, mobile/digital wallet 20.3%, virtual currency 6.5%.
- **Debt collection 2025 (283,827)** — [CFPB API, debt collection](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Debt%20collection)
  - Attempts to collect debt not owed 40.8%. Within it: debt not yours 65,598; debt resulting from identity theft 38,922.
  - Written notification about debt 22.6%
  - Took or threatened negative or legal action 17.2%
  - False statements 13.6%
  - Communication tactics 3.4%
- **2026 year to date (1 Jan–30 Sep 2026):** 5,537,319 complaints, already more than all of 2025. Credit reporting 91.0%, debt collection 4.4%, credit card 1.3%, checking/savings 1.2%, money transfer 0.5%; 10.1% still "In progress" — [CFPB API 2026 YTD](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2026-01-01&date_received_max=2026-10-01&size=0).
- **Caveats stated by CFPB** — [CFPB database page](https://www.consumerfinance.gov/data-research/consumer-complaints/):
  - Only complaints sent to companies are published, "after the company responds… or after 15 days, whichever comes first".
  - Complaints referred to other regulators are not published, e.g., depository institutions with assets under $10bn.
  - The database "is not a statistical sample of consumers' experiences".
- **CFPB process:** "Companies generally respond in 15 days"; in some cases a final response in 60 days. Consumers then have 60 days to give feedback — [CFPB complaint process](https://www.consumerfinance.gov/complaint/process/) (read via search extract; the page blocked direct fetch).

**UK — FCA aggregate complaints data, 2025 H2 (1 Jul–31 Dec 2025)** (first published 28 Apr 2026, updated 15 May 2026) — [FCA 2025 H2](https://www.fca.org.uk/data/complaints-data/aggregate-complaints-data-2025-h2); [XLSX](https://www.fca.org.uk/publication/data/aggregate-complaints-data-2025-h2.xlsx)
- Firms received 1.74m complaints; banking & credit cards received 857,757 (49.3% of the total, my calculation from the XLSX).
- The FCA text says total complaints fell "0.4%" from 1.83m. **Discrepancy:** the XLSX totals (1,828,501 → 1,740,909) imply a 4.8% fall. The FCA's own figures suggest the "0.4%" is a typo.
- Banking & credit cards by product, 2025 H2 (XLSX):

  | Product | Complaints | Share of banking group |
  |---|---|---|
  | Current accounts | 492,149 | 57.4% (down 9.1% vs H1) |
  | Credit cards | 218,456 | 25.5% (up 3.1%) |
  | Savings incl. ISAs | 82,465 | 9.6% |
  | Overdrafts | 26,456 | 3.1% (up 63.4%) |
  | Other banking | 23,166 | 2.7% |
  | Packaged accounts | 15,065 | 1.8% |

- Banking complaints closed in H2: 47.9% within 3 days, 46.0% between 3 days and 8 weeks, 6.1% after more than 8 weeks. 54.3% were upheld. Redress was about £116.7m (my calculation from XLSX rows).
- All-sector upheld rate was 55.54%, and 44.77% of complaints were closed within 3 days — [FCA 2025 H2](https://www.fca.org.uk/data/complaints-data/aggregate-complaints-data-2025-h2).

**UK — Financial Ombudsman Service, 2025/26 (Apr 2025–Mar 2026)** (published 21 May 2026) — [FOS 2025/26](https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/our-insight/annual-complaints-data-and-insight-2025-26); [XLSX](https://www.financial-ombudsman.org.uk/files/324759/Annual-complaints-data-2025-26.xlsx)
- 214,600 new complaints, almost 30% fewer than 305,700 in 2024/25. Average uphold rate 30%.
- Largest products:
  - Hire purchase (motor) 37,673
  - **Current accounts 32,907** — "fraud and scams accounting for 18,900" (57%), uphold rate 28%
  - **Credit cards 22,783** — 8,800 about irresponsible/unaffordable lending, down from 49,400 in 2024/25
  - Car/motorcycle insurance 13,420
  - E-money 8,933
- Note on order: the page's "top five" graphic lists e-money second, but the XLSX ranks it fifth. I treat the graphic as unordered.
- Smaller banking lines (XLSX):
  - Overdrafts 5,863; debit cards 2,192; cash ISAs 1,619; deposit/savings 1,294
  - Merchant services 774; packaged accounts 480; international transfers 477; direct debits 391; online banking 328
  - Cheques 224; money remittance 172; foreign currency 49; CHAPS 41; executorships/trusteeships 30; safe custody 32
  - Banking & Payments ≈ 39.7% of all new FOS cases (my sum of numeric rows; rows shown as "<10" are excluded).
- Professional representatives brought 18% of cases (38,600), down from 50% in 2024/25 after FOS introduced case fees for them.

**EU — EBA Consumer Trends Report 2024/25** (26 Mar 2025, EBA/REP/2025/08; corrected 22 Apr 2025) — [EBA press release](https://www.eba.europa.eu/publications-and-media/press-releases/eba-identifies-payment-fraud-indebtedness-and-de-risking-key-issues-affecting-consumers-eu); [PDF](https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf)
- Top issues for EU consumers: (1) payment fraud, (2) indebtedness (BNPL and small fast credit), (3) de-risking (refused onboarding or offboarding).
- National authority (NCA) and FIN-NET data for 2022–2023, ranked qualitatively; the report gives no counts in the passages reviewed:
  - **Payment services** had the highest number of complaints. Reasons: unauthorised transactions, then fees and charges, then execution problems (incorrect, late, timing).
  - **Payment accounts** were second. Reasons: account closing, then denial of access, then unduly charged fees (maintenance).
  - Deposits: termination, fees, information, interest calculation.
  - Consumer credit: interest calculation and application, information and creditworthiness assessment, fees.
  - Mortgages: interest rates, fees (early repayment), transparency, information, cross-selling.
  - E-money: unclear terms and conditions, especially on fees and safeguarding.
- The CTR is biennial, so 2024/25 is the latest edition I found. It may be superseded in 2027.

**Türkiye — BDDK 2025 annual report** (section 9; published by late May 2026 per press coverage) — [BDDK Faaliyet Raporu 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527) [TR]
- Applications to BDDK: 228,334 (2023), 178,108 (2024), **231,664 (2025, +30%)**. BDDK attributes the rise to restructuring applications after Board Decision 11240 of 10.07.2025 (credit-card debt and consumer-loan restructuring).
- Channels:
  - CİMER 139,637 (60%)
  - BDDK direct channels 92,027, of which e-şikâyet 81,267 (+21%)
  - The remaining 8,207 and 2,553 are petition and call centre; which is which could not be read reliably from the PDF.
- **Topics 2025, count (share)**; the 2024 figures are re-mapped to the new 2025 scheme:

  | Topic | 2025 | 2024 |
  |---|---|---|
  | Another body's remit | 50,466 (21.8%) | 41,277 |
  | Deposits / participation funds | 33,179 (14.3%) | 24,822 |
  | **Bank & credit cards** | 26,537 (11.5%) | 12,599 (×2.1) |
  | Alternative distribution channels | 23,761 (10.3%) | 19,808 |
  | **Deferral/restructuring** | 18,638 (8.0%) | 9,336 (×2.0) |
  | **Fraud** | 17,602 (7.6%) | 19,411 |
  | Enforcement (icra) problems | 10,926 (4.7%) | 9,090 |
  | Commercial customer | 10,154 (4.4%) | 5,716 |
  | Credit/card application & limit | 8,634 (3.7%) | — |
  | Credit score / record amnesty / blacklist | 6,863 (3.0%) | — |
  | Non-bank institutions | 5,825 (2.5%) | — |
  | Savings-finance companies | 4,048 (1.7%) | — |
  | Consumer loans | 3,839 (1.7%) | — |
  | KMH | 3,197 (1.4%) | — |
  | Info/document requests to institutions | 3,099 (1.3%) | — |
  | Whistleblowing (ihbar) | 2,325 (1.0%) | — |
  | Info requests to BDDK | 1,715 (0.7%) | — |
  | Non-specific | 644 (0.3%) | — |
  | Banking for persons with disabilities | 212 (0.1%) | — |

  The narrative of the report confirms which category is the largest (another body's remit), so the row-to-number mapping is reliable.
- Other 2025 facts from the same section:
  - BDDK fined **7 banks** for not meeting the call-centre service-level ratios.
  - It approved 13 appointments of consumer-relations coordination officers.
  - It held disability focus groups, with sector measures planned for 2026.

**Türkiye — complaints made directly to TBB member banks** (TBB 2024 report, May 2025) — [TBB 2024 report](https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf) [TR]
- **3,681,698 applications to banks in 2024** (3,680,218 in 2023). The series in thousands: 2,796 (2020), 2,830 (2021), 3,149 (2022), 3,680 (2023), 3,681 (2024).
- By product: bank & credit cards 2,445,079 (**66%**); other banking products 1,124,802 (31%); consumer loans 79,163 (2%); insurance 32,654 (1%).
- By topic (thousands, 2024):
  - Cards 2,445 (66%) — explicitly includes loss/theft/fraud notifications and spending objections
  - **Alternative distribution channels 810 (22%)**
  - Deposits 243 (6%) — includes safe-deposit boxes and money/value transfers
  - Loans 79 (2%); insurance 33 (1%); bills & other payments 30 (1%); KMH 23 (1%); investment 18 (1%)
- This is the closest thing to a national Turkish **contact-reason distribution**. Because cards include fraud notifications and objections, it is "applications" (başvuru), not only formal complaints.
- The 2025 TBB report was not yet listed on the TBB site on 10 Oct 2026; the URL for a 2025 PDF returned 404 — [TBB annual reports page](https://www.tbb.org.tr/faaliyetler/bireysel-musteri-hakem-heyeti/yillik-raporlar).

**Türkiye — TBB Bireysel Müşteri Hakem Heyeti** (deposit-bank arbitration committee), 2024 — [TBB 2024 report](https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf)
- 29,334 applications (−10%; 32,615 in 2023): 74% cards, 16% other banking, 6% insurance, 4% consumer loans.
- 36% were not admitted: 22% for procedural gaps (form, bank reply, signature), 13% for time limits, matter already in court, or non-individual matters, 1% withdrawn.
- Of admitted applications: 46% resolved in the customer's favour because the bank met the request; 49% bank-favourable committee decision; 5% customer-favourable committee decision. That gives "51% customer-favourable" overall.
- Customer-favour rate in committee decisions: 9% overall (cards 5%, other banking 3%, loans 8%, insurance 64%).
- 3,265 applications were resolved by banks at the pre-evaluation stage.

**Türkiye — TKBB** (participation banks) arbitration committee 2025 (report Feb 2026) — [TKBB 2025 report](https://tkbb.org.tr/upload/raporlar/018-01.01.2025%20-%2031.12.2025%20YILLIK%20FAAL%C4%B0YET%20RAPORU%20%C4%B0%C3%87%C4%B0N%20TIKLAYINIZ.pdf)
- 1,555 applications, of which 410 were redirected to TBB. That leaves **1,145** for participation banks (+31% from 874), including 230 forwarded by BDDK.
- By topic: bank & credit cards 551 (40.1%, +178%), individual finance 292 (21.2%), **ATM 230 (16.7%)** (now reported as its own category because of growth), participation funds 208 (15.1%).
- Decisions: 20.4% fully and 2.2% partly in the customer's favour; 75.7% in the bank's favour.
- 279 applications were returned as out of scope: time limits, commercial matters, transaction never occurred, the bank's credit policies, or matter in court.

**Türkiye — Tüketici Hakem Heyetleri** (consumer arbitration committees), 2025 (Ministry of Trade, 21 Jan 2026) — [Ticaret Bakanlığı](https://ticaret.gov.tr/haberler/tuketici-hakem-heyetleri-2025-yilinda-907-bini-askin-basvuruyu-karara-baglayarak-12-4-milyar-tllik-uyusmazligi-yargiya-tasimadan-cozume-kavusturdu)
- 907,515 applications (+20%); 849,143 decided; about 12.4bn TL in value; 72% filed via e-Devlet.
- **Financial services sector: 86,637 (9.54%)**, third after retail (53.35%) and subscriptions (11.47%).
- By product, **"Kredi kartı üyelik ücreti" (credit-card membership fee) = 3.97%** of all applications, the third-largest product after apparel/footwear (19.6%) and mobile lines (4.75%). Card-fee refunds are therefore a high-volume, externally escalated intent.

**Türkiye — TCMB** [TR]
- TCMB's complaint system handles fee/commission complaints under Communiqués 2020/4 (commercial customers) and 2020/7 (financial consumers), plus payment-services matters — [TCMB Şikayet Yönetim Sistemi](https://esikayet.tcmb.gov.tr/mbnesspfe-kullanici/).
- Fee, commission and interest complaints go through the TCMB system — [TCMB Bilgi Edinme](https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/bottom+menu/diger/bilgiedinme).
- **I found no published TCMB complaint-volume statistics.** TCMB reported 2,167 *information requests* (not complaints) about payment/e-money institutions in 2025 — [TCMB DUY2026-04](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2026/DUY2026-04).

**Türkiye — Şikayetvar** (anecdotal signal only; a private platform, not a statistical sample)
- 2025, per specialist press (egirisim, 12 Feb 2026) citing Şikayetvar — [egirisim](https://egirisim.com/2026/02/12/sikayetvar-2025-verilerini-acikladi-dolandiricilik-ve-bahis-siteleri-gundemde/):
  - 2,868,914 complaints in total; finance sector 312,396 (2nd largest sector)
  - Within finance: **account transactions 36%, credit cards 31%, ATM & branch 22%**
  - "Özel bankalar" (private banks) category: 134,944
  - Fraud complaints 40,105, including "dava/icra SMS" scams 11,368 (+162%)
- Ziraat Bankası brand page: 64,283 complaints; "son 1 yılda şikayetleri cevaplama oranı %96". Its tags show the topic spread: Kredi Kartı, Para Çekme, Banka Kartı, Promosyon, Harçlık Avans, Sigorta, Döviz, Troy Kart, Kira Yardımı, Taşıt Kredisi — [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
- "Banka hesabı dolandırıcılığı" page: complaints are dominated by bank-staff impersonation that asks for the "onay kodu" (OTP) under pretexts of a loan offer, insurance refund or suspicious transaction (109 complaints cited), and by public-official impersonation — [Şikayetvar](https://www.sikayetvar.com/banka-hesabi-dolandiriciligi).

### Inferences
- **For Türkiye, plan capacity around cards, then digital channels, then deposits/transfers.** The TBB 66/22/6 split is the best national proxy. Because the cards bucket includes fraud notifications and spending objections, a large share of "card" contacts are P1/P2 security or dispute contacts, not routine ones.
- **Regulation-driven spikes are real and sudden.** Restructuring applications to BDDK doubled in 2025 after Board Decision 11240, and card complaints rose ×2.1. The taxonomy and intent catalogue need a fast path to add "event intents" when a new rule, outage or scam wave appears [RP].
- **"Another institution's remit" is the largest BDDK bucket (21.8%).** The agent must recognise and signpost out-of-scope issues (insurance → insurer/SEDDK, capital markets → TSPB/SPK, merchants → THH), not treat them as noise [RP].
- **Dispute-investigation status updates are a complaint driver in their own right.** In US credit cards, "Was not notified of investigation status or results" alone accounts for 7,959 complaints. Proactive status updates are an obvious way to reduce failure demand [RP].
- UK data supports fast first-contact resolution: about 45–48% of complaints are closed within 3 days. Most complaints are therefore operationally simple, so the agent should resolve them while still logging them as complaints [RP].

### Gaps
- FIN-NET complaint counts were not retrieved; the EBA CTR passages reviewed give rankings, not numbers.
- No TCMB complaint statistics were found.
- The TBB 2025 report is not yet published, so the newest Turkish direct-to-bank figures are for 2024.
- BDDK: the mapping of the petition and call-centre channel counts is uncertain.
- No reliable national data was found on the share of *contacts* (as opposed to complaints) by reason for any jurisdiction. CFPB, FCA and FOS cover complaints only.

---

## KQ3. Industry and academic evidence on contact drivers, failure demand and channel shift

### Takeaway
Rigorous public data on *why customers contact banks* (as opposed to why they complain) is scarce. The best proxies are complaint category data (KQ2) and intent datasets (KQ1). Industry surveys consistently show:
- self-service resolves only a minority of issues;
- customers insist on a route to a human;
- problem resolution and routine moments (alerts, transfers, fees) drive satisfaction and "soft switching".

"Failure demand" (contacts caused by earlier service failure) is a well-defined concept, but I found no banking-specific measurement.

### Cited Findings
- **J.D. Power 2026 U.S. Retail Banking Satisfaction Study** (industry; 26 Mar 2026; n = 107,059 customers of the largest US banks; fielded Jan 2025–Jan 2026) — [J.D. Power](https://www.jdpower.com/business/press-releases/2026-us-retail-banking-satisfaction-study):
  - Overall satisfaction 657/1,000 (+2), but with "sharp declines in the second half of the year… with phone, branch, online and automated customer engagement channels".
  - 20% of customers moved money from their primary bank in the past 3 months (17% the year before). The average checking customer holds three deposit accounts at different institutions.
  - Problem-resolution satisfaction: national banks 587 (+49 vs 2024); midsize banks 548 (−27).
  - Top banks treat "alerts, funds transfers, fees and face-to-face interactions" as moments that build confidence.
  - Satisfaction has seven dimensions, including "resolving problems or complaints".
- **Gartner** (industry; general customer service, not banking-specific):
  - Only 14% of service issues are fully resolved in self-service; only 36% even for "very simple" issues (n = 5,728, Dec 2023; press release 19 Aug 2024) — [Gartner 2024](https://www.gartner.com/en/newsroom/press-releases/2024-08-19-gartner-survey-finds-only-14-percent-of-customer-service-issues-are-fully-resolved-in-self-service) (read via search extract).
  - 87% of customers say an option to reach a human is essential when GenAI is used; 50% say interactions are easier with GenAI (n = 3,566 B2B/B2C, Feb–Mar 2026; 4 Aug 2026) — [Gartner 2026](https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0).
  - The same release advises "Service leaders should not use GenAI as a mandatory first step for every issue". It says GenAI should "attempt resolution only when confidence is high, with a clear path to human support".
  - 58% of GenAI users have used it to complete a task (74% in B2B).
  - Customers were about 3× more likely to use third-party GenAI tools (ChatGPT, Gemini, Copilot) than company chatbots in their latest service interaction — cited inside the same release; linked [Gartner 8 Jul 2026](https://www.gartner.com/en/newsroom/press-releases/2026-07-08-gartner-survey-finds-customers-are-three-times-more-likely-to-use-third-party-genai-than-company-provided-chatbots-for-customer-service).
- **Failure demand.** Definition: "demand caused by a failure to do something or do something right for the customer" (John Seddon), as opposed to value demand. The Open University example is a council housing service where 80% of 1,200 analysed calls were failure demand. No financial-services figure is given — [OpenLearn](https://www.open.edu/openlearn/society-politics-law/criminology/capacity-and-demand-management/content-section-12).
- **UK supervisory evidence on support friction** — FCA "Consumer support outcome: good practices and areas for improvement" (UK regulator good/poor-practice guidance; published 7 Mar 2025, updated 10 Jul 2026) — [FCA](https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement):
  - Found "longer wait times for existing customers looking to terminate or downgrade".
  - Cites as good practice "automatically directing queries from a webchat chatbot about bereavement to a customer support representative".
  - Criticises monitoring that "relied on transactional metrics, such as contact rates and wait times".
- **Channel shift, as seen in complaint data:**
  - Turkish ADC complaints: 22% of 3.68m direct complaints (TBB 2024) and 10.3% of BDDK applications (2025).
  - BDDK e-şikâyet grew 21% in 2025; 72% of consumer-arbitration filings were made via e-Devlet (KQ2 sources).
  - 99.3% of 2025 CFPB complaints were submitted via the web — [CFPB API 2025](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0). This is the complaint-filing channel, not the bank-contact channel.
- **Academic NLP:** BANKING77/CLINC150/Bitext and their limits (KQ1); label noise in BANKING77 — [Ying & Thomas 2022](https://aclanthology.org/2022.insights-1.19/).

### Inferences
- **"Where is my money" is the biggest problem-type cluster that recurs across sources:**
  - BANKING77 has about 10 labels for it.
  - CFPB checking: "Deposits and withdrawals" is the top sub-issue.
  - CFPB money transfer: "Other transaction problem" is 64%.
  - Şikayetvar finance: account transactions 36%.
  - TBB deposits include transfers.

  No reliable source gives its share of *calls*. I recommend measuring it with the agent's own tagging [RP].
- Much failure demand in banking is probably status-chasing on disputes, transfers and complaints, plus repeat contacts after broken callbacks. CFPB "not notified of investigation status" and Şikayetvar "yanıt alınamaması" titles are consistent with this. **Proactive status messages and case-linked recontact handling** are the main levers [RP][V].

### Gaps
- McKinsey and Deloitte/Accenture banking-specific contact-driver data could not be retrieved: the McKinsey PDF and page timed out or were blocked. They are not cited.
- No peer-reviewed study was found that quantifies retail-bank call reasons or failure demand in banking.

---

## KQ4. Customer language (EN/TR) and mapping symptoms to underlying intents

### Takeaway
Customers describe **symptoms** ("param kayboldu", "EFT gitmedi", "kartım geçmiyor"), not product intents. Turkish wording mixes formal banking terms (EFT, FAST, IBAN, provizyon, bloke, haciz, KMH, ekstre, aidat) with colloquial verbs:
- "yuttu" — "it swallowed" (the ATM kept the card)
- "geçmedi" — "didn't go through / didn't arrive"
- "yansımadı" — "isn't showing / wasn't reflected"
- "çekilmiş" — "has been withdrawn"
- "kesilmiş" — "was deducted"

The agent should first map the symptom to a small set of candidate causes and then disambiguate with **safe, non-credential questions**.

### Cited Findings — real phrasings (anecdotal unless noted)
- **EFT/transfer.** "EFT Yaptım Hesaba Geçmedi", "Hesabıma Para Geçmedi", "EFT İşlemi Yapıldı Ama Para Gelmedi" (Şikayetvar topic titles). Body text: "…EFT işlemi yaptım. Ancak gönderdiğim para ne alıcı hesaba geçti ne de kendi hesabıma geri döndü." Other titles: "Askıda Kalan EFT İşleminin Gecikmeli İadesi…", "EFT İle Yatırdığım Para Hesaba Yansımadı Ve Canlı Destek Sorumluluk Reddi", "Yanlış Alıcı İsmi Nedeniyle 92.700 TL EFT Parası Geri Ödenmedi" — [Şikayetvar EFT](https://www.sikayetvar.com/eft-hesaba-gecmedi).
- **ATM.** "Banka Kartımı Yuttu", "Bankamatik Kartı Yuttu", "Akbank ATM'si 34 Bin TL Ve Kartı Yuttu…", "ATM Zaman Aşımı Sorunu…" — [Şikayetvar](https://www.sikayetvar.com/banka-kartimi-yuttu); "ATM'den Para Alındı Ama Hesaba Yatırılmadı", "ATM'de 200 TL Çekim İadesi Sorunu" — [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
- **Access/OTP.** "Şifre SMS Gelmiyor", "Ziraat Sms Gelmiyor", "Doğrulama Kodu Gelmiyor / Kod Gelmiyor", "Şifre Giriş Yapamıyorum", "Şifre Bloke", "Bloke Kaldırmak… İnternet Bankacılığı" — [VakıfBank](https://www.sikayetvar.com/vakifbank/sifre/sms-gelmiyor), [DenizBank](https://www.sikayetvar.com/denizbank/dogrulama-kodu-gelmiyor/kod-gelmiyor), [Akbank](https://www.sikayetvar.com/akbank/sifre-bloke), [Halkbank](https://www.sikayetvar.com/halkbank/sifre/giris-yapamiyorum).
- **Human access.**
  - "ING Bank mobil uygulaması üzerinden bir türlü müşteri temsilcisine ulaşamıyorum"
  - "…sistem sürekli… 'ürününüz bulunmamaktadır' uyarısı" (the IVR blocks people who hold no product)
  - "…açık hesaplarımı kapatmak istiyorum ancak hiçbir şekilde müşteri temsilcisine bağlanamıyorum"
  - "Sistemin yönlendirmelerine göre defalarca tuşlama…"
  - A fraud-urgent case: "gece saat 03.35 civarında yaklaşık bir milyon tl tutarında şüpheli bir işlem yapılmak istenmiş" in a complaint titled "…Müşteri Temsilcisine Bağlanamıyorum!"
  - Sources: [Şikayetvar müşteri temsilcisine bağlanma](https://www.sikayetvar.com/musteri-temsilcisine-baglanma); [ING](https://www.sikayetvar.com/ing/musteri-temsilcisine-baglanma/yapamiyorum); [TEB](https://www.sikayetvar.com/teb/musteri-temsilcisine-baglanma/sorunu); [Ziraat](https://www.sikayetvar.com/ziraat-bankasi/ziraat-bankasi-musteri-temsilcisine-baglanamiyorum-video).
- **Fees.** "Kart Aidat İadesi", "Kredi Kartı Yıllık Aidatı Kesintisinin İadesi Talebi", "Yıllık Kart Aidatı Haksız Kesildi Ve İade Talebi", "…Yıllık Kart Ücretinin Tam İadesi Ve Mağduriyetimin Giderilmesi" — [Şikayetvar](https://www.sikayetvar.com/kart-aidat-iadesi), [QNB](https://www.sikayetvar.com/qnb-turkiye/kredi-karti-yillik-aidati-kesintisinin-iadesi-talebi), [Yapı Kredi](https://www.sikayetvar.com/yapi-kredi-bankasi/yillik-kart-aidati-haksiz-kesildi-ve-iade-talebi-2).
- **Credit decisions.** "Kredim Onaylanmıyor", "Kredi Başvurum Açıklamasız Reddedildi", "Kredi Kartı Başvurum Sürekli Reddediliyor Net Bir Açıklama Yapılmıyor", "Kredi Başvurumun Yapay Zeka Red Nedeni Açıklanmadı", "Findeks'te Hatalı Gecikme Kaydı Kredi Kullanımını Engelliyor" — [Şikayetvar](https://www.sikayetvar.com/kredim-onaylanmiyor), [Halkbank](https://www.sikayetvar.com/halkbank/kredi-basvurum-aciklamasiz-reddedildi), [İş Bankası](https://www.sikayetvar.com/is-bankasi/kredi-basvurumun-yapay-zeka-red-nedeni-aciklanmadi), [TEB](https://www.sikayetvar.com/teb/findekste-hatali-gecikme-kaydi-kredi-kullanimini-engelliyor).
- **Holds, benefits and other titles from the Ziraat page:**
  - "Hesabımdaki Parayı Kullanamıyorum!"
  - "İBB Kira Yardımı Parası … Blok Olmadan Çekilemiyor"
  - "Emekli Maaşına Haksız Bloke Ve Transfer Engeli"
  - "Kredi Kartı Kısıtı: Çelişkili Bilgiler Ve Açılmama Sorunu"
  - "Altın Hesabından İzinsiz Kesinti"
  - "Onaysız Hayat Sigortası Kesintisi"
  - "Kapanan Taşıt Kredisi Rehini Hâlâ Kaldırılmadı"
  - Source: [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
- **English dataset phrasings, from BANKING77 train.csv** (provenance undocumented) — [PolyAI GitHub](https://github.com/PolyAI-LDN/task-specific-datasets):
  - "What should I do since my card is trapped in the ATM?"
  - "Where is my money that I transfered?!" (sic)
  - "I'm checking the app and I see a payment that's not mine."
  - "How long does a payment show as pending before i should worry about it?"
  - "It is urgency. Please freeze my card now…" (sic)
  - "unhappy with service need to delete account"
  - "My refund for a purchase hasn't cone through yet." (sic)

  These show typos and urgency markers worth keeping in evaluation sets.
- **Platform caveat.** Şikayetvar titles are heavily standardised ("… Ve … Talebi"), which suggests platform or editor normalisation. The body excerpts are closer to raw customer language [V].
- **Provizyon (authorisation hold)** [BP:Halkbank]:
  - "Provizyon; kartlı alışverişler için onay sürecidir."
  - The amount is blocked on the card balance while it waits.
  - The typical wait is 1 day, and can be 2 days when the POS belongs to another bank.
  - "Provizyon iptal işlemi yalnızca banka tarafından gerçekleştirilebilir."
  - Source: [Halkbank blog](https://www.halkbank.com.tr/tr/blog/provizyon-nedir).
- **Account holds.** Holds can come from enforcement proceedings (icra), tax debts, SGK claims, court or prosecutor orders, or the bank's own security review. The first step is to identify the authority that placed it. Salary is protected in part — [ffkpartnerhukuk (law-firm blog, lower-tier; verify with 02)](https://www.ffkpartnerhukuk.com.tr/banka-blokesi-nasil-kaldirilir-hesaba-konulan-bloke-icin-adim-adim-rehber-2026/).

### Symptom → candidate intents → safe disambiguation (synthesis [RP]; causes need institution verification [V])

| Customer says (TR / EN) | Candidate underlying causes (intent IDs) | Safe disambiguating questions (never ask for PIN, password, CVV/CVC or OTP; never request remote access) |
|---|---|---|
| "Param kayboldu", "Hesabımdan para eksildi" / "my money disappeared" | **Common causes:** pending card authorisation (provizyon) (D1→B9/G1); completed transfer or standing order you set up (C7); bank hold (C3/D3); garnishment (haciz/e-haciz) (D4); fee, commission, interest, card fee or KMH interest (G1/B8/D8); auto-debited loan instalment or card minimum payment (F3/B12). **Fraud-type causes:** unauthorised transaction (A1/A2); duplicate charge (B9); scam payment the customer authorised (A3). **Cash and refund causes:** ATM debit without cash, or deposit not credited (D9); refund not yet posted (B9); FX/gold revaluation (I2). **Misreading the balance:** available vs ledger balance; KMH counted as available funds. **Other:** tied insurance premium (G3); promotion-related restriction (J2) [V]. | "Hareketlerde bu tutar hangi açıklamayla görünüyor? 'Provizyon/bekleyen' mi yazıyor?" · "Hangi tarihte, yaklaşık ne kadar?" · "Bu işlem için size SMS/bildirim geldi mi?" · "Hesap özetinde 'bloke' satırı var mı?" · "Son günlerde kimseyle bir kod veya şifre paylaştınız mı? (evet/hayır — kodu söylemeyin)" |
| "EFT gitmedi / Gönderdiğim para karşıya geçmedi" / "transfer not received" | Still processing or sent outside EFT operating hours (C1); wrong IBAN or name mismatch returned (C4); bank security hold (C3); failed and reversed (C5); recipient bank delay (C1); payment to a fraudulent or unlicensed recipient (A3) | "EFT mi FAST mı havale mi?" · "Gönderim saatini ve tutarı söyler misiniz?" · "Para hesabınıza geri döndü mü?" · "Alıcı sizin tanıdığınız biri mi, bir site/satıcı mı?" (scam screening) · Ask the customer to read out the **sorgu/referans numarası** shown in the app. It is not a secret. |
| "Kartım geçmiyor" / "card declined" | Insufficient limit/balance (B2); card blocked after wrong PIN attempts (B3); online/abroad usage closed (B10); fraud-rule block (A1); expired or damaged card (B5); unpaid statement that restricted the card (B12) | "Mağazada mı, internette mi, yurt dışında mı?" · "Ekranda/fişte bir hata mesajı yazıyor mu?" · "Kart yeni mi geldi, aktifleştirdiniz mi?" |
| "Şifrem bloke oldu" / "my password is blocked" | Card PIN blocked (B3) vs internet/mobile password locked (E2) vs SIM-change OTP block (E1) | "Hangi şifre: kart şifresi mi, internet/mobil şube şifresi mi?" · "Son zamanlarda hat/SIM kart değiştirdiniz mi?" |
| "SMS gelmiyor" / "OTP not arriving" | Wrong or old phone number on file (D10); SIM change triggered a security block (E1); operator/roaming issue; commercial-message opt-out confused with transaction SMS | "Bankada kayıtlı numaranız güncel mi?" · "Yurt dışında mısınız?" · "Hat değişikliği yaptınız mı?" — **never** ask the customer to read out the code |
| "Hesabıma bloke konmuş" / "my account is frozen" | Garnishment (haciz, e-haciz) (D4); KYC refresh or document request (D5); fraud or security review (C3/A7); de-risking or closure (D7); deceased-customer notification (H1); promotion or commitment restriction (J2) [V] | "Bloke ne zamandan beri var? Size bir bildirim (SMS, e-Devlet, UYAP, vergi dairesi) geldi mi?" · "Bloke tüm hesapta mı, belli bir tutarda mı?" Note: if the hold is AML-related, disclosure limits apply [V – team 02/10]. |
| "Haciz gelmiş" / "garnishment" | Enforcement office (icra dairesi), tax office/SGK e-haciz, or court order (D4) | "Hangi kurumdan bildirim aldınız?" → give the authority's details per bank policy and route to the legal-holds unit. The agent must not advise on the merits [V]. |
| "Kartımdan bilmediğim bir harcama var" | Fraud (A1); forgotten subscription or free trial; merchant name differs from brand; family member; pre-authorisation such as hotel or fuel (provizyon); duplicate (B9) | "İşlem açıklamasında hangi isim yazıyor?" · "Kart şu an elinizde mi?" · "Daha önce bu firmadan alışveriş/abonelik oldu mu?" → if it is not recognised, offer to block the card immediately |
| "Kartım ATM'de kaldı" | Card retained by the ATM (B1), with or without a cash or deposit error (D9) | "Hangi ATM, saat kaç?" · "Para çıktı mı, hesaptan düştü mü?" → offer card block and replacement; check the bank's retrieval policy [V] |
| "Müşteri temsilcisine bağlanmak istiyorum" | Request for a human (K1) plus whatever the underlying intent is | "Size hemen bağlıyorum; temsilcinin tekrar sormaması için konuyu tek cümleyle not alabilir miyim?" (warm transfer) |

**Constructed augmentation variants [C]** (for robustness testing only; not observed data):
- Typos and missing diacritics: "kartim atmde kaldi", "sifrem blokeye dustu", "eft gitmedii", "param hesaba gecmedi", "hesabima haciz gelmis".
- Code-switching: "EFT'yi cancel edebilir miyim?", "limit increase istiyorum", "app crash oldu, login olamıyorum", "refund hâlâ yansımadı", "chargeback açmak istiyorum".
- Colloquial and emotional: "param buhar oldu", "bankanız paramı yedi", "rezalet, üçüncü kez arıyorum", "kimse dönüş yapmadı".
- English: "where tf is my money", "card got eaten by the ATM", "pls freeze my card asap".

### Inferences
- Disambiguation should come before resolution for the three umbrella symptoms (D1, D3, C1). A wrong guess, such as calling a garnishment a fraud, is high-risk.
- Turkish evaluation sets need diacritic-free and code-switched variants. Banking intent datasets (Bitext) list code-switching as a tag but do not populate it.

### Gaps
- No verified, representative corpus of Turkish bank call transcripts or chats is public. The Şikayetvar phrasing is written and post-hoc (angrier and longer than live speech).
- Ekşi Sözlük and Reddit were not mined, to save budget.
- EFT/FAST operating windows and limits change. They are not stated here; see team 07.

---

## KQ5. Complaint-handling operations: definitions, lifecycle, escalation, root cause, failure patterns

### Takeaway
Across jurisdictions a complaint is defined broadly: any expression of dissatisfaction, oral or written, justified or not. A **dispute/error** is narrower: a challenge to a specific transaction that triggers statutory timelines. Operationally the regimes converge:
- acknowledge with a reference number;
- record minimum fields;
- investigate fairly;
- answer within a deadline in writing, with reasons and the external escalation route;
- keep the customer updated;
- name an accountable senior owner;
- analyse root causes, including remediation of similar customers who did not complain.

Türkiye's specific features are the **Tüketici İlişkileri Koordinasyon Görevlisi** (deputy-GM-level owner), the TBB/TKBB minimum registration rules (unique reference number, 30-day default), the 20-day card-complaint clock, and the 60-day window to go to the Hakem Heyeti.

### Cited Findings — definitions
- **UK [L].** FCA Glossary: "complaint" = "any oral or written expression of dissatisfaction, whether justified or not, from, or on behalf of, a person about the provision of, or failure to provide, a financial service…, which (a) alleges that the complainant has suffered (or may suffer) financial loss, material distress or material inconvenience; and (b) relates to an activity of that respondent…" — [FCA Handbook Glossary](https://www.handbook.fca.org.uk/handbook/glossary/G197.html).
- **EU [L/guidelines].** "A statement of dissatisfaction addressed to a firm by a natural or legal person relating to the provision of" banking services listed in CRD Annex I, payment services, e-money, credit agreements, etc. — [JC 2018 35 (04/10/2018)](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **TR [IP/association rule, binding on members].** "Başvuru" = written or oral complaints and objections by individual customers about "her türlü sorun, mağduriyet, memnuniyetsizlik" (any problem, grievance or dissatisfaction) met while using individual banking products. "İlk temasta çözümlenen başvuru" (resolved during the call by a call-centre employee) need not be registered under these rules — [TBB/TKBB "Bankalara Yapılan Bireysel Başvurulara İlişkin Usul ve Esaslar" (TKBB board 23/08/2017; effective 02.01.2018)](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
- **US [L] — dispute vs query.** Reg E defines "error" as:
  - an unauthorised EFT;
  - an incorrect EFT;
  - an omission from the statement;
  - a computational error;
  - "receipt of an incorrect amount of money from an electronic terminal";
  - requests for documentation or clarification.

  It explicitly excludes "a routine inquiry about the consumer's account balance", "a request for information for tax or other recordkeeping purposes" and "a request for duplicate copies of documentation". The notice of error may be **oral or written**, within 60 days of the statement. The institution investigates within 10 business days, reports within 3 business days, and corrects within 1 business day; or it takes up to 45 days with **provisional credit** (90 days for POS/foreign/new-account cases) — [12 CFR 1005.11, eCFR as of 2026-09-01](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11).
- **ISO 10002:2018** (Edition 3; published 2018-07; confirmed 2023):
  - Gives guidelines for complaints handling covering a customer-focused environment, top-management commitment and resources, the needs of complainants, "an open, effective and easy-to-use complaints process", analysis and evaluation, auditing, and review.
  - It "does not apply to disputes referred for resolution outside the organization" — [ISO](https://www.iso.org/standard/71580.html).
  - The standard's own definitions and guiding principles could not be accessed: the ISO OBP preview needs terms acceptance.

### Cited Findings — lifecycle by step
- **Acknowledge.**
  - UK [L]: "a prompt written acknowledgement" giving reassurance and the applicable response timelines; then keep the complainant "informed thereafter of the progress" — [DISP 1.6.1R, version from 01/06/2026](https://www.handbook.fca.org.uk/handbook/DISP/1/6.html).
  - TR: banks create "tekil bir kayıt numarası" (a unique reference number) and tell the customer the date of receipt and the number via registered contact details (art. 7) — [TBB/TKBB Usul ve Esaslar](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
  - EU: when acknowledging, firms provide written information on the process (GL 6) — [JC 2018 35](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **Record.**
  - TR minimum fields (art. 8): date received, date registered, reference number, name/TCKN (foreign ID or passport for non-citizens), channel, the staff member who registered it, the customer's preferred reply channel, contact details if none are on file.
  - The rules list exclusions where evaluation is at the bank's discretion: abusive content, non-specific complaints, issues unrelated to the bank, no TCKN/name, commercial or legal-entity matters, third parties without a power of attorney (vekaletname), matters in court, no contact information, first-contact-resolved cases — [TBB/TKBB](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
  - EU GL 3: an internal register, e.g., a secure electronic register — [JC 2018 35](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **Investigate.** UK DISP 1.4.1R: "investigate the complaint competently, diligently and impartially"; assess "fairly, consistently and promptly" the subject matter, whether to uphold, and remedy/redress; explain "in a way that is fair, clear and not misleading"; comply promptly with accepted offers — [DISP 1.4](https://www.handbook.fca.org.uk/handbook/DISP/1/4.html).
- **Respond — deadlines (short; 02/03 cover the law):**
  - **TR.**
    - Default: answer within statutory deadlines, otherwise **at most 30 days**. If technical investigation or audit makes that impossible, the customer must be told before the deadline that a final answer will follow. Bulk replies to similar complaints are banned; each must be answered individually (art. 9) — [TBB/TKBB](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
    - BDDK Decision 5491: the coordinator must ensure reasoned answers "en geç otuz gün içinde" (within 30 days at the latest). Cases needing internal control or audit have no fixed limit, but the customer must be informed — [BDDK 5491](https://www.bddk.org.tr/Mevzuat/DokumanGetir/220).
    - Clocks cited by one bank [BP:İş Bankası]:
      - commercial e-message consent cancellation: 3 business days
      - card cancellation and credit-limit reduction: 7 days
      - card-usage complaints and objections: **20 days** (Law 5464 art. 11)
      - other: 30 days, extendable by 10 days if referred to internal audit
      - Source: [İş Bankası policy](https://www.isbank.com.tr/bankamizi-taniyin/Documents/yatirimci-iliskileri/musteri-geri-bildirim-yonetimi-politikasi.pdf).
  - **UK.** By the end of 8 weeks, either a final response or a written explanation of delay with the FOS referral right. PSD/EMD complaints: 15 business days, or 35 in exceptional cases with a holding response — [DISP 1.6](https://www.handbook.fca.org.uk/handbook/DISP/1/6.html). Complaints resolved by the close of the 3rd business day get a "summary resolution communication" that mentions the FOS — [DISP 1.5.4R](https://www.handbook.fca.org.uk/handbook/DISP/1/5.html).
  - **US.** Reg E clocks above; via the CFPB portal, firms generally respond in 15 days, with a final response in 60 days — [CFPB](https://www.consumerfinance.gov/complaint/process/).
- **Final-response contents.**
  - **TR, written or e-mail answer:** name, reference number, date, (for letters) officer names or department, result. If the result is partly or wholly negative, tell the customer they may apply to the Hakem Heyeti within **60 days** of the bank's answer.
  - **TR, SMS answer:** at minimum the surname or reference number and the result.
  - **TR, phone answer:** recorded, with prior notice to the customer.
  - **TR, follow-up:** the customer may ask once for a further explanatory answer (art. 10).
  - Source: [TBB/TKBB](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
  - **UK [L]:** accept or reject with reasons; include the FOS leaflet and website, the referral right, and the time-limit waiver statement — [DISP 1.6.2R](https://www.handbook.fca.org.uk/handbook/DISP/1/6.html).
  - **EU GL 7:** plain language; explain any delay; give a "thorough explanation" and the routes to ombudsman, ADR or NCAs — [JC 2018 35](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **Escalation tiers (external), TR.**
  - **Bank first.** BDDK says to complain to the bank first "daha hızlı sonuç elde edebilmeniz açısından" (to get a faster result) — [BDDK e-Şikayet](https://ebulten.bddk.org.tr/esikayet/).
  - **TBB Bireysel Müşteri Hakem Heyeti:**
    - the disputed event must be at most 2 years old;
    - the bank has 30 days to respond (20 days for credit cards);
    - free of charge;
    - banks must comply with decisions up to **51,158 TL** (valid from 1 Jan 2026, updated yearly);
    - four committees: cards, consumer loans, insurance, other products;
    - each has 5 members: 2 from BDDK, 3 from banks.
    - Source: [TBB](https://www.tbb.org.tr/faaliyetler/bireysel-musteri-hakem-heyeti).
  - **Applying to the Hakem Heyeti:** within 60 days, in writing or via e-Devlet — [Garanti BBVA](https://www.garantibbva.com.tr/musteri-deneyimi/tbb-bireysel-musteri-hakem-heyeti).
  - **Other routes:** Tüketici Hakem Heyeti and consumer courts; BDDK e-şikâyet/CİMER; TCMB for fees and payment services; TSPB for capital markets — [İş Bankası policy](https://www.isbank.com.tr/bankamizi-taniyin/Documents/yatirimci-iliskileri/musteri-geri-bildirim-yonetimi-politikasi.pdf). Thresholds and procedures belong to team 02.
  - **UK:** FOS. **US:** CFPB and prudential regulators. **EU:** national ADR/NCAs.
- **Ownership and governance.**
  - **TR [L].** BDDK Decision 5491 (22/08/2013; RG 27.08.2013/28748): every bank appoints a **Tüketici İlişkileri Koordinasyon Görevlisi** at deputy-GM level who has no sales or marketing responsibility. The coordinator:
    - sets policy for investigating, concluding, answering, monitoring and reporting complaints;
    - answers BDDK information requests within 15 days;
    - ensures reasoned answers within 30 days;
    - acts on internal-audit findings;
    - remediates bank-wide non-compliance;
    - reports **quarterly** to BDDK and the audit committee: topic distribution, response times, numbers decided for and against customers, process changes, critical audit findings.
    - Source: [BDDK 5491](https://www.bddk.org.tr/Mevzuat/DokumanGetir/220).
  - **UK [L].** A named individual holding a governing function is responsible for oversight of DISP 1 compliance — [DISP 1.3.7R](https://www.handbook.fca.org.uk/handbook/DISP/1/3.html).
  - **EU.** Senior-management-endorsed written complaints management policy (GL 1) and a complaints management function (GL 2) — [JC 2018 35](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **Root-cause analysis and feedback loops.**
  - **UK [L].** DISP 1.3.3R: identify and remedy "recurring or systemic problems" by "analysing the causes of individual complaints so as to identify root causes common to types of complaint", checking whether root causes affect other products, and correcting them.
  - **UK guidance.** DISP 1.3.3B G suggests MI on complaint causes, explicitly *including complaints resolved by the 3rd business day*; prioritisation; reporting to senior personnel; and records of decisions.
  - **UK proactive remediation.** DISP 1.3.6G asks firms to consider redress for customers who were harmed but did not complain.
  - **UK ombudsman feedback.** FOS determinations are fed into training (DISP 1.3.2A).
  - Source: [DISP 1.3](https://www.handbook.fca.org.uk/handbook/DISP/1/3.html). The EU equivalent is GL 5 — [JC 2018 35](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec).
- **Call-centre rules that shape escalation (TR [L])**, RG 20.05.2020/31132 — [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2020/05/20200520-9.htm):
  - reachability ≥95% per year; answer rate ≥95% per month; service level ≥80% per month (≥90% for lost/stolen/suspicious calls);
  - lost/stolen/suspicious transactions first in the menu with priority to an agent;
  - callers 60+ get a direct agent option;
  - card cancellations accepted without redirection;
  - all individual products must be transactable via the call centre, or the customer routed to a suitable channel taking any declared disability into account;
  - monthly quality scoring of 50% correct information or routing and 50% communication (respect, tone, empathy, diction);
  - every caller is offered a rating;
  - **agent talk time cannot be capped**;
  - agents may end abusive calls, subject to sampled review.
- **Warm vs cold transfer [IP].**
  - Warm (attended): the agent briefs the receiving agent before handing over.
  - Cold (blind): the call is routed without context, and the customer often has to repeat everything.
  - Sources: [8x8](https://www.8x8.com/blog/call-transfer-types); [Vonage](https://www.vonage.com/resources/articles/warm-transfer/).
- **Failure patterns with evidence:**
  - Can't reach a human; IVR loops or "ürününüz bulunmamaktadır" — Şikayetvar (KQ4).
  - Inconsistent answers: "Kredi Kartı Kısıtı: Çelişkili Bilgiler" — [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
  - No response from customer service, or live support refusing responsibility — [Şikayetvar EFT](https://www.sikayetvar.com/eft-hesaba-gecmedi).
  - Not told the status of an investigation (7,959 US credit-card complaints); disputes not resolved (14,758) — [CFPB API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Credit%20card).
  - Longer waits to cancel or downgrade; monitoring that relies only on transactional metrics — [FCA](https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement).
  - Banks fined for call-centre service levels (7 in 2025) — [BDDK 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527).
  - 22% of TBB arbitration applications rejected for procedural gaps, which suggests customers are not guided through escalation — [TBB 2024](https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf).

### Inferences — an operating model the AI agent can follow [RP]
1. **Classify on four axes.** Primary intent; `complaint_flag` (dissatisfaction present?); `dispute_flag` (challenges a specific transaction or decision?); urgency P1–P4.
   - Query: wants information, no dissatisfaction. Example: Reg E "routine inquiry about … balance".
   - Service request: asks for an action.
   - Complaint: dissatisfaction, oral or written, justified or not.
   - Dispute/error: a specific transaction or decision challenged (harcama itirazı, ATM shortfall, unauthorised debit). This starts statutory or scheme clocks (US Reg E; TR card objections, 20-day answer) [V for scheme deadlines, team 06].
   - One contact can carry several labels, e.g., "nobody helped me with this unknown charge" = A1 + dispute + complaint.
2. **Complaint signal words [RP, derived from the observed wording]:**
   - TR: "şikayet", "mağdur/mağduriyet", "rezalet", "haksız", "kabul etmiyorum", "itiraz ediyorum", "iade istiyorum", "hâlâ", "defalarca", "kimse dönmedi", "BDDK/CİMER/Hakem Heyeti/Tüketici hakem/avukat/Şikayetvar".
   - EN: "complain", "unacceptable", "still", "again", "nobody called back", "ombudsman", "CFPB", "lawyer".
   - Mentions of a regulator, lawyer or media → high-priority complaint.
3. **Always log, even when resolved in the first contact.** TR association rules do not require registering first-contact resolutions, but UK DISP 1.3.3B G expects MI to cover quick resolutions. For root-cause analysis, record every dissatisfaction with its intent and cause code [RP].
4. **Acknowledge with a reference number and expected timeline** in the same contact. Choose the timeline from the intent: card objection 20 days; other 30 days (TR) [BP/L]. Promise only what the case owner's SLA supports [RP].
5. **Tiers** [IP/RP; verify per bank]:
   - **L0**: bot/self-service.
   - **L1**: contact-centre generalist.
   - **L2**: specialist operations — cards/disputes, payments, fraud 24/7, digital support, collections, credit, legal-holds, KYC.
   - **L3**: complaints/customer-relations unit under the TİKG (TR) or DISP-responsible individual (UK).
   - **L4**: internal audit or inspection for staff-misconduct cases, where BDDK 5491 allows longer handling but requires the customer to be informed.
   - **External**: Hakem Heyeti / THH / BDDK / TCMB / KVKK (TR); FOS (UK); CFPB (US).
6. **Repeat-contact handling.** Look up open cases by customer and reference number before opening a new one. Link duplicates. Raise priority on a second contact about the same issue or past the promised date. Offer the TR "one further explanatory answer" right where relevant [RP/L-TR].
7. **Handoffs are warm by default.** Pass a structured summary: intent, flags, verified identity level, steps already taken, customer's desired outcome. Never make the customer repeat. Never route P1 cases through queues that ignore the TR 20-second lost/stolen standard [RP/L-TR].
8. **One named owner per case** until closure. Callbacks get a time window and are tracked as commitments; a missed callback generates its own complaint flag (K5) [RP].
9. **Close the loop.** Final answer with reasons and escalation rights, then a satisfaction check. Cause codes feed a monthly RCA that includes similar non-complainants (DISP 1.3.6G; BDDK 5491 3(k)) [L-UK/TR].

### Gaps
- FCA DISP 1.9 (record-keeping periods) and DISP 1.10 (reporting) were not fetched.
- Card-scheme chargeback deadlines (Visa/Mastercard/TROY) are not covered here; see team 06.
- Turkish secondary legislation behind the 20-day card clock (Law 5464 art. 11) and the 7-day/3-day clocks is cited only via İş Bankası's table; team 02 should confirm.
- The ISO 10002 principles and definition text were not verified.

---

## KQ6. Turkish banks' published complaint processes

### Takeaway
Major Turkish banks publish complaint processes that closely follow the TBB/TKBB rules: multiple channels, an instant acknowledgement with a reference number, a 30-day default (20 days for card complaints), and signposting to the TBB Hakem Heyeti within 60 days. Some publish internal targets well inside the legal maximum, e.g., İş Bankası's 5 business days.

### Cited Findings
- **İş Bankası "Müşterilerimizden Aldığımız Geri Bildirimleri Yönetim Politikamız"** [BP:İş Bankası; undated PDF, accessed 10 Oct 2026] — [PDF](https://www.isbank.com.tr/bankamizi-taniyin/Documents/yatirimci-iliskileri/musteri-geri-bildirim-yonetimi-politikasi.pdf):
  - **Channels:** website contact form; Çözüm Merkezi 0850 724 0 724; branches; written to head office; musteri.iliskileri@isbank.com.tr; KEP.
  - **Helpful evidence to attach:** receipts and invoices; screenshots and error codes from İşCep/İnternet Şube/Bankamatik; product identifiers.
  - **Acknowledgement:** at a branch, a "Şikâyet Başvurusu Alındı Formu" (one copy for the customer); in other channels, a "Başvuru Alındı Mesajı" by SMS and e-mail to verified contacts. "Başvuru anında bir referans numarası sunulur" (a reference number is given at the time of application) for tracking.
  - **Statutory clocks:** the table in KQ5.
  - **Internal target:** "maksimum 5 iş günü" (at most 5 business days), with an "Ara Bilgilendirme Mesajı" (interim update) if it takes longer.
  - **Reply contents:** as in the TBB/TKBB rule.
  - **Escalation:** TSPB for capital markets, the TBB Hakem Heyeti for other matters, each within 60 days, in writing or via e-Devlet.
  - **Stated aim:** service without the customer needing to contact the bank "ikinci kez" (a second time).
- **Garanti BBVA** [BP:Garanti BBVA] — [page](https://www.garantibbva.com.tr/musteri-deneyimi/tbb-bireysel-musteri-hakem-heyeti):
  - The customer must first apply to the bank in writing.
  - Bank answer times: "kredi kartı ve banka kartlarıyla ilgili şikayetler için 20, diğer bankacılık ürünleri ve hizmetleriyle ilgili şikayetler için 30 gün" (20 days for card complaints, 30 for others).
  - If the bank does not answer or resolve, the customer may go to the Hakem Heyeti within 60 days, in writing or via e-Devlet. The page links the Tebliğ, the brochure and the 2025 application form.
- **VakıfBank Customer Satisfaction Policy** [BP:VakıfBank; undated PDF] — [PDF](https://vbassets.vakifbank.com.tr/investor-relations/policies/customer-satisfaction-policy.pdf):
  - **Channels:** Contact Us, internet and mobile banking, branches, head office, call centre (0850 222 07 24), CİMER, social media.
  - **Principles:** "clarity, accessibility, integrity and sensitivity", plus confidentiality of customer information.
  - Commits to regularly reviewing systems "to improve practices that may cause customer complaints" (an RCA commitment).
  - References an ISO 9001:2015 certificate (not ISO 10002). No response-time commitment is stated.
- **Association rules every member bank must follow** (TBB and TKBB) — [Usul ve Esaslar](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398):
  - Accept complaints via call centre, website/internet branch, branches and head office, and publish the accepted channels on the website.
  - The TİKG monitors the central registration system.
  - Unique reference number; minimum record fields; 30-day default; individual replies.
- **Signposting by the regulator.** BDDK's contact page directs "tutar iadesi içeren" (refund-of-amount) individual banking applications to the arbitration committees — [BDDK İletişim](https://www.bddk.org.tr/iletisim) (search snippet). BDDK's e-Şikayet page asks customers to complain to the bank first — [BDDK e-Şikayet](https://ebulten.bddk.org.tr/esikayet/).
- **Public responsiveness metric (anecdotal).** Ziraat's 96% Şikayetvar response rate in the last year — [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi). Banks treat Şikayetvar as a de facto complaint channel [IP][V].

### Inferences
- The agent's closing script in Türkiye should include: (1) the reference number; (2) the expected answer date, using the intent-specific clock; (3) the reply channel; (4) on refusal, the 60-day Hakem Heyeti route plus other routes as team 02 confirms [RP].
- Because the TBB rejects 22% of applications for procedural gaps, the agent should tell customers what they will need if they escalate: the bank's written answer or the reference/confirmation, a signed form, and a clear statement of what they are asking for [RP].

### Gaps
- Akbank, Yapı Kredi, Ziraat, Halkbank, QNB, DenizBank and Enpara complaint-policy pages were not reviewed.
- **TS ISO 10002 adoption by Turkish banks could not be confirmed.** The bank pages and search results found refer to ISO 9001 (VakıfBank) or only to consultancies.

---

## KQ7. Additional or easily overlooked contact reasons

### Takeaway
Regulator categories, ombudsman product lists and complaint platforms point to many low-frequency but high-impact reasons that a generic banking intent set misses. The Turkish-specific ones include:
- haciz and e-haciz holds;
- salary and pension promotion commitments and restrictions;
- social-benefit payments;
- SIM-change OTP blocks;
- card-fee refunds escalated to consumer arbitration;
- lien release after a loan is paid off;
- restructuring under a new regulation;
- "is this call or SMS really from the bank?" checks.

### Cited Findings
- **Bereavement/estates.** FOS "Executorships or Trusteeships" (30 cases, 2025/26) — [FOS XLSX](https://www.financial-ombudsman.org.uk/files/324759/Annual-complaints-data-2025-26.xlsx). FCA good practice routes bereavement chatbot queries to a human — [FCA](https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement).
- **Third-party authority** (POA/vekaletname). Complaints by third parties without a POA fall outside the standard process in TR — [TBB/TKBB](https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398).
- **Documents and letters.** BDDK category "Kuruluşlardan Bilgi/Belge Talepleri" (3,099 in 2025) — [BDDK 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527). In the US, tax and recordkeeping information requests are explicitly *not* Reg E errors — [eCFR](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11).
- **Travel/abroad usage:** Bitext `activate_card_international_usage`; **courier/card delivery:** B77 `card_arrival`, `card_delivery_estimate` — [Bitext](https://huggingface.co/datasets/bitext/Bitext-retail-banking-llm-chatbot-training-dataset); [BANKING77](https://huggingface.co/datasets/PolyAI/banking77).
- **Outages and digital failures.** ADC = 22% of direct complaints to Turkish banks (2024) — [TBB](https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf).
- **Automation complaints and requests for a human:** Bitext `human_agent`; Gartner 87%; TR rule giving callers 60+ direct access to an agent — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0); [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2020/05/20200520-9.htm).
- **Garnishment/haciz:** BDDK "İcraya İlişkin Sorunlar" 10,926 (2025) — [BDDK 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527).
- **KYC refresh and de-risking:**
  - EBA: de-risking is the third key issue; account closing and denial of access are the top payment-account complaint reasons — [EBA CTR](https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf).
  - CFPB: "Company closed your account" 5,051 (checking) — [CFPB API](https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?date_received_min=2025-01-01&date_received_max=2026-01-01&size=0&product=Checking%20or%20savings%20account).
- **"Is this really you?" scam checks.** Şikayetvar 2025: 40,105 fraud complaints, "dava/icra SMS" 11,368 — [egirisim](https://egirisim.com/2026/02/12/sikayetvar-2025-verilerini-acikladi-dolandiricilik-ve-bahis-siteleri-gundemde/). Bank-impersonation requests for OTP — [Şikayetvar](https://www.sikayetvar.com/banka-hesabi-dolandiriciligi).
- **FX/gold:** Garanti chatbot topics; TKBB "Döviz/Kıymetli Maden" category; Ziraat gold-account complaint — [Garanti BBVA](https://www.garantibbva.com.tr/musteri-deneyimi/tbb-bireysel-musteri-hakem-heyeti); [TKBB 2025](https://tkbb.org.tr/upload/raporlar/018-01.01.2025%20-%2031.12.2025%20YILLIK%20FAAL%C4%B0YET%20RAPORU%20%C4%B0%C3%87%C4%B0N%20TIKLAYINIZ.pdf); [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
- **Loyalty and campaigns:** CFPB rewards problems 1,929; Ziraat "Jest Lira" deductions [SV]. Bank programme names vary (e.g., bonus, puan, chip-para) [V].
- **Salary/pension promotion:** Garanti chatbot "3 yıllık maaş taahhütüm ne zaman doluyor?"; Ziraat "#Promosyon" complaint "Emekli Maaşına Haksız Bloke Ve Transfer Engeli" [SV].
- **Data protection.** KVKK art. 13: the controller decides on a data-subject request "en geç otuz gün içinde" (within 30 days at the latest), free of charge (as summarised on kvkk.gov.tr; verify with 02). A KVKK Board decision (2023/1050) concerns a bank that did not provide the transcript of a call-centre recording to the data subject — [KVKK 2023/1050](https://www.kvkk.gov.tr/Icerik/7769/2023-1050).
- **Accessibility:** BDDK "Engelli Kişilerin Bankacılık İşlemleri" (212 in 2025) and BDDK disability focus groups (2025); call-centre routing that considers declared disability — [BDDK 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527); [Resmî Gazete](https://www.resmigazete.gov.tr/eskiler/2020/05/20200520-9.htm).
- **Others observed** [SV, anecdotal]:
  - social-benefit or rent-aid money not credited or held;
  - lien not lifted after loan payoff;
  - unrequested life-insurance deduction;
  - a payment to an illegal betting site raised under a bank's page ("Pusulabet'te 8.000 TL Kayıp…" under İş Bankası);
  - a youth-account cash advance ("Harçlık Avans");
  - Source: [Şikayetvar EFT](https://www.sikayetvar.com/eft-hesaba-gecmedi); [Şikayetvar Ziraat](https://www.sikayetvar.com/ziraat-bankasi).
- **Commercial/SME** issues inside retail channels: BDDK "Ticari Müşteri" 10,154 (2025); FOS merchant services 774 — [BDDK 2025](https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527); [FOS XLSX](https://www.financial-ombudsman.org.uk/files/324759/Annual-complaints-data-2025-26.xlsx).

### Inferences
- Add these to the taxonomy as explicit intents rather than leaving them in "other": H1, H2, D4, D5, D7, A4, I2, J1–J3, L1–L3, M1, M2, F6, G3, plus E1 with a "SIM change" sub-intent. Many are **sensitive** (bereavement, garnishment, hardship). They need human escalation paths and vulnerability flags (team 11) [RP].
- Promotion-related restrictions and AML-related holds can carry legal constraints on what the agent may say (tipping-off) [V – teams 02/10].

### Gaps
- No frequency data exists for most of these overlooked reasons (bereavement, POA, travel notices, courier, KVKK requests) in Türkiye.
- The bank-specific bereavement (veraset) process and documents are not covered here; team 05/02 should confirm.

---

## Source register

| # | Title | Publisher | URL | Pub./updated date | Jurisdiction | Tier | Used for |
|---|---|---|---|---|---|---|---|
| 1 | Efficient Intent Detection with Dual Sentence Encoders (BANKING77) | Casanueva et al., ACL NLP4ConvAI | https://arxiv.org/abs/2003.04807 | Mar 2020 | Global | Peer-reviewed workshop | Taxonomy |
| 2 | BANKING77 dataset card / repo | Hugging Face / PolyAI | https://huggingface.co/datasets/PolyAI/banking77 ; https://github.com/PolyAI-LDN/task-specific-datasets | accessed 10 Oct 2026 | Global | Dataset | Labels, examples |
| 3 | Label Errors in BANKING77 | Ying & Thomas, ACL Insights workshop | https://aclanthology.org/2022.insights-1.19/ | 2022 | Global | Peer-reviewed workshop | Label-noise caveat |
| 4 | An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction (CLINC150) + domains.json | Larson et al., EMNLP / Clinc | https://aclanthology.org/D19-1131/ ; https://github.com/clinc/oos-eval | 2019 | Global | Peer-reviewed | Taxonomy |
| 5 | Bitext Retail Banking LLM Chatbot Training Dataset | Bitext / HF | https://huggingface.co/datasets/bitext/Bitext-retail-banking-llm-chatbot-training-dataset | © 2024 | Global | Vendor dataset | Taxonomy, language tags |
| 6 | Consumer Complaint Database API (queries listed in KQ2) + API spec | CFPB | https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/ ; https://github.com/cfpb/ccdb5-api | data as of 10 Oct 2026 | US | Regulator data | Frequencies |
| 7 | Consumer Complaint Database (about the data) | CFPB | https://www.consumerfinance.gov/data-research/consumer-complaints/ | accessed 10 Oct 2026 | US | Regulator | Caveats |
| 8 | Learn how the complaint process works | CFPB | https://www.consumerfinance.gov/complaint/process/ | accessed via search extract | US | Regulator | 15/60-day process |
| 9 | Aggregate complaints data: 2025 H2 (+XLSX) | FCA | https://www.fca.org.uk/data/complaints-data/aggregate-complaints-data-2025-h2 | 28 Apr 2026; upd. 15 May 2026 | UK | Regulator data | Frequencies |
| 10 | Annual complaints data and insight 2025/26 (+XLSX) | Financial Ombudsman Service | https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/our-insight/annual-complaints-data-and-insight-2025-26 | 21 May 2026 | UK | Ombudsman data | Frequencies |
| 11 | Consumer Trends Report 2024/25 (EBA/REP/2025/08) + press release | EBA | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | 26 Mar 2025; corr. 22 Apr 2025 | EU | Supervisor | Complaint reasons |
| 12 | Joint Committee Guidelines on complaints-handling (JC 2018 35) | EBA/ESMA | https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec | 4 Oct 2018 | EU | Regulatory guidelines | Definitions, process |
| 13 | FCA Handbook Glossary "complaint" | FCA | https://www.handbook.fca.org.uk/handbook/glossary/G197.html | accessed 10 Oct 2026 | UK | Law/regulation | Definition |
| 14 | DISP 1.3, 1.4, 1.5, 1.6 | FCA | https://www.handbook.fca.org.uk/handbook/DISP/1/3.html (and /4, /5, /6) | 1.6 upd. 1 Jun 2026; 1.5 upd. 1 Apr 2018 | UK | Law/regulation | Process, RCA |
| 15 | Consumer support outcome: good practices and areas for improvement | FCA | https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement | 7 Mar 2025; upd. 10 Jul 2026 | UK | Regulator guidance | Failure patterns |
| 16 | ISO 10002:2018 standard page | ISO | https://www.iso.org/standard/71580.html | 2018-07; confirmed 2023 | Global | Standard (abstract only) | Scope/aspects |
| 17 | 12 CFR 1005.11 (Reg E) | eCFR / CFPB | https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11 | version 2026-09-01 | US | Law/regulation | Dispute vs query |
| 18 | BDDK Yıllık Faaliyet Raporu 2025 (sec. 9) | BDDK | https://www.bddk.org.tr/KurumHakkinda/EkGetir/5?ekId=527 | 2026 (by late May) | TR | Regulator | Frequencies, fines |
| 19 | Kurul Kararı 5491 – TİKG Usul ve Esaslar | BDDK | https://www.bddk.org.tr/Mevzuat/DokumanGetir/220 | 22 Aug 2013 (RG 27 Aug 2013) | TR | Law/regulation | Ownership, 30 days, reporting |
| 20 | Banka Çağrı Merkezlerinin Hizmet Seviyesinin ve Kalitesinin Belirlenmesine İlişkin Yönetmelik | Resmî Gazete (BDDK) | https://www.resmigazete.gov.tr/eskiler/2020/05/20200520-9.htm | 20 May 2020 | TR | Law/regulation | Routing, SLAs |
| 21 | BDDK E-Şikayet / İletişim | BDDK | https://ebulten.bddk.org.tr/esikayet/ ; https://www.bddk.org.tr/iletisim | accessed 10 Oct 2026 | TR | Regulator | Escalation ladder |
| 22 | Bireysel Müşteri Hakem Heyeti page | TBB | https://www.tbb.org.tr/faaliyetler/bireysel-musteri-hakem-heyeti | threshold valid from 1 Jan 2026 | TR | Banking association | Escalation rules |
| 23 | Bireysel Müşteri Hakem Heyeti 2024 Faaliyet Raporu | TBB | https://www.tbb.org.tr/sites/default/files/docs/bireysel-musteri-hakem-heyeti-yillik-faaliyet-raporu-2024.pdf | May 2025 | TR | Banking association | Direct-to-bank complaint mix |
| 24 | Bireysel Müşteri Hakem Heyeti Yıllık Faaliyet Raporu 2025 | TKBB | https://tkbb.org.tr/upload/raporlar/018-01.01.2025%20-%2031.12.2025%20YILLIK%20FAAL%C4%B0YET%20RAPORU%20%C4%B0%C3%87%C4%B0N%20TIKLAYINIZ.pdf | Feb 2026 | TR | Banking association | Participation-bank complaints |
| 25 | Bankalara Yapılan Bireysel Başvurulara İlişkin Usul ve Esaslar | TBB & TKBB | https://tkbb.org.tr/mevzuat/birligimiz-duzenlemeleri-details/1398 | adopted 23 Aug 2017; eff. 2 Jan 2018 | TR | Association rule (binding on members) | Registration, timelines |
| 26 | Tüketici Hakem Heyetleri 2025 yılında 907 bini aşkın başvuruyu… | Ticaret Bakanlığı | https://ticaret.gov.tr/haberler/tuketici-hakem-heyetleri-2025-yilinda-907-bini-askin-basvuruyu-karara-baglayarak-12-4-milyar-tllik-uyusmazligi-yargiya-tasimadan-cozume-kavusturdu | 21 Jan 2026 | TR | Ministry | Banking share, card fee |
| 27 | TCMB Şikayet Yönetim Sistemi; Bilgi Edinme; DUY2026-04 | TCMB | https://esikayet.tcmb.gov.tr/mbnesspfe-kullanici/ ; https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/bottom+menu/diger/bilgiedinme ; https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2026/DUY2026-04 | 2026 | TR | Central bank | Scope; no stats |
| 28 | Müşteri Geri Bildirim Yönetimi Politikası | Türkiye İş Bankası | https://www.isbank.com.tr/bankamizi-taniyin/Documents/yatirimci-iliskileri/musteri-geri-bildirim-yonetimi-politikasi.pdf | undated (accessed 10 Oct 2026) | TR | Bank policy | Process exemplar |
| 29 | TBB Bireysel Müşteri Hakem Heyeti (bank page, incl. chatbot menu) | Garanti BBVA | https://www.garantibbva.com.tr/musteri-deneyimi/tbb-bireysel-musteri-hakem-heyeti | undated (accessed 10 Oct 2026) | TR | Bank policy | 20/30/60 days; top intents |
| 30 | Customer Satisfaction Policy | VakıfBank | https://vbassets.vakifbank.com.tr/investor-relations/policies/customer-satisfaction-policy.pdf | undated | TR | Bank policy | Channels, principles |
| 31 | Provizyon Nedir? | Halkbank | https://www.halkbank.com.tr/tr/blog/provizyon-nedir | undated | TR | Bank help content | Symptom mapping |
| 32 | Şikayetvar topic/brand pages (EFT, Ziraat, ATM, SMS, human agent, fees, credit, fraud) | Şikayetvar | URLs inline in KQ2/KQ4 | accessed 10 Oct 2026 | TR | Forum (anecdotal) | Wording, signals |
| 33 | Şikayetvar 2025 verilerini açıkladı | egirisim (specialist press) | https://egirisim.com/2026/02/12/sikayetvar-2025-verilerini-acikladi-dolandiricilik-ve-bahis-siteleri-gundemde/ | 12 Feb 2026 | TR | Press citing platform | Anecdotal volumes |
| 34 | 2026 U.S. Retail Banking Satisfaction Study (press release) | J.D. Power | https://www.jdpower.com/business/press-releases/2026-us-retail-banking-satisfaction-study | 26 Mar 2026; upd. 20 Jun 2026 | US | Industry | Satisfaction, problem resolution |
| 35 | Gartner survey: 87% … must provide access to a human agent | Gartner | https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0 | 4 Aug 2026 | Global | Industry | Human access, GenAI |
| 36 | Gartner survey: only 14% resolved in self-service | Gartner | https://www.gartner.com/en/newsroom/press-releases/2024-08-19-gartner-survey-finds-only-14-percent-of-customer-service-issues-are-fully-resolved-in-self-service | 19 Aug 2024 (via search extract) | Global | Industry | Self-service limits |
| 37 | Capacity and demand management (failure demand) | The Open University (OpenLearn) | https://www.open.edu/openlearn/society-politics-law/criminology/capacity-and-demand-management/content-section-12 | undated | UK/Global | Educational | Definition |
| 38 | Call transfer types / Warm transfer | 8x8; Vonage | https://www.8x8.com/blog/call-transfer-types ; https://www.vonage.com/resources/articles/warm-transfer/ | undated | Global | Vendor training material | Warm/cold definitions |
| 39 | KVKK Board decision 2023/1050 (bank call-recording transcript) | KVKK | https://www.kvkk.gov.tr/Icerik/7769/2023-1050 | 15 Jun 2023 | TR | Regulator decision (title only) | Overlooked intent |
| 40 | Banka blokesi nasıl kaldırılır (law-firm blog) | FFK Partner Hukuk | https://www.ffkpartnerhukuk.com.tr/banka-blokesi-nasil-kaldirilir-hesaba-konulan-bloke-icin-adim-adim-rehber-2026/ | 2026 | TR | Lower-tier commentary | Hold causes (verify) |

---

## Open questions, unverified items, and items needing institution-specific confirmation
1. **FCA headline discrepancy.** The FCA text says total complaints fell "0.4%" from 2025 H1 to H2, but its XLSX implies −4.8%. Use the XLSX figures.
2. **BDDK channel split.** The 8,207 and 2,553 channel counts are petition vs call centre, but which is which is unconfirmed from the PDF text.
3. **Newer reports not yet available.** The TBB 2025 Hakem Heyeti/direct-complaint report was not published as of 10 Oct 2026. The EBA CTR is biennial (next likely 2027). No TCMB complaint statistics were found.
4. **Statutory basis of TR clocks** (20-day card complaints under Law 5464 art. 11; 7-day card cancellation and limit decrease; 3-business-day e-message opt-out; +10-day audit extension). These are cited through İş Bankası's policy table and need confirmation by team 02.
5. **Tüketici Hakem Heyeti monetary thresholds for 2026 and card-fee case law** (aidat refunds) were not verified here; team 02 should confirm.
6. **Chargeback/"ters ibraz" scheme deadlines** and bank-specific dispute forms: team 06.
7. **Haciz/e-haciz handling.** What L1 may disclose (authority, file number), protected-salary rules, and **AML tipping-off limits** for holds: teams 02 and 10, plus the institution's legal-holds procedure.
8. **Bank-specific processes to verify against internal procedure:**
   - retained-card retrieval vs destruction;
   - SIM-change OTP block removal channels;
   - promotion-commitment restrictions on transferring a pension or salary;
   - bereavement document checklists;
   - POA acceptance rules;
   - Şikayetvar response ownership.
9. **ISO 10002:2018.** The definition of "complaint" and the guiding principles could not be accessed (OBP terms wall). Whether any Turkish bank holds TS ISO 10002 certification is unconfirmed.
10. **Contact (not complaint) driver shares** for Turkish banks (e.g., % of calls that are "where is my money") are not publicly available. Measure them from the agent's own tagged traffic.
11. **Şikayetvar titles** appear normalised by the platform. Treat them as indicative of topics, and the body excerpts as closer to customer wording.
12. **Gartner 2024 figures (14%/36%)** and the CFPB process page were read via search extracts; re-check against the pages before external publication.
13. **Not reviewed:** McKinsey, Deloitte and Accenture retail-banking contact-driver material; UK and US bank complaint pages; Ekşi Sözlük and Reddit.
