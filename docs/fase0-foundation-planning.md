# Fase 0: Fondasi dan Perencanaan

Dokumen ini merangkum kebutuhan dasar sebelum pengembangan Dear Diary dimulai. Fase ini memastikan bahwa semua tim memahami visi produk dan tumpukan teknologi yang dipakai.

## Tahap 0.1: Spesifikasi Produk & Fungsional

- **Visi Produk**: Menciptakan ruang aman digital untuk berekspresi lewat percakapan tanpa penghakiman.
- **Persona AI 'Dee'**: Mitra percakapan netral yang menggunakan teknik probing, reflecting, clarifying, dan paraphrasing.
- **Larangan**: Dee tidak boleh memberi penilaian, nasihat, atau solusi kecuali diminta pengguna.
- **Fitur Utama**:
  - Percakapan berbasis teks dengan Dee.
  - Jurnal harian untuk pencatatan mandiri.
  - Personalisasi konteks menggunakan data profil dan riwayat.
- **Kebutuhan Non-Fungsional**:
  - Performa respons chat di bawah 3 detik.
  - Data dienkripsi saat transit maupun disimpan.
  - Sistem dapat diskalakan untuk peningkatan pengguna.

## Tahap 0.2: Konfirmasi Tumpukan Teknologi

- **Backend**: Python 3.10+, FastAPI, SQLAlchemy + Alembic, PostgreSQL, Celery + Redis, Gunicorn.
- **Frontend**: Kotlin, Jetpack Compose, Coroutines + Flow, Hilt, Room, Retrofit.
- **AI**: API LLM eksternal seperti Google AI Platform atau OpenAI API.
- **DevOps**: Docker, Docker Compose, Nginx, GitHub Actions.

## Tahap 0.3: Pengaturan Lingkungan & Alat

- Inisialisasi repositori Git dengan branch `main` dan `develop`.
- Backend menggunakan virtual environment Python dan file `.env` untuk variabel sensitif.
- Frontend menstandarkan versi Android Studio, JDK, serta Gradle.
- Manajemen proyek dijalankan lewat Jira, Trello, atau GitHub Projects.

