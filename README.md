# Publion Disertasi Builder

**Boilerplate untuk merancang, menjalankan, menulis, dan meninjau riset tingkat doktoral dengan bantuan AI.**

Builder ini menyediakan aturan akademik, enam skill, 13 formulir kerja, dan pemeriksaan kesiapan riset. Peneliti menggunakannya untuk menjaga hubungan antara masalah, literatur, teori, metode, bukti, dan kontribusi disertasi.

Status: **builder siap digunakan; penelitian belum dimulai**. Topik, kampus, paradigma, metode, dan data ditetapkan pada masing-masing proyek. Keputusan akademik dan pertanggungjawaban naskah tetap berada pada peneliti.

## 1. Persiapan

Siapkan informasi yang sudah tersedia:

- Bidang/program doktor, pedoman kampus, dan arahan promotor.
- Topik atau masalah awal; boleh belum mempunyai judul final.
- Kemungkinan akses literatur, data, peserta, atau corpus penelitian.
- Batas waktu, sumber daya, serta kebijakan kampus tentang AI dan etika.

Informasi yang belum diketahui tetap ditandai `BELUM DIISI` atau `BELUM DIVERIFIKASI`. Builder membantu memperjelasnya secara bertahap.

## 2. Memulai workspace

### Untuk penelitian baru

Gunakan satu repositori terpisah untuk setiap disertasi. Salin **isi versi aktif builder** ke repositori penelitian baru, kemudian isi identitas proyek. Repositori induk Publion Disertasi Builder digunakan untuk mengembangkan aturan dan template yang dapat dipakai ulang.

Contoh instruksi kepada agent:

> Buat repositori private baru bernama [nama-proyek] di akun saya, menggunakan isi versi aktif Publion Disertasi Builder. Sertakan folder tersembunyi .agents dan .github. Mulai riwayat Git baru, atur origin ke repositori baru, dan jangan mengubah repositori builder. Biarkan topik dan metode kosong sampai saya memberikan informasi.

Ganti `[nama-proyek]` dengan nama yang diinginkan. Instruksi ini baru dijalankan saat diberikan kepada agent; README tidak membuat repositori otomatis.

### Untuk membuka atau mengembangkan builder

Clone repositori ini, lalu buka folder hasil clone sebagai proyek Codex:

```sh
git clone https://github.com/xpasqa/publion-disertasi-builder.git
cd publion-disertasi-builder
```

Repositori memerlukan hak akses GitHub yang sesuai. Clone mempertahankan riwayat Git; gunakan salinan isi versi aktif dengan riwayat baru jika menyiapkan proyek penelitian yang independen.

Di lingkungan agent lain, arahkan agent untuk membaca [AGENTS.md](AGENTS.md) dan SKILL.md yang relevan secara eksplisit. Kemampuan pencarian dan pengelolaan berkas mengikuti alat yang tersedia.

## 3. Sesi pertama

Berikan instruksi berikut di workspace penelitian:

> Baca AGENTS.md, research/project-brief.md, dan research/status.md. Gunakan dissertation-framing untuk membantu saya mengisi brief. Mulai dari masalah dan informasi yang saya miliki. Jangan menebak pedoman kampus, memilih metode, atau mengklaim novelty sebelum ada dasar. Catat keputusan dan informasi yang masih dibutuhkan.

Isi [project brief](research/project-brief.md) bersama agent. Tetapkan tahap aktif di [status penelitian](research/status.md). Untuk mulai menulis bagian tertentu, jelaskan keluaran yang diminta dan bahan yang tersedia.

## 4. Alur penggunaan

