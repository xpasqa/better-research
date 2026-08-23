# Issue #4 — Evidence Audit dan Literature Search Protocol Gemma

## 0. Scope dan rule

Audit ini mengikuti urutan `Research Question -> Theory -> Design -> Data -> Measurement -> Identification -> Analysis`. Literatur dipakai untuk menguji model, bukan untuk membenarkan model yang sudah diasumsikan benar.

Sumber akademik yang dipakai di sini sudah melalui `search -> fetch/open -> metadata verification`. Metadata canonical disimpan di `literature/references.bib`, APA 7 di `manuscript/07-references.md`, dan synthesis di `literature/matrix-literature-review.md`.

Bahasa kausal tidak digunakan untuk studi observasional/asosiasional. Meta-analysis intervention SEL dibedakan dari studi yang hanya mengukur social-emotional competence siswa.

## 1. Audit per evidence cluster

| Cluster | Evidence terverifikasi | Temuan yang boleh dipakai | Batas/kontra-evidence | Implikasi untuk Gemma |
|---|---|---|---|---|
| 1. Digitalisasi kehidupan remaja | Navarro & Tudge [@navarro2023neoecological] | Digital/virtual contexts dapat diposisikan sebagai bagian ekologis perkembangan remaja | Ini theoretical extension, bukan estimasi efek teknologi | Digital context relevan secara teori, tetapi “digitalisasi menyebabkan readiness” tidak boleh diklaim |
| 2. Keluarga-sekolah dalam ekologi | Rosa & Tudge [@rosa2013bronfenbrenner]; Costa et al. [@costa2024achievement] | Family, school, peer, dan personal factors dapat diposisikan sebagai contextual systems/determinants | Mature bioecological theory menekankan proximal process/PPCT; model cross-sectional Gemma tidak menguji full PPCT | Bronfenbrenner dipakai sebagai positioning/explanatory lens, bukan klaim test of theory |
| 3. SMP/adolescence | Costa et al. [@costa2024achievement]; Bharara & Duncan [@bharara2024pstrs] | Middle/secondary-school outcomes dipengaruhi faktor personal/contextual; transition merupakan developmental challenge | Outcome dan konteks berbeda dari readiness sehari-hari | Justifikasi jenjang SMP harus terkait developmental/transition demands, bukan school-readiness preschool |
| 4. DKI context | BPS DKI [@bpsdki2025education] + tabel ICT BPS | DKI dapat dideskripsikan dengan data pendidikan dan akses internet resmi | Aggregate statistics tidak mengukur readiness/SEC siswa | Pakai sebagai contextual evidence dan sampling frame, bukan outcome evidence |
| 5. Digital parenting construct | Modecki et al. [@modecki2022digital] | Digital parenting/parental mediation bersifat multidimensional dan measurement practice terfragmentasi | Positive use, bidirectionality, dan heterogeneity sering kurang terwakili | X1 tidak boleh berupa kumpulan indikator ad hoc tanpa instrument rationale |
| 6. Digital parenting effects | Lukavská et al. [@lukavska2022parenting]; Tong et al. [@tong2024internetparenting] | General/media-specific parenting berhubungan dengan online outcomes, tetapi efek sering lemah/conditional | Media-specific parenting tidak konsisten protektif; child effects/reverse direction kuat pada beberapa domain | Falsifies “digital parenting selalu positif”; causal wording harus diturunkan |
| 7. X1 -> self-regulation/SEC-adjacent | Chen & Chng [@chen2016mediation] | Parental mediation trajectories berasosiasi dengan later online self-regulation/emotion regulation | Tidak mengukur full CASEL SEC atau learning readiness | Jalur X1->Z plausible secara parsial, belum construct-matched |
| 8. Teacher competence | López-Martín et al. [@lopezmartin2023teachers] | Teacher characteristics/competencies berhubungan dengan secondary students' academic achievement | Competence domains heterogeneous; outcome achievement bukan readiness | X2 relevan, tetapi construct definition dan informant harus dikunci |
| 9. Teacher relationship/support as rival mechanism | Emslander et al. [@emslander2025teacherstudent]; Tao et al. [@tao2022teachersupport] | TSR/support berkaitan dengan engagement, motivation, achievement, self-control, well-being | TSR/support ≠ teacher competence | Jika siswa menjadi responden, perceived support/relationship mungkin lebih valid daripada “teacher competence” |
| 10. X2 -> social competence/SEC-adjacent | Magro et al. [@magro2023studentteacher] | TSR quality berkorelasi dengan social competence across ages | School relationship construct, bukan teacher competence; social competence bukan full SEC | Jalur school context->SEC plausible, tapi exact X2->Z belum established |
| 11. SEL vs SEC construct | CASEL [@casel2020framework]; Martinez-Yarza et al. [@martinezyarza2023instruments] | SEL adalah proses; self-awareness, self-management, social awareness, relationship skills, responsible decision-making adalah competence areas; measurement tools beragam | Five domains bukan satu ready-made questionnaire; multi-method/multi-informant dianjurkan | Draft Z secara ontologis mismatch jika mengukur lima kompetensi tetapi menamakannya “Pembelajaran Sosial-Emosional” |
| 12. SEL outcome evidence | Cipriano et al. [@cipriano2023sel]; Durlak et al. [@durlak2022sel] | Universal school-based SEL interventions menunjukkan positive average effects pada skills, behavior, school functioning, achievement | Heterogeneity besar; mechanisms/moderators belum konsisten | Mendukung pentingnya SEL, tetapi tidak membuktikan individual SEC sebagai mediator X1/X2->Y |
| 13. Learning readiness construct | Wang et al. [@wang2023online]; Bharara & Duncan [@bharara2024pstrs] | Readiness dapat dioperasionalisasi secara context-specific: online learning readiness atau school-transition readiness | Verified sources tidak memvalidasi draft Gemma yang mencampur motivation, discipline, adaptation, engagement, strategy sebagai satu generic readiness construct | Y **gagal construct gate dalam bentuk draft sekarang**; perlu re-specification atau instrumen yang benar-benar tervalidasi untuk tujuan penelitian |
| 14. SEC -> learning functioning | Cipriano et al. [@cipriano2023sel]; Wang et al. [@wang2023online] | SEL interventions dan emotional competence berhubungan dengan school/online academic functioning | Intervention evidence dan online-COVID context tidak sama dengan SEC->generic readiness | Z->Y belum construct-matched; tidak boleh disebut established |
| 15. Integrated mediation | Evidence di atas | Family/school contexts, social-emotional capacities, dan learning outcomes secara teori dapat dihubungkan | Tidak ditemukan evidence terverifikasi dalam audit ini yang identik dengan X1-X2-Z-Y Gemma dan tidak cukup untuk mengklaim model belum pernah ada | Mediation tetap hypothesis/model kerja, bukan established mechanism atau novelty |
| 16. Boundary condition DKI | BPS context + ecological theory | DKI dapat diperlakukan sebagai urban educational setting | Belum ada evidence bahwa DKI mengubah strength/direction hubungan antar konstruk | DKI = setting; theoretical boundary-condition claim belum defensible |
| 17. Rival explanations | Costa et al.; Emslander et al.; Tao et al. | SES/parental education, prior achievement, school condition, peers, teacher-student relationship, engagement dan student characteristics berpotensi relevan | Tidak semuanya dapat dikontrol tanpa overfitting/desain memadai | Prioritaskan confounders berdasarkan DAG/theory, bukan memasukkan semua variabel sebagai kontrol dekoratif |

