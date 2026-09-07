# Indeks skill lokal

Buka repositori ini sebagai proyek Codex. Skill disimpan bersama boilerplate, tanpa instalasi global atau ketergantungan plugin. Jika penemuan otomatis belum tersedia, baca SKILL.md melalui tautan berikut dan jalankan panduannya.

| Skill | Gunakan ketika | Keluaran |
|---|---|---|
| [dissertation-framing](../.agents/skills/dissertation-framing/SKILL.md) | Memperjelas masalah, pertanyaan, cakupan, kelayakan | Brief/problem memo dengan keputusan terbuka |
| [dissertation-evidence](../.agents/skills/dissertation-evidence/SKILL.md) | Merancang atau menjalankan penelusuran, seleksi, ekstraksi, appraisal | Protokol, log, source note, claim ledger |
| [dissertation-theory](../.agents/skills/dissertation-theory/SKILL.md) | Mensintesis perdebatan dan menguji kontribusi | Peta argumen, penjelasan alternatif, audit novelty |
| [dissertation-design](../.agents/skills/dissertation-design/SKILL.md) | Menentukan desain, pengukuran, analisis, kesiapan | Design matrix, analysis/ethics plan |
| [dissertation-writing](../.agents/skills/dissertation-writing/SKILL.md) | Menyusun atau memperbaiki naskah berbasis bukti | Naskah dengan sitasi dan batas klaim |
| [dissertation-audit](../.agents/skills/dissertation-audit/SKILL.md) | Menilai mutu, kesiapan, atau persiapan ujian | Review berbasis lokasi/bukti dan tindak lanjut |

Skill dapat dipanggil dengan nama, misalnya `$dissertation-evidence`. Skill ini tidak melakukan pencarian, mengakses database, atau menilai naskah sebelum dijalankan dalam suatu tugas.

## Kombinasi dan batas

Pilih skill utama sesuai keluaran; baca skill tambahan hanya untuk kebutuhan nyata. Alur umum: framing → evidence → theory → design → writing → audit, dengan iterasi bila bukti mengubah keputusan.

Skill dokumen/PDF/spreadsheet dari lingkungan boleh digunakan untuk artefak yang memerlukannya. Skill deep-research atau konektor ilmiah, jika tersedia dan sesuai permintaan, melengkapi akses; hasilnya tetap melalui verifikasi dan appraisal proyek.

Jika tool/sumber tidak tersedia, laporkan batas akses dan lanjutkan bagian yang dapat dikerjakan. Jangan mengklaim pencarian di Scopus, Web of Science, atau basis data lain yang tidak benar-benar diakses.
