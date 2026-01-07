import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# GLOBAL CSS (SAME AS HOME)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background-color: #F9FBFC;
    color: #333;
    direction: rtl;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 900px;
}

/* ===== Header ===== */
.hero {
    background: linear-gradient(135deg, #8A1538, #6E0F2C);
    color: white;
    padding: 2.6em 1em;
    text-align: center;
    margin: -1.5rem -1rem 2.2rem -1rem;
}

.hero-title {
    font-size: 2.6em;
    font-weight: 800;
}

.hero-sub {
    font-size: 1.2em;
    margin-top: 0.4em;
    opacity: 0.95;
}

/* ===== Content Box ===== */
.content-box {
    background: white;
    border-radius: 16px;
    padding: 2em;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    margin-bottom: 2em;
}

.content-box h3 {
    color: #8A1538;
    font-size: 1.4em;
    font-weight: 800;
    margin-bottom: 0.6em;
}

.content-box p, .content-box li {
    line-height: 1.9;
    font-size: 1em;
}

/* ===== Back Button ===== */
.back-btn {
    margin-top: 1.5em;
}

/* ===== Footer ===== */
.footer {
    background-color: #6E0F2C;
    color: white;
    text-align: center;
    padding: 1.2em;
    border-radius: 14px;
    margin-top: 3em;
    font-size: 0.9em;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (SAME STYLE)
# =========================
st.markdown("""
<div class="hero">
    <div class="hero-title">حماية التعليم ضد الهجمات</div>
    <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
</div>
""", unsafe_allow_html=True)

# =========================
# PAGE CONTENT
# =========================
st.markdown("""
<div class="content-box">
    <h3>📅 تاريخ الفعالية</h3>
    <p>9 سبتمبر</p>

    <h3>🎯 الهدف</h3>
    <p>
    تعزيز وعي الطالبات بأهمية حماية التعليم وحق التعلم
    في بيئة مدرسية آمنة.
    </p>

    <h3>✅ أبرز الأنشطة</h3>
    <ul>
        <li>عرض توعوي مبسط حول مفهوم التعليم الآمن</li>
        <li>مناقشة صفية تفاعلية</li>
        <li>نشاط كتابي قصير (لماذا التعليم حق؟)</li>
        <li>إعداد لوحة صفية توعوية</li>
    </ul>

    <h3>🌟 الأثر التعليمي</h3>
    <p>
    رفع مستوى الوعي لدى الطالبات وربط مفهوم
    حماية التعليم بسلوكيات إيجابية داخل المدرسة.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# BACK BUTTON
# =========================
if st.button("← العودة إلى الصفحة الرئيسية", use_container_width=True):
    st.switch_page("Home.py")

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    © صوت السلام – مدرسة آمنة محمود الجيدة
</div>
""", unsafe_allow_html=True)

