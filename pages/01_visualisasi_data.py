import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Visualisasi Dataset")

df = pd.read_csv("dataset.csv")
if "No" in df.columns:
    df = df.drop(columns=["No"])

st.subheader("🔍 Dataset")
st.dataframe(df)

st.subheader("📈 Statistik Deskriptif")
st.write(df.describe(include='all'))

num_cols = df.select_dtypes(include='number').columns.tolist()
if num_cols:
    pilih = st.selectbox("Pilih kolom numerik untuk histogram", num_cols)
    fig, ax = plt.subplots()
    ax.hist(df[pilih], bins=20, color="skyblue", edgecolor="black")
    st.pyplot(fig)
