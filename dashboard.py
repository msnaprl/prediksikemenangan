import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Prediksi Kemenangan Tim Bola", page_icon="🏆", layout="centered")

# ===================== SIDEBAR ===========================
st.sidebar.title("📘 Informasi pembuat Aplikasi")

st.sidebar.markdown("### 👥 Anggota Kelompok")
st.sidebar.markdown("""
1. Syaiful Primordian (4101422069) : Ketua 
2. Mesni Aprilia (4101422072)  
3. Adinda Putri Aribah (4101422057)
4. Rani Oktaviana (2304030001)
""")

# ===================== DASHBOARD (Main Area) ===========================
# Inisialisasi nama pengguna
if "username" not in st.session_state:
    st.session_state.username = ""

# Input nama pengguna
if st.session_state.username == "":
    name_input = st.text_input("Masukkan nama Anda:", placeholder="Contoh: Kayla", key="name_input")

    # Jika sudah diisi, simpan ke session_state
    if name_input.strip() != "":
        st.session_state.username = name_input.strip()

# Tampilkan dashboard jika nama sudah dimasukkan
if st.session_state.username != "":
    st.markdown(f"## 👋 Halo, {st.session_state.username}!")
    st.markdown("""
    Selamat datang di **Dashboard Prediksi Kemenangan Tim**! 🎯  
    Gunakan menu di sebelah kiri untuk mengakses:
    - Visualisasi Data  
    - Evaluasi Model  
    - Prediksi Kemenangan
    """)
    
# Latar Belakang
st.markdown("""
## *Latar Belakang*
Perkembangan teknologi informasi telah memberikan dampak yang signifikan dalam berbagai aspek kehidupan, termasuk dalam bidang olahraga. Salah satu penerapan teknologi yang kini banyak dimanfaatkan adalah pemanfaatan *data science dan machine learning* untuk menganalisis data pertandingan olahraga. Dalam konteks pertandingan sepak bola, data historis seperti jumlah kemenangan, kekalahan, jumlah gol, hingga performa tim dapat digunakan untuk memprediksi kemungkinan hasil pertandingan selanjutnya. 
Prediksi hasil pertandingan bukan hanya menjadi perhatian para penggemar sepak bola, tetapi juga bagi pelatih, analis tim, hingga pelaku industri taruhan olahraga. Dengan adanya sistem prediksi berbasis data, pengambilan keputusan dapat dilakukan dengan lebih objektif dan berbasis bukti (evidence-based).
Aplikasi *“Prediksi Kemenangan Tim Bola”* ini dikembangkan sebagai solusi sederhana untuk membantu pengguna memprediksi kemungkinan kemenangan suatu tim berdasarkan input data historis pertandingan. Aplikasi ini dibangun menggunakan framework *Streamlit* dan menerapkan model *Random Forest Regressor dan KNN*, sebuah algoritma machine learning yang handal dalam menangani data kompleks dan menghasilkan prediksi yang cukup akurat.

### Tujuan Aplikasi:
1. Memberikan gambaran prediktif tentang performa suatu tim berdasarkan data numerik.
2. Menjadi media pembelajaran dalam penerapan *data mining* dan *machine learning* dalam dunia nyata.
3. Menunjukkan potensi integrasi antara teknologi data dan olahraga untuk pengambilan keputusan yang lebih cerdas.

Dengan adanya aplikasi ini, diharapkan masyarakat, terutama mahasiswa dan pengembang pemula, dapat lebih memahami bagaimana proses pemodelan prediktif dilakukan serta manfaatnya dalam kehidupan sehari-hari.

---
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

    # Sidebar ubah nama
    with st.sidebar.expander("⚙️ Ganti Nama Pengguna"):
        new_name = st.text_input("Nama Anda:", value=st.session_state.username, key="change_name")
        if new_name != st.session_state.username and new_name.strip() != "":
            st.session_state.username = new_name.strip()

