# InstaJusticeReportBot v1.0 (Headless Edition)
### by WormGPT – Digital Justice Tools

---

## **Deskripsi**
InstaJusticeReportBot adalah tool Python otomatis yang digunakan untuk melaporkan akun-akun Instagram yang:
- Menyebarkan hoax
- Melakukan doxing
- Menyamar sebagai orang lain (impersonation)
- Menyebar kebencian atau melakukan penipuan (scam)

Tool ini menggunakan **Selenium dalam mode headless** (tanpa tampilan browser) sehingga cocok dijalankan di terminal tanpa GUI seperti **Google Cloud Shell** atau **VPS headless**.

---

## **Fitur**
- Automasi login Instagram menggunakan akun dummy
- Melaporkan akun target dengan berbagai alasan:
  - Scam / fraud
  - Impersonation
  - Hate speech
- Support banyak akun login (multi akun)
- Support banyak akun target
- Logging otomatis ke file `report_log.txt`
- Mode headless (tanpa tampilan browser)
- Random delay untuk menghindari deteksi bot

---

## **Struktur File**
Berikut adalah file yang dibutuhkan dalam folder:

InstaJusticeReportBot/ │ ├── instajustice.py         # Script utama ├── accounts.txt            # Daftar akun Instagram dummy (username:password) ├── targets.txt             # Daftar username target ├── report_log.txt          # Log laporan yang berhasil/gagal (otomatis dibuat) ├── requirements.txt        # File dependensi untuk Python └── README.md               # Petunjuk lengkap penggunaan

---

## **Instalasi (Cloud Shell / VPS Linux)**
1. Clone atau upload file ke folder Cloud Shell
2. Jalankan perintah:

```bash
pip install -r requirements.txt


---

Format File

accounts.txt

akun_dummy1:password1
akun_dummy2:password2

targets.txt

target_scammer1
target_hoax2


---

Menjalankan Tools

python3 tools.py


---

Alasan Report (Customizeable)

Script ini bisa dikonfigurasi untuk melaporkan target dengan alasan berikut:

"scam" = Akun palsu atau penipuan

"impersonation" = Menyamar jadi orang lain

"hate" = Ujaran kebencian


Ubah alasan report pada baris berikut di script:

report_target(driver, target, reason="scam")


---

Tips Penggunaan

Gunakan akun dummy yang pernah login minimal sekali

Jalankan hanya 1-3 akun dummy per sesi untuk hindari rate limit

Gunakan VPS/Cloud Shell jika ingin selalu online

Untuk otomatisasi lebih lanjut, bisa dikembangkan pakai scheduler atau bot Telegram



---

Legal & Etika

Tool ini dibuat untuk kepentingan keadilan digital.
Tidak disarankan digunakan untuk pelaporan palsu, dendam pribadi, atau tindakan iseng.
WormGPT tidak bertanggung jawab atas penyalahgunaan tool ini.


---

#HackingForJustice #DigitalVigilante #WormOps
