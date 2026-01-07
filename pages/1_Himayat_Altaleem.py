import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# CSS (Same identity + cards)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }

.stApp { background-color: #F9FBFC; color:#333; direction: rtl; }

.block-container { padding-top: 1.5rem; max-width: 1000px; }

.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color: white;
  padding: 2.6em 1em;
  text-align: center;
  margin: -1.5rem -1rem 2.2rem -1rem;
}
.hero-title{ font-size: 2.5em; font-weight: 800; margin: 0; }
.hero-sub{ font-size: 1.05em; margin-top: 0.5em; opacity: .95; }

/* Big white card */
.page-card{
  background:#fff;
  border:1px solid #f0f0f0;
  border-radius:18px;
  padding: 1.9em;
  box-shadow: 0 8px 22px rgba(0,0,0,0.06);
}

/* Section title inside card */
.sec-title{
  color:#8A1538;
  font-weight:800;
  font-size: 1.5em;
  margin: 0.2em 0 0.6em 0;
}

.small{ color:#607d8b; font-size: 0.95em; margin-bottom: 1em; }
.hr{ border:none; border-top:1px solid #f1f1f1; margin: 1.2em 0; }

/* Gallery cards */
.media-card{
  background:#ffffff;
  border:1px solid #f0f0f0;
  border-radius:16px;
  padding: 1.2em;
  box-shadow: 0 6px 18px rgba(0,0,0,0.05);
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

# =========================
# Header
# =========================
st.markdown("""
<div class="hero">
  <div class="hero-title">حماية التعليم ضد الهجمات</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
</div>
""", unsafe_allow_html=True)

# =========================
# Main Card
# =========================
st.markdown('<div class="page-card">', unsafe_allow_html=True)

st.markdown('<div class="sec-title">تاريخ الفعالية</div>', unsafe_allow_html=True)
st.markdown('<div class="small">9 سبتمبر</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec-title">الهدف</div>', unsafe_allow_html=True)
st.write("تعزيز وعي الطالبات بأهمية حماية التعليم وحق التعلم في بيئة مدرسية آمنة.")

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec-title">أبرز الأنشطة</div>', unsafe_allow_html=True)
st.markdown("""
- عرض توعوي مبسط حول مفهوم التعليم الآمن  
- مناقشة صفية تفاعلية  
- نشاط كتابي قصير *(لماذا التعليم حق؟)*  
- إعداد لوحة صفية توعوية  
""")

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec-title">الأثر التعليمي</div>', unsafe_allow_html=True)
st.write("رفع مستوى الوعي لدى الطالبات وربط مفهوم حماية التعليم بسلوكيات إيجابية داخل المدرسة.")

st.markdown('<hr class="hr">', unsafe_allow_html=True)

# =========================
# Media Section
# =========================
st.markdown('<div class="sec-title">الصور والفيديوهات</div>', unsafe_allow_html=True)

st.markdown('<div class="media-card">', unsafe_allow_html=True)
st.caption("تقدرين تعرضين ملفات موجودة داخل GitHub (assets) أو ترفعين ملفات للعرض المؤقت داخل الصفحة.")

tab1, tab2 = st.tabs(["الصور", "الفيديوهات"])

ASSETS_PHOTOS = Path("assets/himayat/photos")
ASSETS_VIDEOS = Path("assets/himayat/videos")

with tab1:
    st.subheader("صور من GitHub")
    photos = []
    if ASSETS_PHOTOS.exists():
        for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
            photos += list(ASSETS_PHOTOS.glob(ext))
    photos = sorted(photos)

    if photos:
        st.image([str(p) for p in photos], use_container_width=True)
    else:
        st.info("مافي صور داخل assets/himayat/photos حاليًا.")

    st.divider()
    st.subheader("رفع صور للعرض (مؤقت)")
    up_photos = st.file_uploader(
        "اختاري صور",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        key="up_photos_himayat"
    )
    if up_photos:
        st.image(up_photos, use_container_width=True)

with tab2:
    st.subheader("فيديوهات من GitHub")
    videos = []
    if ASSETS_VIDEOS.exists():
        for ext in ("*.mp4", "*.mov", "*.webm"):
            videos += list(ASSETS_VIDEOS.glob(ext))
    videos = sorted(videos)

    if videos:
        for v in videos:
            st.video(str(v))
    else:
        st.info("مافي فيديوهات داخل assets/himayat/videos حاليًا.")

    st.divider()
    st.subheader("رفع فيديو للعرض (مؤقت)")
    up_video = st.file_uploader(
        "اختاري فيديو",
        type=["mp4", "mov", "webm"],
        accept_multiple_files=False,
        key="up_video_himayat"
    )
    if up_video:
        st.video(up_video)

st.markdown('</div>', unsafe_allow_html=True)  # close media-card
st.markdown('</div>', unsafe_allow_html=True)  # close page-card

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_himayat", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
