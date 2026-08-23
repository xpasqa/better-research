# Issue #19 — Lock Z Social-Emotional Competence

## 0. Decision rule

Z hanya dapat dipertahankan bila construct yang diukur adalah atribut/kompetensi siswa, bukan exposure terhadap program atau proses pembelajaran sosial-emosional. Karena itu `SEL` dan `SEC` dipisahkan secara tegas.

## 1. Construct boundary: SEL ≠ SEC

CASEL mendefinisikan social and emotional learning (SEL) sebagai **proses** melalui mana individu memperoleh dan menerapkan pengetahuan, keterampilan, dan sikap sosial-emosional, sedangkan lima area CASEL adalah domain kompetensi: self-awareness, self-management, social awareness, relationship skills, dan responsible decision-making [@casel2020framework].

Dengan demikian:

- **SEL** = process/program/learning environment;
- **SEC** = student attribute/competence;
- jika kuesioner meminta siswa menilai kemampuan diri pada domain tersebut, variabelnya adalah SEC, bukan SEL.

**Decision:** label `Pembelajaran Sosial-Emosional` tidak digunakan untuk mediator student attribute.

## 2. Final construct name and definition

> **Z = Student Social-Emotional Competence (SEC) / Kompetensi Sosial-Emosional Siswa**

SEC didefinisikan sebagai **kapasitas multidimensional siswa untuk mengenali dan mengelola diri dan emosi, memahami perspektif/situasi sosial, membangun dan mengelola hubungan, serta membuat keputusan yang bertanggung jawab dalam konteks perkembangan dan sekolah**.

Definisi ini tidak menyamakan SEC dengan satu trait psikologis tunggal dan tidak menyamakan seluruh domain dengan emotion regulation saja.

## 3. Dimensionality evidence

Systematic review Martinez-Yarza et al. mengidentifikasi 25 unique assessments untuk social/emotional skills pada siswa usia sekolah dan menekankan pluralitas instrumen serta nilai multi-method/multi-informant assessment [@martinezyarza2023instruments]. Ini sendiri sudah membantah asumsi bahwa lima area CASEL otomatis merupakan satu reflective factor yang sudah tervalidasi.

### 3.1 Primary candidate: Social Emotional Competence Questionnaire (SECQ)

Zhou dan Ee mengembangkan 25-item SECQ untuk lima domain:

1. self-awareness;
2. social awareness;
3. self-management;
4. relationship management;
5. responsible decision-making.

Model tersebut diuji dalam beberapa studi dan direplikasi pada sampel 356 secondary-school students [@zhou2012secq]. Karena struktur konstruk mendekati working definition Gemma dan population fit-nya mencakup secondary students, SECQ menjadi **primary content/measurement candidate**.

### 3.2 Cross-language evidence matters

Jabeen dan Maqsood melakukan translasi dan validation SECQ pada 910 adolescent students dan membandingkan beberapa struktur: five correlated factors, unidimensional, two-global-factor, five factors plus two higher-order, dan five factors plus one higher-order. Five-factor model memberikan fit terbaik dalam validation mereka, sedangkan unidimensional model lebih buruk [@jabeen2023secq].

Portela-Pino et al. pada 429 siswa usia 12–16 juga menemukan bahwa beberapa structural specifications perlu dibandingkan dan bahwa original re-specified model memberi fit terbaik dalam sampel mereka [@portelapino2024secq]. Ini menunjukkan **factor structure tidak boleh di-lock hanya dari nama CASEL; target-sample model comparison tetap wajib**.

### 3.3 Evidence Indonesia

Setiyorini et al. menguji instrumen SEC berbasis lima domain CASEL pada 220 high-school students di Indonesia dan melaporkan CFA fit yang memadai serta internal consistency tinggi [@setiyorini2025sec]. Evidence ini memperkuat cultural plausibility bahwa five-domain SEC dapat dioperasionalisasikan di Indonesia, tetapi tidak merupakan validation langsung SECQ pada siswa SMP DKI dan tidak membuktikan invariance antar jenjang/lokasi.

## 4. Measurement specification

### Primary specification

Default measurement model Gemma:

- **five correlated first-order SEC dimensions**;
- setiap domain memiliki indicators sendiri;
- tidak menjumlahkan seluruh item menjadi satu skor global sebelum model comparison;
- higher-order general SEC hanya boleh digunakan jika CFA/ESEM target sample menunjukkan fit dan interpretability yang memadai dibanding correlated-five-factor alternative.

