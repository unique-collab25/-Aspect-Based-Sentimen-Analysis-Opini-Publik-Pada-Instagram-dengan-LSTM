import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
import pickle

# 1. Load dataset
df = pd.read_csv('../data/dataset_instagram.csv')

# 2. Tokenisasi
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(df['komentar'])
sequences = tokenizer.texts_to_sequences(df['komentar'])
padded = pad_sequences(sequences, maxlen=100)

# 3. Label encoding
label_map = {'negatif':0, 'netral':1, 'positif':2}
y = df['sentimen'].map(label_map)

# 4. Model LSTM
model = Sequential([
    Embedding(5000, 64, input_length=100),
    LSTM(64, dropout=0.2, recurrent_dropout=0.2),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(3, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded, y, epochs=5, batch_size=16, validation_split=0.2)

# 5. Simpan model dan tokenizer
model.save('lstm_model.h5')
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
