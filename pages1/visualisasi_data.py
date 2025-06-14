import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

st.title("📊 Visualisasi Data")

st.dataframe(df)

cols = df.columns.tolist()
for col in cols:
    st.subheader(f"Distribusi {col}")
    fig, ax = plt.subplots()
    df[col].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
