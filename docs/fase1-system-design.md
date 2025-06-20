# Fase 1: Desain & Arsitektur Sistem

Dokumen ini mendeskripsikan langkah-langkah pada fase awal pengembangan
**Dear Diary**. Fase ini berfokus pada pembuatan cetak biru sebelum pembangunan dimulai.

## Tahap 1.1: Desain Skema Database
- Memfinalisasi model-model SQLAlchemy (user, journal, chatmessage, dan lainnya).
- Membuat Entity-Relationship Diagram (ERD) untuk memvisualisasikan hubungan
  antar tabel. Langkah ini membantu seluruh developer backend memahami struktur data.

## Tahap 1.2: Desain Kontrak API
- Mendefinisikan seluruh endpoint menggunakan Spesifikasi OpenAPI 3.0. FastAPI
  akan menggenerasikannya secara otomatis, namun skema perlu dirancang terlebih
  dahulu.
- Contoh kunci untuk endpoint percakapan:
  - **Request**: `POST /api/v1/chat` dengan body `{ "content": "string" }`.
  - **Response sukses (200)**: `{ "text_response": "string" }`.
  - **Response error (4xx/5xx)**: `{ "detail": "string" }`.
- Dokumentasi ini (tersedia lewat `/docs` pada FastAPI) akan menjadi panduan
  utama untuk tim frontend.

## Tahap 1.3: Finalisasi Arsitektur Backend (Two-Call AI)
- Mengadopsi secara formal Arsitektur Dua Panggilan yang telah dibahas.
- Struktur direktori `services` pada backend akan dipecah menjadi:
  - `services/chat_context.py`: tetap ada, bertugas mengumpulkan data.
  - `services/conversation_planner.py`: **baru**, berisi logika panggilan AI #1.
  - `services/response_generator.py`: **baru**, berisi logika panggilan AI #2.
- Penataan ini harus modular dan mudah diuji.

## Tahap 1.4: Finalisasi Arsitektur Frontend (MVVM)
- Menegaskan kembali penggunaan arsitektur MVVM (Model-View-ViewModel) pada
  aplikasi Android.
- Aliran data dijaga ketat: View (Compose UI) -> ViewModel -> Repository ->
  (ApiService/Room DAO).
- Repository tetap menjadi _single source of truth_.