## 2. Construct audit — keputusan utama

### X1 — Pengasuhan Digital

**Status: RETAIN WITH RE-SPECIFICATION.**

Digital parenting layak dipertahankan sebagai family-context construct, tetapi measurement tidak boleh dibentuk dari daftar indikator draft secara bebas. Literature menunjukkan construct fragmentation dan praktik yang berbeda dapat mempunyai arah/implikasi berbeda [@modecki2022digital; @lukavska2022parenting].

Minimum requirement berikutnya:

- tentukan apakah X1 adalah parental mediation, broader digital parenting, atau kombinasi higher-order construct;
- pilih/refine instrument dengan sumber asli;
- bedakan active mediation, restrictive mediation, monitoring, co-use/modeling, autonomy support bila relevan;
- jangan memasukkan parental digital literacy sebagai indikator reflektif X1 tanpa theoretical measurement rationale.

### X2 — Kompetensi Guru

**Status: RETAIN ONLY AFTER INFORMANT DECISION.**

Meta-analysis mendukung relevansi teacher characteristics/competencies bagi secondary achievement [@lopezmartin2023teachers]. Namun, bila responden penelitian hanya siswa, klaim bahwa siswa “mengukur kompetensi guru” membutuhkan instrumen student-report yang valid. Evidence tentang perceived teacher support dan teacher-student relationship sangat kuat dan lebih natural untuk student reports [@emslander2025teacherstudent; @tao2022teachersupport].

