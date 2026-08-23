# Issue #45 — Rencana Preregistration dan Analisis

## 1. Tujuan

Preregistration digunakan supaya keputusan utama **ditetapkan sebelum melihat data studi utama**.

Tujuannya bukan membuat dokumen statistik yang sangat rumit. Yang perlu dikunci adalah:

- pertanyaan utama;
- konstruk dan scoring final;
- analisis utama;
- apa yang dianggap secondary/exploratory;
- cara menangani missingness, clustering, attrition, dan model yang tidak berjalan.

## 2. Status

Skeleton preregistration sudah dapat disiapkan, tetapi versi final belum boleh disubmit sebelum #41–#44 stabil.

Status: **PREREGISTRATION SKELETON READY — FINAL SPECIFICATION PENDING**.

## 3. Pertanyaan penelitian yang akan diprespesifikasi

Gunakan enam RQ dari Bab 1, tetapi pada preregistration dapat ditulis lebih sederhana:

1. Apakah masing-masing strategi DPM di awal berkaitan dengan engagement berikutnya setelah engagement sebelumnya diperhitungkan?
2. Apakah PTS di awal berkaitan dengan engagement berikutnya setelah engagement sebelumnya diperhitungkan?
3. Apakah DPM dan PTS berkaitan dengan perubahan SEC dan BPNS?
4. Apakah SEC dan BPNS berkaitan dengan engagement berikutnya setelah kondisi sebelumnya diperhitungkan?
5. Apakah jalur tidak langsung menuju engagement lebih konsisten melalui SEC, BPNS, atau keduanya?
6. Jika power cukup, apakah enabling DPM dan PTS tampak saling memperkuat atau saling mengompensasi?

RQ6 tetap secondary/power-gated.

## 4. Hipotesis utama

### H1

PTS yang lebih tinggi pada baseline diperkirakan berhubungan dengan engagement berikutnya yang lebih tinggi setelah engagement sebelumnya diperhitungkan.

### H2

PTS yang lebih tinggi diperkirakan berhubungan dengan BPNS berikutnya yang lebih tinggi setelah BPNS sebelumnya diperhitungkan.

### H3

BPNS yang lebih tinggi diperkirakan berhubungan dengan engagement berikutnya yang lebih tinggi setelah kondisi sebelumnya diperhitungkan.

### H4

SEC yang lebih tinggi diperkirakan berhubungan dengan engagement berikutnya yang lebih tinggi setelah kondisi sebelumnya diperhitungkan.

### H5 — lebih lemah

Enabling/interpretative DPM diperkirakan berhubungan positif dengan kapasitas sosial-emosional/regulasi berikutnya. Exact domain mengikuti final instrument #41.

Tidak dibuat hipotesis universal positif untuk restrictive atau observant DPM.

## 5. Analisis utama vs secondary vs exploratory

### Confirmatory utama

- measurement model final yang dikunci di #41;
- stability/baseline-adjusted prospective paths T1→T2 dan T2→T3 yang relevan;
- PTS→BPNS→engagement;
- SEC→engagement dan competing indirect pathway;
- model comparison SEC vs BPNS ketika keduanya dimasukkan bersama;
- selected DPM strategy paths yang ditetapkan sebelum main data collection.

### Secondary confirmatory

- DPM × PTS hanya jika #42 menunjukkan power/precision cukup;
- dimension-specific analyses hanya untuk dimensi yang sudah dikunci sebelum T1.

### Sensitivity

- reciprocal paths engagement↔SEC/BPNS;
- alternative reasonable adjustment set;
- cluster-robust vs multilevel treatment bila keduanya feasible;
- RI-CLPM/within-between model hanya bila data, waves, dan convergence memadai.

### Exploratory

- modification indices yang tidak diprespesifikasi;
- subgroup analysis yang tidak dipower;
- post-hoc interaction;
- item deletion setelah main fielding;
- alternative mediator baru.

Semua exploratory analyses harus diberi label eksploratori.

## 6. Unit dan wave

Unit substantif: individu siswa.

Cluster: kelas/sekolah; teacher ID dipertahankan bila tersedia dan relevan.

Wave utama:

- T1 = baseline;
- T2 = follow-up 1;
- T3 = follow-up 2.

Exact interval ditetapkan sebelum preregistration final setelah feasibility sekolah diketahui.

## 7. Inclusion dan exclusion

Final criteria mengikuti sampling #43, tetapi minimum:

### Include

- siswa pada kelas/sekolah terpilih;
- eligible grade;
- consent/assent sesuai protocol;
- mempunyai participant ID valid.

### Exclude dari specific analysis

- respons yang tidak dapat dipasangkan ke wave yang diperlukan;
- duplicate/invalid session berdasarkan rule yang diprespesifikasi;
- missingness yang membuat estimand tertentu tidak dapat dihitung, bila estimator tidak dapat mengakomodasi.

