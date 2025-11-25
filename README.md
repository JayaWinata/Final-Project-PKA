# 📌 Tugas Penerapan Kecerdasan Artifisial

Praktik penerapan pipeline **Penerapan Kecerdasan Artifisial** dengan **Hugging Face Spaces** sebagai **Deployment**.

**Hugging Face Spaces** : [Final-Project-PKA3](https://huggingface.co/spaces/100andre001/Final-Project-PKA3)

---

## 📊 Dataset

- **Nama**: `Financial Fraud Detection Dataset`  
- **Tipe**: CSV (Comma Separated Values)  
- **Deskripsi**: Riwayat transaksi dari nasabah asli atau pencuri dengan dataset berupa Financial Fraud Detection Dataset dari Kaggle  
- **Tautan**: [Financial Fraud Detection Dataset](https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset)

---

## 💡 Fitur

- Klasifikasi status nasabar dengan model Xgboost Classifier.
- User Interface dengan Gradio
- Aplikasi berada pada platform Hugging Face Spaces

---

## 🧠 Algoritma Model

- **Model**: Xgboost Classifier  
- **Alasan Pemilihan**:
  - Cepat dalam pelatihan dan prediksi.
  - Efektif dalam melakukan prediksi.

---

## ⚙️ Tech Stack

| Tools              | Deskripsi                                      |
|-------------------|-----------------------------------------------|
| **Python**         | Bahasa pemrograman utama                      |
| **Scikit-learn**   | Library untuk model ExtraTreesClassifier                |
| **Gradio**         | UI interaktif berbasis Python                 |
| **Hugging Face Spaces** | Platform hosting dan deployment          |
| **GitHub**         | Control version kode dan pengaturan CI/CD          |
| **Jupyter Noteebook**   | Tempat eksplorasi dan pelatihan model awal    |
| **Podman**   | Tempat eksplorasi dan pembungkusan aplikasi    |

---

## 🧠 Model Overview

- **Tipe Model**: Xgboost
- **Tugas**: Klasifikasi apakah seorang nasabah atau penipu
- **Data**: 
    - step : Merepresentasikan unit waktu dalam dunia nyata, di mana 1 langkah (step) setara dengan 1 jam. Total durasi simulasi mencakup 744 langkah, yang setara dengan 30 hari kalender.
    - type : Jenis transaksi yang dilakukan, mencakup kategori: CASH-IN (Setor Tunai), CASH-OUT (Tarik Tunai), DEBIT, PAYMENT (Pembayaran), dan TRANSFER.
    - amount : Nominal jumlah uang yang ditransaksikan dalam mata uang lokal.
    - nameOrig : Identitas pelanggan yang memulai transaksi (pengirim).
    - oldbalanceOrg : Saldo awal rekening pengirim sebelum transaksi dilakukan.
    - nameDest : Identitas penerima transaksi (tujuan).
    - oldbalanceDest : Saldo awal rekening penerima sebelum transaksi. (Catatan: Data ini tidak tersedia untuk penerima yang teridentifikasi sebagai 'M' atau Merchants/Pedagang).
- **Target**: 
    - isFraud : Mengidentifikasi transaksi yang dilakukan oleh pelaku penipu atau nasabah asli

cols_to_remove = [
    'newbalanceOrig',
    'newbalanceDest',
    'countDest'
] cols_to_drop = ['isFlaggedFraud']
---

## 👥 Tim & Kontribusi

| Nama Lengkap                             | NIM              |
|------------------------------------------|------------------|
| Andrew Salim                             | 205150207111048  |
| Ryan Satrio Pamungkas                    | 205150207111046  |
| Jaya Winata                              | 225150200111038  |

---

## 🏫 Institusi

- **Program Studi**: Teknik Informatika  
- **Departemen**: Teknik Informatika  
- **Fakultas**: Ilmu Komputer  
- **Universitas**: Universitas Brawijaya – Malang  
- **Tahun**: 2025

---