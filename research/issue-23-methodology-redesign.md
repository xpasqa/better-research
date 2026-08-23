# Issue #23 — Methodology Redesign: Identification, Longitudinal Structure, Sampling, Power, and Estimator

## 0. Decision rule

Metode dipilih setelah research question, theory, construct, dan identification problem dikunci. Karena kontribusi yang masih defensible setelah Issue #22 adalah **mechanism discrimination**, **temporal ordering**, dan kemungkinan **cross-context configuration**, desain cross-sectional satu-wave tidak memadai sebagai primary design. SEM/PLS-SEM tidak dipilih sebagai tujuan; estimator mengikuti measurement level, nesting, missingness, dan target estimand.

## 1. Inferential target

### Primary target

Mengestimasi **prospective/temporally ordered associations** antara:

- strategy-specific Adolescent-Perceived Digital Parental Mediation (DPM);
- Perceived Teacher Support (PTS);
- Student Social-Emotional Competence (SEC);
- Basic Psychological Need Satisfaction at School (BPNS) sebagai theory-derived competing mechanism untuk school-support pathway; dan
- Student Engagement in Learning.

Analisis membandingkan apakah family-digital dan school-support contexts menunjukkan pattern indirect association yang sama atau berbeda melalui SEC versus BPNS, sambil mengendalikan prior levels dari mediator/outcome yang relevan.

### What this design does not identify

Desain observasional panel tidak dengan sendirinya mengidentifikasi causal effects. Residual time-varying confounding, selection, measurement error, unmeasured family/classroom factors, dan model misspecification tetap mungkin. Karena cross-sectional mediation dapat menghasilkan estimasi longitudinal yang sangat bias [@maxwellcole2007mediation], istilah primary manuscript adalah **prospective association**, **temporally ordered indirect association**, atau **statistical indirect pathway**, bukan `causal mediation`.

## 2. Primary design choice

### Decision: three-wave prospective panel

**Primary design = three-wave panel siswa SMP di DKI Jakarta**, dengan interval yang mengikuti kalender sekolah dan cukup untuk memungkinkan perubahan substantif tanpa mengklaim satu time-lag universal. Exact interval harus ditetapkan sebelum preregistration berdasarkan kalender sekolah, feasibility, dan theoretical timescale; tidak boleh dipilih setelah melihat hasil.

Minimum measurement schedule:

| Construct | T1 | T2 | T3 | Purpose |
|---|---:|---:|---:|---|
| DPM strategies | ✓ | ✓ | optional/full if burden allows | exposure stability/change; reverse-child sensitivity |
| PTS | ✓ | ✓ | optional/full if burden allows | school-support stability/change |
| SEC | ✓ | ✓ | ✓ | candidate mechanism + reciprocal ordering |
| BPNS at school | ✓ | ✓ | ✓ | SDT competing mechanism + reciprocal ordering |
| Engagement | ✓ | ✓ | ✓ | baseline control, change, reciprocal ordering |
| time-stable covariates | ✓ | — | — | design/DAG adjustment |
| time-varying key covariates | ✓ | ✓ | ✓ when justified | sensitivity to changing context |

Repetition of mediator and outcome is **non-negotiable**. A simple `X at T1 → M at T2 → Y at T3` sequence with no baseline/repeated M/Y is not treated as sufficient evidence of longitudinal mediation because temporal separation alone does not solve autoregressive and stable-difference bias [@maxwellcole2007mediation].

### Why not one wave

One-wave mediation cannot separate temporal ordering and can create misleading indirect paths even if the true longitudinal process differs. Therefore one-wave SEM is **REJECTED as primary design**.

### Why not two waves

Two waves can improve temporal information but remain weak for a process that explicitly compares mediator–outcome directionality and baseline change. Two waves may be used only as a contingency design if a third wave becomes institutionally impossible, with a clear downgrade in contribution claim.

## 3. Longitudinal identification strategy

### 3.1 Baseline adjustment

