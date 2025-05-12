
import gradio as gr
import random
from itertools import cycle
from typing import Dict, List, Tuple


# ========== BANCO DE DADOS ==========
BANDAS_ICONICAS = {
    "Punk": ["The Clash", "Ramones", "Sex Pistols", "Dead Kennedys"],
    "Metal": ["Metallica", "Iron Maiden", "Black Sabbath", "Slayer"],
    "Grunge": ["Nirvana", "Pearl Jam", "Soundgarden", "Alice in Chains"],
    "Shoegaze": ["My Bloody Valentine", "Slowdive", "Ride", "Cocteau Twins"],
    "Dream Rock": ["Mazzy Star", "Beach House", "The xx", "Cigarettes After Sex"],
    "Rock Alternativo": ["Radiohead", "The Smashing Pumpkins", "Pixies", "Joy Division"]
}

SUB_GENEROS = {
    "Metal": {
        "Death Metal": {
            "vocabulario": ["carnificina", "túmulos", "entranhas", "putrefação"],
            "esquema_rima": "ABAB",
            "tempo": "220-300 BPM"
        },
        "Power Metal": {
            "vocabulario": ["dragões", "honra", "espadas", "destino"],
            "esquema_rima": "AABB",
            "tempo": "180-220 BPM"
        }
    },
    "Punk": {
        "Hardcore": {
            "vocabulario": ["revolta", "opressão", "ruínas", "gritos"],
            "esquema_rima": "AAAA",
            "tempo": "Batida rápida"
        }
    }
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

# ========== SISTEMA DE RIMAS ==========
DICIONARIO_RIMAS = {
    "ação": ["destruição", "perdição", "canção"],
    "dor": ["amor", "tambor", "flor"],
    "noite": ["foice", "estoque", "arroite"]
}

def gerar_rima(palavra_chave: str) -> str:
    return random.choice(DICIONARIO_RIMAS.get(palavra_chave[-3:], ["sem rima"])[0])

def aplicar_esquema(frases: List[str], esquema: str) -> List[str]:
    if esquema == "ABAB":
        frases[1] = gerar_rima(frases[0])
        frases[3] = gerar_rima(frases[2])
    elif esquema == "AABB":
        frases[1] = gerar_rima(frases[0])
        frases[3] = gerar_rima(frases[2])
    return frases

# ========== GERADOR DE PARTES ==========
def gerar_frase(subgenero: str, tipo: str) -> str:
    dados = SUB_GENEROS.get(subgenero.split("/")[0], {}).get(subgenero.split("/")[1], {})
    palavras = dados.get("vocabulario", [])
    return f"{random.choice(palavras)} {random.choice(palavras)}" if palavras else "Letra automática"

def gerar_estrofes(subgenero: str) -> Dict[str, str]:
    dados = SUB_GENEROS.get(subgenero.split("/")[0], {}).get(subgenero.split("/")[1], {})
    esquema = dados.get("esquema_rima", "ABAB")
    
    partes = {
        "intro": aplicar_esquema([gerar_frase(subgenero, "intro") for _ in range(4)], esquema),
        "verso": aplicar_esquema([gerar_frase(subgenero, "verso") for _ in range(4)], esquema),
        "refrao": aplicar_esquema([gerar_frase(subgenero, "refrao") for _ in range(6)], esquema)
    }
    
    return {
        "BPM": dados.get("tempo", "120 BPM"),
        "Letra": f"""INTRO ({esquema}):\n{"\n".join(partes['intro'])}\n\n
VERSO:\n{"\n".join(partes['verso'])}\n\n
REFRAO:\n{"\n".join(partes['refrao'])}"""
    }


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
