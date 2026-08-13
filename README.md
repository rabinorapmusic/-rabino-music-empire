import streamlit as st
import time

st.set_page_config(page_title="RABINO RAP MUSIC PRO-MAX", layout="centered", page_icon="🎤")

st.markdown('<div style="font-size:100px;text-align:center;animation:pulse 2s infinite;">🎤</div>', unsafe_allow_html=True)
st.markdown('<style>@keyframes pulse {0%{transform: scale(1);} 50%{transform: scale(1.1);} 100%{transform: scale(1);}}</style>', unsafe_allow_html=True)
st.title("🔥 LA CABINA")
st.subheader("RABINO RAP MUSIC PRO-MAX")
st.markdown("---")

# CAMPO 1
nombre = st.text_input("👤 Nombre del Artista", "Rabino")

# CAMPO 2
col1, col2 = st.columns(2)
with col1:
    genero_bpm = {"Reggaeton": 100, "Dembow": 95, "Bachata": 120, "Trap": 140, "Rap": 85, "Rap Cristiano": 90}
    genero = st.selectbox("🎵 Género", list(genero_bpm.keys()))
    bpm_auto = genero_bpm[genero]
with col2:
    st.metric("⚡ BPM", bpm_auto)

# CAMPO 3
col3, col4, col5 = st.columns(3)
with col3: modo = st.radio("🎙️ Modo", ["Solo", "Dúo"])
with col4: idioma = st.selectbox("🌎 Idioma", ["Español", "English", "Bilingüe EN/ES"])
with col5: vibe = st.selectbox("🔥 Vibe", ["Cristiano", "Secular", "Romántico", "Calle"])

# CAMPO 4
tema = st.text_area("📖 Tema de la canción / Letra", "Ej: victoria, bendición")

if st.button("🚀 GENERAR HIT PARA SUNO AI"):
    if tema:
        with st.spinner("Creando..."):
            time.sleep(2)
            prompt_suno = f"{genero} {vibe} song, {bpm_auto} BPM, {idioma}, about {tema}"
            letra = f"[HOOK]\nYo estoy en {tema}\n{bpm_auto} BPM dándole con fe\n{nombre}"
            st.success("✅ HIT GENERADO")
            tab1, tab2 = st.tabs(["📜 LETRA", "🤖 PROMPT SUNO"])
            with tab1: st.code(letra)
            with tab2: st.code(prompt_suno)

st.markdown("---")
st.markdown("👑 **RABINO MUSIC EMPIRE** | Los Alcarrizos, RD 🇩🇴")
