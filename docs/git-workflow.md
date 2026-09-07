# Issue → Branch → PR → Review → Merge

**Pada proyek disertasi (mode RESEARCH), setiap pekerjaan wajib memiliki GitHub Issue dan setiap perubahan berkas ke main wajib melalui PR yang diperiksa.** Ini mencakup riset, penulisan, review, dokumentasi, skill, dan perbaikan kecil dalam proyek penelitian.

**Pada repositori induk (mode TEMPLATE), pemeliharaan builder yang diminta langsung pengguna boleh dikerjakan, diperiksa, di-commit, dan di-push tanpa issue/PR.** Mode tercatat dalam project brief. Pengecualian ini tidak berlaku pada hasil salinan yang digunakan untuk disertasi; jangan mengubah mode untuk melewati aturan penelitian. Bagian selanjutnya menjelaskan alur mode RESEARCH.

## Fungsi setiap tempat

| Tempat | Sumber utama untuk |
|---|---|
| Issue | Tujuan, konteks, kriteria penerimaan, keputusan, ketergantungan, checkpoint, dan langkah berikutnya |
| Branch/commit | Versi pekerjaan yang dapat dipulihkan |
| PR | Perubahan final, bukti pemeriksaan, komentar review, dan integrasi ke main |
| Berkas proyek | Naskah, bukti terstruktur, protokol, dan catatan penelitian kanonik |
| Percakapan AI | Interaksi sementara; keputusan penting dipindahkan ke issue/berkas |

Issue adalah memori kerja lintas sesi, bukan tempat menyimpan seluruh PDF, data pribadi, atau transkrip percakapan. Ringkas keadaan terbaru di bagian atas issue, pertahankan riwayat keputusan di komentar, dan tautkan artefak yang tepat.

## Urutan wajib

1. **Pastikan repositori benar.** Periksa origin dan nama kanonik GitHub. Jangan memilih upstream sumber. Pada operasi GitHub, gunakan owner/repo eksplisit; setelah rename, periksa redirect dan tujuan aktual sebelum menulis.
2. **Temukan atau buat issue.** Baca body, checkpoint terakhir, komentar relevan, serta PR tertaut. Jangan menduplikasi pekerjaan yang sudah tercakup. Isi scope dan kriteria penerimaan sebelum mulai kerja substantif.
3. **Buat/lanjutkan branch dari main mutakhir:** `issue-<nomor>-<ringkasan>`. Untuk dependensi branch lain, jelaskan base sementara dan ubah target final ke main saat siap.
4. **Kerjakan dalam scope.** Cantumkan `Refs #<nomor>` dalam commit. Simpan checkpoint pada perubahan keputusan, akhir sesi, blocker, atau sebelum pergantian konteks.
5. **Buka draft PR setelah ada perubahan yang dapat ditinjau.** Tautkan issue dan perbarui deskripsi agar mewakili hasil terkini. PR kosong tidak diperlukan.
6. **Periksa dan revisi.** Lengkapi kriteria penerimaan, pemeriksaan akademik yang relevan, tautan, dan keamanan data. Bedakan review agent, review manusia, serta persetujuan institusi.
7. **Merge melalui PR dalam otorisasi pengguna.** Otorisasi menyelesaikan pekerjaan hingga main mencakup merge melalui PR setelah pemeriksaan; permintaan draf saja atau permintaan menunggu review tidak mencakup merge. Hormati persetujuan khusus yang diminta pengguna dan proteksi server; jangan melewati keduanya.
8. **Verifikasi hasil aktual.** Periksa PR benar-benar MERGED, commit tersedia di main, dan status issue sesuai penerimaan. Catat ringkasan penutupan di issue; sinkronkan checkout tanpa menimpa perubahan lokal.

Penyusunan issue, checkpoint, dan draft PR merupakan bagian pekerjaan yang telah diminta; jangan meminta izin ulang untuk setiap langkah tersebut. Menghubungi peserta atau mengirim pesan ke pihak lain tetap mengikuti otorisasi yang sesuai.

## Batas dan kondisi khusus

- Pertanyaan klarifikasi/status dalam pekerjaan berjalan ditautkan ke issue aktif, tidak memerlukan issue baru. Tugas baru yang menghasilkan keputusan/analisis proyek tetap memerlukan issue.
- Hasil pekerjaan baca/review yang menjadi keluaran proyek disimpan sebagai memo lalu masuk melalui PR. Jika issue hanya koordinasi dan tidak menghasilkan perubahan berkas, tutup dengan alasan serta tautan bukti; tidak boleh digunakan untuk menyelundupkan perubahan ke main.
- Jika GitHub tidak tersedia, simpan draft/checkpoint lokal berstatus BELUM TERSINKRON. Jangan mengaku issue sudah dibuat, melakukan pekerjaan substantif baru tanpa issue, atau melewati PR. Boleh menjaga hasil yang sedang berjalan, memeriksa keadaan, dan menyiapkan informasi untuk pemulihan.
- Jangan menulis ulang keputusan lama agar sejarah tampak konsisten. Catat keputusan pengganti, alasan, dan dampaknya.
- Membuat repositori baru boleh menyalin snapshot awal builder sesuai permintaan pengguna dan menetapkan mode RESEARCH sebagai bagian provisioning. Setelah itu, kustomisasi brief dan hasil penelitian mengikuti issue/PR wajib.
- Jangan force-push, menghapus riwayat, atau memakai admin bypass untuk melewati pemeriksaan.

Panduan rinci: [issue](issues.md), [kesinambungan sesi](session-continuity.md), [PR dan merge](pull-requests.md).

## Definisi selesai

Untuk keluaran berkas: kriteria issue terpenuhi, review aktual dicatat, PR merged ke main, hasil diverifikasi, dan penutupan issue memiliki bukti. Selesai secara delivery tidak berarti gate akademik lulus atau penelitian lapangan sudah dilakukan.
