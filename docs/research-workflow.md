# Alur riset doktoral

Alur ini merupakan konvensi kerja proyek. Tahap dapat diulang ketika bukti mengubah keputusan. Lihat [quality gates](quality-gates.md). Draf dan memo boleh dibuat sepanjang proses tanpa mengubah status kesiapan ilmiah.

Pada proyek disertasi (mode RESEARCH), setiap pekerjaan pada tahap di bawah dimulai dari issue aktif dan mengikuti [workflow Git](git-workflow.md). Hasil berkas masuk ke main melalui PR, review, dan merge. Pada akhir sesi simpan checkpoint issue; issue induk memetakan child issue bila satu tahap terdiri atas beberapa keluaran. Pemeliharaan repositori induk TEMPLATE bukan pelaksanaan tahap penelitian ini.

| Tahap | Pertanyaan keputusan | Artefak kerja | Skill |
|---|---|---|---|
| 0. Konteks | Apa mandat, batas, dan kelayakan penelitian? | Project brief dan daftar ketidakpastian | framing |
| 1. Masalah | Apa yang belum dijelaskan dan mengapa penting? | Problem memo dan pertanyaan penelitian | framing |
| 2. Pemetaan | Perdebatan dan konsep apa yang relevan? | Peta awal literatur dan istilah | evidence, theory |
| 3. Protokol | Bagaimana bukti dikumpulkan secara transparan? | Review protocol, rencana seleksi/appraisal | evidence |
| 4. Bukti | Apa isi dan keterbatasan studi yang benar-benar dibaca? | Search log, screening, source notes, claim ledger | evidence |
| 5. Sintesis | Penjelasan mana yang bertahan terhadap bukti tandingan? | Debate map dan contribution audit | theory |
| 6. Desain | Bukti apa yang dapat menjawab pertanyaan secara layak? | Design matrix, analysis plan, ethics/data plan | design |
| 7. Pelaksanaan | Apakah syarat operasional terpenuhi dan rencana dijalankan? | Catatan lapangan/pilot, deviations, hasil analisis | design |
| 8. Interpretasi | Bagaimana hasil mengubah pemahaman? | Sintesis hasil, integrasi, batas kontribusi | theory, writing |
| 9. Naskah/ujian | Apakah argumen dapat ditelusuri dan dipertahankan? | Naskah, audit, tanggapan reviewer, ekspor | writing, audit |

Nama skill lengkap dan tautan ada di [indeks](skills.md). Salin [template](../templates/README.md) hanya ketika dibutuhkan. Gunakan [model provenance](provenance.md) agar source/report, study, claim, decision, dan review finding dapat ditelusuri.

## Penelusuran dan akses

Pemetaan eksploratif boleh mendahului protokol. Jangan menyebutnya review sistematis secara retrospektif tanpa proses yang memenuhi klaim tersebut. Catat batas akses ke basis data; pencarian web atau rekomendasi AI tidak membuktikan cakupan menyeluruh.

Pilih sumber berdasarkan pertanyaan dan disiplin: artikel, monograf, arsip, dokumen kebijakan, dataset, disertasi, atau sumber primer lain dapat mempunyai fungsi berbeda. Bukan semua bukti harus berupa artikel jurnal.

Untuk review terstruktur, tetapkan sebelumnya cara deduplikasi, seleksi, pemeriksaan, penyelesaian perbedaan, appraisal, dan sintesis. Jika keterbatasan personel memengaruhi pemeriksaan independen, laporkan praktik aktual dan dampaknya.

## Kapan berhenti mencari?

Tetapkan kriteria sesuai pendekatan: jalankan seluruh pencarian yang direncanakan, selesaikan seleksi, tangani sumber dekat dan bukti tandingan, serta jelaskan keterbatasan akses dan jadwal pemutakhiran. Pada pencarian iteratif, dokumentasikan alasan kecukupan konseptual. Tidak ada jumlah artikel universal yang membuktikan kedalaman.

## Perubahan arah

Perubahan konsep, metode, atau pertanyaan dicatat dalam [decision log](../research/decision-log.md). Perubahan terhadap protokol yang sudah ditetapkan dicatat pula dalam [deviation log](../research/deviation-log.md), termasuk apakah hasil sudah dilihat. Buka kembali gate yang terdampak.


## Gate dan perubahan basis keputusan

Setiap tahap dinilai dengan [quality gates](quality-gates.md) pada scope dan commit tertentu. Jika bukti baru, correction/retraction, perubahan RQ, perubahan desain, atau temuan lain mengubah basis keputusan, buka kembali gate yang terdampak dan buat assessment baru. Jangan menimpa assessment lama.
