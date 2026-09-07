# Better Research

> **Jangan meminta AI mengingat seluruh riset Anda. Bangun sistem yang membuat konteks riset selalu dapat dipulihkan.**

**Better Research** adalah workspace berbasis Git untuk merancang, menjalankan, menulis, dan mengaudit penelitian dengan bantuan AI tanpa menjadikan percakapan AI sebagai satu-satunya memori kerja.

AI dapat membaca banyak dokumen, tetapi context window tetap terbatas. Penelitian berlangsung berbulan-bulan atau bertahun-tahun, melibatkan banyak sumber, keputusan, revisi, data, kritik, dan perubahan arah. Jika seluruh konteks hanya hidup di chat, cepat atau lambat sebagian konteks akan hilang, tercampur, atau direkonstruksi secara keliru.

Better Research mengubah masalah itu menjadi workflow yang dapat diaudit:

```text
Pertanyaan / masalah
        ↓
GitHub Issue
(bounded context + acceptance criteria)
        ↓
Branch
(perubahan terbatas pada satu tugas)
        ↓
Evidence / analysis / writing
        ↓
Pull Request
(diff + verification + review)
        ↓
Merge ke main
        ↓
Checkpoint + quality gate
```

**Chat bersifat sementara. Issue menyimpan konteks kerja. File menyimpan pengetahuan. Git menyimpan perubahan. PR mengintegrasikan hasil.**

Repositori ini adalah **builder/template induk**. Status awalnya: **siap digunakan; penelitian belum dimulai**.

---

## Mengapa Better Research ada?

Masalah utama penggunaan AI dalam riset bukan hanya "hallucination". Masalah yang lebih sistemik adalah **context drift**.

Dalam proyek besar, AI dapat:

- lupa keputusan dari sesi sebelumnya;
- membaca sumber yang berbeda pada waktu berbeda lalu mencampur konteks;
- mengubah teori, variabel, metode, atau terminologi tanpa menyadari konsekuensinya;
- memperkuat klaim hanya karena terdengar masuk akal;
- menambah kompleksitas yang tidak diperlukan;
- menulis ulang banyak bagian ketika sebenarnya hanya satu argumen yang perlu diperbaiki;
- menyatakan pekerjaan "selesai" meskipun bukti, review, atau gate akademiknya belum terpenuhi.

Better Research tidak mencoba mengatasi semua itu dengan prompt yang semakin panjang.

Ia mengubah **arsitektur kerja**.

Satu tugas mempunyai konteks lokal yang jelas. Satu perubahan mempunyai alasan. Satu klaim mempunyai jalur ke bukti. Satu keputusan mempunyai riwayat. Satu output masuk ke `main` hanya setelah dapat diperiksa.

---

## Prinsip inti

### 1. Issue adalah bounded context

Setiap pekerjaan substantif pada workspace **RESEARCH** dimulai dari GitHub Issue.

Issue menyimpan:

- objective;
- konteks yang diperlukan untuk sesi baru;
- apa yang sudah diketahui dan belum diketahui;
- scope dan out-of-scope;
- bukti yang harus diperiksa;
- acceptance criteria;
- keputusan;
- blocker;
- checkpoint;
- branch, commit, dan PR terkait.

Agent tidak perlu memuat seluruh penelitian ke dalam context window. Ia cukup membaca konteks yang relevan untuk issue aktif, kemudian membuka artefak yang diperlukan.

### 2. File adalah sumber pengetahuan kanonik

Penelitian tidak disimpan di chat.

Artefak utama ditulis sebagai file:

- brief dan keputusan di `research/`;
- jejak literatur dan bukti di `literature/`;
- analisis di `analysis/`;
- naskah di `manuscript/`;
- review di `reviews/`.

Markdown digunakan sebagai sumber utama agar mudah dibaca manusia, AI, Git diff, dan tool lain.

### 3. PR adalah mekanisme integrasi

Perubahan tidak langsung "ditelan" oleh dokumen final.

Agent mengerjakan perubahan pada branch, lalu membuat Pull Request. PR menunjukkan:

- apa yang berubah;
- mengapa berubah;
- issue mana yang diselesaikan;
- bukti apa yang diperiksa;
- acceptance criteria mana yang terpenuhi;
- apa yang masih belum terverifikasi.

