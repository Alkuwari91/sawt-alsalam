import streamlit as st
from pathlib import Path
from styles import inject_global_css

st.set_page_config(
    page_title="اليوم العالمي للتضامن مع فلسطين | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# ===== Header =====
st.markdown(
    """
<div class="hero">
  <div class="hero-title">اليوم العالمي للتضامن مع فلسطين</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">29 نوفمبر – التعليم حق… ويصنع المستقبل</div>
</div>
""",
    unsafe_allow_html=True,
)

# ===== 3 columns =====
col1, col2, col3 = st.columns(3, gap="large")

# ===== Card 1: الهدف =====
with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">الهدف من النشاط</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="p">تعزيز قيمة التعليم لدى الطالبات، ورفع الدافعية للتعلّم، وربط التعليم ببناء المستقبل وتنمية المهارات ضمن بيئة مدرسية آمنة وداعمة.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

# ===== Card 2: وصف النشاط =====
# ===== Card 2: وصف النشاط =====
with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">وصف النشاط</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="p">تنفيذ أنشطة مدرسية احتفالية وتربوية بمناسبة يوم التعليم العالمي، تضمنت مشاركة الطالبات في أنشطة كتابية وفنية تعبّر عن أحلامهن وطموحاتهن ودور التعليم في تحقيقها، وذلك ضمن بيئة مدرسية آمنة وداعمة.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)


# ===== Card 3: معرض الصور =====
with col3:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">معرض الصور</div>', unsafe_allow_html=True)

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

    

        st.markdown("</div>", unsafe_allow_html=True)

# ===== Back + Footer =====
st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_yawm", use_container_width=True):
    st.switch_page("Home.py")

st.markdown(
    '<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>',
    unsafe_allow_html=True,
)
