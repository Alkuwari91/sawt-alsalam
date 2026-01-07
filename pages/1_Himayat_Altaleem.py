import streamlit as st
from pathlib import Path
from styles import inject_global_css

st.set_page_config(
    page_title="حماية التعليم ضد الهجمات | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

st.markdown("""
<div class="hero">
  <div class="hero-title">حماية التعليم ضد الهجمات</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="sec">تاريخ الفعالية</div><div class="p">9 سبتمبر</div>', unsafe_allow_html=True)
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

# Media
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
    up = st.file_uploader("رفع صور للعرض (مؤقت)", type=["png","jpg","jpeg","webp"], accept_multiple_files=True, key="him_ph_up")
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
    upv = st.file_uploader("رفع فيديو للعرض (مؤقت)", type=["mp4","mov","webm"], accept_multiple_files=False, key="him_vid_up")
    if upv:
        st.video(upv)

st.markdown('</div>', unsafe_allow_html=True)  # close media
st.markdown('</div>', unsafe_allow_html=True)  # close card

st.write("")
if st.button("← العودة إلى الصفحة الرئيسية", key="back_home_himayat", use_container_width=True):
    st.switch_page("Home.py")

st.markdown('<div class="footer">© صوت السلام – مدرسة آمنة محمود الجيدة</div>', unsafe_allow_html=True)
