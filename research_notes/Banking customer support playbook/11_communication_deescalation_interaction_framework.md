# Communication, De-escalation, Vulnerable Customers, Interaction Framework and Channels (Researcher 11)

Banking customer-support playbook for an AI agent, including a voice agent. Situation as of 2026-10-10. Sources were accessed on 2026-10-10 unless stated otherwise.

**Tag legend (used throughout):** [T1-Law] law/regulation · [T2-Guidance] supervisory guidance · [T3-Practice] common industry practice · [T4-Research] recommended practice backed by research · [T5-Verify] assumption/opinion/inference needing verification. **Jurisdiction labels:** [UK] [EU] [US] [TR] [Intl] (international standard or multi-country research). A rule from one jurisdiction is never presented as universal.

**Safety rule applied throughout:** no pattern in these notes asks a customer to disclose a PIN, full password, CVV/CVC or one-time code, give remote access, disable security controls or bypass authentication.

**Evidence-quality note:** Most of the research cited here is experimental or survey research from general service settings (hotels, telecoms, retail, social media). Applying it to banking or to an AI agent is an inference and is labelled that way. The named de-escalation mnemonics (HEAT, HEARD, LEAP, LEAPS) are practitioner models with no peer-reviewed validation found in customer service (see §4).

---

## 1. What does research say drives customer satisfaction and effort in service interactions?

### Takeaway
The strongest evidence points the same way. Service interactions mostly *destroy* loyalty rather than create it, and the main lever is low effort: first-time resolution, no repeated contacts, no re-explaining, no channel-hopping and no unexplained transfers. In complaints, *how* people are treated (interactional and procedural justice) matters about as much as the outcome. The "service recovery paradox" holds only weakly: it raises satisfaction but not repurchase or word of mouth. Apology, empathy, explanation quality and concrete, first-person language each have experimental support. Banking-specific industry data for 2026 shows satisfaction with human and automated channels falling during the year, and puts problem resolution and "clarity and confidence" in routine moments at the centre.

### Cited Findings
**Customer effort (industry research, labelled as such)**
- [T4-Research][Intl] CEB's Customer Contact Council surveyed more than 75,000 B2C and B2B customers over three years about non-face-to-face interactions (phone, IVR, web, chat, email). The sample spanned dozens of industries, including banking, in North America, Europe, South Africa, Australia and New Zealand. Note that HBR is a practitioner journal: this is proprietary survey research, not peer-reviewed. — [HBR, Dixon, Freeman & Toman, "Stop Trying to Delight Your Customers", Jul–Aug 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers) (paywalled; read via [reproduction PDF](https://www.satoriconsultinginc.ca/wp-content/uploads/2020/05/Harvard_Business_Review-Stop_Trying_to_Delight_Your_Customers.pdf))
- Findings from that article:
  - 89 of 100 service heads said their main strategy was to exceed expectations, yet 84% of customers said their expectations had *not* been exceeded.
  - 20% of "satisfied" customers intended to leave, and 28% of "dissatisfied" customers intended to stay.
  - "Customers are four times more likely to leave a service interaction disloyal than loyal." — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- Effort obstacles customers reported: 56% had to re-explain an issue, 57% had to switch from web to phone, 59% were transferred, 59% spent moderate-to-high effort, and 62% had to contact the company repeatedly. — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- 22% of repeat calls involved *downstream* issues related to the original problem. Bell Canada's "forward resolution" (anticipating the next issue) cut calls per event by 16% and churn by 6% (company anecdote). — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- 24% of repeat calls stemmed from "emotional disconnects": the customer did not trust the rep's information, did not like the answer, or felt the rep was "hiding behind general company policy". — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- Language reframing:
  - Osram Sylvania coached reps away from "can't", "won't" and "don't". For example, "We don't have that item in stock" became "We'll have stock availability for that item in two weeks", and its Customer Effort Score (CES) fell from 2.8 to 2.2.
  - LoyaltyOne trained reps to position a disappointing outcome around the customer's stated goal, and repeat contacts fell 11%. Both are company anecdotes. — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- Company anecdote: Nedbank (South Africa) ran an "AskOnce" promise, under which the rep who answers owns the issue end to end. — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- CES was measured with the question "How much effort did you personally have to put forth to handle your request?" (1–5). 81% of customers who had a hard time resolving their problem reported an intention to spread negative word of mouth. — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- [T4-Research][Intl] Gartner (2020): customers with a low-effort resolution are 61% likely to stay, versus 37% after a high-effort experience. "At best, a great customer service experience can only mitigate disloyalty – not make customers more loyal." About 40% will still leave even after a high-quality service experience. — [Gartner press release, 19 Aug 2020](https://www.gartner.com/en/newsroom/press-releases/2020-08-19-gartner-reveals-two-actions-customer-service-leaders-)