Primary prospective models include baseline levels of SEC/BPNS and engagement. This reduces—but does not eliminate—confounding by prior functioning and helps distinguish level differences from subsequent change.

### 3.2 Reciprocal/within-person sensitivity

Because support, SEC, and engagement can be reciprocal, the analysis cannot rely mechanically on the traditional Cross-Lagged Panel Model. Hamaker et al. show that the conventional CLPM can conflate stable between-person differences with within-person dynamics, producing misleading cross-lagged parameters when trait-like stability exists [@hamaker2015clpm].

Decision tree:

1. fit longitudinal measurement models and inspect stability/variance decomposition;
2. use autoregressive panel models for the preregistered prospective estimands;
3. where three-wave data, convergence, and sample/cluster structure permit, conduct **RI-CLPM or equivalent within-between decomposition as sensitivity analysis** for reciprocal SEC/BPNS ↔ engagement relations;
4. do not call a cross-lagged coefficient causal merely because it is lagged.

### 3.3 Mechanism discrimination

The confirmatory comparison is deliberately limited:

- **Model M1 — SEC pathway:** T1 contextual predictors → T2 SEC → T3 engagement, adjusting baseline SEC and engagement.
- **Model M2 — SDT/BPNS pathway:** T1 PTS → T2 BPNS → T3 engagement, adjusting baseline BPNS and engagement.
- **Model M3 — joint competing-mechanism model:** SEC and BPNS entered jointly to test whether each retains incremental explanatory association; DPM is not forced through BPNS unless theory/evidence supports it.
- **Model M4 — reciprocal sensitivity:** alternative ordering engagement → later SEC/BPNS, plus reciprocal support paths where identifiable.

Self-efficacy/SRL remain theoretically important rivals but are **not added as further primary mediators** to avoid a kitchen-sink model. They may be collected only if a separate preregistered secondary aim and adequate burden/power justify it.

### 3.4 Cross-context interaction

Enabling DPM × PTS is a **secondary confirmatory target** only if Monte Carlo power shows adequate precision for the interaction. Competing predictions:

- reinforcement: high enabling DPM and high PTS are mutually strengthening;
- compensation: one context is more strongly associated with engagement when the other is weak.

If powered inadequately, the interaction is dropped rather than reported as an underpowered novelty test.

## 4. Construct operationalization

### 4.1 X1 — Adolescent-Perceived DPM

Primary content candidate remains Symons et al.; empirical strategy dimensions are not collapsed into one universal `good parenting` score. Enabling/active/interpretative practices receive the strongest confirmatory focus; restrictive and observant strategies remain distinct and their directions are not forced.

Parent report is strongly recommended for corroboration on a full or prespecified subsample. Parent–adolescent discrepancy is treated as substantive measurement information, not administrative error.

### 4.2 X2 — Perceived Teacher Support

Primary candidate = Wu et al. PTSS with instrumental, emotional, informational, and appraisal support. Student report is appropriate because the construct is perceived support, not objective teacher competence.

Class/teacher/school identifiers are retained so student perceptions can be decomposed or at minimum standard errors corrected for clustering.

### 4.3 Z1 — SEC

Primary candidate = Zhou & Ee SECQ, with five-domain architecture tested rather than assuming one global factor. Indonesian language/content adaptation must not alter domain meaning without psychometric evidence.

### 4.4 Z2 — BPNS at school: required competing mechanism

To make mechanism discrimination real rather than rhetorical, the design adds **Basic Psychological Need Satisfaction at School** as a measured comparator grounded in SDT. Tian et al. developed the Adolescent Students' Basic Psychological Needs at School Scale (ASBPNSS) and reported psychometric evidence across multiple adolescent samples for autonomy, competence, and relatedness at school [@tian2014bpns]. This is the primary content candidate, not an automatically validated Indonesian instrument.

BPNS is distinct from SEC: BPNS measures satisfaction of motivational needs in the school context; SEC measures student social-emotional capacities.

