# Kriteria mutu dan kesiapan

Quality gate adalah keputusan berbasis bukti pada **scope tertentu**, bukan jumlah file atau status delivery. Seluruh gate riset mulai dengan status **BELUM DINILAI**.

Status:

- `BELUM DINILAI`
- `PERLU REVISI`
- `SIAP`
- `TIDAK BERLAKU` — wajib disertai alasan desain

Setiap penilaian mencatat: commit/versi, bukti yang diperiksa, bukti yang tidak diperiksa, penilai dan peran, critical failure bila ada, syarat penyelesaian, dan reopen trigger. Gunakan [template gate review](../templates/gate-review.md).

**PR PASS atau repository checks PASS tidak membuat gate otomatis SIAP.**

## Matriks gate

| Gate | Bukti minimum untuk SIAP | Critical failure / kondisi PERLU REVISI | Reopen trigger |
|---|---|---|---|
| **G0 Konteks** | Brief membedakan informasi terverifikasi, unknown, batas, mandat, dan keputusan terbuka; syarat institusi yang relevan tersedia | Tujuan, akses, aturan institusi, atau mandat inti masih diasumsikan padahal keputusan bergantung padanya | perubahan institusi/pedoman, akses data, tujuan proyek, batas waktu, atau mandat |
| **G1 Masalah** | Masalah empiris/konseptual jelas; RQ, unit analisis, konteks, dan signifikansi selaras serta dapat dijawab | hanya topik luas; problem normatif tanpa objek analisis; RQ mengandung jawaban; unit analisis tidak jelas; pertanyaan tidak dapat dijawab dengan bukti yang realistis | perubahan RQ, unit analisis, fenomena, scope, atau evidence mapping yang menggugurkan framing |
| **G2 Protokol & bukti** | Jenis review beralasan; search/screening trail, source notes, appraisal, dan claim provenance sesuai klaim cakupan | sumber inti tidak dibaca; seleksi tidak terlacak; report dihitung sebagai study berbeda; appraisal tidak sesuai desain; klaim “systematic/comprehensive” tanpa proses yang mendukung | perubahan RQ/protokol, database/akses baru, sumber inti baru, correction/retraction, atau temuan deduplication material |
| **G3 Teori & kontribusi** | Studi terdekat, mekanisme/argumen, teori yang mempunyai fungsi, evidence tandingan, alternatif, boundary conditions, dan batas kontribusi dipetakan | novelty hanya berdasarkan lokasi/kombinasi variabel/metode; tidak ada closest-study comparison; teori dekoratif; counterevidence diabaikan; klaim “pertama” tanpa dasar memadai | close prior study baru, perubahan definisi konstruk/RQ, correction/retraction penting, atau hasil empiris yang mengubah kontribusi |
| **G4 Desain** | RQ–data–design–analysis konsisten; target inferensi, asumsi, sampling/corpus, measurement, feasibility, ethics, dan limitation jelas | metode dipilih karena populer; bukti tidak mampu mendukung klaim; causal language tanpa identification; estimator/model tidak terjustifikasi; access/feasibility tidak realistis | perubahan RQ, data source, sample/corpus, instrument, analysis target, assumption, atau feasibility |
| **G5 Kesiapan pelaksanaan** | status etik/izin dan akses sesuai kegiatan; instrumen/prosedur, pilot bila relevan, governance, kapasitas, dan analysis plan memadai | approval yang diperlukan belum ada; protokol dianggap sama dengan pelaksanaan; consent/access diasumsikan; penyimpanan data tidak aman | perubahan prosedur, populasi, lokasi, data sensitivity, instrument, izin, atau governance |
| **G6 Hasil & interpretasi** | analisis terlacak; preprocessing/parameter/deviasi tersedia; uncertainty, hasil nol/tandingan, sensitivity, dan batas inferensi dilaporkan | hasil dibuat/dipilih tanpa jejak; exclusion tidak dijelaskan; HARKing disembunyikan; claim melampaui design; contradictory result dihapus | data/analysis baru, koreksi kode, exclusion/sensitivity baru, protocol deviation, atau discovery yang mengubah interpretation |
| **G7 Naskah & ujian** | alur masalah→RQ→teori→design→hasil→kontribusi konsisten; claim–evidence traceable; citations, tables/figures, references, response to critique, dan export diperiksa | claim utama tanpa bukti; bab saling inkonsisten; TODO substantif tersembunyi; citation tidak mendukung kalimat; hasil/approval yang belum terjadi ditulis sebagai fakta | perubahan substantif G1–G6, reviewer finding utama, citation correction/retraction, atau perubahan format institusi yang material |

## Kriteria kondisional

### Kuantitatif
Periksa bila relevan: target estimand/populasi, sampling, ukuran sampel berbasis precision/power/simulation, measurement validity/reliability, missingness, clustering, weights, confounding, model assumptions, multiplicity, robustness/sensitivity, dan uncertainty.

### SEM / latent-variable models
Bedakan measurement dan structural model, reflective/formative bila relevan, identification, estimator, sample adequacy, model fit, alternative models, dan batas causal interpretation.

### Kualitatif
Periksa kecocokan tradisi, case selection, positionality/reflexivity, provenance corpus, proses interpretasi, negative/deviant cases, context, dan adequacy sesuai pendekatan. Jangan memaksakan saturation, member checking, atau intercoder agreement pada semua tradisi.

### Mixed methods
Periksa alasan integrasi, sequence/priority, sample relationship, integration points, joint display bila relevan, dan bagaimana hasil yang tidak sejalan memengaruhi meta-inference.

### Konseptual / arsip
Periksa corpus selection, provenance, authenticity/context, aturan pembacaan, alternative interpretation, dan batas akses.

### Review tanpa peserta
Tentukan apakah ethics/permission tertentu masih relevan. Jangan mengarang approval atau menganggap semua review memerlukan prosedur peserta.

## Decision rule

Gunakan status paling konservatif yang sesuai evidence dalam scope:

- **SIAP**: semua evidence minimum yang berlaku telah diperiksa, tidak ada critical failure terbuka, dan limitation dicatat.
- **PERLU REVISI**: ada critical failure atau deficiency yang dapat mengubah validity/defensibility.
- **BELUM DINILAI**: scope/evidence belum cukup untuk penilaian.
- **TIDAK BERLAKU**: gate/kriteria tidak relevan karena desain, dengan alasan eksplisit.

Jangan menggunakan skor agregat untuk menutupi critical failure.

## Scope dan reviewer identity

Setiap gate review menyebutkan apa yang **tidak diperiksa**. Penilaian agent adalah assessment atas artefak yang dibaca, bukan persetujuan promotor, komite etik, reviewer jurnal, atau institusi.

Jika reviewer manusia memberi keputusan, catat identitas/peran sesuai kebutuhan proyek tetapi jangan menyimpulkan independensi atau otorisasi yang tidak dinyatakan.

## Reopening

Gate yang pernah SIAP harus dibuka kembali bila trigger material terjadi. Reopen tidak berarti pekerjaan sebelumnya salah; ia menunjukkan basis keputusan telah berubah.

Contoh:

```text
G3 = SIAP
    ↓
close prior study baru ditemukan
    ↓
G3 = PERLU REASSESSMENT
    ↓
review evidence + contribution
    ↓
SIAP / PERLU REVISI
```

Riwayat gate tidak dihapus. Simpan assessment baru sebagai review baru dan tautkan assessment sebelumnya.