| Langkah | Yang dilakukan | Keluaran utama |
|---|---|---|
| Rumuskan masalah | Perjelas fenomena, masalah pengetahuan, pertanyaan, dan batas penelitian | Brief dan problem memo |
| Petakan literatur | Kenali konsep, istilah, sumber utama, dan perdebatan | Peta awal dan kandidat arah penelitian |
| Susun protokol | Tentukan bentuk review, pencarian, seleksi, appraisal, serta sintesis | Review protocol |
| Kumpulkan dan nilai bukti | Jalankan pencarian, baca sumber, catat seleksi dan keterbatasan | Search log, source notes, claim ledger |
| Uji teori dan kontribusi | Bandingkan studi terdekat dan penjelasan alternatif | Audit kandidat kontribusi |
| Rancang penelitian | Selaraskan pertanyaan, bukti, metode, kelayakan, dan etika | Design matrix serta analysis/data plan |
| Laksanakan dan analisis | Jalankan kegiatan yang syaratnya telah terpenuhi; catat hasil dan perubahan | Jejak pelaksanaan, analisis, deviation log |
| Tulis dan tinjau | Bangun argumen dari bukti, periksa konsistensi, dan tanggapi kritik | Naskah, review, serta ekspor yang diperiksa |

Tahap boleh diulang ketika bukti mengubah keputusan. Draf dapat ditulis sepanjang proses. Kelengkapan draf tidak otomatis membuat tahap riset selesai. Detail ada di [alur riset](docs/research-workflow.md).

## 5. Memilih skill

| Skill | Kapan digunakan | Contoh instruksi |
|---|---|---|
| `dissertation-framing` | Masalah dan pertanyaan belum tajam | “Perjelas masalah dari brief; bandingkan alternatif dan kelayakannya.” |
| `dissertation-evidence` | Menyiapkan atau menjalankan review literatur | “Susun protokol review dahulu. Catat batas akses; jangan mulai pencarian sebelum protokol dibahas.” |
| `dissertation-theory` | Mensintesis teori dan menilai kontribusi | “Uji kandidat novelty terhadap studi terdekat dan bukti yang dapat membantahnya.” |
| `dissertation-design` | Memilih desain atau menyiapkan analisis | “Bandingkan desain berdasarkan pertanyaan, akses data, asumsi, dan batas inferensi.” |
| `dissertation-writing` | Menyusun atau memperbaiki naskah | “Revisi bagian ini memakai sumber terverifikasi; tandai klaim yang belum didukung.” |
| `dissertation-audit` | Memeriksa kesiapan atau berlatih ujian | “Audit G1–G4 dari berkas yang tersedia; tunjukkan bukti, kekurangan, dan prioritas revisi.” |

Skill disimpan di `.agents/skills/`; tautan lengkap ada di [indeks skill](docs/skills.md). Dalam Codex yang mendukungnya, gunakan nama skill atau panggilan seperti `$dissertation-evidence`. Jika belum muncul, buka ulang sesi atau minta agent membaca jalur SKILL.md terkait.

Skill tidak memasang konektor, menyediakan langganan basis data, atau menjalankan pekerjaan tanpa permintaan. Jika akses sumber terbatas, keluaran harus menyebutkan batas tersebut.

## 6. Aturan main akademik

1. **Mulai dari pertanyaan dan bukti.** Pilih teori, metode, dan susunan bab berdasarkan kebutuhan penelitian.
2. **Jangan mengarang.** Larangan mencakup referensi, data, kutipan, halaman, hasil, izin, maupun kegiatan yang belum dilakukan.
3. **Verifikasi dukungan sumber.** Catat apa yang benar-benar dibaca dan bagian yang mendukung klaim; keberadaan DOI saja tidak cukup.
4. **Cari bukti tandingan.** Laporkan hasil nol, kontradiksi, penjelasan alternatif, dan keterbatasan secara proporsional.
5. **Jaga integritas penulisan.** Bedakan kutipan, parafrasa, terjemahan, dan interpretasi; berikan atribusi yang tepat.
6. **Lindungi peserta dan data.** Simpan data sensitif di luar Git dan periksa izin sebelum kegiatan lapangan atau penggunaan layanan eksternal.
7. **Catat perubahan dan penggunaan AI.** Keputusan, penyimpangan protokol, dan bantuan AI harus dapat ditelusuri. Jangan mengaku ada pemeriksaan manusia yang belum terjadi.
8. **Gunakan standar sesuai ruang berlakunya.** Pedoman kampus perlu diverifikasi; APA 7 merupakan pilihan sitasi sementara. PRISMA, JBI, SRQR, dan JARS dipilih sesuai tujuan, disiplin, dan desain.
9. **Nyatakan status secara jujur.** Dokumen protokol yang siap tidak membuktikan pilot, pengumpulan data, analisis, atau persetujuan etik telah selesai.