### 4.5 Y — Student Engagement in Learning

Engagement remains multidimensional. Indonesian SEQ adaptation is a local candidate, with Lam et al. as broader cross-national measurement anchor. Exact final instrument is selected after content/translation/readability audit and pilot CFA; engagement cannot be reduced to attendance or grades.

## 5. Instrument adaptation and measurement validation

Before main fielding:

1. verify licensing/permission and exact item wording for every candidate instrument;
2. forward translation + independent reconciliation + back-translation where needed;
3. expert content review focused on construct equivalence, not stylistic preference;
4. cognitive interviews with SMP students for comprehension, reference period, and response process;
5. pilot administration in a population resembling the main sample;
6. item distribution and missingness audit;
7. CFA/ESEM model comparison where construct evidence warrants it;
8. reliability with omega/appropriate latent reliability, not alpha alone;
9. convergent/discriminant validity among DPM, PTS, SEC, BPNS, and engagement;
10. longitudinal measurement invariance for repeatedly measured SEC, BPNS, and engagement before interpreting latent change/cross-lagged paths.

A factor structure validated abroad is **not assumed invariant in SMP DKI**.

## 6. Sampling design

### 6.1 Target population

Students enrolled in SMP/equivalent schools within the prespecified DKI sampling frame. Any exclusion of an administrative area, school type, special school, or student subgroup must be documented before sampling and reflected in the target-population statement.

### 6.2 Recommended design

**Multistage probability-oriented cluster sampling**, subject to availability of an official sampling frame:

1. stratify schools by administrative area and school status (public/private); additional stratification only if substantively justified and frame information is reliable;
2. randomly select schools within strata;
3. randomly select classes/grade groups within schools;
4. invite all eligible students in selected classes or use a prespecified random selection rule;
5. retain sampling probabilities/weights where unequal probabilities are introduced.

Convenience recruitment through schools that volunteer first is **not** the preferred final design because it weakens population inference and may select on school resources/leadership.

### 6.3 Cluster structure

Students are nested in classes/teachers and schools. Therefore:

- calculate ICCs for key outcomes/constructs;
- report number of clusters and cluster-size distribution;
- use multilevel SEM when the between-cluster estimands are substantively targeted and cluster counts support reliable estimation;
- otherwise use design-based/cluster-robust standard errors and sampling weights where appropriate;
- never treat thousands of students from very few schools as an equivalent simple random sample of thousands of independent observations.

## 7. Sample-size and power plan

No fixed `N=200`, `N=300`, or `10-times rule` is accepted.

Sample size is determined **after pilot/measurement specification** using Monte Carlo simulation for the actual longitudinal model. Mediation power depends on path sizes, reliability, number of indicators, missingness, and model complexity; simulation-based planning is specifically recommended for complex mediation [@schoemann2017power].

Simulation inputs must include:

- smallest effect of substantive interest, not only optimistic published effects;
- factor loadings/reliability from pilot or conservative literature values;
- autoregressive stability;
- number of clusters and realistic ICC;
- unequal cluster sizes if expected;
- wave-specific attrition and item missingness;
- indirect effects for SEC and BPNS models;
- DPM × PTS interaction only if it remains a target;
- convergence, bias, standard-error bias, confidence-interval coverage, and power/precision criteria.

The recruitment target must inflate the required final analytic sample for expected attrition across waves and any design effect. The final N is therefore a **pre-fielding decision after pilot**, not an arbitrary number inserted now.

## 8. Estimator decision

### Default principle

**CB-SEM/latent-variable SEM is the current default family**, because the core constructs are theorized latent dimensions and the inferential goal is explanatory model comparison, not pure prediction. This is not a commitment to one software package or estimator.

### Ordered categorical measurement

Likert-type item data are treated according to number of categories and observed distributions. For clearly ordinal/non-normal item-level CFA, robust categorical estimators such as WLSMV are preferred. Robust maximum likelihood is considered for structural models when its assumptions and scale treatment are defensible.

