# 01 — Banking fundamentals, products, concepts, terminology and internal team responsibilities (general/international, with Turkish equivalents)

Researcher 01 · research date 2026-10-10 · primary jurisdiction Türkiye (TR); comparisons with EU, UK, US.

**How to read the tags.** Each finding carries `[jurisdiction · type · source date]`. Types: **L** = law/regulation (category 1); **P** = common industry practice (2); **B** = individual bank policy, bank named (3); **R** = recommended service practice (4); **V** = assumption / needs verification (5). "INT" = not jurisdiction-specific. **[periodic]** marks figures that change over time (rates, limits, thresholds, hours) and must be re-checked before use.

**Method note.** Primary Turkish legal texts were downloaded from mevzuat.gov.tr and read directly: Banking Law 5411, Card Law 5464, AML Law 5549, Payment Services Law 6493, Consumer Protection Law 6502, Code of Obligations 6098, Enforcement and Bankruptcy Law 2004. Regulator and central-bank pages were scraped or fetched: TMSF, FSCS/PRA, FDIC, European Parliament, CPMI, FCA, CFPB, and EU texts on legislation.gov.uk/EUR-Lex. Bank help pages were used for practice. Weaker sources (aggregators, press, law-firm blogs) are labelled. Forum material (Şikayetvar) is used only for customer wording and marked "anecdotal".

**Safety rule that applies throughout.** Nothing in these notes asks a customer for a PIN, full password, CVV/CVC, one-time/SMS code, or remote access to a device. A support agent (human or AI) must never request these, and must treat a customer who says "the bank asked me for my code" as a possible fraud victim (route to fraud operations, researcher 10).

---

## 1. What banks do, and how bank types differ (retail, SME/commercial, corporate, investment, private, digital-only/neobank)

### Takeaway
Banks (i) take deposits, (ii) lend and (iii) run payments. The **licence**, not the brand or app, decides what an institution may legally do and whether customer money is deposit-insured. Turkish law recognises three bank types: deposit banks, participation banks, and development & investment banks (which take no deposits). Digital-only banks have had their own BDDK licence category since 2022. "Neobank" is a marketing label, not a licence.

### Cited Findings
- [INT · P · IMF F&D "Back to Basics", compiled 2017] Banks' "primary role is to take in funds—called deposits—from those with money, pool them, and lend them to those who need funds". They perform **maturity transformation** ("converting short-term liabilities (deposits) to long-term assets (loans)") and are "essential to the domestic and international payments system". They earn mainly the spread between deposit and loan rates, plus fees (checking accounts, loan servicing, sale of insurance and mutual funds). Deposits can be "available on demand (a checking account, for example) or with some restrictions (such as savings and time deposits)". The article lists investment banks with finance companies and money-market funds as "shadow banks" not regulated like banks. — [IMF](https://www.imf.org/external/pubs/ft/fandd/basics/pdf/gobat-banks.pdf)
- [TR · L · Banking Law 5411 Art. 3, consolidated text] Definitions:
  - *Mevduat bankası*: mainly accepts deposits in its own name and extends credit.
  - *Katılım bankası*: collects funds through special current accounts and participation accounts, and extends credit.
  - *Kalkınma ve yatırım bankası*: extends credit and/or performs special-law duties **without** accepting deposits or participation funds.
  - *Kredi kuruluşu*: deposit banks plus participation banks.
  - *Mevduat*: money accepted "istendiğinde ya da belli bir vadede geri ödenmek üzere" (repayable on demand or at a fixed maturity).
  - *Tasarruf mevduatı*: deposit accounts of real persons that are not used for commercial transactions other than writing cheques.
  — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
