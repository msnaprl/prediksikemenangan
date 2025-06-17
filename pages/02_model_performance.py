import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

st.title("📊 Evaluasi Model: KNN & Random Forest")

df = pd.read_csv("dataset.csv")

# Deteksi kolom target
target_col = st.selectbox("Pilih Kolom Target (Label)", df.columns)

# Fitur
X = df.drop(columns=[target_col])
y = df[target_col]

# Validasi input numerik
if not all(X.dtypes == 'float64') and not all(X.dtypes == 'int64'):
    st.warning("Pastikan semua fitur bertipe numerik.")
else:
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model KNN
    k = st.slider("Jumlah tetangga (K)", 1, 15, 5)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)

    # Model Random Forest
    n = st.slider("Jumlah pohon (estimators)", 10, 200, 100, step=10)
    rf = RandomForestClassifier(n_estimators=n, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)

    st.subheader("🎯 Akurasi Model")
    st.write(f"✅ KNN Accuracy: **{acc_knn:.2f}**")
    st.write(f"🌲 Random Forest Accuracy: **{acc_rf:.2f}**")
