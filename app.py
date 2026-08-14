import gradio as gr
from gtts import gTTS
import os
import datetime

# FUNCIONES DE CEREBRO
def generar_beat(estilo):
    return f"🔥 Beat de {estilo} generado. BPM: 140. Listo para rapear Rabino."

def escribir_letra(tema):
    return f"""[VERSO 1 - Rabino]
Yo soy Rabino en el beat, rompiendo el sistema
{tema} es mi tema, el imperio es mi lema
No me paran, no me frenan, soy la nueva era
CEREBRO en la máquina, la rima verdadera

[HOOK]
Rabino, Rabino, el rey del imperio
Con CEREBRO activo, rompo todo el criterio"""

def clonar_voz(texto):
    tts = gTTS(text=texto, lang='es')
    filename = f"rabino_voz_{datetime.datetime.now().strftime('%H%M%S')}.mp3"
    tts.save(filename)
    return filename

# INTERFAZ DE CEREBRO
with gr.Blocks(title="CEREBRO - Rabino Music Empire", theme=gr.themes.Dark()) as demo:
    
    gr.Markdown("# 🧠 CEREBRO - Rabino Music Empire")
    gr.Markdown("### La IA que domina la creación musical")
    
    with gr.Tab("🎵 Generar Beat"):
        estilo = gr.Dropdown(["Drill", "Trap", "Boombap", "Reggaeton"], label="Elige el estilo")
        btn_beat = gr.Button("GENERAR BEAT 🔥")
        salida_beat = gr.Textbox(label="Resultado")
        btn_beat.click(generar_beat, inputs=estilo, outputs=salida_beat)
    
    with gr.Tab("✍️ Escribir Letra"):
        tema = gr.Textbox(label="¿De qué quieres la letra?", placeholder="Ej: Dinero, Calle, Imperio")
        btn_letra = gr.Button("ESCRIBIR LETRA ✍️")
        salida_letra = gr.Textbox(label="Letra de Rabino", lines=10)
        btn_letra.click(escribir_letra, inputs=tema, outputs=salida_letra)
    
    with gr.Tab("🎤 Clonar Voz"):
        texto_voz = gr.Textbox(label="Escribe lo que dirá Rabino")
        btn_voz = gr.Button("CLONAR VOZ 🎤")
        salida_audio = gr.Audio(label="Audio de Rabino")
        btn_voz.click(clonar_voz, inputs=texto_voz, outputs=salida_audio)

if __name__ == "__main__":
    demo.launch()