Keputusan metodologis:

- **single-informant siswa:** ubah label menjadi konstruk persepsi yang tervalidasi (mis. perceived teacher support/quality/behavior), bukan objective teacher competence;
- **multi-informant guru+siswa:** desain menjadi nested/multilevel atau perlu aggregation/cluster treatment yang eksplisit.

### Z — Pembelajaran Sosial-Emosional

**Status: RE-SPECIFY.**

CASEL mendefinisikan SEL sebagai proses pendidikan, sementara lima area yang digunakan draft adalah competence areas [@casel2020framework]. Systematic measurement review juga memperlakukan social/emotional skills/competencies sebagai objek pengukuran siswa dan menunjukkan instrument diversity [@martinezyarza2023instruments].

**Keputusan working construct:** jika lima CASEL domains tetap diukur sebagai atribut siswa, Z sebaiknya disebut **Kompetensi Sosial-Emosional Siswa (Social-Emotional Competence/SEC)**, bukan “Pembelajaran Sosial-Emosional”.

Jika promotor menghendaki SEL sebagai Z, indikator harus mengukur exposure/quality/implementation of SEL instruction, bukan kompetensi internal siswa.

### Y — Kesiapan Belajar Siswa

**Status: FAILS CURRENT CONSTRUCT GATE.**

Evidence terverifikasi menunjukkan readiness pada remaja cenderung purpose-specific: online-learning readiness [@wang2023online] dan transition readiness [@bharara2024pstrs]. Audit ini belum memverifikasi satu construct/instrument yang mendukung agregasi motivation + discipline + adaptation + engagement + learning strategy menjadi generic “Kesiapan Belajar Siswa” SMP.

Konsekuensi:

1. jangan finalisasi measurement model Y dari indikator draft;
2. jangan menulis bahwa Y adalah established construct untuk SMP tanpa source;
3. sebelum data collection, pilih salah satu:
   - menemukan/menjustifikasi instrument readiness yang benar-benar sesuai konteks SMP; atau
   - re-specify outcome ke construct yang established dan paling sesuai research problem (mis. student engagement/academic adjustment/self-regulated learning), dengan issue keputusan tersendiri.

Audit tidak memilih pengganti Y secara otomatis karena itu merupakan substantive model change yang harus traceable dan sebaiknya mendapat review promotor.

## 3. Theory audit

Rosa dan Tudge menunjukkan teori Bronfenbrenner berevolusi dari ecological ke mature bioecological/PPCT; penelitian harus menyebut versi yang digunakan [@rosa2013bronfenbrenner]. Navarro dan Tudge menunjukkan digital/virtual microsystems dapat dipertimbangkan dalam neo-ecological extension [@navarro2023neoecological].

**Keputusan:** Gemma boleh menggunakan ecological/bioecological lens untuk memosisikan family dan school contexts, tetapi model survei cross-sectional X1/X2->Z->Y **tidak boleh diklaim sebagai empirical test of the full PPCT model**. Ia juga tidak menguji mesosystem family-school interaction jika tidak ada interaction/relationship construct yang diukur.

## 4. Falsification audit

Evidence yang secara langsung membatasi narasi positif model:

- digital parenting measurement terfragmentasi [@modecki2022digital];
- parenting-media associations lemah/conditional pada meta-analysis [@lukavska2022parenting];
- adolescent online behavior dapat memprediksi later parenting lebih kuat daripada arah sebaliknya [@tong2024internetparenting];
- teacher-student relationship/support adalah rival school mechanism yang kuat [@emslander2025teacherstudent; @tao2022teachersupport];
- SEL effects heterogeneous dan mechanism/moderator belum konsisten [@cipriano2023sel; @durlak2022sel];
- readiness bukan satu construct generik yang dapat dipindahkan antar konteks tanpa validation [@wang2023online; @bharara2024pstrs].

