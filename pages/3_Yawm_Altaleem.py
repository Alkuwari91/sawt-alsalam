import streamlit as st
from pathlib import Path
from styles import inject_global_css

st.set_page_config(
    page_title="يوم التعليم العالمي | صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# ===== Header =====
st.markdown(
    """
<div class="hero">
  <div class="hero-title">يوم التعليم العالمي</div>
  <div class="hero-sub">صوت السلام | مدرسة آمنة محمود الجيدة</div>
  <div class="hero-tag">24 يناير – التعليم حق… ويصنع المستقبل</div>
</div>
""",
    unsafe_allow_html=True,
)

# ===== 3 columns =====
col1, col2, col3 = st.columns(3, gap="large")

# ===== Card 1: الهدف =====
with col1:
    c1 = st.container()
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">الهدف من النشاط</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="p">تعزيز قيمة التعليم لدى الطالبات، ورفع الدافعية للتعلّم، وربط التعليم ببناء المستقبل وتنمية المهارات ضمن بيئة مدرسية آمنة وداعمة.</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

# ===== Card 2: وصف النشاط =====
with col2:
    c2 = st.container()
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">وصف النشاط</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="p">تنفيذ أنشطة مدرسية احتفالية وتربوية بمناسبة يوم التعليم العالمي، تضمنت رسائل تحفيزية عن أهمية التعليم، ومشاركة الطالبات في أنشطة كتابية/فنية تعبّر عن أحلامهن وطموحاتهن ودور التعليم في تحقيقها.</div>',
            unsafe_allow_html=True,
        )
        st.markdown('<hr class="hr">', unsafe_allow_html=True)
        st.markdown(
            """
<ul>
  <li>فقرة تحفيزية: لماذا التعليم مهم لحياتنا؟</li>
  <li>نشاط كتابي: "هدفي المستقبلي وكيف يساعدني التعليم"</li>
  <li>عمل فني/ملصق صفّي عن قيمة التعليم</li>
  <li>ركن مدرسي لعرض أعمال الطالبات</li>
</ul>
""",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

# ===== Card 3: معرض الصور =====
with col3:
    c3 = st.container()
    with c3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="sec">معرض الصور</div>', unsafe_allow_html=True)
        st.caption("صور من GitHub داخل: assets/yawm/photos (أو ارفعي صور للعرض المؤقت)")

        photos_dir = Path("assets/yawm/photos")

        photos = []
        if photos_dir.exists():
            for ext in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
                photos +=
