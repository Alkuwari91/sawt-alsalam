import streamlit as st
from pathlib import Path
from styles import inject_global_css

# ملاحظة: إذا Home.py فقط هو اللي فيه set_page_config
# احذفي هذا الجزء من هنا عشان ما يطلع لك Error
st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
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
  <div class="hero-title">حماية التعليم ضد الهجمات</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">9 سبتمبر</div>
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
    تعزيز وعي الطالبات بأهمية حماية التعليم وحق التعلّم،
    وترسيخ مفهوم المدرسة الآمنة كبيئة داعمة للتعلّم،
    وتنمية المسؤولية المجتمعية تجاه حماية المؤسسات التعليمية.
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
    تنفيذ نشاط توعوي بمناسبة اليوم الدولي لحماية التعليم من الهجمات،
    تضمّن رسائل تربوية عن حق التعليم وأهمية توفير بيئة مدرسية آمنة،
    ومشاركة الطالبات في أنشطة صفّية تعزّز مفهوم الأمن والسلام داخل المدرسة.
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

PHOTOS_DIR = Path("assets/himayat/photos")
VIDEOS_DIR = Path("assets/himayat/videos")

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
        "ضعي الصور داخل: assets/himayat/photos\n"
        "وضعي الفيديوات داخل: assets/himayat/videos"
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
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_himayat", use_container_width=True):
    st.switch_page("Home.py")

st.markdown(
    '<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>',
    unsafe_allow_html=True,
)
