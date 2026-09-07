# Menulis issue sebagai memori proyek

Pada proyek disertasi (mode RESEARCH), GitHub Issue wajib dibuat/dipilih sebelum kerja substantif. Tujuannya agar peneliti dan sesi AI baru dapat memahami serta melanjutkan pekerjaan tanpa membaca seluruh percakapan lama. Pemeliharaan repositori induk TEMPLATE mengikuti pengecualian pada [workflow Git](git-workflow.md).

## Ukuran pekerjaan

Satu issue memuat satu keluaran atau keputusan yang dapat dinilai. Contoh judul: “Verifikasi dukungan sumber untuk klaim utama latar belakang” atau “Tetapkan protokol review berdasarkan pertanyaan penelitian”.

Untuk tahap besar, buat issue induk dengan tujuan dan daftar child issue. Setiap child memiliki scope, dependency, serta kriteria sendiri. Tautkan dua arah. Issue induk tetap terbuka sampai seluruh keluaran yang dibutuhkan terintegrasi; merge satu child tidak menutup induknya.

Jangan membuat issue baru untuk setiap pertanyaan kecil dalam tugas yang sama. Pecah issue bila scope berubah menjadi beberapa keluaran yang dapat ditinjau sendiri atau konteksnya sulit dimuat dalam satu ringkasan kerja.

## Isi wajib body

Gunakan [template tugas](../.github/ISSUE_TEMPLATE/research-task.md).

1. **Snapshot terkini:** status, repositori, branch, commit/checkpoint, PR, blocker, dan satu langkah berikutnya.
2. **Masalah dan alasan:** mengapa tugas diperlukan serta kaitannya dengan RQ/gate atau pemeliharaan builder.
3. **Konteks yang cukup:** keputusan sebelumnya, batas desain, asumsi, dan tautan sumber yang harus dibaca.
4. **Scope dan pengecualian:** bagian yang dikerjakan dan yang di luar cakupan.
5. **Keluaran:** berkas yang diharapkan, isi yang harus tersedia, dan letak hasil final.
6. **Kriteria penerimaan:** checklist yang dapat diperiksa melalui bukti; bedakan protokol dirancang dari kegiatan terlaksana.
7. **Rencana dan dependency:** urutan kerja, parent/child, pekerjaan lain yang menghalangi, serta penanggung jawab jika diketahui.
8. **Referensi/batas akses:** source ID/claim ID, dokumen, locator relevan, serta apa yang belum tersedia.
9. **Riwayat keputusan:** ringkasan dan tautan komentar/decision log; pembatalan keputusan lama tetap terlihat.
10. **Kriteria penutupan:** PR final atau alasan issue koordinasi tanpa perubahan berkas.

Tautan GitHub antarberkas sebaiknya menggunakan permalink commit untuk bukti versi yang direview, serta link branch untuk pekerjaan aktif. Jangan menganggap nomor halaman atau hasil pencarian terverifikasi hanya karena tertulis dalam issue.

## Status kerja

GitHub mempunyai status open/closed; status kerja berikut dicatat dalam snapshot body, dengan label sebagai cermin opsional:

| Status kerja | Arti |
|---|---|
| DRAFT | Konteks/kriteria belum cukup untuk mulai |
| READY | Tugas jelas dan dependency awal terpenuhi |
| IN_PROGRESS | Pekerjaan berlangsung; branch/checkpoint tercatat |
| BLOCKED | Ada dependency nyata; tulis kebutuhan pemulihan |
| IN_REVIEW | Draft/final PR sedang diperiksa |
| READY_TO_MERGE | Pemeriksaan selesai; syarat otorisasi/proteksi dievaluasi |
| DONE | Output terintegrasi dan penutupan diverifikasi |
| CANCELLED | Dibatalkan dengan alasan; bukan selesai akademik |

Jangan menandai DONE ketika hanya selesai menulis, push branch, atau membuka PR. Label bukan bukti pelaksanaan. GitHub issue yang ditutup karena dibatalkan tidak disebut hasil penelitian selesai.

## Pembaruan yang tahan pergantian sesi

Perbarui snapshot body dengan keadaan terbaru dan tambahkan komentar [checkpoint](../templates/session-checkpoint.md) pada akhir sesi, sebelum compaction yang diketahui, setelah keputusan besar, saat blocker, dan sebelum/selepas review atau merge. Simpan progres sebelum batas konteks terasa kritis; jangan mengandalkan agent akan selalu menerima peringatan.

Komentar mencatat perubahan sejak checkpoint sebelumnya, keputusan dan alasannya, bukti/commit, apa yang belum diperiksa, dan langkah lanjutan. Jangan membanjiri issue dengan log setiap tool.

## Menutup dan membuka kembali

Untuk issue keluaran, gunakan closing keyword hanya pada PR yang benar-benar memenuhi seluruh kriteria. Jika masih ada pekerjaan wajib dalam scope, issue tetap terbuka. Memindahkannya ke child issue tidak otomatis membuat scope lama selesai; jelaskan dan sepakati perubahan scope.

Bila kesalahan ditemukan setelah penutupan, buka kembali issue atau buat issue koreksi yang tertaut, dengan bukti serta dampak terhadap gate/naskah. Jangan menghapus komentar kritik.
