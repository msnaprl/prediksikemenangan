import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

st.title("🔍 Prediksi Data Baru")

df = pd.read_csv("dataset.csv")
if "No" in df.columns:
    df = df.drop(columns=["No"])

target_col = st.selectbox("Pilih Kolom Target", df.columns)

if target_col:
    X = df.drop(columns=[target_col])
    y = df[target_col]

    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ], remainder='passthrough')

    X_encoded = preprocessor.fit_transform(X)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_encoded, y)

    st.subheader("Input Data Baru")
    user_input = {}
    for col in X.columns:
        if col in num_cols:
            user_input[col] = st.number_input(f"{col}", value=float(df[col].mean()))
        elif col in cat_cols:
            user_input[col] = st.selectbox(f"{col}", df[col].unique())

    input_df = pd.DataFrame([user_input])
    input_encoded = preprocessor.transform(input_df)

    prediction = model.predict(input_encoded)[0]
    st.success(f"🎉 Hasil Prediksi: **{prediction}**")