### Multilevel/design correction

If ICC/cluster structure is material, use multilevel SEM or complex-survey/cluster-robust corrections. Estimator choice must preserve the actual sampling structure.

### PLS-SEM decision

**PLS-SEM is NOT the default.** It may only be reconsidered if final measurement includes genuinely composite/formative constructs and the primary objective shifts toward prediction, with an explicit rationale. `Small sample`, `non-normality`, or `more advanced` are not sufficient reasons.

## 9. Missing data and attrition

Complete-case analysis is not the default.

Required:

- document item-level and wave-level missingness;
- compare retained versus attrited participants on baseline variables;
- use FIML where compatible with estimator/model, or multiple imputation compatible with clustered/longitudinal structure;
- include predictors of missingness when defensible;
- sensitivity analysis for departures from missing-at-random assumptions when attrition is substantial;
- report attrition by school/class and wave.

## 10. DAG-informed covariate strategy

Controls are not selected by `include everything available`.

### Core baseline covariates to consider

- grade/age;
- sex/gender as measured and ethically appropriate;
- household SES / parental education;
- prior achievement if available and construct-compatible;
- baseline engagement;
- baseline SEC/BPNS for relevant prospective paths.

### Family-context confounders/rivals

- general parenting warmth/responsiveness/autonomy support/control;
- parental educational involvement;
- parental digital competence/own media use where theory indicates a backdoor path.

### School-context rivals

- teacher-student relationship;
- classroom climate/instructional quality;
- peer support;
- school resources.

These variables are **not automatically all adjusted**. Before preregistration, construct a causal/theoretical DAG for each primary estimand and identify a minimally sufficient adjustment set. Avoid adjusting for descendants of the exposure/mediator, colliders, or variables that redefine the estimand through overcontrol.

## 11. Common-method and informant strategy

Primary student reports are justified for perceived DPM, PTS, SEC, BPNS, and engagement, but a same-source battery creates common-method risk.

Mitigation hierarchy:

1. temporal separation across three waves;
2. parent corroboration for DPM where feasible;
3. school/class/teacher identifiers and multilevel structure;
4. administrative prior achievement/attendance as auxiliary or validity variables where access and ethics permit—not as replacements for engagement;
5. varied item order/clear reference periods without contaminating scale validity;
6. statistical common-method factor only as a sensitivity model, not a universal repair.

## 12. Ethics and adolescent data governance

Main fielding requires institutional ethics approval and school permissions. Minimum safeguards:

- parent/guardian consent and adolescent assent according to applicable ethics requirements;
- voluntary participation with no academic penalty;
- teachers do not see individual student answers;
- collect no passwords, private messages, browsing histories, account credentials, or device contents;
- data minimization and separation of identifiers from survey data;
- restricted access and encrypted storage consistent with institutional policy;
- clear procedure for withdrawal and handling distress/safeguarding disclosures;
- recruitment wording that avoids school/teacher coercion.

## 13. Preregistration and reproducibility

Before main data collection, preregister:

- primary RQs/hypotheses;
- sampling frame and selection procedure;
- wave timing;
- primary/secondary construct dimensions;
- measurement-model decision rules;
- primary adjustment sets/DAGs;
- primary longitudinal models and competing models;
- treatment of missing data/attrition;
- estimator decision rules;
- smallest effect of substantive interest and Monte Carlo power results;
- multiplicity/secondary analysis policy.

Analysis code, data dictionary, and de-identified/synthetic reproducibility materials should be versioned where ethics/data agreements allow.

## 14. Revised primary RQs for integration

The old seven-path RQ structure is no longer optimal because it assumes a single SEC mediation chain. For Issue #24, use the following working architecture:

1. **RQ1:** Bagaimana masing-masing strategi DPM pada baseline berhubungan secara prospektif dengan Student Engagement in Learning pada siswa SMP di DKI Jakarta setelah memperhitungkan engagement sebelumnya?
2. **RQ2:** Bagaimana PTS pada baseline berhubungan secara prospektif dengan Student Engagement in Learning setelah memperhitungkan engagement sebelumnya?
3. **RQ3:** Bagaimana DPM dan PTS berhubungan dengan perubahan berikutnya pada SEC dan BPNS at school?
4. **RQ4:** Bagaimana SEC dan BPNS berhubungan secara prospektif dengan engagement berikutnya setelah memperhitungkan level sebelumnya?
5. **RQ5:** Apakah temporally ordered indirect associations dari family-digital dan school-support contexts menuju engagement lebih konsisten dengan SEC pathway, BPNS pathway, atau keduanya ketika competing mechanisms diestimasi bersama?
6. **RQ6 (secondary; power-gated):** Apakah hubungan enabling DPM dan PTS dengan engagement lebih konsisten dengan pola cross-context reinforcement atau compensation?

RQ5 adalah mechanism-discrimination question; ia tidak mengasumsikan sebelumnya bahwa SEC pasti mediator. RQ6 hanya masuk confirmatory model bila power simulation memadai.

## 15. Hypothesis status

### Directional hypotheses sufficiently supported

- **H1:** PTS yang lebih tinggi berkaitan secara prospektif dengan engagement yang lebih tinggi, dengan qualification bahwa effect heterogeneity dan reverse paths tetap diuji.
- **H2:** PTS yang lebih tinggi berkaitan dengan BPNS at school yang lebih tinggi.
- **H3:** BPNS at school yang lebih tinggi berkaitan secara prospektif dengan engagement yang lebih tinggi.
- **H4:** SEC yang lebih tinggi berkaitan secara prospektif dengan engagement yang lebih tinggi, tetapi reciprocal ordering tetap dibandingkan.
- **H5:** Enabling/interpretative DPM berkaitan positif dengan selected SEC/regulatory capacities; ini lebih lemah daripada H1–H4 dan harus dilabeli lower-confidence.

### Non-directional / competing hypotheses

- restrictive dan observant DPM tidak diberi universal positive/negative sign;
- SEC versus BPNS indirect association adalah competing-mechanism test, bukan directional certainty;
- reinforcement versus compensation adalah competing prediction, bukan hypothesis dengan sign yang dipaksakan.

## 16. GO/NO-GO gate after Issue #23

### GO

- theoretical/construct architecture cukup jelas untuk menyusun Bab 1–3 final working proposal;
- three-wave longitudinal panel dipilih;
- sampling hierarchy dan clustering treatment jelas;
- competing mechanism BPNS ditambahkan dengan instrument candidate;
- estimator decision rules jelas;
- power strategy tidak memakai rule-of-thumb.

### NO-GO for main data collection until

1. exact instruments/licensing/item sets locked;
2. Indonesian adaptation + cognitive interview completed;
3. pilot measurement models completed;
4. longitudinal/sampling assumptions translated into Monte Carlo power simulation;
5. minimum cluster/sample recruitment target finalized;
6. school sampling frame and permissions available;
7. ethics approval secured;
8. preregistration/analysis plan frozen.

## 17. Decision

**ISSUE #23 DECISION: PASS FOR DESIGN ARCHITECTURE; MAIN FIELDING REMAINS CONDITIONAL NO-GO.**

The study is redesigned from a one-wave SEM mediation study into a **three-wave, multistage clustered prospective panel with explicit competing mechanisms and reciprocal sensitivity analyses**. CB-SEM/longitudinal latent modeling is the default analytic family, with multilevel or cluster-robust treatment as dictated by ICC/cluster structure. PLS-SEM is not the default. Sample size must be produced by model-based Monte Carlo simulation after pilot measurement evidence, not by a generic rule. This architecture is sufficiently specified for Issue #24 manuscript integration while preserving a hard pre-fielding measurement/power/ethics gate.