### Structures to compare in #23

Minimum measurement comparison:

1. five correlated first-order factors;
2. one higher-order general SEC over five lower-order dimensions;
3. unidimensional model sebagai falsification benchmark;
4. bila empirically warranted, ESEM/bifactor sensitivity analysis—bukan otomatis primary model.

Pemilihan model harus mempertimbangkan model fit, factor loadings, residual structure, discriminant validity, factor correlations, reliability/omega, dan substantive interpretability—bukan hanya satu indeks fit.

## 5. Informant decision

### Primary

**Student self-report** dipilih sebagai primary SEC measure karena konstruk yang dimaksud mencakup perceived competencies internal yang sebagian tidak selalu observable oleh guru/orang tua.

### Corroboration

Martinez-Yarza et al. mendukung kombinasi multi-method dan multi-informant untuk social/emotional skills [@martinezyarza2023instruments]. Karena itu, jika sumber daya memungkinkan, teacher/parent report atau direct assessment untuk subset domain digunakan sebagai validation/corroboration, bukan dipaksa menjadi interchangeable measures.

Common-method risk penting: X1, X2, Z, dan Y dapat semuanya berasal dari siswa. #23 harus memitigasi ini melalui temporal separation, multiple informants where feasible, latent-method sensitivity, dan desain survey yang mencegah item-context contamination.

## 6. Discriminant boundary against Y and rival mediators

### SEC vs Student Engagement

SEC adalah **capacity/competence**, sedangkan engagement adalah **state/quality of participation and investment in learning/school activities**. Santos et al.'s systematic review of 91 studies (92,879 youth) menunjukkan association antara SEC dan engagement/disengagement [@santos2023secengagement]. Fakta bahwa kedua construct berkorelasi justru membutuhkan discriminant validity; itu bukan alasan untuk menggabungkannya.

### SEC vs Self-Regulated Learning

SRL mencakup planning, monitoring, strategy use, motivation, and regulation specifically in learning processes. Ia tumpang tindih terutama dengan self-management tetapi lebih domain-specific ke learning. Panadero dan Dent & Koenka menunjukkan SRL sebagai teori/konstruk matang dengan hubungan terhadap achievement [@panadero2017srl; @dent2016srl]. **SRL tetap rival mediator**, bukan indikator SEC.

### SEC vs motivation/self-efficacy

Motivation dan academic self-efficacy adalah motivational-belief mechanisms, bukan SEC secara keseluruhan. Existing PTS literature menunjukkan mechanism melalui motivation/self-efficacy sehingga keduanya harus dipertahankan sebagai rival explanations pada #20/#22, bukan dimasukkan ke SEC score.

### SEC vs emotion regulation

Emotion regulation adalah sub-domain/relevant capability yang dekat dengan self-management, tetapi SEC lebih luas karena mencakup awareness, social awareness, relationships, and responsible decision-making. Jalur X1 yang terutama memengaruhi online self-regulation tidak boleh otomatis digeneralisasikan ke full SEC.

## 7. Antecedent evidence

### 7.1 DPM → SEC

Evidence terdekat tetap Chen & Chng: active/restrictive parental mediation berhubungan longitudinal dengan online self-regulation, emotion regulation, dan impulsivity [@chen2016mediation]. Ini mendukung **plausibility untuk selected self-regulation facets**, tetapi belum merupakan construct-matched evidence bahwa seluruh multidimensional DPM meningkatkan full five-domain SEC.

Dengan demikian:

- `DPM → full SEC` = **plausible but weakly established**;
- strategy-specific DPM effects harus dipertahankan;
- direct global positive hypothesis tidak boleh otomatis dibuat.

### 7.2 PTS → SEC

Collie menunjukkan pada secondary students bahwa perceived autonomy/competence-supportive teaching berhubungan dengan perceived competence untuk emotion regulation dan conflict resolution [@collie2022supportsec]. Teacher-student relationship literature juga menunjukkan links dengan social competence [@magro2023studentteacher].

Dengan demikian:

- `PTS → selected SEC domains` = **supported/plausible**;
- `PTS → full general SEC` = masih memerlukan direct construct-matched testing;
- PTS, TSR, dan instructional quality harus tetap dibedakan.

## 8. Outcome evidence: SEC → engagement

