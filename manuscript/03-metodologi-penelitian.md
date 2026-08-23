# BAB 3 — METODOLOGI PENELITIAN

## 3.1 Desain Penelitian

Penelitian menggunakan pendekatan kuantitatif observasional dengan **three-wave prospective panel design**. Pemilihan desain longitudinal didasarkan pada tujuan penelitian untuk membedakan prospective associations, temporally ordered indirect associations, competing mechanisms, dan reciprocal relations. Cross-sectional one-wave mediation tidak digunakan sebagai primary design karena estimasi cross-sectional dapat memberikan gambaran yang bias terhadap proses mediasi longitudinal (Maxwell & Cole, 2007).

Desain tiga gelombang dipilih agar mediator/candidate mechanisms dan outcome dapat diukur berulang, sehingga analisis dapat memperhitungkan baseline level, autoregressive stability, dan competing temporal ordering. Walaupun temporal separation memperkuat inferential structure dibanding survei satu waktu, penelitian tetap observasional. Karena itu, hasil tidak akan ditafsirkan sebagai causal effects tanpa identification assumptions yang tidak tersedia dalam desain ini.

### 3.1.1 Target estimand

Target utama adalah prospective association antara contextual predictors—Digital Parental Mediation (DPM) dan Perceived Teacher Support (PTS)—dengan Student Engagement in Learning, serta temporally ordered indirect statistical associations melalui dua competing mechanisms:

1. Student Social-Emotional Competence (SEC); dan
2. Basic Psychological Need Satisfaction at School (BPNS).

Target tambahan adalah reciprocal relation SEC/BPNS ↔ engagement dan, apabila adequately powered, cross-context interaction enabling DPM × PTS.

### 3.1.2 Jadwal pengukuran

Minimum measurement schedule ditetapkan sebagai berikut:

| Konstruk | T1 | T2 | T3 | Fungsi utama |
|---|---:|---:|---:|---|
| DPM strategies | ✓ | ✓ | optional/full bila burden memungkinkan | exposure stability/change dan reverse-child sensitivity |
| PTS | ✓ | ✓ | optional/full bila burden memungkinkan | school-support stability/change |
| SEC | ✓ | ✓ | ✓ | candidate mechanism dan reciprocal ordering |
| BPNS at school | ✓ | ✓ | ✓ | SDT competing mechanism dan reciprocal ordering |
| Student Engagement | ✓ | ✓ | ✓ | baseline control, prospective change, reciprocal ordering |
| Time-stable covariates | ✓ | — | — | adjustment berdasarkan DAG |
| Key time-varying covariates | ✓ | ✓ | ✓ bila justified | sensitivity terhadap perubahan konteks |

Exact interval antar-gelombang akan dikunci sebelum preregistration dengan mempertimbangkan kalender sekolah, burden sekolah/siswa, dan theoretical timescale. Interval tidak akan dipilih setelah melihat hasil statistik.

## 3.2 Objek dan Konteks Penelitian

Objek substantif penelitian adalah konfigurasi hubungan antara family-digital context, school-support context, student capacities/needs, dan engagement pada siswa SMP/equivalent di DKI Jakarta. DKI diperlakukan sebagai empirical setting, bukan sebagai theoretical boundary atau novelty.

Data resmi BPS Provinsi DKI Jakarta digunakan untuk mendeskripsikan setting pendidikan dan mendukung penyusunan sampling frame sejauh sesuai dengan unit administratif dan sekolah yang tersedia (Badan Pusat Statistik Provinsi DKI Jakarta, 2025). Data agregat wilayah tidak digunakan sebagai proxy engagement, SEC, BPNS, DPM, atau PTS pada level individu.

Target population harus ditulis berdasarkan sampling frame aktual sebelum main fielding. Setiap exclusion—misalnya wilayah administratif tertentu, school type, special school, atau subgroup siswa—harus ditetapkan sebelum sampling dan tercermin pada batas generalisasi.

## 3.3 Unit Analisis dan Struktur Data

