import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🤖 Performa Model - Prediksi Menang/Tidak")

df = pd.read_csv("dataset.csv")
if "No" in df.columns:
    df = df.drop(columns=["No"])

target_col = st.selectbox("Pilih Kolom Target (Harus berisi Menang/Tidak)", df.columns)

if target_col:
    X = df.drop(columns=[target_col])
    y = df[target_col]

    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ], remainder='passthrough')

    X_encoded = preprocessor.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # KNN
    k = st.slider("Jumlah K (KNN)", 1, 15, 5)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    knn_pred = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, knn_pred)

    # Random Forest
    n = st.slider("Jumlah Pohon (Random Forest)", 10, 200, 100, step=10)
    rf = RandomForestClassifier(n_estimators=n, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, rf_pred)

    st.subheader("🎯 Akurasi Model")
    st.write(f"✅ **KNN**: {acc_knn:.2f}")
    st.write(f"🌲 **Random Forest**: {acc_rf:.2f}")

    st.subheader("📉 Confusion Matrix (Random Forest)")
    cm = confusion_matrix(y_test, rf_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", ax=ax)
    st.pyplot(fig)

    st.subheader("📄 Classification Report (Random Forest)")
    st.text(classification_report(y_test, rf_pred))
