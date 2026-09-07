# Tata kelola data

Belum ada data penelitian. Lengkapi [ethics/data plan](../templates/ethics-data-plan.md) sebelum memasukkan data.

Default boilerplate: data mentah, data olahan peserta, consent, dan linkage key tidak dilacak Git. Gunakan penyimpanan institusi yang disetujui; catat hanya dokumentasi non-sensitif dan ID versi aman di repositori.

Data publik/non-sensitif boleh dilacak hanya setelah hak penggunaan, risiko identifikasi, dan kebutuhan versioning diperiksa. Perubahan pengecualian harus dicatat dalam decision log.

Jangan menimpa data mentah. Dokumentasikan transformasi, codebook, unit, missing value, akses, dan provenance. Data sintetis untuk latihan harus diberi label dan disimpan terpisah dari data empiris.

.gitignore tidak menghapus data yang telanjur masuk riwayat; pemeriksaan sebelum commit tetap diperlukan.