Unit analisis substantif adalah **individu siswa**. Namun, siswa tidak diasumsikan independent secara statistik. Mereka berada dalam kelas, berinteraksi dengan guru, dan berada dalam sekolah. PTS secara khusus berpotensi mengandung shared teacher/classroom variance selain individual perception.

Karena itu, dataset harus mempertahankan identifier pseudonymous untuk:

- siswa;
- kelas;
- guru yang menjadi referent PTS, apabila definisi item/instrumen menggunakan specific teacher referent;
- sekolah; dan
- wave pengukuran.

Intraclass correlations (ICC) untuk construct scores/latent outcomes utama harus diperiksa sebelum final structural estimation. Bila between-class/teacher/school effects merupakan target substantif dan jumlah cluster memadai, multilevel SEM dipertimbangkan. Bila tujuan tetap pada individual-level prospective associations dan cluster counts tidak mendukung reliable multilevel latent estimation, design-based/cluster-robust standard errors digunakan sesuai struktur sampling. Jumlah siswa yang besar dari sedikit sekolah tidak diperlakukan setara dengan simple random sample berukuran sama.

## 3.4 Data dan Sumber Data

### 3.4.1 Data primer siswa

Data primer utama berasal dari repeated student questionnaires yang mengukur DPM, PTS, SEC, BPNS, engagement, serta covariates yang disetujui dalam preregistered DAG/analysis plan. Student report dipilih karena X1 dan X2 secara operasional merupakan perceived exposures dan karena SEC, BPNS, serta engagement mencakup subjective experiences yang relevan pada level siswa.

### 3.4.2 Parent corroboration

Parent report untuk DPM sangat direkomendasikan pada full sample atau prespecified subsample bila feasible. Parent report bukan pengganti student report, melainkan corroborative source untuk mengevaluasi informant discrepancy dan common-method dependence. Ulfa et al. (2025) memberikan local parent-report adaptation anchor, sedangkan Symons et al. (2017) menunjukkan reports antar-informan dapat berbeda walaupun factor structure serupa.

### 3.4.3 Data administratif/sekunder

Bila diperoleh secara etis dan legal, prior achievement dan attendance dapat digunakan sebagai auxiliary validity/covariate variables. Variabel tersebut tidak menggantikan engagement. Data sekolah/administratif juga dapat membantu stratification, weighting, nonresponse analysis, dan deskripsi sampling frame.

Tidak dikumpulkan password, private messages, browsing histories, account credentials, atau isi perangkat digital siswa/orang tua.

## 3.5 Populasi dan Teknik Sampling

### 3.5.1 Sampling frame

Main fielding mensyaratkan official atau otherwise verifiable school sampling frame yang mencakup target population yang dinyatakan. Sampling frame harus memuat setidaknya informasi yang memungkinkan school selection dan stratification yang telah ditetapkan.

### 3.5.2 Multistage probability-oriented cluster sampling

Recommended sampling procedure adalah:

1. **Stratification sekolah.** Minimal berdasarkan wilayah administratif dan status sekolah negeri/swasta. Stratification tambahan hanya digunakan bila substantively justified dan informasi frame reliable.
2. **School selection.** Sekolah dipilih secara acak di dalam strata berdasarkan probability rule yang terdokumentasi.
3. **Class/grade selection.** Kelas atau grade groups dipilih secara acak di sekolah terpilih.
4. **Student selection.** Seluruh siswa eligible pada kelas terpilih diundang atau digunakan prespecified random selection rule apabila census kelas tidak feasible.
5. **Sampling probabilities.** Unequal selection probabilities dicatat agar weights dapat dihitung dan digunakan bila diperlukan.

Convenience recruitment hanya dari sekolah yang bersedia paling awal tidak diperlakukan sebagai preferred design karena dapat memilih sekolah berdasarkan resources, leadership, atau research receptivity.

### 3.5.3 Attrition dan panel retention

Karena desain tiga gelombang, retention strategy harus dirancang sebelum T1. Prosedur follow-up harus menjaga voluntariness dan privacy. Attrition dilaporkan pada level siswa, kelas, dan sekolah serta dibandingkan berdasarkan baseline constructs/covariates sejauh etis dan tersedia.

