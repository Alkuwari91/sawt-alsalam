import streamlit as st

st.set_page_config(
    page_title="صوت السلام | مدرسة آمنة محمود الجيدة",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# GLOBAL CSS (Rasekhon-like)
# =========================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

html, body, [class*="css"]  {
  font-family: 'Cairo', sans-serif;
}

body {
  background-color: #F9FBFC;
  color: #333;
  direction: rtl;
}

.block-container {
  padding-top: 1.2rem;
  max-width: 1100px;
}

header, .hero {
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  c
