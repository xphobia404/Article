# 📝 Project Setup Guide

## Clone Code
```sh
git clone git@github.com:xphobia404/Article.git
```

## 🔥 Backend Setup (Python Flask)

### 1️⃣ Install Dependencies
Buka buka terminal baru lalu masuk ke direktori
```sh
cd BE
```

### 2️⃣ Install Dependencies
Pastikan Anda sudah menginstal **Python 3** dan **pip**. Jika belum, unduh dari [python.org](https://www.python.org/downloads/).

Lalu, instal dependensi dengan:
```sh
pip install -r requirements.txt
```

### 3️⃣ Jalankan Backend Server
Jalankan perintah berikut di terminal untuk memulai server Flask:
```sh
python app.py
```
Jika berjalan dengan sukses, Anda akan melihat output seperti:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

## 🎨 Frontend Setup (Vue 3 + Vuetify)

### 1️⃣ Open
Pastikan Anda sudah menginstal **Node.js** (minimal versi 14). Buka buka terminal baru lalu masuk ke direktori
```sh
CD FE
```

### 2️⃣ Install Dependencies
```sh
npm install
```

### 3️⃣ Jalankan Front-End
```sh
npm run dev
```
Vue akan berjalan di `http://localhost:5173/` (sesuai dengan konfigurasi Vite).

---

## 🚀 Testing Backend & Frontend
- Buka `http://127.0.0.1:5000/` untuk menguji API Backend.
- Buka `http://localhost:5173/` untuk melihat UI Frontend.
- Pastikan frontend bisa mengambil data dari backend.

---

## 🎯 Fitur Utama
- ✅ **CRUD Articles** – Tambah, edit, hapus, dan lihat artikel.
- ✅ **Pagination** – Menampilkan daftar artikel dengan navigasi halaman.

---