Karena itu, empat proposisi berikut **ditolak sebagai premis**:

1. Pengasuhan Digital selalu berdampak positif.
2. Kompetensi Guru selalu mempunyai direct effect pada readiness.
3. SEC/SEL adalah mediator utama/unik.
4. Konteks DKI dengan sendirinya memberikan novelty teoretis.

## 5. Evidence map untuk direct/indirect paths

| Path kerja | Evidence status | Keputusan |
|---|---|---|
| X1 -> Z/SEC | Adjacent, bukan exact: parental mediation -> self/emotion regulation [@chen2016mediation] | PLAUSIBLE, NOT ESTABLISHED |
| X2 -> Z/SEC | Adjacent: TSR -> social competence [@magro2023studentteacher] | PLAUSIBLE, NOT ESTABLISHED |
| Z/SEC -> Y | Misaligned outcomes: SEL intervention/online performance evidence [@cipriano2023sel; @wang2023online] | UNRESOLVED |
| X1 -> Y | Parenting evidence mostly digital-behavior outcomes, not generic readiness | UNRESOLVED |
| X2 -> Y | Teacher competence/support evidence mostly achievement/engagement, not generic readiness | UNRESOLVED |
| X1 -> Z -> Y | No construct-matched verified mediation chain in current audit | UNKNOWN |
| X2 -> Z -> Y | Alternative mediators (engagement/TSR/climate) have stronger direct literature | UNKNOWN / RIVAL MECHANISMS PRESENT |

## 6. Method claim audit: SEM-PLS

**Belum ada dasar untuk menyatakan SEM-PLS sebagai metode yang “tepat” hanya karena model memiliki mediasi dan beberapa konstruk laten.** Pemilihan estimator harus menunggu:

- final construct definitions;
- reflective/formative measurement specification;
- sampling design dan clustering;
- tujuan inferensi (explanatory vs predictive);
- sample size/power berdasarkan model final;
- distribution/missingness;
- identification dan common-method considerations.

Dengan demikian, SEM-PLS **bukan novelty dan bukan design rationale** pada Bab 1.

## 7. DKI evidence rule

BPS DKI 2025 menggunakan Susenas Maret 2024 dan registrasi sekolah 2023/2024 untuk menggambarkan kondisi pendidikan wilayah [@bpsdki2025education]. BPS juga menyediakan tabel official akses internet penduduk usia 5+ menurut kabupaten/kota dan jenis kelamin.

Penggunaannya dibatasi untuk:

- menggambarkan setting;
- membangun sampling frame/coverage;
- menunjukkan relevansi konteks digital secara makro.

Tidak boleh digunakan untuk menyimpulkan bahwa siswa SMP DKI mengalami rendah/tinggi readiness, SEC, digital parenting, atau teacher competence.

## 8. Kesimpulan evidence audit

### Established

- Digital parenting adalah construct multidimensional dengan measurement issues.
- Teacher characteristics/competencies dan especially teacher-student relationships/support berhubungan dengan student outcomes.
- Universal school-based SEL interventions mempunyai broad positive average effects.
- Lima CASEL areas adalah social-emotional competence areas di dalam systemic SEL framework.
- Secondary outcomes ditentukan oleh multi-level personal/family/school/peer factors.

### Mixed/conditional

- Arah dan strength digital parenting effects.
- Parent-vs-child directionality.
- Kondisi/moderator SEL effects.
- Teacher-side mechanism yang paling relevan untuk student report.

### Unknown/unresolved

- Generic learning readiness Y seperti pada draft.
- Construct-matched direct paths ke Y.
- SEC sebagai mediator spesifik X1/X2->Y.
- DKI sebagai true boundary condition.
- Novelty of integrated model.

## 9. Gate ke Issue #3 dan #5

Issue #3 boleh dilanjutkan karena evidence audit sekarang cukup untuk membedakan established/mixed/unknown dan menguji novelty secara falsificatory.

Issue #5 boleh melakukan rekonstruksi Bab 1, tetapi **tidak boleh menyembunyikan bahwa Y belum lulus construct gate**. Manuscript final tahap proposal harus membawa unresolved model decision tersebut secara eksplisit sampai promotor/user mengunci Y atau evidence measurement tambahan ditemukan.
