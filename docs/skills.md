# Indeks skill lokal

Buka repositori ini sebagai proyek Codex. Skill disimpan bersama boilerplate, tanpa instalasi global atau ketergantungan plugin. Jika penemuan otomatis belum tersedia, baca SKILL.md melalui tautan berikut dan jalankan panduannya.

| Skill | Gunakan ketika | Keluaran |
|---|---|---|
| [research-workflow](../.agents/skills/research-workflow/SKILL.md) | Memulai/melanjutkan issue, menyimpan konteks, menyiapkan PR dan penutupan | Issue, checkpoint, branch/PR dan jejak integrasi |
| [research-rigor](../.agents/skills/research-rigor/SKILL.md) | Menetapkan guardrail lintas tahap untuk asumsi, parsimoni, scope, falsifikasi, dan verification | Success criteria, batas scope, status pass/blocked, jejak keputusan |
| [research-framing](../.agents/skills/research-framing/SKILL.md) | Memperjelas masalah, pertanyaan, cakupan, kelayakan | Brief/problem memo dengan keputusan terbuka |
| [research-evidence](../.agents/skills/research-evidence/SKILL.md) | Merancang atau menjalankan penelusuran, seleksi, ekstraksi, appraisal | Protokol, log, source note, claim ledger |
| [research-theory](../.agents/skills/research-theory/SKILL.md) | Mensintesis perdebatan dan menguji kontribusi | Peta argumen, penjelasan alternatif, audit novelty |
| [research-design](../.agents/skills/research-design/SKILL.md) | Menentukan desain, pengukuran, analisis, kesiapan | Design matrix, analysis/ethics plan |
| [research-writing](../.agents/skills/research-writing/SKILL.md) | Menyusun atau memperbaiki naskah berbasis bukti | Naskah dengan sitasi dan batas klaim |
| [research-audit](../.agents/skills/research-audit/SKILL.md) | Menilai mutu, kesiapan, atau persiapan ujian | Review berbasis lokasi/bukti dan tindak lanjut |

Skill dapat dipanggil dengan nama, misalnya `$research-evidence`. Skill ini tidak melakukan pencarian, mengakses database, atau menilai naskah sebelum dijalankan dalam suatu tugas.

## Kombinasi dan batas

Gunakan workflow untuk koordinasi, terapkan research-rigor sebagai disiplin lintas tahap, dan pilih skill akademik sesuai keluaran. Alur akademik: framing → evidence → theory → design → writing → audit, dengan iterasi bila bukti mengubah keputusan. Jangan memuat semua skill sekaligus; baca hanya tahap yang diperlukan.

Skill dokumen/PDF/spreadsheet dari lingkungan boleh digunakan untuk artefak yang memerlukannya. Skill deep-research atau konektor ilmiah, jika tersedia dan sesuai permintaan, melengkapi akses; hasilnya tetap melalui verifikasi dan appraisal proyek.

Jika tool/sumber tidak tersedia, laporkan batas akses dan lanjutkan bagian yang dapat dikerjakan. Jangan mengklaim pencarian di Scopus, Web of Science, atau basis data lain yang tidak benar-benar diakses.