## 3.6 Operasionalisasi Konstruk dan Instrumen

### 3.6.1 Adolescent-Perceived Digital Parental Mediation

DPM diperlakukan sebagai **multidimensional family of strategy constructs**, bukan unidimensional reflective score. Working theory-level dimensions adalah enabling, restrictive, dan observant mediation. Symons et al. (2017) menjadi primary adolescent-age content/structure candidate; Kuldas et al. (2021), Ho et al. (2019), Purboningsih et al. (2025), dan Ulfa et al. (2025) digunakan untuk construct/content audit dan adaptation.

Exact item battery belum dikunci sebelum licensing/content review. Final dimensionality mengikuti pilot CFA/ESEM/model comparison dan tidak dipaksa mengikuti tiga-factor architecture apabila item evidence mendukung structure lain.

### 3.6.2 Perceived Teacher Support

PTS menggunakan Wu et al. (2024) sebagai primary candidate karena skala tersebut dikembangkan pada siswa grade 7–10 dan membedakan:

- instrumental support;
- emotional support;
- informational support; dan
- appraisal support.

Item referent harus konsisten. Bila siswa menilai satu specific teacher, teacher ID harus dicatat. Bila skala meminta general teachers, interpretation pada level dyadic/classroom harus disesuaikan dan tidak boleh disebut objective teacher competence.

### 3.6.3 Student Social-Emotional Competence

SEC menggunakan Zhou dan Ee (2012) SECQ sebagai primary candidate dengan five-domain structure. Default measurement hypothesis adalah five correlated first-order factors, berdasarkan original development dan adolescent cross-language evidence (Jabeen & Maqsood, 2023). Alternative higher-order/re-specified structures diuji karena external validation menunjukkan factor structure tidak selalu identical di semua populations (Portela-Pino et al., 2024).

SEC diukur T1–T3. Longitudinal invariance harus dievaluasi sebelum latent mean/change atau cross-lagged interpretation.

### 3.6.4 Basic Psychological Need Satisfaction at School

BPNS menggunakan Adolescent Students’ Basic Psychological Needs at School Scale sebagai primary candidate (Tian et al., 2014). Konstruk mencakup autonomy, competence, dan relatedness satisfaction dalam konteks sekolah dan diukur T1–T3.

BPNS tidak digabung dengan SEC. Discriminant validity antara BPNS, SEC, PTS, dan engagement wajib diuji sebelum structural model.

### 3.6.5 Student Engagement in Learning

Engagement diukur sebagai multidimensional student outcome. Lam et al. (2014) menjadi broader measurement anchor, sedangkan Diniyah et al. (2025) menjadi Indonesian secondary-school candidate. Exact instrument selection mengikuti content alignment terhadap final definition, licensing, readability, dan pilot measurement results.

Engagement bukan nilai akademik, attendance, motivation, atau school adjustment. Construct overlap diperiksa melalui discriminant validity, bukan diselesaikan dengan menggabungkan indikator yang berbeda secara konseptual.

## 3.7 Adaptasi Instrumen dan Pilot Study

Tidak ada foreign scale yang diasumsikan otomatis valid di SMP DKI. Pre-fielding measurement protocol mencakup:

1. verifikasi permission/licensing dan exact item wording;
2. forward translation oleh translator yang memahami konteks psikometri/pendidikan;
3. independent reconciliation;
4. back-translation bila diperlukan oleh licensing/adaptation protocol;
5. expert content review untuk semantic, conceptual, dan developmental equivalence;
6. cognitive interviews dengan siswa SMP untuk comprehension, response process, recall/reference period, dan ambiguous wording;
7. pilot administration pada population yang menyerupai main target;
8. item distribution, floor/ceiling, missingness, dan response-pattern audit;
9. CFA/ESEM/model comparison sesuai construct evidence;
10. reliability menggunakan omega/latent reliability yang sesuai, bukan alpha sebagai satu-satunya indikator;
11. convergent/discriminant validity;
12. revision decision yang terdokumentasi sebelum main study.