Dengan begitu, perubahan kecil dapat diintegrasikan tanpa kehilangan coherence keseluruhan.

### 4. Evidence lebih penting daripada kelancaran bahasa

Kalimat akademik yang terdengar meyakinkan bukan bukti.

Better Research memaksa pemisahan antara:

- **KNOWN** — diketahui/diberikan;
- **SUPPORTED** — didukung bukti yang diperiksa;
- **INFERRED** — inferensi dengan alasan;
- **ASSUMED** — asumsi kerja;
- **UNKNOWN** — belum diketahui;
- **DECISION NEEDED** — membutuhkan keputusan atau bukti tambahan.

Jika bukti tidak cukup, status yang benar adalah `BELUM DIVERIFIKASI` atau `BLOCKED`, bukan paragraf yang lebih percaya diri.

---

# Quick Start

## Prasyarat

Minimal Anda perlu memahami:

- dasar Git dan GitHub;
- branch, commit, Issue, dan Pull Request;
- Markdown;
- cara memeriksa sumber akademik secara mandiri.

Better Research tidak menggantikan kemampuan metodologis, penilaian akademik, promotor, atau komite etik.

---

## 1. Buat satu repository untuk satu proyek penelitian

Jangan menjalankan beberapa penelitian substantif dalam satu workspace.

Untuk membuat proyek independen dari builder ini:

```bash
git clone https://github.com/xpasqa/better-research.git my-research
cd my-research

rm -rf .git
git init
git add .
git commit -m "chore: initialize research workspace"
git branch -M main
git remote add origin <URL-REPOSITORY-PRIVATE-ANDA>
git push -u origin main
```

Gunakan repository private bila proyek memerlukan privasi. Namun **repository private bukan izin untuk menyimpan data peserta atau data sensitif di Git**.

Pastikan folder tersembunyi `.agents/` dan `.github/` ikut tersalin.

---

## 2. Ubah workspace menjadi mode RESEARCH

Buka [`research/project-brief.md`](research/project-brief.md).

Ubah:

```text
Mode workspace: TEMPLATE
```

menjadi:

```text
Mode workspace: RESEARCH
```

Mode mempunyai fungsi penting:

| Mode | Digunakan untuk | Aturan Git |
|---|---|---|
| `TEMPLATE` | Memelihara builder Better Research | Maintenance dapat dilakukan langsung sesuai instruksi pengguna |
| `RESEARCH` | Menjalankan proyek penelitian nyata | Issue + Branch + PR wajib untuk pekerjaan substantif |

Jangan mengganti mode untuk menghindari workflow penelitian.

---

## 3. Mulai sesi pertama

Berikan instruksi ini kepada agent:

> Baca AGENTS.md, research/project-brief.md, research/status.md, dan docs/skills.md. Verifikasi owner/repository yang sedang digunakan dan pastikan mode workspace RESEARCH. Gunakan research-workflow untuk mencari atau membuat issue inisialisasi project brief, lalu gunakan research-framing. Mulai hanya dari informasi dan sumber yang benar-benar tersedia. Jangan memilih metode, teori, variabel, atau mengklaim novelty tanpa dasar. Catat unknown, keputusan, acceptance criteria, dan checkpoint pada issue. Semua perubahan file masuk melalui branch dan Pull Request.

Kemudian isi [project brief](research/project-brief.md) secara bertahap.

Anda **tidak perlu** sudah mempunyai judul final, metode final, atau model konseptual final.

Yang belum diketahui boleh tetap:

```text
BELUM DIISI
BELUM DITETAPKAN
BELUM DIVERIFIKASI
```

Itu lebih baik daripada keputusan prematur.

---

# Cara bekerja sehari-hari

## Mental model sederhana

Setiap kali ingin mengerjakan sesuatu, jangan mulai dari:

> "AI, lanjutkan disertasi saya."

Mulailah dari unit kerja yang dapat diperiksa:

> "Apakah argumen theoretical gap pada bagian X benar-benar didukung sumber yang sudah dibaca?"

Kemudian jalankan:

```text
1. Temukan / buat Issue
2. Tentukan objective
3. Tentukan scope
4. Tentukan bukti yang diperlukan
5. Tentukan success criteria
6. Buat / lanjutkan branch
7. Kerjakan perubahan minimum
8. Verifikasi
9. Simpan checkpoint
10. Buka / perbarui PR
11. Review
12. Merge
13. Verifikasi main
14. Tutup issue bila seluruh acceptance criteria terpenuhi
```

