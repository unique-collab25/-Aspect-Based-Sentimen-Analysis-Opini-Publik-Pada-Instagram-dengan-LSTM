# -Aspect-Based-Sentimen-Analysis-Opini-Publik-Pada-Instagram-dengan-LSTM
Sistem berbasis kecerdasan buatan yang dirancang untuk menganalisis sentimen masyarakat terhadap topik atau aspek tertentu pada media sosial Instagram. Menganalisis opini publik pada Instagram berdasarkan aspek tertentu (pembangunan, bantuan sosial, pendidikan dan pelayanan kesehatan) dengan metode LSTM (Long Short-Term Memory) untuk klasifikasi sentimen:
1. Positif
2. Negatif
3. Netral
   
⚙️ Alur Kerja Aplikasi

Input Data: Dataset komentar Instagram (file .csv berisi kolom: komentar, aspek, sentimen).

Preprocessing:
1. Pembersihan teks (hapus emoji, tanda baca, URL, dll)
2. Stopword removal
3. Tokenisasi
4. Padding sequence

Embedding Layer:
1. Word2vec
    
Model LSTM:
1. LSTM layer
2. Dense output (Softmax)
3. Pengujian menggunakan confusion matrix
    
Prediksi Sentimen: Model memprediksi sentimen dari teks baru berdasarkan aspek tertentu.
Tampilan Aplikasi (streamlit): form input teks komentar, pilihan aspek, dan hasil nalisis.