Pilot sample tidak digabung otomatis ke main analytic sample apabila instrument revision dilakukan setelah pilot.

## 3.8 Penentuan Ukuran Sampel dan Power

Tidak digunakan aturan `N = 200`, `N = 300`, `10-times rule`, atau fixed respondent-per-item rule sebagai dasar utama.

Final recruitment target ditentukan **setelah pilot** melalui tailored Monte Carlo simulation untuk longitudinal clustered model. Simulation-based planning relevan karena power indirect effects bergantung pada magnitudes tiap path dan model complexity, bukan hanya total sample size (Schoemann et al., 2017).

Simulation input minimal mencakup:

- smallest effect of substantive interest;
- factor loadings dan reliability dari pilot atau conservative literature values;
- autoregressive stability SEC, BPNS, dan engagement;
- realistic ICC dan jumlah cluster;
- unequal cluster sizes;
- wave-specific attrition dan item missingness;
- indirect effects pada SEC dan BPNS models;
- DPM × PTS interaction bila tetap menjadi confirmatory target;
- convergence rate;
- parameter bias dan standard-error bias;
- confidence-interval coverage; dan
- target power/precision yang dipra-spesifikasi.

Recruitment target T1 harus menginflasi kebutuhan analytic T3 untuk expected attrition dan design effect. Karena input tersebut belum tersedia sebelum pilot, proposal tidak mencantumkan angka final N yang dibuat secara arbitrer.

## 3.9 Teknik Pengumpulan Data

### 3.9.1 Pra-pengumpulan

Sebelum T1:

- sampling frame dan selection rule dibekukan;
- ethics approval dan school permissions diperoleh;
- instrument permissions, adaptation, cognitive interviews, dan pilot selesai;
- Monte Carlo power analysis selesai;
- preregistration primary/secondary analyses selesai;
- survey administration SOP dan data-security plan diuji.

### 3.9.2 Administrasi survei

Survei dilakukan dalam kondisi yang meminimalkan coercion dan social desirability dari guru/orang tua. Guru tidak melihat individual responses. Instruksi menyatakan bahwa jawaban tidak memengaruhi nilai, disciplinary evaluation, atau hubungan sekolah.

Participant linkage antar-gelombang menggunakan pseudonymous code system yang dipisahkan dari analytical responses. File linkage disimpan dengan akses terbatas.

### 3.9.3 Reference period

Reference period item harus konsisten dengan construct dan wave interval. Apabila instrument original menggunakan wording tertentu, perubahan reference period hanya dilakukan bila secara substantif dan licensing memungkinkan serta dicatat sebagai adaptation yang perlu diuji.

## 3.10 Teknik Analisis Data

### 3.10.1 Data quality dan descriptive analysis

Analisis awal mencakup:

- response rate per sampling stage dan wave;
- sample composition serta weighted/unweighted characteristics bila weights tersedia;
- item distributions;
- missingness;
- attrition patterns;
- cluster-size distribution dan ICC;
- bivariate correlations sebagai descriptive evidence, bukan causal evidence.

### 3.10.2 Measurement model

Measurement analysis dilakukan sebelum structural model. Untuk setiap construct:

1. test theoretically plausible factor structures;
2. evaluate global/local fit dan factor loadings;
3. examine reliability;
4. test convergent/discriminant validity;
5. evaluate longitudinal measurement invariance untuk repeated constructs SEC, BPNS, dan engagement;
6. evaluate relevant group invariance hanya jika substantively needed dan adequately powered.

Higher-order factors hanya digunakan apabila lower-order relations dan model comparison mendukung interpretasinya. Fit statistics tidak menggantikan construct interpretation.

### 3.10.3 Primary prospective models

Primary analysis membandingkan:

**M1 — SEC pathway**

T1 DPM strategies dan PTS → T2 SEC → T3 engagement, dengan SEC_T1 dan engagement_T1 diperhitungkan. Direct prospective paths juga diestimasi sesuai preregistration.

**M2 — BPNS pathway**

