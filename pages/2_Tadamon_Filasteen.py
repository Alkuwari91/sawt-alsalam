import streamlit as st
from pathlib import Path
from styles import inject_global_css

# إذا Home.py فقط فيه set_page_config
# احذفي هذا الجزء لو مكرر عندك
st.set_page_config(
    page_title="اليوم العالمي للتضامن مع فلسطين | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# =========================
# HEADER
# =========================
st.markdown(
    """
<div class="hero">
  <div class="hero-title">اليوم العالمي للتضامن مع فلسطين</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">29 نوفمبر</div>
</div>
""",
    unsafe_allow_html=True,
)

# =========================
# 2 BIG CARDS (مثل الرؤية والرسالة)
# =========================
c2, c1 = st.columns(2, gap="large")

with c1:  # الهدف (يمين)
    st.markdown(
        """
<div class="big-card-wrap">
  <div class="big-card-title">الهدف من النشاط</div>
  <p class="big-card-text">
    ترسيخ قيم التضامن الإنساني والعدالة لدى الطالبات،
    وتنمية الوعي بحقوق الشعوب، وتعزيز التعاطف والسلام
    من خلال أنشطة تربوية هادفة داخل البيئة المدرسية.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

with c2:  # وصف المشروع (يسار)
    st.markdown(
        """
<div class="big-card-wrap">
  <div class="big-card-title">وصف المشروع</div>
  <p class="big-card-text">
    تنفيذ نشاط توعوي بمناسبة اليوم العالمي للتضامن مع فلسطين،
    تضمّن رسائل تربوية حول معاني التضامن والإنسانية،
    ومشاركة الطالبات في أنشطة صفّية وفنية تعبّر عن
    قيم السلام والتعاطف واحترام حقوق الإنسان.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

# =========================
# GALLERY تحتهم بالنص
# =========================
st.write("")
st.markdown(
    '<div class="media-grid-title">معرض الصور والفيديوات</div>',
    unsafe_allow_html=True,
)

PHOTOS_DIR = Path("assets/tadamon/photos")
VIDEOS_DIR = Path("assets/tadamon/videos")

photos = []
if PHOTOS_DIR.exists():
    for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        photos += list(PHOTOS_DIR.glob(ext))
photos = sorted(photos)

videos = []
if VIDEOS_DIR.exists():
    for ext in ("*.mp4","*.MP4","*.mov","*.MOV","*.webm","*.WEBM","*.m4v","*.M4V"):
        videos += list(VIDEOS_DIR.glob(ext))
videos = sorted(videos)

items = [("photo", p) for p in photos] + [("video", v) for v in videos]

if not items:
    st.info(
        "مافي ملفات مضافة بعد.\n\n"
        "ضعي الصور داخل: assets/tadamon/photos\n"
        "وضعي الفيديوات داخل: assets/tadamon/videos"
    )
else:
    cols = st.columns(3, gap="large")
    for i, (kind, path) in enumerate(items):
        with cols[i % 3]:
            st.markdown('<div class="media-card">', unsafe_allow_html=True)

            if kind == "photo":
                st.image(str(path), use_container_width=True)
            else:
                st.video(str(path))

            st.markdown(
                f'<div class="media-caption">{path.name}</div>',
                unsafe_allow_html=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)

# =========================
# BACK + FOOTER
# =========================
st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_tadamon", use_container_width=True):
    st.switch_page("Home.py")

st.markdown(
    '<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>',
    unsafe_allow_html=True,
)
