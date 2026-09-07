# Melanjutkan pekerjaan ketika konteks AI terbatas

Percakapan tidak menjadi satu-satunya penyimpan keadaan. Gunakan tiga lapis: snapshot issue yang singkat, komentar checkpoint sebagai riwayat, dan berkas/commit sebagai bukti.

Panduan ini untuk mode RESEARCH. Pemeliharaan TEMPLATE atas instruksi langsung pengguna dapat dilanjutkan dari berkas dan riwayat Git tanpa issue, sesuai [workflow Git](git-workflow.md).

## Memulai atau melanjutkan sesi

1. Baca AGENTS.md, brief, status, dan owner/repo aktif. Periksa checkout agar tidak berpindah ke repositori sumber.
2. Baca issue aktif: snapshot, scope, checklist, checkpoint terakhir, dependency, dan keputusan yang masih berlaku.
3. Baca PR tertaut, perubahan setelah checkpoint, review terbuka, serta branch/commit aktual. Fetch/status diperlukan untuk melihat perubahan dari sesi lain; jangan checkout/menimpa pekerjaan lokal secara paksa.
4. Buka hanya bukti dan skill yang diperlukan. Issue panjang dibaca bertahap; ambil komentar lebih lama bila snapshot/tautan belum menjawab kebutuhan.
5. Ringkas posisi saat ini dan langkah berikutnya. Jika body, komentar, dan Git berbeda, periksa timestamp dan bukti aktual, rekonsiliasi di issue, lalu lanjutkan. Jangan memilih versi yang paling nyaman.
6. Jalankan tugas dalam scope dan simpan checkpoint pada titik penting.

## Isi checkpoint

Gunakan [template checkpoint](../templates/session-checkpoint.md). Cantumkan:

- Waktu, issue, repo, branch, HEAD, dan PR.
- Apa yang selesai sejak checkpoint sebelumnya serta artefak/commit.
- Keputusan, alasan, dan opsi yang ditolak.
- Pemeriksaan aktual, keterbatasan, serta review yang belum dijawab.
- Perubahan lokal belum commit/push beserta lokasi penyimpanan aman.
- Blocker/dependency dan siapa atau apa yang dibutuhkan.
- Langkah berikutnya yang dapat langsung dikerjakan.
- Batas otorisasi yang relevan; jangan menyimpan rahasia.

Usahakan ringkasan mudah dibaca dalam satu layar; rincian panjang ditautkan. Ini pedoman keterbacaan, bukan alasan membuang keputusan atau bukti penting.

## Sinkronisasi

Issue menyimpan status delivery dan koordinasi. research/status.md menyimpan tahap serta gate akademik, dengan tautan issue aktif bila relevan. Jangan membuat dua daftar status delivery manual yang saling bersaing; setelah merge, bukti penutupan ada di issue/PR.

Keputusan ilmiah tetap berada di decision/deviation log dan ditautkan dari issue. Bibliografi, claim ledger, naskah dan analisis tetap kanonik di berkas, bukan disalin seluruhnya ke komentar.

Jika GitHub sedang gagal, simpan checkpoint sementara pada berkas lokal yang aman dan jelas lokasinya; sinkronkan ke issue ketika pulih sebelum melanjutkan pekerjaan substantif baru. Jangan menyatakan checkpoint sudah tersimpan jarak jauh hanya karena berkas lokal dibuat.

## Handoff selesai bila

Sesi baru dapat menjawab: apa tujuan, apa yang sudah dilakukan, apa dasar keputusannya, versi mana yang aktif, apa yang belum selesai, dan tindakan berikutnya. Uji dengan membaca issue dan berkas tertaut tanpa mengandalkan percakapan.
