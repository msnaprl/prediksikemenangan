import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns

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

# Train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

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
    st.title("Evaluasi Model KNN")

    y_pred = model.predict(X_test)

    st.write("### Akurasi")
    st.write(f"{accuracy_score(y_test, y_pred):.2f}")

    st.write("### Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    st.pyplot(fig)

    st.write("### Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose())

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

    prediction = model.predict(input_encoded)[0]
    label = le.fit(df['Menang']).inverse_transform([prediction])[0]

    st.subheader("Hasil Prediksi:")
    st.write(f"Prediksi: **{label}**")
