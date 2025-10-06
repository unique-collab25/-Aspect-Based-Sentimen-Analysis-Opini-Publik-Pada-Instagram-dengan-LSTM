import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle, re

# Load model dan tokenizer
model = tf.keras.models.load_model('model/lstm_model.h5')
tokenizer = pickle.load(open('model/tokenizer.pkl', 'rb'))

# Preprocessing sederhana
def clean_text(text):
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    return text.lower()

st.title("📊 Aspect-Based Sentiment Analysis Instagram dengan LSTM")
st.write("Analisis opini publik berdasarkan aspek menggunakan Deep Learning")

komentar = st.text_area("Masukkan komentar Instagram:")
aspek = st.selectbox("Pilih aspek:", ["Pelayanan", "Produk", "Harga", "Kualitas"])

if st.button("Analisis"):
    if komentar.strip() != "":
        teks = clean_text(komentar)
        seq = tokenizer.texts_to_sequences([teks])
        padded = pad_sequences(seq, maxlen=100)
        pred = model.predict(padded)
        label = ['Negatif', 'Netral', 'Positif']
        hasil = label[pred.argmax()]
        st.success(f"Hasil analisis aspek **{aspek}**: {hasil}")