Jangan mengeksklusi siswa karena jawabannya “aneh” tanpa rule data-quality yang ditetapkan sebelumnya.

## 8. Measurement

Preregistration final harus menyebut:

- instrumen final;
- subskala;
- item/reverse scoring;
- response scale;
- higher-order vs correlated-factor decision dari #41;
- apakah score latent atau observed/composite digunakan pada tiap analysis;
- longitudinal measurement invariance decision rule.

Jangan mengubah measurement model hanya agar structural path menjadi signifikan.

## 9. Measurement invariance — aturan sederhana

Urutan minimum:

1. cek apakah struktur faktor yang sama bekerja di T1–T3;
2. cek apakah loading cukup comparable;
3. cek intercept/threshold sesuai jenis item jika ingin membandingkan latent means/change;
4. partial invariance hanya dipakai bila ada alasan jelas dan dilaporkan.

Jika invariance gagal secara berat, interpretasi perubahan longitudinal harus diturunkan, bukan dipaksakan.

## 10. Missing data

Default:

- laporkan missingness per item/wave;
- analisis attrition T1→T2→T3;
- gunakan FIML atau multiple imputation yang sesuai model/data, bukan complete-case sebagai default;
- auxiliary variables dapat digunakan bila justified dan ditentukan sebelum analysis final.

Method final mengikuti estimator dan data type.

## 11. Clustering dan weighting

- school/class IDs selalu dipertahankan;
- cek ICC dan design structure;
- gunakan multilevel model atau cluster-robust SE sesuai final cluster count dan model complexity;
- sampling weights digunakan bila unequal selection probability/nonresponse adjustment memang dapat dihitung dari frame.

Jangan membuat weight buatan jika informasi tidak cukup.

## 12. Covariates

Covariates tidak dipilih berdasarkan “mana yang signifikan”.

Sebelum preregistration final, buat DAG/logic sederhana untuk estimand utama. Kandidat yang sudah diketahui dari literature antara lain prior engagement/achievement, SES/parental education, general parenting, peer support, dan classroom/school conditions.

Masukkan hanya yang diperlukan untuk estimand tertentu dan benar-benar dapat diukur dengan kualitas memadai.

## 13. Estimator

Default family tetap latent-variable/covariance-based SEM karena fokusnya confirmatory model comparison.

Final estimator mengikuti:

- response scale/item type;
- distribution;
- missingness;
- cluster structure;
- convergence.

PLS-SEM tidak menjadi fallback otomatis hanya karena model sulit converge atau sampel lebih kecil dari harapan.

## 14. Indirect association

Untuk jalur tidak langsung:

- baseline mediator/outcome diperhitungkan sesuai model;
- SEC dan BPNS dibandingkan dalam model yang sama bila feasible;
- laporkan estimate + confidence interval;
- hindari bahasa “causal mediation effect”.

Bahasa utama: **jalur tidak langsung yang terurut waktu / prospective indirect association**.

Dalam naskah Indonesia, istilah teknis ini dapat dijelaskan sederhana sebagai “apakah hubungan awal dengan engagement berikutnya tampak berjalan melalui perubahan SEC atau BPNS”.

## 15. Multiplicity

Tidak perlu correction yang rumit untuk setiap tabel.

Prinsip:

- batasi confirmatory hypotheses;
- tandai primary vs secondary;
- gunakan confidence intervals dan effect sizes;
- jika banyak domain DPM/subscale diuji, prespecify family of tests dan correction/interpretation rule yang proporsional.

Exact rule ditentukan setelah item/subscale final #41.

## 16. Model failure/fallback

Jika model utama tidak converge:

1. cek coding/data errors;
2. cek measurement model;
3. cek over-complexity;
4. gunakan fallback yang sudah ditulis sebelumnya;
5. jangan langsung membuang indikator/path berdasarkan modification index.

Fallback harus membuat model lebih sederhana, bukan mengganti pertanyaan penelitian.

## 17. Deviations

Setiap perubahan setelah preregistration dicatat dengan:

- apa yang berubah;
- kapan diputuskan;
- mengapa;
- apakah sebelum/after melihat outcome;
- status confirmatory atau exploratory setelah perubahan.

## 18. Yang masih menunggu

Preregistration final belum dapat diselesaikan sampai:

- #41 final battery/scoring;
- #42 final sample/cluster dan interaction decision;
- #43 final sampling frame/weights;
- #44 final ethics/data governance;
- exact wave schedule.

## 19. Definition of Done

Issue #45 ditutup bila:

- full preregistration/SAP sudah diisi dengan keputusan final;
- primary/secondary/exploratory boundary jelas;
- missingness/clustering/weights/attrition rules jelas;
- model comparison SEC vs BPNS dapat dijalankan;
- preregistration siap disubmit sebelum T1.

Saat ini issue tetap **OPEN**.
