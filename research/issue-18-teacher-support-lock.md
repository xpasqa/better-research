# Issue #18 — Lock X2 Teacher/School Construct

## 0. Decision rule

X2 tidak boleh disebut `Kompetensi Guru` bila primary exposure berasal dari student report. Konstruk harus sesuai dengan apa yang benar-benar dapat diamati/dirasakan siswa, memiliki construct boundary yang jelas, dan tidak mencampur professional teacher competence, enacted instructional quality, relationship quality, serta perceived support menjadi satu label.

## 1. Comparative construct audit

| Candidate | Construct level | Best informant | Fit with Y engagement | Fit with Z SEC | Measurement maturity | Decision |
|---|---|---|---|---|---|---|
| Teacher professional competence | teacher/class level | teacher tests, records, observations, multi-source | indirect through instruction | indirect/plausible | strong but resource-intensive | **REJECT as primary X2** |
| Student-perceived instructional quality | student perception + class/teacher level variance | students, often aggregated; observation useful | strong | plausible but broad | strong | **RANK #2 / rival-secondary construct** |
| Teacher-student relationship | dyadic/student level and class context | student + teacher | strong | strong adjacent evidence | very strong | **RANK #3 / rival relational mechanism** |
| Perceived Teacher Support | student-perceived/dyadic exposure | student | **very strong and construct-matched** | direct adjacent secondary-school evidence | strong, including recent adolescent scale | **KEEP / FINAL WORKING X2** |

## 2. Why `Kompetensi Guru` is rejected as the primary X2

Teacher professional competence is an attribute of the teacher, not a perception that can be validly reconstructed from a general student questionnaire. Kunter et al. operationalized professional competence with multiple teacher-level components, including pedagogical content knowledge, professional beliefs, work-related motivation, and self-regulation; in 194 German secondary mathematics classes, these teacher attributes were linked to instructional quality and then student outcomes through two-level modeling [@kunter2013competence]. This evidence supports the importance of teacher competence, but also demonstrates why it is a different construct from student-perceived support.

The existing López-Martín et al. meta-analysis likewise shows that teacher characteristics/competencies relate to secondary-school achievement, but competency domains are heterogeneous [@lopezmartin2023teachers]. Therefore a student-report item such as “guru saya kompeten” would not substitute for direct measurement of pedagogical/content competence.

**Decision:** professional teacher competence is retained as a possible upstream/contextual teacher attribute for future studies, not Gemma's primary X2.

## 3. Instructional quality: strong but broader than the focal mechanism

Student perceptions of instructional quality are methodologically defensible. Wisniewski et al. validated the two-level structure of secondary students' perceptions across 15,005 students in 690 classrooms and found strict invariance across subject groups, school types, and grade levels [@wisniewski2020instructional]. Ruzek et al. further showed, using a cross-subject within-student design, that ratings of teacher support contain both student-rater and teacher-rated variance; student-reported teacher support was associated with achievement gains and self-efficacy, while monitoring was inconsistent [@ruzek2022instructional].

However, instructional quality commonly includes cognitive activation, classroom management, instructional clarity, and supportive climate. That breadth creates two problems for Gemma: it changes X2 into a classroom-process construct much wider than the support mechanism, and it substantially increases the need for subject-specific/class-level linkage and multilevel interpretation.

**Decision:** instructional quality remains a strong rival/secondary school mechanism, not primary X2.

## 4. Teacher-student relationship: powerful rival, but conceptually different

The existing second-order meta-analysis by Emslander et al. shows robust relations between teacher-student relationships and multiple student outcomes, including motivation, belonging/engagement, behavior, executive functioning/self-control, and achievement [@emslander2025teacherstudent]. Magro et al. also show a meta-analytic association between teacher-student relationship quality and peer social competence [@magro2023studentteacher].

Nevertheless, relationship quality captures dyadic closeness/conflict/help and relational history. It is not identical to the specific resources/support provided by teachers. Because the dissertation already needs a school-side exposure that maps parsimoniously onto engagement and social-emotional functioning, perceived support has the cleaner boundary.

**Decision:** teacher-student relationship is retained as a major rival/alternative relational mechanism and should be tested theoretically in #20/#22, not folded into X2.

## 5. Final construct: Perceived Teacher Support

### 5.1 Name

> **X2 = Perceived Teacher Support (PTS) / Dukungan Guru yang Dipersepsikan Siswa**

### 5.2 Conceptual definition

PTS is defined as **the student's perception that teachers provide resources and responses that help the student function academically and socio-emotionally, including instrumental, emotional, informational, and appraisal support**.

This is deliberately a student-experienced construct. It does not claim to measure objective teacher competence, teacher credentials, pedagogical content knowledge, or the total quality of instruction.

## 6. Evidence fit with final Y: Student Engagement

Tao et al.'s meta-analysis of 71 empirical articles shows a small-to-medium association between perceived teacher support and achievement and, importantly for Gemma, indicates that general engagement and behavioral, cognitive, and emotional engagement partially account statistically for the support-achievement relation [@tao2022teachersupport].

A more focused meta-analysis by Vargas-Madriz et al. synthesized 141 studies covering 525,129 students and found a positive association between teacher support and school engagement. Effect magnitude varied by support domain, engagement dimension, school level, sex, design, and informant [@vargasmadriz2024support]. This is strong evidence against treating PTS as a homogeneous one-dimensional “good teacher” score.

