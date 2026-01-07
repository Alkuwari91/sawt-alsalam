import streamlit as st
from pathlib import Path
from styles import inject_global_css

st.set_page_config(
    page_title="اليوم العالمي للتضامن مع فلسطين | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

st.markdown("""
<div class="hero">
  <div class="hero-title">اليوم العالمي للتضامن مع فلسطين</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">قيم التضامن والإنسانية والعدالة</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

# ===== Card 1: الهدف =====
with col1:
    with st.container(border=True):
        st.markdown('<div class="sec">الهدف من النشاط</div>', unsafe_allow_html=True)
        st.write("تعزيز قيم التضامن والرحمة والعدالة لدى الطالبات، وتنمية الوعي الإنساني واحترام حقوق الإنسان، وربط هذه القيم بسلوكيات إيجابية داخل المدرسة.")

# ===== Card 2: وصف النشاط =====
with col2:
    with st.container(border=True):
        st.markdown('<div class="sec">وصف النشاط</div>', unsafe_allow_html=True)
        st.write("تنفيذ أنشطة تربوية توعوية بمناسبة اليوم العالمي للتضامن مع فلسطين، شملت حوارًا صفّيًا حول معنى التضامن، ورسائل طلابية تعبّر عن القيم الإنسانية، ومشاركة أعمال فنية/كتابية تعكس التعاطف والسلام.")
        st.markdown('<hr class="hr">', unsafe_allow_html=True)
        st.markdown("""
- فقرة توعوية قصيرة عن مفهوم التضامن  
- مناقشة صفية: كيف نعبّر عن التضامن بطرق إيجابية؟  
- نشاط كتابي: رسالة سلام/تضامن  
- لوحة صفية أو ركن مدرسي للمبادرة
""")

# ===== Card 3: معرض الصور =====
with col3:
    with st.container(border=True):
        st.markdown('<div class="sec">معرض الصور</div>', unsafe_allow_html=True)
        st.caption("صور من GitHub داخل: assets/tadamon/photos (أو ارفعي صور للعرض المؤقت)")

        photos_dir = Path("assets/tadamon/photos")
        photos = []
        if photos_dir.exists():
            for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
                photos += list(photos_dir.glob(ext))
        photos = sorted(photos)

        if photos:
            st.image([str(p) for p in photos], use_container_width=True)
        else:
            st.info("مافي صور مضافة بعد داخل assets/tadamon/photos")

        st.divider()
        up = st.file_uploader(
            "رفع صور للعرض (مؤقت)",
            type=["png", "jpg", "jpeg", "webp"],
            accept_multiple_files=True,
            key="tadamon_photos_upload",
        )
        if up:
            st.image(up, use_container_width=True)

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_tadamon", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