Panduan lengkap: [Git workflow](docs/git-workflow.md).

---

## Contoh Issue yang baik

Misalnya Anda ingin menguji apakah sebuah moderator benar-benar diperlukan.

```markdown
## Objective

Menentukan apakah institutional trust layak dipertahankan
sebagai moderator hubungan X → Y.

## Known

- RQ2 saat ini memuat moderation.
- Tiga sumber membahas institutional trust.

## Unknown

- Apakah studi terdekat sudah menguji mekanisme yang sama.
- Apakah moderation diperlukan secara teoretis.
- Apakah desain/data mampu mengidentifikasi moderation.

## Scope

Termasuk:
- theory memo;
- source notes terkait;
- claim ledger;
- paragraf teori yang langsung terdampak.

Di luar scope:
- redesign seluruh metodologi;
- penambahan konstruk baru;
- rewrite bab lain.

## Success criteria

- [ ] Definisi konstruk diverifikasi.
- [ ] Studi terdekat dibandingkan.
- [ ] Bukti tandingan diperiksa.
- [ ] Penjelasan alternatif diperiksa.
- [ ] Keputusan retain / narrow / defer / reject dicatat.
```

Issue seperti ini memberi agent konteks yang cukup tanpa harus memasukkan seluruh penelitian ke satu percakapan.

Template resmi tersedia di [`.github/ISSUE_TEMPLATE/research-task.md`](.github/ISSUE_TEMPLATE/research-task.md).

---

# Delapan skill

Skill berada di [`.agents/skills/`](.agents/skills/) dan indeks lengkapnya ada di [`docs/skills.md`](docs/skills.md).

| Skill | Fungsi |
|---|---|
| `research-workflow` | Mengelola Issue, checkpoint, branch, PR, review, dan handoff lintas sesi |
| `research-rigor` | Guardrail lintas tahap: asumsi, parsimoni, scope, falsifikasi, dan verification |
| `research-framing` | Memperjelas masalah, pertanyaan penelitian, batas, dan kelayakan |
| `research-evidence` | Pencarian, screening, extraction, appraisal, source notes, dan claim tracking |
| `research-theory` | Sintesis teori, mekanisme, studi terdekat, penjelasan alternatif, dan kontribusi |
| `research-design` | Menyelaraskan pertanyaan, data, desain, analisis, etika, dan inferensi |
| `research-writing` | Menulis/revisi naskah berbasis bukti dan menjaga konsistensi antarbab |
| `research-audit` | Mengaudit kualitas, readiness, konsistensi, dan persiapan ujian |

Contoh pemanggilan:

```text
Gunakan research-evidence untuk memeriksa apakah claim CLM-014
benar-benar didukung oleh source notes yang tersedia.
```

atau, pada environment yang mendukung skill invocation:

```text
$research-evidence
```

Jangan memuat semua skill sekaligus. Gunakan skill yang sesuai dengan keluaran yang sedang dikerjakan.

---

# Research Rigor: agar AI tidak "terlihat pintar" tetapi salah arah

`research-rigor` diadaptasi dari prinsip eksekusi pada [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills), lalu ditulis ulang untuk konteks penelitian.

Lima prinsip utamanya:

### Think Before Claiming

Jangan mengubah ketidakpastian menjadi kepastian secara diam-diam.

Contoh kegagalan:

```text
sedikit hasil pencarian
        ↓
"ini research gap"
```

Yang benar:

```text
sedikit hasil pencarian
        ↓
cek query, database, sinonim, literatur berdekatan,
citation chasing, dan batas akses
        ↓
baru tentukan apa yang dapat diklaim
```

### Parsimony First

Kompleksitas bukan kualitas.

Jangan otomatis membuat:

```text
3 teori + 8 konstruk + 4 mediator + 2 moderator + SEM
```

jika pertanyaan dapat dijawab dengan desain yang lebih sederhana dan lebih defensible.

### Surgical Changes

Setiap perubahan substantif harus mempunyai alasan yang dapat ditelusuri ke:

- issue;
- bukti;
- keputusan;
- review finding;
- acceptance criterion.

