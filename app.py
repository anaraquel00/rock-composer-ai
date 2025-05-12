
import gradio as gr
import random
from itertools import cycle

# ========== BANCO DE DADOS ==========
BANDAS_ICONICAS = {
    "Punk": ["The Clash", "Ramones", "Sex Pistols", "Dead Kennedys"],
    "Metal": ["Metallica", "Iron Maiden", "Black Sabbath", "Slayer"],
    "Grunge": ["Nirvana", "Pearl Jam", "Soundgarden", "Alice in Chains"],
    "Shoegaze": ["My Bloody Valentine", "Slowdive", "Ride", "Cocteau Twins"],
    "Dream Rock": ["Mazzy Star", "Beach House", "The xx", "Cigarettes After Sex"],
    "Rock Alternativo": ["Radiohead", "The Smashing Pumpkins", "Pixies", "Joy Division"]
}

PROGRESSOES = {
    "Punk": ["I-IV-V", "I-VIIb-IV", "Power chords"],
    "Metal": ["i-VI-III-VII", "i-VII-VI", "Trítonos"],
    "Grunge": ["I-V-IV-IV", "i-VIIb-VI-V", "Drop D"],
    "Shoegaze": ["I-iii-IV", "Maj7/add9", "Wall of Sound"],
    "Dream Rock": ["ii-V-I", "IV-I-V-vi", "Sustained chords"],
    "Rock Alternativo": ["I-V-vi-IV", "vi-IV-I-V", "Dissonances"]
}

EFEITOS_SONOROS = {
    "Punk": ["Feedback agressivo", "Palmas", "Gritos"],
    "Metal": ["Harmônicos artificiais", "Double kick", "Growl"],
    "Grunge": ["Chorus pesado", "Fuzz", "Feedback controlado"],
    "Shoegaze": ["Reverse reverb", "Tremolo arm", "Ebow"],
    "Dream Rock": ["Reverb infinito", "Synth pads", "Tape delay"],
    "Rock Alternativo": ["Delay analógico", "Staccato", "Palm mute"]
}

TEMPLATES = {
    "Punk": ("{tematica} ANTI-TUDO", "VERSO:\n{verso1}\nREFRAO: {refrao}!\nVERSO:\n{verso2}\nPONTE: {ponte}\nREFRAO FINAL: {refrao}!!!"),
    "Metal": ("{tematica} das Trevas", "[INTRO]\n{intro}\n\nVERSO 1:\n{verso1}\n\nREFRAO:\n{refrao}\n\n[SOLO]\n{solo}\n\nREFRAO FINAL:\n{refrao}"),
    "Shoegaze": ("{tematica} no Vácuo", "{verso1}\n\n(ocêo)\n{refrao}\n\n{verso2}\n\n[OUTRO] {outro}")
}

# ========== LÓGICA DE GERAÇÃO ==========
def gerar_completa(tematica, estilo, complexidade=0.7):
    # Seleciona elementos do estilo
    banda = random.choice(BANDAS_ICONICAS[estilo])
    acordes = PROGRESSOES[estilo]
    efeito = random.choice(EFEITOS_SONOROS[estilo])
    
    # Gera partes da música
    partes = {
        "verso1": gerar_verso(tematica, estilo),
        "verso2": gerar_verso(tematica, estilo),
        "refrao": gerar_refrao(tematica, estilo),
        "ponte": gerar_ponte(estilo),
        "outro": gerar_outro(estilo),
        "solo": f"[{random.choice(['SOLO DISTORCIDO', 'SOLO PSICODÉLICO', 'BREAKDOWN'])}]",
        "intro": f"[{efeito} + {random.choice(acordes)}]"
    }
    
    # Monta a estrutura completa
    estrutura = TEMPLATES.get(estilo, TEMPLATES["Rock Alternativo"])
    letra_pronta = estrutura[1].format(**partes)
    
    return {
        "Banda Referência": banda,
        "Progressão": " | ".join(acordes),
        "Efeito Chave": efeito,
        "Título": estrutura[0].format(tematica=tematica),
        "Letra": letra_pronta,
        "Estrutura": gerar_diagrama(estilo)
    }

def gerar_diagrama(estilo):
    estruturas = {
        "Punk": "VERSO-REFRAO-VERSO-PONTE-REFRAO",
        "Shoegaze": "VERSO-REFRAO-VERSO-OUTRO",
        "Metal": "INTRO-VERSO-REFRAO-SOLO-REFRAO"
    }
    return estruturas.get(estilo, "VERSO-REFRAO-PONTE-REFRAO")

# (Funções gerar_verso, gerar_refrao etc. seriam similares às anteriores mas com mais variações)

# ========== INTERFACE ==========
with gr.Blocks(theme=gr.themes.Monochrome()) as app:
    gr.Markdown("""# 🎸🤖 **Gerador Completo de Rock**  
    *De Punk a Shoegaze - Tudo que sua banda precisa*""")
    
    with gr.Row():
        with gr.Column():
            inputs = [
                gr.Textbox(label="Tema Central", value="angústia urbana"),
                gr.Dropdown(label="Estilo", choices=list(BANDAS_ICONICAS.keys())),
                gr.Slider(0.1, 1.0, value=0.7, label="Complexidade")
            ]
            btn = gr.Button("Gerar Música Completa", variant="primary")
        
        with gr.Column():
            outputs = [
                gr.Textbox(label="Banda Referência"),
                gr.Textbox(label="Progressão de Acordes"),
                gr.Textbox(label="Efeito Sonoro"),
                gr.Textbox(label="Título"),
                gr.Textbox(label="Letra", lines=12),
                gr.Textbox(label="Estrutura")
            ]
    
    # Exemplos
    gr.Examples(
        examples=[
            ["revolta adolescente", "Punk", 0.8],
            ["mistérios cósmicos", "Shoegaze", 0.6],
            ["labirintos mentais", "Metal", 0.9]
        ],
        inputs=inputs
    )
    
    btn.click(fn=gerar_completa, inputs=inputs, outputs=outputs)

app.launch()