- [T4-Research][Intl] Gartner headline (title only; body not accessible, HTTP 403): "Gartner Survey Finds 62 Percent of Customer Service Channel Transitions Are High Effort". — [Gartner press release, 11 Jul 2023](https://www.gartner.com/en/newsroom/press-releases/2023-07-11-gartner-survey-finds-62-percent-of-customer-service-channel-transitions-are-high-effort)

**Justice and complaint handling (peer-reviewed)**
- [T4-Research][Intl] Most complaining customers were dissatisfied with how their complaint was handled. Customers judge complaint handling on outcomes (distributive justice), procedures (procedural justice) and interpersonal treatment (interactional justice). Satisfaction with complaint handling directly drives trust and commitment, and prior good experiences cushion poor handling only "to a limited extent". — [Tax, Brown & Chandrashekaran, Journal of Marketing 62(2), Apr 1998](https://doi.org/10.1177/002224299806200205)
- [T4-Research][Intl] A meta-analysis traced the path: organisational responses (compensation, employee behaviour, procedures) → justice perceptions → satisfaction → loyalty and word of mouth. Distributive justice drives *transaction-specific* satisfaction. *Cumulative* satisfaction, the main antecedent of loyalty, depends slightly more on interactional than on distributive justice, especially for non-monetary failures and service industries. — [Gelbrich & Roschk, Journal of Service Research 14(1), 2011 (online Dec 2010)](https://doi.org/10.1177/1094670510387914)
- [T4-Research][Intl] A review framework sets out six dimensions of the organisational response to complaints: timeliness, facilitation, redress, apology, credibility and attentiveness. — [Davidow, Journal of Service Research, 2003](https://doi.org/10.1177/1094670502238917)
- [T4-Research][Intl] The service recovery paradox (recovered customers ending up more satisfied than if nothing had failed) had a significant positive cumulative effect on satisfaction. It had *no significant effect* on repurchase intentions, word of mouth or corporate image, and results varied by study design. — [de Matos, Henrique & Rossi, Journal of Service Research, Aug 2007](https://doi.org/10.1177/1094670507303012)

**Apology, appreciation, explanation, empathy, language (peer-reviewed)**
- [T4-Research][Intl] An apology works through its *delivery*, not its mere presence. Empathy, intensity and timing each affect recovery satisfaction, with empathy strongest. A late apology lowers satisfaction. For process failures the apology's effect size is comparable to compensation. — [Roschk & Kaiser, Marketing Letters 24(3):293–309, 2013](https://ideas.repec.org/a/kap/mktlet/v24y2013i3p293-309.html)
- [T4-Research][Intl] Saying "thank you" (appreciation) was often *more* effective than saying "sorry" in initial recovery, because it raises the customer's state self-esteem. It was as effective as combined appreciation-plus-apology messages. — [You, Yang, Wang & Deng, Journal of Marketing, 2020](https://doi.org/10.1177/0022242919889894)
- [T4-Research][Intl] Explanation type and quality interact. Apologies and excuses produced higher satisfaction than justifications or referential accounts, but only when the explanation was perceived as high quality. — [Bradley & Sparks, Journal of Services Marketing, 2012](https://doi.org/10.1108/08876041211199715)
- [T4-Research][Intl] Agents who refer to themselves as "I" rather than "we" are perceived as more empathic and more agentic, which raises satisfaction and purchase. Customer-referencing "you" has little effect and is sometimes negative. — [Packard, Moore & McFerran, Journal of Marketing Research, 2018](https://doi.org/10.1509/jmr.16.0118)
- [T4-Research][Intl] Concrete, specific employee language raises satisfaction and purchase because customers infer the employee is listening. The evidence comes from five studies, including more than 1,000 real interactions. — [Packard & Berger, Journal of Consumer Research (online Jul 2020)](https://doi.org/10.1093/jcr/ucaa038)
- [T4-Research][Intl] In text-based social-media complaints, adding active listening and empathy to the firm's response evoked gratitude among high-arousal customers "even if the actual failure is not (yet) recovered". This rests on three field studies using natural-language processing plus three preregistered experiments. — [Herhausen et al., "Complaint De-Escalation Strategies on Social Media", Journal of Marketing (online Aug 2022)](https://doi.org/10.1177/00222429221119977)

**AI-specific evidence**
- [T4-Research][Intl] When customers *enter* a chatbot interaction angry, a humanised (anthropomorphised) chatbot lowers satisfaction, firm evaluation and purchase intent. The cause is inflated expectations that the bot then violates. There was no such effect for non-angry customers. — [Crolic, Thomaz, Hadi & Stephen, "Blame the Bot", Journal of Marketing (online Aug 2021)](https://doi.org/10.1177/00222429211045687)
- [T4-Research][Intl] Disclosing chatbot identity reduced purchases in a field experiment, because customers perceived the disclosed bot as less knowledgeable and less empathetic. This was a sales context, not a service one. — [Luo, Tong, Fang & Qu, Marketing Science, 2019](https://doi.org/10.1287/mksc.2019.1192)

**Banking-specific (industry study, US)**
- [T4-Research][US] The 2026 J.D. Power U.S. Retail Banking Satisfaction Study (released 26 Mar 2026) reports:
  - Overall satisfaction rose 2 points to 657 (out of 1,000), "but sharp declines in the second half of the year show growing strain in the customer experience with phone, branch, online and automated customer engagement channels".
  - 20% of customers moved money away from their primary bank in the past 3 months, up from 17%.
  - Problem-resolution satisfaction was 587 at national banks (+49 vs 2024) and 548 at midsize banks (−27 vs 2024).
  - Top performers "treat routine customer experiences–such as alerts, funds transfers, fees and face-to-face interactions–as opportunities to reinforce clarity and confidence".
  - The seven satisfaction dimensions, in order of importance: trust; people; account offerings; banking how and when customers want; saving time and money; digital channels; resolving problems or complaints.
  - Sample: n=107,059, fielded Jan 2025–Jan 2026. — [J.D. Power press release, 26 Mar 2026](https://www.jdpower.com/business/press-releases/2026-us-retail-banking-satisfaction-study)

**Türkiye-specific evidence**
- [T4-Research][TR] In a Turkish survey (n=738, online convenience sample), bank call-centre service quality had a positive effect on consumer-based bank brand equity (path β=0.79; r=0.677). The authors call for measuring human and technical (system) factors together. They also report, citing call-centre statistics, that 13,319,264 customers used bank call centres in March 2018. — [Işık & Ay, İşletme Araştırmaları Dergisi 14(1):232–248, 2022](https://doi.org/10.20491/isarder.2022.1377)
- [T3-Practice][TR] The official vocational textbook of the Ministry of National Education (MEB) states that finance is the sector using call centres most, citing 2021 data. — [MEB, *Çağrı Merkezi İşlemleri 11*, approved 24.12.2020, ISBN 978-975-11-6851-1](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)

**Customer psychology relevant to banking**
- [T4-Research][Intl] Retrospective evaluations of unpleasant experiences are dominated by the worst and the final moments, and duration matters little (peak-end effect, lab study). — [Kahneman et al., Psychological Science, 1993](https://doi.org/10.1111/j.1467-9280.1993.tb00589.x)
- [T4-Research][Intl] Inducing thoughts about finances reduced cognitive performance among poorer participants: money worries consume mental bandwidth. — [Mani, Mullainathan, Shafir & Zhao, Science, 2013](https://doi.org/10.1126/science.1238041)
- [T4-Research][Intl] Putting feelings into words ("affect labelling") reduced amygdala response to negative images in an fMRI study. — [Lieberman et al., Psychological Science, 2007](https://doi.org/10.1111/j.1467-9280.2007.01916.x)
- [T3-Practice][Intl] Norman's practitioner synthesis of the psychology of waiting gives eight principles, including:
  - "Emotions dominate".
  - "Eliminate confusion: provide a conceptual model, feedback and explanation".
  - "Set expectations, then meet or exceed them".
  - "Filled time passes more quickly than unfilled time".
  - "Be fair".
  - "End strong, start strong".
  - "Memory of an event is more important than the experience".
  — [Donald Norman, "The Psychology of Waiting Lines" (jnd.org, c. 2008)](https://jnd.org/the-psychology-of-waiting-lines/) (Maister's 1985 essay is the classic precursor: [davidmaister.com](https://davidmaister.com/articles/the-psychology-of-waiting-lines/))

### Inferences
- [T5-Verify] For an AI banking agent, the main success metric should be *effortless resolution*: one contact, no repeated identification, no re-explaining, warm hand-offs. "Delight" behaviours (effusive praise, chatty empathy) are unlikely to build loyalty and may irritate. This is supported by the HBR 2010 and Gartner 2020 findings, but those come from cross-industry proprietary data.
- [T5-Verify] Complaints and fee disputes need explicit *procedural* signals (what happens, who decides, by when) and *interactional* signals (respect, empathy, explanation), even when the distributive outcome (refund or no refund) is fixed. That follows from Tax 1998 and Gelbrich & Roschk 2011.
- [T5-Verify] Do not engineer "recovery moments". Because the paradox does not reliably lift repurchase (de Matos 2007), prevention and first-time resolution remain the priority.
- [T5-Verify] An AI agent should be designed *not* to over-humanise when customers are angry: a plain, competent, non-cute persona with a quick human exit (Crolic 2021). It should also disclose AI status as legally required (see §7) while compensating with demonstrated competence and empathy cues (inference from Luo 2019).
- [T5-Verify] Customers who call about money problems may have less cognitive bandwidth (Mani 2013). That argues for short steps, one question at a time, written follow-up and no information dumps.
- [T5-Verify] Under the peak-end effect, the close of the interaction carries disproportionate weight. End with a clear recap and a concrete next step, not an abrupt transfer.

### Gaps
- The widely quoted "96% of high-effort customers become disloyal vs 9% low-effort" figure is attributed to Gartner or *The Effortless Experience* in many secondary sites. I could not verify it in a primary Gartner document, so it is not used.
- No peer-reviewed banking-specific study of conversational techniques (phrasing) was found. The J.D. Power data is a proprietary industry survey and is US-only.
- No European or UK equivalent of the J.D. Power 2026 banking study was checked (for example the UK CMA service-quality survey or the UK Customer Satisfaction Index).
- The body text of the Turkish 2022 study shows a convenience sample skewed to public-sector employees (47.6%), so generalisability is limited.

---

## 2. Core communication techniques and phrasing patterns

### Takeaway
Seven techniques have the best support and translate directly to an AI agent:
- active listening with concrete paraphrase;
- naming the customer's emotion briefly;
- funnel questioning (open → focused → closed confirmation);
- signposting and chunking (at most ~3–4 items per turn);
- plain language with layering;
- honest uncertainty framed as "what I know / don't know / will do next";
- teach-back on high-stakes steps.
First-person, specific language ("I've checked… I will…") outperforms corporate "we" and vague reassurance.

### Cited Findings
- [T4-Research][Intl] Concrete wording signals listening and raises satisfaction ([Packard & Berger](https://doi.org/10.1093/jcr/ucaa038)). "I" language raises perceived empathy and agency ([Packard et al. 2018](https://doi.org/10.1509/jmr.16.0118)).
- [T4-Research][Intl] Short-term memory capacity averages about four chunks (range 3–5), not Miller's "seven". — [Cowan, Behavioral and Brain Sciences, 2001](https://doi.org/10.1017/s0140525x01003922)
- [T4-Research][Intl] Communicating uncertainty openly produced only a small drop in trust, mostly when the uncertainty was *verbal* (vague hedging) rather than numeric (ranges). Total n=5,780, including a field experiment on BBC News. — [van der Bles et al., PNAS, 2020](https://doi.org/10.1073/pnas.1913678117)
- [T4-Research][Intl] Teach-back proved effective in 19 of 20 healthcare studies of moderate quality, covering knowledge recall, retention and some health outcomes. — [Talevski et al., PLoS ONE, 2020](https://doi.org/10.1371/journal.pone.0231350)
- [T4-Research][Intl] Clinical de-escalation consensus offers relevant technique guidance:
  - "Be concise": agitated people struggle to process information, so use short sentences and simple vocabulary, and repeat.
  - "Identify wants and feelings": ask what the person needs "whether or not the request can be granted".
  - "Listen closely": use active listening and clarify.
  - "Agree or agree to disagree".
  - "Offer choices and optimism".
  — [Richmond et al., Project BETA consensus, Western Journal of Emergency Medicine, 2012](https://doi.org/10.5811/westjem.2011.9.6864) (full text: [PMC3298202](https://pmc.ncbi.nlm.nih.gov/articles/PMC3298202/))
- [T4-Research][Intl] Affect labelling dampens limbic response in the lab ([Lieberman et al. 2007](https://doi.org/10.1111/j.1467-9280.2007.01916.x)). Applying this to a spoken "That sounds really worrying" is an extrapolation.
- [T2-Guidance][UK] Under the FCA Consumer Duty consumer-understanding outcome, firms must tailor communications to the characteristics of recipients, including vulnerability and the communication channel. The outcome applies to verbal communications too ("including verbally – such as during conversations"). FCA lists good practices for clarity:
  - **Layering:** key information first, including any action required and the consequences of inaction, with links to detail.
  - **Engaging:** headings, bullet points, tables.
  - **Relevant:** the appropriate level of detail.
  — [FCA FG22/5, Jul 2022, §§8.4, 8.13, 8.18](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T2-Guidance][UK] A poor-practice example in that guidance: a product summary "complex and full of jargon and technical terms". — [FCA FG22/5](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T2-Guidance][UK] Firms can offer simple definitions of jargon (for example, on hover) and proactive help in digital journeys. — [FCA FG21/1, Feb 2021, §4.18](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T1-Law][TR] Under the Consumer Protection Law, contracts and information notices that must be in writing are to be drafted "in at least twelve-point size, in an understandable language, clearly, plainly and legibly" ("en az on iki punto büyüklüğünde, anlaşılabilir bir dilde, açık, sade ve okunabilir"). This is a written-document rule, not a rule about conversations. — [Law No. 6502, Art. 4(1), official text (mevzuat.gov.tr)](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6502.pdf)
- [T3-Practice][US] The US federal plain-language guidelines site plainlanguage.gov now redirects to digital.gov's plain-language guide (checked 10 Oct 2026). Older references to plainlanguage.gov may be outdated. — [digital.gov plain language guide](https://digital.gov/guides/plain-language/)
- [T3-Practice][TR] Turkish official training norms: never say "Bilmiyorum" ("I don't know") but "Araştırıp size bilgi vereceğim" ("I'll look into it and get back to you") ([MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)). Representatives must listen effectively and speak "fluently and understandably" ([MYK 15UY0203-4, Rev. 01, 30/10/2019](https://portal.myk.gov.tr/index.php?dl=Yeterlilik%2F2632%2FSON_TASLAK_PDF_20200625_092024.pdf&fileName=15UY0203-4+Rev+01+%C3%87a%C4%9Fr%C4%B1+Merkezi+M%C3%BC%C5%9Fteri+Temsilcisi&option=com_yeterlilik)). More detail is in §9.

### Inferences — technique → adaptable pattern (EN / TR)
All patterns are [T5-Verify] adaptations. Turkish should be reviewed by a native-speaking banking writer. Amounts, dates and timescales in examples are illustrative and must come from systems of record.

| Technique | Pattern (EN) | Turkish equivalent (gloss in brackets where needed) |
|---|---|---|
| Open question, then funnel | "What's happening with your card today?" → "When did you last use it successfully?" → "So it was declined at a shop at 14:10 today — correct?" | "Kartınızla ilgili ne yaşadınız?" → "En son ne zaman sorunsuz kullandınız?" → "Yani bugün 14.10'da bir mağazada reddedildi; doğru mu?" |
| Concrete paraphrase (shows listening) | "If I've understood correctly, a 2,450-lira payment you don't recognise left your account yesterday." | "Doğru anladıysam, dün hesabınızdan tanımadığınız 2.450 TL'lik bir ödeme çıkmış." |
| Emotion label (brief, once, then act) | "That sounds really worrying. Let's make sure your money is safe first." | "Bunun sizi çok endişelendirdiğini anlıyorum. Önce paranızın güvende olduğundan emin olalım." |
| Signposting | "I'll do three things: check the payment, secure your card, then explain what happens next." | "Üç şey yapacağım: ödemeyi kontrol edeceğim, kartınızı güvene alacağım, sonra da sürecin nasıl ilerleyeceğini anlatacağım." |
| Chunking (≤3–4 items) | "There are two steps. Step one…" (pause/confirm) "Step two…" | "İki adım var. Birinci adım…" (onay) "İkinci adım…" |
| Plain-language analogy | "A 'pending' amount is reserved but not yet taken — like a hotel holding a deposit." | "'Provizyon', tutarın bloke edildiği ama henüz kesinleşmediği anlamına gelir; otelin depozito ayırması gibi düşünebilirsiniz." |
| Know / don't know / next | "Here's what I can confirm… What I can't see yet is… What happens next is…" | "Şu an kesin olarak söyleyebileceğim şu: … Henüz göremediğim kısım: … Bundan sonra şu olacak: …" |
| Numeric rather than vague uncertainty | "Most transfers like this arrive within 1 working day; occasionally up to 3." (only if the policy says so) | "Bu tür transferler çoğunlukla 1 iş günü içinde ulaşır; nadiren 3 iş gününe kadar sürebilir." |
| Teach-back (high stakes) | "So I know I explained it clearly — what will you do if the refund isn't there by Friday?" | "Doğru anlatabildiğimden emin olmak için sorayım: İade cuma gününe kadar hesabınıza geçmezse ne yapacaksınız?" |
| Positive positioning instead of "can't" | "I can't reverse that payment myself, but I can open a dispute now — that's the fastest route." | "Bu ödemeyi doğrudan iptal edemiyorum; ancak hemen bir itiraz kaydı açabilirim, en hızlı yol bu." |
| First-person ownership | "I've checked… I'll send you…" (not "the system shows / it has been forwarded") | "Kontrol ettim… Size SMS ile göndereceğim…" (not "iletilmiştir / sistemde görünmektedir") |
| Summary of agreed next steps | "To recap: card blocked; new card in 5–7 working days; dispute reference CB-1234." | "Özetlersek: Kartınız kapatıldı; yeni kartınız 5–7 iş günü içinde gelecek; itiraz numaranız CB-1234." |

- [T5-Verify] For a voice agent, keep each turn to one main point plus one question, and confirm critical items (amounts, dates, references) back to the customer. Cowan's ~4-chunk limit is a lab estimate, so treat "≤3–4 items" as a design heuristic.
- [T5-Verify] Prefer numeric ranges taken from policy over vague hedges ("should be soon"), based on van der Bles 2020. Never invent ranges.

### Gaps
- CFPB-specific plain-language resources were not reviewed in this session (they belong to lane 03). No official Turkish "sade dil" guideline for banking conversations was found. Law 6502 Art. 4 covers written contracts and information notices only.
- No research on teach-back in banking or call-centre settings was found; the evidence is from healthcare.

---

## 3. Building trust while keeping security: explaining verification without sounding accusatory

### Takeaway
Frame verification as *protection of the customer's money*, not suspicion. State clearly what the bank will never ask for. Make security friction proportionate and explained, and acknowledge repeat-verification frustration by giving a reason for each additional step. Regulators treat fraud-prevention friction as legitimate ("positive friction"), but unexplained or repeated hurdles damage trust and add effort. Turkish banks' practice is that agents never ask customers to *say* passwords: telephone-banking passwords are keyed into the IVR, and messaging channels carry explicit "we will never ask" warnings.

### Cited Findings
- [T3-Practice][UK] Take Five (UK Finance's national campaign) advises: "Never disclose security details, such as your full PIN or full password"; "Don't be rushed – a genuine organisation won't mind waiting"; and to contact companies using known contact details. — [NatWest, "What is Take Five" (undated)](https://www.natwest.com/support-centre/bank-accounts-and-supporting-information/general/what-is-take-five-and-how-does-it-help-prevent-fraud.html); [Take Five site, © 2026 UK Finance](https://www.takefive-stopfraud.org.uk/about/take-five/) ("Only criminals will try to rush or panic you.")
- [T3-Practice][TR] At Ziraat Dinamik (Ziraat Bankası's digital bank), customers are expected to verify themselves with card password, digital password or digital approval, or SMS code, and simply key in their password in the IVR. "Bankamız müşteri temsilcisi sizden şifrenizi söylemenizi istemeyecektir" ("Our customer representative will not ask you to say your password"). Outbound calls come from the registered number, and "all calls … are recorded". — [Ziraat Dinamik, "Müşteri İletişim Merkezinde Güvenlik" (undated)](https://www.ziraatdinamik.com.tr/tr/gizlilik-guvenlik/musteri-iletisim-merkezinde-guvenlik)
- [T3-Practice][TR] ING Türkiye's guidance:
  - Personal data, passwords or security elements should never be shared with anyone on the phone.
  - No financial transaction should be made on a third party's instruction.
  - A suspicious call should be ended immediately and the bank contacted.
  — [ING Türkiye, "Bilgi ve İşlem Güvenliği Farkındalığı Bildirimi"](https://www.ing.com.tr/tr/ing/guvenlik/ing-bilgi-islem-guvenligi-farkindaligi-bildirimi)
- [T3-Practice][TR] Garanti BBVA's WhatsApp line (an AI bot, 24/7, "over 200 topics") tells customers to check for the green-tick verified business account. The bank says it never requests passwords, personal information, card details or SMS codes via WhatsApp. — [Garanti BBVA WhatsApp page](https://www.garantibbva.com.tr/dijital-bankacilik/garanti-bbva-whatsapp)
- [T3-Practice][TR] Yapı Kredi's warning: "Şifrelerinizi ve kişisel bilgilerinizi banka personeli dahil kimseyle WhatsApp üzerinden paylaşmayınız" ("Don't share your passwords and personal information with anyone on WhatsApp, including bank staff"). — [Yapı Kredi WhatsApp page](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/yapi-kredi-whatsapp)
- [T2-Guidance][UK] Additional steps "designed to prevent fraud … can benefit customers" and are not unreasonable barriers. However, friction must be justified and evidenced, and "sludge" that deters customers from acting in their interests is inconsistent with the Duty. — [FCA FG22/5 §§9.19–9.25](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T2-Guidance][UK] Digital-only firms still need exception processes for "security or fraud concerns, technical issues, or other more complex or sensitive customer journeys". FCA says "it is likely that firms will need a real-time human interface, such as a phone service" for some of these. — [FCA FG22/5 §9.18](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T2-Guidance][UK] Case study: a consumer acting for his ill partner "found it stressful and frustrating to have to prove he had permission … and repeat the story every time". — [FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T4-Research][Intl] Customers' feeling that the agent was "hiding behind general company policy" was a driver of repeat calls. — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)
- [T1-Law/T2][TR] KVKK Board Decision 2022/224 (10.03.2022). A bank call-centre agent offered to pass a caller's name and phone number to a third party, and the caller replied "tamam" ("okay"). The Board found that explicit consent must relate to a specific matter and be limited to it, and imposed an administrative fine. The bank's KVKK information notice at the call centre was found adequate. — [KVKK decision summary](https://www.kvkk.gov.tr/Icerik/7296/2022-224)

### Inferences — patterns
- [T5-Verify] **Why we verify (non-accusatory):**
  - EN: "Before I look at your account, I need to confirm it's really you. It protects your money from anyone pretending to be you. I'll never ask for your full PIN, password, the security code on your card, or any one-time code."
  - TR: "Hesabınıza bakabilmem için önce sizin olduğunuzu doğrulamam gerekiyor; bu, paranızı sizin adınıza işlem yapmaya çalışabilecek kişilere karşı korur. Sizden hiçbir zaman kart şifrenizi, internet bankacılığı şifrenizi, kartınızın arkasındaki güvenlik kodunu ya da SMS ile gelen tek kullanımlık kodu istemeyeceğim."
- [T5-Verify] **Frustration at repeated verification:** acknowledge, explain why *this* step differs, and state how many steps remain.
  - EN: "You're right, you confirmed your details earlier. Because this request moves money, there's one extra check, and then I can go ahead."
  - TR: "Haklısınız, bilgilerinizi daha önce doğruladınız. Bu talep para transferi içerdiği için tek bir ek güvenlik adımı var; ardından işleminize devam edebilirim."
- [T5-Verify] **Step-up design:**
  - Verify proportionately to the action: information requests need less than payments or contact-detail changes.
  - Carry authentication state across hand-offs, so a warm transfer should not restart verification where the bank's policy allows. This addresses HBR and FG22/5 concerns about repetition.
  - Where verification needs a secret, use the bank's own authentication service (for example in-app approval or biometrics, or IVR keypad entry where that is the bank's established method, as at Ziraat Dinamik).
  - The AI agent must never receive, hear, transcribe, echo or store the secret. Keypad tones (DTMF) and one-time codes must be captured by the authentication service and masked from the AI's context, transcripts and logs. This design requirement belongs to lane 08 and lane 12 to confirm.
- [T5-Verify] **Third parties:** never act on a vague "okay" to share data or accept a caller as authorised (KVKK 2022/224 [TR]). Ask a specific, limited consent question, or follow the bank's third-party authority process (FG21/1 [UK]).
- [T5-Verify] **Outbound and AI contacts:** because customers are trained to distrust unsolicited contact (Take Five), outbound AI calls should invite the customer to call back on the number on their card or in the app, and must never ask for secrets.

### Gaps
- No peer-reviewed research was found on *how phrasing of verification requests* affects trust or abandonment. These patterns are practitioner-derived.
- Turkish regulation on remote customer authentication (for example BDDK rules on information systems and electronic banking) belongs to lane 02/08 and was not verified here.

---

## 4. De-escalation, professional boundaries and safeguarding

### Takeaway
Effective de-escalation follows a consistent pattern:
1. Listen and let the customer finish.
2. Name the emotion briefly.
3. Acknowledge the *impact* without confirming unverified allegations.
4. Avoid argument and blame.
5. Offer a concrete next step and genuine choices.
6. Set respectful limits if abuse continues: warning, then ending per policy, with a route back.

Threats of harm to self or others leave the de-escalation track and enter safeguarding: immediate escalation to trained humans and emergency services per policy. The underlying components (active listening, empathy, conciseness, limit-setting, choices) have expert-consensus and experimental support. Branded mnemonics do not have validation evidence, and even clinical de-escalation has a thin trial base.

### Cited Findings
- [T4-Research][Intl] The Project BETA consensus sets out "10 domains of de-escalation":
  1. Respect personal space.
  2. Do not be provocative.
  3. Establish verbal contact: one person speaks, introduces themselves and orients the person.
  4. Be concise.
  5. Identify wants and feelings.
  6. Listen closely.
  7. Agree or agree to disagree.
  8. Lay down the law and set clear limits, "in a respectful manner".
  9. Offer choices and optimism.
  10. Debrief.
  It is *expert consensus* from emergency psychiatry. — [Richmond et al., WestJEM 2012](https://doi.org/10.5811/westjem.2011.9.6864)
- [T4-Research][Intl] A thematic synthesis of 11 papers found de-escalation themes of staff skills (maintaining personal control, verbal and non-verbal skills) and process: engaging, timing, safe conditions, "autonomy confirming interventions" and "limit-setting and authoritative interventions". It notes that de-escalation "has been overlooked by rigorous research". — [Price & Baker, International Journal of Mental Health Nursing, 2012](https://doi.org/10.1111/j.1447-0349.2011.00793.x)
- [T4-Research][Intl] A Cochrane review of de-escalation for non-psychosis aggression in care settings found only *one* eligible trial, so efficacy remains unclear. — [Spencer, Johnson & Smith, Cochrane 2018](https://doi.org/10.1002/14651858.CD012034.pub2)
- [T4-Research][Intl] Supporting evidence from §1: active listening and empathy de-escalate ([Herhausen et al.](https://doi.org/10.1177/00222429221119977)); empathic, timely apologies work best ([Roschk & Kaiser](https://ideas.repec.org/a/kap/mktlet/v24y2013i3p293-309.html)); angry customers react worse to humanised bots ([Crolic et al.](https://doi.org/10.1177/00222429211045687)).
- [T3-Practice][UK] The Financial Ombudsman Service's "Unreasonable behaviour policy" (v04, undated) defines aggressive or abusive behaviour as "violent, insulting or threatening, such as: offensive language, any form of discrimination, inflammatory statements … any threat of physical violence, malicious communication". Possible actions include:
  - stopping phone contact and communicating only in writing;
  - communicating only via a verifiable representative;
  - stopping communication on a particular issue.
  — [FOS policy](https://www.financial-ombudsman.org.uk/corporate/policies/unreasonable-behaviour-policy)
- [T3-Practice][UK] NS&I's policy says it "will take into account the personal circumstances of that customer, such as any vulnerability, and/or relevant protected characteristic, before we make a decision". It may write to warn the customer, and for "particularly serious or extreme" behaviour threatening staff safety it may report to authorities without prior warning. — [NS&I Unreasonable customer policy (undated PDF)](https://www.nsandi.com/files/asset/corporate/unreasonable-customer-policy.pdf)
- [T3-Practice][TR] MEB guidance says staff must never reflect their own distress back to the customer, even when exposed to rude language. It includes a "difficult customer" role-play in which the employee calms the customer and seeks a solution. — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T3-Practice][UK] Money Advice Trust (an FCA-regulated charity) states that "each year, 1 in 4 frontline staff will receive one or more disclosures of suicide" and that "each year, 100,000 customers in financial difficulty will attempt suicide". These are the charity's own claims; the methodology was not shown. It runs "Suicide First Aid for Essential Services". — [MAT SFA page (undated)](https://moneyadvicetrust.org/sfa/)
- [T3-Practice][UK] The **BLAKE** protocol for suicide-risk disclosures was developed by Chris Fitch and colleagues at the University of Bristol's Personal Finance Research Centre (PFRC) for debt collection: "Breathe (to focus), Listen (to understand), Ask (to discover), Keep safe (from harm), End (with summary)". Its source is Fitch, Evans & Trend (2016), *21 questions, 21 steps – Vulnerability: a guide for debt collection*. — [University of Bristol PFRC workshop summary, Apr 2018](https://www.bristol.ac.uk/media-library/sites/geography/pfrc/Financial%20difficulty%20%26%20mental%20wellbeing%20-%20workshop%20series%20summary.pdf)
- [T3-Practice][UK] A firm's training material expands BLAKE with:
  - example questions ("Where are you now?", "Is there anyone you can call or speak to?", "Have you made any plans to end your life?");
  - keep-safe advice ("Keep the customer talking… Validate how they feel");
  - an end-with-summary prompt ("What are you going to do after this call?").
  It also tells staff to escalate to a manager or vulnerable-customer champion. — [Just Group vulnerable-customer toolkit (© 2026)](https://prep.vulnerablecustomers.wearejust.co.uk/Your-Toolkit/blake/what-is-blake/)
- **Correction to the brief:** the "IDEA" approach is *not* the suicide-disclosure tool. IDEA (Impact, Duration, Experience, Assistance) is used to *explore how a disclosed condition affects the customer*. BLAKE is the suicide-disclosure protocol. — [Just Group toolkit, "What is IDEA"](https://inte.vulnerablecustomers.wearejust.co.uk/Your-Toolkit/idea/what-is-idea/); [Bristol PFRC 2018](https://www.bristol.ac.uk/media-library/sites/geography/pfrc/Financial%20difficulty%20%26%20mental%20wellbeing%20-%20workshop%20series%20summary.pdf)
- **Named training models.** All are practitioner mnemonics; no validation studies were found.

| Model | Expansion | Origin / use | Source status |
|---|---|---|---|
| HEAT | Hear, Empathize, Apologize, Take action | Widely used in contact centres; origin undocumented | [TTEC blog](https://www.ttecjobs.com/en/handling-difficult-calls-in-philippine-call-centers-real-strategies-that-work) (search summary only) |
| HEARD | Hear, Empathize, Apologize, Respond/Resolve, Diagnose | Hospitality and healthcare patient-experience training; Disney attribution unverified | [VUMC poster](https://www.vumc.org/elevate/sites/default/files/public_files/HRLS100%20-%20HEARD%20poster%2010.2002%20v2.4.pdf) located but not retrievable |
| LEAP | Listen, Empathize, Agree, Partner | Xavier Amador's approach for serious mental illness and anosognosia; "evidence-based" per its proponents only | [Georgia DBHDD listing](https://dbhdd.georgia.gov/node/17691) (403; search summary) |
| LEAPS | Listen, Empathize, Ask, Paraphrase, Summarize | Attributed to George Thompson's *Verbal Judo* (1993) in secondary sources | Thompson's approach confirmed in [IUP slides (2018)](https://www.iup.edu/teachingexcellence/files/reflective_practice/past_events/2018-19/facilitating_challenging_conversations_in_the_classroom/11-7-18-rplgm-de-escalation-powerpoint-verbal-judo.pdf); acronym not found there |
| LAST / LATTE | — | Attributed to hotel or coffee brands | No primary source found |

### Inferences — scenario playbook (patterns, not scripts)
All entries are [T5-Verify]. Guiding principle: acknowledge the *feeling and its impact*, not the *unverified claim*. For example, say "I can see why that's alarming", not "the bank made a mistake".

| Situation | Do | Avoid | EN pattern | TR pattern |
|---|---|---|---|---|
| Anger | Let them finish; one brief label; move to action; offer choices | Arguing about facts early; "calm down"; over-apologising | "I can hear how frustrating this is. Let me look at it now — I'll tell you exactly what I find." | "Ne kadar can sıkıcı olduğunu anlıyorum. Hemen inceleyeyim ve ne bulduğumu açıkça söyleyeyim." |
| Impatience after a long wait | Thank, apologise once, show you are now acting | Blaming volume or staffing; repeating apologies | "Thank you for waiting, and I'm sorry it took so long. I'm on it now." | "Beklediğiniz için teşekkür ederim; uzun sürdüğü için özür dilerim. Şimdi hemen ilgileniyorum." |
| Distress about missing money | Secure first (block, freeze), then trace; give timelines from policy | "It's probably just pending" (false reassurance) | "Let's make sure your account is safe first; then I'll trace the payment and tell you what I can confirm." | "Önce hesabınızı güvene alalım; ardından ödemenin izini sürüp kesin olarak söyleyebildiklerimi paylaşayım." |
| Fear of a scam / "the bank called me" | Praise checking; stop any ongoing contact; never ask for codes | Shaming ("you should have known") | "You did the right thing by checking with us. Please don't share any codes with that caller." | "Bizi arayıp kontrol etmeniz çok doğru oldu. Lütfen o kişiyle hiçbir kod paylaşmayın." |
| Confusion about terminology | Define once, use an analogy, check understanding | Repeating the term louder; jargon | "'Available balance' is what you can spend right now; 'balance' includes amounts still on hold." | "'Kullanılabilir bakiye' şu an harcayabileceğiniz tutardır; 'bakiye' ise henüz bloke olan tutarları da içerir." |
| Upset about fees or interest | Explain what the fee is for (procedural fairness); state options and who decides | Promising a refund without authority; defending with "it's in the T&Cs" alone | "Let me show you what this charge was for, and then what options exist." | "Önce bu ücretin ne için alındığını göstereyim, sonra mevcut seçeneklere birlikte bakalım." |
| Rejected application | Empathise; share what *can* be shared about reasons per jurisdiction; give alternatives and the complaint route | Speculating about scoring; "the computer says no" | "I'm sorry this isn't the answer you hoped for. I can explain what I'm able to share and what you can do next." | "Beklediğiniz yanıt bu olmadığı için üzgünüm. Paylaşabildiğim bilgileri ve şimdi neler yapabileceğinizi anlatayım." |
| Can't access essential funds | Treat as urgent; fastest safe route; interim options per policy; human escalation | Generic "within 5 working days" without alternatives | "Not being able to reach your money is serious, so I'm treating it as urgent. The quickest safe option is…" | "Paranıza erişememeniz ciddi bir durum; bunu öncelikli ele alıyorum. En hızlı güvenli seçenek şu: …" |

- [T5-Verify] **Boundary ladder for abuse** (align with the bank's policy; assess vulnerability first, per the NS&I approach):
  1. **Redirect:** "I want to help sort this out. Can we focus on getting your card working?" / "Bu sorunu çözmenize yardımcı olmak istiyorum. Kartınızın yeniden çalışmasına odaklanabilir miyiz?"
  2. **Boundary plus warning:** "I can't continue if the conversation includes insults. If it continues, I'll need to end the call." / "Görüşme hakaret içerdiği sürece devam edemem. Devam ederse görüşmeyi sonlandırmak zorunda kalacağım."
  3. **End with a route back:** "I'm ending the call now because of the language used. Your reference is …; you can contact us again by phone or in-app chat." / "Kullanılan ifadeler nedeniyle görüşmeyi şimdi sonlandırıyorum. Başvuru numaranız …; bize telefonla ya da mobil uygulamadaki sohbet kanalından yeniden ulaşabilirsiniz."
  4. **Log the incident and flag it for human review.** An AI agent should not impose contact restrictions such as written-only contact. That is a human policy decision (FOS and NS&I examples).
- [T5-Verify] **Threats to others:** do not argue or negotiate. State that threats are taken seriously, end or transfer per policy, and log for the security and safeguarding team. Reporting to police is a human decision, except where a bank's protocol says otherwise.
- [T5-Verify] **Suicide or self-harm disclosure (AI agent):**
  - Do not continue the transaction, and never end the conversation abruptly.
  - Acknowledge without judgement: "Thank you for telling me. I'm really sorry you're feeling like this." / "Bunu benimle paylaştığınız için teşekkür ederim. Böyle hissettiğiniz için gerçekten üzgünüm."
  - Ask about immediate safety: "Are you safe right now?" / "Şu anda güvende misiniz?"
  - If there is immediate danger, give the emergency number (999 [UK]; 112 [EU, TR]; 911 or the 988 Suicide & Crisis Lifeline [US]) and warm-transfer to a trained human *without hold music or a queue*.
  - Record the disclosure per the bank's process and the applicable data-protection basis.
  - BLAKE ("Ask… Keep safe… End with summary") is designed for trained humans. Whether an AI should ask direct questions about suicide plans needs clinical and legal sign-off, so do not deploy that step without it.
- [T5-Verify] **Model choice for training data:** use a *component checklist* rather than a branded mnemonic: listen → label → acknowledge impact → apologise or thank where appropriate → explain → offer choices → act → confirm → close. Every element maps to a cited study above. The mnemonics add memorability, not evidence.

### Gaps
- No controlled study was found comparing HEAT, HEARD, LAST or LEAPS outcomes in financial-services contact centres.
- I found no verified Türkiye-specific equivalent of BLAKE, TEXAS or Suicide First Aid for banks.
- Turkish crisis resources beyond 112 (for example whether a national suicide helpline exists, or the role of the ALO 183 social-support line) need verification.
- Primary sources for HEARD, LEAP and LEAPS returned HTTP 403 or did not contain the acronym; their descriptions rest on search summaries.

---

## 5. Vulnerable customers: practical handling

### Takeaway
UK guidance (FCA FG21/1, kept unchanged after the March 2025 review) gives the most operational framework. The core ideas:
- Vulnerability is a *spectrum of risk* driven by four drivers: health, life events, resilience and capability.
- Never label customers "vulnerable" to their face.
- Record needs once, transparently and lawfully (TEXAS), so customers never repeat themselves.
- Adapt the channel and format; allow third-party support and an "exit lane" from automation.
- Respond flexibly beyond standard procedure.

In Türkiye, the Turkish Banks Association (TBB) data shows broad but uneven accessibility provision for disabled customers. TBB also offers staff e-training on inclusive communication, but I found no Turkish equivalent of FG21/1's conversational guidance.

### Cited Findings
- [T2-Guidance][UK] Definition: customers who, "due to their personal circumstances, are especially susceptible to harm, particularly when a firm is not acting with appropriate levels of care". The four drivers:
  - **Health:** conditions or illnesses affecting day-to-day tasks.
  - **Life events:** bereavement, job loss, relationship breakdown.
  - **Resilience:** low ability to withstand financial or emotional shocks.
  - **Capability:** low financial knowledge or confidence, literacy or digital skills.
  — [FCA FG21/1, 23 Feb 2021, §2.5](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] 46% of UK adults had characteristics of vulnerability in February 2020, rising to 53% by October 2020. This is now dated data from the FCA's Financial Lives survey. — [FCA FG21/1 §2.7](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] "We suggest that firms do not use this label in their interactions with consumers. Instead, firms should focus on what harm or disadvantage customers may be vulnerable to." — [FCA FG21/1 §2.9](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] **TEXAS** is endorsed as an example of good practice:
  - **T**hank the customer for the disclosure.
  - **E**xplain how the information will be used.
  - Seek e**X**plicit consent *or* make che**X**s that the customer does not object, depending on the lawful basis.
  - **A**sk questions to understand the situation.
  - **S**ignpost to internal or external support.
  FCA notes the ICO view that consent is not the only lawful basis. — [FCA FG21/1 §§3.18–3.20](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T3-Practice][UK] Example TEXAS phrasing in firm training material: "Thank you for sharing"; "This will mean you won't need to keep repeating yourself"; "Are you happy for me to make a note of what you've shared today?"; "Is there anything you'd like us to do which will help?" — [Just Group toolkit, "TEXAS in action"](https://inte.vulnerablecustomers.wearejust.co.uk/recording-vulnerability/texas-in-action/)
- [T2-Guidance][UK] "Consumers should not have to repeat information". FCA cites a "tell us once" style bereavement notification as an example. — [FCA FG21/1 §4.60–4.61 area](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] Channel flexibility: a call-back service for people who struggle with phone menus; an "exit lane" from automated phone services; chatbots or text boxes for sharing needs; and multiple channels "so vulnerable consumers have a choice" ([FCA FG21/1 §§4.17, 4.36, 4.43 area, Figure 1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)).
- [T2-Guidance][UK] Format adaptations: British/Irish Sign Language video, simplified communications, dyslexia-friendly colours, large print, accessible websites, Next Generation Text (relay) and audio options ([FCA FG21/1 §§4.67–4.69](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)).
- [T2-Guidance][UK] Case studies from FG21/1:
  - **Poor practice:** a bank kept sending paper to a customer who could not read large print or braille and wanted email for text-to-speech.
  - **Good practice:** a bank offering BSL interpreters in branch, in-app and on the web.
  - **Poor practice:** staff addressing the wife of a customer with cerebral palsy instead of the customer himself.
  — [FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] On third-party representation and capacity:
  - Firms should provide "straightforward options" for legitimate delegated access (third-party mandates, Power of Attorney) "while maintaining robust safeguards".
  - Firms may act on a family member's instructions in some urgent situations.
  - A firm "should not regard a customer as lacking capacity … unless the firm has taken reasonable steps without success to help the customer to make that decision" (Mental Capacity Act 2005 [UK]).
  — [FCA FG21/1 §§4.46–4.56](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] Firms should respond flexibly to customers with characteristics of vulnerability, usually through different channels or adapted approaches. Some customers find phone information hard to absorb and need written communications, and vice versa. — [FCA FG22/5 §§9.13–9.16](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T2-Guidance][UK] FCA's review, "Firms' treatment of customers in vulnerable circumstances – review" (published 7 Mar 2025, updated 3 Dec 2025), identified four areas for improvement:
  - adapting standardised processes;
  - encouraging disclosure;
  - consistent recording and use of information;
  - outcomes monitoring.
  "Consumers continue to report challenges, particularly if they have multiple characteristics of vulnerability." FCA will "not be updating" FG21/1. — [FCA review page](https://www.fca.org.uk/publications/multi-firm-reviews/firms-treatment-vulnerable-customers)
- [T3-Practice][UK] **IDEA** (Impact, Duration, Experience, Assistance) is a question set for understanding how a situation affects a customer. Prompts include: "What are they finding hard…?", "How long…?", "Has this happened before…?", "Are they receiving any support…?" — [Just Group toolkit](https://inte.vulnerablecustomers.wearejust.co.uk/Your-Toolkit/idea/what-is-idea/)
- [T4-Research][UK] Money and Mental Health Policy Institute findings (Populus survey of 2,000 UK adults):
  - 54% of people with mental health problems have serious difficulties using the phone for essential admin, versus 32% of people without.
  - Four in ten have severe "admin anxiety".
  - 20.5 million UK adults struggle to use the phone to contact essential service providers.
  The press release is undated; the report is "Access Essentials", c. 2019. — [MMH press release](https://www.moneyandmentalhealth.org/press-release/access-essentials-pressrelease/)
- [T2-Guidance][UK] 86% of respondents to a Money and Mental Health survey said their financial situation had made their mental health problems worse (as cited by FCA). — [FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T3-Practice][Intl] **ISO 22458:2022** "Consumer vulnerability — Requirements and guidelines for the design and delivery of inclusive service" (published April 2022) covers culture, inclusive design and identifying and responding to vulnerability, including in financial services. It is paywalled and was not read. — [ISO 22458 listing (via SCC)](https://scc-ccn.ca/standardsdb/standards/8178665)
- [T3-Practice][TR] TBB data (as of June 2025), reported by Sözcü on 30 Nov 2025:
  - 23 banks provide services for disabled customers.
  - 20 banks offer remote support for hearing-impaired customers; 11 offer online chat support for them.
  - 25 banks make SMS one-time passwords readable by screen readers; 21 banks' mobile apps support voice-conversion tools.
  - Registered disabled customers: 34,146 orthopaedic, 11,472 visual and 14,551 hearing.
  — [Sözcü, 30 Nov 2025](https://www.sozcu.com.tr/turkiye-de-23-banka-engelli-bireylere-bankacilik-hizmeti-veriyor-p264995)
- [T3-Practice][TR] TBB launched a free e-training, "Engeli Olan Bireylerle Kapsayıcı İletişim" ("Inclusive Communication with Persons with Disabilities"): 10 videos totalling 50 minutes. Topics include first steps in communication, communication by disability group, inclusive language, branch communication and disability rights. It is hosted on TBB's education portal. — [Alomaliye reproduction of the TBB announcement, 19 Oct 2023](https://www.alomaliye.com/2023/10/19/engeli-olan-bireylerle-kapsayici-iletisim-e-egitimleri-hakkinda/)

### Inferences — AI-agent handling rules
All rules are [T5-Verify].
1. **Detect, don't diagnose.** Listen for cues such as bereavement, illness, job loss, confusion, mentions of carers, distress or coercion. Respond to the *need* (time, format, channel, a person), not a label (FG21/1 §2.9).
2. **On disclosure, follow TEXAS-style handling.** Thank the customer, explain use ("so you won't need to repeat this"), check lawful basis and consent per the bank's data-protection approach (GDPR/UK GDPR [UK/EU]; KVKK [TR]), ask what would help (IDEA-style), and signpost.
3. **Use recorded needs automatically.** At the next contact, honour stored preferences such as slower pace, written follow-up, no phone calls or a third-party representative, without making the customer re-disclose.
4. **Adapt to cognitive load and capability.**
   - Offer to repeat or slow down, or to send written steps.
   - Give one instruction at a time and avoid time pressure.
   - Offer a call-back or human help.
   - For low digital literacy, never force app-only resolution; offer an alternative channel.
5. **Hearing or speech impairments:** support text, relay services or video sign-language channels where the bank offers them. For a voice AI, allow extra response time and do not time out quickly on silence or slow speech.
6. **Visual impairment:** describe options verbally, avoid "click the blue button", and send accessible formats.
7. **Language barriers:** offer the bank's supported languages or interpreter services, use short sentences, and confirm key facts. Do not rely on machine translation for legally significant explanations without the bank's approval.
8. **Older customers and dementia:**
   - Speak to the customer, not the companion (FG21/1 case).
   - Check understanding through teach-back.
   - Be alert to signs of financial abuse or scam coaching.
   - Use the bank's third-party authority process.
9. **Always provide a human exit lane**, and route faster when vulnerability is detected (FG21/1; FG22/5 §9.18).

### Gaps
- Turkish regulators (BDDK, TCMB) have no FG21/1-equivalent conversational guidance that I could find. Lane 02 should confirm whether BDDK, TCMB or the Ministry of Family and Social Services have issued accessibility or vulnerability rules for bank call centres.
- TBB's own publications on disabled customers were not accessed directly; the data here comes from press reproduction. TBB documents should be confirmed.
- FCA's more recent Financial Lives data (2022 or 2024 waves) on vulnerability prevalence was not checked; the 46%/53% figures are from 2020.
- A law-firm summary of the FCA 2025 review quoted statistics (for example "58%", "88%", "29%") that do *not* appear on the FCA landing page. They are excluded pending a check of the full FCA report.

---

## 6. Common communication mistakes, better alternatives and why they work

### Takeaway
Most damaging mistakes increase customer effort (repetition, transfers, channel switching), signal not listening (generic or scripted replies), or undermine trust (blame, false reassurance, unverified facts, promises without authority). Regulators in the UK and Türkiye have documented several of these as poor practice.

### Cited Findings (evidence underpinning the catalogue)
- Repeat contacts, re-explaining, transfers and channel switching are core effort drivers ([HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers)). Low effort is associated with retention ([Gartner 2020](https://www.gartner.com/en/newsroom/press-releases/2020-08-19-gartner-reveals-two-actions-customer-service-leaders-)). [T4-Research]
- [T2-Guidance][UK] FCA poor practice:
  - "multiple customer service advisers sequentially enter the same chat and ask the customer the same questions";
  - an automated phone system offering options for only a few common issues with "no route" for others;
  - harms from "phone systems, menus or webchats that are difficult to navigate" and "poor hand-off processes".
  — [FCA FG22/5 §9.10 and examples](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T4-Research][Intl] Customers can detect scripted service. Heavy scripting lowered perceived quality in *customised* encounters (concierge), with no difference in standardised ones (check-in). — [Victorino, Verma & Wardell, Cornell Center for Hospitality Research publication, 2008](https://scholarship.sha.cornell.edu/chrpubs/153)
- [T3-Practice][TR] MEB guidance:
  - avoid "Bilmiyorum" ("I don't know");
  - do not say "Bir saniye bekleyin" ("Wait a second") when holding;
  - do not close with "Maalesef onu yapamayız" ("Unfortunately we can't do that");
  - the mute key "is not used to hold the customer".
  — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T1-Law/T2][TR] Sharing customer data on an ambiguous "okay" led to a fine. — [KVKK 2022/224](https://www.kvkk.gov.tr/Icerik/7296/2022-224)
- [T2-Guidance][UK] Addressing a companion instead of the customer is a documented poor practice. — [FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)

### Inferences — catalogue
Each row is [T5-Verify] synthesis with its evidence anchor.

| # | Mistake | Better alternative (EN / TR example) | Why it works (anchor) |
|---|---|---|---|
| 1 | Interrupting, or a voice bot barging in over the customer | Let them finish; use short acknowledgement tokens; summarise after. Voice: tune end-of-speech detection; never cut off during distress. "Go on, I'm listening." / "Buyurun, dinliyorum." | Listening closely and concise paraphrase de-escalate (Project BETA); concreteness signals listening (Packard & Berger) |
| 2 | Assuming the problem (pattern-matching too early) | Open question, then funnel and confirm: "Before I check — what exactly happened when you tried to pay?" / "Kontrol etmeden önce sorayım: Ödeme yapmaya çalıştığınızda tam olarak ne oldu?" | Prevents wrong fixes and repeat contacts; 22% of repeat calls are downstream issues (HBR) |
| 3 | Generic responses ("We value your feedback") | Specific, customer-referenced content: "The 2,450 TL payment on 8 October is still pending with the merchant." | Concrete language raises satisfaction (Packard & Berger) |
| 4 | Repeating the same scripted phrase and ignoring new information | Acknowledge the new fact explicitly: "Thanks, that changes things — if the card was in your wallet, this looks like card-not-present use." | Scripts are detectable and hurt customised encounters (Victorino 2008); emotional disconnects drive repeat calls (HBR) |
| 5 | Blaming another department, the system or the customer | Own the next step: "I can't see that team's notes, so I'll make sure they get this with the full details now." | Ownership and "AskOnce" (HBR, Nedbank); interactional justice (Gelbrich & Roschk) |
| 6 | Jargon ("chargeback", "provizyon", "valör") | Define once in plain words plus an analogy; check understanding | FCA consumer-understanding expectations (FG22/5 §8); TR Law 6502 Art. 4 ethos for written information |
| 7 | Sounding dismissive or robotic ("As I said…", "Calm down") | Brief emotion label, then action; "I" statements; vary phrasing naturally | Empathy is the strongest apology component (Roschk & Kaiser); "I" raises perceived empathy (Packard 2018) |
| 8 | Promising without authority ("I'll get that fee refunded") | Promise only the process: "I'll submit a refund request today; the fees team decides within X days and you'll get an SMS." | Credibility is a complaint-response dimension (Davidow 2003); broken promises create repeat contacts (HBR) |
| 9 | Quoting unverified policy or transaction facts (including AI "hallucination") | Use only system-of-record data and approved policy; otherwise: "I can't confirm that yet — here's how I'll find out." | Honest numeric or bounded uncertainty preserves trust better than vague claims (van der Bles 2020) |
| 10 | Declaring "resolved" before verification | "I've submitted the change; you'll see it in the app within 2 hours. If not, contact us with reference …" | Avoids a false close and repeat contacts; customers judge procedure (Tax 1998) |
| 11 | Asking customers to repeat what's on record | Use context passed from IVR, earlier contacts and vulnerability notes; confirm, don't re-ask: "I can see you reported this yesterday at 18:00 — I'll pick up from there." | 56% re-explain (HBR); FCA: "should not have to repeat information" (FG21/1) |
| 12 | Repeated or blind transfers | Warm transfer with a summary, and tell the customer who and why: "I'm transferring you to the fraud team because they can block card-not-present payments; I've passed on everything, so you won't need to repeat it." | 59% transferred (HBR); poor hand-offs listed as harm (FG22/5 §9.10) |
| 13 | False reassurance ("Don't worry, it's definitely safe") | Calibrated reassurance plus action: "I've blocked the card, so no new card payments can go through. The disputed one is under review." | Trust depends on credibility; unexplained certainty can backfire (van der Bles; Davidow) |
| 14 | Requesting sensitive information unnecessarily | Ask only what this task needs; never PIN, password, CVV or one-time code; route secrets to the keypad or app. "I don't need your card number — I can see your cards once you're verified." | Take Five; TR bank practice (Ziraat, Garanti, Yapı Kredi); data-minimisation principles (GDPR, KVKK — lanes 02/03) |
| 15 | Ending without a clear next step | Recap + reference + timescale + what to do if it doesn't happen + anything else? | Peak-end effect (Kahneman 1993); MEB/MYK closing norms; downstream-issue prevention (HBR) |
| 16 | Talking to the companion, not the customer | Address the customer directly; ask how they prefer to communicate | FG21/1 poor-practice case |
| 17 | Acting on a vague "okay" to share data or accept a third party | A specific, limited consent question, or the bank's third-party authority process | KVKK 2022/224 [TR]; FG21/1 third-party guidance [UK] |
| 18 | Labelling the customer ("vulnerable", "difficult") | Talk about needs and options: "Would it help if I sent this in writing?" | FG21/1 §2.9 |
| 19 | "Wait a second" or silent mute instead of a proper hold | Ask permission, give a reason and duration, check back, thank: "May I put you on hold for about two minutes while I check with the card team?" / "Kart ekibimizle kontrol etmem gerekiyor; sizi yaklaşık iki dakika bekletmemde sakınca var mı?" | MEB norms; explained, bounded waits feel shorter (Norman) |

### Gaps
- No quantitative study isolates the effect of each individual mistake in banking. The ranking of severity is a judgement call; HBR, Gartner and FCA indicate that repetition and transfers are the biggest drivers.
- AI-hallucination risk in banking service is not addressed in the regulatory texts reviewed here (lane 12 for evaluation design).

---

## 7. End-to-end interaction framework

### Takeaway
An evidence-aligned interaction flow puts **risk and security triage before problem-solving** and **ownership before transfer**, and closes with a *verifiable* next step. Formal contact-centre standards (ISO 18295-1, COPC) set organisational requirements but are paywalled. Turkey's national qualification (MYK) and the MEB curriculum describe a compatible call flow: greeting announcement, active listening, name-based address, clear language, correct case recording, routing unresolved cases, and a quality-standard close. Since 2 Aug 2026 the EU AI Act requires that people are informed they are interacting with an AI at the latest at first interaction (unless obvious).

### Cited Findings
- [T1-Law][EU] AI Act Article 50(1): providers must ensure AI systems "intended to interact directly with natural persons" are designed so persons "are informed that they are interacting with an AI system", unless obvious. Article 50(5): the information must be given "in a clear and distinguishable manner at the latest at the time of the first interaction" and "conform to the applicable accessibility requirements". Article 50 applies from 2 August 2026. — [Regulation (EU) 2024/1689, Art. 50 (consolidated text via artificialintelligenceact.eu)](https://artificialintelligenceact.eu/article/50/)
- [T1-Law][EU] Law-firm summaries report a provisional "Digital Omnibus on AI" agreement (7 May 2026) that delays high-risk obligations and the AI-generated-content marking duties (to 2 Dec 2026 for some systems). They do *not* report a delay to the Art. 50(1) chatbot-disclosure duty. Formal adoption status needs lane-03 verification. — [White & Case](https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules); [Sidley, 22 Jun 2026](https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/)
- [T3-Practice][Intl] ISO 18295-1:2017, "Customer contact centres — Part 1: Requirements for customer contact centres", "specifies service requirements for customer contact centres". It is applicable to in-house and outsourced centres, all sectors and all channels, inbound and outbound, and includes KPIs "as and where required". It was reviewed and confirmed in 2023. The full text is paywalled and was not read. — [ISO 18295-1 page](https://www.iso.org/standard/64739.html)
- [T3-Practice][Intl] COPC CX Standard Release 7.0 includes editions for customer operations and contact centres. It emphasises managing the whole "service journey" and digital assisted channels, and was announced in 2021–22 per press coverage. It is licensed, not read, and later releases were not checked. — [COPC press release](https://www.copc.com/copc-inc-announces-release-7-0-of-the-copc-customer-experience-cx-standard)
- [T3-Practice][TR] Turkey's national qualification sets out an implied call flow:
  1. Greeting announcement per quality standards.
  2. Effective listening.
  3. Fluent, understandable speech.
  4. Address by name.
  5. Correct case recording by type (information, transaction, sale, complaint, satisfaction, suggestion).
  6. Routing of cases "not resolved at first contact to the correct units".
  7. Closing "according to the speaking-quality standards set by the institution".
  — [MYK 15UY0203-4 Rev.01 (30/10/2019)](https://portal.myk.gov.tr/index.php?dl=Yeterlilik%2F2632%2FSON_TASLAK_PDF_20200625_092024.pdf&fileName=15UY0203-4+Rev+01+%C3%87a%C4%9Fr%C4%B1+Merkezi+M%C3%BC%C5%9Fteri+Temsilcisi&option=com_yeterlilik)
- MEB adds that agents should solve problems "within delegated authority" and ask at the end whether further help is needed. — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T2-Guidance][UK] Non-standard issues (security and fraud, technical, sensitive) likely need a real-time human interface. Automated journeys need routes for unlisted issues and an exit lane. — [FCA FG22/5 §9.18](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf); [FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf)
- [T2-Guidance][UK] The Duty sets no rigid wait or call-length standards, "except where prescribed in other rules, such as our DISP complaint handling rules which require firms to respond to a complaint within eight weeks". — [FCA FG22/5 §9.30 area](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T4-Research][Intl] Forward resolution of predictable next issues reduces repeat contact (HBR, Bell Canada anecdote). End experiences shape memory (Kahneman 1993). Explained, bounded waits are better tolerated (Norman). — [HBR 2010](https://hbr.org/2010/07/stop-trying-to-delight-your-customers); [Kahneman 1993](https://doi.org/10.1111/j.1467-9280.1993.tb00589.x); [Norman](https://jnd.org/the-psychology-of-waiting-lines/)

### Inferences — the framework
All steps are [T5-Verify] design. Each step lists its goal, the agent's behaviour and its guardrail.

0. **Pre-contact context.** Load the intent from IVR or app, the authentication state, open cases and recorded needs (vulnerability, format, representative). *Guardrail:* do not re-ask anything already known; do not reveal account data before authentication.
1. **Opening and disclosures.**
   - Greeting, bank name and AI disclosure at the first turn (required in the EU from 2 Aug 2026; good practice elsewhere).
   - Recording notice where the bank's policy or law requires it. Wording and lawful basis are jurisdiction-specific: KVKK information notice [TR]; UK/EU GDPR transparency; US state consent laws (lane 02/03).
   - Then an open question.
   - EN: "Hello, you're through to [Bank]. I'm the bank's AI assistant. How can I help today?"
   - TR: "[Banka]'ya hoş geldiniz. Ben bankanın yapay zekâ asistanıyım. Size nasıl yardımcı olabilirim?"
2. **Understand the request: symptom vs underlying problem.** Open → funnel → confirm by paraphrase. Ask "what are you trying to achieve?" (for example, the card declined because the customer is abroad and the travel limit is off). Label emotion once if present.
3. **Assess urgency and risk first.**
   - Screen for: active fraud or scam in progress ("someone is on the other line telling me to move money"); lost or stolen card; inability to access essential funds; safeguarding (self-harm, abuse, coercion); vulnerability cues.
   - Then act: fraud and security issues jump the queue (block or freeze first, explain after); safeguarding goes to a human immediately.
   - *Guardrail:* fraud-prevention friction is legitimate when explained (FCA FG22/5 §9.24).
4. **Authenticate proportionately.** Explain why; use step-up only for higher-risk actions; route secrets to secure input; never request PIN, password, CVV or OTP verbally or in text. Carry authentication across transfers where policy allows.
5. **Gather the minimum necessary information.** Ask only what the task requires (data minimisation); confirm critical data by read-back.
6. **Diagnose.**
   - Check systems and tell the customer what you are checking (signposting). Use hold etiquette for longer checks.
   - Distinguish system facts from customer reports. Do not "confirm" an allegation (for example "the merchant stole from you"); record it as reported.
7. **Explain findings in three tiers:** *confirmed facts*, *possibilities* (labelled as such, with policy-based likelihoods) and *unknowns* plus how and when they will be resolved. Plain language, ≤3–4 chunks, an analogy where helpful.
8. **Resolve or escalate.**
   - Act within authority, and state what you have done, not what you "will try".
   - If escalating: say why, to whom, what happens next and expected timing. Warm-transfer with a summary so the customer does not repeat.
   - Offer a human exit at any time, and immediately for complex, sensitive or angry interactions.
9. **Confirm understanding.** Use teach-back for high-stakes or complex steps (disputes, fraud reimbursement claims, loan restructuring). Check agreement with the plan ("Does that plan work for you?").
10. **Set expectations and close.**
    - Recap the actions taken, the reference number, timescales (from policy), how updates will arrive (SMS or app), what to do if nothing happens by date X, and how to complain or escalate (lane 04 for jurisdiction rules).
    - Forward-resolve the predictable next issue (for example new card PIN delivery, or updating recurring payments with the new card number).
    - Ask "anything else?" and end warmly.
    - TR close: "Başka yardımcı olabileceğim bir konu var mı? … İyi günler dilerim."

**Variants by contact type** [T5-Verify]

| Type | What changes |
|---|---|
| Routine information request | Short path: steps 1 → 2 → (4 only if account-specific) → 7 → 10. Answer first, detail second (layering). Offer a self-service link only if the customer wants it. |
| Technical troubleshooting | Reproduce the symptom with closed questions (device, app version, error text); one instruction per turn with confirmation; never ask the customer to disable security features or install remote-access tools; have a fallback channel; forward-resolve (for example "after reinstalling, you'll need to re-register the device"). |
| Suspected fraud or scam | Step 3 dominates: stop the harm (block, freeze), tell the customer to stop contact with the scammer, never request codes. Calm, directive, short sentences (Project BETA "be concise"). Explain the process and timelines without promising reimbursement (rules differ: lanes 07 and 10). Hand off to the fraud specialist warmly. |
| Formal complaint | Treat procedural and interactional justice explicitly. Acknowledge, capture the complaint in the customer's words, confirm what outcome they seek, explain the process, owner and statutory timeframes for the jurisdiction (lane 04), give a reference, and avoid defending policy before listening. |
| Emotionally charged (bereavement, illness, distress) | Slow the pace; TEXAS-style handling; offer a specialist team, call-back or written follow-up; never push sales; check how the customer wants to be contacted. Use the safeguarding route if risk is disclosed. |

### Gaps
- The ISO 18295-1 and COPC requirement texts (for example any mandated customer information on waiting times or complaint handling) could not be read. A detailed clause-by-clause comparison is not possible without licensed copies.
- It was not verified whether Türkiye has adopted ISO 18295-1 as a TS standard, or what replaced EN 15838 (customer contact centres) in TSE's catalogue.
- No Turkish AI-disclosure law was found as of Oct 2026; this needs lane-02 confirmation. No US federal AI-disclosure duty was found; state laws such as California's bot-disclosure statute (SB 1001) and Utah's AI disclosure law are for lane 03 to verify.

---

## 8. Channel-specific variations

### Takeaway
The same framework applies across channels, but pacing, confirmation and security differ:
- **Voice** needs explicit signposting, read-back of numbers in groups, and proper hold and transfer etiquette.
- **Chat** needs concise turns and continuity: never make the customer repeat to a new agent.
- **Email** needs complete, structured, self-contained answers without sensitive data.
- **Messaging apps** (widely used by Turkish banks via verified WhatsApp accounts) are suited to information and guidance under strict "never share secrets" rules.
- **Social media** should acknowledge publicly with empathy and move account matters to private, secure channels.
- **Branch-assisted** contacts must preserve the customer's own voice and choices.

### Cited Findings
- [T1-Law][TR] The CBRT IBAN Communiqué (No. 2008/6, Official Gazette 27020, 10 Oct 2008) sets out the Turkish IBAN:
  - It is "26 alphanumeric characters": TR + 2 check digits + 5-digit bank code + 1 reserved digit + 16-character account number.
  - "On written documents, the IBAN shall be shown in groups of 4 characters starting from left and separated by blank spaces."
  - Electronic form has no spaces.
  — [TCMB, IBAN Communiqué](https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Bottom+Menu/IBAN/Communique)
- [T3-Practice][TR] Turkish spelling-out of letters commonly uses the TDK-originated "Türk Kodlama Sistemi", which uses place names (A–Adana, B–Bolu, C–Ceyhan, Ç–Çanakkale, D–Denizli…). These are secondary sources; the official TDK or TSE document was not located. — [turkedebiyati.org explainer](https://www.turkedebiyati.org/?p=48379)
- [T3-Practice][TR] The mute key is for brief needs such as a cough; hold is for longer waits, with music or institutional information played. First-contact resolution is described as lower in email, SMS and social media, which rely more on back-office processing. — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T3-Practice][TR] MEB's standard hold sentences include "İşleminizi gerçekleştiriyorum, benimle birlikte çok kısa hatta bekleyebilir misiniz?" ("I'm processing your transaction — could you hold with me very briefly?") and "Beklediğiniz için teşekkür ederim" ("Thank you for waiting"). — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T4-Research][Intl] In a customer-service chatbot experiment, *dynamic* response delays (scaled to message complexity) increased perceived humanness, social presence and overall satisfaction compared with near-instant replies. — [Gnewuch, Morana, Adam & Maedche, ECIS 2018](https://aisel.aisnet.org/ecis2018_rp/113)
- [T2-Guidance][UK] Poor practice in chat: several advisers asking the same questions sequentially. Support must be effective "regardless of the channel used". — [FCA FG22/5 §9.7 and example](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)
- [T3-Practice][TR] Turkish banks run official WhatsApp lines with AI bots and human escalation (Garanti BBVA 444 0 333; Yapı Kredi 0850 222 0 444 "BankacıBot"), with verified-badge and never-share-secrets warnings (§3). — [Garanti BBVA](https://www.garantibbva.com.tr/dijital-bankacilik/garanti-bbva-whatsapp); [Yapı Kredi](https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/yapi-kredi-whatsapp)
- [T3-Practice][TR] A bank example of a call-recording statement: "Müşteri İletişim Merkezimiz ile yaptığınız tüm görüşmeler kayıt altına alınmaktadır" ("All calls with our Customer Contact Centre are recorded"). A bank's call-centre KVKK information notice was found adequate in decision 2022/224. — [Ziraat Dinamik](https://www.ziraatdinamik.com.tr/tr/gizlilik-guvenlik/musteri-iletisim-merkezinde-guvenlik); [KVKK 2022/224](https://www.kvkk.gov.tr/Icerik/7296/2022-224)
- Further channel evidence appears earlier: social-media empathy ([Herhausen](https://doi.org/10.1177/00222429221119977)); phone barriers for people with mental health problems ([MMH](https://www.moneyandmentalhealth.org/press-release/access-essentials-pressrelease/)); channel choice, call-backs, relay and sign-language video, and exit lanes ([FCA FG21/1](https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf); [FG22/5 §§9.11–9.18](https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf)).

### Inferences — channel guidance
All items are [T5-Verify].

**Phone and voice (human or AI)**
- **Pacing:** one idea per turn; pause for confirmation; slower pace for older or distressed callers; never talk over the caller (barge-in tuning).
- **Verbal signposting:** "First… then… finally…"; announce silences ("I'm checking your recent payments now, this takes about 20 seconds").
- **Numbers:** read amounts with currency ("two thousand four hundred and fifty lira"). Read IBANs, references and phone numbers digit by digit in **groups of four**, following the TCMB written format: "T-R, three-three; zero-zero-zero-six; …" Confirm group by group for long strings. In TR, use the letter-coding system for letters ("TR: Trabzon'un T'si…"; check the coding list in the bank's style guide). Mask what isn't needed, for example read only the last 4 digits of a card or account. Never read full card numbers aloud.
- **Hold etiquette:**
  - Ask permission, give the reason and an estimated time.
  - Return within the estimate; if it overruns, check back with an update rather than leaving the customer in silence.
  - Thank them on return ("Beklediğiniz için teşekkür ederim").
  - Never use mute as hold (MEB). An AI agent should not need hold for most look-ups; if a back-end call is slow, narrate it.
- **Warm transfer:** explain who and why, pass a summary and the authentication state, and tell the customer they won't need to repeat. If a cold transfer is unavoidable, give a reference and say what to tell the next person.
- **Recording and AI disclosure:** at the start, in jurisdiction-approved wording (see §7, step 1).

**Live chat**
- Concise turns (1–3 sentences); one question per message.
- Set expectations if back-end checks take time ("This may take 2–3 minutes — I'll update you").
- Avoid instant walls of text; light, natural delays may be acceptable per Gnewuch, but never at the expense of speed for urgent issues.
- Use secure in-app links only, never ask for secrets in chat, and preserve the transcript and context across hand-offs (FG22/5 poor practice).
- The multitasking pitfall for human agents (slow, generic replies) maps to an AI risk of losing context. Persist case state and re-read history before replying.

**Email or secure message**
- Self-contained structure: subject with reference → one-line answer → what we did → what happens next (dates) → what you need to do (numbered) → how to contact us.
- No full account numbers, card numbers or secrets; link to the secure inbox or app.
- Answer every question asked (numbered to match); plain language; layering per FG22/5.
- In Turkish, avoid bureaucratic constructions ("…'e istinaden", "tarafınıza dönüş sağlanacaktır") in favour of direct statements (see §9).

**Messaging apps (for example WhatsApp)**
- Asynchronous; the customer may reply hours later, so re-summarise the context when the conversation resumes.
- Start by reminding customers of the verified-account check and the "we never ask for passwords, card details or SMS codes" rule (Turkish bank practice).
- Keep account-specific actions inside authenticated bank channels (app or IVR), per the bank's security model.
- Offer human escalation; handle media (screenshots) carefully, and tell customers not to send images of cards or IDs unless the bank's secure process requires it.

**Social media**
- Public reply: empathise and listen ("We're sorry to hear about this, and we want to look into it"; "Yaşadığınız sorun için üzgünüz; hemen ilgilenmek istiyoruz").
- Move to a private or secure channel, and never confirm account relationships or details publicly.
- Warn against impersonators ("We will never ask for passwords or codes by DM").
- Close the loop publicly where appropriate ("We've been in touch privately").
- Herhausen supports listening and empathy cues in the public reply itself, not just a redirect.

**Branch-assisted (agent supporting branch staff or a customer at a branch tablet)**
- Address the customer, not the companion (FG21/1 case).
- Offer accessible formats (sign-language video interpreters, large print); allow time; avoid jargon.
- Hand over to branch staff with context; respect privacy in a public space (lower voice; no reading of balances aloud).

### Gaps
- No authoritative benchmark was found for live-chat response-time expectations in banking (most figures online are vendor marketing). This is excluded pending a credible industry survey (lane 12).
- The official TDK or TSE letter-coding list was not retrieved. The bank style guide should fix the list and pronunciation for voice agents.
- Social-media practice of Turkish banks (public-reply wording, DM migration policies) was not systematically reviewed.

---

## 9. Turkish communication norms

### Takeaway
Turkish banking service uses formal *siz* and corporate (non-colloquial) register. It addresses customers by name, typically first name + Bey or Hanım ("Hakan Bey", "Ayşe Hanım"), rather than generic "beyefendi" or "hanımefendi" throughout. Official vocational materials (MEB, MYK) set greeting, name-based address, clear language, patience, ownership and an "anything else?" close as expected behaviours. Many legacy "standard sentences" are passive or bureaucratic. Research on concrete, first-person language suggests rewriting them into direct, owned, specific statements.

### Cited Findings
- [T3-Practice][TR] TDK (Turkish Language Association) definitions:
  - **"Bey":** "a word of respect used after men's names".
  - **"Hanım":** "a title given to girls and women".
  - **"Hanımefendi" / "beyefendi":** used after or instead of names to show respect.
  - **"Sayın":** "a word placed before personal names in speech and correspondence as a mark of respect".
  - **"Efendim":** means "I'm here, go ahead" in response to a call, expresses respect and courtesy, and is used to ask someone to repeat something not understood.
  — [TDK Güncel Türkçe Sözlük API (sozluk.gov.tr)](https://sozluk.gov.tr/gts?ara=bey)
- [T3-Practice][TR] MEB expectations: greet customers "in a corporate language", learn and use the customer's name throughout, and speak fluently and understandably. A test item treats "greeting customers in everyday colloquial language" and "addressing as hanımefendi/beyefendi throughout" as *not* the expected behaviour, and "fluent and understandable language" as the expected one. The textbook dialogue models name + Bey ("Bakın Sait Bey…") and the opener "Merhaba! Size nasıl yardımcı olabilirim?" — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T3-Practice][TR] MEB's list of "Çağrı Merkezi Standart Cümleleri" (call-centre standard sentences) includes:
  - "Bilgilerinizi güncelliyorum, lütfen hattan ayrılmayın" ("I'm updating your details, please stay on the line")
  - "Kaydınızı oluşturuyorum" ("I'm creating your record")
  - "Sistemlerimizde güncelleme olması nedeniyle bilgilerinize ulaşılamıyor" ("Your information cannot be accessed due to an update in our systems")
  - "Tarafınıza dönüş sağlanacaktır" ("A return will be provided to you")
  - "Prosedür gereği bunu sizden istemek durumundayım" ("Per procedure I have to ask you for this")
  - "İstisna yapmam söz konusu olamıyor" ("Making an exception is not possible")
  - "Buyurun ben yetkiliyim, nasıl yardımcı olabilirim?" ("Go ahead, I'm the authorised person — how can I help?")
  - "… konulu talebinizi iletiyorum" ("I'm forwarding your request regarding …")
  — [MEB textbook](https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf)
- [T3-Practice][TR] MYK performance criteria include addressing the customer "by name within quality standards", speaking "in line with language rules, fluently and understandably", and closing per the institution's speaking-quality standards. — [MYK 15UY0203-4](https://portal.myk.gov.tr/index.php?dl=Yeterlilik%2F2632%2FSON_TASLAK_PDF_20200625_092024.pdf&fileName=15UY0203-4+Rev+01+%C3%87a%C4%9Fr%C4%B1+Merkezi+M%C3%BC%C5%9Fteri+Temsilcisi&option=com_yeterlilik)
- [T4-Research][Intl] First-person "I" and concrete language improve perceived empathy and listening. — [Packard et al. 2018](https://doi.org/10.1509/jmr.16.0118); [Packard & Berger](https://doi.org/10.1093/jcr/ucaa038)
- [T3-Practice][TR] Industry body: the call-centre association ÇAĞMER (Çağrı Merkezleri Derneği) runs a service-quality certification ("tescil"), as reported in trade press. Its criteria and any quality-language guidance were not accessible. — [CX Magazine TR report](https://cxmag.com.tr/erisim-musteri-hizmetlerinin-servis-kalitesi-cagri-merkezleri-dernegi-tarafindan-tescillendi/)

### Inferences — Turkish phrase bank and style rules
All entries are [T5-Verify]; native-speaker banking review recommended.

**Address**
- Use *siz* throughout, and verb forms in the polite plural ("yapabilir misiniz?", "rica etsem…").
- Use first name + Bey or Hanım only when the bank's record supports it (stored title or preferred address). Otherwise use "Sayın Ad Soyad" in writing and avoid gendered address in speech. A voice agent must not infer gender from voice or name.
- Do not use first names alone; avoid "canım" and "abla/abi"-type familiar address.
- "Efendim" is acceptable as a polite particle and to ask for repetition: "Efendim, sizi tam duyamadım; tekrar edebilir misiniz?" ("Sorry, I didn't quite catch that — could you repeat it?")

**Core phrases (with gloss)**
- "Size nasıl yardımcı olabilirim?" — How can I help you?
- "Beklediğiniz için teşekkür ederim." — Thank you for waiting. (The MEB standard form. The commonly heard "Beklettiğim için teşekkür ederim" literally means "thank you for my having made you wait" and is semantically awkward; prefer "Beklediğiniz için teşekkür ederim" or "Sizi beklettiğim için özür dilerim" — "sorry to keep you waiting".)
- "Anlayışınız için teşekkür ederim." — Thank you for your understanding. Use after you have actually helped; it can sound dismissive if used to shut down a complaint.
- "Yaşadığınız durumun can sıkıcı olduğunu anlıyorum." — I understand the situation is frustrating. Use once, then act.
- "Hemen kontrol ediyorum." — I'm checking right now.
- "Şu an kesin olarak söyleyebileceğim şu: …" — What I can confirm right now is …
- "Bunu yapma yetkim yok; ancak yapabileceğim şu: …" — I'm not authorised to do that, but here's what I can do …
- "Başka yardımcı olabileceğim bir konu var mı?" — Is there anything else I can help with?
- "İyi günler dilerim." / "İyi akşamlar dilerim." — Have a good day / evening.

**Rewrite stiff or bureaucratic constructions (owned, specific, active)**

| Avoid (passive or bureaucratic) | Prefer (direct, owned, concrete) |
|---|---|
| "Talebiniz ilgili birime iletilmiştir." (Your request has been forwarded to the relevant unit.) | "Talebinizi kart itiraz ekibine ilettim; 3 iş günü içinde size SMS ile bilgi verilecek." (I've sent your request to the card dispute team; you'll get an SMS within 3 working days.) |
| "Tarafınıza dönüş sağlanacaktır." (A return will be provided to you.) | "Sizi 15 Ekim'e kadar arayacağız." (We'll call you by 15 October.) |
| "…'e istinaden" (with reference to) | "… ile ilgili olarak" / "… konusunda" |
| "Bilgilerinize ulaşılamamaktadır." (Your information cannot be reached.) | "Şu anda bilgilerinize ulaşamıyorum; sistemde kısa bir güncelleme var. İsterseniz 30 dakika içinde sizi geri arayayım." (I can't access your information right now — there's a brief system update. Shall I call you back within 30 minutes?) |
| "Prosedür gereği bunu sizden istemek durumundayım." (Per procedure I must ask this.) | "Hesabınızı korumak için bunu sormam gerekiyor." (I need to ask this to protect your account.) |
| "İstisna yapmam söz konusu olamıyor." (An exception is out of the question.) | "Bu konuda istisna yapma yetkim yok; ancak şu seçenek mümkün: …" (I can't make an exception, but this option is available: …) |
| "Değerli müşterimiz…" (repeated) | Name + Bey/Hanım, or no address form |

**Register for AI disclosure**
"Ben [Banka]'nın yapay zekâ asistanıyım" ("I'm [Bank]'s AI assistant"). Avoid pretending to be human. Offer a human: "Dilerseniz sizi bir müşteri temsilcisine aktarabilirim" ("If you like, I can transfer you to a customer representative").

### Gaps
- No ÇAĞMER publication on quality language or banned phrases was accessible.
- No YÖK Tez or DergiPark study specifically analysing *linguistic* politeness in Turkish bank call centres was retrieved. A YÖK thesis on Turkish address terms was located ("Address terms in Turkish: A corpus-based study", [acikbilim.yok.gov.tr](https://acikbilim.yok.gov.tr/handle/20.500.12812/220373)) but could not be read (connection error).
- Whether Turkish customers prefer name + Bey/Hanım or surname-based address in banking contexts was not empirically verified; it is based on MEB materials and common practice.

---

## Source register

Access date for all: 2026-10-10. Type tag: R = peer-reviewed research; I = industry or practitioner research; G = regulator or official guidance; L = law or official legal text; S = standard; B = bank or industry-body page; P = press or secondary.

| # | Title | Publisher / author | Date | Jurisdiction | Type | URL | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Stop Trying to Delight Your Customers | HBR; Dixon, Freeman, Toman | Jul–Aug 2010 | Intl | I | https://hbr.org/2010/07/stop-trying-to-delight-your-customers | Paywalled; read via reproduction PDF https://www.satoriconsultinginc.ca/wp-content/uploads/2020/05/Harvard_Business_Review-Stop_Trying_to_Delight_Your_Customers.pdf; dated but foundational |
| 2 | Gartner Reveals Two Actions Customer Service Leaders Must Prioritize… | Gartner | 19 Aug 2020 | Intl | I | https://www.gartner.com/en/newsroom/press-releases/2020-08-19-gartner-reveals-two-actions-customer-service-leaders- | Press release |
| 3 | Gartner Survey Finds 62 Percent of Customer Service Channel Transitions Are High Effort | Gartner | 11 Jul 2023 | Intl | I | https://www.gartner.com/en/newsroom/press-releases/2023-07-11-gartner-survey-finds-62-percent-of-customer-service-channel-transitions-are-high-effort | Title only (403) |
| 4 | Customer Evaluations of Service Complaint Experiences | J. Marketing; Tax, Brown, Chandrashekaran | Apr 1998 | Intl | R | https://doi.org/10.1177/002224299806200205 | Abstract via OpenAlex |
| 5 | A Meta-Analysis of Organizational Complaint Handling and Customer Responses | J. Service Research; Gelbrich & Roschk | 2011 (online Dec 2010) | Intl | R | https://doi.org/10.1177/1094670510387914 | Abstract |
| 6 | Organizational Responses to Customer Complaints: What Works and What Doesn't | J. Service Research; Davidow | Feb 2003 | Intl | R | https://doi.org/10.1177/1094670502238917 | Abstract |
| 7 | Service Recovery Paradox: A Meta-Analysis | J. Service Research; de Matos, Henrique, Rossi | Aug 2007 | Intl | R | https://doi.org/10.1177/1094670507303012 | Abstract |
| 8 | The nature of an apology | Marketing Letters 24(3); Roschk & Kaiser | 2013 | Intl | R | https://ideas.repec.org/a/kap/mktlet/v24y2013i3p293-309.html | Abstract (IDEAS) |
| 9 | When and Why Saying "Thank You" Is Better Than Saying "Sorry"… | J. Marketing; You, Yang, Wang, Deng | 2020 | Intl | R | https://doi.org/10.1177/0022242919889894 | Abstract |
| 10 | Explanations: if, when, and how they aid service recovery | J. Services Marketing; Bradley & Sparks | 2012 | Intl | R | https://doi.org/10.1108/08876041211199715 | Abstract |
| 11 | (I'm) Happy to Help (You) | J. Marketing Research; Packard, Moore, McFerran | 2018 | Intl | R | https://doi.org/10.1509/jmr.16.0118 | Abstract |
| 12 | How Concrete Language Shapes Customer Satisfaction | J. Consumer Research; Packard & Berger | online Jul 2020 | Intl | R | https://doi.org/10.1093/jcr/ucaa038 | Abstract |
| 13 | Complaint De-Escalation Strategies on Social Media | J. Marketing; Herhausen et al. | online Aug 2022 | Intl | R | https://doi.org/10.1177/00222429221119977 | Abstract |
| 14 | Blame the Bot: Anthropomorphism and Anger… | J. Marketing; Crolic et al. | online Aug 2021 | Intl | R | https://doi.org/10.1177/00222429211045687 | Abstract |
| 15 | Machines vs. Humans: AI Chatbot Disclosure… | Marketing Science; Luo et al. | Sep 2019 | Intl | R | https://doi.org/10.1287/mksc.2019.1192 | Abstract (TL;DR only) |
| 16 | Faster is Not Always Better: Dynamic Response Delays… | ECIS 2018; Gnewuch et al. | 2018 | Intl | R (conference) | https://aisel.aisnet.org/ecis2018_rp/113 | Abstract via OpenAlex |
| 17 | Service Scripting: A Customer's Perspective of Quality and Performance | Cornell Center for Hospitality Research; Victorino, Verma, Wardell | 2008 | Intl | I/R | https://scholarship.sha.cornell.edu/chrpubs/153 | Abstract |
| 18 | When More Pain Is Preferred to Less | Psychological Science; Kahneman et al. | Nov 1993 | Intl | R | https://doi.org/10.1111/j.1467-9280.1993.tb00589.x | Abstract |
| 19 | Poverty Impedes Cognitive Function | Science; Mani et al. | Aug 2013 | Intl | R | https://doi.org/10.1126/science.1238041 | Abstract |
| 20 | Putting Feelings Into Words | Psychological Science; Lieberman et al. | May 2007 | Intl | R | https://doi.org/10.1111/j.1467-9280.2007.01916.x | Abstract |
| 21 | The magical number 4 in short-term memory | Behavioral and Brain Sciences; Cowan | Feb 2001 | Intl | R | https://doi.org/10.1017/s0140525x01003922 | Abstract |
| 22 | The effects of communicating uncertainty on public trust… | PNAS; van der Bles et al. | Mar 2020 | Intl | R | https://doi.org/10.1073/pnas.1913678117 | Abstract |
| 23 | Teach-back: A systematic review | PLoS ONE; Talevski et al. | Apr 2020 | Intl | R | https://doi.org/10.1371/journal.pone.0231350 | Healthcare evidence |
| 24 | Verbal De-escalation of the Agitated Patient (Project BETA) | WestJEM; Richmond et al. | Feb 2012 | US/Intl | R (consensus) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3298202/ | Expert consensus |
| 25 | Key components of de-escalation techniques: thematic synthesis | Int J Mental Health Nursing; Price & Baker | Feb 2012 | Intl | R | https://doi.org/10.1111/j.1447-0349.2011.00793.x | Abstract |
| 26 | De-escalation techniques for non-psychosis induced aggression | Cochrane; Spencer, Johnson, Smith | Jul 2018 | Intl | R | https://doi.org/10.1002/14651858.CD012034.pub2 | Abstract |
| 27 | The Psychology of Waiting Lines | Donald Norman (jnd.org) | c. 2008 | Intl | I | https://jnd.org/the-psychology-of-waiting-lines/ | Practitioner essay; Maister 1985 precursor at davidmaister.com |
| 28 | 2026 U.S. Retail Banking Satisfaction Study | J.D. Power | 26 Mar 2026 | US | I | https://www.jdpower.com/business/press-releases/2026-us-retail-banking-satisfaction-study | Industry survey, n=107,059 |
| 29 | Banka Çağrı Merkezi Hizmet Kalitesinin Tüketici Temelli Banka Marka Değerine Etkisi | İşletme Araştırmaları Dergisi 14(1); Işık & Ay | 2022 | TR | R | https://doi.org/10.20491/isarder.2022.1377 | n=738, convenience sample |
| 30 | FG21/1 Guidance for firms on the fair treatment of vulnerable customers | FCA | 23 Feb 2021 | UK | G | https://www.fca.org.uk/publication/finalised-guidance/fg21-1.pdf | Not revised after the 2025 review |
| 31 | FG22/5 Final non-Handbook Guidance on the Consumer Duty | FCA | Jul 2022 | UK | G | https://www.fca.org.uk/publication/finalised-guidance/fg22-5.pdf | Chapters 8–9 used |
| 32 | Firms' treatment of customers in vulnerable circumstances – review | FCA | 7 Mar 2025 (updated 3 Dec 2025) | UK | G | https://www.fca.org.uk/publications/multi-firm-reviews/firms-treatment-vulnerable-customers | Landing page only |
| 33 | Take Five (via NatWest support page; campaign site) | NatWest / UK Finance | undated / © 2026 | UK | B | https://www.natwest.com/support-centre/bank-accounts-and-supporting-information/general/what-is-take-five-and-how-does-it-help-prevent-fraud.html ; https://www.takefive-stopfraud.org.uk/about/take-five/ | |
| 34 | Access Essentials press release | Money and Mental Health Policy Institute | undated (c. 2019) | UK | I | https://www.moneyandmentalhealth.org/press-release/access-essentials-pressrelease/ | Populus survey n=2,000 |
| 35 | Suicide First Aid for Essential Services | Money Advice Trust | undated | UK | B | https://moneyadvicetrust.org/sfa/ | Charity claims |
| 36 | Financial difficulty and mental wellbeing: 2017 workshop series summary (BLAKE) | University of Bristol PFRC | Apr 2018 | UK | I | https://www.bristol.ac.uk/media-library/sites/geography/pfrc/Financial%20difficulty%20%26%20mental%20wellbeing%20-%20workshop%20series%20summary.pdf | Cites Fitch, Evans & Trend 2016 |
| 37 | Vulnerable customers toolkit (TEXAS, IDEA, BLAKE pages) | Just Group plc | © 2026 | UK | B (firm training) | https://inte.vulnerablecustomers.wearejust.co.uk/Your-Toolkit/idea/what-is-idea/ ; https://prep.vulnerablecustomers.wearejust.co.uk/Your-Toolkit/blake/what-is-blake/ ; https://inte.vulnerablecustomers.wearejust.co.uk/recording-vulnerability/texas-in-action/ | Firm material, not official |
| 38 | Unreasonable behaviour policy (v04) | Financial Ombudsman Service | undated | UK | B | https://www.financial-ombudsman.org.uk/corporate/policies/unreasonable-behaviour-policy | |
| 39 | Unreasonable customer policy | NS&I | undated (a Jan 2021 version exists) | UK | B | https://www.nsandi.com/files/asset/corporate/unreasonable-customer-policy.pdf | |
| 40 | AI Act Article 50 (Regulation (EU) 2024/1689) | EU (consolidated text, FLI site) | applies 2 Aug 2026 | EU | L | https://artificialintelligenceact.eu/article/50/ | Verify against EUR-Lex |
| 41 | Digital Omnibus on AI – provisional agreement summaries | White & Case; Sidley | May–Jun 2026 | EU | P | https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules ; https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ | Secondary; lane 03 |
| 42 | ISO 18295-1:2017 Customer contact centres – Part 1 | ISO | 2017 (confirmed 2023) | Intl | S | https://www.iso.org/standard/64739.html | Paywalled |
| 43 | ISO 22458:2022 Consumer vulnerability | ISO | Apr 2022 | Intl | S | https://scc-ccn.ca/standardsdb/standards/8178665 | Paywalled |
| 44 | COPC CX Standard Release 7.0 | COPC Inc. | c. 2021–22 | Intl | S | https://www.copc.com/copc-inc-announces-release-7-0-of-the-copc-customer-experience-cx-standard | Licensed; later release unknown |
| 45 | digital.gov plain language guide (plainlanguage.gov redirect) | US GSA | checked Oct 2026 | US | G | https://digital.gov/guides/plain-language/ | Redirect observed; content not reviewed |
| 46 | Çağrı Merkezi İşlemleri 11 (ders materyali) | MEB; Yıldız, Güler, Özen | approved 24.12.2020 | TR | G (official curriculum) | https://meslek.meb.gov.tr/upload/dersmateryali/pdf/%C3%87A%C4%9ERI%20MERKEZ%C4%B0%20%C4%B0%C5%9ELEMLER%C4%B0%2011%20(Halkla%20%C4%B0li%C5%9Fkiler).pdf | ISBN 978-975-11-6851-1 |
| 47 | 15UY0203-4 Çağrı Merkezi Müşteri Temsilcisi (Seviye 4) Ulusal Yeterlilik | MYK | Rev.01, 30/10/2019 | TR | S (national qualification) | https://portal.myk.gov.tr/index.php?dl=Yeterlilik%2F2632%2FSON_TASLAK_PDF_20200625_092024.pdf&fileName=15UY0203-4+Rev+01+%C3%87a%C4%9Fr%C4%B1+Merkezi+M%C3%BC%C5%9Fteri+Temsilcisi&option=com_yeterlilik | |
| 48 | Güncel Türkçe Sözlük (bey, hanım, hanımefendi, beyefendi, sayın, efendim) | TDK | live | TR | G | https://sozluk.gov.tr/gts?ara=bey | API queried |
| 49 | Law No. 6502 Tüketicinin Korunması Hakkında Kanun, Art. 4 | TBMM / mevzuat.gov.tr | 2013 (as amended) | TR | L | https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6502.pdf | Official text |
| 50 | IBAN Communiqué No. 2008/6 | TCMB (CBRT) | OG 27020, 10 Oct 2008 | TR | L | https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Bottom+Menu/IBAN/Communique | English page |
| 51 | KVKK Board Decision 2022/224 | KVKK | 10 Mar 2022 | TR | L/G | https://www.kvkk.gov.tr/Icerik/7296/2022-224 | Summary via fetch |
| 52 | Müşteri İletişim Merkezinde Güvenlik | Ziraat Dinamik | undated | TR | B | https://www.ziraatdinamik.com.tr/tr/gizlilik-guvenlik/musteri-iletisim-merkezinde-guvenlik | |
| 53 | ING Bilgi ve İşlem Güvenliği Farkındalığı Bildirimi | ING Türkiye | undated | TR | B | https://www.ing.com.tr/tr/ing/guvenlik/ing-bilgi-islem-guvenligi-farkindaligi-bildirimi | Via Firecrawl search snippet |
| 54 | Garanti BBVA WhatsApp | Garanti BBVA | undated | TR | B | https://www.garantibbva.com.tr/dijital-bankacilik/garanti-bbva-whatsapp | |
| 55 | Yapı Kredi WhatsApp | Yapı Kredi | undated | TR | B | https://www.yapikredi.com.tr/isim-icin/sinirsiz-bankacilik/iletisim-ve-yardim/yapi-kredi-whatsapp | |
| 56 | Türkiye'de 23 banka engelli bireylere bankacılık hizmeti veriyor | Sözcü (TBB data) | 30 Nov 2025 (data Jun 2025) | TR | P | https://www.sozcu.com.tr/turkiye-de-23-banka-engelli-bireylere-bankacilik-hizmeti-veriyor-p264995 | Press reproduction of TBB data |
| 57 | Engeli Olan Bireylerle Kapsayıcı İletişim e-Eğitimleri | Alomaliye (TBB announcement) | 19 Oct 2023 | TR | P | https://www.alomaliye.com/2023/10/19/engeli-olan-bireylerle-kapsayici-iletisim-e-egitimleri-hakkinda/ | Secondary reproduction |
| 58 | TDK harf kodlama explainer | turkedebiyati.org | undated | TR | P | https://www.turkedebiyati.org/?p=48379 | Secondary; official list not found |
| 59 | ÇAĞMER service-quality certification news | CX Magazine TR | c. 2020 | TR | P | https://cxmag.com.tr/erisim-musteri-hizmetlerinin-servis-kalitesi-cagri-merkezleri-dernegi-tarafindan-tescillendi/ | Criteria not accessible |
| 60 | Verbal Judo training slides | Indiana University of Pennsylvania / PA Municipal League | 2018 (© 2016) | US | I | https://www.iup.edu/teachingexcellence/files/reflective_practice/past_events/2018-19/facilitating_challenging_conversations_in_the_classroom/11-7-18-rplgm-de-escalation-powerpoint-verbal-judo.pdf | LEAPS acronym not found in the slides |

---

## Open questions, unverified items and items needing institution-specific confirmation

1. **The Gartner "96% vs 9%" disloyalty statistic.** Not verified in a primary Gartner source; do not use until it is.
2. **FCA 2025 vulnerability review statistics** ("58%", "88%", "29%" quoted by a law-firm summary). Not on the FCA landing page; check the full report before use. The summary also misstated the four drivers.
3. **"IDEA" vs "BLAKE".** The brief described IDEA as a suicide-risk approach. The sources show IDEA is a vulnerability-exploration question set and BLAKE is the suicide-disclosure protocol (University of Bristol PFRC; Fitch, Evans & Trend 2016). The detailed BLAKE prompts come from a firm's training site. The original 2016 guide and the Money Advice Trust/Royal College of Psychiatrists guidance were not retrieved.
4. **AI agent and suicide-risk questioning.** Whether an AI agent should ask direct questions about suicide plans (the BLAKE "Ask" step) needs clinical, legal and bank-policy sign-off. The safe default is an immediate warm transfer to trained humans plus emergency-number signposting.
5. **Turkish crisis resources.** Confirm the national emergency number usage (112) and whether any dedicated crisis or suicide helpline exists, as well as bank safeguarding procedures in Türkiye.
6. **EU AI Act.** Confirm (lane 03) the formal adoption of the Digital Omnibus and that Art. 50(1) applies unchanged from 2 Aug 2026. Confirm whether Türkiye (lane 02) or the UK and US (lane 03) impose any AI-disclosure duty on bank chatbots or voicebots.
7. **Call-recording notices.** Exact KVKK information-notice wording and lawful basis for recording [TR] (lane 02). UK/EU GDPR transparency, and US one-party versus all-party consent states for recorded calls (lane 03).
8. **Turkish regulatory guidance on vulnerable or disabled customers in bank contact centres** (BDDK, TCMB, the Ministry of Family and Social Services accessibility rules, TBB recommendations). Only TBB statistics and an e-training were found; the primary TBB documents still need retrieving.
9. **ÇAĞMER quality-language standards.** Not accessible; ask ÇAĞMER or partner banks for their quality-monitoring forms ("kalite değerlendirme formu") and banned-phrase lists.
10. **ISO 18295-1, ISO 22458 and the COPC CX Standard** were not read (paywalled or licensed). Whether TSE adopted ISO 18295-1 (and what replaced TS EN 15838) is unverified, as is whether COPC has released a version later than 7.0.
11. **Bank-specific items to confirm with each institution:**
    - authentication methods and step-up thresholds;
    - which secrets are entered via IVR or app (never spoken);
    - official WhatsApp and social handles and what may be handled there;
    - complaint timeframes and escalation routes (lane 04);
    - refund or reimbursement authorities (lanes 07/10);
    - accessible-channel availability (sign-language video, relay, large print);
    - third-party authority and power-of-attorney processes;
    - the vulnerability recording process and lawful basis;
    - the unacceptable-behaviour policy (warning wording, who may end a contact, restrictions);
    - the safeguarding escalation path.
12. **Turkish phrasing.** All Turkish patterns in these notes need review by a native-speaking banking writer and the bank's legal team. Pay particular attention to gender-neutral address, the "Beklettiğim/Beklediğiniz" usage, and terminology ("provizyon", "kullanılabilir bakiye", "itiraz").
13. **Live-chat response-time expectations, and voice-agent pacing and barge-in parameters.** No credible banking-specific benchmark was found (lane 12).
14. **Dated evidence.** HBR 2010 and the FCA's Feb–Oct 2020 vulnerability prevalence are dated; Gartner 2020 is more recent but still cross-industry. Newer effort or vulnerability data (Gartner 2023–2026; FCA Financial Lives 2024) were not accessed.
15. **Primary sources for the de-escalation mnemonics** (HEAT, HEARD, LAST, LEAP, LEAPS) were not retrieved (403 errors or acronym not found). Treat them as practitioner tools without validation evidence, and train on evidence-based components instead.