Longitudinally, Martin et al. followed 7,769 students across four waves from early to mid-adolescence and found that perceived teaching support was associated with more favorable motivation and engagement trajectories, including sustaining and escalating associations across time [@martin2024support]. This strengthens temporal plausibility but still does not transform observational support ratings into an identified causal effect.

## 7. Evidence fit with SEC

Collie examined 319 secondary students and found that perceived social-emotional instructional support—particularly autonomy- and competence-support—was positively associated with students' perceived competence for emotion regulation and conflict resolution [@collie2022supportsec]. This is more construct-matched to the planned PTS→SEC pathway than general teacher-competence evidence.

The result is **supportive but not sufficient for causal mediation**. The study is observational and focuses on selected social-emotional competencies rather than establishing a universal pathway from all forms of teacher support to full multidimensional SEC. Issue #19 must still lock Z, and Issue #20 must compare SEC against rival mechanisms.

## 8. Measurement decision

### 8.1 Primary candidate

Wu et al. developed the **Perceived Teacher Support Scale (PTSS)** with 1,138 students in grades 7–10. The final 25-item instrument distinguishes four theoretically meaningful support domains:

1. instrumental support;
2. emotional support;
3. informational support;
4. appraisal support.

Factor and Rasch analyses supported the psychometric quality of the scale, gender invariance was reported, and correlation with student engagement supported concurrent validity [@wu2024ptss].

**Decision:** PTSS is the primary measurement candidate for content/structure review, subject to Indonesian adaptation, readability/cognitive interviewing, CFA/ESEM comparison, reliability, discriminant validity, and invariance testing in the target DKI sample.

### 8.2 Measurement specification

Default specification:

- four correlated first-order PTS dimensions;
- do **not** assume a single reflective total score before target-sample model comparison;
- if a higher-order PTS factor is considered, it must outperform or adequately represent the multidimensional structure and preserve substantive interpretation;
- domain-specific paths should be considered if support dimensions show materially different relations with SEC/engagement.

## 9. Informant and level-of-analysis lock

### Primary informant

**Student report**.

The construct is explicitly `perceived teacher support`, so student report is not a proxy error; it is the construct definition. This also keeps the focal exposure aligned with students' experienced environment.

### Level

Primary estimand is **individual student-level perceived support**. However, students are nested within classes/teachers/schools and perceptions can contain both individual/dyadic and shared teacher/class components. Therefore:

- student-level observations cannot automatically be treated as independent;
- teacher/class/school identifiers must be retained;
- ICCs must be estimated;
- cluster-robust or multilevel analysis must be considered in #23;
- aggregation to teacher/class level requires empirical justification (e.g., sufficient between-cluster variance and agreement), not convenience.

Ruzek et al.'s variance decomposition directly reinforces this point: student ratings contained meaningful student-rater and teacher-rated variance [@ruzek2022instructional].

## 10. Implications for RQ and hypotheses

Old wording such as:

> “Bagaimana hubungan Kompetensi Guru yang Dipersepsikan Siswa dengan ...?”

must become:

> “Bagaimana hubungan Dukungan Guru yang Dipersepsikan Siswa dengan Kompetensi Sosial-Emosional siswa SMP di DKI Jakarta?”

and

> “Bagaimana hubungan Dukungan Guru yang Dipersepsikan Siswa dengan Keterlibatan Siswa dalam Pembelajaran pada siswa SMP di DKI Jakarta?”

Any indirect pathway through SEC remains a **statistical/longitudinal indirect association** unless #23 provides stronger identification. Do not use `pengaruh`/`effect` as a causal claim from ordinary observational associations.

## 11. Rival explanations and controls for later design

Key school-side rivals include:

- teacher-student relationship quality;
- instructional quality/cognitive activation;
- classroom management;
- classroom climate and peer climate;
- teacher competence/professional knowledge;
- school resources and leadership;
- prior student achievement and motivation;
- student response style / generalized positive perception of teachers.

These are not automatic statistical controls. #20 and #23 must use theory/DAG logic to avoid over-adjustment or controlling mediators.

## 12. Consequences for method

A student-report PTS design is substantially more coherent than pretending to measure teacher competence through students, but it creates explicit design requirements:

1. preserve class/teacher/school clustering IDs;
2. where feasible, collect teacher/class contextual data for corroboration rather than relabeling student PTS as objective teacher quality;
3. use temporal separation if mediation is tested;
4. consider multi-level/complex-survey SEM when cluster structure and cluster count permit;
5. test measurement invariance across relevant subgroups before comparing structural paths.

## 13. Definition of Done

- [x] Teacher competence, perceived teacher support, instructional quality, and TSR compared.
- [x] Label/informant mismatch resolved.
- [x] Final X2 name and definition locked.
- [x] Primary informant and construct level locked.
- [x] Validated adolescent instrument candidate identified.
- [x] Multidimensional measurement specification stated.
- [x] Nested-data implications stated.
- [x] Fit with final Y engagement and SEC audited.
- [x] Rival school mechanisms retained rather than hidden.
- [x] Causal language restricted.

## 14. Decision

**ISSUE #18 SUBSTANTIVE DECISION: PASS.**

`Kompetensi Guru` is **dropped as the primary X2**. The working X2 is locked as **Perceived Teacher Support / Dukungan Guru yang Dipersepsikan Siswa**, measured primarily from students and interpreted as an individual/dyadic perceived exposure with possible shared teacher/class variance. The PTSS four-domain structure is the primary instrument candidate. Teacher professional competence, instructional quality, and teacher-student relationship remain distinct upstream/rival constructs rather than being conflated into X2.