Jika issue hanya meminta memperbaiki mekanisme antara A dan B, agent tidak boleh diam-diam mengganti sampel, metode, RQ, dan teori lain.

### Goal-Driven Research

Instruksi seperti:

> "Perbaiki literature review saya."

terlalu lemah.

Ubah menjadi tujuan yang dapat diperiksa:

```text
Goal:
Menentukan apakah literature review membangun
unresolved theoretical problem yang defensible.

Success criteria:
[ ] Konstruk utama didefinisikan.
[ ] Studi terdekat dibandingkan.
[ ] Bukti tandingan dimasukkan.
[ ] Klaim utama dapat dilacak ke sumber.
[ ] Unsupported claims dihapus atau ditandai.
[ ] Gap dinyatakan tanpa novelty inflation.
```

### Falsification Before Affirmation

Untuk klaim penting:

```text
candidate claim
   ↓
supporting evidence
   ↓
contradictory evidence
   ↓
alternative explanations
   ↓
boundary conditions
   ↓
claim strength
```

Agent tidak hanya mencari bukti yang mengonfirmasi model yang sudah disukai.

---

# Workflow akademik

Better Research tidak memaksa satu metode atau paradigma.

Urutan berikut adalah workflow keputusan, bukan struktur bab wajib:

| Tahap | Pertanyaan utama | Artefak |
|---|---|---|
| Konteks | Apa mandat, batas, sumber daya, dan ketidakpastian? | Project brief |
| Framing | Apa masalah pengetahuan yang benar-benar dapat diteliti? | Problem memo, RQ |
| Mapping | Konsep dan perdebatan apa yang relevan? | Literature map |
| Protocol | Bagaimana bukti akan dicari dan dinilai? | Review protocol |
| Evidence | Apa yang benar-benar dilaporkan sumber? | Search log, screening, source notes, claim ledger |
| Theory | Penjelasan mana yang bertahan terhadap pembanding dan bukti tandingan? | Theory/contribution memo |
| Design | Bukti apa yang diperlukan untuk menjawab RQ? | Design matrix, analysis plan, ethics/data plan |
| Execution | Apakah kegiatan benar-benar dilakukan sesuai izin dan rencana? | Execution/analysis trail, deviation log |
| Interpretation | Apa arti hasil dan apa batas inferensinya? | Result synthesis |
| Writing & Audit | Apakah argumen dapat ditelusuri dan dipertahankan? | Manuscript, review, export |

Detail: [`docs/research-workflow.md`](docs/research-workflow.md).

Tahap boleh diulang. Bukti baru boleh mengubah teori, desain, atau pertanyaan—asal perubahan dicatat.

---

# Quality Gates G0–G7

File lengkap tidak berarti penelitian siap.

Better Research memisahkan dua hal:

```text
Delivery status
Issue / PR selesai
        ≠
Academic readiness
Quality gate SIAP
```

| Gate | Menilai |
|---|---|
| G0 | Konteks dan mandat penelitian |
| G1 | Masalah dan pertanyaan |
| G2 | Protokol dan bukti literatur |
| G3 | Teori dan kontribusi |
| G4 | Desain penelitian |
| G5 | Kesiapan pelaksanaan |
| G6 | Hasil dan interpretasi |
| G7 | Naskah dan kesiapan ujian |

Status:

- `BELUM DINILAI`
- `PERLU REVISI`
- `SIAP`
- `TIDAK BERLAKU` — harus disertai alasan

Kriteria lengkap: [`docs/quality-gates.md`](docs/quality-gates.md).

Penilaian agent bukan persetujuan promotor, komite etik, reviewer jurnal, atau institusi.

---

# Literatur, sitasi, dan reference manager

Metadata bibliografis kanonik disimpan di:

[`literature/references.bib`](literature/references.bib)

File ini sengaja dimulai kosong agar builder tidak membawa referensi fiktif.

Workflow yang disarankan:

```text
Search
  ↓
Screening
  ↓
Read original source
  ↓
Source note
  ↓
Verified metadata
  ↓
references.bib
  ↓
Claim ledger
  ↓
Manuscript citation
```

Naskah Markdown dapat menggunakan citation key seperti:

```markdown
... sebagaimana dibahas dalam literatur sebelumnya [@citation-key].
```

`references.bib` dapat dipakai sebagai basis pertukaran BibTeX dengan reference manager seperti Zotero atau Mendeley. Hindari memelihara metadata yang sama secara manual di banyak tempat.

