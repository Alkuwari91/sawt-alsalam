import streamlit as st
from styles import inject_global_css
from pathlib import Path
import base64

# مسار مجلد الشعارات
LOGOS_DIR = Path(__file__).parent / "assets" / "logos"

def img_to_data_uri(p: Path) -> str:
    data = p.read_bytes()
    ext = p.suffix.lower().replace(".", "")
    if ext == "jpg":
        ext = "jpeg"
    return f"data:image/{ext};base64,{base64.b64encode(data).decode('utf-8')}"


# =========================
# GLOBAL CSS (RASEKHON STYLE)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');

html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }

.stApp{
  background-color:#F9FBFC;
  color:#333;
  direction:rtl;
}

.block-container{
  padding-top:1.5rem;
  max-width:1100px;
}

/* ===== Header ===== */
.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color:white;
  padding: 2.6em 1em;
  text-align:center;
  margin: -1.5rem -1rem 2.2rem -1rem;
  border-radius: 18px;
  position: relative;
}

/* logos row */
/* logos (يمين + يسار) */
.hero-logo-right,
.hero-logo-left{
  position:absolute;
  top:16px;
  z-index: 10;
}

.hero-logo-right{
  right:16px;
}

.hero-logo-left{
  left:16px;
}

.hero-logo-right img,
.hero-logo-left img{
  height:42px;
  width:auto;
  background: rgba(255,255,255,0.92);
  padding:6px 10px;
  border-radius:10px;
}

/* text */
.hero-title{ font-size:2.8em; font-weight:800; }
.hero-sub{ font-size:1.25em; margin-top:0.4em; opacity:0.95; }
.hero-tag{ font-size:0.95em; margin-top:0.8em; opacity:0.85; }

/* ===== Section title ===== */
.section-title{
  color:#8A1538;
  text-align:center;
  font-size:1.9em;
  font-weight:800;
  margin-bottom:1.4em;
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

unesco_src = img_to_data_uri(LOGOS_DIR / "UNESCO.png")
moehe_src  = img_to_data_uri(LOGOS_DIR / "moehe_qatar.png")

/* ===== Header ===== */
.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color:white;
  padding: 4.2em 1em 2.6em;   /* ✅ زدنا البادينق من فوق عشان اللوقوات تبين */
  text-align:center;
  margin: -1.5rem -1rem 2.2rem -1rem;
  border-radius: 18px;
  position: relative;
  overflow: visible;
}

/* logos (يمين + يسار) */
.hero-logo-right,
.hero-logo-left{
  position:absolute;
  top:22px;                 /* ✅ نزلناهم شوي تحت بعيد عن شريط Streamlit */
  z-index: 9999;            /* ✅ فوق أي عنصر */
}

.hero-logo-right{ right:16px; }
.hero-logo-left{ left:16px; }

.hero-logo-right img,
.hero-logo-left img{
  height:52px;              /* ✅ كبرناهم شوي */
  width:auto;
  background: rgba(255,255,255,0.92);
  padding:8px 12px;
  border-radius:12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}


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
