import streamlit as st

st.set_page_config(page_title="Dashboard Prediksi", layout="wide")

# -- Input nama pengguna (sekali saja)
if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.username == "":
    st.session_state.username = st.text_input("Masukkan nama Anda:", placeholder="Contoh: Mesni")
    st.stop()  # Hentikan eksekusi sampai nama dimasukkan

# -- Setelah nama dimasukkan
st.title(f"Halo, {st.session_state.username}! 👋")
st.markdown("""
Selamat datang di dashboard prediksi kemenangan tim!  
Silakan gunakan menu di sebelah kiri untuk:
- Melihat **Visualisasi Data**
- Mengevaluasi **Performa Model**
- Melakukan **Prediksi**
""")

