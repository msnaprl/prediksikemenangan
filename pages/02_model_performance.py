import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

st.title("🏆 Performa Model - Prediksi Kemenangan Tim")

# Load dataset
df = pd.read_csv("dataset.csv")

# Drop kolom "No" jika ada
if "No" in df.columns:
    df.drop(columns=["No"], inplace=True)

# Pastikan kolom 'Menang' ada
if "Menang" not in df.columns:
    st.error("Kolom 'kemenangan' tidak ditemukan di dataset.")
    st.stop()

# Pisahkan fitur dan target
X = df.drop(columns=["Menang"])
y = df["Menang"]

# Deteksi tipe kolom
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

# Preprocessing kategorikal
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
], remainder="passthrough")

X_encoded = preprocessor.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Slider parameter
k = st.slider("🔢 Jumlah Tetangga (K untuk KNN)", 1, 15, 5)
n = st.slider("🌲 Jumlah Pohon (Random Forest)", 10, 200, 100, step=10)

# Model KNN
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
knn_acc = accuracy_score(y_test, knn_pred)

# Model Random Forest
rf = RandomForestClassifier(n_estimators=n, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# Akurasi
st.subheader("📊 Akurasi Model")
st.write(f"**KNN (k={k})**: {knn_acc:.2f}")
st.write(f"**Random Forest (n={n})**: {rf_acc:.2f}")

# Confusion Matrix - KNN
st.subheader("📌 Confusion Matrix - KNN")
cm_knn = confusion_matrix(y_test, knn_pred)
fig1, ax1 = plt.subplots()
sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Blues', xticklabels=knn.classes_, yticklabels=knn.classes_)
ax1.set_xlabel("Prediksi")
ax1.set_ylabel("Aktual")
st.pyplot(fig1)

# Classification Report - KNN
st.subheader("📄 Classification Report - KNN")
st.text(classification_report(y_test, knn_pred))

# Confusion Matrix - Random Forest
st.subheader("📌 Confusion Matrix - Random Forest")
cm_rf = confusion_matrix(y_test, rf_pred)
fig2, ax2 = plt.subplots()
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', xticklabels=rf.classes_, yticklabels=rf.classes_)
ax2.set_xlabel("Prediksi")
ax2.set_ylabel("Aktual")
st.pyplot(fig2)

# Classification Report - RF
st.subheader("📄 Classification Report - Random Forest")
st.text(classification_report(y_test, rf_pred))

  
