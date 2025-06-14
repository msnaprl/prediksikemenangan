import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
if 'Nomor' in df.columns:
    df = df.drop(columns=['Nomor'])

st.title("📊 Visualisasi Data")

st.dataframe(df)

for col in df.columns:
    st.subheader(f"Distribusi {col}")
    fig, ax = plt.subplots()
    df[col].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

