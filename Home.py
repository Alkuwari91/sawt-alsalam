import streamlit as st

st.set_page_config(
    page_title="صوت السلام",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ STYLE (Rasekhon-like cards, no icons) ============
st.markdown("""
<style>
/* remove extra top padding */
.block-container { padding-top: 1.2rem; }

/* header */
.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  padding: 34px 26px;
  border-radius: 22px;
  color: #fff;
  text-align: center;
}
.hero .title{ font-size: 36px; font-weight: 800; line-height: 1.2; }
.hero .sub{ font-size: 18px; margin-top: 8px; opacity: .95; }
.hero .tag{ font-size: 14px; margin-top: 10px; opacity: .85; }

/* cards row */
.card{
  background: #ffffff;
  border: 1px solid #f0f0f0;
  border-radius: 18px;
  padding: 20px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.04);
  height: 100%;
}
.card .h{ color:#8A1538; font-weight:800; font-size:20px; }
.card .d{ color:#666; margin-top:6px; font-size:14px; }
.card .p{ margin-top:12px; line-height:1.8; font-size:14px; color:#222; }

/* UNESCO boxes */
.box{
  background:#fff;
  border:1px solid #f0f0f0;
  border-radius:18px;
  padding:22px;
  height:100%;
}
.box .h{ color:#8A1538; font-weight:800; font-size:20px; }
.box .p{ margin-top:12px; line-height:1.9; font-size:15px; }
</style>
""", unsafe_allow_html=True)

# ============ HEADER ============
st.markdown("""
<div class="hero">
  <div class="title">صوت السلام</div>
  <div class="sub">مدرسة آمنة محمود الجيدة</div>
  <div class="tag">تعليمٌ آمن… ومستقبلٌ أكثر سلامًا</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### المبادرات والفعاليات")

c1, c2, c3 = st.columns(3, gap="large")

def card(title, date_text, desc):
    st.markdown(f"""
    <div class="card">
      <div class="h">{title}</div>
      <div class="d">{date_text}</div>
      <div class="p">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

with c1:
    card("حماية التعليم ضد الهجمات", "9 سبتمبر", "مبادرة توعوية لتعزيز حق التعليم الآمن وحماية المدارس كمساحات آمنة.")
    st.write("")
    if st.button("فتح الصفحة", key="go1", use_container_width=True):
        st.switch_page("pages/1_Himayat_Altaleem.py")

with c2:
    card("اليوم العالمي للتضامن مع فلسطين", "29 نوفمبر", "أنشطة تربوية وإنسانية لترسيخ قيم التضامن والعدالة والرحمة.")
    st.write("")
    if st.button("فتح الصفحة", key="go2", use_container_width=True):
        st.switch_page("pages/2_Tadamon_Filasteen.py")

with c3:
    card("يوم التعليم العالمي", "24 يناير", "احتفاء بالتعليم ودوره في بناء المستقبل وتنمية الدافعية للتعلم.")
    st.write("")
    if st.button("فتح الصفحة", key="go3", use_container_width=True):
        st.switch_page("pages/3_Yawm_Altaleem.py")

st.write("")
st.write("")

# ============ UNESCO VISION + MISSION (together) ============
st.markdown("### رؤية ورسالة مدارس اليونسكو")

v1, v2 = st.columns(2, gap="large")

with v1:
    st.markdown("""
    <div class="box">
      <div class="h">الرؤية</div>
      <div class="p">
        بناء جيل واعٍ يؤمن بالسلام، ويحترم حقوق الإنسان، ويقدّر التنوع الثقافي،
        ويساهم في تحقيق تعليم آمن وشامل للجميع.
      </div>
    </div>
    """, unsafe_allow_html=True)

with v2:
    st.markdown("""
    <div class="box">
      <div class="h">الرسالة</div>
      <div class="p">
        ترسيخ قيم السلام وحماية التعليم وتعزيز التضامن الإنساني عبر مبادرات تعليمية نوعية
        وأنشطة مدرسية هادفة داخل بيئة مدرسية آمنة.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("© صوت السلام | مدرسة آمنة محمود الجيدة")