Baca [aturan agent](AGENTS.md), [integritas akademik](docs/academic-integrity.md), dan [register standar](docs/standards.md) untuk rincian. Builder tidak menggantikan arahan promotor atau persetujuan institusi.

## 7. Menyimpan pekerjaan dan memeriksa kesiapan

Salin formulir dari [templates/](templates/README.md) ke lokasi kerja saat diperlukan. Isi dengan informasi nyata; tabel kosong tidak perlu diisi dengan data contoh.

Di akhir setiap pekerjaan, minta agent:

- Menunjukkan berkas yang berubah, sumber yang diperiksa, dan batas pemeriksaan.
- Mencatat keputusan substantif serta perubahan protokol jika ada.
- Memperbarui status berdasarkan bukti kegiatan aktual.
- Memeriksa perubahan dan menyimpannya ke Git dalam cakupan yang sudah diotorisasi.

Gunakan [workflow Git](docs/git-workflow.md) untuk branch, commit, dan review. Untuk revisi substantif yang memerlukan peninjauan, siapkan PR dengan alasan perubahan dan bukti yang diperiksa.

| Gate | Yang dinilai |
|---|---|
| G0 | Konteks dan mandat penelitian |
| G1 | Masalah dan pertanyaan |
| G2 | Protokol dan bukti literatur |
| G3 | Teori dan kontribusi |
| G4 | Desain penelitian |
| G5 | Kesiapan pelaksanaan |
| G6 | Hasil dan interpretasi |
| G7 | Naskah dan kesiapan ujian |

Statusnya: `BELUM DINILAI`, `PERLU REVISI`, `SIAP`, atau `TIDAK BERLAKU` dengan alasan. Gunakan [kriteria mutu](docs/quality-gates.md) dan [template audit](templates/gate-review.md). Penilaian agent tidak sama dengan persetujuan promotor atau komite etik.

## 8. Peta berkas

| Lokasi | Fungsi |
|---|---|
| [AGENTS.md](AGENTS.md) | Aturan utama; AGENT.md hanya pengarah kompatibilitas |
| [docs/](docs/research-workflow.md) | Panduan proses, integritas, standar, skill, dan Git |
| [.agents/skills/](docs/skills.md) | Enam skill lokal |
| [research/](research/project-brief.md) | Brief, status, keputusan, deviasi, dan catatan penggunaan AI |
| [templates/](templates/README.md) | 13 formulir kerja |
| [literature/](literature/README.md) | Metadata terverifikasi, catatan sumber, dan jejak bukti |
| [manuscript/](manuscript/README.md) | Naskah Markdown kanonik |
| [data/](data/README.md) | Dokumentasi tata kelola data |
| [analysis/](analysis/README.md) | Rencana dan jejak analisis |
| [reviews/](reviews/README.md) | Review akademik dan tanggapannya |
| [exports/](exports/README.md) | Hasil ekspor beserta versi sumber dan pemeriksaannya |

## 9. Melanjutkan pekerjaan pada sesi berikutnya

> Baca AGENTS.md, project brief, status penelitian, serta keputusan terakhir yang relevan. Ringkas pekerjaan yang sudah selesai dan bukti yang masih kurang. Lanjutkan tugas [sebutkan tugas] dengan skill yang sesuai. Jangan mengulang tahap yang sudah selesai tanpa alasan baru.

Ganti bagian dalam kurung siku dengan tugas konkret. Untuk masalah yang belum terselesaikan, jelaskan informasi atau bukti yang diperlukan agar pekerjaan dapat dilanjutkan.

## 10. Batas versi awal

Builder menyediakan panduan dan formulir; belum ada pipeline ekspor, otomatisasi audit sitasi, atau analisis statistik siap pakai. Pemeriksaan format dan tautan tidak membuktikan mutu keputusan riset. Peneliti perlu meninjau hasil agent dan menyesuaikan proyek dengan ketentuan institusi.

Lihat [catatan pemeriksaan boilerplate](reviews/2026-09-07-boilerplate-check.md) untuk cakupan validasi awal.
