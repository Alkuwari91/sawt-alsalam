import streamlit as st

def inject_global_css():
    st.markdown(
        """
<style>
/* =========================
   GLOBAL: LIGHT + RTL
========================= */
:root{
  --brand1:#8A1538;   /* Qatar maroon */
  --brand2:#6E0F2C;
  --bg:#F9FBFC;
  --card:#FFFFFF;
  --text:#111111;
  --muted:#666;
  --border:#EEF1F4;
  --shadow: 0 10px 24px rgba(0,0,0,0.06);
}

html, body, [class*="stApp"]{
  direction: rtl !important;
  text-align: right !important;
  font-family: "Cairo","Segoe UI",sans-serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}

.stApp{
  background: var(--bg) !important;
}

/* main container spacing */
.block-container{
  padding-top: 1.2rem !important;
  padding-bottom: 2rem !important;
  max-width: 1250px !important;
}

/* hide default top gap */
header[data-testid="stHeader"]{
  background: transparent !important;
}

/* sidebar (even if collapsed) */
section[data-testid="stSidebar"]{
  background: #fff !important;
  border-left: 1px solid var(--border) !important;
}

/* remove Streamlit focus outlines look ugly */
*:focus { outline: none !important; }

/* =========================
   HERO HEADER
========================= */
.hero{
  background: linear-gradient(135deg, var(--brand1), var(--brand2));
  color: #fff;
  padding: 1.7rem 1.3rem;
  border-radius: 22px;
  text-align:center;
  box-shadow: 0 10px 24px rgba(0,0,0,.10);
  margin: 0.2rem 0 1.2rem 0;
}
.hero-title{
  font-size: 2.1rem;
  font-weight: 900;
  margin-bottom: .35rem;
  letter-spacing: .2px;
}
.hero-sub{
  opacity: .95;
  font-size: 1.05rem;
  margin-bottom: .35rem;
}
.hero-tag{
  display:inline-block;
  background: rgba(255,255,255,.14);
  border:1px solid rgba(255,255,255,.18);
  padding:.35rem .95rem;
  border-radius:999px;
  font-weight:800;
  font-size:.95rem;
}

/* =========================
   SECTION TITLES
========================= */
.h2{
  font-size: 2rem;
  font-weight: 900;
  color: var(--brand1);
  text-align:center;
  margin: 1.2rem 0 1.0rem 0;
}

/* divider inside cards */
.hr{
  border:0;
  height:1px;
  background: #EEE;
  margin: 1rem 0;
}

/* =========================
   BIG CARDS (Vision/Mission style)
========================= */
.big-card-wrap{
  background: var(--card);
  border-radius: 22px;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  padding: 1.6rem 1.6rem;
  position: relative;
  overflow: hidden;

  /* keep them balanced */
  min-height: 280px;
  display:flex;
  flex-direction: column;
  justify-content:flex-start;
}

.big-card-wrap:after{
  content:"";
  position:absolute;
  top:0; bottom:0;
  right:0;            /* RTL strip */
  width:6px;
  background: linear-gradient(180deg, var(--brand1), var(--brand2));
}

.big-card-title{
  color: var(--brand1);
  font-weight: 900;
  font-size: 1.75rem;
  margin: 0 0 .7rem 0;
  text-align:center;
}

.big-card-text{
  font-size: 1.05rem;
  line-height: 2;
  margin: 0;
  color: #333;
}

.big-card-wrap ul{
  margin-top: .85rem;
  padding-right: 1.2rem;
}
.big-card-wrap li{
  margin-bottom: .45rem;
  line-height: 1.9;
  color:#222;
}

/* =========================
   HOME: Small initiative cards (like Rasekhon)
========================= */
.grid-title{
  color: var(--brand1);
  font-weight: 900;
  font-size: 2rem;
  margin: 1.4rem 0 1rem 0;
  text-align:center;
}

.tile{
  background: var(--card);
  border-radius: 22px;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  padding: 1.2rem 1.2rem 1.0rem 1.2rem;
  min-height: 240px;
  display:flex;
  flex-direction: column;
  justify-content: space-between;
}

.tile-date{
  color: #777;
  font-size: .95rem;
  margin-bottom: .35rem;
}

.tile-title{
  color: var(--brand1);
  font-weight: 900;
  font-size: 1.45rem;
  margin: .2rem 0 .6rem 0;
  line-height: 1.6;
}

.tile-desc{
  color:#333;
  font-size: 1.03rem;
  line-height: 1.9;
  margin: 0 0 1rem 0;
}

.btn-primary{
  width:100%;
  border: none !important;
  background: #0F172A !important; /* نفس زرّك الداكن */
  color: #fff !important;
  padding: .9rem 1rem !important;
  border-radius: 14px !important;
  font-weight: 900 !important;
  cursor: pointer;
  text-align:center;
}

/* Streamlit button tweak to match */
div.stButton > button{
  width: 100%;
  background: #0F172A !important;
  color: #fff !important;
  border: none !important;
  padding: .85rem 1rem !important;
  border-radius: 14px !important;
  font-weight: 900 !important;
}
div.stButton > button:hover{
  opacity: .92;
}

/* =========================
   MEDIA GRID (photos/videos) small cards
========================= */
.media-grid-title{
  color: var(--brand1);
  font-weight: 900;
  font-size: 2rem;
  margin: 1.2rem 0 1rem 0;
  text-align:center;
}

.media-card{
  background: var(--card);
  border-radius: 18px;
  box-shadow: 0 8px 22px rgba(0,0,0,0.06);
  border: 1px solid var(--border);
  padding: 0.9rem;
  overflow:hidden;
}

.media-card img{
  width:100%;
  height: 180px;
  object-fit: cover;
  border-radius: 12px;
  display:block;
}

.media-caption{
  margin-top: .65rem;
  font-size: .95rem;
  color: #444;
  text-align:center;
}

/* video inside cards spacing */
.media-card video{
  border-radius: 12px;
}

/* =========================
   FOOTER
========================= */
.footer{
  margin-top: 1.4rem;
  text-align:center;
  color: #777;
  font-size: .9rem;
}
</style>
""",
        unsafe_allow_html=True,
    )
