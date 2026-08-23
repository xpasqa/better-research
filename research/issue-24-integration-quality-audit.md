# Issue #24 — Final Bab 1–3 Integration and Quality Audit

## 0. Scope

Audit ini memeriksa integrasi keputusan Issues #16–#23 ke canonical manuscript:

- `manuscript/01-latar-belakang.md`
- `manuscript/02-tinjauan-pustaka.md`
- `manuscript/03-metodologi-penelitian.md`
- `manuscript/07-references.md`
- `literature/references.bib`
- `literature/matrix-literature-review.md`

Audit tidak menyatakan bahwa instrument adaptation/pilot atau main fielding sudah selesai. Tujuannya adalah menentukan apakah proposal architecture sudah coherent, evidence-traceable, dan methodologically defensible untuk masuk tahap pre-fielding.

## 1. Working title

**Hubungan Mediasi Digital Orang Tua dan Dukungan Guru dengan Keterlibatan Belajar Siswa SMP: Perbandingan Mekanisme Kompetensi Sosial-Emosional dan Kebutuhan Psikologis Dasar di DKI Jakarta**

### Title audit

- menggunakan `Hubungan`, bukan `Pengaruh`, sehingga tidak mengklaim causality;
- X1 dan X2 menggunakan final construct labels;
- Y menggunakan final outcome `Keterlibatan Belajar`;
- contribution candidate dinyatakan sebagai `Perbandingan Mekanisme`, bukan novelty absolut;
- DKI ditempatkan sebagai setting;
- title tidak menyebut SEM/PLS atau generic `Kesiapan Belajar`.

**Decision: PASS.**

## 2. Construct alignment

| Position | Old label | Final label | Status |
|---|---|---|---|
| X1 | Pengasuhan Digital | Adolescent-Perceived Digital Parental Mediation / Mediasi Digital Orang Tua yang Dipersepsikan Siswa | **LOCKED as multidimensional strategy family** |
| X2 | Kompetensi Guru | Perceived Teacher Support / Dukungan Guru yang Dipersepsikan Siswa | **LOCKED as student-perceived support** |
| M1 | Pembelajaran Sosial-Emosional | Student Social-Emotional Competence | **LOCKED as student attribute, not SEL process** |
| M2 | — | Basic Psychological Need Satisfaction at School | **ADDED as theory-derived competing mechanism** |
| Y | Kesiapan Belajar | Student Engagement in Learning / Keterlibatan Belajar | **LOCKED as multidimensional outcome** |

No unresolved ontological mismatch remains among the core labels. Exact item batteries and local factor structures remain pre-fielding measurement tasks, not conceptual blockers.

**Decision: PASS.**

## 3. Theory audit

### Contextual theory

Bioecological/neo-ecological theory now has a bounded role: contextual positioning, transactional logic, digital context recognition, and cross-context questions. Manuscript explicitly states that the three-wave panel is not a full PPCT test.

### Proximal mechanism theory

SDT is used specifically for PTS → BPNS → engagement. BPNS is measured rather than invoked decoratively.

### Developmental mechanism

SEC is explicitly separated from SDT and SEL process. It competes with BPNS rather than being privileged as the only mediator.

### Rival theories/mechanisms

Self-regulation, self-efficacy, teacher-student relationship, classroom/instructional quality, general parenting, peer support, prior achievement, and prior engagement are acknowledged. They are not all inserted mechanically as controls.

**Decision: PASS.**

## 4. Empirical problem and significance audit

The manuscript no longer claims an unmeasured DKI `engagement crisis`. Official BPS evidence is restricted to setting/sampling context. Engagement significance is justified through multidimensional measurement, developmental longitudinal evidence, and links with learning/achievement-related processes.

Indonesia-specific evidence is used as local measurement/context plausibility rather than as population prevalence. The manuscript explicitly states that construct-matched prevalence for low engagement among SMP DKI has not been verified.

**Decision: PASS.**

## 5. Research-gap and novelty audit

### Rejected claims

- no-study-combines-X1-X2-M-Y;
- DPM+SEC as a new combination;
- SEC-as-mediator novelty;
- PTS→engagement novelty;
- DKI-as-novelty;
- SEM/PLS-SEM as novelty;
- instrument adaptation alone as novelty.

### Candidate contribution retained

1. **Mechanism discrimination:** SEC versus BPNS in temporally ordered pathways.
2. **Cross-context configuration:** reinforcement versus compensation for enabling DPM and PTS, only if adequately powered.
3. **Temporal ordering:** prospective and reciprocal SEC/BPNS–engagement relations.
4. **Empirical contribution:** construct-valid, clustered, probability-oriented longitudinal evidence for SMP DKI.