- [TR · L/press · regulation in force 01.01.2022 (date from a press-based search summary; verify against the Official Gazette)] BDDK's "Dijital Bankaların Faaliyet Esasları ile Servis Modeli Bankacılığı Hakkında Yönetmelik" took effect on 01.01.2022. In April 2023 the press reported more than 35 applications to set up digital banks. — [Para Dergi, 13.04.2023](https://www.paradergi.com.tr/finans/2023/04/13/dijital-banka-kurmak-icin-basvuru-sayisi-35i-asti) It allows branchless banks that serve only through digital channels. The press reported Hayat Finans Katılım Bankası as the first licensed digital bank, and reported approvals for TOM Katılım Bankası, Adil Katılım Bankası and Colendi Bank (a digital deposit bank). Approval dates were not verified. — [Capital](https://www.capital.com.tr/haberler/tum-haberler/turkiyenin-ilk-dijital-bankasi-hayat-finans-oldu); [Ekonomist](https://www.ekonomist.com.tr/haberler/bddk-tom-katilim-bankasinin-kurulusunu-onayladi-pozitif-varlik-yonetime-izin-verdi-34010); [Diken](https://www.diken.com.tr/?p=1432356)
- [EU (ES) · L/P · Banco de España, 03.12.2020] Banco de España describes neobanks as technology-intensive firms that offer services "exclusively online, mainly through a mobile app". A neobank may be one of three things:
  1. A credit institution, whose deposits "are protected by a deposit guarantee scheme".
  2. An e-money or payment institution. These "are not affiliated to a deposit guarantee scheme" but "must deposit their customers' money in special accounts in banks or invest these funds in safe assets".
  3. An unauthorised entity.

  Only credit institutions may use the word "bank", so "it is important to know who the legal person behind a brand is." — [Banco de España](https://clientebancario.bde.es/pcb/en/blog/neobanco-que-son-y-que-ofrecen.html)
- [UK · P · trade press] E-money fintechs safeguard customer funds but are not FSCS-protected. The FCA has pressed such firms to make their non-bank status clear to customers. This is a trade-press report and the primary FCA document was not retrieved. — [FinTech Futures](https://www.fintechfutures.com/bankingtech/fca-demands-uk-fintechs-clarify-non-bank-status-to-customers)

### Inferences
- **Segment model (P; verify per bank).**

  | Segment | Who it serves | Typical products | Typical channels |
  |---|---|---|---|
  | Retail | Individuals | Mass-market products | Digital and contact centre |
  | SME / commercial (KOBİ, esnaf) | Small firms and tradespeople | Business accounts, POS, commercial loans, cheques | Branch or portfolio managers |
  | Corporate | Large firms | Cash management, trade finance, treasury, FX | Dedicated relationship managers (RMs) |
  | Private banking | High-net-worth individuals | Investment products through licensed staff or affiliates | RM-led |
  | Investment banking | Issuers and capital markets | Capital markets, M&A advisory | Normally outside retail support |

  The segment decides the channel, the fee schedule, the service-level agreements (SLAs) and the escalation route. The agent should therefore identify the segment before answering "can I do X?".
- **Licence, not brand.** When a customer names an app or brand, the operative question is which licensed entity holds the money: a bank, a participation bank, or an e-money/payment institution. Deposit insurance, interest or profit-share, lending ability and complaint routes all follow the licence.

### Gaps
- No dated, authoritative BDDK list of operating digital banks as of October 2026 was retrieved. Verify against BDDK's institution list.
- Segment thresholds (SME turnover bands, private-banking asset minimums) are bank-specific and not published in comparable form.

---

## 2. Payment institutions and e-money institutions (ödeme kuruluşu, elektronik para kuruluşu) compared with banks

### Takeaway
In Türkiye, payment institutions (PIs) and e-money institutions (EMIs) are licensed and supervised by **TCMB** under Law 6493.
- **They can:** hold payment accounts and issue e-money.
- **They cannot:** accept deposits, lend, or (EMIs) pay interest.
- **How customer money is protected:** through **safeguarding** in separate bank accounts, not TMSF deposit insurance.

Banks can also issue e-money and provide payment services.

### Cited Findings
- [TR · L · Law 6493 Arts. 3(b) and 18] In Law 6493, "Banka" means TCMB (Art. 3(b)). Law 7192 (12.11.2019) changed licensing and supervisory references from BDDK ("Kurul/Kurum") to TCMB ("Banka"). Under Art. 18(1), only three kinds of entity may issue e-money: banks operating under Law 5411, PTT, and EMIs licensed by TCMB. — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
- [TR · L · 6493 Art. 14(2)(d), (3), (4)]
  - A payment institution may hold a payment account **only if it is used solely for payment transactions**.
  - Funds that PIs and EMIs receive for payment services **are not deposits or participation funds** (Banking Law Art. 60), and are not e-money.
  - "Ödeme kuruluşu kredi verme faaliyetinde bulunamaz" (cannot extend credit). TCMB decides by regulation whether payment-related activities count as lending.
  - Licensing requires the institution to set up complaint and objection units ("şikâyet ve itirazlarla ilgili birimleri oluşturması").
  — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
- [TR · L · 6493 Art. 20] An EMI:
  - issues e-money equal to the funds it receives and makes it usable "gecikmeksizin" (without delay);
  - must transfer collected funds to a **separate account at a bank** (amended by Law 7192);
  - **may not lend**;
  - "elektronik para hamiline faiz veremez ve herhangi bir menfaat sağlayamaz" (may not pay interest or any benefit tied to holding time);
  - its e-money funds are **not deposits/participation funds**.
  — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
- [TR · L · 6493 Art. 22] PI and EMI funds are protected under TCMB rules. If the institution is liquidated or its licence is cancelled, the funds are used to compensate fund owners "başka kanunlarda belirtilen önceliklere bakılmaksızın" (regardless of priorities in other laws). — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
- [TR · case · 27.05.2025] Papara Elektronik Para A.Ş.:
  - TMSF was appointed trustee (kayyum) during a criminal investigation.
  - TCMB said user funds are held in "koruma hesapları" at banks under Art. 22, and temporary daily payment limits were applied.
  - Later web reports say TCMB cancelled Papara's e-money issuance authorisation on 31.10.2025. This was not verified against a TCMB primary notice.
  — [Forbes Türkiye](https://www.forbes.com.tr/haberler/tcmb-den-papara-aciklamasi-iceride-parasi-olanlara-ne-olacak); [Alomaliye (copy of TCMB press release)](https://www.alomaliye.com/2025/05/27/papara-elektronik-para-a-s-hakkinda-basin-duyurusu/)
- [EU (ES) · L/P · 2020] EMIs and PIs are outside deposit guarantee schemes. They safeguard customer money in special bank accounts or safe assets. — [Banco de España](https://clientebancario.bde.es/pcb/en/blog/neobanco-que-son-y-que-ofrecen.html)
- **Discrepancy noted.** An AI-generated search summary claimed that BDDK supervises Turkish PIs/EMIs. The primary law text shows TCMB has been the authority since the 2019 amendment. Rely on the law. — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)

### Inferences
- **E-money is not insured as a deposit.** E-money balances (wallets, EMI-issued prepaid cards) are not deposits. TMSF deposit cover therefore does not apply; protection comes from safeguarding and the Art. 22 priority. This is inferred from 6493 Art. 20(7) and TMSF's scope, which is limited to credit institutions.
  - Draft agent wording (to be checked by Legal): "Bu tutar mevduat değil elektronik paradır; TMSF mevduat sigortası kapsamında değildir, kanun gereği bankalardaki koruma hesaplarında tutulur."
- **Customer vocabulary.** Customers often call EMI wallets "hesap" or even "banka". The agent should not correct them pedantically, but must not imply bank-level protections or interest.
- **Lending refusals.** "Wallet credit" or "kredi verir misiniz" requests to a PI/EMI brand should be answered from the licence: such firms cannot lend under 6493. Any credit product shown in their app is provided by a partner bank or financing company, so the agent should say which entity provides it.

### Gaps
- TCMB's 2021 secondary regulation on payment services and e-money was not reviewed. It covers safeguarding mechanics, wallet limits and identity-verification tiers (researcher 02).
- The EU/UK rules that allow PIs limited credit linked to payments (PSD2 Art. 18(4)) were not verified here (researcher 03).
- Papara's final status (licence cancellation, refund process) needs confirmation from TCMB/TMSF primary notices.

---

## 3. Participation (Islamic) banks in Türkiye — product language

### Takeaway
Participation banks fund themselves through two account types:
- **özel cari hesap**: no return, withdrawable at any time;
- **katılma hesabı**: profit-and-loss sharing, no pre-set return, principal not guaranteed.

They lend through trade, leasing or partnership ("finansman"), and pay or charge **kâr payı** rather than "faiz". The agent must not use "faiz", "mevduat" or "garantili getiri" for these products.

### Cited Findings
- [TR · L · 5411 Art. 3]
  - *Özel cari hesap*: can be withdrawn partly or fully at any time; "karşılığında hesap sahibine herhangi bir getiri ödenmeyen" (no return paid).
  - *Katılma hesabı*: gives participation in the profit or loss from using the funds; "önceden belirlenmiş herhangi bir getiri ödenmeyen ve anaparanın aynen geri ödenmesi garanti edilmeyen" (no predetermined return; repayment of principal not guaranteed).
  - *Katılım fonu*: the money held in özel cari and katılma accounts.
  — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
- [TR · P · TKBB brochure, undated; its figures pre-date 2019]
  - Funds are collected on profit-and-loss sharing.
  - Funds are used through trade (*murabaha*: the bank buys the asset for cash and sells it to the customer on deferred terms, paying the seller against an invoice), leasing and partnership.
  - There is no cash-loan system, except qard hasan and tawarruq in exceptional cases.
  - Profit share "vade sonunda belli olur" (is known only at maturity). It is distributed daily from TL/USD/EUR pools.
  - Products are approved by advisory boards (danışma kurulları).
  - The brochure's "100.000 TL" TMSF figure is outdated; the 2026 limit is 1,200,000 TL (§4).
  — [TKBB](https://tkbbegitim.org.tr/Documents/Yonetmelikler/TKBB-Katilim-Bankaciligi-Nedir-Brosur.pdf)
- [TR · L · 5464 Art. 26] In the Card Law, for participation banks "faiz" applies as **kâr payı** and default interest ("gecikme faizi") applies as **gecikme cezası**. — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · Council of Ministers Decision 2006/11188, RG 22.11.2006/26354, amended 01.01.2013] Withdrawing from a katılma hesabı before maturity returns the amount deposited, or the unit account value if it shows a loss. In effect, the profit share is forfeited. Summary via Lexpera; check the verbatim text before quoting. — [Lexpera](https://www.lexpera.com.tr/mevzuat/bakanlar-kurulu-kararlari/mevduat-ve-kredi-faiz-oranlari-ve-katilma-hesaplari-kar-ve-zarara-katilma-oranlari-ile-ozel-cari)
- [TR · B · Kuveyt Türk, updated 17.08.2026] Profit share on a katılma hesabı is subject to withholding tax (stopaj) by maturity and currency, not to BSMV. BSMV applies to the bank's own profit share and fees on financing (consumer financing 15%). — [Kuveyt Türk](https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir)
- [TR · L/B · Albaraka Türk TMSF page] TMSF cover for katılma hesapları is calculated on unit account values. Profit shares accrued above the average profit-share rate of the three largest participation banks (by funds), at the date the licence is revoked, are not covered. — [Albaraka Türk](https://www.albaraka.com.tr/tr/bireysel/hesaplar/tmsf-guvencesi)

### Inferences
- **Vocabulary map for agents** (P; verify against each bank's product names):

  | Conventional term | Participation-bank term |
  |---|---|
  | faiz | kâr payı |
  | kredi | finansman (bireysel / konut / taşıt finansmanı) |
  | mevduat | katılım fonu |
  | vadeli hesap | katılma hesabı |
  | vadesiz hesap | özel cari hesap |
  | gecikme faizi | gecikme cezası |
  | kredi faiz oranı | kâr oranı (financing) |
  | mevduat faiz oranı | kâr payı oranı (deposit side) |

  Cards are still called kredi kartı / banka kartı.
- **No guaranteed returns.** The agent must never promise a return on a katılma hesabı. Quote past or indicative profit-share rates only as published by the bank, labelled as non-guaranteed.
- **Financing is tied to an asset.** Financing is linked to an asset or invoice (murabaha), so a request for "nakit kredi" may not map one-to-one to a participation product. Check the bank's catalogue.

### Gaps
- Current TKBB / Central Advisory Board standards (for example, how late-payment penalties are used) were not reviewed.
- Bank-specific katılma-hesabı products and their partial-withdrawal rules were not catalogued.

---

## 4. Deposit insurance basics and current limits (TMSF; EU DGS; UK FSCS; US FDIC)

### Takeaway
Limits as of October 2026 [periodic]:

| Jurisdiction | Limit | Basis |
|---|---|---|
| TR (TMSF) | **1,200,000 TL** | per person, per credit institution; reset each calendar year |
| EU (DGS) | **€100,000** | per depositor, per bank |
| UK (FSCS) | **£120,000** (since 1 Dec 2025) | per eligible person, per authorised firm |
| US (FDIC) | **$250,000** | per depositor, per insured bank, per ownership category |

Generally outside these schemes: investment products, crypto, e-money, and accounts at foreign branches or offshore units.

### Cited Findings
- **TR [L · TMSF FAQ, accessed 2026-10-10] [periodic]**
  - **Limit history (TL):**

    | Period | Limit |
    |---|---|
    | 15.02.2013–25.09.2019 | 100,000 |
    | 25.09.2019–31.12.2021 | 150,000 |
    | 2022 | 200,000 |
    | 2023 | 400,000 |
    | 2024 | 650,000 |
    | 2025 | 950,000 |
    | 2026 | **1,200,000** |

    The Fon Kurulu raises the limit each calendar year, taking the previous year's revaluation rate (yeniden değerleme oranı) into account.
  - **Scope:** deposits at the *domestic* branches of credit institutions, denominated in TL, FX or **precious metals** (principal plus accrued interest), and participation funds (katılma unit values plus özel cari balances). Deposits of official institutions, credit institutions and financial institutions are excluded. Commercial deposits are covered (tasarruf, ticari kuruluşlar and diğer kuruluşlar mevduatı).
  - **Not covered:**
    - accounts at overseas branches of Turkish banks;
    - institutions doing only offshore banking;
    - deposits of controlling or qualifying shareholders, board members and senior managers, and their close family;
    - criminal proceeds (TCK 282);
    - government bonds, T-bills, investment funds and crypto assets sold through banks.
  - **How cover is computed:**
    - per person, per credit institution, adding up all branches; each bank is counted separately;
    - a deposit bank and a participation bank are counted separately;
    - a person's own account and their sole-proprietorship business account count as two persons;
    - joint accounts are split per holder (equal shares if not specified);
    - minors' accounts are covered separately from the parent's;
    - non-residents' accounts at domestic branches are covered;
    - free-zone branches are covered.
  - **Payout:**
    - only if BDDK revokes the licence (there is no payout while a bank is operating);
    - paid in TL: FX converted at TCMB's buying rate; precious metals at the Istanbul gold-exchange closing price times the TCMB rate;
    - within **3 months**, extendable by 3 months;
    - the uninsured excess ranks as a privileged claim in bankruptcy (third rank under İİK 206), after TMSF and public receivables.
  - **Disclosure:** banks must display the TMSF notice in branches and in digital channels.
  — [TMSF](https://www.tmsf.org.tr/tr/Tmsf/Finansman/mevduat.sss.guncel); the 2026 increase (950,000 → 1,200,000, effective 1 January 2026) is confirmed by [Anadolu Ajansı](https://www.aa.com.tr/tr/ekonomi/tmsf-sigortaya-tabi-mevduat-ve-katilim-fon-tutarini-yukseltti/3770056)
  - The legal basis for covering commercial deposits is Banking Law Art. 63(1) as amended on 26.05.2022 by Law 7407: "…resmi kuruluşlar, kredi kuruluşları ve finansal kuruluşlara ait olanlar haricindeki tüm mevduat ve katılım fonları… sigorta edilir". — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
- **EU [L · EBA; European Parliament 26.03.2026]**
  - Coverage is harmonised at €100,000 per depositor per bank. — [EBA](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/depositor-protection/deposit-guarantee-schemes-data)
  - The **CMDI reform** (BRRD/SRMR/DGSD) was adopted by Parliament on 26.03.2026. It:
    - keeps €100,000;
    - protects certain deposits linked to real-estate transactions at "€500,000 up to €2,500,000";
    - gives the DGS top priority in insolvency, with retail depositors and SMEs in the second tier.

    It enters into force on the twentieth day after publication in the Official Journal and applies, with exceptions, from 24 months after entry into force. A law-firm note reports OJ publication on 20.04.2026; this was not checked on EUR-Lex. — [European Parliament](https://www.europarl.europa.eu/news/en/press-room/20260323IPR38827/new-rules-to-address-bank-failures-protecting-taxpayers-and-depositors); [Lexology](https://www.lexology.com/library/detail.aspx?g=94d43f9c-4c63-43d2-ba59-07c2adfffb39)
- **UK [L · PRA PS24/25, Nov 2025; FSCS]** The FSCS deposit limit rose from £85,000 (set in 2017) to **£120,000 from 1 December 2025**. The PRA had consulted on £110,000 and settled higher. The limit applies per eligible person, per UK-authorised firm, and joint accounts get £120,000 per eligible person. — [FSCS](https://www.fscs.org.uk/what-we-cover/); [Bank of England PS24/25](https://www.bankofengland.co.uk/prudential-regulation/publication/2025/november/depositor-protection-policy-statement); [FSCS press release](https://www.fscs.org.uk/media/press/2025/nov/fscs-welcomes-higher-deposit-protection-limit-of-120000--giving-people-confidence-their-money-is-protected/)
- **US [L · FDIC page updated 01.04.2024]** Cover is "$250,000 per depositor, per FDIC-insured bank, for each account ownership category". Categories include single, joint, IRA, trust, employee-benefit and government accounts.
  - Covered: checking, savings, money-market deposit accounts, CDs and cashier's checks.
  - **Not covered:** stocks, bonds, mutual funds, annuities, life insurance, safe-deposit contents, US Treasuries, municipal securities and crypto.
  — [FDIC](https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance)

### Inferences
- **Agent script (R).**
  - State the limit as "per person, per bank".
  - Say that the TR figure changes every year.
  - Point to TMSF's own page.
  - Never comment on a particular bank's soundness, and never steer money to products to "stay insured" (that would be advice).
- **Brand vs licence.** The TR limit applies per credit institution. Two brands run under one banking licence therefore share one limit. This is inferred from "her bir kredi kuruluşunda"; verify for digital brands of parent banks.
- **Typical customer phrasings:**
  - "Bankada 2 milyon param var, batarsa ne olur?"
  - "TMSF güvencesi ne kadar, eşimle ortak hesabımız var?" → split per holder.
  - "Altın hesabım da sigortalı mı?" → yes: precious-metal deposits are in scope, paid out in TL.
  - "Fonlarım / hisselerim / kriptom TMSF kapsamında mı?" → no.

### Gaps
- The UK temporary-high-balance limit after PS24/25 was not captured.
- The EU DGSD repayment deadline (7 working days) was not re-verified here.
- Whether TMSF treats a bank's separately branded digital unit as part of the same institution should be confirmed with TMSF or the bank's legal team.

---

## 5. Customer-facing channels — what each can do, and why some actions still need a branch, a wet signature or an in-person ID check

### Takeaway
Most servicing has moved to mobile/internet banking and contact centres.
- Türkiye has allowed fully remote, video-based onboarding since **2021**.
- Distance consumer-credit contracts have been explicitly valid since **October 2024**.

Some actions still require a branch:
- legal form rules (e.g., a guarantor's handwriting);
- original documents (court/enforcement letters, inheritance, power of attorney, guardianship);
- physical items (cash, cheques, safe deposit boxes);
- fraud and vulnerability risk.

Messaging channels such as WhatsApp are usually **information-only**.

### Cited Findings
- [TR · L · BDDK regulation, RG 01.04.2021 No. 31441, in force 01.05.2021] "Bankalarca Kullanılacak Uzaktan Kimlik Tespiti Yöntemlerine ve Elektronik Ortamda Sözleşme İlişkisinin Kurulmasına İlişkin Yönetmelik":
  - allows remote identification;
  - allows contracts concluded through an information or communication device in place of written form, under conditions;
  - makes the bank responsible for minimising the risk of misidentifying the person.
  — [Erdem & Erdem](https://www.erdem-erdem.av.tr/bilgi-bankasi/bankalarca-kullanilacak-uzaktan-kimlik-tespiti-yontemlerine-ve-elektronik-ortamda-sozlesme-iliskisinin-kurulmasina-iliskin-yonetmelik-yayimlandi)

  The press describes the video-call model and a later BDDK move to let registered legal entities onboard remotely; that article is undated. — [Ekonomist](https://www.ekonomist.com.tr/haberler/bddkdan-yeni-karar-tuzel-kisiler-de-uzaktan-kimlik-tespiti-yoluyla-banka-musterisi-olabilecek-34536)
- [TR · L · Law 6502 Art. 22(3), amended 24.10.2024 by Law 7529] Consumer-credit contracts are valid if made "yazılı **veya mesafeli**" (in writing or at a distance). — [Law 6502](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6502.pdf)
- [TR · L · Code of Obligations 6098 Arts. 583–584]
  - A guarantee (kefalet) is valid only in writing, stating the maximum amount and the date.
  - The guarantor must write **in their own handwriting**:
    - the maximum amount;
    - the date;
    - for a joint-and-several guarantee, that capacity.
  - A married guarantor needs the spouse's written consent, given before or at signing. There are exceptions for business-related guarantees.
  — [TBK](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6098.pdf)
- [TR · L · Card Law 5464 Art. 8] Card issuers must:
  - keep the system for notifications, requests, complaints and objections "kesintisiz olarak açık" (continuously open);
  - keep PINs and codes secret;
  - mask card numbers on receipts and in correspondence;
  - hand cards only to the cardholder (a minor's supplementary card is delivered to the main cardholder).

  This is why card-blocking lines run 24/7. — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · B · Garanti BBVA, page undated] Garanti BBVA's WhatsApp line (+90 444 0 333, verified business account):
  - gives bot-based information on 200+ topics, 7/24;
  - does **not** process transactions;
  - comes with the bank's warning not to share passwords or personal information on WhatsApp.
  — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/garanti-bbva-whatsapp)
- [TR · B · Yapı Kredi] Yapı Kredi's WhatsApp line (0850 222 0 444) connects customers to an AI chatbot or to customer representatives for information and requests. — [Yapı Kredi](https://www.yapikredi.com.tr/yapi-kredi-hakkinda/haberler/detay/134685)
- [EU · L · Payment Accounts Directive (PAD) Art. 17] Even a basic payment account must allow cash withdrawals "at the counter or at automated teller machines during or outside the credit institution's opening hours". — [legislation.gov.uk (Directive 2014/92/EU)](https://www.legislation.gov.uk/eudr/2014/92/article/17)
- [TR · V · press, March 2026] Several Turkish outlets report that selected branches (malls, airports, tourist areas) began opening on Saturdays from 09:00 to 13:00, citing parliamentary approval. No law number and no BDDK or TBB primary source was found. **Treat as unverified.** — [hisse.net](https://www.hisse.net/haber/bankalar-cumartesi-gunleri-acik-olacak-tbmm-onayladi-iste-yeni-calisma-saati-duzenlemesi-63727); [Karar](https://www.karar.com/guncel-haberler/bankalar-cumartesi-gunu-calisacak-mi-2026-banka-calisma-saatleri-ve-2034997)

### Inferences — channel capability matrix (P; verify per bank)

| Channel | Typically possible | Typically restricted / not possible | Main reason |
|---|---|---|---|
| Mobile app / internet banking | Balances, history, statements; havale/EFT/FAST; SWIFT at many banks; bill payments; card controls (temporary block, e-commerce/abroad toggles, limits); virtual cards; FX/gold buy-sell; time deposits; funds; loan/card applications; document download; contact-detail updates under strong authentication | High-risk first-time actions may be held or limited; some products (minors, guardianship, some loans) need a branch | Strong customer authentication and fraud controls |
| Contact centre (IVR + human/AI agent) | 24/7 card blocking; information after caller authentication; dispute and complaint intake; guided digital help; some product changes | Changing phone number/e-mail, adding beneficiaries, lifting legal or AML blocks, approving credit | Weaker identity assurance by phone; legal/compliance ownership elsewhere |
| Branch | Cash; cheques; safe deposit; original-document processes (inheritance/veraset, power of attorney/vekaletname, guardianship/vasi, court or enforcement letters); guarantor signatures; KYC refresh when remote is impossible; complex cases | — | Legal form rules, originals, in-person identity and vulnerability checks |
| ATM / ITM | Cash withdrawal and deposit (QR / card-less at some banks); transfers; bill payments; PIN change | Complex servicing | Physical cash handling |
| Video banking (görüntülü görüşme) | Remote onboarding (TR since 2021); some servicing | Varies by bank | Regulated remote ID |
| Messaging (WhatsApp, in-app chat) | Information, guidance, application status, hand-off to a human | Transactions usually not allowed; never share passwords or OTPs | Channel security |
| Relationship / portfolio manager | SME, corporate and private clients: pricing, credit, trade, investments | — | Segment model |
| Social media | Acknowledge and redirect to a private channel | No account details in public | Bank secrecy (Banking Law Art. 73, §15) |

- **Security rule (R, all channels).** Never ask for or accept:
  - a PIN;
  - a full internet-banking password;
  - a CVV/CVC;
  - an OTP / SMS approval code;
  - remote access or screen sharing.

  If a customer reports "bank staff" asking for these, route to fraud operations.
- **Why "please visit a branch" happens (P/V).** The five reason classes are:
  1. legal form (a guarantor's handwriting; some notarised documents);
  2. original documents (inheritance, power of attorney, court or enforcement letters);
  3. identity or vulnerability checks after fraud flags;
  4. physical instruments (cash, cheques, safe deposit boxes);
  5. product rules (minors, guardianship).

  The agent should name the reason class without blaming the customer. Where the bank supports it, offer a remote alternative such as video onboarding or e-Devlet documents; verify per bank.

### Gaps
- Bank-by-bank capability lists are not public in comparable form, e.g., which banks allow a phone-number change only in a branch. Verify against the institution's internal procedure.
- The technical details of Turkish remote ID were not verified (NFC chip reading of the ID card, liveness checks, first-transaction limits) (researcher 08).

---
## 6. How the back end works: systems, real-time vs batch, business days, cut-off times, value date vs booking date

### Takeaway
A bank runs several linked systems: the core banking ledger, the card processor, the payment hub, the general ledger, a fraud engine, AML screening, and CRM/case management. Some things happen in real time: card authorisations, FAST/instant payments and most digital postings. Other things run in cycles and only on business days: clearing and settlement, interest, fees and the accounting close (end-of-day/batch). This split explains most "timing" complaints:
- "pending" items;
- weekend EFTs that arrive on Monday;
- statements that differ from the live balance;
- value dates that differ from transaction dates.

### Cited Findings
- [INT · P · industry/encyclopaedic] A core banking system is the back-office platform that opens and maintains accounts, processes deposits and withdrawals, calculates interest, manages loans and maintains (or feeds) the general ledger. Ledgers use double-entry bookkeeping. Modern cores post in real time but still run end-of-day batches for interest accrual, fees and the accounting close. These are vendor and encyclopaedic sources, so treat this as a descriptive model. — [Wikipedia: Core banking](https://en.wikipedia.org/wiki/Core_banking); [SDK.finance](https://sdk.finance/blog/what-is-a-ledger-in-banking-and-fintech-a-complete-guide/); [Spark glossary](https://www.spark.money/glossary/core-banking-system)
- [INT · P · card-industry documentation, 2026] The card transaction lifecycle has three stages:
  1. **Authorisation.** The issuer checks the card, available funds and fraud risk in real time and places a hold. At this stage "no money has moved yet".
  2. **Clearing.** The acquirer submits the final transaction, typically in end-of-day batch files.
  3. **Settlement.** Funds move between banks.

  Holds that are never captured usually drop off in about 1–5 business days, or up to about 30 days for hotels and car rentals. "Authorization success does not equal guaranteed settlement." — [Adyen docs](https://docs.adyen.com/issuing/payment-stages/authorisation-holds.md); [Increase docs](https://www.increase.com/documentation/card-payment-lifecycle); [PaymentExpert, 02.03.2026](https://paymentexpert.com/2026/03/02/the-payment-lifecycle-explained/)
- [INT · standard · BIS CPMI glossary] **Value date**: "The day on which the payment, transfer instruction or other obligation is due and the associated funds and securities are typically available to the receiving participant." — [BIS CPMI](https://www.bis.org/committees/cpmi/glossary?selection=71)
- [EU · L · PSD2 Art. 78] Time of receipt is when the payer's payment service provider (PSP) receives the order. An order received on a non-business day is deemed received on the next business day. A PSP may set a cut-off time near the end of a business day; orders received after it are "deemed to have been received on the following business day". — [PSD2 Art. 78](https://www.legislation.gov.uk/eudr/2015/2366/article/78)
- [EU · L · PSD2 Art. 83(1)] After receipt, the amount must reach the payee's PSP "by the end of the following business day". Paper-initiated orders may take one more business day. — [PSD2 Art. 83](https://www.legislation.gov.uk/eudr/2015/2366/article/83)
- [EU · L · PSD2 Art. 87] Value-date rules:
  - The credit value date is no later than the business day on which the payee's PSP is credited.
  - Funds must be available immediately when there is no currency conversion, or only conversion between EU currencies.
  - The debit value date is no earlier than the time the account is actually debited.
  — [PSD2 Art. 87](https://www.legislation.gov.uk/eudr/2015/2366/article/87)
- [TR · P/press · August 2026] [periodic] FAST, the TCMB instant-payment system:
  - runs 24/7;
  - its per-transaction limit rose from 100,000 TL to **300,000 TL on 26 August 2026**;
  - the "Ödeme İste" (request-to-pay) limit also rose from 100,000 to 300,000 TL;
  - the limit for FAST-TR Karekod merchant payments with dynamic verification rose from 250,000 to 300,000 TL.

  Transfers above the FAST limit go through EFT. EFT runs only on business days within system hours, and EFT orders given at weekends or on holidays are executed on the next business day. — [Webrazzi, 24.08.2026](https://webrazzi.com/2026/08/24/fast-islem-limiti-300-bin-tlye-yukseliyor/); [Bloomberg HT](https://www.bloomberght.com/tcmb-fast-islem-limitini-artirdi-3786250). EFT hours come only from secondary aggregators (e.g., [Enuygun](https://www.enuygunfinans.com/finans-rehberi/eft-saatleri-bankalarda-eft-saat-kaca-kadar-yapilir/)), so verify exact system and bank cut-off hours.
- [US · L/P] FedNow went live on 20 July 2023. It runs 24x7x365 alongside FedACH (next-day and same-day *batch* ACH) and Fedwire. — [Federal Reserve](https://www.federalreserve.gov/paymentsystems/FedNow_about.htm); [FRB Services](https://frbservices.org/news/fed360/issues/080123/fednow-service-instant-payments)
- [EU · L · Instant Payments Regulation (EU) 2024/886] Deadlines for euro-area PSPs:
  - be able to *receive* SEPA instant credit transfers by 9 January 2025;
  - be able to *send* them by 9 October 2025;
  - offer **Verification of Payee** for all credit transfers by 9 October 2025;
  - charge no more for instant transfers than for regular ones.
  — [Bird & Bird](https://www.twobirds.com/en/insights/2024/global/instant-payments-regulation)

### Inferences — system map and how it explains confusion (P; verify per bank)

| System | What it does | What the customer sees | Usual owner |
|---|---|---|---|
| Core banking system (CBS) | Accounts, ledger balances, interest, fees, loans, standing orders | Ledger balance; interest/fee postings after end of day | IT + operations |
| Card management system / card processor (in-house or outsourced) | Card records, limits, real-time authorisations, holds, credit-card statements | "Provizyonda" items; available limit ≠ statement debt | Card operations |
| Payment hub / gateways (EFT, FAST, SWIFT, SEPA) | Routing, cut-offs, repair/return queues, investigations | "Sent but not received", returns, recall requests | Payment operations |
| General ledger (GL) | Accounting of all postings | Rarely visible | Finance |
| Fraud engine | Real-time scoring, step-up checks, holds/blocks | Declines, "güvenlik blokesi", verification calls/SMS | Fraud operations |
| AML / sanctions screening | Name screening, transaction monitoring | Payment held "for review", document requests | Compliance |
| CRM / case management | Contact history, complaints, cases, SLAs | Case/ticket numbers, callbacks | Contact centre, complaints |
| Digital channel platform | App/web, authentication, notifications | Login/OTP/notification problems | Digital channels / IT |

- **Four dates the agent must keep apart:**
  - *İşlem tarihi* (transaction date): when the customer acted.
  - *Valör* (value date): when interest starts or stops counting and funds are due.
  - *Kayıt / hesaba yansıma tarihi* (booking/posting date): when it hit the ledger.
  - *Ekstre / hesap özeti dönemi* (statement period): which statement it falls in.
- **Weekend transfer logic (TR).** Up to the FAST limit, the transfer arrives within seconds at any time. Above the limit, or via EFT, it is queued to the next business day. A SWIFT payment also depends on correspondent banks' business days and time zones.
- **Pending vs posted.** An authorisation hold is a promise, not a debit. The final amount can differ (fuel, hotel, tips, FX). A posted refund or reversal follows the merchant's and the issuer's processing.

### Gaps
- Bank-specific cut-off times (EFT; SWIFT per currency) and end-of-day times are not published uniformly. Verify against the institution's internal procedure.
- No primary TCMB statement of current EFT operating hours was retrieved (researcher 07).

---

## 7. Account types and customer-relevant features

### Takeaway
The core Turkish retail accounts are:
- **vadesiz**: demand account;
- **vadeli**: time deposit; early withdrawal normally earns only the demand rate;
- **DTH**: FX deposit account;
- **altın hesabı**: gold account;
- **KMH**: overdraft attached to a demand account;
- **joint accounts**: teselsüllü vs teselsülsüz;
- **minors' accounts**;
- **salary/pension accounts**, often with promotions.

KKM (FX-protected deposits) has closed. The EU, unlike Türkiye, has a statutory right to a basic payment account.

### Cited Findings
- [INT · P · IMF] Deposits can be on demand (checking) or restricted (savings, time). — [IMF](https://www.imf.org/external/pubs/ft/fandd/basics/pdf/gobat-banks.pdf)
- [TR · L · Council of Ministers Decision 2006/11188 (RG 22.11.2006; amended 01.01.2013)] A time deposit withdrawn before maturity **with the bank's consent** earns the **demand-deposit rate** ("vadesiz mevduat faiz oranı uygulanır"). The Decision also contains special partial-withdrawal rules for accounts of one year or longer and for accumulation accounts; confirm the exact text before quoting. — [Lexpera](https://www.lexpera.com.tr/mevzuat/bakanlar-kurulu-kararlari/mevduat-ve-kredi-faiz-oranlari-ve-katilma-hesaplari-kar-ve-zarara-katilma-oranlari-ile-ozel-cari)
- [TR · L · tax, via EY Vergi Rehberi 2026 (as of 14.01.2026)] [periodic] Withholding tax (stopaj) on interest:

  | Income | Rate | Basis |
  |---|---|---|
  | TL deposit interest, demand and ≤6 months | **17.5%** | Accounts opened/renewed from 09.07.2025 (Presidential Decision 10041) |
  | TL deposit interest, ≤1 year | **15%** | Same |
  | TL deposit interest, >1 year | **10%** | Same |
  | FX-deposit (DTH) interest | **25%** | Since 28.06.2023 (Decision 7332) |
  | Participation-account profit shares | Same as TL deposits | — |
  | Repo income | 15% | 2026 |

  Deposit interest already taxed by withholding does not need to be declared by individuals.

  Press in October 2026 still quotes 17.5% for deposits of up to 6 months. — [EY Vergi Rehberi 2026](https://www.ey.com/content/dam/ey-unified-site/ey-com/tr-tr/services/tax/documents/2026/ey-tr-vergi-rehberi-2026.pdf); [Kırşehir Çiğdem (press)](https://www.kirsehircigdem.com/mevduat-faizi-ne-kadar-oldu-500-bin-1-milyon-ve-2-milyon-tl-ne-kadar-kazandiriyor)
- [TR · L · TMSF] FX and precious-metal deposits are within TMSF scope (1.2m TL per person per bank, paid out in TL). — [TMSF](https://www.tmsf.org.tr/tr/Tmsf/Finansman/mevduat.sss.guncel)
- [TR · B · Kuveyt Türk, 17.08.2026] Buying FX or book-entry precious metals bears **0.2% BSMV** on the sale amount. Since 17.03.2025, sales of book-entry gold without physical delivery are treated as FX (kambiyo) transactions at the same rate. — [Kuveyt Türk](https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir)
- [TR · P · secondary] KMH ("ek hesap", "artı para") lets the customer overdraw a demand account up to a limit. Interest accrues daily on the amount used and is charged monthly. Rate ceilings are tied to TCMB-announced maximums [periodic; verify current rate]. — [HesapKurdu](https://www.hesapkurdu.com/ihtiyac-kredisi/rehber/kredili-mevduat-hesabi-kmh-nedir); [Habertürk](https://www.haberturk.com/kmh-faizi-nedir-kmh-faizi-nasil-hesaplanir-2741095)
- [TR · L · Law 6502 Art. 26(2)] For open-ended credit agreements (KMH is typically one), a rate increase must be notified on paper or another durable medium **30 days** in advance. A customer who repays fully and stops using the credit within 60 days of the notice is not affected by the increase. — [Law 6502](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6502.pdf)
- [TR · B · İş Bankası, 27.12.2024; Akbank] Joint accounts come in two types:
  - **Müşterek (teselsülsüz)**: all holders must act together.
  - **Münferit / teselsüllü**: any holder can transact alone. ATM use requires a teselsüllü account.
  — [İş Bankası](https://www.isbank.com.tr/blog/ortak-hesap-nedir); [Akbank](https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay)
- [TR · L · TMSF] Joint accounts are insured per holder, in equal shares unless specified otherwise. Minors' accounts opened by a parent or guardian are covered separately from the parent's own accounts. — [TMSF](https://www.tmsf.org.tr/tr/Tmsf/Finansman/mevduat.sss.guncel)
- [TR · L · Banking Law 5411 Art. 62] Deposits, participation funds, items held in safekeeping and receivables that go unclaimed for **10 years** after the last request, transaction or written instruction become time-barred. If the bank cannot reach the holder, it publishes an announcement and then credits the money to TMSF as revenue. — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
- [TR · B · Ziraat Bankası, pension-promotion undertaking form] Ziraat pays the pension promotion upfront for a **3-year commitment** that starts on the payment date. If the pension is moved elsewhere early, the remaining part is refunded pro rata (kıst-ı yevm). Enforcement (haciz) and alimony (nafaka) deductions are mentioned. — [Ziraat](https://www.ziraatbank.com.tr/tr/Forms/emekli_promosyon_taahhutname__39C78.pdf)
- [TR · L (TCMB), via press, 24.01.2026] KKM status:
  - New openings and renewals ended on 23.08.2025, except YUVAM accounts.
  - The legal basis (Communiqués 2021/14 and 2021/16) was repealed by Communiqués 2026/1 and 2026/2 in January 2026.
  - Gold-conversion accounts ("FATSİ") continue until their existing maturities.
  — [CNN Türk](https://www.cnnturk.com/ekonomi/kkm-donemi-resmen-sona-erdi-2388577)
- [EU · L · PAD 2014/92 Arts. 16–17] Consumers legally resident in the EU have a right to open a payment account with basic features. This includes consumers with no fixed address, asylum seekers, and people who cannot be expelled for legal or factual reasons.
  - Services that must be included: opening, operating and closing the account; placing funds; cash withdrawals; direct debits; card payments including online; credit transfers and standing orders.
  - An overdraft may be offered only at the consumer's request, and access to the account "shall not be… conditional on the purchase of such credit services".
  — [PAD Art. 17](https://www.legislation.gov.uk/eudr/2014/92/article/17); [EUR-Lex summary](https://eur-lex.europa.eu/summary/EN/090406_1)

### Inferences
- **"Vadeli hesabımı bozarsam faizim yanar mı?"** As a rule, yes: the customer gets the demand rate, which is usually close to nothing. The agent should read the exact effect from the product terms and the bank's system rather than estimate it. A participation account early-withdrawal forfeits the profit share (§3).
- **Salary credit and KMH.** A salary credited to a demand account with a KMH balance will typically clear the overdraft first: "maaşım yattı ama param yok". This is P; verify the bank's netting rule.
- **"Tasarruf hesabı" ≠ "tasarruf mevduatı".** In everyday speech, *tasarruf hesabı* means a savings account. Legally, *tasarruf mevduatı* means any real-person deposit, demand or time.
- **KKM questions in 2026 are legacy matters** (matured accounts, tax certificates, conversion history). There is no new product to offer.
- **Salary promotions.** Promotions depend on the employer–bank protocol or the pension campaign. Never quote an amount or refund calculation without the actual protocol or form.
- **Dormant accounts.** "Eski hesabımda param vardı" → check the 10-year time-bar status (Art. 62) through operations before answering.

### Gaps
- Minimum ages and permissions for minors' accounts and cards vary by bank and were not verified (researcher 05).
- Not verified: DTH cash ("efektif") withdrawal notice periods and fees, and whether a TCMB-allowed cash-FX commission currently applies. A 2020 commission was reportedly withdrawn. — [Habertürk](https://www.haberturk.com/nakit-doviz-cekiminden-alinan-komisyon-kaldirildi-2782038-ekonomi)
- The status of YUVAM accounts and FATSİ maturities in October 2026 was not checked.
- Türkiye has no statutory equivalent of the EU basic payment account in the sources reviewed.

---

## 8. Card types (conceptual; card operations belong to researcher 06)

### Takeaway
The main card types work as follows:
- **Debit card (banka kartı):** spends the customer's own money from a deposit or özel cari account.
- **Credit card (kredi kartı):** spends a credit line that runs on a statement cycle (statement → due date → minimum or full payment).
- **Prepaid card (ön ödemeli kart):** holds e-money.
- **Virtual card (sanal kart):** a card number without plastic. Turkish law treats it as a credit card where it gives access to a credit line.
- **Supplementary card (ek kart):** draws on the main cardholder's account or limit.

Card schemes (Visa, Mastercard, Amex, Troy) set network rules, including dispute (chargeback) rights.

### Cited Findings
- [TR · L · Card Law 5464 Art. 3] Definitions:
  - **Banka kartı**: a card giving access to banking services, including deposit or özel cari accounts.
  - **Kredi kartı**: "basılı kartı veya fizikî varlığı bulunmayan kart numarasını" (a printed card or a card number without physical form) for buying goods and services or withdrawing cash without using cash.
  - The law also defines the card issuer, the merchant acquirer, the merchant (üye işyeri), *dönem borcu*, *asgarî tutar*, *son ödeme tarihi*, and the **alacak belgesi** (a credit document the merchant issues for returns, cancellations or abandoned services).
  — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · 5464 Art. 8]
  - No card may be issued without the customer's request and a contract.
  - Issuers must provide records of completed transactions on request, within at most 30 days (60 days for foreign transactions).
  - If the minimum payment is unpaid for three months after the due date and is still unpaid one month after notice, the issuer cancels the credit cards, and no new card is issued until the debt is fully paid.
  — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · 5464 Art. 12] If a card or its details are lost or stolen, the holder is liable only up to "yüzelli Yeni Türk Lirası" (150 TL) for unlawful use in the **24 hours before notifying** the bank. The cap does not apply in cases of gross negligence, intent, or failure to notify. Issuers must insure this exposure on request. The 150 TL figure is the nominal amount in the law text; check whether secondary rules have changed its effect (researcher 06/10). — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · 5464 Art. 26] [periodic]
  - The minimum payment is at least **20%** of the statement balance. The Board may raise it to 40% and set different rates for different cardholder groups.
  - Card debts, including defaulted ones, attract **no compound interest**.
  - **TCMB sets maximum contractual and default interest rates** (amended by Law 7222 in 2020).
  - There must be **at least 10 days** between the statement date and the due date.
  - Fees, commissions or costs that are not in the contract cannot be charged.
  — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · P/press] **Troy** is Türkiye's domestic card scheme, launched by BKM (Bankalararası Kart Merkezi) in April 2016. Some Troy cards are accepted abroad through the Discover Global Network partnership. — [Electronic Payments International](https://www.electronicpaymentsinternational.com/?p=46712); [CNBC-e](https://www.cnbce.com/fintech/troy-nedir-neden-kuruldu-sahibi-kim-troyun-pazar-payi-ne-h8585)
- [TR · B · İş Bankası, 08.08.2024] Chargeback (ters ibraz / harcama itirazı):
  - The cardholder first tries to resolve the issue with the merchant, then applies to the bank.
  - The usual window is **120 days** from the relevant date (purchase date, promised delivery date, etc.), or up to **540 days** in special cases allowed by the card schemes.
  - The process can take up to about **180 days**.
  — [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir)
- [TR · L · 5464 Art. 11] Cardholders may object to credit-card transactions within **10 days of the due date**. A statement not objected to in time becomes final, but the cardholder keeps the right to go to court. Issuers must answer complaints and objections **within 20 days**, using the channel the cardholder used. — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)

### Inferences
- **Two dispute clocks.** The statutory 10-day statement objection (5464 Art. 11) and the scheme chargeback windows (e.g., 120 days) are different clocks. Agents should log disputes immediately and not tell customers they are "too late" without checking scheme rules (researcher 06).
- **Supplementary cards.** An ek kart normally shares the main card's limit, and the primary cardholder is liable under the contract. Law 5464 Art. 8 requires a minor's supplementary card to be delivered to the primary cardholder. This is P; verify contract terms per bank.
- **Prepaid cards.** Prepaid cards issued by EMIs are e-money products: no interest, not deposits, and not TMSF-insured (inferred from Law 6493). Bank-issued prepaid cards are also e-money (6493 Art. 18).
- **Debit vs credit timing.** Debit-card purchases reduce the deposit balance (hold, then posting). Credit-card purchases reduce the available limit and appear on the next statement after the cut-off.

### Gaps
- Scheme rules (Visa/Mastercard reason codes, time limits, liability shifts) belong to researcher 06.
- Card annual-fee rules, such as whether issuers must offer a fee-free card, were not verified (researchers 02/09).

---

## 9. Payment concepts (conceptual; mechanics belong to researcher 07)

### Takeaway
Classify a payment in two ways:
- **By rail:**
  - same-bank *havale*;
  - interbank *EFT* (business days only);
  - *FAST* (instant, 24/7, up to a limit);
  - *SWIFT* (cross-border via correspondent banks);
  - *SEPA* (euro area, now instant-capable);
  - ACH / FedNow (US).
- **By who starts recurring payments:**
  - the customer (standing order / düzenli ödeme talimatı);
  - the payee under a mandate (direct debit);
  - the merchant using stored card details (recurring card payment / CPA).

The initiator decides who can cancel and which protections apply.

### Cited Findings
- [TR · P/press] **Havale** is a transfer within the same bank (instant). **EFT** is an interbank transfer through TCMB's EFT system on business days, within system hours. **FAST** is an interbank instant transfer, 24/7, up to the per-transaction limit (300,000 TL since 26.08.2026 [periodic]). — [Webrazzi](https://webrazzi.com/2026/08/24/fast-islem-limiti-300-bin-tlye-yukseliyor/); [HesapKurdu FAST guide](https://www.hesapkurdu.com/uzaktan-musteri-edinimi/rehber/fast-limiti-nedir)
- [TR · L/P] A Turkish **IBAN** has **26 characters**: "TR" + 2 check digits + a 5-digit bank code + 1 reserve digit (always "0") + a 16-character account number. TCMB sets the bank codes (TCMB IBAN Communiqué, 2008). — [Yapı Kredi](https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/iban-nedir-nasil-ogrenilir); [Halkbank copy of TCMB IBAN Tebliği](https://www.halkbank.com.tr/content/dam/halkbank/tr/dokumanlar/bireysel/iban_tebligi.pdf)
- [INT · standard] A **BIC** (ISO 9362, the "SWIFT code") has 8 or 11 characters: a 4-character institution code, a 2-letter country code, a 2-character location code, and an optional 3-character branch code ("XXX" for the head office). — [Wikipedia: ISO 9362](https://en.wikipedia.org/wiki/ISO_9362); [Stripe](https://stripe.com/en-cn/resources/more/swift-code-and-bic)
- [INT · P · fintech help page] SWIFT charge options:
  - **OUR**: the sender pays all fees.
  - **SHA**: fees are shared; this is the default on many platforms.
  - **BEN**: the beneficiary pays.

  Intermediary (correspondent) banks may deduct "lifting" fees along the way. This is a weak source; confirm with the bank's tariff. — [Qonto help](https://support-es.qonto.com/hc/en-us/articles/23951014100753)
- [EU · L] SEPA Instant is mandatory for euro-area PSPs, together with Verification of Payee and price parity with regular transfers (§6). — [Bird & Bird](https://www.twobirds.com/en/insights/2024/global/instant-payments-regulation)
- [UK · B/scheme]
  - **Standing order:** set up and controlled by the payer; fixed amount; the payer "can amend or cancel… as and when you like".
  - **Direct Debit:** "can only be set up by the organisation" under the payer's mandate. The Direct Debit Guarantee promises advance notice of changes to amount, date or frequency ("normally 10 working days"), a "full and immediate refund" for errors, and that the payer can cancel "at any time by simply contacting your bank".
  - **Continuous Payment Authority (CPA):** lets a business take regular, fixed or varying, payments from a debit or credit card; "the payment instruction is with the business, not with a bank".
  — [Barclays](https://barclays.co.uk/help/payments/payment-information/difference-order-debits); [Direct Debit Guarantee (Bacs)](https://www.directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/)
- [UK · P · consumer organisation] For recurring card payments, the card provider must cancel them if the customer asks, and must refund payments taken after the cancellation. — [Which?](https://www.which.co.uk/money/banking/banking-security-and-payment-methods/direct-debits-and-standing-orders-explained-aU1tE5d00CI5)
- [US · L/P] In the US, ACH is a batch system (FedACH next-day/same-day) and FedNow is instant, 24x7x365 (§6). — [Federal Reserve](https://www.federalreserve.gov/paymentsystems/FedNow_about.htm)

### Inferences
- **Turkish equivalents (P/V):**
  - *Düzenli ödeme / havale-EFT talimatı*: a standing order; the customer controls it and cancels it at the bank.
  - *Otomatik (fatura) ödeme talimatı*: the customer authorises the bank to pay a biller's invoices as they arrive, in variable amounts. In effect it resembles a direct debit, but the instruction is held at the bank; it is cancelled at the bank and/or the biller.
  - *Kredi kartına tanımlı abonelik / düzenli kart ödemesi*: a merchant-initiated recurring card payment (CPA-like). The customer cancels with the merchant; the issuer may block the merchant or open a dispute, according to bank policy.

  Turkish revocation and refund rights for these payments were **not verified** (TCMB 2021 payment-services regulation; researchers 02/07).
- **Triage for "gönderdim ama gelmedi":**
  1. Which rail was used (FAST / EFT / SWIFT)?
  2. When was the order given, compared with the cut-off and business days?
  3. Was the amount above the FAST limit (so routed to EFT)?
  4. Was there a name/IBAN mismatch (return)?
  5. Is it held at the receiving bank or in an AML/fraud review?
  6. For SWIFT: correspondent delays and charge option.

  Customers should get the dekont (receipt) or reference, not a guess.

### Gaps
- Turkish legal rules on revoking recurring payments and on refunds for payee-initiated transactions were not verified (researchers 02/07).
- Official EFT system hours and bank cut-offs were not verified from a primary source.

---
## 10. Lending concepts

### Takeaway
Turkish consumer credit is governed by Law 6502 and the Tüketici Kredisi Sözleşmeleri Yönetmeliği. The main rules are:
- the rate is fixed for fixed-term loans;
- the customer has a 14-day right of withdrawal (cayma);
- early repayment earns a discount on interest;
- the whole debt can be called in only after two consecutive missed instalments plus a 30-day notice;
- the **yıllık maliyet oranı** (annual cost rate, also called *efektif yıllık faiz oranı*) must be disclosed. Like the US APR, it includes fees and taxes, not just interest.

Interest on consumer loans carries **15% BSMV + 15% KKDF** [periodic]. Credit-bureau data flows through TBB's Risk Merkezi and KKB, and the KKB/Findeks score runs from 1 to 1900.

### Cited Findings
- [TR · L · Law 6502 Arts. 22–28]
  - **Art. 22:** A credit-card contract that defers payment for more than 3 months, or allows instalments, against interest counts as a consumer credit. The contract must be written or distance ("mesafeli", added 24.10.2024).
  - **Art. 23:** A pre-contract information form must be given a reasonable time before signing.
  - **Art. 24:** The customer may withdraw within **14 days** without reason or penalty. Principal plus accrued contractual interest must be repaid within 30 days of the withdrawal notice.
  - **Art. 25:** The rate on fixed-term consumer credit is **fixed** and cannot be changed against the consumer. If the contract omits the contractual rate, the effective annual rate or the total cost, the credit is interest-free.
  - **Art. 27:** On early repayment of one or more instalments or the whole debt, the lender must discount interest and other cost elements.
  - **Art. 28:** The lender may call in the whole debt (acceleration) only if it reserved that right, the consumer has missed **at least two consecutive instalments**, and the lender gave **at least 30 days'** notice.
  — [Law 6502](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6502.pdf)
- [TR · L · Tüketici Kredisi Sözleşmeleri Yönetmeliği, RG 22.05.2015/29363, last amended 31.12.2024, Art. 4(1)] Definitions:
  - **Efektif yıllık faiz oranı** = "Kredinin toplam maliyetinin yıllık yüzde değeri olarak hesaplanması sonucu ortaya çıkan yıllık maliyet oranı".
  - **Kredinin toplam maliyeti** = contractual interest, taxes, duties and similar legal charges, and any fees under other names, excluding notary costs.
  - **Akdi faiz oranı** = the rate used to build the repayment plan.
  — [Lexpera](https://www.lexpera.com.tr/mevzuat/yonetmelikler/tuketici-kredisi-sozlesmeleri-yonetmeligi/3)
- [US · P/regulator education · CFPB, reviewed 28.08.2026] The interest rate is "the cost you pay to the lender for borrowing money". The APR is "the interest rate plus any additional fees charged by the lender", such as origination charges. — [CFPB](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/)
- [TR · L · 5464 Art. 26] Card debts carry no compound interest, and TCMB sets maximum contractual and default rates (§8). — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · B · taxes on loans, 2026] [periodic]
  - Kuveyt Türk's 2026 table shows **BSMV 15%** on consumer financing used after 7 July 2023, and **5%** on commercial financing and service commissions. — [Kuveyt Türk](https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir)
  - Industry calculators apply **KKDF 15%** to consumer-loan interest. — [HesapKurdu KKDF](https://www.hesapkurdu.com/ihtiyac-kredisi/rehber/kaynak-kullanimi-destekleme-fonu-nedir)
  - **Conflict:** Yapı Kredi's worked example (05.03.2026) labels BSMV as "%5" but shows a BSMV amount equal to the 15% KKDF amount. This is an internal inconsistency; the weight of sources supports 15% for consumer credit. — [Yapı Kredi](https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/kredi-nasil-hesaplanir-adim-adim-kredi-hesaplama-rehberi)
- [TR · B · Yapı Kredi, 05.03.2026] Equal instalments use the annuity formula `Taksit = Anapara × [r(1+r)^n] / [(1+r)^n − 1]`. The YMO "faizi ve dosya masrafı, sigorta, BSMV, KKDF gibi tüm ek ücretleri içerir", and the bank advises comparing offers on YMO. — [Yapı Kredi](https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/kredi-nasil-hesaplanir-adim-adim-kredi-hesaplama-rehberi)
- [TR · L · TBK 583–584] Guarantor (kefil) formalities, including handwriting and spouse consent (§5). — [TBK](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6098.pdf)
- [TR · L · Banking Law 5411 Additional Art. 1 (2011)] A **Risk Merkezi** (risk centre) sits within TBB. It collects customers' risk data from credit institutions and approved financial institutions. It shares that data with members, with the persons themselves, and with third parties if the person consents. Membership is mandatory. — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
- [TR · P · KKB annual report 2022] KKB was founded on 11.04.1995 by nine banks. TBB's Risk Merkezi started operating on 28.06.2013. KKB launched **Findeks**, its platform for individuals and businesses, in 2014. — [KKB 2022 report](https://www.kkb.com.tr/Resources/ContentFile/2125/01kkbfrat2022.pdf)
- [TR · B · Yapı Kredi, 31.03.2026] KKB calculates the Findeks score to predict payment performance over the next 12 months. The range is **1–1900**, with these bands:

  | Band | Range |
  |---|---|
  | Çok Riskli | 1–969 |
  | Orta Riskli | 970–1149 |
  | Az Riskli | 1150–1469 |
  | İyi | 1470–1719 |
  | Çok İyi | 1720–1900 |

  **Conflict:** other web summaries quote different bands (e.g., "0–699 En Riskli"), probably outdated. Confirm on findeks.com before using band names. — [Yapı Kredi](https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/findeks-kredi-notu-nedir)
- [UK · L · in force 15.07.2026] Buy-now-pay-later in the form of **deferred payment credit** became FCA-regulated on 15 July 2026, when provided by third-party lenders. This means interest-free credit repaid in 12 or fewer instalments within 12 months. Lenders must give clear information, carry out proportionate affordability checks, and support customers in difficulty. — [Wiggin](https://wiggin.co.uk/insight/buy-now-pay-later-new-rules-come-into-force/); [Skadden](https://www.skadden.com/insights/publications/2025/07/fca-publishes-new-proposals)
- [EU · L · CCD2, Directive 2023/2225] CCD2 applies from **20 November 2026**. It brings most BNPL arrangements and small loans into EU consumer-credit law and makes creditworthiness checks mandatory. — [Taylor Wessing](https://www.taylorwessing.com/zh-hant/insights-and-events/insights/2025/06/new-consumer-credit-directive); [Vixio](https://vixio.com/insights/pc-mapping-eu-legislation-directive-eu-20232225-consumer-credit)

### Inferences
- **Plain-language mechanics (P):**
  - *Simple interest* (basit faiz) is charged on principal only. *Compound interest* (bileşik faiz) is also charged on interest already added. Turkish card debt cannot be compounded (5464).
  - In an *amortising* loan, the instalment stays the same, but early instalments are mostly interest (plus BSMV/KKDF on the interest) and later ones mostly principal. This explains "taksit ödüyorum ama anapara az düşüyor".
  - The repayment plan (ödeme planı) is the authoritative breakdown.
- **The agent MAY:**
  - explain these terms;
  - show where the YMO, the ödeme planı and the contract are;
  - explain the 14-day withdrawal right and early-repayment discount in general terms;
  - explain what affects credit scores in general terms;
  - take hardship disclosures and route them.
- **The agent MAY NOT:**
  - approve, decline or predict a credit decision;
  - negotiate rates;
  - advise whether to borrow;
  - promise that a restructuring or a credit-report change will be granted.
- **Typical escalations:** financial difficulty → collections / financial-support team; disputed bureau record → the bank's credit-reporting correction process.

### Gaps
- Turkish rules on credit-linked insurance (free choice of insurer, refund on early repayment) were not researched (researcher 09).
- Current TCMB maximum rates for cards and KMH, and the current minimum-payment thresholds, were not checked [periodic] (researcher 09).
- No Turkish-specific BNPL regulation was found in this research.

---

## 11. FX concepts, and Turkish taxes on FX purchases and banking transactions

### Takeaway
Basic FX terms:
- Banks quote a **buy rate** (alış: the bank buys from you) and a **sell rate** (satış: the bank sells to you). The gap is the **spread** (makas). The mid-market rate sits between them.
- A card payment abroad converts at the card scheme's rate plus any issuer FX fee. If the customer accepts **Dynamic Currency Conversion (DCC)** at the terminal or ATM, the merchant or ATM provider converts instead, usually at a worse rate.

Turkish taxes and charges [periodic]:
- FX and book-entry gold purchases bear **0.2% BSMV** (kambiyo vergisi).
- Fees bear general BSMV of 5%.
- Consumer-loan interest bears BSMV 15% and KKDF 15%.
- Deposit interest is subject to stopaj (§7).

### Cited Findings
- [TR · L · history of the FX-sale BSMV]
  - **15.05.2019:** 0.1% BSMV on FX sales. — [ProCompliance](https://www.procompliance.net/kambiyo-muamele-vergisi-geri-geldi-kambiyo-satislarinda-binde-1-vergi-alinacak/)
  - **2019:** sales to exporters and industrial-registry holders zero-rated. — [Verginet](https://www.verginet.net/dtt/11/Vergi-Sirkuleri-2019-80.aspx)
  - **2020, before 30 September** (exact date not captured): raised from 0.2% to **1%**. — [PwC](https://www.pwc.com.tr/tr/sektorler/bankacilik-sermaye-piyasalari/bultenler/kambiyo-muamelelerinde-banka-ve-sigorta-muameleleri-vergisine-iliskin-degisiklikler.html)
  - **30.09.2020:** cut back to **0.2%** for "döviz ve altın işlemlerinde" by Presidential Decision (RG 31260). — [ATO](https://www.atonet.org.tr/IcerikDetay/12449_kambiyo-islemlerinde-uygulanan-bsmv-orani-hakkinda)
- [TR · B · Kuveyt Türk, 2026 table, updated 17.08.2026]

  | Item | BSMV rate | Base |
  |---|---|---|
  | Consumer financing | 15% | The bank's profit share, fees and commissions |
  | Commercial financing and service commissions | 5% | — |
  | FX and book-entry precious-metal purchases | 0.2% | The sale amount |
  | Insurance | 5% | — |
  | Participation-account profit share | None | Stopaj applies instead |

  On a transfer, BSMV is charged on the **fee**, not on the amount sent (e.g., a 100 TL fee + 5% = 105 TL). — [Kuveyt Türk](https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir)
- [EU · L · Regulation (EU) 2019/518] DCC providers must show the amount in both currencies before the transaction, at ATMs and points of sale. They must disclose total currency-conversion charges as a **percentage mark-up over the latest ECB euro reference rates**. Card issuers must send electronic notifications for foreign-currency card transactions. — [Regulation 2019/518 (legislation.gov.uk)](https://www.legislation.gov.uk/eur/2019/518/contents/data.html); [Piraeus Bank FAQ](https://piraeusbank.gr/en/idiwtes/kartes/faqs-kartes-xrewseis-metatropis-nomismatwn)
- [TR · P/press] **Döviz vs efektif:** *döviz* is foreign currency held as account money or transfers; *efektif* is foreign banknotes and coins. Different rates (efektif kuru) can apply. A 2020 commission on cash-FX withdrawals that TCMB rules had allowed was later withdrawn after objections, according to press reports. — [Habertürk](https://www.haberturk.com/nakit-doviz-cekiminden-alinan-komisyon-kaldirildi-2782038-ekonomi)
- [TR · L/P · funds, 2025–2026] Withholding tax on investment funds was set at 17.5% from 09.07.2025 (Decision 10041). In 2026 the rate on money-market funds for corporate investors rose from 0% to 10%; the 17.5% rate for individuals was unchanged (press). — [İş Portföy](https://www.isportfoy.com.tr/medya-ve-blog/yatirim-fonlarina-uygulanan-stopaj-duzenlemesi-hakkinda); [Yeni Alanya](https://www.yenialanya.com/para-piyasasi-fonlarinda-stopaj-yuzde-10a-yukseltildi-kimleri-kapsiyor)

### Inferences
- **How the agent explains an FX cost (R):** split it into rate, spread, fee and tax, and quote live rates only from the bank's system or screens. Do not forecast exchange rates. Do not suggest timing a purchase.
- **TCMB rates vs bank rates (P; source quality low):** TCMB publishes daily *indicative* (gösterge niteliğinde) rates, but banks price FX freely. "Merkez Bankası kuru neden farklı?" is a common confusion. Verify the wording with the bank's FX desk.
- **DCC advice (P):** at foreign terminals, customers are often better off paying in the local currency. This is general cost information about DCC, not investment advice. The bank's own card FX fee should be quoted from its tariff.

### Gaps
- Not verified: whether the 0.2% BSMV applies to card purchases in foreign currency or to FX transfers without conversion.
- Not verified: card issuers' cross-border fee practices in Türkiye (researcher 06).
- No primary text was retrieved for the exact 2026 money-market-fund decision.

---

## 12. Balance and transaction concepts

### Takeaway
- The **ledger (current) balance** includes everything posted.
- The **available balance** is what can be spent now: posted balance, minus holds (provizyon/bloke), plus any overdraft (KMH).
- **Authorisations reduce the available balance or limit before posting.** Pre-authorisations (hotel, car rental, fuel) may hold more than the final charge.
- **Statements** (hesap özeti / ekstre) are period snapshots. **History** (hesap hareketleri) is live and can include pending items.
- **Legal attachments (haciz), injunctions (tedbir) and AML/fraud blocks are a different category from card holds.** Front-line staff cannot lift them.

### Cited Findings
- [US · B · Citi help guide] The current balance is the bank-record total and can include deposits still on hold. The available balance is what can be spent or withdrawn right now. — [Citi](https://www.citi.com/banking/personal-banking-guide/basic-finance/current-balance-vs-account-balance)
- [TR · B · Akbank, 11.07.2025] Akbank defines **provizyon** as "kredi kartınız ile yaptığınız harcamanın bankanız tarafından geçici olarak bloke edilmesi". The amount is deducted from the available limit but is not yet debt. It typically finalises in **1–3 business days**. Examples include hotel and car-rental security holds, online purchases with variable final amounts, and fuel. — [Akbank](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek)
- [INT · P · Adyen/Increase] An uncaptured hold expires; a captured one becomes a posted transaction. The final amount can differ from the authorised amount (§6). — [Adyen](https://docs.adyen.com/issuing/payment-stages/authorisation-holds.md)
- [TR · L · 5464 Art. 3, Art. 26] Credit-card terms (§8):
  - **Dönem borcu** (statement balance) = the balance of debit and credit entries up to the statement date (hesap kesim tarihi) plus the previous statement balance.
  - **Asgarî tutar** (minimum payment) = the least that must be paid.
  - **Son ödeme tarihi** (due date) = the last day to pay without falling into arrears.
  - There must be at least **10 days** between the statement date and the due date.
  — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · Enforcement and Bankruptcy Law (İİK) Art. 89]
  - The enforcement office notifies a third party, such as a bank, by a garnishment notice (*haciz ihbarnamesi*). From then on the bank may pay the debtor's money only to the enforcement office.
  - The bank must object within **7 days** if it claims it holds nothing. If it does not object, the amount is deemed to be in its hands.
  — [İİK](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf)
- [TR · L · İİK Art. 83] Salaries, pensions and similar income can be attached only after deducting what the debtor and family need to live. The attached amount cannot be less than one quarter. Several garnishments queue in order. — [İİK](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf)
- [TR · P · law-firm blog] An **enforcement attachment (icra haczi)** is creditor-driven and applied by the enforcement office to collect a debt; public receivables are often enforced electronically as e-haciz. A **MASAK or prosecutor block** serves public order and financial-crime purposes, not debt collection. — [Hukukçular Evi](https://hukukcularevi.com/masak-blokesi-icra-haczi-farki-oncelik-siralamasi/)
- [TR · L · Law 5549 Art. 4(2)] Obliged parties may not tell anyone, **including the parties to the transaction**, that a suspicious-transaction report was filed (only inspectors and courts may be told). — [Law 5549](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)
- [TR · anecdotal · Şikayetvar, 2025–2026] Real customer wording:
  - "Hesabıma, borcum ve icram olmamasına rağmen bloke konulmuş ve sebebi bana bildirilmiyor."
  - "Güvenlik nedeni ile konulan bloke kaldırılmıştır mesajı gelmesine rağmen giriş yapamıyorum."
  - "…2024 yılından beri güvenlik incelemesi gerekçesiyle bloke konulmuş durumda."
  - "Kocaeli İcra Dairesinden kısıt…"
  - "Kredi kartımla yurt dışında otel ödemem için… ön provizyon alındı."

  These quotes are anecdotal and show wording only, not frequency. — [Şikayetvar (Enpara, hesap/avukat)](https://www.sikayetvar.com/enpara/hesap/avukat?page=2); [Şikayetvar (Enpara, mesaj geldi)](https://www.sikayetvar.com/enpara/hesap/mesaj-geldi?page=2); [Şikayetvar (bloke / paramı çekemiyorum)](https://www.sikayetvar.com/bloke/parami-cekemiyorum); [Şikayetvar (Enpara, icra)](https://www.sikayetvar.com/enpara/hesap/icra?page=3); [Şikayetvar (VakıfBank, yurt dışı)](https://www.sikayetvar.com/vakifbank/kredi-karti-yurt-disina)

### Inferences — "bloke" triage the agent should run (R; verify against internal procedure)
1. **Authorisation hold (provizyon / ön provizyon).** Explain it and give the expected timeline. If it has not dropped off after the expected period, route to card operations or disputes.
2. **Bank security / fraud hold ("güvenlik blokesi").** Authenticate the customer through the approved flow, then route to fraud operations. Never ask for codes.
3. **Legal hold (haciz, ihtiyati tedbir, court order).** Explain that the bank must comply. Give the identifying details the bank's policy allows (authority, file number) and direct the customer to the creditor or enforcement office. The bank cannot "lift" the hold itself. Salary or pension protections (İİK 83) are for legal teams to apply.
4. **AML/compliance restriction.** Use neutral language ("hesabınızda bir inceleme süreci var"). Do not speculate or confirm reasons. Escalate to compliance through an internal case. Tipping-off rules apply (§15).
5. **Administrative restriction** (expired ID, KYC refresh, dormant account). Explain the document-update route.

**Documents and statement lines:**
- *Hesap özeti* is the periodic account statement; for credit cards it is commonly called *ekstre*.
- *Hesap hareketleri / hesap dökümü* is the live history, which can show pending items.
- *Dekont* is the receipt for a single transaction.
- Tax lines on statements typically appear as "BSMV", "KKDF", or "Stopaj / Gelir vergisi kesintisi" on interest or profit-share payouts.

### Gaps
- Turkish cheque clearing (takas) timelines and the treatment of uncleared funds were not researched (researchers 05/07).
- What a bank may disclose about an icra file to the customer is bank policy and should be verified.
- Statement-timing rules for deposit accounts in Türkiye were not researched.

---

## 13. Fee taxonomy (conceptual only; Turkish fee specifics belong to researchers 02/09)

### Takeaway
Fees fall into recognisable families: account, transfer, card, cash, FX, credit, late payment, documents, investment and safe deposit. In Türkiye, chargeable consumer fees are governed by TCMB's 2020 fee regulation and Communiqué 2020/7, and card fees must be in the contract. BSMV (generally 5%) is added on top of the fee.

### Cited Findings
- [TR · L · TCMB, 2020] TCMB's "Finansal Tüketicilerden Alınacak Ücretlere İlişkin Usul ve Esaslar Hakkında Yönetmelik" and Communiqué 2020/7 list the products and services for which fees may be charged. Examples include the credit-card annual membership fee (kart aidatı), branch cash withdrawal, EFT, havale and international transfers. Exact Official Gazette dates were not verified. — [TKBB explanatory note on Tebliğ 2020/7](https://www.tkbb.org.tr/upload/TKBB_2020_7_Sayili_Teblig_Kapsaminda_Ucretlendirilebilecek_Urun_ve_Hizmetlere_iliskin_izahname-revize%20%281%29.pdf); [Lexpera](https://www.lexpera.com.tr/mevzuat/yonetmelikler/finansal-tuketicilerden-alinacak-ucretlere-iliskin-usul-ve-esaslar-hakkinda-yonetmelik)
- [TR · L · 5464 Art. 26] Interest, commissions or costs that are not in the card contract cannot be charged. — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · B · Kuveyt Türk] General BSMV of 5% applies on fees and commissions. — [Kuveyt Türk](https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir)
- [EU · L · PAD] The EU PAD also mandates fee transparency, comparability and switching. — [EUR-Lex summary](https://eur-lex.europa.eu/summary/EN/090406_1)

### Inferences — taxonomy (P)

| Family | Examples (TR term) | Note for agent |
|---|---|---|
| Account | hesap işletim ücreti; account package fees | Check whether the fee is permitted for the product |
| Transfers | havale/EFT/FAST fee; SWIFT fee; correspondent charges (OUR/SHA/BEN) | Intermediary deductions are not the bank's fee |
| Cards | kart aidatı (yıllık üyelik ücreti); ek kart ücreti; replacement card | Waivers and campaigns vary |
| Cash | branch withdrawal; other-bank ATM; cash advance (nakit avans: fee + interest from day one, P) | Cash advance ≠ purchase |
| FX | spread (makas); efektif charges; card FX fee; DCC mark-up | Tax 0.2% BSMV on FX purchases |
| Credit | dosya masrafı / kredi tahsis ücreti; ekspertiz; insurance premiums; early-repayment compensation where allowed | Included in YMO |
| Late payment | gecikme faizi (interest, not a "fee"); participation banks: gecikme cezası | Capped by TCMB for cards |
| Documents | statement copy (ekstre/hesap özeti kopyası); reference letters | Often free digitally |
| Investment | custody (saklama), trading commission, fund management fee | Disclosed in product documents |
| Safe deposit | kiralık kasa ücreti | Branch-specific |

- **Rule (R):** quote fees from the bank's current tariff. Never invent fee amounts. Treat refund or waiver requests as policy decisions and escalate them.

### Gaps
- Specific fee caps, inflation-indexed maximums and banned fees in Türkiye belong to researchers 02/09.

---

## 14. Savings and investment basics, and the boundary between product information and personalised advice

### Takeaway
- **Deposits** are insured up to the limit and their return is set in advance; participation accounts are the exception and their returns are not guaranteed.
- **Investment products** (funds, bonds, equities, through the bank or an affiliated brokerage) are **not deposit-insured** and can lose value.
- Support may give factual information and help with processes.
- A **personal recommendation** ("which fund should I buy?", "should I sell my shares?") is regulated investment advice:
  - **EU:** MiFID II personal recommendation with a suitability test.
  - **TR:** SPK-regulated *yatırım danışmanlığı*, provided only by authorised firms under an advisory contract.
  - **UK:** advice, or since 6 April 2026 FCA "targeted support" by authorised firms.

### Cited Findings
- [EU · L · MiFID II Art. 4(1)(4)] "'investment advice' means the provision of personal recommendations to a client, either upon its request or at the initiative of the investment firm, in respect of one or more transactions relating to financial instruments". — [MiFID II (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065)
- [EU · L · MiFID II Art. 25(2)] For advice or portfolio management, the firm must obtain information on the client's "knowledge and experience in the investment field…, financial situation including his ability to bear losses, and his investment objectives including his risk tolerance" (the **suitability** test). — [MiFID II](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065)
- [EU · L · MiFID II Art. 25(3)] For other services, the firm asks about knowledge and experience in order to assess whether the product or service is **appropriate**. — [MiFID II](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065)
- [UK · L · FCA PS25/22] Targeted support lets authorised firms "provide suggestions designed for groups of consumers with common characteristics" on pensions and retail investments. It sits between guidance and a personal recommendation. Timeline:
  - near-final rules: 11.12.2025;
  - final rules confirmed: 26.02.2026;
  - permission applications open: 02.03.2026;
  - rules live: **06.04.2026**.
  — [FCA PS25/22](https://www.fca.org.uk/publications/policy-statements/ps25-22-supporting-consumers-pensions-investment-decisions-rules-targeted-support)
- [TR · P · standard SPK-driven disclaimer, used across the market] "Burada yer alan yatırım bilgi, yorum ve tavsiyeleri yatırım danışmanlığı kapsamında değildir. Yatırım Danışmanlığı hizmeti; aracı kurumlar, portföy yönetim şirketleri, mevduat kabul etmeyen bankalar ile müşteri arasında imzalanacak yatırım danışmanlığı sözleşmesi çerçevesinde sunulmaktadır." TEB Portföy's version adds "kişiye özel" (personalised). — [İş Yatırım](https://www.isyatirim.com.tr/tr-tr/urunler/Sayfalar/uyari-notu.aspx); [TEB Portföy](https://www.tebportfoy.com.tr/yasal-uyari); [Yatırım Finansman](https://www.yf.com.tr/yasal-uyari)
- [TR · L · SPK Communiqué III-37.1, RG 11.07.2013/28704, amended incl. 07.04.2022 (III-37.1.c)] This communiqué governs investment services and activities. The 2022 amendment states that certain pension-company recommendations and fund-platform communications are not investment advice (Art. 45/5–45/6). — [Alomaliye](https://www.alomaliye.com/2022/04/07/yatirim-hizmetleri-ve-faaliyetleri-ile-yan-hizmetler-iii-37-1-c/)
- [TR · P · secondary summary] Investment advice is "yönlendirici yorum ve tavsiye" given to a specific person or a group with similar financial situation and risk preferences, and only authorised institutions may provide it. Selling services labelled as "general" (e.g., buy/sell signals) that in substance amount to advice breaches capital-markets rules. This comes from an AI-generated search summary of SPK-related pages, so verify against the communiqué text. — [QNB Invest notice on SPK signal rules](https://www.qnbinvest.com.tr/forex/duyuru/spk-al-sat-sinyallerine-dair-tebligi)
- [TR · L · TMSF] "…devlet tahvili, hazine bonosu, yatırım fonu gibi yatırım araçları ile kripto varlıklar… sigorta edilmemektedir." — [TMSF](https://www.tmsf.org.tr/tr/Tmsf/Finansman/mevduat.sss.guncel)
- [US · L · FDIC] Stocks, bonds, mutual funds, annuities and crypto are not FDIC-insured (§4). — [FDIC](https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance)

### Inferences — what the support agent may / may not say (R; verify with Compliance)
- **MAY:**
  - describe product types and features using official documents (fund izahname / yatırımcı bilgi formu, KID, product terms);
  - state published past performance, with the "past performance is not a guide" disclaimer;
  - explain fees, taxes as published, how to buy, sell or redeem, and settlement/valör days as published;
  - say whether the product is deposit-insured;
  - show the issuer's risk class;
  - explain what the risk-profile / suitability / appropriateness questionnaire is and how to complete it;
  - explain how to reach a licensed advisor or portfolio manager.
- **MAY NOT:**
  - say "bunu almalısınız / satmalısınız";
  - rank products for this customer's situation;
  - forecast returns, interest rates or FX;
  - describe a katılma hesabı or a fund as having a guaranteed return;
  - help a customer get around a failed appropriateness warning;
  - give personal tax advice.
- **Escalation:** requests for personalised advice go to the licensed investment advisory or portfolio-management unit, or to the bank's affiliated brokerage. In Türkiye the standard disclaimer lists "**mevduat kabul etmeyen** bankalar" among advisory providers. This implies that deposit-taking banks route advice through authorised affiliates; verify against SPK III-37.1 and the bank's licence model (V).
- **Customer phrasings:**
  - "Hangi fona yatırayım?"
  - "Dolar mı alayım altın mı?"
  - "Faizler düşecek mi, vadeliye mi koyayım?"

  All three are requests for advice. Respond with neutral information and a referral.

### Gaps
- The SPK III-37.1 text defining "yatırım danışmanlığı" and its distinction from "genel yatırım tavsiyesi" was not retrieved verbatim.
- US Regulation Best Interest and FINRA suitability rules were not verified here (researcher 03).
- Whether Turkish deposit banks may give any investment advice directly needs confirmation with Compliance / SPK rules.

---

## 15. KYC, CDD, EDD, PEPs, sanctions screening, AML/CFT, source of funds and wealth, periodic refresh — and why staff may be unable to explain restrictions (tipping-off)

### Takeaway
Banks must:
- identify customers and beneficial owners;
- understand the relationship;
- monitor activity;
- apply enhanced measures to higher-risk customers, including politically exposed persons (PEPs);
- report suspicions to the financial intelligence unit (MASAK in Türkiye);
- keep records (8 years in Türkiye).

Telling anyone, including the customer, that a suspicious-transaction report exists is unlawful in Türkiye, the UK and the US. Front-line and AI agents therefore often **cannot say why** an account is restricted. Bank secrecy also restricts sharing customer data with third parties, including relatives.

### Cited Findings
- [TR · L · Law 5549, RG 18.10.2006/26323]
  - **Art. 3 (müşterinin tanınması; retitled by Law 7262, 27.12.2020):** obliged parties must identify the people transacting, and those on whose behalf they transact, **before** the transaction, and take "gerekli diğer tedbirleri".
  - **Art. 4(1):** suspicious transactions must be reported to MASAK.
  - **Art. 4(2):** the report may not be disclosed "işleme taraf olanlar dahil hiç kimseye", except to inspectors and courts.
  - **Art. 8:** documents must be kept for **8 years**; identification documents for 8 years from the last transaction.
  — [Law 5549](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)
- [TR · L · MASAK compliance-programme regulation (2008; amended several times, including an amendment published 25.12.2024; a further AML regulation change was published 22.08.2025, scope not verified)] A bank's compliance programme must include:
  - institutional policies and procedures;
  - risk management;
  - monitoring and control;
  - **a compliance officer (uyum görevlisi) and assistant**;
  - training;
  - internal audit.
  — [Alomaliye (25.12.2024 compliance amendment)](https://www.alomaliye.com/2024/12/25/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesi-uyum-degisiklik-25-12-2024/amp/); [Alomaliye (22.08.2025 change)](https://www.alomaliye.com/2025/08/22/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesi-22-08-2025/); [TOM Bank AML policy](https://www.tombank.com.tr/assets/images/doc/AML_tr.pdf)
- [TR · L · MASAK General Communiqué (No. 21), RG 17.11.2022] Rules for PEPs ("**kamusal nüfuz sahibi kişiler**"):
  - take reasonable measures to find out whether customers or beneficial owners are PEPs;
  - get **senior-level approval** for the relationship;
  - take reasonable measures to establish the **source of assets and funds**;
  - apply stricter measures to foreign PEPs and their spouses, relatives and close associates, and to domestic PEPs when risk is high;
  - continue the measures **for at least one year** after the person leaves office.
  — [İstiklal (17.11.2022)](https://www.istiklal.com.tr/ekonomi/nufuz-sahibi-kisilerin-finansal-islemlerine-tedbir-722638h); [Mondaq](https://www.mondaq.com/turkey/white-collar-crime-anti-corruption-fraud/1253060/masak-introduced-the-definition-of-politically-exposed-persons-with-communique-no-21)
- [INT · standard · FATF]
  - **Recommendation 10:** customer due diligence (CDD), including identifying and verifying the customer, applied on a risk basis (enhanced or simplified).
  - **Recommendation 12:** PEPs, i.e., "individuals who are or have been entrusted with prominent public functions by a foreign country", require measures beyond normal CDD.
  — [FSB page on FATF PEP guidance](https://www.fsb.org/2013/06/fatf-guidance-politically-exposed-persons-recommendations-12-and-22/)
- [UK · L · POCA 2002 s.333A] In the regulated sector it is an offence to disclose that a report (SAR) has been made, or that a money-laundering investigation is contemplated or under way, where the disclosure is likely to prejudice it. — [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2002/29/section/333A/data.htm); [Law Society](https://www.lawsociety.org.uk/topics/anti-money-laundering/tipping-off-a-client)
- [US · L · 31 USC 5318(g)(2); 31 CFR 1020.320(e)] A bank and its staff "may not notify any person involved in the transaction that the transaction has been reported", and must decline to produce a SAR or information revealing it. — [eCFR 31 CFR 1020.320](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320); [Cornell LII 12 CFR 21.11](https://www.law.cornell.edu/cfr/text/12/21.11)
- [TR · L · Banking Law 5411 Art. 73, amended 20.02.2020 by Law 7222]
  - People who learn bank or customer secrets through their role may disclose them only to legally authorised authorities.
  - Data about real and legal persons that arises after a banking relationship begins becomes **"müşteri sırrı"** (customer secret).
  - Except under the statutory exceptions, it may not be shared with third parties in Türkiye or abroad without the customer's own request or instruction, "**müşterinin açık rızası alınsa dahi**" (even with explicit consent under the data-protection law KVKK).
  — [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)

### Inferences — what this means for the support agent (R)
- **Why banks ask.** Banks ask for documents, purpose of account, occupation, source of funds or wealth, and periodic KYC refreshes because law requires risk-based CDD/EDD (FATF R.10; Law 5549 Art. 3). Agents can say this generically: "yasal yükümlülüklerimiz gereği bilgi ve belge talep ediyoruz".
- **What not to say when an AML block is possible:**
  - do not confirm or deny a report or investigation;
  - do not hint ("muhtemelen MASAK");
  - do not predict outcomes;
  - do not advise how to avoid checks.

  Do log the contact, the customer's statements and documents, and route an internal case to compliance or financial crime. Give the customer only the approved next step and the approved timeline wording. Where frustration or vulnerability is present, apply researcher 11's guidance.
- **Third-party questions.** "Annemin hesabında ne kadar var?" or calls from spouses and children: do not disclose without legal authority (power of attorney, guardianship, inheritance documents). This follows from Banking Law Art. 73 and data-protection rules.
- **Sanctions-screening holds** (e.g., a name match on a SWIFT payment) are usually resolved by the compliance team, which may ask the customer for information. The agent should not speculate about lists.

### Gaps
- EU AMLR/AMLA timing and UK MLR details belong to researcher 03.
- Turkish asset-freezing (Law 6415) and MASAK transaction-postponement powers were not reviewed (researcher 02).
- Whether, and how, a Turkish bank must tell the customer the reason for closing an account was not researched.

---

## 16. Organisational roles and hand-offs

### Takeaway
Front-line support (L1 contact centre, chat or AI) owns identification, information, guided self-service, intake and triage. Specialist teams own decisions and actions:
- payments, card and dispute operations;
- fraud, collections and lending;
- complaints;
- compliance / MLRO and legal;
- IT and digital channels.

Governance follows the "three lines of defence" model. Good hand-offs carry verified facts and context, never secrets.

### Cited Findings
- [EU · L · EBA Guidelines on internal governance, EBA/GL/2021/05, 02.07.2021] The three lines of defence:
  - **First line:** business lines and internal units that run operations and carry operational risk, including support functions such as IT.
  - **Second line:** the independent **risk management and compliance** function.
  - **Third line:** **internal audit**.
  — [EBA final report](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf)
- [TR · L · 5464 Arts. 8 and 11] Card issuers must keep a notification, request, complaint and objection system "kesintisiz olarak açık". They must answer complaints **within 20 days** through the cardholder's channel and make sure complaints reach the relevant units easily. — [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
- [TR · L · 6493 Art. 14(2)(d), Art. 18(3)] Payment and e-money institutions must set up complaint and objection units as a licensing condition. — [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
- [TR · L · MASAK compliance programme] Banks must appoint a compliance officer (uyum görevlisi) with an assistant and run a compliance unit (§15). — [TOM Bank AML policy](https://www.tombank.com.tr/assets/images/doc/AML_tr.pdf)
- [TR · B · İş Bankası] The dispute (chargeback) process involves bank-to-card-scheme procedures and can take up to about 180 days (§8). — [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir)

### Inferences — role map (P; generic model; verify against the institution's internal procedure)

| Team (TR name) | Owns | Typical triggers for escalation from L1/AI | What L1/AI should do first |
|---|---|---|---|
| L1 contact centre / chat / AI assistant (Müşteri İletişim Merkezi) | Authentication via approved flows; information; guided self-service; intake; triage; simple changes | — | Authenticate; classify; check known causes (cut-off, holds, limits) |
| L2 / specialist desks (kart, ödeme, kredi, dijital) | Complex enquiries, investigations within policy, callbacks | L1 can't resolve; policy exception; repeat contact | Package the case (see checklist below) |
| Branch operations (şube operasyon) | Cash; original documents; in-person ID; inheritance; power of attorney; guardianship; guarantor signatures | Document-based processes | Book appointment / list documents |
| Relationship / portfolio managers (müşteri / portföy yöneticisi) | SME, corporate and private clients: pricing, credit, investments | Segment customers; pricing questions | Warm transfer |
| Payment operations (ödeme / EFT-SWIFT operasyon) | EFT/FAST/SWIFT investigations, returns, recalls, repairs | Not received after cut-off + business days; wrong IBAN; SWIFT trace | Collect dekont / reference, amount, date-time, IBANs (masked) |
| Card operations (kart operasyon) | Card production and delivery, limits, statements, holds | Holds not released; card not received; statement errors | Check status; transaction details |
| Disputes / chargebacks (harcama itirazı / ters ibraz) | Scheme disputes, merchant-dispute evidence | Non-delivery, duplicate charge, cancelled-but-charged, unrecognised (if not fraud) | Log the dispute promptly (statutory and scheme clocks) |
| Fraud operations (dolandırıcılık / güvenlik) | 24/7 blocks, fraud claims, account takeover, scam cases | Unauthorised transactions; customer shared codes; "bank called me"; suspicious logins | Block cards/channels per policy immediately; never ask for codes |
| Collections and recoveries (tahsilat / takip, yapılandırma) | Arrears, payment plans, restructuring, legal follow-up | Missed payments; hardship; legal letters | Record hardship/vulnerability; no promises |
| Lending / underwriting (kredi tahsis) | Credit decisions, limits, collateral, guarantors | Application status, declined credit, limit changes | Status only; no decision talk |
| Complaints / customer relations (şikâyet yönetimi / müşteri ilişkileri) | Formal complaints, root cause, regulatory deadlines | Customer says "şikâyet etmek istiyorum"; dissatisfaction after resolution attempt | Log as complaint; give reference and timeline |
| Compliance / MLRO (uyum birimi, uyum görevlisi) | KYC/EDD decisions, AML/sanctions holds, suspicious-activity reports | Possible AML block; PEP / source-of-funds requests; sanctions hits | Neutral wording; internal referral; no tipping off |
| Legal (hukuk) | Garnishments, injunctions, court orders, inheritance disputes | Haciz/tedbir questions beyond basic info; lawyer letters | Route documents |
| IT service desk / digital channels | App and web incidents, outages, authentication issues | Error codes; outages; repeated OTP failures | Capture device/app version, time, error text (no secrets) |
| Data protection (KVKK) | Data-subject requests, data breaches | Customer asks for personal-data copy or deletion | Route the formal request |

**Hand-off checklist (R).** A good hand-off (warm transfer or case) contains:
1. Authentication outcome and method. Never include the credentials themselves.
2. Customer reference, segment and preferred channel / language.
3. Issue category and sub-type, in the customer's own words plus a normalised summary.
4. Timeline with dates and times: transaction date, value date, when the customer noticed.
5. Amounts and currency.
6. References: dekont number, masked IBAN, last 4 digits of the card, merchant name, case number.
7. What has already been checked or tried, and the result.
8. The customer's desired outcome.
9. Urgency or risk flags (fraud in progress, vulnerability, deadline).
10. Commitments made (callback window) and consents obtained.
11. Attachments.

**Exclude:** full card numbers, CVV, PIN, passwords and OTPs.

### Gaps
- Bank-specific team names, SLAs and routing rules are internal. Regulatory complaint deadlines beyond Law 5464 Art. 11 belong to researchers 02/04.
- No public Turkish source describes contact-centre tiering (L1/L2) in banks. The table above is a practice model and needs validation with the client institution.

---
## 17. Commonly confused pairs — precise distinctions

### Takeaway
Most "the bank took my money" or "the money hasn't arrived" contacts come from mixing up one of the pairs below. For each pair the table gives:
- the exact distinction;
- the Turkish terms;
- a typical customer phrasing;
- what the agent should do.

Customer phrasings are illustrative unless marked as anecdotal.

### Cited Findings (basis for the table)
- Balances and holds:
  - Available vs current balance: [Citi](https://www.citi.com/banking/personal-banking-guide/basic-finance/current-balance-vs-account-balance)
  - Provizyon: [Akbank](https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek)
  - Holds and the card lifecycle: [Adyen](https://docs.adyen.com/issuing/payment-stages/authorisation-holds.md)
- Card statements and disputes:
  - Card statement terms, minimum payment, ≥10-day gap, objections, card cancellation after non-payment: [Law 5464](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf)
  - Chargeback windows: [İş Bankası](https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir)
- Recurring payments:
  - Standing order, Direct Debit and CPA: [Barclays](https://barclays.co.uk/help/payments/payment-information/difference-order-debits); [Direct Debit Guarantee](https://www.directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/); [Which?](https://www.which.co.uk/money/banking/banking-security-and-payment-methods/direct-debits-and-standing-orders-explained-aU1tE5d00CI5)
- Credit cost:
  - APR / YMO: [CFPB](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/); [Tüketici Kredisi Sözleşmeleri Yönetmeliği](https://www.lexpera.com.tr/mevzuat/yonetmelikler/tuketici-kredisi-sozlesmeleri-yonetmeligi/3)
- Payment identifiers and rails:
  - IBAN: [Yapı Kredi](https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/iban-nedir-nasil-ogrenilir)
  - BIC: [ISO 9362](https://en.wikipedia.org/wiki/ISO_9362)
  - FAST / EFT: [Webrazzi](https://webrazzi.com/2026/08/24/fast-islem-limiti-300-bin-tlye-yukseliyor/)
- Legal holds and tipping-off:
  - Haciz: [İİK](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf)
  - Haciz vs MASAK block: [Hukukçular Evi](https://hukukcularevi.com/masak-blokesi-icra-haczi-farki-oncelik-siralamasi/)
  - Tipping-off: [Law 5549](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf)
- Account and product types:
  - Participation accounts: [Law 5411](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf)
  - E-money: [Law 6493](https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf)
  - Döviz vs efektif: [Habertürk](https://www.haberturk.com/nakit-doviz-cekiminden-alinan-komisyon-kaldirildi-2782038-ekonomi)
- Dates and advice:
  - Value date: [BIS CPMI](https://www.bis.org/committees/cpmi/glossary?selection=71)
  - Advice: [MiFID II](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065)

### Inferences — the table (R/P; Turkish legal points as cited above)

| Pair (EN / TR) | Precise distinction | Typical customer phrasing | Agent move / owner |
|---|---|---|---|
| **Available vs ledger (current) balance** / kullanılabilir bakiye vs hesap bakiyesi | Ledger = all *posted* entries. Available = ledger − holds (provizyon, bloke, uncleared items) + unused overdraft (KMH) where the bank includes it | "Bakiyem 5.000 görünüyor ama 3.000 harcayabiliyorum." | List holds and pending items with dates. If a hold is older than the expected window → card ops |
| **Authorisation vs settlement/posting** / provizyon vs kesinleşme (hesaba yansıma) | Authorisation = issuer approval plus a *temporary* reservation; no money has moved. Settlement = the final amount posts. It can differ from the hold or never post, in which case the hold expires | "Harcama yapmadım ama param düşmüş." / "Provizyon ne zaman kalkar?" | Explain the typical timeline (bank-specific; e.g., Akbank 1–3 business days; hotels and car rentals longer). If the customer doesn't recognise it → fraud |
| **Reversal vs refund vs chargeback** / iptal vs iade vs harcama itirazı (ters ibraz) | *İptal*: merchant cancels before settlement; the hold drops and the charge may never post. *İade*: merchant credits money back after settlement (alacak belgesi); timing depends on merchant, acquirer and issuer. *Chargeback*: issuer-raised dispute under scheme rules when the merchant won't fix it (non-delivery, duplicate, cancelled-but-charged). Unauthorised use is handled as fraud | "İade yaptılar dediler ama karta yansımadı." / "Ürün gelmedi, paramı istiyorum." | Ask for the merchant's refund reference and date. If none or overdue → dispute intake (scheme window, e.g., 120 days; TR statement objection 10 days after due date). Unauthorised → fraud ops |
| **Standing order vs direct debit vs recurring card payment** / düzenli ödeme talimatı vs otomatik ödeme talimatı vs düzenli kart ödemesi (abonelik) | Standing order: customer-created fixed transfer; the customer amends or cancels at the bank. Direct debit (UK): payee collects under a mandate, with advance notice of changes and refund guarantee; cancel via the bank. TR otomatik fatura talimatı: bank pays the biller's bills as issued. CPA: merchant charges the card; cancel with the merchant; UK card issuers must stop it on request | "Aboneliği iptal ettim, hâlâ çekiyorlar." / "Faturam otomatik ödenmemiş." | Identify the instrument first. Bank-held instructions → cancel or change in channel. Card subscriptions → merchant cancellation evidence; then issuer block or dispute per policy (TR rights: verify) |
| **Interest rate vs APR** / akdi faiz (oranı) vs yıllık maliyet oranı (efektif yıllık faiz) | Interest = the price of borrowing on principal. YMO/APR = *total* annualised cost: interest plus fees plus taxes (BSMV, KKDF) plus other charges, excluding notary costs in TR | "Faiz %3 dediniz, ödeme planı neden daha yüksek?" | Show the repayment plan; explain BSMV/KKDF and fees; compare offers on YMO; no rate negotiation |
| **Purchase vs cash advance** / alışveriş vs nakit avans | Cash advance draws *cash* on a credit card. It typically carries interest from the transaction date plus a fee, and is not eligible for interest-free periods (P; check the card tariff). Some quasi-cash transactions may be classified as cash advances (V) | "Karttan para çektim, neden hemen faiz işledi?" | Quote the tariff and statement lines; no waiver promises |
| **Statement date vs due date** / hesap kesim tarihi vs son ödeme tarihi | The statement date closes the period. The due date is the last day to pay without arrears (TR law: at least 10 days later). Spending after the cut-off goes on the next statement | "Ekstrem kesildi mi? Son ödeme hafta sonuna denk geldi." | Give both dates from the system; weekend/holiday handling is bank policy (verify) |
| **Minimum payment vs full statement balance** / asgari ödeme tutarı vs dönem borcu | Paying the minimum (TR: at least 20% of the statement balance by law; may be higher) avoids default, but the unpaid balance accrues contractual interest. Paying below the minimum triggers default interest. Minimum unpaid for 3 months, then 1 month after notice → cards cancelled (5464 Art. 8) | "Asgariyi ödedim, neden faiz geldi?" | Explain the mechanics; route hardship to collections or financial support |
| **IBAN vs account number vs BIC/SWIFT** / IBAN vs hesap numarası vs SWIFT (BIC) kodu | IBAN identifies an *account* across banks (TR: 26 characters, includes the bank code and account number). The account number is bank-internal. BIC identifies the *bank* (8 or 11 characters), needed for SWIFT | "SWIFT kodu ile IBAN aynı şey mi?" | Explain what the sender needs: domestic = IBAN + name; international = IBAN + BIC (+ intermediary if instructed) |
| **Havale vs EFT vs FAST** | Havale: same bank, instant. EFT: interbank on business days within system hours (queued otherwise). FAST: interbank instant 24/7 up to the limit (300,000 TL from 26.08.2026 [periodic]) | "Hafta sonu EFT yaptım, ne zaman geçer?" | Check which rail was used and the time vs cut-off; above the FAST limit → EFT next business day |
| **Block vs garnishment vs freeze** / bloke vs haciz vs dondurma / tedbir | *Bloke* is a generic word for a restriction by the bank (security/fraud, card hold, collateral "teminat blokesi"). *Haciz*: the enforcement office orders the bank to pay a creditor (İİK 89); the bank must comply; the customer deals with the creditor or icra office; salaries and pensions are partly protected (İİK 83). *Freeze / tedbir*: imposed by a court, prosecutor, MASAK or a sanctions regime; the bank cannot explain or lift it | (anecdotal) "Hesabıma, borcum ve icram olmamasına rağmen bloke konulmuş ve sebebi bana bildirilmiyor." | Run the §12 triage. Legal → give the identifiers policy allows. AML → neutral wording, no tipping-off, internal escalation |
| **Deposit vs participation account** / mevduat (faiz) vs katılma hesabı (kâr payı) | A deposit pays an agreed interest rate. A katılma hesabı shares profit or loss, has no predetermined return, and its principal is not guaranteed in law. Both are TMSF-covered up to the limit | "Katılım bankasında faiz oranı ne?" | Use kâr payı vocabulary; quote only published indicative or past rates |
| **Deposit vs e-money balance** / mevduat vs elektronik para | A deposit is at a bank: TMSF-insured, may pay interest. E-money at an EMI: safeguarded, no interest, not a deposit | "Cüzdan uygulamasındaki param da TMSF güvencesinde mi?" | Explain the licence difference; refer legal questions |
| **Döviz vs efektif** | Döviz = FX held as account money or transfers. Efektif = foreign banknotes; separate (usually wider) rates. Cash-FX withdrawal conditions and fees are bank-specific | "Dolar hesabımdan nakit dolar çekebilir miyim?" | Check branch cash availability, notice periods and tariff |
| **Statement vs history vs receipt** / hesap özeti (ekstre) vs hesap hareketleri (döküm) vs dekont | Statement = a fixed period's official summary. History = live list, including pending items. Dekont = proof of one transaction | "Dekont lazım, ekstre değil." | Point to the right document in the channel |
| **Value date vs transaction date vs posting date** / valör vs işlem tarihi vs kayıt tarihi | Value date = when funds are due or available and interest counts. Transaction date = when the customer acted. Posting date = when the ledger was updated | "Paranın valörü neden ertesi gün?" | Explain cut-off and business-day rules |
| **Information/guidance vs advice** / bilgi vs yatırım danışmanlığı | Information explains products and processes. Advice is a personal recommendation (licensed; suitability test) | "Hangi fonu alayım?" | Give neutral facts plus a referral to a licensed adviser (§14) |
| **Debit vs credit vs prepaid card** / banka kartı vs kredi kartı vs ön ödemeli kart | Debit spends own deposit money. Credit spends a credit line repaid via statements. Prepaid spends pre-loaded e-money | "Banka kartıma taksit yapılır mı?" | Explain the product; installment and credit features belong to credit cards (bank-specific exceptions) |
| **Credit score vs credit report** / kredi notu vs risk raporu | Score = a single number (Findeks 1–1900). Report = the underlying records of accounts and payments | "Kredi notum neden düştü?" | General factors only; correction requests → the bank's reporting team / KKB process |

### Gaps
- Turkish legal rights for cancelling recurring card payments, and bank holiday rules for due dates, were not verified (researchers 02/06/07).

---

## 18. Bilingual glossary (English | Turkish | one-line definition | typical customer phrasing)

### Takeaway
About 150 core terms follow. Definitions are plain-language and take Turkish legal meanings where cited above. Customer phrasings are illustrative constructions unless marked "(anecdotal)". The agent should treat **[periodic]** numbers as needing a live check.

### Cited Findings
The glossary draws only on sources already cited in §§1–17 (e.g., Laws 5411, 5464, 5549, 6493, 6502, 6098 and 2004; TMSF; Kuveyt Türk; CPMI; MiFID II; FCA; CFPB). No new factual claims are introduced in this section.

### Inferences — glossary

| # | English | Turkish | One-line definition | Typical customer phrasing |
|---|---|---|---|---|
| 1 | Bank / credit institution | Banka / kredi kuruluşu | Licensed institution that takes deposits (or participation funds) and lends; in TR "kredi kuruluşu" = deposit and participation banks | "Bu uygulama banka mı?" |
| 2 | Deposit bank | Mevduat bankası | Bank whose main business is accepting deposits and extending credit | — |
| 3 | Participation (Islamic) bank | Katılım bankası | Bank funding itself via özel cari / katılma accounts on profit-loss sharing; finances via trade, lease or partnership | "Faizsiz banka mı?" |
| 4 | Development & investment bank | Kalkınma ve yatırım bankası | Bank that lends but may not accept deposits or participation funds | — |
| 5 | Digital bank | Dijital banka | Branchless bank serving only via digital channels (BDDK regime since 2022) | "Şubeniz yok mu?" |
| 6 | Neobank | Neobank / dijital finans uygulaması | Marketing term for app-first providers; may be a bank, an e-money/payment institution or a partner model | "Bu uygulama güvenli mi, banka mı?" |
| 7 | Payment institution | Ödeme kuruluşu | TCMB-licensed firm providing payment services; no deposits, no lending | — |
| 8 | E-money institution | Elektronik para kuruluşu | TCMB-licensed e-money issuer; no interest, no lending; funds safeguarded | "Cüzdanımdaki para güvende mi?" |
| 9 | E-money | Elektronik para | Stored monetary value issued against funds received and used for payments; not a deposit | "Bakiye yükledim." |
| 10 | Safeguarding | Fonların korunması / koruma hesabı | Keeping PI/EMI customer funds separate at banks so they can be returned if the firm fails | — |
| 11 | Deposit insurance | Mevduat (ve katılım fonu) sigortası | Statutory cover if a bank's licence is revoked (TR 2026: 1,200,000 TL per person per bank [periodic]) | "Param devlet güvencesinde mi?" |
| 12 | TMSF | Tasarruf Mevduatı Sigorta Fonu | Turkish deposit insurer / resolution body | "TMSF limiti ne kadar?" |
| 13 | BDDK | Bankacılık Düzenleme ve Denetleme Kurumu | Turkish banking regulator and supervisor | — |
| 14 | TCMB | Türkiye Cumhuriyet Merkez Bankası | Central bank; runs EFT/FAST; regulates PIs/EMIs, fees and maximum card rates | "Merkez Bankası kuru farklı." |
| 15 | MASAK | Mali Suçları Araştırma Kurulu | Turkish financial intelligence unit receiving suspicious-transaction reports | "MASAK'a mı takıldım?" |
| 16 | SPK | Sermaye Piyasası Kurulu | Capital-markets regulator (investment services, advice) | — |
| 17 | Risk centre | Risk Merkezi (TBB) | Register of customers' credit risk data shared among lenders | "Risk raporumu nasıl alırım?" |
| 18 | Credit bureau | Kredi Kayıt Bürosu (KKB) | Bank-owned bureau (1995) operating Findeks | — |
| 19 | Correspondent bank | Muhabir banka | Bank that carries cross-border payments for another bank, sometimes deducting fees | "Aradaki banka kesinti yapmış." |
| 20 | Card scheme | Kart şeması / kartlı sistem kuruluşu | Network setting card rules (Visa, Mastercard, Amex, Troy) | — |
| 21 | Troy | Troy | Türkiye's domestic card scheme run by BKM (since 2016) | "Troy kart yurt dışında geçer mi?" |
| 22 | Issuer | Kart çıkaran kuruluş | Institution that issues the card and approves or declines authorisations | — |
| 23 | Acquirer | Üye işyeri anlaşması yapan kuruluş | Institution that contracts merchants for card acceptance | — |
| 24 | Merchant | Üye işyeri | Business accepting card payments | "İşyeri iade yapmıyor." |
| 25 | Current / checking account | Vadesiz hesap (vadesiz mevduat) | Account withdrawable on demand for day-to-day payments | "Vadesiz hesaba faiz var mı?" |
| 26 | Savings deposit (legal category) | Tasarruf mevduatı | Real persons' deposits not used for commercial transactions (except cheques) | — |
| 27 | Time deposit | Vadeli mevduat / vadeli hesap | Deposit for a fixed term at an agreed rate | "Vadeliye koymak istiyorum." |
| 28 | Maturity | Vade / vade sonu | End date of a deposit or loan term | "Vadem ne zaman doluyor?" |
| 29 | Early withdrawal | Vade bozma | Withdrawing a time deposit before maturity; normally only the demand rate is paid | "Vadeliyi bozarsam faizim yanar mı?" |
| 30 | Automatic rollover | Otomatik vade yenileme | Deposit renews at maturity at the then-current rate | "Hesabım kendiliğinden yenilenmiş." |
| 31 | FX deposit account | Döviz tevdiat hesabı (DTH) | Deposit account in foreign currency; interest withholding 25% [periodic] | "Dolar hesabı açmak istiyorum." |
| 32 | Gold account | Altın hesabı | Book-entry gold (grams); TMSF-covered; 0.2% BSMV on purchases [periodic] | "Gram altınımı fiziki alabilir miyim?" |
| 33 | Participation account | Katılma hesabı | Profit/loss-sharing account; no predetermined return; principal not guaranteed | "Kâr payı ne kadar olacak?" |
| 34 | Special current account | Özel cari hesap | Participation-bank demand account paying no return | — |
| 35 | Profit share | Kâr payı | Return on participation accounts, known at maturity (also the "interest" equivalent on participation financing) | "Kâr payım neden düşük?" |
| 36 | Unit account value | Birim hesap değeri | Value basis of a participation account (used for TMSF cover) | — |
| 37 | Arranged overdraft | Kredili mevduat hesabı (KMH); brand names e.g. "ek hesap", "artı para" | Credit line attached to a demand account; daily interest on the amount used | "Ek hesaptan habersiz para kullanmışım." |
| 38 | Joint account (either-to-sign) | Teselsüllü (münferit) ortak hesap | Each holder may transact alone | "Eşim tek başına çekebilir mi?" |
| 39 | Joint account (all-to-sign) | Teselsülsüz (müşterek) hesap | All holders must act together | "Neden ATM'den çekemiyoruz?" |
| 40 | Minor's account | Çocuk hesabı (veli/vasi) | Account for under-18s opened or run by a parent or guardian; TMSF-covered separately | "Çocuğuma hesap açabilir miyim?" |
| 41 | Basic payment account | Temel ödeme hesabı (EU) | EU statutory account with basic features for legal residents | — |
| 42 | Salary account | Maaş hesabı | Account receiving salary, often under an employer–bank protocol | "Maaş hesabımı taşımak istiyorum." |
| 43 | Salary / pension promotion | Maaş / emekli promosyonu | Upfront payment for committing salary or pension for a period; pro-rata refund if leaving early (bank/protocol-specific) | "Promosyonu iade etmem gerekir mi?" |
| 44 | FX-protected deposit | Kur Korumalı Mevduat (KKM) | Discontinued TL deposit with FX compensation; no openings or renewals since 23.08.2025 | "KKM hesabım ne olacak?" |
| 45 | Time-barred (dormant) funds | Zamanaşımına uğrayan mevduat | Funds unclaimed for 10 years; transferred to TMSF after announcement (5411 Art. 62) | "Eski hesabımdaki para nerede?" |
| 46 | Withholding tax | Stopaj / gelir vergisi tevkifatı | Tax deducted at source from interest or profit share (TL ≤6m: 17.5% [periodic]) | "Faizimden neden kesinti var?" |
| 47 | Debit card | Banka kartı | Card giving access to deposit or özel cari accounts | "Banka kartıma taksit yapılır mı?" |
| 48 | Credit card | Kredi kartı | Card (or card number) giving a credit line with a statement cycle | — |
| 49 | Prepaid card | Ön ödemeli kart | Card loaded in advance, usually e-money; no credit line | "Kartıma para yükledim." |
| 50 | Virtual card | Sanal kart | Card number without plastic, for online use | "Sanal kart limitimi nasıl ayarlarım?" |
| 51 | Supplementary card | Ek kart | Extra card on the main cardholder's account or limit; primary holder usually liable | "Oğluma ek kart çıkarmak istiyorum." |
| 52 | Corporate / business card | Kurumsal / ticari kart | Card for business expenses; liability model per contract | — |
| 53 | Card annual fee | Kart aidatı / yıllık üyelik ücreti | Annual credit-card fee, chargeable only if in the contract | "Aidat iadesi istiyorum." |
| 54 | Cash advance | Nakit avans | Cash drawn on a credit card; interest typically from day one plus a fee | "Karttan para çektim, faiz işledi." |
| 55 | Instalment purchase | Taksitli alışveriş | Purchase split over months on a credit card | "Taksit sayısını değiştirebilir miyim?" |
| 56 | Statement closing date | Hesap kesim tarihi | Date the card statement period closes | "Ekstrem kesildi mi?" |
| 57 | Payment due date | Son ödeme tarihi | Last day to pay without arrears (≥10 days after the statement in TR law) | "Son ödeme günü ne zaman?" |
| 58 | Statement balance | Dönem borcu | Amount owed for the period, including the previous balance | — |
| 59 | Minimum payment | Asgari ödeme tutarı | Least payment to avoid default (≥20% of the statement balance in TR law; may be higher) | "Asgariyi ödesem yeter mi?" |
| 60 | Contractual interest | Akdi faiz | Interest on an unpaid balance under the contract (TCMB caps for cards) | — |
| 61 | Default (late) interest / late penalty | Gecikme faizi / (katılım) gecikme cezası | Higher charge when less than the minimum is paid or debt is overdue | "Gecikme faizi neden bu kadar?" |
| 62 | Authorisation (hold) | Provizyon / otorizasyon | Issuer approval reserving funds or limit; not yet a final debit | "Provizyonda bekliyor." |
| 63 | Pre-authorisation | Ön provizyon | Estimated hold (hotel, car rental, fuel), later adjusted or released | (anecdotal) "…otel ödemem için… ön provizyon alındı." |
| 64 | Reversal / cancellation | İptal | Merchant cancels before settlement; the hold is released | "İptal ettiler ama limitim açılmadı." |
| 65 | Refund | İade (alacak belgesi) | Merchant returns money after settlement as a credit | "İade yaptılar ama karta yansımadı." |
| 66 | Chargeback | Harcama itirazı / ters ibraz | Issuer-raised dispute under card-scheme rules (windows e.g. 120 days) | "Ürün gelmedi, itiraz etmek istiyorum." |
| 67 | Dynamic currency conversion | Dinamik kur çevrimi (DCC) | Merchant or ATM converts to the card's currency at the terminal, usually with a mark-up | "Yurt dışında TL ile öde dedi, pahalı mı?" |
| 68 | 3-D Secure | 3D Secure / 3D güvenli ödeme | Online card authentication step (app or SMS approval) — the bank never asks for the code | "3D şifresi gelmiyor." |
| 69 | Card security code | Güvenlik kodu (CVV/CVC) | 3-digit code; never to be requested by the bank or agent | "Bankadan aradılar, CVV'mi sordular." → fraud |
| 70 | Same-bank transfer | Havale | Transfer within the same bank, usually instant | — |
| 71 | EFT | Elektronik Fon Transferi | Interbank TL transfer via TCMB, on business days within system hours | "Hafta sonu EFT yaptım." |
| 72 | FAST | FAST (Fonların Anlık ve Sürekli Transferi) | Interbank instant 24/7 transfer up to a limit (300,000 TL from 26.08.2026 [periodic]) | "FAST limiti ne kadar?" |
| 73 | IBAN | IBAN | Standard account identifier; TR format is 26 characters | "IBAN'ımı nereden bulurum?" |
| 74 | Account number | Hesap numarası | Bank-internal account identifier (embedded in the IBAN) | — |
| 75 | BIC / SWIFT code | BIC / SWIFT kodu | 8- or 11-character bank identifier for international payments | "SWIFT kodunuz nedir?" |
| 76 | SWIFT transfer | SWIFT ile yurt dışı transfer | Cross-border transfer via SWIFT messaging and correspondent banks | "Yurt dışından para gelecek, ne lazım?" |
| 77 | Charge options OUR/SHA/BEN | Masraf seçeneği (OUR/SHA/BEN) | Who pays SWIFT fees: sender, shared, or beneficiary | "Gelen paradan kesinti yapılmış." |
| 78 | SEPA | SEPA (Tek Avro Ödeme Alanı) | Euro payment area schemes; instant transfers mandatory for euro-area PSPs since 2025 | — |
| 79 | Instant payment | Anlık ödeme | Payment credited within seconds, 24/7 (FAST, SCT Inst, FedNow) | — |
| 80 | Verification / confirmation of payee | Alıcı adı doğrulama (VoP / CoP) | Pre-payment check that the payee name matches the account (EU mandatory Oct 2025) | — |
| 81 | ACH | ACH (otomatik takas, ABD) | US batch electronic payments (next-day / same-day) | — |
| 82 | Standing order | Düzenli ödeme talimatı | Customer-set recurring fixed transfer | "Her ay kiramı otomatik göndermek istiyorum." |
| 83 | Direct debit / bill auto-pay | Otomatik ödeme talimatı (doğrudan borçlandırma) | Payee-initiated collection under a mandate (UK) / bank pays the biller's invoices automatically (TR) | "Faturam otomatik ödenmemiş." |
| 84 | Recurring card payment (CPA) | Düzenli kart ödemesi / abonelik | Merchant-initiated repeat charges to a card | "Aboneliği iptal ettim, hâlâ çekiyor." |
| 85 | Cut-off time | Son işlem saati / kesim saati | Time after which orders are treated as next-business-day orders | "Saat kaçtan sonra ertesi güne kalır?" |
| 86 | Business day | İş günü | Day payment systems settle (excludes weekends and holidays) | — |
| 87 | Value date | Valör (valör tarihi) | Date funds are due or available and interest starts or stops | "Valörü ne zaman?" |
| 88 | Transaction / posting date | İşlem tarihi / kayıt (hesaba yansıma) tarihi | When the customer acted / when the ledger was updated | — |
| 89 | Receipt | Dekont | Bank's proof of a single transaction | "Dekont gönderir misiniz?" |
| 90 | Returned transfer | Geri dönen havale/EFT | Transfer bounced back (wrong IBAN/name, closed account, etc.) | "Gönderdiğim para geri döndü." |
| 91 | Payment recall | Geri çağırma (ör. SWIFT recall) | Sender's request to retrieve a sent payment; needs the receiving side's cooperation (P) | "Yanlış IBAN'a gönderdim, geri alır mısınız?" |
| 92 | Ledger / current balance | Hesap bakiyesi | Total of all posted entries | — |
| 93 | Available balance | Kullanılabilir bakiye | Ledger minus holds, plus any available overdraft | "Kullanılabilir bakiyem neden az?" |
| 94 | Pending transaction | Bekleyen / provizyondaki işlem | Authorised but not yet posted | — |
| 95 | Posted / settled transaction | Kesinleşmiş (hesaba yansımış) işlem | Final entry on ledger and statement | — |
| 96 | Clearing | Takas | Exchange and confirmation of transaction details between institutions before settlement | — |
| 97 | Settlement | Mutabakat / hesaplaşma | Final transfer of funds between institutions | — |
| 98 | Statement | Hesap özeti / (kart) ekstre | Periodic official summary of an account or card | "Ekstrem gelmedi." |
| 99 | Transaction history | Hesap hareketleri / hesap dökümü | Live list of entries, including pending items | "Son üç ayın dökümünü istiyorum." |
| 100 | Block / hold | Bloke | Restriction on funds (bank security, card hold, collateral, or legal) | (anecdotal) "Hesabıma bloke konmuş, sebebi söylenmiyor." |
| 101 | Collateral block | Teminat blokesi | Funds blocked as security for a loan or guarantee (P) | — |
| 102 | Garnishment / attachment | Haciz | Enforcement-office seizure of funds for a creditor | "Hesabıma haciz geldi." |
| 103 | Garnishment notice | Haciz ihbarnamesi (89/1) | Notice to a third party (the bank) under İİK 89; the bank answers within 7 days | — |
| 104 | Salary garnishment | Maaş haczi | Attachment of salary or pension after a living allowance; at least 1/4 attachable (İİK 83) | "Maaşımın tamamına mı haciz kondu?" |
| 105 | Injunction | İhtiyati tedbir | Court-ordered provisional measure (e.g., freezing funds) | — |
| 106 | Asset freeze / transaction postponement | Malvarlığının dondurulması / işlemin ertelenmesi | Authority-imposed restriction (crime / terror financing / sanctions) | — |
| 107 | Cheque | Çek | Written order to pay from a cheque account | "Çekim takasta." |
| 108 | Bounced cheque | Karşılıksız çek | Cheque presented without sufficient funds | — |
| 109 | Uncleared funds | Takastaki / tahsil edilmemiş tutar | Credited items not yet usable until cleared | "Çek yatırdım, neden kullanamıyorum?" |
| 110 | Consumer loan | İhtiyaç kredisi (tüketici kredisi) | Personal loan repaid in instalments | "İhtiyaç kredisi faizi ne?" |
| 111 | Auto loan | Taşıt kredisi | Loan to buy a vehicle, often with a pledge | — |
| 112 | Mortgage loan | Konut kredisi | Home loan secured by a mortgage (ipotek) | — |
| 113 | Revolving credit | Döner kredi (kart, KMH) | Credit line that becomes available again as it is repaid | — |
| 114 | Buy now, pay later | Şimdi al sonra öde / alışveriş kredisi | Short-term split payment at checkout (UK regulated 15.07.2026; EU CCD2 20.11.2026) | — |
| 115 | Interest rate | Faiz oranı (akdi faiz oranı) | Price of borrowing applied to principal | "Aylık faiz kaç?" |
| 116 | APR / annual cost rate | Yıllık maliyet oranı / efektif yıllık faiz oranı | Total cost of credit (interest + fees + taxes, excl. notary) as an annual percentage | "Yıllık maliyet neden faizden yüksek?" |
| 117 | Simple interest | Basit faiz | Interest only on principal | — |
| 118 | Compound interest | Bileşik faiz | Interest on principal plus accumulated interest; prohibited on card debt in TR | — |
| 119 | Amortisation | İtfa / anapara geri ödemesi | Gradual repayment of principal through instalments | "Anaparam neden az düşüyor?" |
| 120 | Repayment plan | Ödeme planı | Schedule of instalments split into principal, interest and taxes | "Ödeme planımı görebilir miyim?" |
| 121 | Instalment | Taksit | Periodic repayment amount | — |
| 122 | Principal | Anapara | Amount borrowed that is still owed | — |
| 123 | Early repayment | Erken ödeme / erken kapama / ara ödeme | Paying before schedule; interest must be discounted (6502 Art. 27) | "Kredimi erken kapatırsam ne öderim?" |
| 124 | Right of withdrawal | Cayma hakkı | 14-day right to withdraw from a consumer credit (6502 Art. 24) | "Krediden vazgeçmek istiyorum." |
| 125 | Acceleration | Muacceliyet | Calling the whole debt due (TR consumer loans: after 2 consecutive missed instalments + 30-day notice) | "Borcun tamamını istiyorlar." |
| 126 | Collateral | Teminat | Asset or right securing a loan | — |
| 127 | Mortgage (lien) | İpotek | Real-estate security registered at the land registry | — |
| 128 | Pledge | Rehin | Security over movable assets (e.g., vehicle) | — |
| 129 | Guarantor | Kefil / müteselsil kefil | Person liable if the borrower doesn't pay; strict handwriting and spouse-consent rules (TBK 583–584) | "Kefil olduğum kredi ödenmiyor." |
| 130 | Credit-linked insurance | Kredi bağlantılı (hayat) sigorta | Insurance attached to a loan (TR rules not verified here) | "Sigortayı zorunlu tuttular." |
| 131 | Credit score | Kredi notu (Findeks) | KKB score 1–1900 predicting repayment behaviour | "Kredi notum neden düştü?" |
| 132 | Credit report | Risk raporu / KKB raporu | Record of credit accounts and payment history | — |
| 133 | Restructuring | Yapılandırma | Revised repayment plan for debts in difficulty | "Borcumu yapılandırmak istiyorum." |
| 134 | Collections / legal follow-up | Tahsilat / yasal takip | Recovery of overdue debt, possibly via enforcement | "Avukatlık bürosu aradı." |
| 135 | Buy rate | Alış kuru | Rate at which the bank buys currency from the customer | "Dolar alış kaç?" |
| 136 | Sell rate | Satış kuru | Rate at which the bank sells currency to the customer | — |
| 137 | Spread | Makas (kur farkı) | Difference between the buy and sell rates | "Makas neden bu kadar açık?" |
| 138 | Mid-market rate | Piyasa orta kuru | Midpoint between wholesale buy and sell rates | — |
| 139 | Indicative central-bank rate | TCMB gösterge kuru | Daily reference rate published by TCMB; not a dealing rate (P) | "Merkez Bankası kuruyla neden satmıyorsunuz?" |
| 140 | Cash FX (banknotes) | Efektif | Physical foreign banknotes, with their own rates and conditions | "Efektif çekmek istiyorum." |
| 141 | BSMV | Banka ve Sigorta Muameleleri Vergisi | Tax on banks' fees and income; 0.2% on FX/gold purchases; 15% on consumer-credit interest; 5% general [periodic] | "Dekonttaki BSMV ne?" |
| 142 | KKDF | Kaynak Kullanımını Destekleme Fonu | Levy on consumer-loan interest (15% [periodic]) | "KKDF neden kesiliyor?" |
| 143 | FX-purchase tax (popular name) | Kambiyo vergisi | Popular name for the 0.2% BSMV on FX and gold purchases | — |
| 144 | Investment fund | Yatırım fonu | Pooled portfolio; can lose value; not deposit-insured | "Fon zarar eder mi?" |
| 145 | Government bond / T-bill | Devlet tahvili / hazine bonosu | Government debt securities; not deposit-insured | — |
| 146 | Equity / share | Hisse senedi | Ownership share in a company traded on Borsa İstanbul | — |
| 147 | Brokerage firm | Aracı kurum | SPK-licensed securities intermediary | — |
| 148 | Investment advice | Yatırım danışmanlığı | Personal recommendation; licensed activity under an advisory contract | "Hangi fonu alayım?" |
| 149 | Suitability / appropriateness test | Yerindelik / uygunluk testi | Checks of client fit before advice (suitability) or non-advised sales (appropriateness) | "Uygunluk testi neden çıktı?" |
| 150 | Know your customer | Müşterinin tanınması (KYC) | Identifying and understanding customers (5549 Art. 3) | "Neden bu belgeleri istiyorsunuz?" |
| 151 | CDD / EDD | Müşteri tanıma tedbirleri / sıkılaştırılmış tedbirler | Standard vs enhanced checks according to risk | — |
| 152 | Politically exposed person | Kamusal nüfuz sahibi kişi | Holder of a prominent public function; enhanced measures (≥1 year after leaving office in TR) | — |
| 153 | Beneficial owner | Gerçek faydalanıcı | Natural person who ultimately owns or controls the customer or transaction | — |
| 154 | Source of funds / wealth | Fonların kaynağı / malvarlığının kaynağı | Origin of specific money / of overall wealth | "Bu para nereden geldi diye soruyorlar." |
| 155 | Sanctions screening | Yaptırım taraması | Checking names and payments against sanctions lists | "Transferim neden incelemede?" |
| 156 | Suspicious transaction report | Şüpheli işlem bildirimi | Confidential report to MASAK | — |
| 157 | Tipping off | Bildirimin açıklanması yasağı | Ban on revealing that a report or investigation exists | "Neden bloke olduğunu söylemiyorsunuz?" |
| 158 | Compliance officer / MLRO | Uyum görevlisi | Officer responsible for the AML/CFT compliance programme | — |
| 159 | Bank / customer secrecy | Banka sırrı / müşteri sırrı | Duty not to disclose customer data without legal basis or the customer's instruction (5411 Art. 73) | "Eşimin hesabını sorabilir miyim?" |
| 160 | Power of attorney | Vekâletname | Notarised authority to act for someone | "Annem adına işlem yapabilir miyim?" |
| 161 | Inheritance certificate | Mirasçılık belgesi (veraset ilamı) | Document identifying heirs, needed to release a deceased person's funds | "Babamın hesabındaki parayı nasıl alırız?" |
| 162 | Contact centre | Çağrı merkezi / müşteri iletişim merkezi | Phone and chat customer service, with IVR | — |
| 163 | Relationship manager | Müşteri temsilcisi / portföy yöneticisi | Named banker for a customer portfolio | "Temsilcime bağlanmak istiyorum." |
| 164 | Complaint | Şikâyet | Expressed dissatisfaction requiring a formal response (TR cards: within 20 days) | "Şikâyet kaydı açmak istiyorum." |

### Gaps
- Terms specific to cards, payments, fraud and digital authentication are covered in more depth by researchers 06, 07, 08 and 10.

---

## Source register

All accessed 2026-10-10 unless stated. "n.c." = date not captured.

| # | Title | Publisher | Date (pub / updated) | Jurisdiction | URL |
|---|---|---|---|---|---|
| 1 | Mevduat Sigortacılığı Hakkında Sıkça Sorulan Sorular | TMSF | current (2026 limit) | TR | https://www.tmsf.org.tr/tr/Tmsf/Finansman/mevduat.sss.guncel |
| 2 | TMSF, sigortaya tabi mevduat ve katılım fon tutarını yükseltti | Anadolu Ajansı | late 2025 (n.c.) | TR | https://www.aa.com.tr/tr/ekonomi/tmsf-sigortaya-tabi-mevduat-ve-katilim-fon-tutarini-yukseltti/3770056 |
| 3 | TMSF Güvencesi | Albaraka Türk | n.c. | TR | https://www.albaraka.com.tr/tr/bireysel/hesaplar/tmsf-guvencesi |
| 4 | 5411 sayılı Bankacılık Kanunu (consolidated) | mevzuat.gov.tr | consolidated text | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5411.pdf |
| 5 | 5464 sayılı Banka Kartları ve Kredi Kartları Kanunu | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5464.pdf |
| 6 | 5549 sayılı Suç Gelirlerinin Aklanmasının Önlenmesi Hakkında Kanun (RG 18.10.2006/26323) | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5549.pdf |
| 7 | 6493 sayılı Ödeme ve Menkul Kıymet Mutabakat Sistemleri, Ödeme Hizmetleri ve Elektronik Para Kuruluşları Hakkında Kanun | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf |
| 8 | 6502 sayılı Tüketicinin Korunması Hakkında Kanun | mevzuat.gov.tr | consolidated (incl. 24.10.2024 amendment) | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6502.pdf |
| 9 | 6098 sayılı Türk Borçlar Kanunu | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6098.pdf |
| 10 | 2004 sayılı İcra ve İflas Kanunu | mevzuat.gov.tr | consolidated | TR | https://www.mevzuat.gov.tr/MevzuatMetin/1.3.2004.pdf |
| 11 | Tüketici Kredisi Sözleşmeleri Yönetmeliği, Art. 4 | Lexpera (RG 22.05.2015/29363; amended to 31.12.2024) | 2024 | TR | https://www.lexpera.com.tr/mevzuat/yonetmelikler/tuketici-kredisi-sozlesmeleri-yonetmeligi/3 |
| 12 | BKK 2006/11188 on deposit/loan rates and participation accounts | Lexpera (RG 22.11.2006/26354; amended 01.01.2013) | 2013 | TR | https://www.lexpera.com.tr/mevzuat/bakanlar-kurulu-kararlari/mevduat-ve-kredi-faiz-oranlari-ve-katilma-hesaplari-kar-ve-zarara-katilma-oranlari-ile-ozel-cari |
| 13 | KKM dönemi resmen sona erdi | CNN Türk | 24.01.2026 | TR | https://www.cnnturk.com/ekonomi/kkm-donemi-resmen-sona-erdi-2388577 |
| 14 | EY Vergi Rehberi 2026 | EY Türkiye | as of 14.01.2026 | TR | https://www.ey.com/content/dam/ey-unified-site/ey-com/tr-tr/services/tax/documents/2026/ey-tr-vergi-rehberi-2026.pdf |
| 15 | Finansal Şeffaflık: BSMV Nedir ve Nasıl Hesaplanır? | Kuveyt Türk | 21.08.2026 (upd. 17.08.2026) | TR | https://www.kuveytturk.com.tr/blog/finans/finansal-seffaflik-bsmv-banka-ve-sigorta-muameleleri-vergisi-nedir-ve-nasil-hesaplanir |
| 16 | Kambiyo işlemlerinde uygulanan BSMV oranı hakkında | Ankara Ticaret Odası | 30.09.2020 | TR | https://www.atonet.org.tr/IcerikDetay/12449_kambiyo-islemlerinde-uygulanan-bsmv-orani-hakkinda |
| 17 | Kambiyo Muamelelerinde BSMV'ye İlişkin Değişiklikler | PwC Türkiye | 2020 | TR | https://www.pwc.com.tr/tr/sektorler/bankacilik-sermaye-piyasalari/bultenler/kambiyo-muamelelerinde-banka-ve-sigorta-muameleleri-vergisine-iliskin-degisiklikler.html |
| 18 | Kambiyo Muamele Vergisi Geri Geldi… | ProCompliance | 15.05.2019 | TR | https://www.procompliance.net/kambiyo-muamele-vergisi-geri-geldi-kambiyo-satislarinda-binde-1-vergi-alinacak/ |
| 19 | Sanayicilere ve İhracatçılara Yapılan Döviz Satışlarında BSMV Oranı Sıfır | Verginet | 2019 | TR | https://www.verginet.net/dtt/11/Vergi-Sirkuleri-2019-80.aspx |
| 20 | TCMB'den Papara açıklaması | Forbes Türkiye | 27.05.2025 | TR | https://www.forbes.com.tr/haberler/tcmb-den-papara-aciklamasi-iceride-parasi-olanlara-ne-olacak |
| 21 | Papara Elektronik Para A.Ş. Hakkında Basın Duyurusu (copy) | Alomaliye | 27.05.2025 | TR | https://www.alomaliye.com/2025/05/27/papara-elektronik-para-a-s-hakkinda-basin-duyurusu/ |
| 22 | "Neobanks": what are they and what do they offer? | Banco de España | 03.12.2020 | EU (ES) | https://clientebancario.bde.es/pcb/en/blog/neobanco-que-son-y-que-ofrecen.html |
| 23 | FCA demands UK fintechs clarify non-bank status to customers | FinTech Futures | n.c. | UK | https://www.fintechfutures.com/bankingtech/fca-demands-uk-fintechs-clarify-non-bank-status-to-customers |
| 24 | Katılım Bankacılığı Nedir? Nasıl Çalışır? (brochure) | TKBB | undated (pre-2019 figures) | TR | https://tkbbegitim.org.tr/Documents/Yonetmelikler/TKBB-Katilim-Bankaciligi-Nedir-Brosur.pdf |
| 25 | Banks: At the Heart of the Matter | IMF F&D (J. Gobat) | compiled 2017 | INT | https://www.imf.org/external/pubs/ft/fandd/basics/pdf/gobat-banks.pdf |
| 26 | Türkiye'nin ilk dijital bankası Hayat Finans oldu | Capital | n.c. | TR | https://www.capital.com.tr/haberler/tum-haberler/turkiyenin-ilk-dijital-bankasi-hayat-finans-oldu |
| 27 | BDDK TOM Katılım Bankası'nın kuruluşunu onayladı | Ekonomist | n.c. | TR | https://www.ekonomist.com.tr/haberler/bddk-tom-katilim-bankasinin-kurulusunu-onayladi-pozitif-varlik-yonetime-izin-verdi-34010 |
| 28 | BDDK'dan üç yeni banka kuruluşuna izin | Diken | n.c. | TR | https://www.diken.com.tr/?p=1432356 |
| 29 | Uzaktan kimlik tespiti… yönetmelik yayımlandı | Erdem & Erdem | 2021 | TR | https://www.erdem-erdem.av.tr/bilgi-bankasi/bankalarca-kullanilacak-uzaktan-kimlik-tespiti-yontemlerine-ve-elektronik-ortamda-sozlesme-iliskisinin-kurulmasina-iliskin-yonetmelik-yayimlandi |
| 30 | BDDK'dan yeni karar: tüzel kişiler de uzaktan… | Ekonomist | n.c. | TR | https://www.ekonomist.com.tr/haberler/bddkdan-yeni-karar-tuzel-kisiler-de-uzaktan-kimlik-tespiti-yoluyla-banka-musterisi-olabilecek-34536 |
| 31 | Garanti BBVA WhatsApp | Garanti BBVA | n.c. | TR | https://www.garantibbva.com.tr/dijital-bankacilik/garanti-bbva-whatsapp |
| 32 | Yapı Kredi WhatsApp hizmeti (news) | Yapı Kredi | n.c. | TR | https://www.yapikredi.com.tr/yapi-kredi-hakkinda/haberler/detay/134685 |
| 33 | Bankalar cumartesi günleri açık olacak… | hisse.net | 10.03.2026 (unverified claim) | TR | https://www.hisse.net/haber/bankalar-cumartesi-gunleri-acik-olacak-tbmm-onayladi-iste-yeni-calisma-saati-duzenlemesi-63727 |
| 34 | Bankalar cumartesi günü çalışacak mı? 2026… | Karar | 2026 | TR | https://www.karar.com/guncel-haberler/bankalar-cumartesi-gunu-calisacak-mi-2026-banka-calisma-saatleri-ve-2034997 |
| 35 | What we cover | FSCS | current | UK | https://www.fscs.org.uk/what-we-cover/ |
| 36 | PS24/25 – Depositor protection | Bank of England / PRA | Nov 2025 | UK | https://www.bankofengland.co.uk/prudential-regulation/publication/2025/november/depositor-protection-policy-statement |
| 37 | FSCS welcomes higher deposit protection limit of £120,000 | FSCS | Nov 2025 | UK | https://www.fscs.org.uk/media/press/2025/nov/fscs-welcomes-higher-deposit-protection-limit-of-120000--giving-people-confidence-their-money-is-protected/ |
| 38 | Understanding Deposit Insurance | FDIC | updated 01.04.2024 | US | https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance |
| 39 | Deposit Guarantee Schemes data | EBA | current | EU | https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/depositor-protection/deposit-guarantee-schemes-data |
| 40 | New rules to address bank failures… | European Parliament | 26.03.2026 | EU | https://www.europarl.europa.eu/news/en/press-room/20260323IPR38827/new-rules-to-address-bank-failures-protecting-taxpayers-and-depositors |
| 41 | EU Resolution Framework Reform (CMDI) | Lexology | 2026 | EU | https://www.lexology.com/library/detail.aspx?g=94d43f9c-4c63-43d2-ba59-07c2adfffb39 |
| 42 | Core banking | Wikipedia | current | INT | https://en.wikipedia.org/wiki/Core_banking |
| 43 | What Is a Bank Ledger? | SDK.finance | n.c. | INT | https://sdk.finance/blog/what-is-a-ledger-in-banking-and-fintech-a-complete-guide/ |
| 44 | Core banking system (glossary) | Spark | n.c. | INT | https://www.spark.money/glossary/core-banking-system |
| 45 | Authorisation holds | Adyen Docs | current | INT | https://docs.adyen.com/issuing/payment-stages/authorisation-holds.md |
| 46 | Card payment lifecycle | Increase | current | INT | https://www.increase.com/documentation/card-payment-lifecycle |
| 47 | The payment lifecycle explained | PaymentExpert | 02.03.2026 | INT | https://paymentexpert.com/2026/03/02/the-payment-lifecycle-explained/ |
| 48 | CPMI Glossary – value date | BIS CPMI | current | INT | https://www.bis.org/committees/cpmi/glossary?selection=71 |
| 49 | PSD2 Art. 78 (receipt of payment orders) | legislation.gov.uk (Dir. 2015/2366) | — | EU | https://www.legislation.gov.uk/eudr/2015/2366/article/78 |
| 50 | PSD2 Art. 83 (execution time) | legislation.gov.uk | — | EU | https://www.legislation.gov.uk/eudr/2015/2366/article/83 |
| 51 | PSD2 Art. 87 (value date and availability) | legislation.gov.uk | — | EU | https://www.legislation.gov.uk/eudr/2015/2366/article/87 |
| 52 | FAST işlem limiti 300 bin TL'ye yükseliyor | Webrazzi | 24.08.2026 | TR | https://webrazzi.com/2026/08/24/fast-islem-limiti-300-bin-tlye-yukseliyor/ |
| 53 | TCMB FAST işlem limitini artırdı | Bloomberg HT | Aug 2026 | TR | https://www.bloomberght.com/tcmb-fast-islem-limitini-artirdi-3786250 |
| 54 | EFT saatleri (aggregator) | Enuygun Finans | n.c. | TR | https://www.enuygunfinans.com/finans-rehberi/eft-saatleri-bankalarda-eft-saat-kaca-kadar-yapilir/ |
| 55 | FedNow – About | Federal Reserve Board | current | US | https://www.federalreserve.gov/paymentsystems/FedNow_about.htm |
| 56 | FedNow Service instant payments | FRB Services | 01.08.2023 | US | https://frbservices.org/news/fed360/issues/080123/fednow-service-instant-payments |
| 57 | Instant Payments Regulation | Bird & Bird | 2024 | EU | https://www.twobirds.com/en/insights/2024/global/instant-payments-regulation |
| 58 | Kredili Mevduat Hesabı – KMH Nedir? (aggregator) | HesapKurdu | n.c. | TR | https://www.hesapkurdu.com/ihtiyac-kredisi/rehber/kredili-mevduat-hesabi-kmh-nedir |
| 59 | KMH faizi nedir | Habertürk | n.c. | TR | https://www.haberturk.com/kmh-faizi-nedir-kmh-faizi-nasil-hesaplanir-2741095 |
| 60 | Ortak Hesap Nedir? | İş Bankası | 27.12.2024 | TR | https://www.isbank.com.tr/blog/ortak-hesap-nedir |
| 61 | Ortak Hesap Hakkında Bilmeniz Gereken 8 Detay | Akbank | n.c. | TR | https://www.akbank.com/blog/ortak-hesap-hakkinda-bilmeniz-gereken-8-detay |
| 62 | Emekli promosyon taahhütnamesi | Ziraat Bankası | form (n.c.) | TR | https://www.ziraatbank.com.tr/tr/Forms/emekli_promosyon_taahhutname__39C78.pdf |
| 63 | Directive 2014/92/EU (PAD) Art. 17 | legislation.gov.uk | — | EU | https://www.legislation.gov.uk/eudr/2014/92/article/17 |
| 64 | PAD summary | EUR-Lex | — | EU | https://eur-lex.europa.eu/summary/EN/090406_1 |
| 65 | Nakit döviz çekiminden alınan komisyon kaldırıldı | Habertürk | 2020 | TR | https://www.haberturk.com/nakit-doviz-cekiminden-alinan-komisyon-kaldirildi-2782038-ekonomi |
| 66 | Troy–Discover agreement | Electronic Payments International | n.c. | TR/INT | https://www.electronicpaymentsinternational.com/?p=46712 |
| 67 | TROY nedir, neden kuruldu… | CNBC-e | n.c. | TR | https://www.cnbce.com/fintech/troy-nedir-neden-kuruldu-sahibi-kim-troyun-pazar-payi-ne-h8585 |
| 68 | Ters İbraz (Chargeback) Nedir… | İş Bankası | 08.08.2024 | TR | https://www.isbank.com.tr/blog/ters-ibraz-chargeback-nedir-ve-basvurusu-nasil-yapilir |
| 69 | Provizyon Bekleyen Ödeme Ne Demek? | Akbank | 11.07.2025 | TR | https://www.akbank.com/blog/provizyon-bekleyen-odeme-ne-demek |
| 70 | IBAN Nedir? Nasıl Öğrenilir? | Yapı Kredi | n.c. | TR | https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/iban-nedir-nasil-ogrenilir |
| 71 | TCMB IBAN Tebliği (copy) | Halkbank | 2008 | TR | https://www.halkbank.com.tr/content/dam/halkbank/tr/dokumanlar/bireysel/iban_tebligi.pdf |
| 72 | ISO 9362 | Wikipedia | current | INT | https://en.wikipedia.org/wiki/ISO_9362 |
| 73 | BIC and SWIFT codes | Stripe | n.c. | INT | https://stripe.com/en-cn/resources/more/swift-code-and-bic |
| 74 | How much does receiving a SWIFT transfer cost? | Qonto | n.c. | EU | https://support-es.qonto.com/hc/en-us/articles/23951014100753 |
| 75 | Difference between payments, transfers, standing orders, Direct Debits and CPAs | Barclays | n.c. | UK | https://barclays.co.uk/help/payments/payment-information/difference-order-debits |
| 76 | The Direct Debit Guarantee | Bacs / directdebit.co.uk | n.c. | UK | https://www.directdebit.co.uk/direct-debit-explained/direct-debit-guarantee/ |
| 77 | Direct debits, standing orders and other regular payments | Which? | n.c. | UK | https://www.which.co.uk/money/banking/banking-security-and-payment-methods/direct-debits-and-standing-orders-explained-aU1tE5d00CI5 |
| 78 | Difference between a loan interest rate and the APR | CFPB | reviewed 28.08.2026 | US | https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/ |
| 79 | Kredi Nasıl Hesaplanır? | Yapı Kredi | 05.03.2026 | TR | https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/kredi-nasil-hesaplanir-adim-adim-kredi-hesaplama-rehberi |
| 80 | BSMV Nedir, Nasıl Hesaplanır? (aggregator) | HesapKurdu | n.c. | TR | https://www.hesapkurdu.com/ihtiyac-kredisi/rehber/bsmv-nedir-nasil-hesaplanir |
| 81 | KKDF Nedir? (aggregator) | HesapKurdu | n.c. | TR | https://www.hesapkurdu.com/ihtiyac-kredisi/rehber/kaynak-kullanimi-destekleme-fonu-nedir |
| 82 | KKB 2022 Faaliyet Raporu | KKB | 2023 | TR | https://www.kkb.com.tr/Resources/ContentFile/2125/01kkbfrat2022.pdf |
| 83 | Findeks Kredi Notu Nedir? | Yapı Kredi | 31.03.2026 | TR | https://www.yapikredi.com.tr/blog/surdurulebilirlik/finansal-okuryazarlik/detay/findeks-kredi-notu-nedir |
| 84 | Buy now pay later: new rules come into force | Wiggin | 2026 | UK | https://wiggin.co.uk/insight/buy-now-pay-later-new-rules-come-into-force/ |
| 85 | FCA publishes new proposals for BNPL regulation | Skadden | July 2025 | UK | https://www.skadden.com/insights/publications/2025/07/fca-publishes-new-proposals |
| 86 | New Consumer Credit Directive | Taylor Wessing | June 2025 | EU | https://www.taylorwessing.com/zh-hant/insights-and-events/insights/2025/06/new-consumer-credit-directive |
| 87 | Mapping EU legislation: CCD2 | Vixio | n.c. | EU | https://vixio.com/insights/pc-mapping-eu-legislation-directive-eu-20232225-consumer-credit |
| 88 | Regulation (EU) 2019/518 | legislation.gov.uk | — | EU | https://www.legislation.gov.uk/eur/2019/518/contents/data.html |
| 89 | Regulation (EU) 518/2019 FAQs | Piraeus Bank | n.c. | EU | https://piraeusbank.gr/en/idiwtes/kartes/faqs-kartes-xrewseis-metatropis-nomismatwn |
| 90 | Yatırım fonlarına uygulanan stopaj düzenlemesi | İş Portföy | 2025 | TR | https://www.isportfoy.com.tr/medya-ve-blog/yatirim-fonlarina-uygulanan-stopaj-duzenlemesi-hakkinda |
| 91 | Para piyasası fonlarında stopaj %10'a yükseltildi | Yeni Alanya | 2026 | TR | https://www.yenialanya.com/para-piyasasi-fonlarinda-stopaj-yuzde-10a-yukseltildi-kimleri-kapsiyor |
| 92 | Current balance vs available balance | Citi | n.c. | US | https://www.citi.com/banking/personal-banking-guide/basic-finance/current-balance-vs-account-balance |
| 93 | MASAK blokesi – icra haczi farkı | Hukukçular Evi (law blog) | n.c. | TR | https://hukukcularevi.com/masak-blokesi-icra-haczi-farki-oncelik-siralamasi/ |
| 94 | Şikayetvar complaint pages (Enpara hesap/avukat; Enpara mesaj geldi; bloke/paramı çekemiyorum; Enpara icra; VakıfBank yurt dışı) | Şikayetvar (anecdotal) | 2025–2026 | TR | https://www.sikayetvar.com/enpara/hesap/avukat?page=2 ; https://www.sikayetvar.com/enpara/hesap/mesaj-geldi?page=2 ; https://www.sikayetvar.com/bloke/parami-cekemiyorum ; https://www.sikayetvar.com/enpara/hesap/icra?page=3 ; https://www.sikayetvar.com/vakifbank/kredi-karti-yurt-disina |
| 95 | Tebliğ 2020/7 kapsamında ücretlendirilebilecek ürün ve hizmetler (izahname) | TKBB | 2020 | TR | https://www.tkbb.org.tr/upload/TKBB_2020_7_Sayili_Teblig_Kapsaminda_Ucretlendirilebilecek_Urun_ve_Hizmetlere_iliskin_izahname-revize%20%281%29.pdf |
| 96 | Finansal Tüketicilerden Alınacak Ücretlere İlişkin… Yönetmelik | Lexpera | 2020 | TR | https://www.lexpera.com.tr/mevzuat/yonetmelikler/finansal-tuketicilerden-alinacak-ucretlere-iliskin-usul-ve-esaslar-hakkinda-yonetmelik |
| 97 | Directive 2014/65/EU (MiFID II) | EUR-Lex | 2014 (consolidated) | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065 |
| 98 | PS25/22 – Targeted support | FCA | 11.12.2025; final 26.02.2026; live 06.04.2026 | UK | https://www.fca.org.uk/publications/policy-statements/ps25-22-supporting-consumers-pensions-investment-decisions-rules-targeted-support |
| 99 | Uyarı Notu | İş Yatırım | n.c. | TR | https://www.isyatirim.com.tr/tr-tr/urunler/Sayfalar/uyari-notu.aspx |
| 100 | Yasal Uyarı | TEB Portföy | n.c. | TR | https://www.tebportfoy.com.tr/yasal-uyari |
| 101 | Yasal Uyarı | Yatırım Finansman | n.c. | TR | https://www.yf.com.tr/yasal-uyari |
| 102 | Yatırım Hizmetleri ve Faaliyetleri ile Yan Hizmetler (III-37.1.c) | Alomaliye | 07.04.2022 | TR | https://www.alomaliye.com/2022/04/07/yatirim-hizmetleri-ve-faaliyetleri-ile-yan-hizmetler-iii-37-1-c/ |
| 103 | SPK al-sat sinyallerine dair notice | QNB Invest | n.c. | TR | https://www.qnbinvest.com.tr/forex/duyuru/spk-al-sat-sinyallerine-dair-tebligi |
| 104 | MASAK compliance-programme amendment (25.12.2024) and AML regulation change (22.08.2025; scope not verified) | Alomaliye | 25.12.2024; 22.08.2025 | TR | https://www.alomaliye.com/2024/12/25/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesi-uyum-degisiklik-25-12-2024/amp/ ; https://www.alomaliye.com/2025/08/22/suc-gelirlerinin-aklanmasinin-ve-terorun-finansmaninin-onlenmesi-22-08-2025/ |
| 105 | AML policy (Türkçe) | TOM Bank | n.c. | TR | https://www.tombank.com.tr/assets/images/doc/AML_tr.pdf |
| 106 | Nüfuz sahibi kişilerin finansal işlemlerine tedbir | İstiklal | 17.11.2022 | TR | https://www.istiklal.com.tr/ekonomi/nufuz-sahibi-kisilerin-finansal-islemlerine-tedbir-722638h |
| 107 | MASAK introduced the definition of PEPs with Communiqué No. 21 | Mondaq | 2022 | TR | https://www.mondaq.com/turkey/white-collar-crime-anti-corruption-fraud/1253060/masak-introduced-the-definition-of-politically-exposed-persons-with-communique-no-21 |
| 108 | FATF Guidance: PEPs (Recs 12 and 22) | FSB (FATF document) | 2013 | INT | https://www.fsb.org/2013/06/fatf-guidance-politically-exposed-persons-recommendations-12-and-22/ |
| 109 | Proceeds of Crime Act 2002 s.333A | legislation.gov.uk | — | UK | https://www.legislation.gov.uk/ukpga/2002/29/section/333A/data.htm |
| 110 | Tipping off and prejudicing an investigation | The Law Society | n.c. | UK | https://www.lawsociety.org.uk/topics/anti-money-laundering/tipping-off-a-client |
| 111 | 31 CFR 1020.320 (SAR rule for banks) | eCFR | current | US | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320 |
| 112 | 12 CFR 21.11 (SAR confidentiality) | Cornell LII | current | US | https://www.law.cornell.edu/cfr/text/12/21.11 |
| 113 | Final Report: Guidelines on internal governance (EBA/GL/2021/05) | EBA | 02.07.2021 | EU | https://www.eba.europa.eu/sites/default/files/document_library/Publications/Guidelines/2021/1016721/Final%20report%20on%20Guidelines%20on%20internal%20governance%20under%20CRD.pdf |
| 114 | Mevduat faizi ne kadar oldu… (press, Oct 2026) | Kırşehir Çiğdem | Oct 2026 | TR | https://www.kirsehircigdem.com/mevduat-faizi-ne-kadar-oldu-500-bin-1-milyon-ve-2-milyon-tl-ne-kadar-kazandiriyor |
| 115 | Dijital banka kurmak için başvuru sayısı 35'i aştı | Para Dergi | 13.04.2023 | TR | https://www.paradergi.com.tr/finans/2023/04/13/dijital-banka-kurmak-icin-basvuru-sayisi-35i-asti |

---

## Open questions, unverified items and items needing institution-specific confirmation

**Unverified or conflicting facts**
1. **Saturday branch opening (TR, March 2026):** press claims parliamentary approval of a 09:00–13:00 Saturday model at selected branches. No law number or BDDK/TBB source was found, so do not use it until it is verified.
2. **EFT system hours and bank cut-offs:** only aggregator sources were found. Verify TCMB EFT hours and each bank's cut-offs for EFT and SWIFT by currency.
3. **Papara:** confirm the TCMB licence cancellation (reported for 31.10.2025) and the refund process from TCMB/TMSF primary notices.
4. **EU CMDI:** confirm the OJ publication date (reported 20.04.2026) and exact application dates on EUR-Lex.
5. **UK FSCS and EU DGSD:** the temporary-high-balance limit after PS24/25 and the DGSD 7-working-day payout were not captured.
6. **Findeks bands:** Yapı Kredi (31.03.2026) bands conflict with other online summaries. Confirm on findeks.com.
7. **Consumer-loan BSMV:** 15% (Kuveyt Türk 2026, multiple sources) vs Yapı Kredi's example labelling "%5". Confirm with the bank's tax team.
8. **0.2% BSMV scope:** whether it applies to card FX spending or to FX transfers without conversion.
9. **2026 money-market-fund withholding change:** obtain the Presidential Decision text and date.

**Rules not researched in depth (belong to other researchers)**

10. **Current [periodic] figures** (researchers 06/09):
    - TCMB maximum rates for credit cards and KMH;
    - current minimum-payment percentages and thresholds;
    - FAST limit after 26.08.2026 (monitor);
    - TMSF limit for 2027.
11. **SPK:** the exact III-37.1 text separating "yatırım danışmanlığı" from general commentary, and whether deposit banks may advise directly or must route customers to affiliates.
12. **Recurring payments in TR:** legal revocation and refund rights for recurring card payments and bill auto-pay under the TCMB 2021 payment-services regulation (researchers 02/07).
13. **Credit-linked insurance rules in TR** (free choice of insurer, refunds on early repayment) (researcher 09).
14. **Lost/stolen card liability:** whether the 150 TL nominal cap in Law 5464 Art. 12 has been updated in effect (researchers 06/10).
15. **TCMB fee regulation:** exact Official Gazette dates of the 2020 regulation and Communiqué 2020/7, and current caps (researchers 02/09).
16. **US rules:** Regulation Best Interest / FINRA suitability not verified (researcher 03).
17. **EU AMLR/AMLA timelines:** not covered (researcher 03).
18. **Cheque clearing (takas) in TR** and the treatment of uncleared funds (researchers 05/07).
19. **YUVAM accounts:** status in 2026; FATSİ maturity end dates.

**Confirm with the client institution**

20. **Institution-specific confirmations** (verify against the institution's internal procedure):
    - channel capability matrix (§5);
    - team names, SLAs and escalation routing (§16);
    - which data the agent may disclose about icra files;
    - minors' account rules;
    - efektif withdrawal fees and notice periods;
    - netting of salary credits against KMH;
    - weekend and holiday due-date handling;
    - pension/salary promotion protocols;
    - how digital brands map to licences (TMSF limit sharing).
21. **No public Turkish source** describing bank contact-centre tiering (L1/L2) was found. The role table is a practice model to be validated.
22. **No statutory Turkish equivalent** of the EU basic payment account was found in the sources reviewed.
