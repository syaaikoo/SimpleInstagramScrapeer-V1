Instagram Caption Scraper

Versi: 1.0
Dibuat oleh: @syaaikoo

📜 Deskripsi

Instagram Caption Scraper ini adalah tool yang bisa ngambil caption dari postingan Instagram secara otomatis. Skrip ini pakai teknologi web scraping kayak BeautifulSoup dan Requests buat ambil data. Selain itu, tool ini juga punya tampilan yang kece dengan Rich Console buat output yang lebih enak dilihat.

Catatan Penting: Gunakan alat ini dengan bijak dan pastikan tetep patuhi aturan dan kebijakan privasi Instagram.


---

✨ Fitur Utama

Validasi URL Otomatis: Biar URL yang dimasukin beneran URL postingan Instagram.

Scraping Caption: Nggak cuma ambil data, captionnya juga akurat.

Filter Kata Kunci: Bisa filter caption sesuai kata kunci yang lo cari.

Retry Mechanism: Kalo gagal, coba lagi sampe 3 kali supaya nggak gagal terus.

Output Gokil: Hasilnya tampil dalam bentuk tabel dan bisa disimpan ke file teks.

Logging: Semua aktivitas dicatat buat debugging.



---

📂 Struktur File

instagramsc.py: Script utama buat jalanin aplikasi.

instagram_scraper.log: File log yang nyatet aktivitas scraping.

captions.txt: Tempat lo nyimpen caption yang udah di-scrape.

failed_urls.txt: File buat nyimpen URL yang gagal diproses.



---

🛠️ Cara Pakai

1. Pastikan lo udah punya Python 3.7 ke atas.


2. Install dependensi yang dibutuhkan pake perintah:

pip install -r requirements.txt


3. Jalankan script pake perintah:

python instagramsc.py


4. Masukin URL postingan Instagram atau file yang berisi daftar URL pas diminta.


5. Bisa juga tentuin kata kunci (opsional) buat filter caption yang lo cari.


6. Tentuin nama file output buat nyimpen hasil scraping.




---

🔧 Pengaturan

Logging: Semua aktivitas bakal dicatat di instagram_scraper.log buat troubleshooting.

Header HTTP: Skrip ini pakai header User-Agent biar nggak ketahuan bot.



---

📝 Batasan

Script ini nggak bisa ngambil data dari profil yang diprivate.

Hasil scraping bisa berubah kalo ada update atau perubahan di struktur HTML Instagram.



---

📊 Teknologi yang Dipake

Python: Bahasa pemrograman utamanya.

Requests: Buat kirim permintaan HTTP.

BeautifulSoup: Buat ngolah HTML.

Rich: Biar tampilannya di terminal lebih kece.

Logging: Buat catat aktivitas scraping.



---

🧪 Unit Testing

Lo bisa jalanin pengujian pake framework unittest dengan nambahin skrip testing di folder terpisah (opsional).


---

🚀 Pengembangan dan Kontribusi

1. Fork repository ini.


2. Buat branch baru buat fitur yang pengen lo tambahin.


3. Kirim pull request kalo udah selesai.




---

📩 Hubungi Pembuat

Instagram: @syaaikoo
Kalo lo ada pertanyaan, feedback, atau nemu masalah, jangan ragu buat DM di Instagram.


---

Moga alat ini ngebantu dan bikin kerjaan lo lebih gampang!
