import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Visualisasi Data")

df = pd.read_csv("dataset.csv")
st.subheader("Data")
st.dataframe(df)

st.subheader("Statistik Deskriptif")
st.write(df.describe(include='all'))

numeric_cols = df.select_dtypes(include='number').drop(columns=["No"], errors='ignore').columns.tolist()
if numeric_cols:
    col = st.selectbox("Pilih Kolom Histogram", numeric_cols)
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    st.pyplot(fig)
else:
    st.warning("Tidak ada kolom numerik selain kolom 'No'.")
