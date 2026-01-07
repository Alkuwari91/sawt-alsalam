import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
    /* ===== RTL Global ===== */
html, body, [class*="stApp"] {
  direction: rtl;
  text-align: right;
  font-family: "Cairo", "Segoe UI", sans-serif;
}

    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }

    .stApp{ background-color:#F9FBFC; color:#333; direction: rtl; }
    .block-container{ padding-top: 1.5rem; max-width: 1100px; }

    .hero{
      background: linear-gradient(135deg, #8A1538, #6E0F2C);
      color: white;
      padding: 2.6em 1em;
      text-align: center;
      margin: -1.5rem -1rem 2.2rem -1rem;
    }
    .hero-title{ font-size: 2.7em; font-weight: 800; margin: 0; }
    .hero-sub{ font-size: 1.15em; margin-top: .45em; opacity: .95; }
    .hero-tag{ font-size: .95em; margin-top: .8em; opacity: .85; }

    .section-title{
      color:#8A1538; text-align:center; font-size: 1.9em; font-weight:800;
      margin: 0.2em 0 1.4em 0;
    }

    .card{
      background:#ffffff;
      border-radius:16px;
      padding: 1.8em;
      box-shadow: 0 6px 18px rgba(0,0,0,0.06);
      border:1px solid #f0f0f0;
    }

    .sec{ color:#8A1538; font-weight:800; font-size: 1.5em; margin: 0.2em 0 0.6em 0; }
    .p{ font-size: 1.02em; line-height: 1.9; margin: 0 0 0.8em 0; }
    .hr{ border:none; border-top:1px solid #f1f1f1; margin: 1.1em 0; }

    ul{ margin: 0.3em 0 0.6em 0; padding-right: 1.2em; line-height: 1.9; font-size: 1.02em; }

    .media{
      background:#ffffff;
      border:1px solid #f0f0f0;
      border-radius:16px;
      padding: 1.2em;
      box-shadow: 0 6px 18px rgba(0,0,0,0.05);
      margin-top: 1.2em;
    }

    .footer{
      background-color:#6E0F2C;
      color:white;
      text-align:center;
      padding:1.1em;
      border-radius:14px;
      margin-top: 2.2em;
      font-size:.9em;
    }
    /* Streamlit bordered containers as "cards" */
div[data-testid="stVerticalBlockBorderWrapper"]{
  background:#ffffff !important;
  border:1px solid #f0f0f0 !important;
  border-radius:16px !important;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06) !important;
  padding: 1.2rem 1.2rem !important;
}
/* ===== Big Cards (Vision/Mission style) ===== */
.big-card-wrap{
  background:#ffffff;
  border-radius:22px;
  box-shadow: 0 10px 24px rgba(0,0,0,0.06);
  border:1px solid #f0f0f0;
  padding: 1.6rem 1.6rem;
  position: relative;
  overflow: hidden;
  min-height: 260px;
}
.big-card-wrap:after{
  content:"";
  position:absolute;
  top:0; bottom:0;
  left:0;            /* شريط جانبي */
  width:6px;
  background: linear-gradient(180deg, #8A1538, #6E0F2C);
}
.big-card-title{
  color:#8A1538;
  font-weight:800;
  font-size: 1.7em;
  margin: 0 0 .6rem 0;
  text-align: center;
}
.big-card-text{
  font-size: 1.05em;
  line-height: 2;
  margin: 0;
  color:#333;
  text-align: right;
}

/* ===== Small media cards (like initiative cards) ===== */
.media-grid-title{
  color:#8A1538;
  font-weight:800;
  font-size: 1.7em;
  margin: 0 0 1rem 0;
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
  font-size:.95em;
  color:#444;
  text-align:center;
}

    </style>
    """, unsafe_allow_html=True)
