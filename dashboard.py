import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Kemenangan", page_icon="🏆", layout="wide")

# Inisialisasi session_state
if "username" not in st.session_state:
    st.session_state.username = ""

# Input nama pengguna (pertama kali)
if st.session_state.username == "":
    name_input = st.text_input("Masukkan nama Anda:", placeholder="Contoh: Kayla", key="name_input")

    # Setelah nama diisi, simpan dan rerun
    if name_input.strip() != "":
        st.session_state.username = name_input.strip()
        st.experimental_rerun()  # refresh supaya tidak masuk ulang
    else:
        st.stop()

# Halaman utama setelah nama ada
st.markdown(f"## 👋 Halo, {st.session_state.username}!")
st.markdown("""
Selamat datang di **Dashboard Prediksi Kemenangan Tim**! 🎯  
Gunakan menu di sebelah kiri untuk mengakses:
- Visualisasi Data  
- Evaluasi Model  
- Prediksi Kemenangan
""")

# Statistik dummy
st.markdown("### 📈 Statistik Singkat")
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Data", "120")
col2.metric("Rasio Menang", "72%")
col3.metric("Jumlah Pelatih Unik", "8")

# Visualisasi dummy
st.markdown("### 🔍 Contoh Visualisasi")
data = pd.DataFrame({
    "Kategori": ["A", "B", "C", "D"],
    "Jumlah": [40, 25, 35, 20]
})
fig, ax = plt.subplots()
ax.bar(data["Kategori"], data["Jumlah"], color="skyblue")
ax.set_title("Distribusi Kategori Tim")
st.pyplot(fig)

# Sidebar untuk mengganti nama
with st.sidebar.expander("⚙️ Ganti Nama Pengguna"):
    new_name = st.text_input("Nama Anda:", value=st.session_state.username, key="change_name")
    if new_name != st.session_state.username and new_name.strip() != "":
        st.session_state.username = new_name.strip()
        st.experimental_rerun()
