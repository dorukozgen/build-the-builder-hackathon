# EU, UK and US rules and supervisory expectations shaping retail-banking customer support (status as of 10 October 2026) — Researcher 03

**Scope.** Consumer rights and firm obligations that determine how a support agent (human or AI) must handle unauthorised transactions, payment errors/misdirected payments, APP fraud, card disputes, complaints, vulnerable customers, accessibility, data protection, AML confidentiality, collections/forbearance and AI/chatbot use, in the EU, UK and US, for later comparison with Türkiye (Türkiye column left blank for researcher 02's material).

**Legend used throughout.**
- Jurisdiction: **[EU]**, **[UK]**, **[US]**, **[INTL]** (card schemes, PCI SSC), **[CA-BC]** (British Columbia tribunal), **[TR-context]**.
- Statement type: **(1)** law/regulation · **(2)** supervisory guidance / regulator statement · **(3)** industry practice / scheme rule · **(4)** recommended service practice (my inference for the playbook) · **(5)** assumption or item needing verification.
- Status: **IN FORCE** · **ADOPTED – NOT YET APPLICABLE** · **AGREED – NOT ADOPTED** · **PROPOSED** · **WITHDRAWN**.
- All URLs accessed 10 Oct 2026. Article/section numbers are cited only where I read them in the official text this session (EUR-Lex, Council register, legislation.gov.uk, FCA Handbook, eCFR API, Cornell LII for US Code/UCC text, CRT decision PDF); otherwise flagged (5).
- Baseline safety rule for every scenario (4): the agent never requests PINs, full passwords, CVV/CVC, one-time codes, remote access or the disabling of security controls. This is consistent with the user's duty to keep credentials safe and the PSP's duty to keep them inaccessible to others ([PSD2 Art. 69–70](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)), with PCI rules on card security codes ([PCI SSC FAQ 1210](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/are-audio-voice-recordings-permitted-to-contain-sensitive-authentication-data/)), and with the US anti-pretexting statute ([15 U.S.C. 6821](https://www.law.cornell.edu/uscode/text/15/6821)).

---

## 1. Unauthorised payment transactions and payer liability (PSD2 / UK PSRs 2017 / Reg E / Reg Z / card schemes)

### Takeaway
In the EU and UK, the payer's bank must refund an unauthorised payment by the end of the next business day, with only a narrow exception for suspected fraud. The payer's liability is capped at €50 in the EU and £35 in the UK unless they acted fraudulently or with intent or gross negligence. The outer limit for notifying the bank is 13 months, and the bank carries the burden of proof: an authentication log on its own does not prove that the customer authorised the payment or was grossly negligent.

In the US, Reg E sets liability by how quickly the customer reported: $50, $500, or unlimited for transfers after the 60-day statement window. It also runs a strict error-resolution clock (10 business days, or provisional credit and up to 45 or 90 days), and the customer's negligence plays no part. For credit cards, Reg Z adds a $50 cap and a separate *written* billing-error procedure. Card-scheme "zero liability" is a promise made by the scheme, not law.

### Cited Findings
**[EU] (1) IN FORCE — PSD2 (Directive (EU) 2015/2366)**
- Art. 71(1): the user obtains rectification only if they notify the bank "without undue delay" and "no later than 13 months after the debit date". The time limit does not apply if the bank failed to provide the transaction information. — [PSD2, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- Art. 72: if the user denies authorising a payment, the bank must prove it was authenticated, accurately recorded and unaffected by a technical breakdown. "The use of a payment instrument recorded by the payment service provider … shall in itself not necessarily be sufficient" to prove authorisation, fraud or gross negligence, and the bank "shall provide supporting evidence". — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- Art. 73(1): refund "immediately, and in any event no later than by the end of the following business day" after noting or being notified. The only exception is where the bank "has reasonable grounds for suspecting fraud and communicates those grounds to the relevant national authority in writing". The bank must also restore the account and backdate the value date. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- Art. 74(1): the payer may bear up to **EUR 50** for a lost, stolen or misappropriated instrument. This does not apply if the loss was not detectable before the payment, or was caused by the bank's staff, agents, branches or outsourcers. The payer bears **all** losses if they acted fraudulently or breached Art. 69 with intent or gross negligence. Member States may reduce the cap.
- Art. 74(2): if the bank does not require strong customer authentication (SCA), the payer bears no loss unless they acted fraudulently.
- Art. 74(3): the payer bears no loss after notification, except for fraud. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- Art. 69: the user must use the instrument according to its terms, notify loss or theft without undue delay, and "take all reasonable steps to keep its personalised security credentials safe".
- Art. 70: the bank must ensure credentials are not accessible to others, provide means at all times to report a lost or stolen instrument (and, on request, proof of that report for 18 months), make reporting free of charge, and prevent use after the report. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- Payee-initiated payments, including direct debits:
  - Art. 77(1): the payer may request a refund for 8 weeks from the debit.
  - Art. 76(1): for SEPA direct debits the refund right is unconditional.
  - Art. 76(2): within 10 business days the bank must refund or justify its refusal and name the bodies the payer can take the matter to. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)

**[UK] (1) IN FORCE — Payment Services Regulations 2017 (SI 2017/752)**
- reg 74(1): redress only if the customer notifies without undue delay, and in any event within 13 months of the debit date. — [legislation.gov.uk reg 74](https://www.legislation.gov.uk/uksi/2017/752/regulation/74)
- reg 75(3): the recorded use of a payment instrument "is not in itself necessarily sufficient" to prove authorisation. — [reg 75](https://www.legislation.gov.uk/uksi/2017/752/regulation/75)
- reg 76(2): refund "as soon as practicable, and in any event no later than the end of the business day following the day on which it becomes aware".
- reg 76(3) exception: the bank has reasonable grounds to suspect the *customer's* fraudulent behaviour and notifies, in writing, "a person mentioned in section 333A(2)" of the Proceeds of Crime Act 2002. — [reg 76](https://www.legislation.gov.uk/uksi/2017/752/regulation/76)
- reg 77(1): payer liability up to **£35**.
- reg 77(2): the same carve-outs as the EU (loss not detectable; caused by the bank's staff or agents).
- reg 77(3): all losses if the payer acted fraudulently or with intent or gross negligence.
- reg 77(4): no liability (absent fraud) after notification; where the bank gave no means to notify; where SCA was required but not applied; or for distance contracts other than excepted contracts. — [reg 77](https://www.legislation.gov.uk/uksi/2017/752/regulation/77)

**[US] (1) IN FORCE — Regulation E (12 CFR 1005), consumer accounts and debit cards**
- §1005.6(b)(1): if the consumer notifies within **two business days** of learning of a lost or stolen access device, liability is capped at the lesser of **$50** or the transfers made before notice.
- §1005.6(b)(2): if notice is later, the cap is **$500**, under a defined formula.
- §1005.6(b)(3): the consumer must report an unauthorised transfer shown on a statement **within 60 days** of the statement being sent. Otherwise they are liable for later transfers that the bank shows would not have happened with timely notice.
- §1005.6(b)(4): the bank must extend these time limits for extenuating circumstances.
- §1005.6(b)(5): notice may be given in person, by phone or in writing. Constructive notice applies when the bank becomes aware of the circumstances.
- §1005.6(b)(6): lower liability set by state law or by agreement prevails. — [eCFR §1005.6](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.6)
- §1005.11, the error-resolution procedure:
  - **What counts as an "error":** unauthorised EFTs, incorrect EFTs, omissions, computational errors, and more. Routine balance enquiries do not count.
  - **Customer's notice:** must be received within 60 days of the statement. The bank may require written confirmation within 10 business days of an oral notice, but only if it tells the consumer this, and the address, at the time of the oral notice.
  - **Investigation clock:** determine whether an error occurred within **10 business days**, report the result within 3 business days, and correct an error within 1 business day.
  - **Extension to 45 days:** allowed only if the bank **provisionally credits** the account within 10 business days. It may withhold up to $50 for unauthorised EFTs. It must notify the provisional credit within 2 business days and give full use of the funds.
  - **Longer windows:** 20 business days instead of 10 for new accounts (first deposit within 30 days). **90 days** instead of 45 for transfers not initiated within a state, point-of-sale debit-card transactions, and new accounts.
  - **If the bank finds no error:** it must give a written explanation and the right to request the documents relied on. Before reversing a provisional credit it must give notice and honour items for 5 business days. — [eCFR §1005.11](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11)
- CFPB EFT FAQs (2) (several answers updated 4 Jun 2021 / 13 Dec 2021; page includes a 15 Jan 2025 update):
  - A bank may **not** require a police report or other documentation as a condition of starting an investigation.
  - The consumer's negligence "cannot be used as the basis for imposing greater liability" (Comment 6(b)-2).
  - A consumer "fraudulently induced into providing account information has not furnished an access device". Transfers made by a bank impersonator who tricked the consumer into giving login details or a texted code are **unauthorised EFTs**.
  - A credit-push P2P transfer initiated by a fraudster with credentials obtained by fraudulent inducement is an unauthorised EFT. — [CFPB EFT FAQs](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/)
- These FAQs do **not** appear on the CFPB's Withdrawn Guidance list (page last modified 22 Jul 2026). — [CFPB Withdrawn Guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/)

**[US] (1) IN FORCE — Regulation Z (12 CFR 1026), credit cards (Fair Credit Billing Act)**
- §1026.12(b): unauthorised-use liability is capped at the lesser of **$50** or the amount obtained before notification. Notification may be in person, by phone or in writing.
- §1026.12(c): claims and defences against the card issuer, subject to a $50 transaction threshold and a same-state or 100-mile condition. — [eCFR §1026.12](https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.12)
- §1026.13, billing errors:
  - The billing-error notice must be **written**, sent to the address the creditor disclosed, and received **within 60 days** after the first statement showing the error.
  - The creditor must acknowledge within 30 days and resolve within **2 complete billing cycles, and in no event later than 90 days**.
  - Pending resolution, the consumer need not pay the disputed amount, the creditor may not collect it, and no adverse credit reporting is allowed. — [eCFR §1026.13](https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.13)

**[INTL] (3) Card-scheme policy, not law**
- Visa (US page): "Zero Liability" means the cardholder "won't be held responsible for unauthorized charges". It excludes certain commercial and anonymous prepaid cards and transactions not processed by Visa. Issuers must replace funds "within five business days of notification", on a provisional basis that may be withheld for gross negligence, fraud or delayed reporting. — [Visa Zero Liability](https://www.visa.com/en-us/personal/security/zero-liability-policy.html)

**[EU] AGREED – NOT ADOPTED: PSD3 / Payment Services Regulation (PSR)** — Council compromise text ST 8221/26 (April 2026); article numbers may change.
- Art. 56(1): the refund deadline remains the end of the following business day.
- Art. 56(2): where the bank has "objectively justified reasons" to suspect fraud or gross negligence and communicates those grounds to the payer in writing, it has **15 business days** to refund or justify the refusal and name the dispute-resolution bodies.
- Art. 54: the notification limit is extended to **18 months**.
- Art. 55(2a): before concluding gross negligence, the bank must invite the user to explain the events, and silence alone is not proof.
- Art. 60(1): the €50 cap is retained.
- Art. 60(2): the payer bears no loss where an SCA exemption was applied.
- Art. 53(1)(c): free **human support** for reporting and unblocking, at least during business hours, in an official language. — [Council ST 8221/26](https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf)

### Inferences (practical consequences for the agent)
- (4) **Timestamp the first notification**, whatever the channel or wording, because several clocks start from it:
  - EU and UK: refund deadline at end of the next business day.
  - US: 10-business-day investigation and provisional-credit clock.
  - US: if the bank requires written confirmation of an oral notice, the agent must say so and give the address on that same contact.
- (4) **Never** tell a customer "you're liable because it was your card/PIN/OTP", and never require proof such as a police report before opening a claim. In the EU and UK the bank bears the burden of proof. In the US, negligence cannot increase liability and a police report cannot be a precondition.
- (4) **Classify early**, because the regime differs:
  - unauthorised (fraudster-initiated, including credentials obtained by deception: Reg E unauthorised; EU/UK unauthorised);
  - authorised but induced (APP: see §2);
  - incorrectly executed;
  - merchant dispute (scheme chargeback, Reg Z claims and defences).
- (4) **US credit-card disputes:** the bank may take disputes by phone as a policy, but the agent should tell the customer that the statutory FCBA billing-error rights depend on a **written** notice within 60 days. Do not imply that a phone call alone preserves those rights.
- (4) **Card-scheme timelines** (e.g. Visa's 5 business days) are scheme commitments. Present them as bank or scheme policy, never as legal rights, and do not promise chargeback outcomes.

### Gaps
- National PSD2 transposition details are not covered: Member-State reductions of the €50 cap, and which body is the "relevant national authority" under Art. 73.
- The UK SCA-RTS (FCA) exemption thresholds were not re-checked this session.
- Visa or Mastercard scheme-rule documents (as opposed to consumer pages) were not reviewed.

---

## 2. Misdirected payments, payee verification and APP fraud (incl. PSD3/PSR status)

### Takeaway
- **Wrong account details entered by the customer:** in both the EU and UK the bank is not liable for executing a payment to the wrong unique identifier, but must make reasonable efforts to recover the money. The payee's bank must cooperate, and on written request the payer gets the information needed to sue.
- **[EU] Verification of Payee (VoP):** mandatory for euro credit transfers since **9 Oct 2025** for banks in euro-area Member States, and from **9 Jul 2027** for banks in non-euro Member States. The bank must refund if it failed to run the check.
- **[UK] APP fraud:** the UK leads with *mandatory* reimbursement since **7 Oct 2024**. The cap is £85,000, the claim window 13 months, and the payout is due within 5 business days, extendable ("stop the clock") to 35. The PSR's functions are moving into the FCA through a Bill introduced in May 2026.
- **[EU] PSD3/PSR:** the new regime (VoP for all credit transfers; full refund for bank-impersonation fraud) is **agreed but not adopted**. OEIL shows "Awaiting Council's 1st reading position", with an indicative plenary date of **14 Dec 2026**.
- **[US] No federal right** to reimbursement for scams the customer authorised. Reg E covers fraudster-initiated transfers, including those using credentials obtained by deception. Scam liability is being fought out in state enforcement (NY AG v. Zelle operator: motion to dismiss denied 20 Jul 2026).

### Cited Findings
**[EU] (1) IN FORCE — PSD2 Art. 88** (incorrect unique identifier)
- A payment executed in accordance with the unique identifier is deemed correctly executed.
- The bank is not liable under Art. 89 if the identifier was wrong, but "shall make reasonable efforts to recover the funds". The payee's bank "shall cooperate … by communicating … all relevant information".
- If recovery is impossible, the payer's bank must provide, "upon written request", all available information relevant to filing a legal claim. It may charge for recovery if the framework contract allows.
- Art. 88(5): extra information supplied (such as the payee name) does not extend liability under PSD2 alone. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)

**[EU] (1) IN FORCE — Instant Payments Regulation (EU) 2024/886**, inserting Art. 5c into Reg. 260/2012
- The payer's bank must offer VoP for **credit transfers** (instant and non-instant euro transfers):
  - it runs the check immediately after the payee details are entered and before authorisation;
  - it runs on every channel;
  - for paper orders, it runs on receipt if the payer is present. — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886)
- Possible results:
  - **Mismatch:** the payer is told that authorising "might lead to transferring the funds to a payment account not held by the payee".
  - **Almost match:** the bank shows the payer "the name of the payee associated with" the account.
  - **Payer's choice:** the check must not prevent the payer from authorising.
  - **Business opt-out:** non-consumers may opt out for bulk orders.
  - **Explaining consequences:** banks must explain the liability and refund implications of ignoring a notification. — [Art. 5c(1),(5)–(7)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886)
- Art. 5c(8):
  - A bank that complied is not liable under PSD2 Art. 88 for a transfer to an unintended payee.
  - If the payer's bank failed to perform VoP and that caused a defective execution, it "shall without delay refund the payer". If the failure was the payee's bank's, that bank must compensate the payer's bank.
- Art. 5c(9): compliance deadlines are **9 Oct 2025** (euro-area Member States) and **9 Jul 2027** (non-euro Member States). — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886)
- Related provisions:
  - Art. 5d: banks offering instant transfers screen their own users against EU targeted financial sanctions at least daily, not transaction by transaction.
  - Art. 5a(6) of Reg. 260/2012 (as inserted by Reg. 2024/886): on the customer's request, the bank must offer a per-day or per-transaction limit on instant transfers, at the customer's sole discretion. — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886)

**[EU] AGREED – NOT ADOPTED — PSD3 + Payment Services Regulation (PSR)**
- **Political agreement, 27 Nov 2025** (EP press release):
  - banks must check that payee name and identifier match;
  - "If a fraudster initiates or changes a transaction, it will be treated as unauthorised";
  - for bank-employee impersonation fraud, the bank "must refund the full amount as long as the customer reports the fraud to the police and informs their PSP";
  - online platforms are liable to banks if they fail to remove fraudulent content they were told about;
  - "users must have access to human customer support (not only chatbots)";
  - all banks must take part in ADR if the consumer chooses it. — [European Parliament press release, 27 Nov 2025](https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees)
- **Council compromise text ST 8221/26** (published 23 Apr 2026):
  - Art. 50 applies the IPR VoP rules "to all credit transfers"; Art. 57 makes a bank that fails VoP refund the payer.
  - Art. 59 (impersonation fraud): applies where a consumer was manipulated by someone "pretending to be the consumer's payment service provider using communication channels attributed to" it. The bank refunds in full if the consumer reported to the bank and to the police without undue delay. Within **15 business days** of notification and the police report, the bank refunds or justifies its refusal. There is no refund for fraud or gross negligence, which the bank must prove after inviting the consumer's account of events.
  - Art. 51(1)–(1c): customer-set spending limits. A **4-hour delay** applies to remote limit increases and remote mobile-app activation (the customer may adjust or opt out).
  - Art. 51(3): reasons for blocking an instrument must be given unless prohibited by law, and the block must be reassessed within 2 business days.
  - Art. 112: application **21 months** after entry into force; Arts 50 and 57 at **27 months**. — [Council ST 8221/26](https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf); [Matheson, 29 Apr 2026](https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/)
- **Procedure status:**
  - OEIL (2023/0210(COD)): ECON approved the text agreed in early second-reading negotiations on **5 May 2026**.
  - Stage: "**Awaiting Council's 1st reading position**". Indicative plenary sitting: **14 Dec 2026**. — [OEIL procedure file](https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD))
- **Discrepancies:**
  - MoFo (30 Apr 2026) says that under the PSR APP fraud generally "will be treated as an unauthorised transfer" with full reimbursement. The official compromise text limits the full-refund rule to impersonation of the customer's *own bank* (Art. 59) and to fraudster-initiated or modified transactions. Prefer the Council text. — [MoFo](https://www.mofo.com/resources/insights/260430-psd3-and-the-payment-services-regulation-key-developments)
  - A search-engine summary cited 18- and 24-month application periods. The official compromise text says 21 and 27 months.

**[UK] (1) IN FORCE — PSRs 2017 reg 90** (incorrect unique identifier)
- Mirrors PSD2 Art. 88: reasonable efforts to recover; the payee's bank must cooperate; information to the payer on written request; a charge only if agreed.
- reg 90(6): nothing in reg 90 affects bank liability under a "relevant requirement" (e.g. PSR directions) where a payment follows fraud or dishonesty. This is the hook for the APP reimbursement rules. — [reg 90](https://www.legislation.gov.uk/uksi/2017/752/regulation/90)

**[UK] (1) IN FORCE since 30 Oct 2024 — outbound payment delay (reg 86(2A)–(2D), inserted by SI 2024/1013)**
- If, by the end of the business day after receipt, the bank establishes reasonable grounds to suspect the order follows "fraud or dishonesty perpetrated by a person other than the payer", it may delay crediting the payee's bank to contact the payer or third parties.
- The delay must be no longer than necessary and **no later than the end of the 4th business day** after receipt.
- The bank must notify the payer of the delay, the reasons, and any information or action needed. It must do so by the end of the business day after receipt, "except to the extent complying … would be otherwise unlawful". — [reg 86](https://www.legislation.gov.uk/uksi/2017/752/regulation/86); [SI 2024/1013](https://www.legislation.gov.uk/uksi/2024/1013/made)

**[UK] (1)/(2) IN FORCE since 7 Oct 2024 — mandatory APP scam reimbursement (PSR)**
- **Scope:** Faster Payments and CHAPS transfers between UK accounts. Covers individuals, micro-enterprises and charities. Credit unions, municipal banks and national savings banks are excluded.
- **Claims:** report within 13 months. Reimbursement is expected "within 5 business days"; stop-the-clock extends to a maximum of **35 business days**.
- **Excess and cap:** optional excess up to **£100**, which cannot be applied to vulnerable consumers. Maximum claim **£85,000**, though firms may pay more. Above that the customer can go to the FOS.
- **Exceptions:** no reimbursement if the customer was complicit or grossly negligent. "Gross negligence is a high bar and this exception does not apply to vulnerable consumers."
- **Excluded case types:** civil disputes and card, cash and cheque payments. — [PSR consumer page](https://www.psr.org.uk/information-for-consumers/app-fraud-reimbursement-protections/)
- **Consumer standard of caution** (guidance, Dec 2023):
  - have regard to specific, directed interventions from the bank or police;
  - report promptly;
  - respond to reasonable and proportionate information requests;
  - consent to police reporting.
  Summary obtained via search of PSR material; full PDF not read. — [PSR consumer standard of caution guidance](https://www.psr.org.uk/media/as3a0xan/sr1-consumer-standard-of-caution-guidance-dec-2023.pdf)
- **Cost split and cap source:** the sending and receiving banks split the cost 50/50; the PSR reduced the cap to £85,000. — [A&O Shearman horizon report 2026](https://www.aoshearman.com/en/insights/financial-services-horizon-report-2026/payment-services-and-payment-systems); [PSR PS24/7](https://www.psr.org.uk/publications/policy-statements/ps247-faster-payments-app-scams-reimbursement-requirement-confirming-the-maximum-level-of-reimbursement/)
- **Outcomes:**
  - £243m reimbursed by end-2025. — [PSR news, 9 Jul 2026](https://www.psr.org.uk/news-and-updates/latest-news/news/fraud-victims-get-243-million-back-as-psr-marks-a-year-of-progress/)
  - Dashboard (updated 30 Jul 2026): 88% (£316m) of money lost reimbursed since Oct 2024; 89% in Q1 2026; 82% of claims resolved within five days; an independent evaluation by Frontier Economics published in Q1 2026. — [PSR APP dashboard](https://www.psr.org.uk/information-for-consumers/app-scams-reimbursement-dashboard/)
- **Confirmation of Payee:** expanded to 350+ more firms by end-Oct 2024. — [PSR consumer page](https://www.psr.org.uk/information-for-consumers/app-fraud-reimbursement-protections/) The PSR fined Bank of Ireland UK in Feb 2026 for missing the CoP deadline. — [PSR news, 9 Jul 2026](https://www.psr.org.uk/news-and-updates/latest-news/news/fraud-victims-get-243-million-back-as-psr-marks-a-year-of-progress/)
- **PSR→FCA consolidation:** "The Financial Services and Markets Bill, introduced to Parliament in May 2026, includes provisions to transfer the PSR's functions to the FCA while preserving their substance and scope." — [PSR news, 9 Jul 2026](https://www.psr.org.uk/news-and-updates/latest-news/news/fraud-victims-get-243-million-back-as-psr-marks-a-year-of-progress/)
- **Dated source:** the PSR consumer page still says the FOS limit is £430,000. The FOS limit from 1 Apr 2026 is £455,000 (see §4). Prefer the FOS source.

**[US] (1) IN FORCE + litigation**
- Regulation E treats fraudster-initiated transfers as unauthorised, including transfers using credentials obtained by deception (CFPB FAQs, above). A transfer the consumer makes themselves after being deceived is "authorized", and federal law gives no reimbursement right for it. — [Forbes, 27 Jul 2026](https://www.forbes.com/sites/zennonkapron/2026/07/27/new-york-is-writing-americas-zelle-fraud-rules-one-lawsuit-at-a-time/) (specialist press; consistent with the Reg E definitions above)
- **Zelle litigation:**
  - The CFPB sued Zelle's operator and three banks in late 2024, then dropped the case in March 2025. — [Washington Post, 14 Sep 2026](https://www.washingtonpost.com/ripple/2026/09/14/ai-is-supercharging-money-scams-heres-what-you-can-do-to-protect-yourself/)
  - In *People of the State of New York v. Early Warning Services* (Index No. 654753/2025, N.Y. Sup. Ct.), the court on **20 Jul 2026** refused to dismiss the AG's deceptive-practices claims over APP fraud on Zelle. This is not a finding of liability. — [Ballard Spahr Consumer Finance Monitor, 31 Jul 2026](https://www.consumerfinancemonitor.com/2026/07/31/new-york-court-refuses-to-dismiss-attorney-generals-sweeping-fraud-case-against-zelle-operator-early-warning-services/)
- **Wires and remittances:**
  - Wires between banks: UCC 4A-207 lets the beneficiary's bank rely on the account number if it "does not know that the name and number refer to different persons". — [UCC 4A-207, Cornell LII](https://www.law.cornell.edu/ucc/4A/4A-207)
  - Consumer remittance transfers (Reg E subpart B):
    - the sender has **180 days** to report an error and the provider has **90 days** to investigate (§1005.33);
    - a wrong account number supplied by the sender is not an "error" only if the provider shows the conditions in §1005.33(h) are met. These are: prior notice that funds could be lost; reasonable checks of the institution identifier; deposit into a non-recipient account; and prompt "reasonable efforts to recover". — [eCFR §1005.33](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-B/section-1005.33)

### Inferences (practical consequences for the agent)
- (4) **Misdirected payment caused by a customer typo:**
  - EU/UK: open a recovery request with the payee's bank, explain that recovery cannot be guaranteed and any agreed fee, and offer the written-request route for the information needed to make a claim (PSD2 Art. 88; UK reg 90).
  - Do not disclose the payee's personal data beyond what the law allows. It is released to the payer only through that written-request route (5: national data-protection practice may differ).
- (4) **EU after 9 Oct 2025 (euro-area banks):**
  - First check whether VoP ran and what result the customer saw (match, almost match, mismatch). A bank failure to perform VoP shifts the loss to the bank (Art. 5c(8)).
  - The customer proceeding after a mismatch warning generally weakens their claim, but the agent should not pre-judge it. Escalate to disputes.
- (4) **UK APP claims:**
  - Take the claim on first contact, without making a police report a precondition. The bank can ask the customer to consent to police reporting.
  - Explain the 5-business-day expectation, possible stop-the-clock, the £85k cap, any excess (none for vulnerable customers) and the FOS route.
  - Check for vulnerability before applying any gross-negligence or consumer-standard-of-caution exception.
- (4) **UK payment holds under reg 86:** the agent may tell the customer the payment is delayed for checks and what information is needed. Where telling them would be unlawful (tipping-off; see §8), use neutral wording and escalate.
- (4) **US scam victims:** first establish who initiated the transfer. Fraudster-initiated, including via tricked credentials or codes, means a Reg E error claim with full error-resolution rights. Customer-initiated after deception means no federal right, but the bank may have network, goodwill or state-law remedies. Never tell a customer "Reg E doesn't cover scams" without that analysis.
- (4) **EU PSR is not yet law.** Do not tell EU customers they have a right to a refund for impersonation fraud under the "new rules". Inference: on the OEIL timetable (plenary indicated 14 Dec 2026), the general application date could fall roughly in late 2028 and VoP for all credit transfers roughly in 2029, depending on the Official Journal publication date (5).

### Gaps
- PSR→FCA Bill: progress after its May 2026 introduction is unverified.
- Whether the PSR or FCA changed the £85,000 cap or the consumer-standard-of-caution rules after the 2026 evaluation is unverified.
- Full PSR PS25/5 consolidated policy statement not read.
- US state laws (beyond the NY AG litigation) requiring scam reimbursement: none found in this session.
- EPC VoP scheme rulebook (operational detail, response codes) not reviewed.

---

## 3. Strong customer authentication and what agents may or may not do

### Takeaway
SCA (EU/UK) is a legal requirement for online account access, payment initiation and any risky remote action. It requires two independent factors from knowledge, possession and inherence, plus dynamic linking for remote payments, with defined exemptions. Weak SCA shifts losses to the bank.

The US relies on risk-based supervisory guidance: the FFIEC's 2021 statement emphasises layered security, multifactor authentication, and the specific risks of call-centre and help-desk authentication.

For agents this means no override of SCA, no changes to contact details or credentials without strong verification through a separate channel, and treating any request to change phone, email or device as high-risk.

### Cited Findings
- [EU] (1) IN FORCE — PSD2 Art. 4(30):
  - SCA uses "two or more elements categorised as knowledge (something only the user knows), possession (something only the user possesses) and inherence (something the user is) that are independent".
  - Art. 97(1): SCA applies when the payer accesses the account online, initiates an electronic payment, or "carries out any action through a remote channel which may imply a risk of payment fraud or other abuses".
  - Art. 97(2): remote payments require dynamic linking to amount and payee. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- [EU] (1) IN FORCE — SCA RTS (Delegated Reg. (EU) 2018/389), original text:
  - Art. 11 contactless at point of sale: ≤ EUR 50 per transaction, and a cumulative ≤ EUR 150 or ≤ 5 consecutive transactions since the last SCA.
  - Art. 13 trusted beneficiaries: SCA is required to create or amend the list.
  - Art. 16 low-value remote: ≤ EUR 30, with a cumulative ≤ EUR 100 or 5 transactions.
  - Art. 18 transaction risk analysis, with fraud-rate-linked thresholds up to EUR 500 in the Annex. — [RTS 2018/389](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389)
  - (5) Later amendments to the RTS (e.g. to the Art. 10 account-information exemption) were not checked.
- [EU] (1) IN FORCE — PSD2 Art. 74(2): no SCA means no payer liability, absent fraud. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- [UK] (1) IN FORCE — UK reg 77(4)(c): no payer liability where SCA was required under reg 100 but not applied. — [reg 77](https://www.legislation.gov.uk/uksi/2017/752/regulation/77)
- [EU] AGREED – NOT ADOPTED — PSR text:
  - SCA plus "different communication channels" to activate a mobile banking app;
  - a 4-hour delay for remote activation;
  - notification through different channels, with instructions if the customer did not install the app;
  - a duty to disable access once the customer reports an activation they did not make. — [Council ST 8221/26, Art. 51(4a)–(4d)](https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf)
- [US] (2) IN FORCE — FFIEC "Authentication and Access to Financial Institution Services and Systems" (11 Aug 2021), replacing the 2005 and 2011 guidance. Its highlights include:
  - "the adoption of layered security" and "the weaknesses in single factor authentication";
  - "multifactor authentication or controls of equivalent strength";
  - "risks associated with call center and information technology help desk authentication";
  - customer awareness programmes. — [OCC Bulletin 2021-36](https://occ.treas.gov/news-issuances/bulletins/2021/bulletin-2021-36.html)
  - (The FFIEC PDF itself was behind a CAPTCHA, so the OCC bulletin summary is used.)
- [US] (1) IN FORCE — GLBA pretexting prohibition: it is unlawful to obtain customer information of a financial institution "by making a false, fictitious, or fraudulent statement or representation to an officer, employee, or agent of a financial institution". — [15 U.S.C. 6821](https://www.law.cornell.edu/uscode/text/15/6821)

### Inferences (practical consequences for the agent)
- (4) The agent must never bypass or "help complete" SCA. That includes reading out or requesting OTPs, approving pushes on the customer's behalf, or disabling 2FA.
- (4) Treat contact-detail changes (phone, email, device binding), credential resets and limit increases as **high-risk remote actions**. Under PSD2 Art. 97(1)(c) they require SCA or equivalent strong verification, through a separate channel and with notification to the old contact details. The future EU PSR codifies 4-hour delays for remote limit increases and app activations; banks may adopt them now as good practice.
- (4) A US agent should assume social-engineering attempts against the call centre (FFIEC) and that impostors may commit GLBA pretexting. Follow scripted verification; do not reveal account data before verification; never "confirm" data the caller volunteers.
- (4) An AI agent must not have tool permissions to change credentials, contact details or limits without step-up authentication completed by the customer in the bank's own channel.

### Gaps
- UK FCA SCA-RTS changes in 2025–2026 (e.g. contactless limits) not verified (card team 06 / digital team 08).
- EBA Q&A on SCA for call-centre-initiated payments (MOTO) not reviewed.

---

## 4. Complaint handling and ADR

### Takeaway
- **EU:** payment-services complaints need a written reply addressing all points within **15 business days**, or a holding reply and a final reply within **35 business days** (PSD2 Art. 101). The ESAs' complaint-handling guidelines (JC 2018 35) set governance, register, plain-language and ADR-signposting expectations. The ADR Directive was revised by Directive (EU) 2025/2647 (in force 19 Jan 2026, transposition by ~March 2028).
- **UK:** a final response within **8 weeks** (DISP 1.6), or **15/35 business days** for payment-services and e-money complaints. Complaints resolved by the close of the **3rd business day** can be closed with a "summary resolution communication". The Ombudsman (FOS) referral deadline is **6 months** from the final response. The FOS award limit is **£455,000** from 1 Apr 2026.
- **US:** no single statutory complaint deadline. The hard clocks are the Reg E and Reg Z error-resolution timelines. CFPB portal companies "generally respond in 15 days", with a final response within 60.

### Cited Findings
- [EU] (1) IN FORCE — PSD2 Art. 101:
  - banks must have complaint procedures in an official language of the Member State;
  - they must reply "on paper or, if agreed … on another durable medium", addressing "all points raised" "at the latest within 15 business days";
  - in exceptional situations, a holding reply giving the reasons and the date of the final reply, with the final reply "not [to] exceed 35 business days";
  - Member States may set more favourable rules;
  - banks must name at least one competent ADR body on their website, at the branch and in the general terms. — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- [EU] (2) IN FORCE — Joint Committee (ESMA/EBA) Guidelines on complaints-handling (JC 2018 35); applicable from 1 May 2019 for the PSD2/MCD "new institutions". The seven guidelines cover:
  - a complaints management policy and function;
  - an internal register;
  - reporting to authorities;
  - root-cause follow-up;
  - provision of information (written information on the process when acknowledging a complaint; indicative timelines; ADR availability; keeping the complainant informed);
  - responding: gather all relevant evidence, "communicate in plain language", reply without unnecessary delay or within national time limits and explain any delay, and give a thorough written explanation plus the options to escalate (ombudsman, ADR, authority) when the complaint is not fully upheld. — [JC 2018 35 PDF](https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec); [EBA page](https://www.eba.europa.eu/regulation-and-policy/consumer-protection-and-financial-innovation/guidelines-for-complaints-handling-for-the-securities-esma-and-banking-eba-sectors)
- [EU] (1) ADOPTED – NOT YET APPLICABLE (transposition pending) — Directive (EU) 2025/2647 amending the ADR Directive 2013/11/EU:
  - adopted Dec 2025, published in the OJ 30 Dec 2025, in force 19 Jan 2026;
  - transposition by about March 2028;
  - follows the discontinuation of the EU ODR platform;
  - scope extended to pre-contractual and digital-content disputes. — [EAPIL, 23 Jan 2026](https://eapil.org/2026/01/23/directive-eu-2025-2647-amending-the-adr-framework-for-consumer-disputes/); [Bird & Bird 2026](https://cm.twobirds.com/en/insights/2026/eu-the-new-alternative-dispute-resolution-framework--directive-20252647); [Commission ADR transposition workshop, 1 Oct 2026](https://commission.europa.eu/get-involved/events/adr-transposition-workshop-2026-10-01_en)
  - (5) Exact transposition date not read in the OJ text.
- [EU] AGREED – NOT ADOPTED — PSR Art. 94 keeps the 15/35-business-day rule. The EP says all banks must participate in ADR if the consumer chooses. — [Council ST 8221/26](https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf); [EP press release](https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees)
- [UK] (1) IN FORCE — FCA DISP:
  - **DISP 1.6.2R:** by the end of **eight weeks** the firm must send a final response, or a written response explaining the delay.
  - **DISP 1.6.2AR:** PSD/EMD complaints need a final response by the end of **15 business days**, or in exceptional circumstances a holding response by 15 business days and a final response by **35 business days**, on paper or another agreed durable medium. — [DISP 1.6](https://www.handbook.fca.org.uk/handbook/DISP/1/6.html)
  - **DISP 1.5:** complaints resolved by close of business on the **third business day** after receipt are exempt from the time-limit and forwarding rules. They are "resolved" when the complainant indicates acceptance, which need not be in writing. A written "summary resolution communication" must state that the complaint is resolved, mention the possible FOS referral and time-limit waiver, and give the FOS website. Last updated 01/04/2018. — [DISP 1.5](https://www.handbook.fca.org.uk/handbook/DISP/1/5.html)
  - **DISP 2.8:** referral to the FOS is out of time if made more than **six months** after the final response or summary resolution communication, or more than six years after the event (or, if later, three years after awareness), subject to exceptions. — [DISP 2.8](https://www.handbook.fca.org.uk/handbook/DISP/2/8.html)
  - **DISP 1.10:** complaints reporting twice a year. The page was last updated 07/04/2026 and shows a **future version from 31/12/2026**, so reporting changes are pending (detail for team 04). — [DISP 1.10](https://www.handbook.fca.org.uk/handbook/DISP/1/10.html)
  - (5) Definition of "complaint": the FCA Glossary covers any oral or written expression of dissatisfaction, whether justified or not, alleging financial loss, material distress or material inconvenience. Not re-read in the Glossary this session.
- [UK] (2) — FOS award limits from 1 Apr 2026: **£455,000** for acts on or after 1 Apr 2019; £205,000 for earlier acts. — [FOS news](https://www.financial-ombudsman.org.uk/news/fca-confirms-increase-award-limits-2)
- [US] (2) — CFPB complaint portal: "Companies generally respond in 15 days. In some cases, the company will let you know their response is in progress and provide a final response in 60 days." Consumers have 60 days to give feedback. — [CFPB complaint process](https://www.consumerfinance.gov/complaint/process/)
- [US] (2) WITHDRAWN 12 May 2025 — CFPB policy statements on disclosing consumer complaint data and narratives. This changes the CFPB's publication practice, not banks' legal error-resolution duties. — [CFPB Withdrawn Guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/)
- [US] (2) — CFPB institutional status: three federal courts have held the administration must keep requesting CFPB funding from the Federal Reserve, the latest being D. Or., reported 28 Sep 2026. The agency continues to operate. — [ABA Banking Journal, 28 Sep 2026](https://bankingjournal.aba.com/2026/09/third-court-rules-against-trump-administration-over-cfpb-funding/)

### Inferences (practical consequences for the agent)
- (4) **Recognise complaints by their substance, not keywords.** EU guidelines and DISP both cover oral complaints, and chatbots must flag dissatisfaction plus a loss or inconvenience claim. The CFPB spotlight documents chatbots failing to recognise disputes (§10).
- (4) **Route to the shortest applicable clock:**
  - EU payment complaints: 15 business days;
  - UK payment or e-money complaints: 15 business days; other UK complaints: 8 weeks;
  - US: Reg E or Reg Z clocks where an error is asserted.
  The agent should never tell customers "8 weeks" for UK payment complaints.
- (4) **UK three-business-day resolutions** still need the written summary resolution communication with the FOS signposting.
- (4) **Final responses** must signpost ADR (EU: the named ADR body; UK: FOS within 6 months). An AI agent must not discourage escalation.
- (4) **Log every complaint in the register** (JC Guideline 3; DISP), including those resolved in the same contact.

### Gaps
- FCA/FOS "modernising redress" reforms (2025–2026) and the content of the DISP 1.10 version due 31 Dec 2026: not verified (team 04).
- US OCC/Fed/FDIC complaint channels: names and URLs not re-verified this session (5).
- FIN-NET membership and current role after the ADR revision not re-checked (5).

---

## 5. UK Consumer Duty (consumer support), vulnerability, and EU/US equivalents

### Takeaway
- **UK:** the Consumer Duty's consumer-support outcome (PRIN 2A.6) is binding on every channel, including chatbots and social media, and on outsourced support. It bans "unreasonable barriers", including post-sale support that is harder to reach than sales. FG21/1 (four vulnerability drivers) remains the FCA's reference, with no new rules after its March 2025 review.
- **EU:** there is no single EU vulnerability guideline. Vulnerability appears in specific instruments (EAA; CCD2; AI Act Art. 5) and EBA consumer-trends work.
- **US:** non-binding interagency elder-exploitation practices (trusted contacts, transaction holds), issued 4 Dec 2024 and revised 2 Jun 2026.

### Cited Findings
- [UK] (1) IN FORCE (31 Jul 2023; application text updated 26 Jun 2026) — PRIN 2A.6:
  - **Scope:** applies to firms that interact with and support retail customers, "including where the firm outsources its interactions … to a third party", "regardless of the channel … including via electronic communications such as on social media", and to support before, during and after sale. — [PRIN 2A.6](https://www.handbook.fca.org.uk/handbook/PRIN/2A/6.html)
  - **PRIN 2A.6.2R:** support must meet the needs of customers "including those with characteristics of vulnerability". It must include "appropriate friction … to mitigate the risk of harm", and ensure customers face no "unreasonable barriers" when they make enquiries, switch, claim, **complain**, cancel, and so on.
  - **PRIN 2A.6.3G:** unreasonable barriers include steps that are onerous, time-consuming, complex or hard to understand, and "asking retail customers for unnecessary information or evidence".
  - **PRIN 2A.6.4G:** examples of failure include "disproportionately longer call waiting times to cancel … than to purchase", and unreasonable delays to payments or to processing evidence.
  - **PRIN 2A.6.5R:** give a power-of-attorney holder or other representative the same level of support as the customer. — [PRIN 2A.6](https://www.handbook.fca.org.uk/handbook/PRIN/2A/6.html)
- [UK] (2) — FCA "Consumer support outcome: good practices and areas for improvement" (published 7 Mar 2025, updated 10 Jul 2026):
  - good practice includes "automatically directing queries from a webchat chatbot about bereavement to a customer support representative", vulnerability keywords triggering priority routing, and customer-journey mapping to find "sludge";
  - areas for improvement include making post-sale support less accessible than pre-sale, relying on transactional metrics, and weak oversight of outsourced support;
  - 48% of surveyed firms offer dedicated phone support for vulnerable customers. — [FCA good/poor practice page](https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement)
- [UK] (2) — FG21/1 (Feb 2021):
  - a vulnerable customer is "someone who, due to their personal circumstances, is especially susceptible to harm, particularly when a firm is not acting with appropriate levels of care";
  - vulnerability is a "spectrum of risk";
  - four drivers: **health**, **life events** (e.g. bereavement, job loss, relationship breakdown), **resilience** (low ability to withstand financial or emotional shocks) and **capability** (low financial knowledge or confidence, literacy, digital skills). — [FG21/1 PDF](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [UK] (2) — FCA multi-firm review published 7 Mar 2025: FG21/1 "still useful"; no new guidance or rules. Only 39% of firms had formal governance bodies overseeing vulnerable-customer outcomes. — [FCA review page](https://www.fca.org.uk/publications/multi-firm-reviews/firms-treatment-vulnerable-customers) (statistic from a search summary of the FCA/A&O Shearman pages; verify)
- [UK] (1) IN FORCE — APP reimbursement: no gross-negligence exception and no excess for vulnerable consumers (§2).
- [EU] (2) — EBA Consumer Trends Report 2024/25: key consumer issues are payment fraud, indebtedness and de-risking. Access to accounts is particularly difficult for vulnerable groups (migrants, refugees, homeless people and others). Summary via search; PDF not read. — [EBA CTR 2024/25](https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf)
- [EU] (1) IN FORCE (since 2 Feb 2025) — AI Act Art. 5(1)(b) prohibits AI that "exploits any of the vulnerabilities of a natural person … due to their age, disability or a specific social or economic situation" so as to materially distort behaviour and cause significant harm. — [AI Act Art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)
- [US] (2) — Interagency Statement on Elder Financial Exploitation (Fed, CFPB, FDIC, NCUA, OCC, FinCEN and state regulators; 4 Dec 2024, "Revised June 2, 2026"):
  - "does not establish new supervisory expectations or impose new regulatory requirements";
  - examples: staff training; "transaction holds and disbursement delays"; letting customers "designate one or more trusted contacts"; voluntary SARs; reporting to Adult Protective Services or law enforcement where state law requires; expediting records for APS and law enforcement. — [FDIC FIL page](https://www.fdic.gov/news/financial-institution-letters/2024/agencies-issue-interagency-statement-elder-financial)
  - (5) Nature of the 2026 revision not determined.

### Inferences (practical consequences for the agent)
- (4) **Ease of reaching a human:** an AI agent must offer a clear, early route to a human, especially for complaints, bereavement, financial difficulty, suspected fraud and vulnerability cues. A bot that blocks or delays access is a PRIN 2A.6 "unreasonable barrier" risk. The agreed EU PSR also requires human support (§10).
- (4) **Vulnerability cues** across the four drivers (health, life events, resilience, capability) should trigger tailored handling: slower pace, plain language, alternative channels, recording needs with consent, and no reliance on gross-negligence exceptions in UK APP cases.
- (4) **Representatives** (power of attorney, deputies and so on) must get the same level of support once verified.
- (4) **Elder exploitation (US):** recognised practice is to offer trusted-contact designation, apply holds where policy and law permit, and escalate to the fraud and BSA teams. The agent must not disclose any SAR (see §8).

### Gaps
- A binding EU-level vulnerability framework: none found. Member-State rules exist but are out of scope.
- US Senior Safe Act and FINRA trusted-contact rules (broker-dealers only) not verified this session (5).

---

## 6. Accessibility

### Takeaway
The European Accessibility Act has applied to **consumer banking services** provided after **28 June 2025**. It covers websites and apps; identification, e-signature, security and payment features that are perceivable, operable, understandable and robust; information at a complexity no higher than CEFR level **B2**; and support services that explain accessibility in accessible formats. There are transitional periods to 2030 for existing products and up to 20 years for existing self-service terminals.

UK: the Equality Act 2010 duty to make reasonable adjustments applies to service providers (s.29(7)). US: ADA Title III web accessibility is enforced through litigation and DOJ guidance, not a Title III web regulation (5).

### Cited Findings
- [EU] (1) IN FORCE (applies from 28 Jun 2025) — Directive (EU) 2019/882 (EAA):
  - **Scope:** Art. 2(2) covers services provided to consumers after 28 June 2025, including "(d) consumer banking services".
  - **Definition (Art. 3(28)):** credit agreements under the Consumer Credit and Mortgage Credit Directives; specified MiFID services; payment services; services linked to the payment account; and e-money. — [EAA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882)
  - **Annex I, Section IV(e), banking:** "providing identification methods, electronic signatures, security, and payment services which are perceivable, operable, understandable and robust" and "ensuring that the information is understandable, without exceeding a level of complexity superior to level B2 (upper intermediate)" of the CEFR.
  - **Annex I, Section III(c):** "making websites, including the related online applications, and mobile device-based services, including mobile applications, accessible in a consistent and adequate way by making them perceivable, operable, understandable and robust".
  - **Annex I, Section III(d):** "where available, support services (help desks, call centres, technical support, relay services and training services) providing information on the accessibility of the service and its compatibility with assistive technologies, in accessible modes of communication". — [EAA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882)
  - **Transitional rules:**
    - Art. 32(1): a transitional period ending **28 June 2030**, during which service providers may keep providing services using products they lawfully used for similar services before 28 June 2025; service contracts agreed before 28 June 2025 may continue unaltered until expiry, but no longer than 5 years from that date.
    - Art. 32(2): Member States may allow self-service terminals to stay in use until the end of their economic life, but no more than 20 years.
    - Art. 4(5): micro-enterprises providing services are exempt. — [EAA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882)
- [EU] (1) IN FORCE — AI Act Art. 50(5): the AI-interaction disclosure "shall conform to the applicable accessibility requirements". — [AI Act Art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- [UK] (1) IN FORCE — Equality Act 2010 s.29(7): "A duty to make reasonable adjustments applies to … a service-provider". — [s.29](https://www.legislation.gov.uk/ukpga/2010/15/section/29)
  - (5) The text of s.20, which defines the duty, was not retrieved this session; the anticipatory nature (Sch. 2) is not re-verified.
- [UK] (1) IN FORCE — PRIN 2A.6.2R(1): support must meet the needs of customers with vulnerability characteristics. — [PRIN 2A.6](https://www.handbook.fca.org.uk/handbook/PRIN/2A/6.html)
- [US] (2) — DOJ web-accessibility guidance (18 Mar 2022): businesses open to the public (Title III) "must ensure that the programs, services, and goods that they provide to the public – including those provided online – are accessible". It points to WCAG and the Section 508 Standards as options. — [US Access Board news on DOJ guidance](https://www.access-board.gov/news/2022/03/21/department-of-justice-issues-web-accessibility-guidance-under-the-ada/)
  - (5) Section 508 binds federal agencies, not private banks, and there is no DOJ Title III web regulation. Both statements are from background knowledge and were not verified this session.

### Inferences (practical consequences for the agent)
- (4) **Bot responses in the EU:** keep EU customer-facing bot answers at or below CEFR B2. Avoid jargon and offer accessible formats (large print, screen-reader-friendly documents, relay services).
- (4) **Explaining accessibility:** support staff and bots must be able to explain the accessibility features of the bank's app and identification methods, and compatibility with assistive technology.
- (4) **Alternatives to inaccessible authentication:** if a customer cannot use an authentication method (e.g. biometric or app-based), offer accessible alternatives and record reasonable-adjustment needs, with consent (UK). Do not weaken SCA; provide an equivalent accessible method.

### Gaps
- National EAA transposition and enforcement (e.g. which authority handles bank complaints) not covered.
- Whether any 2025–2026 EU proposals change EAA deadlines: none found, not specifically searched (5).

---

## 7. Data protection, secrecy, call recording and PCI DSS

### Takeaway
- **EU/UK GDPR:** purpose limitation and data minimisation govern what an agent asks for and logs. Subject access requests (SARs) are answered within **1 month**, extendable by **2 months** with notice. Identity can be checked where there is reasonable doubt. Art. 22 limits solely automated decisions with significant effects.
- **UK changes:** the Data (Use and Access) Act 2025 introduced "stop the clock" and "reasonable and proportionate searches" for SARs and liberalised automated decision-making, with most provisions commenced in Feb 2026 (5: commencement detail from secondary sources).
- **Call recording:** the EU ePrivacy Directive allows legally authorised recording "for the purpose of providing evidence of a commercial transaction". FCA SYSC 10A recording duties apply to **investment** business, not ordinary payment calls. US federal law is one-party consent, with stricter state laws.
- **PCI DSS (v4.0.1):** card security codes must never be retained after authorisation, including in audio recordings (FAQ 1210, June 2025).

### Cited Findings
- [EU] (1) IN FORCE — GDPR (Reg. (EU) 2016/679):
  - Art. 5(1)(b): data "collected for specified, explicit and legitimate purposes" ("purpose limitation").
  - Art. 5(1)(c): "adequate, relevant and limited to what is necessary" ("data minimisation").
  - Art. 5(1)(e): storage limitation. — [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679)
  - Art. 12(3): act on requests "without undue delay and in any event within one month of receipt"; this "may be extended by two further months where necessary", informing the data subject within one month with reasons.
  - Art. 12(4): if the controller does not act, it must explain why and give the complaint and remedy options within one month.
  - Art. 12(6): additional information may be requested where there are "reasonable doubts concerning the identity". — [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679)
  - Art. 22(1): a right "not to be subject to a decision based solely on automated processing, including profiling", with legal or similarly significant effects.
  - Art. 22(3): where contract or consent exceptions apply, at minimum the right to "obtain human intervention", to express a point of view and to contest the decision.
  - Recital 71 cites "automatic refusal of an online credit application" as an example. — [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679)
- [EU] (1) IN FORCE — ePrivacy Directive 2002/58/EC Art. 5(2): confidentiality rules "shall not affect any legally authorised recording of communications … in the course of lawful business practice for the purpose of providing evidence of a commercial transaction or of any other business communication". — [ePrivacy Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32002L0058)
- [UK] (1) IN FORCE (stages 2025–2026) — Data (Use and Access) Act 2025:
  - **SARs:** statutory "stop the clock" while clarification is "reasonably required"; only "reasonable and proportionate searches" are needed. ICO guidance updated, with the 16 Jul 2026 date from a search snippet. — [ICO: responding to a SAR](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/right-of-access/what-should-we-consider-when-responding-to-a-request/)
  - **Automated decision-making:** a more permissive framework, with safeguards (information about significant decisions, the right to make representations and challenge, and human intervention). — [GOV.UK DUAA guidance, 27 Jun 2025](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)
  - **Commencement:** most provisions commenced **5 Feb 2026**; complaint-handling provisions on 19 Jun 2026. Secondary sources only. — [Mills & Reeve, 6 Feb 2026](https://www.mfmac.com/insights/manufacturing-media-technology/major-provisions-of-the-uk-data-use-and-access-act-2025-take-effect/)
- [UK] (1) IN FORCE — SYSC 10A (last updated 23/10/2025):
  - applies to MiFID investment firms, AIFMs, UCITS management companies and others carrying out investment activities in financial instruments;
  - records kept for 5 years, or up to 7 if the FCA requests;
  - does not apply to ordinary retail payment or deposit calls (inferred from the scope text). — [SYSC 10A.1](https://www.handbook.fca.org.uk/handbook/SYSC/10A/1.html)
- [US] (1) IN FORCE — 18 U.S.C. 2511(2)(d): it is not unlawful for a party to a communication, or where "one of the parties to the communication has given prior consent", to intercept it, unless for a criminal or tortious purpose. — [18 U.S.C. 2511](https://www.law.cornell.edu/uscode/text/18/2511)
  - (5) Some states require all-party consent (e.g. California); not verified this session.
- [US] (1) IN FORCE — GLBA anti-pretexting: [15 U.S.C. 6821](https://www.law.cornell.edu/uscode/text/15/6821).
  - (5) GLBA privacy (Reg P) and safeguards obligations (the interagency Information Security Guidelines for banks; the FTC Safeguards Rule for non-banks) were not re-read this session.
- [INTL] (3) — PCI DSS:
  - v4.0.1 is the only active version since v4.0 was retired on 31 Dec 2024, and the future-dated requirements became mandatory 31 Mar 2025. — [PCI SSC blog](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1)
  - FAQ 1210 (June 2025): Requirement 3.3.1 "prohibits storage of sensitive authentication data … after authorization even if the data is encrypted". Storing CVV2/CVC2/CID "in any form of digital audio recording … after authorization is therefore a violation". If collected on a call, "every effort must be made to prevent the data from being recorded" (suppress or redact audio). Otherwise delete securely immediately after authorisation, or apply documented compensating controls. "PCI DSS does not override local or regional audio retention laws." — [PCI SSC FAQ 1210](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/are-audio-voice-recordings-permitted-to-contain-sensitive-authentication-data/)
  - Further guidance: PCI SSC Information Supplement "Protecting Telephone-Based Payment Card Data" (v3.0, Nov 2018). — [PCI SSC](https://listings.pcisecuritystandards.org/documents/Protecting_Telephone_Based_Payment_Card_Data_v3-0_nov_2018.pdf)
  - (3) Industry commentary says pause-and-resume alone is not a complete control; DTMF masking or descoping is preferred. — [Eckoh blog](https://www.eckoh.com/blog/pause-and-resume-of-call-recordings-is-obsolete-exploring-pci-dss-4-0-1-and-its-impact-on-data-security-practices) (vendor source)

### Inferences (practical consequences for the agent)
- (4) **Collect the minimum.** A support bot should not ask for full card numbers, CVV, PINs, passwords or OTPs. If a card payment must be taken by phone, use DTMF masking or IVR descoping so that the agent, the bot and the recordings never capture card security codes.
- (4) **Identity checks:** use the bank's verification flow. Do not over-collect, but where identity is in doubt (including on SAR requests) the bank may request more (GDPR Art. 12(6)).
- (4) **SARs:** recognise one in any channel and route it to the data-protection team with the date received. The agent must not refuse, stall or "answer" it informally. UK clock rules have changed (stop-the-clock); EU rules have not.
- (4) **Call-recording notice:** state that the call is recorded and why (evidence of transactions, quality, fraud). For US calls, state law may require every party's consent, so a recording notice and consent at the start is the safe practice (5).
- (4) **Automated decisions** (e.g. auto-declines or limit cuts) that significantly affect a customer need a human-review route. Agents should tell customers how to request it (GDPR Art. 22(3); UK DUAA safeguards).

### Gaps
- EU "Digital Omnibus" GDPR amendment proposals (Nov 2025): status not checked; treat as PROPOSED until verified (5).
- UK ICO guidance on call recording and AI transcription not reviewed.
- US state privacy laws (e.g. CCPA's GLBA carve-outs) not covered.

---

## 8. AML / financial-crime boundaries: tipping-off, freezes, holds, closures

### Takeaway
All three jurisdictions criminalise or prohibit disclosure that a suspicious-activity report has been or will be filed, or that an investigation exists:
- **EU:** AMLD Art. 39; AMLR Art. 73 from 10 Jul 2027.
- **UK:** POCA s.333A.
- **US:** 31 U.S.C. 5318(g)(2); 31 CFR 1020.320(e).

Payment laws nonetheless require banks to explain blocks, delays or closures, *except where doing so would be unlawful*:
- EU: PSD2 Art. 68(3);
- UK: reg 86(2D)(c); SI 2025/688 (90-day closure notice with reasons from 28 Apr 2026, with financial-crime exceptions).

Agents therefore need a "neutral explanation + escalate" script and must never speculate about investigations.

### Cited Findings
- [EU] (1) IN FORCE — AMLD (EU) 2015/849 Art. 39(1): obliged entities "shall not disclose to the customer concerned or to other third persons the fact that information is being, will be or has been transmitted … or that a money laundering or terrorist financing analysis is being, or may be, carried out". Exceptions: competent authorities, law enforcement, and intra-group sharing. Original text; consolidated text not checked. — [AMLD](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L0849)
- [EU] (1) ADOPTED – NOT YET APPLICABLE — AMLR (EU) 2024/1624:
  - Art. 73 ("Prohibition of disclosure") extends Art. 39 to the fact "that transactions or activities are being or have been assessed".
  - The Regulation applies from **10 July 2027** (10 Jul 2029 for certain entities in Art. 3(3)(n)–(o)). — [AMLR](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1624)
- [EU] (1) IN FORCE — PSD2 Art. 68(3): when blocking an instrument, the bank must tell the payer and give the reasons, "unless providing such information would compromise objectively justified security reasons or is prohibited by other relevant Union or national law". — [PSD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366)
- [EU] (1) IN FORCE — IPR Art. 5d: daily screening of users against EU targeted financial sanctions for banks offering instant transfers. — [Reg. 2024/886](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886)
- [UK] (1) IN FORCE — POCA s.333A, up to date with changes in force by 9 Oct 2026 per legislation.gov.uk:
  - offence to disclose that a disclosure (SAR) has been made where the disclosure "is likely to prejudice any investigation";
  - offence to disclose that an investigation "is being contemplated or is being carried out";
  - applies to information obtained in the regulated sector; permitted-disclosure exceptions in ss.333B–333D. — [POCA s.333A](https://www.legislation.gov.uk/ukpga/2002/29/section/333A)
- [UK] (1) IN FORCE — POCA s.335 (DAML consent): a 7-working-day notice period, and a 31-day moratorium if consent is refused. This explains multi-week holds. — [POCA s.335](https://www.legislation.gov.uk/ukpga/2002/29/section/335)
- [UK] (1) IN FORCE — Payment holds and refund delays:
  - reg 86(2D)(c): the duty to explain a fraud-check payment delay does not apply "to the extent complying with it would be otherwise unlawful". — [reg 86](https://www.legislation.gov.uk/uksi/2017/752/regulation/86)
  - reg 76(3): a refund can be delayed on suspicion of the customer's fraud, with a report to a s.333A(2) person. — [reg 76](https://www.legislation.gov.uk/uksi/2017/752/regulation/76)
- [UK] (1) IN FORCE from 28 Apr 2026 — SI 2025/688 (Payment Services and Payment Accounts (Contract Termination) (Amendment) Regulations 2025):
  - **New reg 51B, notice and reasons:** for indefinite framework contracts entered into **on or after 28 Apr 2026**, the termination notice must explain the reasons "sufficiently detailed and specific to enable the payment service user to understand why", say how to complain to the bank and about any FOS right, and be given **at least 90 days** before termination.
  - **Contracts before 28 Apr 2026:** reg 51A keeps two months' notice.
  - **Conflicting legal requirements:** reg 51B(4) says another legal requirement (e.g. tipping-off) prevails to the extent of the conflict.
  - **No notice at all (reg 51C):** where customer due diligence cannot be applied, an Immigration Act closure applies, the bank has reasonable grounds to suspect use in connection with "serious crime", the FCA or Treasury directs, and similar cases.
  - **Immediate notice (reg 51D):** allowed where the customer's conduct toward staff amounts to certain public-order offences.
  - **Basic bank account refusals:** reasons must be given "unless providing that information would be unlawful". — [SI 2025/688](https://www.legislation.gov.uk/uksi/2025/688/made)
- [US] (1) IN FORCE — 31 U.S.C. 5318(g)(2)(A)(i): neither the institution nor its current or former officers, employees or contractors "may notify any person involved in the transaction that the transaction has been reported or otherwise reveal any information that would reveal that the transaction has been reported". — [31 U.S.C. 5318](https://www.law.cornell.edu/uscode/text/31/5318)
- [US] (1) IN FORCE — 31 CFR 1020.320(e): "A SAR, and any information that would reveal the existence of a SAR, are confidential". Requests for a SAR must be declined and reported to FinCEN. Sharing the underlying facts is permitted only in defined cases (law enforcement, a joint SAR, within the corporate group), "provided that no person involved … is notified". — [eCFR 31 CFR 1020.320](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320)

### Inferences (practical consequences for the agent)
- (4) **Never say or imply:**
  - that a SAR, SAR-equivalent or DAML was filed or is being considered;
  - that "compliance/AML is investigating you";
  - that a law-enforcement inquiry exists;
  - whether a hold relates to sanctions screening, unless the bank's financial-crime team has approved specific wording.
- (4) **Permitted neutral wording** (to be approved by the bank's MLRO/BSA officer): "Your payment/account is subject to a review. I'm unable to share more at this stage. Here is what you can do / what information we need / how to complain."
  - Where law requires reasons (PSD2 Art. 68(3); UK reg 86 delays; UK closure notices from 28 Apr 2026), the *reason text* is decided by the financial-crime team, not generated by an AI agent.
- (4) **The bot must not speculate** about why a customer is flagged, confirm or deny sanctions matches, or reveal internal case notes or alert scores. Hand over to a specialist queue with tight access controls.
- (4) **Complaints about freezes or closures** are still complaints. Register them and follow DISP/PSD2 timelines; the complaint response itself must not tip off.
- (4) **UK account closures (contracts from 28 Apr 2026):** the customer is entitled to 90 days' notice, reasons, and complaint and FOS information, unless the financial-crime exceptions apply. Agents should not promise reasons in exception cases.

### Gaps
- AMLA (Reg. (EU) 2024/1620) operational and supervisory dates not re-verified (5).
- UK Terrorism Act 2000 s.21D tipping-off and US OFAC customer-communication practice not verified this session (5).
- Whether UK SI 2025/688's "serious crime" exception is construed to cover AML suspicions generally needs legal confirmation.

---

## 9. Debt collection, arrears and forbearance

### Takeaway
- **US:** the FDCPA and Regulation F bind *third-party* collectors (not a creditor's own employees collecting in its name). They set the 7-calls-in-7-days presumption, the 8 a.m.–9 p.m. default, validation notices and limits on third-party contact. Banks collecting their own debts are policed through UDAAP, but the CFPB **withdrew** its 2013 UDAAP-in-collections bulletin on 12 May 2025.
- **UK:** CONC 7.3, as strengthened from **4 Nov 2024**, requires forbearance and due consideration, sustainable repayment plans, objective income-and-expenditure checks, signposting to free debt advice, and no pressure tactics.
- **EU:** CCD2 Art. 35 (forbearance before enforcement) and Art. 18(8) (human intervention in automated creditworthiness assessment) apply from **20 Nov 2026**, so they are **adopted but not yet applicable** as of 10 Oct 2026. MCD Art. 28 already encourages forbearance on mortgages.

### Cited Findings
- [US] (1) IN FORCE — FDCPA scope: "debt collector" covers those collecting debts "owed or due … another", and excludes "any officer or employee of a creditor while, in the name of the creditor, collecting debts for such creditor". — [15 U.S.C. 1692a](https://www.law.cornell.edu/uscode/text/15/1692a)
- [US] (1) IN FORCE — Regulation F (12 CFR 1006):
  - **§1006.6(b)(1)(i):** "a time before 8:00 a.m. and after 9:00 p.m. local time at the consumer's location is inconvenient", absent knowledge to the contrary. — [eCFR §1006.6](https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.6)
  - **§1006.6(d):** limits communications with third parties. — [eCFR §1006.6](https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.6)
  - **§1006.14(b)(2):** a collector is presumed compliant if it calls a person about a particular debt no more than **seven times within seven consecutive days** (plus a post-conversation limit), and presumed in violation if it exceeds this. — [eCFR §1006.14](https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.14)
  - **§1006.34:** validation information must be given in the initial communication or within 5 days. The validation period ends 30 days after receipt, and a written dispute in that period stops collection until verification is sent. — [eCFR §1006.34](https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.34)
- [US] (2) WITHDRAWN 12 May 2025:
  - CFPB Bulletin 2013-07 ("Prohibition of unfair, deceptive, or abusive acts or practices in the collection of consumer debts");
  - Reg F advisory opinions on time-barred debt, pay-to-pay fees and medical debt;
  - the 2023 abusiveness policy statement.
  The withdrawal notice is effective 12 May 2025, and the list page was last modified 22 Jul 2026. — [CFPB Withdrawn Guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/); [Federal Register 2025-08286](https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal)
  - (5) The UDAAP statutory prohibitions (Dodd-Frank §§1031/1036) and the FTC Act still apply; the statutory text was not re-read this session.
- [UK] (1) IN FORCE — CONC 7.3 (key rules effective 04/11/2024; CONC 7.3.2G and 7.3.8G updated 26/06/2026):
  - **7.3.4R:** treat customers "in or approaching arrears or in default with forbearance and due consideration". **7.3.4A G:** "approaching arrears" includes a customer saying they are at risk of missing a payment.
  - **7.3.4B R:** take account of the customer's individual circumstances.
  - **7.3.5G:** examples include suspending, reducing, waiving or cancelling interest or charges; deferring arrears; accepting token or no payments for a reasonable period; repayment plans; refinancing.
  - **7.3.5B R:** repayment arrangements must be sustainable, and **7.3.5C G** says a plan is unlikely to be sustainable if the customer cannot meet priority debts or essential living expenses.
  - **7.3.5D R:** income-and-expenditure assessments must be objective (Standard Financial Statement allowed).
  - **7.3.5I R:** keep forbearance under review.
  - **7.3.7A G:** tell customers about free, impartial debt advice, communicate its benefits and refer them (e.g. to MoneyHelper, or by direct call transfer).
  - **7.3.8G:** refusing a reasonable payment proposal is likely to breach Principle 6 or the Consumer Duty.
  - **7.3.9R:** no policy of refusing to negotiate.
  - **7.3.10R:** do not pressure a customer to pay in one or very few instalments, within unreasonably short periods, or by selling property or borrowing. — [CONC 7.3](https://www.handbook.fca.org.uk/handbook/CONC/7/3.html)
  - (5) The policy statement number for the Nov 2024 changes was not verified.
- [EU] (1) ADOPTED – NOT YET APPLICABLE — CCD2 (Directive (EU) 2023/2225):
  - **Art. 35(1):** creditors must "exercise, where appropriate, reasonable forbearance before enforcement proceedings are initiated", taking account of the consumer's circumstances.
  - **Art. 35(1) measures:** these "shall include modification of the existing terms", which may include extending the term, changing the credit type, deferring payments, reducing the rate, a payment holiday, partial repayments, currency conversion, or partial forgiveness and debt consolidation.
  - **Art. 35(3)–(4):** default charges limited to costs, and caps on additional charges where Member States allow them.
  - **Art. 18(8):** where the creditworthiness assessment involves automated processing, the consumer may obtain human intervention, a "clear and comprehensible explanation", express their view and request a review.
  - **Art. 18(9):** on rejection, the consumer must be told and, where relevant, referred to debt advisory services, and informed of any automated processing and the right to human assessment.
  - **Art. 48(1):** transposition by **20 Nov 2025**; "apply those measures from **20 November 2026**". — [CCD2](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023L2225)
- [EU] (1) IN FORCE — MCD 2014/17/EU Art. 28(1): Member States "shall adopt measures to encourage creditors to exercise reasonable forbearance before foreclosure proceedings are initiated". Default charges are capped at cost where Member States allow; there are best-price and post-foreclosure repayment measures. — [MCD](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0017)

### Inferences (practical consequences for the agent)
- (4) **Treat "I'm going to miss a payment" as approaching arrears (UK)** and as a forbearance trigger (EU MCD now; CCD2 from 20 Nov 2026). Offer options, signpost free debt advice, and never pressure the customer to borrow or sell assets.
- (4) **AI agents in collections:**
  - no repeated contact beyond policy;
  - respect contact-time windows (US third-party collectors: 8 a.m.–9 p.m. local; banks' own collections should follow similar UDAAP-safe practice);
  - no discussion of the debt with third parties;
  - disclose that the customer is talking to AI (EU Art. 50);
  - never exploit vulnerability (EU AI Act Art. 5(1)(b)).
- (4) **Income-and-expenditure checks** done by bots must be objective (CONC 7.3.5D R). Where possible, give the customer a record of the assessment to share with other lenders and debt advisers (CONC 7.3.7A(4) G, guidance not a rule).
- (4) **US validation disputes** (third-party collectors): once a written dispute is received within the validation period, collection stops until verification is sent. Route such disputes to the right team.

### Gaps
- CCD2 transposition status by Member State, and any postponement: no postponement found, but not exhaustively checked (5).
- UK BNPL/deferred-payment-credit regulation start date (2026) not verified (team 09).
- US state debt-collection laws not covered.

---

## 10. AI and chatbot-specific rules

### Takeaway
**EU:**
- AI Act Art. 50(1) (people must be told they are interacting with AI) applies from **2 Aug 2026**, unchanged by the Digital Omnibus on AI (Reg. (EU) 2026/1744, in force 27 Jul 2026).
- The Omnibus moved Annex III high-risk obligations (including **creditworthiness and credit scoring**) to **2 Dec 2027** and softened the Art. 4 AI-literacy duty.
- The Art. 5 prohibitions, including exploiting vulnerabilities, have applied since 2 Feb 2025.
- GDPR Art. 22 and (from Nov 2026) CCD2 Art. 18(8) give human-review rights. DORA (since 17 Jan 2025) governs ICT vendors, including AI providers.
- The agreed (not adopted) PSR adds a right to human support.

**UK:** no AI-specific rules. The FCA relies on the Consumer Duty and SM&CR (confirmed in Jun–Jul 2026, including the Mills Review).

**US:**
- The CFPB's June 2023 chatbot spotlight (doom loops, inaccuracy, failure to recognise disputes) is still published.
- The CFPB's AI adverse-action circulars were withdrawn in May 2025, but Reg B's "specific reasons" requirement still applies.

**Liability precedent:** a firm is responsible for what its chatbot says (Moffatt v. Air Canada).

### Cited Findings
- [EU] (1) IN FORCE (applies 2 Aug 2026) — AI Act Art. 50:
  - Art. 50(1): providers must design AI systems that "interact directly with natural persons" so people "are informed that they are interacting with an AI system, unless this is obvious from the point of view of a natural person who is reasonably well-informed, observant and circumspect".
  - Art. 50(5): the information must be given "in a clear and distinguishable manner at the latest at the time of the first interaction" and conform to accessibility requirements. — [AI Act Art. 50 (Service Desk, consolidated to 27 Jul 2026)](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- [EU] (1) — Art. 113 as amended by the Digital Omnibus on AI:
  - general application from 2 Aug 2026;
  - Chapters I–II from 2 Feb 2025, except the new prohibitions in Art. 5(1)(ba)–(bb), which apply from 2 Dec 2026;
  - high-risk obligations under Art. 6(2) / Annex III from **2 Dec 2027**, and under Art. 6(1) / Annex I from **2 Aug 2028**. — [AI Act Art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)
  - The Omnibus is Regulation (EU) 2026/1744 of 8 Jul 2026, published in the OJ 24 Jul 2026 and in force 27 Jul 2026. — [Lewis Silkin, 27 Jul 2026](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo); the earlier agreement (6 May 2026) is described by [Gibson Dunn, 27 May 2026](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/). (5) Confirm the regulation number on EUR-Lex.
  - Grace period: AI systems placed on the market before 2 Aug 2026 get until 2 Dec 2026 for the Art. 50(2) watermarking duty (from the agreement summary). The Art. 50(1) disclosure duty is unaffected. — [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [EU] (1) — Annex III point 5(b): high-risk includes AI "intended to be used to evaluate the creditworthiness of natural persons or establish their credit score, with the exception of AI systems used for the purpose of detecting financial fraud". — [AI Act Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)
- [EU] (1) IN FORCE, AMENDED — Art. 4: providers and deployers "shall take measures to support the development of AI literacy of their staff". This "does not require providers or deployers to guarantee any specific level of AI literacy". — [AI Act Art. 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)
- [EU] (1) IN FORCE — GDPR Art. 22 (see §7); CCD2 Art. 18(8)–(9) from 20 Nov 2026 (see §9).
- [EU] (1) IN FORCE since 17 Jan 2025 — DORA (Reg. (EU) 2022/2554):
  - ICT risk and third-party risk management;
  - a register of information on all ICT third-party arrangements;
  - EU oversight of critical ICT third-party providers (CTPPs), designated after 2025 criticality assessments. — [ESMA DORA page](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora); [EBA DORA page](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act)
- [EU] AGREED – NOT ADOPTED — PSR: "users must have access to human customer support (not only chatbots)". — [EP press release](https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees) The compromise text's Art. 53(1)(c) requires human support for reporting and unblocking instruments. — [Council ST 8221/26](https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf)
- [UK] (2) — FCA, 8 Jun 2026: "We have been clear that we are not going to introduce new regulations for AI. Instead, we'll rely on existing frameworks, including the Consumer Duty, the Senior Managers and Certification Regime (SM&CR)…" It also runs AI Live Testing (cohort 2). — [FCA blog](https://www.fca.org.uk/news/blogs/ai-financial-services-approach)
- [UK] (2) — Mills Review published 6 Jul 2026, with seven priority recommendations including agentic-finance foundations. The FCA's principles-based approach relies "on the Consumer Duty and Senior Managers Regime". — [FCA press release](https://www.fca.org.uk/news/press-releases/fca-publishes-landmark-review-impact-ai-retail-financial-services); [report PDF](https://www.fca.org.uk/publication/corporate/the-mills-review.pdf) (PDF not read)
- [UK] (1) — PRIN 2A.6 applies "regardless of the channel", so chatbots fall under consumer-support outcome rules (§5). — [PRIN 2A.6](https://www.handbook.fca.org.uk/handbook/PRIN/2A/6.html)
- [US] (2) — CFPB issue spotlight "Chatbots in consumer finance" (6 Jun 2023):
  - all top-10 commercial banks use chatbots; about 37% of the US population is estimated to have interacted with a bank chatbot in 2022;
  - risks: "Difficulties in recognizing and resolving people's disputes"; "Providing inaccurate, unreliable, or insufficient information"; "doom loops" with no "offramp to a human customer service representative"; "Hindering access to timely human intervention"; impersonation and phishing; treating chat logs as sensitive data;
  - "chatbots must comply with all applicable federal consumer financial laws". — [CFPB spotlight](https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/)
  - It is not on the CFPB Withdrawn Guidance list as of the 22 Jul 2026 page. Note that issue spotlights are research reports, not rules. — [CFPB Withdrawn Guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/)
- [US] (2) WITHDRAWN 12 May 2025 — CFPB Circular 2022-03 (adverse action and "complex algorithms") and Circular 2023-03. — [CFPB Withdrawn Guidance](https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/)
- [US] (1) IN FORCE — Reg B §1002.9: notice of action taken within 30 days of a completed application. The statement of reasons "must be specific and indicate the principal reason(s)"; references to internal standards or a failed score are insufficient. — [eCFR §1002.9](https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.9)
- [CA-BC] (precedent, persuasive only) — *Moffatt v. Air Canada*, 2024 BCCRT 149 (decided 14 Feb 2024, Tribunal Member C. Rivers):
  - para 27: the argument that a chatbot is "a separate legal entity that is responsible for its own actions … is a remarkable submission". "It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot."
  - para 28: Air Canada "did not take reasonable care to ensure its chatbot was accurate", and customers should not have to double-check one part of a website against another.
  - Damages: $650.88, for negligent misrepresentation. — [CRT decision PDF](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do)

### Inferences (practical consequences for the agent)
- (4) **Disclosure:** from 2 Aug 2026 every EU customer-facing AI agent (chat or voice) must say it is AI at the first interaction, clearly and accessibly. Doing the same in the UK and US is good practice under the Consumer Duty and UDAAP.
- (4) **Escalation:** design a guaranteed human route (no doom loops), with mandatory triggers. These cover complaints and disputes (Reg E/Reg Z/PSD2 errors), fraud, vulnerability, bereavement, financial difficulty, data-protection requests, and any request the bot cannot resolve. EU PSR requirements (once adopted) and UK PRIN 2A.6 make this a compliance matter.
- (4) **Accuracy and liability:** the bank owns the bot's statements (Moffatt reasoning; Consumer Duty; UDAAP). The bot should quote only approved policy and fee data, never invent legal rights or timelines, and say when it is unsure.
- (4) **Credit decisions:** a bot must not make or explain final credit decisions unless the bank has a lawful setup. That means EU high-risk AI obligations from Dec 2027, GDPR Art. 22, CCD2 Art. 18(8) from Nov 2026, and US Reg B specific reasons. The bot should route customers to human review and the formal notices.
- (4) **Governance:** AI vendors are ICT third parties under DORA (register, contracts, exit plans). Staff AI literacy (Art. 4) is still required in the EU, though softened.

### Gaps
- EU Commission guidelines and codes of practice on Art. 50 (e.g. the transparency code) not reviewed.
- Whether any UK FCA statement specifically addresses mandatory human access for chatbots: none found beyond PRIN 2A.6 and good-practice examples.
- Status of US federal AI policy affecting banks (e.g. 2025–2026 executive actions) not reviewed.

---

## 11. Summary comparison tables (rows = topic; Türkiye column to be completed from researcher 02)

Status key: **IF** = in force · **NYA** = adopted, not yet applicable · **AG** = agreed, not adopted · **W** = withdrawn guidance · (5) = verify.

### Table A — Payments, fraud and authentication

| Topic | EU | UK | US | Türkiye |
|---|---|---|---|---|
| Refund deadline, unauthorised payment | End of next business day; exception for suspected fraud reported in writing to the national authority (PSD2 Art. 73) **IF**. PSR: 15-business-day investigation route on justified suspicion **AG** | As soon as practicable, by end of next business day; exception if customer fraud is suspected and reported to a s.333A(2) person (PSRs reg 76) **IF** | Determine within 10 business days; otherwise provisional credit within 10 business days and up to 45 days (20 / 90 in special cases) (Reg E §1005.11) **IF** | |
| Payer liability cap | €50; all losses for fraud or intent/gross negligence; €0 if no SCA or after notification (Art. 74) **IF** | £35; same exceptions plus distance contracts (reg 77) **IF** | Debit/EFT: $50 if reported within 2 business days; up to $500 if later; unlimited for post-60-day transfers. Negligence irrelevant (§1005.6) **IF**. Credit card: $50 (§1026.12) **IF** | |
| Outer notification limit | 13 months (Art. 71). PSR: 18 months **AG** | 13 months (reg 74) | 60 days after statement (Reg E); written billing-error notice within 60 days (Reg Z) | |
| Burden of proof | On the bank; an authentication log alone is not proof (Art. 72) | Same (reg 75) | The bank must investigate; police report cannot be a precondition (CFPB FAQs, (2)) | |
| Credit-card disputes | National law plus scheme chargebacks (3) | Consumer Credit Act s.75 not reviewed (5) plus chargebacks (3) | Reg Z billing errors (written, 60 days, ≤2 cycles / 90 days) and claims and defences | |
| Card-scheme zero liability | Scheme policy (3) | Scheme policy (3) | Visa: replace funds within 5 business days, provisional (3) | |
| Misdirected payment (wrong identifier) | Bank not liable; reasonable recovery efforts; information on written request (Art. 88) | Same (reg 90) | Wires: UCC 4A-207 (rely on number). Remittances: 180/90 days; §1005.33(h) conditions | |
| Payee name check | VoP mandatory: 9 Oct 2025 (euro area), 9 Jul 2027 (non-euro); refund if bank fails (IPR Art. 5c) **IF**. All credit transfers under PSR Art. 50 **AG** | Confirmation of Payee widely mandated (PSR direction; 350+ additional firms by end-Oct 2024 per PSR; Bank of Ireland UK fined Feb 2026 for missing the deadline) **IF** (5 on direction number and details) | No federal requirement (none found) | |
| APP / scam reimbursement | None general under PSD2. PSR: full refund for bank-impersonation fraud, police report required, 15 business days (Art. 59) **AG** | Mandatory since 7 Oct 2024: FPS/CHAPS; £85k cap; ≤£100 excess; 13 months; 5 business days (≤35 with stop-the-clock); consumer standard of caution; no exceptions for vulnerable **IF**. PSR functions moving to FCA (Bill, May 2026) | No federal right for customer-authorised scams; credential-phishing transfers are unauthorised under Reg E (FAQs). NY AG v. EWS proceeding (MTD denied 20 Jul 2026) | |
| Fraud-related payment delay | PSR: receiving bank to freeze suspicious transactions **AG** | Delay up to 4th business day with notice of reasons unless unlawful (reg 86(2A)–(2D)) **IF** since 30 Oct 2024 | Holds under bank policy; Reg CC not reviewed (5) | |
| SCA / authentication | 2 of 3 factors + dynamic linking (PSD2 Art. 97; RTS exemptions: €50/€150/5 contactless; €30/€100/5 remote; TRA up to €500) **IF**. PSR: 4-hour delay on remote app activation and limit increases **AG** | SCA via reg 100 + FCA SCA-RTS **IF** (thresholds not re-checked, 5) | Risk-based; FFIEC 2021 guidance: layered security, MFA, call-centre risks (2) | |

### Table B — Complaints, conduct, vulnerability, accessibility

| Topic | EU | UK | US | Türkiye |
|---|---|---|---|---|
| Complaint response deadline | Payment services: 15 business days; holding reply then ≤35 (PSD2 Art. 101) **IF**. Others: national law + JC 2018 35 (2) | 8 weeks (DISP 1.6.2R); payment/e-money: 15/35 business days (DISP 1.6.2AR); summary resolution if closed by 3rd business day (DISP 1.5) **IF** | No general statutory deadline; Reg E/Z clocks; CFPB portal: ~15 days, final 60 (2) | |
| ADR / ombudsman | Named ADR body required (PSD2 Art. 101(3)); ADR Directive amended by 2025/2647 (in force 19 Jan 2026; transposition ~2028) **NYA**; mandatory bank participation under PSR **AG** | FOS: 6 months from final response; 6 years / 3 years limits; award limit £455k (from 1 Apr 2026) | No ombudsman; CFPB/state AG complaints; litigation | |
| Complaint governance | JC 2018 35: policy, function, register, reporting, root cause, plain language (2) | DISP recording and twice-yearly reporting; DISP 1.10 future version 31 Dec 2026 (5) | Bank-regulator expectations (not reviewed, 5) | |
| Customer-support conduct standard | No single equivalent; PSR human support **AG** | Consumer Duty PRIN 2A.6: no unreasonable barriers; all channels incl. social media and outsourced support **IF** | UDAAP (Dodd-Frank) **IF**; CFPB chatbot spotlight (2) | |
| Vulnerable customers | No EU-wide guideline; AI Act Art. 5(1)(b) bans exploiting vulnerability **IF**; EBA consumer-trends work (2) | FG21/1 (4 drivers) (2); FCA review 7 Mar 2025: no new rules; APP exceptions do not apply to vulnerable consumers **IF** | Interagency elder-exploitation statement (Dec 2024, rev. Jun 2026): trusted contacts, holds (2) | |
| Accessibility | EAA applies to consumer banking from 28 Jun 2025: WCAG-type POUR principles, B2 language, accessible support services; transition to 2030 / 20 years for terminals **IF** | Equality Act s.29(7) reasonable adjustments **IF**; Consumer Duty needs | ADA Title III (DOJ guidance 2022, (2)); no Title III web rule (5) | |

### Table C — Data, AML, collections, AI

| Topic | EU | UK | US | Türkiye |
|---|---|---|---|---|
| SAR (data subject request) deadline | 1 month + 2 months (GDPR Art. 12(3)) **IF** | UK GDPR + DUAA 2025: stop-the-clock; reasonable and proportionate searches (commenced 2026, 5) **IF** | No general access right for banking data (GLBA privacy notices) (5) | |
| Automated decisions | GDPR Art. 22 (human intervention, contest) **IF**; CCD2 Art. 18(8) from 20 Nov 2026 **NYA** | DUAA reformed ADM with safeguards **IF** (5 on dates) | Reg B specific adverse-action reasons (§1002.9) **IF**; CFPB AI circulars **W** | |
| Call recording | ePrivacy Art. 5(2) business-evidence recording + GDPR lawful basis **IF** | SYSC 10A only for investment business (records kept 5 years, up to 7 on FCA request) **IF**; otherwise UK GDPR plus UK interception/monitoring rules (5) | One-party consent federally (18 U.S.C. 2511(2)(d)); some states all-party (5) | |
| Card data on calls | PCI DSS v4.0.1: no CVV after authorisation, including audio (FAQ 1210) (3) | Same (3) | Same (3) | |
| Tipping-off | AMLD Art. 39 **IF** → AMLR Art. 73 from 10 Jul 2027 **NYA** | POCA s.333A **IF**; DAML 7 working days / 31-day moratorium (s.335) | 31 U.S.C. 5318(g)(2); 31 CFR 1020.320(e) **IF** | |
| Explaining blocks and closures | PSD2 Art. 68(3): reasons unless security or law prohibits | Closure: 90 days + reasons + complaint/FOS info for contracts from 28 Apr 2026, with financial-crime exceptions (SI 2025/688) **IF** | No federal reason-giving duty for closures found (5) | |
| Collections conduct | CCD2 Art. 35 forbearance from 20 Nov 2026 **NYA**; MCD Art. 28 **IF** | CONC 7.3 forbearance, sustainable plans, debt-advice referral, no pressure (strengthened 4 Nov 2024) **IF** | Reg F (third-party collectors): 7-in-7, 8 a.m.–9 p.m., validation **IF**; CFPB Bulletin 2013-07 **W**; UDAAP statute **IF** | |
| AI disclosure | AI Act Art. 50(1) from 2 Aug 2026 **IF** | No AI-specific rule; Consumer Duty (2) | No federal rule; UDAAP / state laws (5) | |
| AI high-risk (credit scoring) | Annex III 5(b): obligations from 2 Dec 2027 (Omnibus) **NYA** | No specific rule; Consumer Duty / SM&CR (2) | Reg B / ECOA; fair-lending law | |
| Human access / chatbots | PSR: human support beyond chatbots **AG** | PRIN 2A.6 + FCA good practice: route complex or vulnerable cases to humans (2) | CFPB 2023 spotlight on doom loops (2) | |
| Chatbot misinformation | General civil and consumer law; no EU-specific chatbot-liability rule identified in this session (5) | Consumer Duty; FOS "fair and reasonable" approach (5) | UDAAP; *Moffatt* (Canada, persuasive only) | |

---

## 12. Source register

All accessed 10 Oct 2026. "Read" means relevant parts read in full from the official text; "summary" means content taken from a search-result summary only.

| # | Title | Publisher | Date (pub. / last updated) | Jur. | URL | Notes |
|---|---|---|---|---|---|---|
| 1 | Directive (EU) 2015/2366 (PSD2) | EUR-Lex / EU | OJ L 337, 23.12.2015 (original text) | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366 | Read Arts 4(30), 68–74, 76–77, 88, 97, 101 |
| 2 | Regulation (EU) 2024/886 (Instant Payments; VoP Art. 5c, 5d) | EUR-Lex | 2024 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R0886 | Read |
| 3 | Delegated Regulation (EU) 2018/389 (SCA RTS) | EUR-Lex | 2018 (original) | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389 | Read Arts 11, 13, 16, 18; amendments not checked |
| 4 | PSR — Council final compromise text ST 8221/26 | Council of the EU | Apr 2026 (published 23 Apr 2026) | EU | https://data.consilium.europa.eu/doc/document/ST-8221-2026-INIT/en/pdf | Read Arts 50–60, 94, 112; LIMITE; numbering may change |
| 5 | Payment services deal (press release) | European Parliament | 27 Nov 2025 | EU | https://www.europarl.europa.eu/news/en/press-room/20251121IPR31540/payment-services-deal-more-protection-from-online-fraud-and-hidden-fees | Read |
| 6 | Procedure file 2023/0210(COD) (PSR) | EP Legislative Observatory | accessed 10 Oct 2026 | EU | https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD) | Read; status "Awaiting Council's 1st reading position" |
| 7 | PSD3 and the PSR: Key Developments | Morrison Foerster | 30 Apr 2026 | EU | https://www.mofo.com/resources/insights/260430-psd3-and-the-payment-services-regulation-key-developments | Law firm; APP statement conflicts with official text |
| 8 | PSD3 and PSR published | Matheson | 29 Apr 2026 | EU | https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/ | Law firm |
| 9 | JC Guidelines on complaints-handling (JC 2018 35) | ESMA / EBA | 31 Jul 2018; applies from 1 May 2019 (new institutions) | EU | https://www.eba.europa.eu/documents/10180/2381463/Joint+Committee+Guidelines+on+complaints-handling+%28JC+2018+35%29_EN.pdf/cd6e3328-7442-4582-8b68-819346d200ec | Read |
| 10 | Directive (EU) 2025/2647 (ADR revision) — commentary | EAPIL; Bird & Bird; Commission event page | Jan 2026; 2026; 1 Oct 2026 | EU | https://eapil.org/2026/01/23/directive-eu-2025-2647-amending-the-adr-framework-for-consumer-disputes/ ; https://cm.twobirds.com/en/insights/2026/eu-the-new-alternative-dispute-resolution-framework--directive-20252647 ; https://commission.europa.eu/get-involved/events/adr-transposition-workshop-2026-10-01_en | Summary; OJ text not read |
| 11 | Directive (EU) 2019/882 (European Accessibility Act) | EUR-Lex | OJ L 151, 7.6.2019 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882 | Read Arts 2, 3(28), 4(5), 31, 32; Annex I III(d), IV(e) |
| 12 | Regulation (EU) 2016/679 (GDPR) | EUR-Lex | 2016 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 | Read Arts 5, 12, 22; recitals 64, 71 |
| 13 | Directive 2002/58/EC (ePrivacy) | EUR-Lex | 2002 (original) | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32002L0058 | Read Art. 5(2) |
| 14 | Directive (EU) 2015/849 (AMLD) | EUR-Lex | 2015 (original) | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L0849 | Read Art. 39 |
| 15 | Regulation (EU) 2024/1624 (AMLR) | EUR-Lex | 2024 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1624 | Read Art. 73 and application article |
| 16 | Directive (EU) 2023/2225 (CCD2) | EUR-Lex | 2023 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023L2225 | Read Arts 18(8)–(9), 35, 48 |
| 17 | Directive 2014/17/EU (MCD) | EUR-Lex | 2014 | EU | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0017 | Read Art. 28 |
| 18 | AI Act Arts 4, 5, 50, 113, Annex III (consolidated to 27 Jul 2026) | European Commission AI Act Service Desk | consolidated 27 Jul 2026 | EU | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50 (also /article-4, /article-5, /article-113, /annex-3) | Read; marks Omnibus amendments |
| 19 | EU AI Act Omnibus Agreement | Gibson Dunn | 27 May 2026 | EU | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ | Law firm; pre-adoption |
| 20 | The Digital Omnibus on AI enters into force today | Lewis Silkin | 27 Jul 2026 | EU | https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo | Summary (Reg. 2026/1744; verify on EUR-Lex) |
| 21 | DORA pages | ESMA; EBA | ongoing | EU | https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora ; https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act | Summary |
| 22 | EBA Consumer Trends Report 2024/25 | EBA | Mar 2025 | EU | https://www.eba.europa.eu/sites/default/files/2025-03/514b651f-091b-42d3-b738-1fae79264044/Consumer%20Trends%20Report%202024-2025.pdf | Summary |
| 23 | Payment Services Regulations 2017, regs 74, 75, 76, 77, 86, 90 | legislation.gov.uk | as amended (reg 86 amended 30 Oct 2024) | UK | https://www.legislation.gov.uk/uksi/2017/752/regulation/76 (change the number for others) | Read |
| 24 | SI 2024/1013 Payment Services (Amendment) Regs 2024 | legislation.gov.uk | in force 30 Oct 2024 | UK | https://www.legislation.gov.uk/uksi/2024/1013/made | Read commencement |
| 25 | SI 2025/688 Payment Services and Payment Accounts (Contract Termination) (Amendment) Regs 2025 | legislation.gov.uk | in force 28 Apr 2026 | UK | https://www.legislation.gov.uk/uksi/2025/688/made | Read |
| 26 | Proceeds of Crime Act 2002 ss.333A, 335 | legislation.gov.uk | up to date to 9 Oct 2026 | UK | https://www.legislation.gov.uk/ukpga/2002/29/section/333A ; https://www.legislation.gov.uk/ukpga/2002/29/section/335 | Read |
| 27 | Equality Act 2010 s.29 | legislation.gov.uk | current | UK | https://www.legislation.gov.uk/ukpga/2010/15/section/29 | Read s.29(7) |
| 28 | FCA Handbook DISP 1.5, 1.6, 1.10, 2.8 | FCA | updated 01/04/2018; —; 07/04/2026 (future 31/12/2026); 13/01/2018 | UK | https://www.handbook.fca.org.uk/handbook/DISP/1/6.html (and /1/5, /1/10, /2/8) | Read |
| 29 | FCA Handbook PRIN 2A.6 | FCA | updated 26/06/2026 | UK | https://www.handbook.fca.org.uk/handbook/PRIN/2A/6.html | Read |
| 30 | FCA Handbook CONC 7.3 | FCA | key rules 04/11/2024; parts 26/06/2026 | UK | https://www.handbook.fca.org.uk/handbook/CONC/7/3.html | Read |
| 31 | FCA Handbook SYSC 10A.1 | FCA | updated 23/10/2025 | UK | https://www.handbook.fca.org.uk/handbook/SYSC/10A/1.html | Read scope and retention |
| 32 | FG21/1 Guidance on fair treatment of vulnerable customers | FCA | Feb 2021 | UK | https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf | Read paras 1.1, 2.5 |
| 33 | Firms' treatment of customers in vulnerable circumstances – review | FCA | 7 Mar 2025 | UK | https://www.fca.org.uk/publications/multi-firm-reviews/firms-treatment-vulnerable-customers | Summary |
| 34 | Consumer support outcome: good practices and areas for improvement | FCA | 7 Mar 2025 / updated 10 Jul 2026 | UK | https://www.fca.org.uk/publications/good-and-poor-practice/consumer-support-outcome-good-practices-areas-improvement | Fetched (quotes) |
| 35 | AI in financial services: shaping our approach (blog) | FCA | 8 Jun 2026 | UK | https://www.fca.org.uk/news/blogs/ai-financial-services-approach | Read |
| 36 | FCA publishes landmark review (Mills Review) | FCA | 6 Jul 2026 | UK | https://www.fca.org.uk/news/press-releases/fca-publishes-landmark-review-impact-ai-retail-financial-services | Read; report PDF not read |
| 37 | APP fraud reimbursement protections | PSR | 2024 page (dated FOS figure) | UK | https://www.psr.org.uk/information-for-consumers/app-fraud-reimbursement-protections/ | Read |
| 38 | Fraud victims get £243 million back… | PSR | 9 Jul 2026 | UK | https://www.psr.org.uk/news-and-updates/latest-news/news/fraud-victims-get-243-million-back-as-psr-marks-a-year-of-progress/ | Read |
| 39 | APP scams reimbursement dashboard | PSR | updated 30 Jul 2026 | UK | https://www.psr.org.uk/information-for-consumers/app-scams-reimbursement-dashboard/ | Fetched summary |
| 40 | Consumer standard of caution guidance; PS24/7; PS25/5 | PSR | Dec 2023; Oct 2024; May 2025 | UK | https://www.psr.org.uk/media/as3a0xan/sr1-consumer-standard-of-caution-guidance-dec-2023.pdf ; https://www.psr.org.uk/publications/policy-statements/ps247-faster-payments-app-scams-reimbursement-requirement-confirming-the-maximum-level-of-reimbursement/ ; https://www.psr.org.uk/media/rhelv4op/ps25-5-app-scams-reimbursement-consolidated-policy-statement-may-2025.pdf | Summary only |
| 41 | FCA confirms increase to award limits | Financial Ombudsman Service | 2026 (effective 1 Apr 2026) | UK | https://www.financial-ombudsman.org.uk/news/fca-confirms-increase-award-limits-2 | Summary |
| 42 | DUAA 2025 data protection changes; ICO SAR guidance | GOV.UK; ICO | 27 Jun 2025; ICO updated (16 Jul 2026 per search) | UK | https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes ; https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/right-of-access/what-should-we-consider-when-responding-to-a-request/ | Fetched / summary |
| 43 | Major provisions of the DUAA take effect | Mills & Reeve | 6 Feb 2026 | UK | https://www.mfmac.com/insights/manufacturing-media-technology/major-provisions-of-the-uk-data-use-and-access-act-2025-take-effect/ | Secondary (commencement dates) |
| 44 | A&O Shearman FS Horizon Report 2026 — payments | A&O Shearman | 2026 | UK | https://www.aoshearman.com/en/insights/financial-services-horizon-report-2026/payment-services-and-payment-systems | Law firm |
| 45 | 12 CFR 1005.6, 1005.11, 1005.33 (Reg E) | eCFR (via official API) | current at 10 Oct 2026 | US | https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.11 | Read |
| 46 | 12 CFR 1026.12, 1026.13 (Reg Z) | eCFR | current | US | https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.13 | Read |
| 47 | 12 CFR 1006.6, 1006.14, 1006.34 (Reg F) | eCFR | current | US | https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.14 | Read |
| 48 | 12 CFR 1002.9 (Reg B) | eCFR | current | US | https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.9 | Read |
| 49 | 31 CFR 1020.320 (bank SARs) | eCFR | current | US | https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320 | Read (e) |
| 50 | 31 U.S.C. 5318; 15 U.S.C. 6821; 15 U.S.C. 1692a; 18 U.S.C. 2511; UCC 4A-207 | Cornell LII (US Code / UCC text) | current | US | https://www.law.cornell.edu/uscode/text/31/5318 (and /15/6821, /15/1692a, /18/2511, /ucc/4A/4A-207) | Read; secondary host of official text |
| 51 | Electronic Fund Transfers FAQs | CFPB | answers updated 2021; page incl. 15 Jan 2025 update | US | https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/electronic-fund-transfers-faqs/ | Read |
| 52 | Withdrawn Guidance | CFPB | last modified 22 Jul 2026 | US | https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/ | Read |
| 53 | Interpretive Rules, Policy Statements, and Advisory Opinions; Withdrawal | Federal Register | 12 May 2025 | US | https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal | Not opened (cited via CFPB page) |
| 54 | Chatbots in consumer finance (issue spotlight) | CFPB | 6 Jun 2023 | US | https://www.consumerfinance.gov/data-research/research-reports/chatbots-in-consumer-finance/chatbots-in-consumer-finance/ | Read |
| 55 | Complaint process | CFPB | current | US | https://www.consumerfinance.gov/complaint/process/ | Read |
| 56 | OCC Bulletin 2021-36 (FFIEC authentication guidance) | OCC | 11 Aug 2021 | US | https://occ.treas.gov/news-issuances/bulletins/2021/bulletin-2021-36.html | Read; FFIEC PDF CAPTCHA-blocked |
| 57 | Interagency Statement on Elder Financial Exploitation (FIL) | FDIC et al. | 4 Dec 2024; revised 2 Jun 2026 | US | https://www.fdic.gov/news/financial-institution-letters/2024/agencies-issue-interagency-statement-elder-financial | Fetched |
| 58 | Third court rules against administration over CFPB funding | ABA Banking Journal | 28 Sep 2026 | US | https://bankingjournal.aba.com/2026/09/third-court-rules-against-trump-administration-over-cfpb-funding/ | Trade press |
| 59 | NY court refuses to dismiss AG case against Zelle operator | Ballard Spahr (Consumer Finance Monitor) | 31 Jul 2026 | US | https://www.consumerfinancemonitor.com/2026/07/31/new-york-court-refuses-to-dismiss-attorney-generals-sweeping-fraud-case-against-zelle-operator-early-warning-services/ | Law-firm blog |
| 60 | New York is writing America's Zelle fraud rules | Forbes | 27 Jul 2026 | US | https://www.forbes.com/sites/zennonkapron/2026/07/27/new-york-is-writing-americas-zelle-fraud-rules-one-lawsuit-at-a-time/ | Press; context only |
| 61 | AI is supercharging money scams | Washington Post | 14 Sep 2026 | US | https://www.washingtonpost.com/ripple/2026/09/14/ai-is-supercharging-money-scams-heres-what-you-can-do-to-protect-yourself/ | Press (CFPB suit dropped Mar 2025) |
| 62 | DOJ issues web accessibility guidance under the ADA | US Access Board | 21 Mar 2022 | US | https://www.access-board.gov/news/2022/03/21/department-of-justice-issues-web-accessibility-guidance-under-the-ada/ | Summary |
| 63 | Visa Zero Liability Policy | Visa | current | US/INTL | https://www.visa.com/en-us/personal/security/zero-liability-policy.html | Fetched |
| 64 | FAQ 1210: audio recordings and SAD | PCI SSC | June 2025 | INTL | https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/are-audio-voice-recordings-permitted-to-contain-sensitive-authentication-data/ | Fetched (verbatim) |
| 65 | Just Published: PCI DSS v4.0.1 | PCI SSC blog | June 2024 | INTL | https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 | Summary |
| 66 | Protecting Telephone-Based Payment Card Data (Info Supplement v3.0) | PCI SSC | Nov 2018 | INTL | https://listings.pcisecuritystandards.org/documents/Protecting_Telephone_Based_Payment_Card_Data_v3-0_nov_2018.pdf | Not read |
| 67 | Moffatt v. Air Canada, 2024 BCCRT 149 | BC Civil Resolution Tribunal | 14 Feb 2024 | CA-BC | https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do | Read paras 1–3, 27–28 |
| 68 | AB–PSD2'yi takip eden ikincil mevzuat yürürlüğe girdi | Moroğlu Arseven | 2021 article | TR-context | https://www.morogluarseven.com/tr/insights/yayinlar/makaleler/odeme-hizmetleri-ve-e-para-ihracina-iliskin-ab-psd2yi-takip-eden-ikincil-mevzuat-duzenlemeleri-yururluge-girdi/ | Read intro |

**[TR-context] note for the writer (not Turkish law analysis).** Turkish practitioners describe Law No. 6493 as corresponding to PSD1. Law No. 7192 (published 22 Nov 2019, effective 1 Jan 2020) added payment-initiation and account-information services "in parallel with PSD2". The TCMB Regulation on Payment Services and E-Money Issuance and Payment Service Providers, with its communiqué, entered into force on 1 Dec 2021, "uyumlu şekilde" with PSD2. — [Moroğlu Arseven](https://www.morogluarseven.com/tr/insights/yayinlar/makaleler/odeme-hizmetleri-ve-e-para-ihracina-iliskin-ab-psd2yi-takip-eden-ikincil-mevzuat-duzenlemeleri-yururluge-girdi/); [Erdem & Erdem (snippet)](https://www.erdem-erdem.av.tr/bilgi-bankasi/avrupa-birligi-odeme-hizmetleri-direktifi-ve-turk-odeme-sistemleri-mevzuatina-etkileri). The terms "ödeme hizmeti kullanıcısı" (payment service user) and "ödeme emri başlatma hizmeti" (payment initiation service) appear in that source. Researcher 02 should supply the official Turkish equivalents for "unauthorised transaction", "SCA" and "verification of payee" (5).

---

## 13. Open questions / unverified items / items needing institution-specific confirmation

1. **EU PSD3/PSR adoption timing.** OEIL (accessed 10 Oct 2026) shows "Awaiting Council's 1st reading position" and an indicative EP plenary on 14 Dec 2026. Confirm the final article numbers, OJ publication date, and the 21/27-month application dates once adopted.
2. **Digital Omnibus on AI.** Confirm the regulation number (reported as 2026/1744), the OJ reference, and the exact transitional rules for Art. 50(2) on EUR-Lex.
3. **UK PSR→FCA.** Status of the Financial Services and Markets Bill (introduced May 2026). Check whether APP reimbursement rules move into the FCA Handbook, and any change to the £85k cap, the excess or the consumer standard of caution after the 2026 Frontier Economics evaluation.
4. **UK DUAA commencement.** Verify the exact commencement regulations and dates for the SAR and ADM provisions (secondary sources say 5 Feb 2026 and 19 Jun 2026).
5. **DISP 1.10 future version (31 Dec 2026)** and any FCA/FOS complaint-handling reforms (team 04).
6. **CFPB.** Operational capacity in late 2026 (funding litigation in three courts). Check whether any Reg E, Reg F or UDAAP guidance was withdrawn or changed after 22 Jul 2026, and the nature of the 2 Jun 2026 revision to the interagency elder-exploitation statement.
7. **US scam reimbursement.** Outcome or appeal of *NY v. Early Warning Services*. Any state statutes mandating APP-type reimbursement (none found).
8. **EU VoP operations.** Check the EPC VoP scheme rulebook response categories and whether non-euro Member States brought forward their 9 Jul 2027 deadline.
9. **PSD2 national variations:** reduced €50 caps, the designated "relevant national authority" (Art. 73), and national complaint deadlines more favourable than 15 business days.
10. **UK SI 2025/688 interpretation.** Does the "serious crime" exception (reg 51C(c)) cover typical AML exits? How should banks word reasons without tipping off? This needs legal or MLRO confirmation per bank.
11. **US call-recording consent by state** (all-party states) and bank-specific recording disclosures. Needs institution and legal confirmation.
12. **PCI telephone controls.** The bank's chosen method (DTMF masking, IVR, pause-and-resume plus compensating controls) must be confirmed per institution; QSA-dependent.
13. **Items flagged (5)** that could not be verified in this session: the FCA Glossary "complaint" definition text; Equality Act s.20/Sch. 2 wording; Section 508 and Title III rule status; GLBA Safeguards / Reg P details; UDAAP statutory text; AMLA dates; UK Terrorism Act s.21D; OFAC customer-communication practice; FIN-NET current role; the CONC policy-statement number for 4 Nov 2024; PSR CoP direction details.
14. **Institution-specific confirmations for the playbook:**
    - each bank's approved neutral wording for holds, freezes and closures;
    - whether the bank applies the UK £100 APP excess;
    - scheme chargeback timelines used in scripts;
    - its Reg E written-confirmation policy;
    - its human-handoff SLAs for the AI agent;
    - its AI-disclosure wording (EU Art. 50) and accessibility (B2-level) standards.