PDF berlisensi sebaiknya disimpan lokal atau pada storage institusi sesuai izin. Jangan commit PDF berhak cipta atau data sensitif hanya karena repository bersifat private.

Panduan: [`literature/README.md`](literature/README.md) dan [`manuscript/README.md`](manuscript/README.md).

---

# Markdown sebagai sumber kanonik

Better Research sengaja memprioritaskan Markdown.

Alasannya:

- mudah dibaca manusia dan AI;
- diff Git tetap jelas;
- perubahan beberapa paragraf dapat direview secara surgical;
- tidak bergantung pada satu aplikasi;
- mudah dikonversi ke format lain;
- referensi dan artefak dapat ditautkan secara eksplisit.

Output Word, PDF, LaTeX, atau format kampus dapat menjadi hasil ekspor. Namun sumber kerja sebaiknya tetap dapat ditelusuri ke Markdown dan `references.bib`.

---

# Peta repository

```text
.
├── AGENTS.md
├── .agents/
│   └── skills/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── research/
├── literature/
├── analysis/
├── manuscript/
├── data/
├── reviews/
├── exports/
├── templates/
└── docs/
```

| Lokasi | Fungsi |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Satu-satunya pintu masuk aturan agent |
| [`.agents/skills/`](.agents/skills/) | Delapan skill lokal |
| [`research/`](research/project-brief.md) | Brief, status, keputusan, deviation, dan AI-use log |
| [`literature/`](literature/README.md) | Search trail, screening, source notes, claim ledger, dan references.bib |
| [`analysis/`](analysis/README.md) | Analysis plan dan jejak analisis |
| [`manuscript/`](manuscript/README.md) | Naskah Markdown kanonik |
| [`data/`](data/README.md) | Dokumentasi tata kelola data |
| [`reviews/`](reviews/README.md) | Audit, review, dan respons |
| [`exports/`](exports/README.md) | Hasil ekspor dan pemeriksaan |
| [`templates/`](templates/README.md) | Formulir kerja |
| [`docs/`](docs/research-workflow.md) | Dokumentasi workflow, integritas, standar, skill, Issue, PR, dan Git |

---

# Template yang tersedia

Better Research menyediakan formulir untuk:

- session checkpoint;
- problem memo;
- review protocol;
- search log;
- screening log;
- source note;
- claim ledger;
- theory & contribution;
- design matrix;
- analysis plan;
- ethics & data plan;
- chapter plan;
- gate review;
- review response.

Lihat [`templates/README.md`](templates/README.md).

Template tidak perlu diisi sekaligus. Buat hanya ketika tahap penelitian membutuhkannya.

---

# Melanjutkan pekerjaan pada sesi AI berikutnya

Inilah inti dari desain Better Research.

Anda tidak perlu mengatakan:

> "Ingat pembicaraan kita minggu lalu?"

Gunakan Issue.

Contoh instruksi:

> Baca AGENTS.md dan lanjutkan issue #[nomor] pada repository [owner/repo]. Baca snapshot, checkpoint terakhir, keputusan, dependency, source/claim yang ditautkan, serta PR dan review terkait. Cocokkan dengan branch dan commit aktual. Ringkas posisi terakhir, nyatakan unknown atau blocker yang masih berlaku, lalu lanjutkan hanya pekerjaan yang belum memenuhi acceptance criteria. Simpan checkpoint sebelum sesi berakhir.

Agent dapat merekonstruksi konteks dari repository, bukan mengandalkan memori percakapan.

---

# Kapan membuat Issue baru?

Buat Issue baru bila ada **unit keputusan atau output yang dapat direview secara mandiri**.

Contoh:

```text
Baik:
#31 Verify theoretical mechanism for RQ2
#32 Audit measurement validity for construct X
#33 Revise discussion against contradictory findings
```

Hindari:

```text
Buruk:
#31 Kerjakan disertasi
#32 Lanjutkan riset
#33 Bikin lebih bagus
```

Pertanyaan klarifikasi yang masih bagian dari Issue aktif tidak memerlukan Issue baru.

Untuk pekerjaan besar, gunakan parent issue + child issues.

---

# Definisi selesai

Sebuah output file dianggap selesai secara **delivery** ketika:

