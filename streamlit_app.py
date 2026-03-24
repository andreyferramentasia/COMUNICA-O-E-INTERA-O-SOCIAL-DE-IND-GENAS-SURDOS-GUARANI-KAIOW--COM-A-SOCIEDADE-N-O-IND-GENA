import streamlit as st
from pathlib import Path
from PIL import Image

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Indígenas Surdos Guarani-Kaiowá",
    page_icon="🪶",
    layout="wide",
)

# ── CSS – identidade visual da apresentação ───────────────────────────────────
st.markdown("""
<style>
/* Importa fonte */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

/* Reset de fundo e texto */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #FAF5EE !important;
    font-family: 'Montserrat', sans-serif;
}
[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"] { background: transparent; }

/* Cabeçalho principal */
.hero {
    background: linear-gradient(135deg, #6B3A1F 0%, #9C5A2D 40%, #C4842A 100%);
    border-radius: 0 0 40px 40px;
    padding: 60px 40px 50px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 10px;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background-image: repeating-linear-gradient(
        45deg,
        transparent, transparent 18px,
        rgba(255,255,255,0.05) 18px, rgba(255,255,255,0.05) 20px
    );
}
.hero-institution {
    color: #F5D5A8;
    font-size: 0.80rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.hero-title {
    color: #FFFFFF;
    font-size: 2.0rem;
    font-weight: 900;
    text-transform: uppercase;
    line-height: 1.25;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    margin-bottom: 24px;
}
.hero-meta {
    color: #F5D5A8;
    font-size: 0.85rem;
    font-weight: 600;
}
.hero-feather {
    font-size: 3rem;
    margin-bottom: 16px;
    display: block;
}

/* Faixa geométrica decorativa */
.geo-bar {
    height: 22px;
    background: repeating-linear-gradient(
        90deg,
        #8B4513 0px, #8B4513 20px,
        #C4842A 20px, #C4842A 30px,
        #FAF5EE 30px, #FAF5EE 40px,
        #9C5A2D 40px, #9C5A2D 60px,
        #FAF5EE 60px, #FAF5EE 70px
    );
    margin: 0 0 30px 0;
    border-radius: 0 0 8px 8px;
}

/* Seção */
.section-title {
    background: #555555;
    color: #FFFFFF;
    font-size: 1.25rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: 12px 24px;
    border-radius: 8px;
    display: inline-block;
    margin-bottom: 20px;
    box-shadow: 3px 3px 0px #333;
}

/* Card */
.card {
    background: #FFFFFF;
    border: 2px solid #E8D5B7;
    border-radius: 16px;
    padding: 28px 30px;
    margin-bottom: 20px;
    box-shadow: 0 4px 16px rgba(139,69,19,0.10);
}
.card-salmon {
    background: #FDF0E6;
    border: 2px solid #E8C49A;
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 16px;
    box-shadow: 0 2px 10px rgba(139,69,19,0.08);
}

/* Bullet com seta Guaraní */
.bullet-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 12px;
    font-weight: 700;
    font-size: 0.95rem;
    color: #2d1a0a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.bullet-arrow {
    color: #C4842A;
    font-size: 1.2rem;
    flex-shrink: 0;
    margin-top: 1px;
}

/* Badge / tag */
.badge {
    display: inline-block;
    background: #8B4513;
    color: #FAF5EE;
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin: 4px;
}

/* Citação de fechamento */
.quote-box {
    background: #FFFFFF;
    border-left: 6px solid #C4842A;
    border-radius: 0 16px 16px 0;
    padding: 28px 32px;
    margin: 30px 0;
    font-size: 1.15rem;
    font-weight: 700;
    color: #2d1a0a;
    text-transform: uppercase;
    line-height: 1.6;
    letter-spacing: 0.5px;
    box-shadow: 0 4px 16px rgba(139,69,19,0.10);
}
.quote-source {
    font-size: 0.78rem;
    color: #8B4513;
    font-weight: 700;
    margin-top: 10px;
}

/* Footer */
.footer {
    background: #6B3A1F;
    color: #F5D5A8;
    text-align: center;
    padding: 32px 20px;
    border-radius: 24px 24px 0 0;
    margin-top: 40px;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 1px;
}
.footer-title {
    font-size: 1rem;
    font-weight: 900;
    color: #FFFFFF;
    margin-bottom: 8px;
    text-transform: uppercase;
}

/* Imagem container */
.img-frame {
    background: #FFFFFF;
    border: 3px solid #C4842A;
    border-radius: 16px;
    padding: 14px;
    box-shadow: 0 6px 24px rgba(139,69,19,0.18);
    text-align: center;
    margin-bottom: 12px;
}
.img-caption {
    margin-top: 10px;
    font-size: 0.80rem;
    font-weight: 700;
    color: #6B3A1F;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Abas – texto visível em qualquer estado */
[data-testid="stTabs"] button[role="tab"] {
    color: #6B3A1F !important;
    font-weight: 700 !important;
    font-family: 'Montserrat', sans-serif !important;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    color: #FFFFFF !important;
    background-color: #8B4513 !important;
    border-radius: 8px 8px 0 0;
}
[data-testid="stTabs"] button[role="tab"]:hover {
    color: #9C5A2D !important;
}

/* Zigzag bottom decoration */
.zigzag {
    height: 30px;
    background:
        linear-gradient(135deg, #FAF5EE 25%, transparent 25%) -20px 0,
        linear-gradient(225deg, #FAF5EE 25%, transparent 25%) -20px 0,
        linear-gradient(315deg, #FAF5EE 25%, transparent 25%),
        linear-gradient(45deg, #FAF5EE 25%, transparent 25%);
    background-size: 40px 30px;
    background-color: #C4842A;
    margin: 20px 0 10px 0;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
  <span class="hero-feather">🪶</span>
  <div class="hero-institution">
    Universidade Federal da Grande Dourados &nbsp;·&nbsp;
    Faculdade Intercultural Indígena &nbsp;·&nbsp;
    PPGET &nbsp;·&nbsp; Linha: Educação e Diversidade
  </div>
  <div class="hero-title">
    Comunicação e Interação Social de<br>
    Indígenas Surdos Guarani-Kaiowá<br>
    com a Sociedade Não Indígena:<br>
    Um Estudo de Caso sobre o Papel da LIBRAS
  </div>
  <div class="hero-meta">
    Mestranda: Camila Carollo Trento &nbsp;|&nbsp;
    Orientadora: Prof.ª Dr.ª Luciana Lopes Coelho &nbsp;|&nbsp; Dourados · 2026
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="geo-bar"></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 – INQUIETAÇÃO / PROBLEMA
# ══════════════════════════════════════════════════════════════════════════════
col_l, col_r = st.columns([1, 1], gap="large")

with col_l:
    st.markdown('<div class="section-title">Uma Inquietação que Nasceu na Escola</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-salmon">
      <div class="bullet-item"><span class="bullet-arrow">▶</span>
        Como uma criança indígena surda se comunica com sua família?
      </div>
      <div class="bullet-item"><span class="bullet-arrow">▶</span>
        Existe uma língua compartilhada?
      </div>
      <div class="bullet-item"><span class="bullet-arrow">▶</span>
        Que sinais utilizam?
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Problematização</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <div class="bullet-item"><span class="bullet-arrow">❯</span>
        Como a escola e professora de AEE poderiam colaborar com a comunicação
        da criança e sua família?
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    st.markdown('<div class="section-title">Objetivos</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
      <p style="font-weight:900;text-transform:uppercase;color:#8B4513;margin-bottom:12px;">Geral</p>
      <div class="bullet-item"><span class="bullet-arrow">◆</span>
        Investigar o ensino plurilíngue de uma estudante indígena surda Kaiowá.
      </div>
      <p style="font-weight:900;text-transform:uppercase;color:#8B4513;margin:16px 0 12px;">Específicos</p>
      <div class="bullet-item"><span class="bullet-arrow">1.</span>Analisar cultura e interações familiares</div>
      <div class="bullet-item"><span class="bullet-arrow">2.</span>Identificar formas de comunicação familiar</div>
      <div class="bullet-item"><span class="bullet-arrow">3.</span>Refletir sobre o ensino plurilíngue na escola</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 – METODOLOGIA
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Metodologia</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5, gap="medium")
for col, icon, label in zip(
    [c1, c2, c3, c4, c5],
    ["🔍", "📋", "🔎", "👁️", "🏫"],
    ["Abordagem\nEtnográfica", "Estudo\nde Caso", "Pesquisa Exploratória\ne Descritiva", "Observação\nParticipante", "Acompanhamento\nEscola · Família · Interações"],
):
    with col:
        st.markdown(f"""
        <div class="card" style="text-align:center;padding:20px 14px;">
          <div style="font-size:2rem;">{icon}</div>
          <div style="font-weight:900;text-transform:uppercase;font-size:0.80rem;color:#6B3A1F;
                      line-height:1.4;margin-top:8px;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 – GALERIA DE IMAGENS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Materiais Produzidos</div>', unsafe_allow_html=True)

# Coleta todas as imagens da pasta imagens/
img_dir = Path(__file__).parent / "imagens"
supported = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}
image_files = sorted([f for f in img_dir.iterdir() if f.suffix.lower() in supported])

