# Issue #22 — Novelty and Contribution Re-audit

## 0. Decision rule

Novelty hanya dipertahankan bila ia bertahan terhadap targeted falsification. Perbedaan kombinasi variabel, lokasi DKI, penggunaan mediator SEC, penggunaan SEM, atau penggunaan instrumen tertentu **tidak** cukup. Kontribusi harus berupa explanatory discrimination, boundary/configuration insight, measurement insight yang transferable, atau empirical evidence yang bernilai karena design dan population evidence-nya—bukan karena sekadar `belum pernah digabung`.

## 1. Final construct map setelah Issues #16–#21

- **X1:** Adolescent-Perceived Digital Parental Mediation (DPM), multidimensional dan strategy-specific.
- **X2:** Perceived Teacher Support (PTS), multidimensional dan student-perceived.
- **Z:** Student Social-Emotional Competence (SEC), multidimensional student attribute.
- **Y:** Student Engagement in Learning, multidimensional.
- **Contextual theory:** bioecological/neo-ecological positioning.
- **Primary proximal theory:** Self-Determination Theory / self-system process logic untuk need support → motivation/engagement.
- **Competing mechanisms:** basic psychological needs, autonomous motivation, self-efficacy, self-regulation/SRL, teacher-student relationship, classroom climate, prior engagement, general parenting, peers.

## 2. Falsification search findings

Targeted search menemukan model-model yang cukup dekat untuk menggugurkan sebagian besar novelty claims berbasis konfigurasi.

### 2.1 DPM + SEC sudah pernah dipertemukan

Cheng et al. meneliti active/restrictive digital parental mediation dan social-emotional competence pada sekitar 1,599 anak/remaja di China dalam kaitannya dengan cyberbullying [@cheng2024dpmsec]. Outcome berbeda dari engagement, tetapi temuan ini cukup untuk menolak klaim bahwa menghubungkan DPM dengan SEC merupakan kombinasi baru. Studi tersebut juga menunjukkan pattern yang tidak selalu searah dengan asumsi normatif: SEC memiliki association yang tidak sederhana terhadap cyberbullying roles.

**Falsification result:** `DPM → SEC is novel` = **REJECT**.

### 2.2 Parent + teacher support + engagement + regulatory/self-belief mediators sudah sangat dekat

Song et al. menguji teacher support dan parent support terhadap learning engagement siswa middle school melalui self-regulation dan self-efficacy [@song2026supportengagement]. Ini sangat dekat dengan arsitektur cross-context support → student capacity → engagement.

Jelas et al. sebelumnya juga menguji perceived support dari orang tua, guru, dan teman dengan engagement sebagai mediator menuju achievement [@jelas2016learningsupport]. Wang dan Eccles menunjukkan secara longitudinal bahwa berbagai sumber dukungan tidak mempunyai efek yang sama pada setiap dimensi engagement [@wangeccles2012support].

**Falsification result:** `family + school contexts → student mechanism → engagement is novel` = **REJECT**.

### 2.3 Arah SEC ↔ engagement tidak boleh diasumsikan satu arah

Santos et al. menunjukkan association SEC–engagement secara sistematis [@santos2023secengagement], tetapi Martinez-Yarza et al. menemukan konfigurasi family involvement → school engagement → social-emotional development, yaitu arah di mana engagement menjadi mediator menuju SEC [@martinezyarza2024familysec]. Ini penting karena model Gemma semula menempatkan SEC sebagai mediator menuju engagement.

**Falsification result:** `SEC is naturally upstream of engagement` = **REJECT as assumption; RETAIN only as competing temporal model to test**.

### 2.4 Alternative mediators memiliki evidence yang kuat dan lebih proximal

An et al. menunjukkan teacher support → technology acceptance/motivation → engagement [@an2022teachersupport]. Song et al. menunjukkan self-regulation/self-efficacy sebagai mediators [@song2026supportengagement]. Wang et al. menggunakan longitudinal design dan menemukan cognitive reappraisal sebagai mediator teacher support → engagement, sementara family cohesion memiliki pattern berbeda [@wang2024socialsupport]. SDT meta-analytic evidence juga mendukung basic psychological needs/autonomous motivation sebagai proximal mechanisms dari supportive contexts menuju student outcomes [@howard2025needsupport; @bureau2022motivation].

**Falsification result:** `SEC is the uniquely warranted mediator` = **REJECT**.

### 2.5 Teacher-support effect tidak universal

