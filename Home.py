import streamlit as st
from styles import inject_global_css

st.set_page_config(
    page_title="صوت السلام | مدرسة آمنة محمود الجيدة",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_global_css()

# =========================
# PAGE CONFIG
# =========================

# =========================
# GLOBAL CSS (RASEKHON STYLE)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.stApp {
    background-color: #F9FBFC;
    color: #333;
    direction: rtl;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1100px;
}

/* ===== Header ===== */
.hero{
    position: relative;
    background: linear-gradient(135deg, #8A1538, #6E0F2C);
    color: white;
    padding: 3.2em 1em 2.6em 1em;  /* ✅ زيادة مساحة فوق عشان الشعارات */
    text-align: center;
    margin: -1.5rem -1rem 2.2rem -1rem;
}

/* شريط الشعارات أعلى الهيدر */
.hero-logos{
    position: absolute;
    top: 18px;
    right: 18px;          /* ✅ RTL: يمين */
    display: flex;
    gap: 12px;
    align-items: center;
}

/* حجم شكل الشعارات */
.hero-logos img{
    height: 56px;
    width: auto;
    object-fit: contain;
    background: rgba(255,255,255,0.92); /* خلفية بيضاء خفيفة عشان يبانون */
    padding: 6px;
    border-radius: 12px;
}


.hero-title {
    font-size: 2.8em;
    font-weight: 800;
}

.hero-sub {
    font-size: 1.25em;
    margin-top: 0.4em;
    opacity: 0.95;
}

.hero-tag {
    font-size: 0.95em;
    margin-top: 0.8em;
    opacity: 0.85;
}

/* ===== Section title ===== */
.section-title {
    color: #8A1538;
    text-align: center;
    font-size: 1.9em;
    font-weight: 800;
    margin-bottom: 1.4em;
}

/* ===== Cards ===== */
.card {
    background: #ffffff;
    border-radius: 16px;
    padding: 1.7em;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    transition: transform 0.3s, box-shadow 0.3s;
    height: 100%;
    border: 1px solid #f0f0f0;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 28px rgba(138,21,56,0.25);
}

.card h3 {
    color: #8A1538;
    font-size: 1.18em;
    font-weight: 800;
}

.card .date {
    font-size: 0.9em;
    color: #607d8b;
    margin-bottom: 0.8em;
}

.card p {
    font-size: 0.95em;
    line-height: 1.7;
}

/* ===== Vision & Mission ===== */
.vm-box {
    background: white;
    border-radius: 16px;
    padding: 1.7em;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    border-right: 4px solid #8A1538;
}

.vm-box h4 {
    color: #8A1538;
    font-size: 1.45em;
    font-weight: 800;
}

.vm-box p {
    line-height: 1.9;
}

/* ===== Footer ===== */
.footer {
    background-color: #6E0F2C;
    color: white;
    text-align: center;
    padding: 1.2em;
    border-radius: 14px;
    margin-top: 3em;
}
</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================
st.markdown(
    """
<div class="hero">
    <div class="hero-logos">
        <img src="assets/logos/moehe_qatar.png" alt="MOEHE Qatar">
        <img src="assets/logos/unesco.png" alt="UNESCO">
    </div>

    <div class="hero-title">صوت السلام</div>
    <div class="hero-sub">في ظل مدرسة آمنة محمود الجيدة</div>
    <div class="hero-tag">تعليمٌ آمن… ومستقبلٌ أكثر سلامًا</div>
</div>
""",
    unsafe_allow_html=True,
)




# =========================
# VISION & MISSION (UNESCO)
# =========================
st.markdown('<div class="section-title">رؤية ورسالة مدارس اليونسكو</div>', unsafe_allow_html=True)

v1, v2 = st.columns(2, gap="large")

with v1:
    st.markdown(
        """
    <div class="vm-box">
        <h4>الرؤية</h4>
        <p>
        تحقيق تعليم نوعي يُسهم في بناء جيل واعٍ ومسؤول، يؤمن بثقافة السلام، ويحترم حقوق الإنسان، ويقدّر التنوع الثقافي، ويسهم بفاعلية في تحقيق التنمية المستدامة والمواطنة العالمية.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with v2:
    st.markdown(
        """
    <div class="vm-box">
        <h4>الرسالة</h4>
        <p>
        العمل على توفير بيئة تعليمية شاملة وآمنة، تُعزّز قيم السلام والحوار والتسامح، وتنمّي التفكير النقدي والمسؤولية المجتمعية لدى الطلبة، من خلال برامج وأنشطة تعليمية وتربوية تتوافق مع مبادئ اليونسكو وأهدافها في التعليم من أجل السلام والتنمية المستدامة.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
# =========================
# TABS AS CARDS
# =========================
st.markdown('<div class="section-title">المبادرات والفعاليات</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown(
        """
    <div class="card">
        <div class="date">9 سبتمبر</div>
        <h3>حماية التعليم ضد الهجمات</h3>
        <p>
        مبادرة توعوية لتعزيز حق التعليم الآمن
        وحماية المدارس كمساحات تعليمية آمنة.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("فتح الصفحة", key="open_himayat", use_container_width=True):
        st.switch_page("pages/1_Himayat_Altaleem.py")

with c2:
    st.markdown(
        """
    <div class="card">
        <div class="date">29 نوفمبر</div>
        <h3>اليوم العالمي للتضامن مع فلسطين</h3>
        <p>
        أنشطة تربوية وإنسانية لترسيخ قيم
        التضامن والعدالة والرحمة.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("فتح الصفحة", key="open_filasteen", use_container_width=True):
        st.switch_page("pages/2_Tadamon_Filasteen.py")

with c3:
    st.markdown(
        """
    <div class="card">
        <div class="date">24 يناير</div>
        <h3>يوم التعليم العالمي</h3>
        <p>
        احتفاء بالتعليم ودوره في بناء المستقبل
        وتنمية الدافعية للتعلم.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    if st.button("فتح الصفحة", key="open_edu", use_container_width=True):
        st.switch_page("pages/3_Yawm_Altaleem.py")
# =========================
# FOOTER
# =========================
st.markdown(
    """
<div class="footer">
    © صوت السلام – مدرسة آمنة محمود الجيدة
</div>
""",
    unsafe_allow_html=True,
)