Theoretical contribution remains candidate until observed results discriminate competing mechanisms. This is an appropriate level of uncertainty for a proposal.

**Decision: PASS.**

## 6. RQ–objective–theory alignment

Six RQs in Bab 1 map one-to-one to six objectives. RQ1–RQ4 ask prospective construct relations; RQ5 asks mechanism discrimination; RQ6 is explicitly secondary and power-gated.

Bab 2 hypotheses do not force directional claims where evidence is mixed:

- H1 PTS → prospective engagement;
- H2 PTS → BPNS;
- H3 BPNS → prospective engagement;
- H4 SEC → prospective engagement with reciprocal sensitivity;
- H5 enabling DPM → selected SEC/regulatory capacities, marked lower-confidence;
- restrictive/observant DPM remain non-directional;
- SEC vs BPNS and reinforcement vs compensation remain competing predictions.

**Decision: PASS.**

## 7. Identification and design audit

### Primary design

Three-wave prospective panel is aligned with the temporal/explanatory problem. Repeated SEC, BPNS, and engagement plus baseline adjustment address a major weakness of one-wave mediation.

### Causal limit

The manuscript consistently restricts inference to prospective/temporally ordered statistical associations. It acknowledges residual confounding, selection, time-varying omitted variables, and measurement error.

### Reciprocal processes

Traditional CLPM is not treated as causal. RI-CLPM/within-between decomposition is reserved for sensitivity analysis when measurement, sample size, and convergence support it.

### Clustering

Class/teacher/school identifiers, ICC, multilevel/cluster-robust decision rules, and sampling weights are explicitly specified.

**Decision: PASS for identification architecture.**

## 8. Sampling and power audit

Sampling is no longer a generic convenience survey plan. The manuscript specifies multistage probability-oriented cluster sampling conditional on a verified frame, with strata, random school/class selection, and unequal-probability tracking.

Sample size is deliberately **not fabricated**. Final recruitment N requires pilot-informed Monte Carlo simulation incorporating effect sizes, factor loadings/reliability, autoregression, ICC, clusters, attrition, missingness, indirect effects, and any interaction target.

This means the proposal has a defensible sample-size **procedure**, but does not yet have a justified final N.

**Decision: PASS for proposal architecture; conditional pre-fielding gate remains.**

## 9. Measurement audit

The manuscript specifies candidate instruments rather than pretending they are already locally validated:

- DPM: Symons et al. content/structure candidate plus Kuldas/Ho/Indonesian contextual sources;
- PTS: Wu et al. PTSS;
- SEC: Zhou & Ee SECQ;
- BPNS: Tian et al. ASBPNSS;
- Engagement: Lam et al. broader anchor plus Diniyah et al. Indonesian secondary-school candidate.

Adaptation protocol includes licensing, translation/reconciliation, cognitive interviews, pilot, CFA/ESEM where warranted, omega/latent reliability, discriminant validity, and longitudinal measurement invariance.

**Decision: PASS as pre-fielding measurement plan; instruments are not yet field-ready.**

## 10. Estimator audit

- latent-variable covariance-based SEM is the default family because the aim is explanatory model comparison;
- categorical/robust estimation follows item properties;
- multilevel/cluster-robust treatment follows design and ICC;
- PLS-SEM is explicitly not the default and cannot be justified merely by small sample or nonnormality.

**Decision: PASS.**

## 11. Missingness, common method, and covariate audit

- complete-case analysis is not default;
- FIML or appropriate multiple imputation is planned;
- attrition diagnostics are required;
- common-method risk is addressed through temporal separation, parent corroboration where feasible, identifiers, and auxiliary data;
- covariates follow DAG/minimally sufficient adjustment logic rather than statistical significance screening;
- overcontrol/collider risk is explicitly acknowledged.

**Decision: PASS.**

## 12. Ethics and reproducibility audit

Adolescent consent/assent, voluntariness, teacher non-access to individual responses, data minimization, pseudonymous linkage, restricted/encrypted storage, withdrawal, safeguarding, and anti-coercion rules are explicit. The study does not collect passwords, private messages, browsing histories, account credentials, or device contents.

Preregistration requires RQs/hypotheses, sampling, waves, measurement rules, DAG/adjustment sets, model specifications, missingness, estimators, power assumptions, and multiplicity policy. Analysis scripts/data dictionary are version-controlled subject to ethics/data agreements.

**Decision: PASS.**

## 13. Reference and citation audit

Reference database and APA-style manuscript reference list were synchronized in Issues #22–#23 for all newly used sources. Bab 1–3 use author–date citations in manuscript prose rather than repository citation keys. No source is cited in Bab 1–3 solely on the basis of a claim that could not be verified during the prior evidence audits.