Meta-analysis mendukung positive average association tetapi heterogeneous [@vargasmadriz2024support]. Ansong et al. menemukan pada sampel Ghana bahwa classmate dan parent support lebih kuat, sementara teacher support tidak menjadi direct predictor atau mediator engagement dalam model mereka [@ansong2017support]. Quin et al. juga menunjukkan bahwa setelah broader ecological predictors dimasukkan, prior engagement dan academic grades menjelaskan porsi lebih besar dibanding teacher support [@quin2018ecological; TODO-CITATION-KEY if not yet in central bibliography].

Karena `quin2018ecological` belum ada pada central bibliography saat audit ini disusun, manuscript tidak boleh menggunakannya sampai metadata disinkronkan pada integration issue. Falsification utama tetap dapat berdiri dari Vargas-Madriz, Ansong, Wang, dan existing evidence.

**Falsification result:** `PTS has a universal direct effect on engagement` = **REJECT**.

### 2.6 Digital parenting effects conditional, bidirectional, dan strategy-specific

Existing audit sudah menunjukkan bahwa broad DPM effects weak/heterogeneous [@lukavska2022parenting; @vossen2024parenting], child effects dapat mendominasi pada beberapa online-behavior domains [@tong2024internetparenting], dan specification-curve evidence tidak mendukung blanket longitudinal benefits dari parental media mediation [@huang2023mediation].

**Falsification result:** `higher DPM is uniformly beneficial` = **REJECT**.

## 3. Novelty claim inventory

| Candidate claim | Decision | Reason |
|---|---|---|
| X1-X2-Z-Y combination | **REJECT** | Combination novelty; adjacent integrated models already exist |
| DPM + SEC | **REJECT** | Direct adjacent evidence exists [@cheng2024dpmsec] |
| Parent + teacher context + mediator + engagement | **REJECT** | Song/Jelas/Wang-Eccles already cover close architecture |
| SEC as mediator | **REJECT** | SEC/engagement relationship already modeled; direction also contested |
| PTS → engagement | **REJECT as novelty** | Mature meta-analytic/longitudinal literature |
| DKI Jakarta location | **REJECT** | Location ≠ boundary condition or theory contribution |
| SEM/PLS-SEM | **REJECT** | Estimator is method, not novelty |
| Indonesian adaptation of instruments | **REJECT as standalone novelty** | Local validation is methodological necessity; contribution only if transferable measurement insight emerges |
| Strategy-specific DPM instead of one global parenting score | **QUALIFY** | Conceptually stronger, but multidimensional DPM is already established in literature |
| Cross-context reinforcement vs compensation between DPM and PTS | **RETAIN as candidate explanatory contribution** | Requires explicit interaction/configuration test and survives only if theory-driven and empirically discriminable |
| SEC versus SDT/self-regulation/self-efficacy as competing mechanisms | **RETAIN as candidate mechanism-discrimination contribution** | Valuable only if design compares mechanisms rather than assuming SEC mediation |
| Temporal ordering SEC ↔ engagement | **RETAIN as candidate empirical/explanatory contribution** | Existing evidence allows competing direction; longitudinal design needed |
| Individual-level SMP DKI evidence with construct-valid measurement | **QUALIFY as empirical contribution** | Useful contextual evidence, not theory novelty; value depends on sampling/design quality |

## 4. Contribution matrix

### 4.1 Theoretical contribution

**Potential, not established:** The strongest defensible theoretical contribution is **mechanism discrimination across ecological contexts**, specifically whether family digital mediation strategies and perceived teacher support relate to engagement through the same proximal mechanism, through distinct mechanisms, or through conditional cross-context configurations.

This is stronger than simply saying `SEC mediates both X1 and X2`. The contribution requires comparing SEC against at least one theoretically proximal rival mechanism, preferably basic psychological need satisfaction/autonomous motivation for PTS and/or self-regulatory competence for DPM.

### 4.2 Empirical contribution

**Retain with qualification:** High-quality individual-level evidence among SMP students in DKI can be useful because current Indonesia evidence is fragmented across constructs, instruments, and settings. This is an **empirical/contextual extension**, not theoretical novelty. Its value rises if sampling is probability-based/multistage, constructs are validated, clustering is handled, and temporal structure improves on prevailing cross-sectional evidence.

### 4.3 Methodological contribution

**Do not claim by default:** CFA, SEM, multilevel SEM, longitudinal mediation, measurement invariance, or Monte Carlo power analysis are not methodological contributions merely because they are used correctly. A methodological contribution would require evidence that the study develops or validates a measurement/estimation insight that generalizes beyond this sample.

### 4.4 Practical contribution

**Potential:** If strategy-specific DPM and specific PTS domains show different associations with engagement mechanisms, practical recommendations can distinguish enabling/restrictive/observant parental practices and instrumental/emotional/informational/appraisal teacher support. But practical recommendations must follow effect sizes and robustness, not merely statistical significance.

