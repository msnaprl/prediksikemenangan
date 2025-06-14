import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi
st.set_page_config(page_title="Dashboard Kemenangan", page_icon="🏆", layout="wide")

# Input nama pengguna
if "username" not in st.session_state or st.session_state.username == "":
    st.session_state.username = st.text_input("Masukkan nama Anda:", placeholder="Contoh: kayla")
    st.stop()

# Judul dan sambutan
st.markdown(f"## 👋 Halo, {st.session_state.username}!")
st.markdown("Selamat datang di **Dashboard Prediksi Kemenangan Tim**! 🎯
Gunakan menu di sebelah kiri untuk mengakses:
- 📈 Visualisasi Data  
- 🤖 Evaluasi Model  
- 🔮 Prediksi Kemenangan
")
# Tambahkan statistik dummy (misal diambil dari dataset)
st.markdown("### 📈 Statistik Singkat")
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Data", "120")
col2.metric("Rasio Menang", "72%")
col3.metric("Jumlah Pelatih Unik", "8")

# Tambahkan grafik dummy
st.markdown("### 🔍 Contoh Visualisasi")
data = pd.DataFrame({
    "Kategori": ["A", "B", "C", "D"],
    "Jumlah": [40, 25, 35, 20]
})
fig, ax = plt.subplots()
ax.bar(data["Kategori"], data["Jumlah"], color="skyblue")
ax.set_title("Distribusi Kategori Tim")
st.pyplot(fig)

# Ganti nama
with st.sidebar.expander("⚙️ Ganti Nama Pengguna"):
    st.session_state.username = st.text_input("Nama Anda:", value=st.session_state.username)



