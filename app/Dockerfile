# Menggunakan base image Node.js versi 18
FROM python:3.12-slim

# Menetapkan direktori kerja di dalam kontainer
WORKDIR /app

# Menyalin semua berkas dari direktori lokal ke /app di dalam kontainer
COPY . .

# Menjalankan perintah untuk menginstal dependensi
RUN pip install --no-cache-dir -r requriements.txt

# Mengekspos port tempat aplikasi berjalan
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Menjalankan aplikasi saat kontainer dimulai
CMD ["python", "app.py"]