## 5. Competing-model map

The final methodology should compare a small set of theory-derived models rather than one preferred mediation chain.

### Model A — SEC mechanism

- enabling DPM → SEC → engagement
- PTS → SEC → engagement
- direct PTS → engagement retained
- restrictive/observant DPM paths estimated non-directionally or exploratory unless evidence warrants direction

### Model B — SDT/self-system mechanism

- PTS → basic psychological need satisfaction / autonomous motivation → engagement
- DPM included as context but not forced through the same mediator

This model is expected to be especially competitive for the school-support pathway.

### Model C — self-regulation/self-efficacy mechanism

- DPM/PTS → self-regulation and/or self-efficacy → engagement

Song et al. and related literature make this a serious rival rather than a nuisance model [@song2026supportengagement].

### Model D — reciprocal/temporal alternative

- prior engagement → later perceived support and/or SEC
- engagement → later SEC

Existing developmental and transactional evidence makes reverse pathways plausible [@tong2024internetparenting; @martinezyarza2024familysec].

### Model E — cross-context interaction

- enabling DPM × PTS → engagement and/or SEC

Two competing predictions must be pre-specified:

1. **Reinforcement:** high support in both contexts yields strongest engagement/capacity.
2. **Compensation:** strong PTS matters more when enabling DPM is low, or vice versa.

A main-effects-only model cannot distinguish these theories.

## 6. Final contribution statement

> Penelitian ini tidak mengklaim novelty dari penggabungan Digital Parental Mediation, Perceived Teacher Support, Social-Emotional Competence, dan Student Engagement, maupun dari lokasi DKI Jakarta atau penggunaan SEM. Candidate contribution yang lebih defensible adalah menguji secara individual-level dan temporally ordered apakah family-digital dan school-support contexts menunjukkan mekanisme yang sama atau berbeda menuju student engagement; apakah SEC memberi explanatory value setelah dibandingkan dengan proximal motivational/regulatory mechanisms; dan apakah hubungan lintas konteks lebih konsisten dengan reinforcement atau compensation. Kontribusi empiris berada pada kualitas evidence SMP DKI yang construct-valid dan design-aware, bukan pada klaim bahwa setting tersebut belum pernah diteliti.

## 7. Model implications

1. **Drop:** one global DPM latent score dan one global positive DPM hypothesis.
2. **Retain:** PTS as a multidimensional school-context predictor.
3. **Retain but challenge:** SEC as one candidate mechanism, not privileged mediator.
4. **Add:** at least one competing proximal mechanism in design/analysis plan; basic psychological needs/autonomous motivation is the strongest theory-derived comparator for PTS.
5. **Add:** baseline engagement in longitudinal design to address stability/reverse pathways.
6. **Consider:** DPM × PTS interaction only if sample size/power supports it and construct dimensionality is manageable.
7. **Do not over-expand:** avoid a kitchen-sink SEM with every rival mediator; Issue #23 must prioritize a confirmatory core and limited preregistered competing models.

## 8. Boundary conditions

Boundary-condition claims must be mechanism-based. Current evidence does **not** establish DKI as a theoretical boundary. More defensible conditions are:

- school level / developmental stage;
- informant and level of aggregation;
- type of DPM strategy;
- type of PTS domain;
- prior engagement level;
- digital-use purpose/context;
- possibly SES/general parenting as moderators only when theory predicts differential mechanisms.

These are candidate conditions, not all required moderators.

## 9. Reference synchronization

New targeted-falsification sources to synchronize in this issue/final integration:

- Cheng, Huang, & Lai (2024), DOI 10.1007/s40299-024-00838-1.
- Song, Ishak, & Wei (2026), DOI 10.36941/jesr-2026-0347.
- Martinez-Yarza, Solabarrieta-Eizaguirre, & Santibáñez-Gruber (2024), DOI 10.1007/s10212-024-00862-1.
- Wang, Jimerson, Saiding, Guo, & Chen (2024), DOI 10.1037/spq0000673.
- Ansong, Okumu, Bowen, Walker, & Eisensmith (2017), DOI 10.1016/j.ijedudev.2017.03.010.

## 10. Decision

**ISSUE #22 DECISION: PASS, WITH NOVELTY REFRAMED.**

Most original novelty claims fail falsification. The study remains potentially doctoral-level only if it is redesigned as a **mechanism-discrimination and cross-context configuration study**, supported by longitudinal/temporally ordered data and explicit competing models. The theoretical contribution is therefore **candidate**, not yet established; the empirical contribution is defensible as high-quality individual-level evidence in SMP DKI if Issue #23 delivers a strong design.