One conservative rule remains: any new citation added after this integration must update both `literature/references.bib` and `manuscript/07-references.md` in the same PR.

**Decision: PASS.**

## 14. Quality ratings

Scores are proposal-stage ratings, not claims that data or results already exist.

| Dimension | Score /10 | Rationale |
|---|---:|---|
| Problem significance | **8.7** | engagement is substantively justified without artificial DKI crisis; local magnitude remains unknown |
| Theoretical architecture | **8.6** | context theory separated from proximal mechanism; actual competing mechanism measured |
| Construct validity | **8.7** | major construct mismatches resolved; local validation still pre-fielding |
| Literature synthesis | **8.8** | consensus, mixed/null evidence, reversals, and rivals retained |
| Research gap logic | **8.5** | explanatory/identification gap replaces combination gap |
| Novelty/contribution potential | **8.0** | mechanism discrimination is defensible but contribution is not established before results |
| Identification strategy | **8.6** | longitudinal baseline/reciprocal architecture is strong for observational study; causal identification remains limited |
| Sampling design | **8.3** | probability-oriented clustered design specified; actual frame/participation not yet secured |
| Measurement plan | **8.4** | candidate instruments + adaptation/invariance plan; field readiness pending pilot |
| Analysis strategy | **8.7** | model comparison, clustering, missingness, DAG, robust estimator decisions aligned |
| Ethics/data governance | **8.6** | adolescent safeguards and data minimization explicit |
| Internal coherence Bab 1–3 | **9.0** | title–problem–RQ–objective–theory–hypothesis–method now aligned |

### Overall proposal-stage rating

**8.6/10 — doctoral-level working proposal architecture, conditional on successful pre-fielding validation.**

This score does not mean novelty or causal effects are established. The weakest substantive dimension is contribution potential because its value depends on whether the final data actually discriminate SEC versus BPNS mechanisms and/or cross-context configurations. That uncertainty is intrinsic to a falsifiable doctoral proposal and should not be hidden.

## 15. Residual risks

1. **DPM→general engagement remains the weakest core evidence link.** Direct strategy-specific engagement relations may be small/null; the study must accept that possibility.
2. **BPNS addition increases respondent burden.** Item selection must preserve construct coverage without ad hoc shortening.
3. **Three-wave school panel feasibility is nontrivial.** School turnover, schedule constraints, and attrition can reduce effective sample and cluster coverage.
4. **RI-CLPM may be underpowered or unstable.** It is a sensitivity analysis, not a requirement for declaring the entire study failed.
5. **Interaction novelty is power-sensitive.** Reinforcement/compensation must be dropped from confirmatory claims if simulation shows inadequate precision.
6. **Probability-oriented sampling depends on frame and school cooperation.** Nonresponse/participation bias must be quantified where possible.
7. **Common student-report source remains a limitation** despite temporal separation and optional parent corroboration.

## 16. Final GO/NO-GO

### GO

- **GO for proposal/manuscript continuation.** Bab 1–3 now form a coherent canonical working proposal.
- **GO for instrument permission/adaptation, cognitive interviewing, pilot study, sampling-frame preparation, ethics submission, and preregistration preparation.**

### NO-GO

- **NO-GO for main three-wave data collection** until all eight pre-fielding gates in Bab 3 are completed.
- **NO-GO for causal-effect claims** from the planned observational panel.
- **NO-GO for novelty claims** based on variable combination, DKI, SEC mediation, or SEM/PLS-SEM.

## 17. Definition of Done

- [x] title aligned with final constructs and noncausal language;
- [x] Bab 1 rewritten around final problem/outcome/mechanisms;
- [x] Bab 2 populated with bounded theory, construct definitions, synthesis, gap, model, hypotheses;
- [x] Bab 3 populated with longitudinal design, sampling, measurement, analysis, ethics, power, and pre-fielding gate;
- [x] RQs and objectives aligned one-to-one;
- [x] hypotheses follow theory/evidence rather than desired SEM shape;
- [x] novelty re-audited and downgraded where falsified;
- [x] main causal limitation explicit;
- [x] references remain synchronized from upstream evidence issues;
- [x] final quality audit completed;
- [x] explicit GO/NO-GO decision recorded.

## 18. Decision

**ISSUE #24 DECISION: PASS.**

The canonical proposal manuscript is now ready for the next legitimate stage: instrument/adaptation/pilot and institutional preparation. It is **not yet ready for main data collection**, and that distinction is part of the final quality gate rather than an unfinished manuscript decision.