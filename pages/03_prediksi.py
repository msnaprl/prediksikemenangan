import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

st.title("🔮 Prediksi Kemenangan Tim Lomba")

# Load data
df = pd.read_csv("dataset.csv")

# Drop kolom 'No' jika ada
if "No" in df.columns:
    df.drop(columns=["No"], inplace=True)

# Target kolom
target = "Menang"

if target not in df.columns:
    st.error("Kolom 'Menang' tidak ditemukan.")
    st.stop()

# Fitur dan Target
X = df.drop(columns=[target])
y = df[target]

# Deteksi kolom numerik dan kategorik
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

# Preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
], remainder="passthrough")

X_encoded = preprocessor.fit_transform(X)

# Train models
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_encoded, y)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_encoded, y)

st.markdown("Masukkan data tim untuk memprediksi apakah akan **menang** atau **tidak**.")

# Buat input user
user_input = {}
for col in X.columns:
    if col in num_cols:
        user_input[col] = st.number_input(f"{col}", value=float(X[col].mean()))
    elif col in cat_cols:
        user_input[col] = st.selectbox(f"{col}", options=sorted(X[col].unique()))

# Convert input jadi DataFrame
user_df = pd.DataFrame([user_input])

# Preprocessing user input
user_encoded = preprocessor.transform(user_df)

# Prediksi
pred_knn = knn.predict(user_encoded)[0]
pred_rf = rf.predict(user_encoded)[0]

st.subheader("📢 Hasil Prediksi")
st.write(f"🔹 Prediksi Menang berdasarkan **KNN**: {pred_knn}")
st.write(f"🔸 Prediksi Menang berdasarkan **Random Forest**: {pred_rf}")

 
