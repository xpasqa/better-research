---
name: dissertation-workflow
description: Kelola issue wajib, checkpoint lintas sesi, branch, PR, review, dan penutupan output proyek disertasi agar konteks dapat dipulihkan.
---

# Koordinasi pekerjaan dan konteks

Gunakan ketika mulai/melanjutkan pekerjaan proyek, menyimpan handoff, atau menyiapkan output untuk merge. Baca [workflow Git](../../../docs/git-workflow.md) dan panduan yang relevan: [issue](../../../docs/issues.md), [sesi](../../../docs/session-continuity.md), atau [PR](../../../docs/pull-requests.md).

Periksa mode pada project brief terlebih dahulu. Pemeliharaan repositori induk TEMPLATE yang diminta pengguna boleh langsung diperbaiki dan disimpan tanpa issue/PR, setelah pemeriksaan. Untuk proyek hasil salinan, tetapkan RESEARCH saat provisioning; semua ketentuan issue/PR di bawah berlaku. Jangan mengganti mode untuk melewati alur penelitian.

## Invarian

- Pilih/buat issue sebelum pekerjaan substantif. Jangan membuat issue duplikat untuk kelanjutan tugas yang sama.
- Verifikasi origin dan nama kanonik GitHub; gunakan owner/repo eksplisit untuk operasi eksternal, jangan mengikuti upstream sumber.
- Semua perubahan berkas menuju main melalui branch dan PR; tidak ada bypass untuk dokumentasi atau bootstrap lanjutan.
- Issue menyimpan konteks delivery; artefak tetap kanonik di berkas. Ringkas informasi terbaru dan tautkan rincian agar issue panjang tidak menghabiskan seluruh konteks.
- Review/merge harus benar-benar terjadi dan mengikuti otorisasi serta proteksi yang berlaku. Jangan menyatakan output final terintegrasi hanya karena branch sudah di-push.

## Langkah kerja

1. Baca issue, checkpoint terakhir, keputusan, PR/review dan keadaan Git; rekonsiliasi bila berbeda.
2. Tentukan scope, penerimaan, dependency, branch dan skill akademik yang diperlukan. Ketidakjelasan dicatat sebelum mengambil keputusan yang bergantung padanya.
3. Kerjakan bagian yang diotorisasi; simpan [checkpoint](../../../templates/session-checkpoint.md) pada akhir sesi, perubahan keputusan, blocker, dan transisi review.
4. Siapkan draft PR dengan bukti dan batas. Gunakan Refs untuk pekerjaan parsial; Closes hanya bila seluruh issue terpenuhi.
5. Periksa output dan temuan review; lanjutkan merge hanya dalam otorisasi yang berlaku.
6. Verifikasi PR merged, commit main, status issue dan komentar penutupan. Bedakan delivery selesai dari gate akademik.

Jika GitHub tidak tersedia, simpan draft/checkpoint lokal BELUM TERSINKRON dan laporkan batasnya. Jangan berpura-pura mempunyai issue atau PR. Pertanyaan klarifikasi/status masuk issue aktif; tugas baca yang menghasilkan keputusan proyek memiliki issue dan memo yang diintegrasikan melalui PR.