- acceptance criteria Issue terpenuhi;
- perubahan ada pada branch yang benar;
- pemeriksaan aktual tercatat;
- PR direview;
- PR merged ke `main`;
- commit di `main` diverifikasi;
- Issue ditutup dengan status yang sesuai.

Tetapi:

```text
MERGED ≠ scientifically valid
MERGED ≠ ethical approval
MERGED ≠ supervisor approval
MERGED ≠ research completed
```

Mutu akademik tetap dinilai melalui evidence, metode, review, dan quality gates.

---

# Aturan yang tidak boleh dinegosiasikan

1. Jangan mengarang sumber, DOI, kutipan, halaman, data, hasil, izin, atau aktivitas penelitian.
2. Jangan menyatakan sumber mendukung klaim sebelum dukungannya diperiksa.
3. Jangan memilih metode hanya karena populer atau terlihat canggih.
4. Jangan menyembunyikan contradictory evidence.
5. Jangan menyebut dua agent AI sebagai dua reviewer manusia independen.
6. Jangan menyimpan data peserta sensitif di Git.
7. Jangan mengklaim ethical approval, pilot, fieldwork, analysis, atau human review yang belum benar-benar terjadi.
8. Jangan menjadikan banyaknya sitasi, panjang naskah, signifikansi statistik, atau rendahnya similarity score sebagai bukti mutu penelitian.
9. Jangan mengubah banyak bagian hanya karena agent "sekalian memperbaiki".
10. Jangan menggunakan chat history sebagai satu-satunya sumber keputusan proyek.

Rincian: [`docs/academic-integrity.md`](docs/academic-integrity.md).

---

# Contoh satu siklus kerja

Misalnya review menemukan satu klaim teori terlalu kuat.

```text
Review finding
    ↓
Issue #47
"Narrow causal claim in theoretical mechanism"
    ↓
Read source notes SRC-021, SRC-044, SRC-052
    ↓
Check contradictory evidence
    ↓
Decision:
causal → associational / conditional claim
    ↓
Edit 3 relevant paragraphs only
    ↓
Update claim ledger
    ↓
PR
    ↓
Review diff
    ↓
Merge
    ↓
Checkpoint
```

Tidak perlu meminta agent membaca seluruh corpus dan menulis ulang seluruh bab.

Itulah tujuan bounded-context research.

---

# Batas Better Research

Better Research adalah **research operating system**, bukan mesin kebenaran.

Ia tidak otomatis:

- menyediakan akses Scopus, Web of Science, ProQuest, atau database berbayar;
- membaca sumber yang tidak diberikan atau tidak dapat diakses;
- menjadikan AI sebagai reviewer manusia;
- memberikan ethical approval;
- memilih desain penelitian yang benar tanpa informasi;
- membuktikan novelty hanya dari pencarian singkat;
- melakukan statistical analysis tanpa data dan asumsi yang sesuai;
- menjamin naskah diterima jurnal atau lulus ujian;
- menggantikan penilaian peneliti, promotor, reviewer, atau institusi.

Workflow yang baik mengurangi kegagalan. Ia tidak menghapus kebutuhan akan judgement.

---

# Filosofi

Penelitian besar tidak seharusnya bergantung pada kemampuan satu sesi AI untuk "mengingat semuanya".

Lebih baik membangun sistem di mana:

```text
setiap klaim memiliki bukti,
setiap keputusan memiliki alasan,
setiap perubahan memiliki diff,
setiap tugas memiliki scope,
setiap sesi memiliki checkpoint,
dan setiap kontribusi dapat dipertahankan.
```

**Better Research tidak mencoba membuat AI mengingat seluruh penelitian.  
Better Research membuat penelitian dapat dipulihkan, diperiksa, dan dilanjutkan.**

---

## Dokumentasi penting

- [Aturan agent](AGENTS.md)
- [Workflow penelitian](docs/research-workflow.md)
- [Workflow Git](docs/git-workflow.md)
- [Aturan Issue](docs/issues.md)
- [Kesinambungan sesi](docs/session-continuity.md)
- [Pull Request dan merge](docs/pull-requests.md)
- [Quality gates](docs/quality-gates.md)
- [Integritas akademik](docs/academic-integrity.md)
- [Indeks skill](docs/skills.md)
- [Register standar](docs/standards.md)