def friendly(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").title()

if not image_files:
    st.info("Nenhuma imagem encontrada na pasta `imagens/`. Adicione imagens lá para exibi-las aqui.")
else:
    IMGS_PER_TAB = 6
    COLS = 3
    chunks = [image_files[i : i + IMGS_PER_TAB] for i in range(0, len(image_files), IMGS_PER_TAB)]
    tab_labels = [f"Galeria {i + 1}" for i in range(len(chunks))]
    tabs = st.tabs(tab_labels)

    for tab, chunk in zip(tabs, chunks):
        with tab:
            rows = [chunk[i : i + COLS] for i in range(0, len(chunk), COLS)]
            for row in rows:
                cols = st.columns(COLS, gap="medium")
                for col, img_path in zip(cols, row):
                    with col:
                        try:
                            img = Image.open(img_path)
                            st.markdown('<div class="img-frame">', unsafe_allow_html=True)
                            st.image(img, use_container_width=True)
                            st.markdown(
                                f'<div class="img-caption">{friendly(img_path)}</div>',
                                unsafe_allow_html=True,
                            )
                            st.markdown('</div>', unsafe_allow_html=True)
                        except Exception:
                            st.warning(f"Não foi possível carregar: {img_path.name}")

    st.markdown(f"""
    <div style="text-align:center;margin-top:10px;font-size:0.82rem;color:#8B4513;font-weight:600;">
        {len(image_files)} imagem(ns) · {len(chunks)} aba(s) · Adicione mais arquivos à pasta
        <code>imagens/</code> para que apareçam automaticamente.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 – RESULTADOS
# ══════════════════════════════════════════════════════════════════════════════
col_res, col_extra = st.columns([3, 2], gap="large")

with col_res:
    st.markdown('<div class="section-title">Principais Resultados</div>', unsafe_allow_html=True)
    resultados = [
        "Melhoria significativa da comunicação familiar",
        "Maior participação da criança na escola",
        "Fortalecimento do vínculo entre mãe e filha",
        "Aumento da autoestima da criança",
        "Participação ativa da família",
    ]
    items = "".join(
        f'<div class="bullet-item"><span class="bullet-arrow">✦</span>{r}</div>'
        for r in resultados
    )
    st.markdown(f'<div class="card">{items}</div>', unsafe_allow_html=True)

with col_extra:
    st.markdown('<div class="section-title">Um Resultado Além do Esperado</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card-salmon" style="text-align:center;padding:30px;">
      <div style="font-size:2.5rem;">📚</div>
      <div style="font-weight:900;text-transform:uppercase;color:#6B3A1F;
                  font-size:0.95rem;margin-top:16px;line-height:1.6;">
        A mãe decidiu retornar aos estudos<br>e ingressou na Educação de<br>Jovens e Adultos (EJA).
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5 – CONTRIBUIÇÕES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">Contribuições da Pesquisa</div>', unsafe_allow_html=True)

contrib_cols = st.columns(2, gap="medium")
contribuicoes = [
    ("🏡", "Fortalecimento da comunicação no ambiente familiar"),
    ("🪶", "Valorização da língua materna e da cultura indígena"),
    ("🤝", "Trabalho colaborativo entre família e escola"),
    ("📖", "Ampliação dos estudos sobre crianças indígenas surdas"),
]
for i, (icon, text) in enumerate(contribuicoes):
    with contrib_cols[i % 2]:
        st.markdown(f"""
        <div class="card-salmon" style="display:flex;align-items:center;gap:16px;">
          <div style="font-size:1.8rem;flex-shrink:0;">{icon}</div>
          <div style="font-weight:700;text-transform:uppercase;font-size:0.88rem;
                      color:#2d1a0a;letter-spacing:0.5px;">{text}</div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# CITAÇÃO FINAL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="quote-box">
  "Assim como a Língua Portuguesa, a LIBRAS atua como uma ponte de comunicação
  e interação social."
  <div class="quote-source">(ORTIZ, 2022, p. 21)</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote-box" style="border-left-color:#8B4513;font-size:1.05rem;">
  "A educação escolar de uma criança indígena surda é mais do que ensinar
  palavras ou sinais. É construir caminhos de comunicação, identidade e
  pertencimento."
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="zigzag"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
  <div class="footer-title">
    Comunicação e Interação Social de Indígenas Surdos Guarani-Kaiowá
  </div>
  Universidade Federal da Grande Dourados · Faculdade Intercultural Indígena · PPGET<br>
  Mestranda: Camila Carollo Trento · Orientadora: Prof.ª Dr.ª Luciana Lopes Coelho · Dourados · 2026
</div>
""", unsafe_allow_html=True)
