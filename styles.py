def inject_global_css():
    import streamlit as st

    st.markdown(
        """
<style>
/* ===== RTL Global ===== */
html, body, [class*="stApp"]{
  direction: rtl;
  text-align: right;
  font-family: "Cairo","Segoe UI",sans-serif;
}

/* ===== Hero (if not already in your styles) ===== */
.hero{
  background: linear-gradient(135deg, #8A1538, #6E0F2C);
  color: #fff;
  padding: 2.2rem 1.2rem;
  border-radius: 22px;
  text-align:center;
  box-shadow: 0 10px 24px rgba(0,0,0,.10);
  margin-bottom: 1.2rem;
}
.hero-title{ font-size: 2.2rem; font-weight: 900; margin-bottom:.4rem; }
.hero-sub{ opacity:.95; font-size: 1.05rem; margin-bottom:.35rem; }
.hero-tag{
  display:inline-block;
  background: rgba(255,255,255,.14);
  border:1px solid rgba(255,255,255,.18);
  padding:.35rem .9rem;
  border-radius:999px;
  font-weight:700;
}

/* ===== Divider inside cards ===== */
.hr{ border:0; height:1px; background:#eee; margin: 1rem 0; }

/* ===== Big Cards (Vision/Mission style) ===== */
.big-card-wrap{
  background:#ffffff;
  border-radius:22px;
  box-shadow: 0 10px 24px rgba(0,0,0,0.06);
  border:1px solid #f0f0f0;
  padding: 1.6rem 1.6rem;
  position: relative;
  overflow: hidden;
  min-height: 280px;
  display:flex;
  flex-direction: column;
  justify-content:flex-start;
}
.big-card-wrap:after{
  content:"";
  position:absolute;
  top:0; bottom:0;
  right:0;     /* شريط للـ RTL */
  width:6px;
  background: linear-gradient(180deg, #8A1538, #6E0F2C);
}
.big-card-title{
  color:#8A1538;
  font-weight:900;
  font-size: 1.8rem;
  margin: 0 0 .6rem 0;
  text-align:center;
}
.big-card-text{
  font-size: 1.05rem;
  line-height: 2;
  margin: 0;
  color:#333;
}
.big-card-wrap ul{
  margin-top: .8rem;
  padding-right: 1.2rem;
}
.big-card-wrap li{
  margin-bottom: .4rem;
  line-height: 1.8;
}

/* ===== Media cards (like bottom initiatives) ===== */
.media-grid-title{
  color:#8A1538;
  font-weight:900;
  font-size: 2rem;
  margin: 1rem 0 1rem 0;
  text-align:center;
}
.media-card{
  background:#ffffff;
  border-radius:18px;
  box-shadow: 0 8px 22px rgba(0,0,0,0.06);
  border:1px solid #f0f0f0;
  padding: 0.9rem;
  overflow:hidden;
}
.media-card img{
  width:100%;
  height:170px;
  object-fit: cover;
  border-radius:12px;
  display:block;
}
.media-caption{
  margin-top:.65rem;
  font-size:.95rem;
  color:#444;
  text-align:center;
}

/* ===== Footer ===== */
.footer{
  margin-top: 1.2rem;
  text-align:center;
  color:#777;
  font-size:.9rem;
}
</style>
""",
        unsafe_allow_html=True,
    )
