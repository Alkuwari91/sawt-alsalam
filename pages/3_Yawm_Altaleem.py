import streamlit as st
from pathlib import Path
from styles import inject_global_css

st.set_page_config(
    page_title="يوم التعليم العالمي | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# =========================
# HEADER
# =========================
st.markdown("""
<div class="hero">
  <div class="hero-title">يوم التعليم العالمي</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">24 يناير – التعليم حق… ويصنع المستقبل</div>
</div>
""", unsafe_allow_html=True)

# =========================
# 3 CARDS
# =========================
col1, col2, col3 = st.columns(3, gap="large")

# -------- Card 1: الهدف --------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sec">الهدف من النشاط</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="p">
تعزيز قيمة التعليم لدى الطالبات، ورفع الدافعية للتعلّم، وربط التعليم
ببناء المستقبل وتنمية المهارات، ضمن بيئة مدرسية آمنة وداعمة.
</div>
""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------- Card 2: وصف النشاط --------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="sec">وصف النشاط</div>', unsafe_allow_html=

