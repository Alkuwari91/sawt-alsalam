import streamlit as st

st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# نفس CSS المستخدم في Home (مختصر + ثابت)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }

.stApp {
  background-color: #F9FBFC;
  color: #333;
  direction: rtl;
}

.block-container { padding-top: 1.5rem; max-width: 900px; }

.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color: white;
  padding: 2.6em 1em;
  text-align: center;
  margin: -1.5rem -1rem 2.2rem -1rem;
}
.hero-title{ font-size: 2.4em; font-weight: 800; margin: 0; }
.hero-sub{ font-size: 1.05em; margin-top: 0.5em; opacity: 0.95; }

.content-box{
  background:#fff;
  border-radius:16px;
  padding: 2em;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  border: 1px solid #f0f0f0;
}

.footer{
  background-color:#6E0F2C;
  color:#fff;
  text-align:center;
  padding:1.1em;
  border-radius:14px;
  margin-top: 2.2em;
  font-size: 0.9em;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
  <div class="hero-title">حماية التعليم ضد الهجمات</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
</div>
""", unsafe_allow_html=True)

# Content (بدون HTML داخل النص)
st.markdown('<div class="content-box">', unsafe_allow_html=True)

st.markdown("## تاريخ الفعالية")
st.write("9 سبتمبر")

st.markdown("## الهدف")
st.write("تعزيز وعي الطالبات بأهمية حماية التعليم وحق التعلم في بيئة مدرسية آمنة.")

st.markdown("## أبرز الأنشطة")
st.markdown("""
- عرض توعوي مبسط حول مفهوم التعليم الآمن  
- مناقشة صفية تفاعلية  
- نشاط كتابي قصير *(لماذا التعليم حق؟)*  
- إعداد لوحة صفية توعوية  
""")

st.markdown("## الأثر التعليمي")
st.write("رفع مستوى الوعي لدى الطالبات وربط مفهوم حماية التعليم بسلوكيات إيجابية داخل المدرسة.")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