T1 PTS → T2 BPNS → T3 engagement, dengan BPNS_T1 dan engagement_T1 diperhitungkan. DPM tidak dipaksa melalui BPNS tanpa theory-derived reason.

**M3 — Joint competing-mechanism model**

SEC dan BPNS dimasukkan bersama untuk menilai apakah masing-masing mempertahankan incremental association. Model comparison memperhatikan fit, parameter stability, confidence intervals, dan substantive effect sizes, bukan hanya p-values.

**M4 — Reciprocal sensitivity model**

Alternative paths engagement → later SEC/BPNS dan, bila identifiable, reciprocal support processes diperiksa. Traditional CLPM tidak diperlakukan sebagai within-person causal model. Karena CLPM dapat mencampur stable between-person differences dan within-person dynamics (Hamaker et al., 2015), RI-CLPM atau equivalent within-between decomposition digunakan sebagai sensitivity analysis apabila wave structure, sample size, convergence, dan measurement support memadai.

### 3.10.4 Indirect associations

Indirect effects dilaporkan sebagai **temporally ordered statistical indirect associations** dengan confidence intervals. Cross-sectional causal-mediation language dilarang. Maxwell dan Cole (2007) menjadi methodological basis untuk membatasi interpretasi.

### 3.10.5 Secondary interaction model

Enabling DPM × PTS diuji hanya bila Monte Carlo simulation menunjukkan adequate power/precision. Interaction diinterpretasikan melalui predicted values/marginal effects, bukan coefficient sign saja. Reinforcement dan compensation dibandingkan sebagai competing predictions.

### 3.10.6 Estimator decision

Current default analytical family adalah **latent-variable covariance-based SEM**, karena constructs bersifat laten dan tujuan utama explanatory model comparison.

Estimator dipilih berdasarkan measurement scale dan distribution:

- clearly ordinal/non-normal item-level CFA: robust categorical estimator seperti WLSMV dipertimbangkan;
- continuous/approximately continuous latent structural models: robust maximum-likelihood family dipertimbangkan bila assumptions defensible;
- clustered sampling: multilevel estimator atau complex/cluster-robust correction sesuai number of clusters dan estimand;
- sampling weights dimasukkan bila unequal probabilities/nonresponse adjustment menghasilkan weights yang relevan.

**PLS-SEM bukan default.** Ia hanya dapat dipertimbangkan ulang apabila final measurement benar-benar composite/formative dan primary aim berubah menjadi prediction. Small sample atau nonnormal data bukan rationale yang cukup.

### 3.10.7 Missing data

Complete-case analysis tidak menjadi default. Missingness ditangani melalui:

- description item/wave missingness;
- baseline comparison retained versus attrited participants;
- FIML bila compatible dengan estimator/model; atau
- multiple imputation yang compatible dengan longitudinal/cluster structure.

Predictors of missingness dapat dimasukkan bila substantively defensible. Jika attrition substantial, sensitivity analysis terhadap departures from missing-at-random assumptions dipertimbangkan dan limitation dinyatakan.

### 3.10.8 Covariate selection dan DAG

Covariates tidak dipilih karena tersedia atau karena bivariate significance. Untuk setiap primary estimand dibuat theoretical/causal DAG dan ditentukan minimally sufficient adjustment set.

Candidate baseline variables mencakup grade/age, sex/gender bila relevan dan ethically measured, SES/parental education, prior achievement, prior engagement, serta baseline SEC/BPNS. Rival family variables dapat mencakup general parenting, educational involvement, dan parental media-use/digital competence. Rival school variables dapat mencakup teacher-student relationship, classroom/instructional quality, peer support, dan school resources.

Tidak semua candidate controls dimasukkan sekaligus. Descendants of exposures/mediators, colliders, dan variables yang menyebabkan overcontrol harus dihindari sesuai estimand.

### 3.10.9 Common-method sensitivity

Karena beberapa constructs menggunakan student report, common-method risk ditangani terutama melalui design:

- temporal separation;
- parent corroboration untuk DPM bila feasible;
- class/teacher/school identifiers;
- auxiliary administrative variables bila available dan ethical;
- reference periods dan survey administration yang jelas.

