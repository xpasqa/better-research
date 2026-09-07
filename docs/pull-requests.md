# PR, review, dan integrasi output final

Pada proyek disertasi (mode RESEARCH), setiap perubahan berkas menuju main wajib melalui Pull Request. PR adalah paket keluaran yang dapat ditinjau; issue menyimpan kebutuhan dan konteks. Jangan menganggap push branch sudah mengintegrasikan hasil final. Pemeliharaan repositori induk TEMPLATE mengikuti pengecualian pada [workflow Git](git-workflow.md).

## Membuat PR

- Buat branch `issue-<nomor>-<ringkasan>` dan commit yang menyebut issue. Verifikasi owner/repo dan base/head sebelum membuka PR.
- Buka draft PR setelah ada perubahan bermakna. Gunakan [template PR](../.github/pull_request_template.md).
- Cantumkan masalah, perilaku/hasil sebelum–sesudah, scope final, file kanonik, bukti, perubahan keputusan, pemeriksaan aktual, keterbatasan, dan checklist penerimaan.
- Satu PR dapat menyelesaikan satu bagian dari issue; gunakan `Refs #<nomor>` bila belum menyelesaikan keseluruhan.
- Gunakan `Closes #<nomor>` hanya pada PR final yang menyelesaikan semua kriteria issue terkait. Jangan memasukkannya untuk parent issue yang masih memiliki pekerjaan.
- Base akhir adalah main (atau default branch proyek yang sudah diverifikasi). Jangan menaruh closing keyword hanya di komentar lalu mengasumsikan issue akan tertutup otomatis.

GitHub menafsirkan closing keyword pada deskripsi PR yang menargetkan default branch; merge ke default branch dapat menutup issue terkait. Tetap periksa keadaan aktual sesudah merge. Lihat [dokumentasi GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

## Review sebelum merge

1. Cocokkan output dengan issue dan checklist. Jika scope berubah, perbarui issue dan deskripsi PR secara terbuka.
2. Periksa isi perubahan, sumber/batas klaim, konsistensi naskah, data rahasia, dan aturan yang terdampak.
3. Jalankan pemeriksaan sesuai perubahan: tautan/frontmatter untuk dokumentasi dan skill; audit sitasi untuk literatur; pemeriksaan analisis untuk hasil; render untuk ekspor.
4. Catat reviewer/peran, versi HEAD yang diperiksa, temuan, dan tindakan koreksi. Review mandiri/agent tidak diklaim sebagai review manusia independen atau promotor.
5. Selesaikan temuan yang memengaruhi validitas, integritas, scope, atau keamanan. Perubahan baru setelah review harus diperiksa sesuai dampaknya.
6. Ubah draft menjadi ready hanya ketika tidak ada pekerjaan wajib yang belum selesai. Catat checkpoint READY_TO_MERGE.

## Merge dan otorisasi

Merge dilakukan hanya setelah review aktual, kriteria penerimaan terpenuhi, dan dalam otorisasi pengguna yang berlaku. Penyelesaian tugas hingga main yang diotorisasi pengguna memakai jalur PR ini; jangan meminta izin ulang jika otorisasi merge sudah jelas. Bila pengguna meminta berhenti pada draf, menunggu promotor, atau memberi persetujuan khusus, patuhi batas itu.

Skill atau checkbox tidak dapat memberi izin baru. Jangan menganggap persetujuan etik atau promotor tersedia dari label PR. Jangan menggunakan admin bypass untuk melewati review/proteksi wajib.

Pilih metode merge yang diizinkan repositori. Catat commit hasil aktual; jangan mengandalkan commit branch sama dengan commit hasil squash. Jika konflik muncul, selesaikan di branch dan ulangi pemeriksaan yang terdampak.

## Setelah merge

- Periksa PR berstatus MERGED dan commit hasil ada pada main.
- Pastikan issue final tertutup hanya bila semua kriteria terpenuhi; periksa child/parent dan tugas lanjutan.
- Tambahkan komentar penutupan: ringkasan hasil, PR/merge commit, validasi, batas, dan tautan tindak lanjut.
- Sinkronkan checkout secara aman. Jangan menandai gate akademik SIAP hanya karena PR merged.
- Issue yang memiliki PR parsial tetap terbuka sampai semua output yang disepakati selesai.

## Aturan tertulis dan enforcement server

Markdown menjelaskan kewajiban agent; tidak memblokir push di server dengan sendirinya. Branch protection/ruleset adalah lapisan enforcement terpisah, bergantung pada pengaturan dan fitur akun. Catat keadaan yang benar-benar diperiksa dan jangan mengklaim proteksi aktif hanya karena aturan ini ada.

Jika proteksi sudah ada, patuhi serta jangan melemahkannya. Konfigurasi baru harus mempertahankan aturan lama dan memperhitungkan reviewer yang tersedia; jangan mensyaratkan persetujuan diri sendiri sebagai review independen.