Santos et al. memberikan systematic-review evidence paling direct untuk hubungan social/emotional competencies dengan student engagement pada youth [@santos2023secengagement]. Existing Yin et al. juga menunjukkan SEC dan academic engagement dapat berada dalam mediation/configuration models pada adolescent sample [@yin2023secengagement].

**Decision:** SEC→engagement memiliki construct-matched association evidence yang cukup untuk dipertahankan sebagai substantive pathway candidate. Namun evidence tersebut **tidak membuktikan bahwa SEC secara kausal memediasi DPM/PTS → engagement**.

## 9. Mediator role: retain, but as a competing mechanism

SEC dipertahankan sebagai **primary candidate developmental mechanism**, bukan sebagai mediator yang otomatis benar karena posisinya di tengah diagram.

Untuk standard doctoral-level contribution, #20/#22 harus membandingkan explanatory status SEC terhadap minimal satu rival mechanism yang lebih proximal terhadap engagement, terutama:

- academic motivation / basic psychological needs;
- academic self-efficacy;
- self-regulated learning/self-management;
- teacher-student relational quality where relevant.

Tidak semua rivals harus masuk model final. Pemilihan harus mengikuti theory, construct overlap, parsimony, sample/power, dan estimand.

## 10. Causal and mediation language

Dengan observational survey:

- gunakan `berhubungan dengan`, `association`, `indirect statistical pathway`;
- longitudinal ordering meningkatkan temporal plausibility tetapi tidak menghapus unmeasured confounding;
- cross-sectional mediation tidak boleh disebut mechanism effect;
- baseline SEC dan engagement sangat disarankan bila mediation menjadi central contribution.

## 11. Instrument decision

| Candidate | Population | Structure | Strength | Limitation | Role |
|---|---|---|---|---|---|
| Zhou & Ee SECQ | children + secondary students | 5 domains, 25 items | direct CASEL-like domain coverage; secondary replication | older original development; requires Indonesian adaptation | **PRIMARY candidate** |
| Jabeen & Maqsood Urdu SECQ | adolescents 10–19 | five-factor best among tested models | strong cross-language/adolescent evidence | Pakistan; non-random sample | structural/adaptation evidence |
| Portela-Pino et al. SECQ | adolescents 12–16 | compared alternative structures | age fit and current psychometrics | Spanish context; structure not identical in all details | sensitivity evidence |
| Setiyorini et al. CASEL-based SEC instrument | Indonesian high school | 5 domains | Indonesian-language/context evidence | not necessarily same SECQ; N=220; high school | local contextual psychometric anchor |

## 12. Consequences for final structural model

The provisional core is now:

- X1 = multidimensional adolescent-perceived DPM;
- X2 = multidimensional PTS;
- Z = multidimensional student SEC;
- Y = multidimensional student engagement.

This is **not yet a license to draw every possible direct and indirect path**. #20 must derive paths from proximal theory. #22 must falsify novelty and competing mechanisms. #23 must determine whether the resulting latent model is estimable with the proposed longitudinal/nested design.

## 13. Definition of Done

- [x] SEL process and SEC attribute separated.
- [x] SEC name/definition locked.
- [x] Primary adolescent instrument candidate identified.
- [x] Five-factor versus higher-order/unidimensional alternatives specified for comparison.
- [x] Multi-informant recommendation recorded.
- [x] Boundary against engagement, SRL, motivation/self-efficacy and emotion regulation audited.
- [x] DPM→SEC evidence rated weak/adjacent rather than overstated.
- [x] PTS→SEC evidence rated plausible/partial rather than universal.
- [x] SEC→engagement construct-matched evidence documented.
- [x] Mediator status retained conditionally with rival mechanisms.

## 14. Decision

**ISSUE #19 SUBSTANTIVE DECISION: PASS WITH QUALIFICATION.**

Working Z is locked as **Student Social-Emotional Competence (SEC) / Kompetensi Sosial-Emosional Siswa**, operationalized primarily as five correlated first-order competence domains. The Zhou & Ee SECQ is the primary measurement candidate, with cross-language adolescent evidence supporting its five-factor structure. A higher-order general SEC factor remains optional and must be justified through target-sample model comparison. SEC remains a candidate mediator because the SEC→engagement link is well-supported and school-support→SEC is plausible, but the DPM→full-SEC path is still weak/construct-adjacent. Therefore SEC must be treated as a mechanism to test against rivals, not an established causal mediator.