# 🖼️ convert-png-jpg-jpeg-to-webp

Aplikasi web sederhana berbasis **Streamlit** untuk mengonversi file gambar **(PNG, JPG, JPEG)** maupun **PDF** menjadi format **WebP**.
Didesain agar mudah digunakan: cukup unggah file → lihat pratinjau → unduh hasil konversi.

---

## 🚀 Fitur

* ✅ Upload file gambar (.png, .jpg, .jpeg)
* ✅ Upload file PDF (otomatis konversi setiap halaman ke WebP)
* ✅ Preview gambar sebelum download
* ✅ Download hasil konversi dengan kualitas terjaga (80%)
* ✅ Berjalan di web (via Streamlit Cloud atau lokal)

---

## 🛠️ Instalasi Lokal

1. Clone repo:

   ```bash
   git clone https://github.com/username/convert-png-jpg-jpeg-to-webp.git
   cd convert-png-jpg-jpeg-to-webp
   ```

2. Buat virtual environment (opsional tapi disarankan):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:

   ```bash
   streamlit run app.py
   ```

5. Buka di browser:

   ```
   http://localhost:8501
   ```

---

## 🌍 Deploy ke Streamlit Cloud

1. Push project ini ke GitHub.
2. Buka [Streamlit Cloud](https://share.streamlit.io).
3. Login dengan GitHub → **New app** → pilih repo & branch → pilih file `app.py`.
4. Klik **Deploy**.
5. App kamu langsung online dengan link:

   ```
   https://username-convert-png-jpg-jpeg-to-webp.streamlit.app
   ```

---

## 📦 Dependencies

* [streamlit](https://streamlit.io) - framework web untuk Python
* [pillow (PIL)](https://python-pillow.org) - manipulasi gambar
* [pdf2image](https://github.com/Belval/pdf2image) - konversi PDF ke gambar
* [poppler-utils](https://poppler.freedesktop.org/) - backend untuk pdf2image (harus diinstal manual di sistem)

---

## 📦 requirements.txt

```
streamlit>=1.25.0
pillow>=10.0.0
pdf2image>=1.17.0
```

⚠️ Catatan:

* **Poppler** tidak bisa diinstall via `pip`.

  * **Linux**: `sudo apt install poppler-utils`
  * **Mac**: `brew install poppler`
  * **Windows**: Download [poppler for Windows](http://blog.alivate.com.au/poppler-windows/) dan tambahkan ke PATH.

---

## 📝 Lisensi

Proyek ini menggunakan lisensi **MIT**. Silakan gunakan, modifikasi, dan distribusikan sesuai kebutuhan.
