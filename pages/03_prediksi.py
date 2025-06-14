import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("dataset.csv")
if 'Nomor' in df.columns:
    df = df.drop(columns=['Nomor'])

le = LabelEncoder()
df_encoded = df.copy()
for col in df.columns:
    df_encoded[col] = le.fit_transform(df[col])

X = df_encoded.drop(columns=['Menang'])
y = df_encoded['Menang']
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

st.title("🔮 Prediksi Kemenangan")

input_data = {}
for col in X.columns:
    input_data[col] = st.selectbox(col, df[col].unique())

input_df = pd.DataFrame([input_data])
input_encoded = input_df.copy()
for col in input_encoded.columns:
    input_encoded[col] = le.fit(df[col]).transform(input_encoded[col])

prediction = model.predict(input_encoded)[0]
label = le.fit(df['Menang']).inverse_transform([prediction])[0]
st.subheader("Hasil Prediksi")
st.write(f"🏆 Prediksi: **{label}**")
