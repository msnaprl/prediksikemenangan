import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("dataset.csv")

# Label encoding
le = LabelEncoder()
df_encoded = df.copy()
for col in ['Pelatih', 'Kandang Sendiri', 'Latihan', 'Stamina', 'Mental', 'Menang']:
    df_encoded[col] = le.fit_transform(df_encoded[col])

X = df_encoded[['Pelatih', 'Kandang Sendiri', 'Latihan', 'Stamina', 'Mental']]
y = df_encoded['Menang']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sidebar Navigation
page = st.sidebar.selectbox("Pilih Halaman", ["Visualisasi Data", "Performa Model", "Prediksi"])

# Page 1: Visualisasi Data
if page == "Visualisasi Data":
    st.title("Visualisasi Data Awal")
    st.dataframe(df)

    st.subheader("Distribusi Kategori")
    for col in ['Pelatih', 'Kandang Sendiri', 'Latihan', 'Stamina', 'Mental', 'Menang']:
        st.write(f"### {col}")
        fig, ax = plt.subplots()
        df[col].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

# Page 2: Performa Model
elif page == "Performa Model":
    st.title("Evaluasi Performa Model")

    st.header("1. Dataset dan Preprocessing")
    st.write("Menampilkan data yang telah di-label encoding:")
    st.dataframe(df_encoded)

    st.subheader("Fitur dan Target")
    st.write("Fitur digunakan untuk prediksi:")
    st.write(X.columns.tolist())
    st.write("Target:")
    st.write("Menang")

    st.header("2. Training dan Evaluasi Model")

    # KNN
    st.subheader("Model 1: K-Nearest Neighbors (KNN)")
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)

    st.write("Akurasi KNN:")
    st.write(f"{accuracy_score(y_test, y_pred_knn):.2f}")

    st.write("Confusion Matrix - KNN")
    fig, ax = plt.subplots()
    sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt='d', cmap='Blues')
    st.pyplot(fig)

    st.write("Classification Report - KNN")
    st.dataframe(pd.DataFrame(classification_report(y_test, y_pred_knn, output_dict=True)).transpose())

    # Random Forest
    st.subheader("Model 2: Random Forest")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    st.write("Akurasi Random Forest:")
    st.write(f"{accuracy_score(y_test, y_pred_rf):.2f}")

    st.write("Confusion Matrix - Random Forest")
    fig, ax = plt.subplots()
    sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Greens')
    st.pyplot(fig)

    st.write("Classification Report - Random Forest")
    st.dataframe(pd.DataFrame(classification_report(y_test, y_pred_rf, output_dict=True)).transpose())

# Page 3: Prediksi
elif page == "Prediksi":
    st.title("Prediksi Menang")

    pelatih = st.selectbox("Pelatih", df["Pelatih"].unique())
    kandang = st.selectbox("Kandang Sendiri", df["Kandang Sendiri"].unique())
    latihan = st.selectbox("Latihan", df["Latihan"].unique())
    stamina = st.selectbox("Stamina", df["Stamina"].unique())
    mental = st.selectbox("Mental", df["Mental"].unique())

    # Transform input
    input_data = pd.DataFrame({
        'Pelatih': [pelatih],
        'Kandang Sendiri': [kandang],
        'Latihan': [latihan],
        'Stamina': [stamina],
        'Mental': [mental]
    })

    input_encoded = input_data.copy()
    for col in input_encoded.columns:
        input_encoded[col] = le.fit(df[col]).transform(input_encoded[col])

    prediction = knn.predict(input_encoded)[0]
    label = le.fit(df['Menang']).inverse_transform([prediction])[0]

    st.subheader("Hasil Prediksi:")
    st.write(f"Prediksi: **{label}**")
