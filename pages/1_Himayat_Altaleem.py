import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# SAME CSS AS HOME (Unified)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }

.stApp{
  background-color:#F9FBFC;
  color:#333;
  direction: rtl;
}

/* نفس عرض الصفحة الرئيسية */
.block-container{
  padding-top: 1.5rem;
  max-width: 1100px;
}

/* Header نفس Home */
.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color: white;
  padding: 2.6em 1em;
  text-align: center;
  margin: -1.5rem -1rem 2.2rem -1rem;
}
.hero-title{ font-size: 2.6em; font-weight: 800; margin: 0; }
.hero-sub{ font-size: 1.1em; margin-top: .45em; opacity: .95; }

/* Card مثل Home */
.card{
  background:#ffffff;
  border-radius:16px;
  padding: 1.8em;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  border:1px solid #f0f0f0;
}

/* عناوين داخل الكارد بنفس لون Home */
.sec{
  color:#8A1538;
  font-weight:800;
  font-size: 1.5em;
  margin: 0.2em 0 0.6em 0;
}

/* نصوص */
.p{
  font-size: 1.02em;
  line-height: 1.9;
  margin: 0 0 0.8em 0;
}

/* خط فاصل لطيف */
.hr{
  border:none;
  border-top:1px solid #f1f1f1;
  margin: 1.1em 0;
}

/* قائمة RTL مرتبة */
ul{
  margin: 0.3em 0 0.6em 0;
  padding-right: 1.2em;
  line-height: 1.9;
  font-size: 1.02em;
}

/* Media section cards */
.media{
  background:#ffffff;
  border:1px solid #f0f0f0;
  border-radius:16px;
  padding: 1.2em;
  box-shadow: 0 6px 18px rgba(0,0,0,0.05);
  margin-top: 1.2em;
}

/* Footer نفس Home */
.footer{
  background-color:#6E0F2C;
  color:white;
  text-align:center;
  padding:1.1em;
  border-radius:14px;
  margin-top: 2.2em;
  font-size:.9em;
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
# Main Card (Everything inside)
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="sec">تاريخ الفعالية</div>', unsafe_allow_html=True)
st.markdown('<div class="p">9 سبتمبر</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec">الهدف</div>', unsafe_allow_html=True)
st.markdown('<div class="p">تعزيز وعي الطالبات بأهمية حماية التعليم وحق التعلم في بيئة مدرسية آمنة.</div>', unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec">أبرز الأنشطة</div>', unsafe_allow_html=True)
st.markdown("""
<ul>
  <li>عرض توعوي مبسط حول مفهوم التعليم الآمن</li>
  <li>مناقشة صفية تفاعلية</li>
  <li>نشاط كتابي قصير (لماذا التعليم حق؟)</li>
  <li>إعداد لوحة صفية توعوية</li>
</ul>
""", unsafe_allow_html=True)

st.markdown('<hr class="hr">', unsafe_allow_html=True)

st.markdown('<div class="sec">الأثر التعليمي</div>', unsafe_allow_html=True)
st.markdown('<div class="p">رفع مستوى الوعي لدى الطالبات وربط مفهوم حماية التعليم بسلوكيات إيجابية داخل المدرسة.</div>', unsafe_allow_html=True)

# =========================
# Photos & Videos (Optional) داخل نفس الكارد
# =========================
st.markdown('<hr class="hr">', unsafe_allow_html=True)
st.markdown('<div class="sec">الصور والفيديوهات</div>', unsafe_allow_html=True)

st.markdown('<div class="media">', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["الصور", "الفيديوهات"])

PHOTOS = Path("assets/himayat/photos")
VIDEOS = Path("assets/himayat/videos")

with tab1:
    photos = []
    if PHOTOS.exists():
        for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
            photos += list(PHOTOS.glob(ext))
    photos = sorted(photos)

    if photos:
        st.image([str(p) for p in photos], use_container_width=True)
    else:
        st.info("مافي صور مضافة بعد داخل assets/himayat/photos")

    st.divider()
    st.caption("رفع صور للعرض المؤقت داخل الصفحة:")
    up = st.file_uploader("اختاري صور", type=["png", "jpg", "jpeg", "webp"], accept_multiple_files=True, key="him_ph_up")
    if up:
        st.image(up, use_container_width=True)

with tab2:
    vids = []
    if VIDEOS.exists():
        for ext in ("*.mp4", "*.mov", "*.webm"):
            vids += list(VIDEOS.glob(ext))
    vids = sorted(vids)

    if vids:
        for v in vids:
            st.video(str(v))
    else:
        st.info("مافي فيديوهات مضافة بعد داخل assets/himayat/videos")

    st.divider()
    st.caption("رفع فيديو للعرض المؤقت داخل الصفحة:")
    upv = st.file_uploader("اختاري فيديو", type=["mp4", "mov", "webm"], accept_multiple_files=False, key="him_vid_up")
    if upv:
        st.video(upv)

st.markdown('</div>', unsafe_allow_html=True)  # close media

st.markdown('</div>', unsafe_allow_html=True)  # close card

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_himayat", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