Common-method latent factor dapat diuji sebagai sensitivity model bila measurement structure mengizinkan, tetapi tidak diperlakukan sebagai universal statistical repair.

### 3.10.10 Robustness dan reporting

Reporting mencakup standardized dan unstandardized estimates yang relevan, confidence intervals, effect sizes, model fit, missing/attrition diagnostics, cluster information, sensitivity results, dan deviations from preregistration. Mixed/null results dilaporkan apa adanya.

Statistical significance tidak dianggap cukup untuk contribution claim. Substantive magnitude, precision, robustness, competing-model performance, dan consistency across dimensions menjadi bagian dari interpretation.

## 3.11 Validitas, Reliabilitas, dan Identification Limit

Construct validity diprioritaskan sebelum structural inference. Measurement validity meliputi content equivalence, factor structure, convergent/discriminant validity, reliability, dan longitudinal invariance.

Internal causal validity tetap terbatas karena desain observasional. Baseline adjustment, repeated measures, reciprocal analysis, DAG-based covariates, dan within-between sensitivity dapat mengurangi beberapa alternative explanations, tetapi tidak menjamin no unmeasured confounding. Karena itu, causal statements tidak dibuat.

External validity bergantung pada sampling frame, school participation, response rate, attrition, weighting, dan target-population definition. Probability-oriented sampling memperkuat population inference tetapi tidak memperbaiki causal identification secara otomatis.

## 3.12 Etika Penelitian dan Tata Kelola Data

Main study hanya dilaksanakan setelah institutional ethics approval dan izin sekolah diperoleh. Karena partisipan adalah remaja, prosedur mengikuti applicable requirements untuk parent/guardian consent dan adolescent assent.

Prinsip minimum:

- participation voluntary;
- tidak ada academic/disciplinary penalty untuk refusal/withdrawal;
- guru tidak mengakses individual answers;
- informasi sensitif diminimalkan;
- identifier dipisahkan dari survey response;
- storage dienkripsi/restricted sesuai institutional policy;
- data-sharing hanya dalam bentuk de-identified atau synthetic/reproducibility material yang diizinkan;
- tersedia procedure untuk withdrawal;
- safeguarding/distress disclosure ditangani melalui approved protocol;
- recruitment language menghindari coercion oleh sekolah/guru.

Penelitian tidak meminta password, account credentials, private messages, browsing histories, atau device contents.

## 3.13 Preregistration dan Reproducibility

Sebelum T1 main study, preregistration minimal memuat:

- primary RQs dan hypotheses;
- sampling frame dan selection procedure;
- wave timing;
- primary/secondary construct dimensions;
- measurement-model decision rules;
- DAG dan adjustment sets;
- M1–M4 model specifications;
- interaction status dan power gate;
- estimator decision rules;
- missing-data/attrition strategy;
- smallest effect of substantive interest;
- Monte Carlo power results;
- multiplicity/secondary-analysis policy.

Analysis scripts, data dictionary, codebook, dan reproducibility outputs disimpan dalam version control. Public sharing menyesuaikan ethics approval, consent, school agreements, dan data-protection requirements.

## 3.14 Pre-Fielding GO/NO-GO Gate

Arsitektur desain telah cukup jelas untuk proposal, tetapi **main data collection tetap NO-GO** sampai seluruh gate berikut selesai:

1. exact instruments dan licensing/permissions dikunci;
2. Indonesian adaptation dan cognitive interviews selesai;
3. pilot measurement models dan discriminant validity selesai;
4. preliminary longitudinal measurement plan diterjemahkan ke final item/wave battery;
5. tailored Monte Carlo power simulation menghasilkan target sample/cluster recruitment;
6. verified school sampling frame dan permissions tersedia;
7. institutional ethics approval diperoleh; dan
8. preregistration serta analysis plan dibekukan.

Dengan demikian, status metodologi adalah **GO untuk instrument adaptation, pilot, sampling preparation, ethics submission, dan preregistration preparation; NO-GO untuk main three-wave fielding sampai delapan gate tersebut dipenuhi**.