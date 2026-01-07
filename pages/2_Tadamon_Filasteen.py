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
st.markdown("""
<div class="hero">
  <div class="hero-title">اليوم العالمي للتضامن مع فلسطين</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">29 نوفمبر</div>
</div>
""", unsafe_allow_html=True)

# ===== 3 BIG CARDS (Vision/Mission style) =====
c3, c2, c1 = st.columns(3, gap="large")

with c1:  # الهدف
    st.markdown("""
<div class="big-card-wrap">
  <div class="big-card-title">الهدف من النشاط</div>
  <p class="big-card-text">
    تعزيز قيم التضامن والرحمة والعدالة لدى الطالبات، وتنمية الوعي الإنساني
    واحترام حقوق الإنسان.
  </p>
</div>
""", unsafe_allow_html=True)

with c2:  # الوصف
    st.markdown("""
<div class="big-card-wrap">
  <div class="big-card-title">وصف النشاط</div>
  <p class="big-card-text">
    تنفيذ أنشطة تربوية توعوية بمناسبة اليوم العالمي للتضامن مع فلسطين.
  </p>
  <ul>
    <li>فقرة توعوية عن مفهوم التضامن</li>
    <li>مناقشة صفية</li>
    <li>نشاط كتابي</li>
    <li>لوحة صفية</li>
  </ul>
</div>
""", unsafe_allow_html=True)

with c3:  # الأثر
    st.markdown("""
<div class="big-card-wrap">
  <div class="big-card-title">الأثر التعليمي</di


# ===== Media Grid (Small cards like initiatives) =====
PHOTOS_DIR = Path("assets/tadamon/photos")
VIDEOS_DIR = Path("assets/tadamon/videos")

photos = []
if PHOTOS_DIR.exists():
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        photos += list(PHOTOS_DIR.glob(ext))
photos = sorted(photos)

videos = []
if VIDEOS_DIR.exists():
    for ext in ("*.mp4", "*.mov", "*.webm"):
        videos += list(VIDEOS_DIR.glob(ext))
videos = sorted(videos)

items = [("photo", p) for p in photos] + [("video", v) for v in videos]

if not items:
    st.info("مافي ملفات مضافة بعد. ضعي الصور داخل assets/tadamon/photos والفيديوات داخل assets/tadamon/videos")
else:
    cols = st.columns(3, gap="large")
    for i, (kind, path) in enumerate(items):
        with cols[i % 3]:
            st.markdown('<div class="media-card">', unsafe_allow_html=True)

            if kind == "photo":
                # Image card
                st.markdown(
                    f'<img src="{path.as_posix()}" />',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="media-caption">{path.name}</div>',
                    unsafe_allow_html=True
                )
            else:
                # Video card (use Streamlit video inside the card container)
                st.video(str(path))
                st.markdown(
                    f'<div class="media-caption">{path.name}</div>',
                    unsafe_allow_html=True
                )

            st.markdown('</div>', unsafe_allow_html=True)

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_tadamon", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
