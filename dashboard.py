import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Dashboard Prediksi Kemenangan",
    page_icon="📊",
    layout="wide"
)

# Input nama pengguna satu kali saat awal
if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.username == "":
    st.session_state.username = st.text_input(
        "Masukkan nama Anda:", placeholder="Contoh: Kayla"
    )
    st.stop()

# Tampilan dashboard setelah nama dimasukkan
st.markdown(f"# 👋 Halo, {st.session_state.username}!")
st.markdown("""
Selamat datang di **Dashboard Prediksi Kemenangan Tim**.  
Gunakan menu di sebelah kiri untuk mengakses:
- 📊 Visualisasi Data  
- 🤖 Evaluasi Model  
- 🔮 Prediksi Kemenangan
""")

# Sidebar tambahan: ubah nama pengguna
with st.sidebar.expander("⚙️ Ganti Nama Pengguna"):
    st.session_state.username = st.text_input(
        "Nama Anda:", value=st.session_state.username
    )


