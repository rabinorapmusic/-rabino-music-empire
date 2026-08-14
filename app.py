gradio==4.44.0
gTTS==2.5.4
librosa==0.10.2
transformers==4.44.2
torch==2.4.1
numpy==1.26.4
soundfile==0.12.1import gradio as gr
import random
from gtts import gTTS

def cancion_duo(tema):
    if tema == "":
        return "Escribe un tema bro 😈 Ej: Dembow de Los Alcarrizos", None, ""
    
    artistas_tipo = [
        ["Romeo Santos", "Karol G"],
        ["Bad Bunny", "Rosalia"],
        ["Aventura", "Shakira"],
        ["Anuel", "Natti Natasha"],
        ["Juan Luis Guerra", "Natti Natasha"],
        ["El Alfa", "Becky G"]
    ]
    estilos = ["Bachata", "Reggaeton", "Dembow", "Trap", "Merengue"]

    duo = random.choice(artistas_tipo)
    estilo = random.choice(estilos)

    cancion = f"""🔥 NUEVO DÚO: {duo[0]} x {duo[1]} 🔥
**Género:** {estilo}
**Tema:** {tema}

**[Verso 1 - {duo[0]}]**
Llegué a tu vida como un dembow en la noche
Con flow de barrio pero corazón de broche
{tema}, baby, tú me tienes mal

**[Coro - Los 2]**
Dale que esto está caliente 
Rabino Rap en el ambiente
"""
    # CREAR EL AUDIO
    archivo = "cerebro.mp3"
    tts = gTTS(cancion, lang='es')
    tts.save(archivo)
    
    acordes = "TONO: D menor | ACORDES: Dm - Gm - C - F | 95 BPM"
    return cancion, archivo, acordes

with gr.Blocks(title="RABINO RAP - Cerebro") as demo:
    gr.Markdown("# 🧠 RABINO RAP APP")
    gr.Markdown("Generador de Dúos + Voz + Acordes")
    
    tema = gr.Textbox(label="Escribe el tema", placeholder="Ej: Amor en Los Alcarrizos")
    btn = gr.Button("Despertar a Cerebro 🔥")
    
    with gr.Row():
        salida_texto = gr.Textbox(label="Tu Canción", lines=12)
        audio = gr.Audio(label="Voz de Cerebro")
    
    acordes_out = gr.Textbox(label="Acordes para cantar")
    
    btn.click(cancion_duo, inputs=tema, outputs=[salida_texto, audio, acordes_out])

demo.launch()
