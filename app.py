import gradio as gr
import random
from typing import Dict, List, Tuple

# ========== SISTEMA DE SAUDAÇÃO ==========
def greet(name: str) -> str:
    return f"🎸 Olá {name}! Eu sou seu assistente de composição musical. Vamos criar algo épico hoje?"

# ========== BANCO DE DADOS MUSICAL ==========
BANDAS_ICONICAS = {
    "Metal/Death Metal": ["Cannibal Corpse", "Morbid Angel", "Death"],
    "Metal/Power Metal": ["Helloween", "Blind Guardian", "DragonForce"],
    "Punk/Hardcore": ["Bad Brains", "Black Flag", "Dead Kennedys"],
    "Shoegaze": ["My Bloody Valentine", "Slowdive", "Ride"],
    "Dream Rock": ["Beach House", "Mazzy Star", "Cocteau Twins"]
}

PROGRESSOES = {
    "Metal/Death Metal": ["i-VII-VI", "i-VIIb-V", "Trítonos"],
    "Metal/Power Metal": ["I-V-vi-IV", "IV-V-I", "Harmônicos"],
    "Punk/Hardcore": ["I-IV-V", "Power chords", "Palm mute"],
    "Shoegaze": ["I-iii-IV", "Maj7/add9", "Wall of Sound"],
    "Dream Rock": ["ii-V-I", "IV-I-V-vi", "Sustained chords"]
}

DICIONARIO_RIMAS = {
    "ação": ["destruição", "perdição", "canção"],
    "dor": ["amor", "tambor", "flor"],
    "noite": ["foice", "estoque", "arroite"]
}

# ========== GERADOR MUSICAL ==========
def gerar_rima(palavra: str) -> str:
    return random.choice(DICIONARIO_RIMAS.get(palavra[-3:], [f"{palavra} (sem rima)"]))

def gerar_estrofe(subgenero: str, tipo: str, linhas: int) -> List[str]:
    temas = BANDAS_ICONICAS.get(subgenero, ["rock"])
    esquema = "ABAB" if "Death" in subgenero else "AABB"
    
    frases = []
    for i in range(linhas):
        frase = f"{random.choice(temas)} {random.choice(['sombrio', 'épico', 'etéreo'])}"
        if i % 2 == 1 and esquema == "ABAB":
            frase = gerar_rima(frases[i-1])
        elif i % 2 == 1 and esquema == "AABB":
            frase = gerar_rima(frases[i-1])
        frases.append(frase)
    
    return frases

def gerar_musica_completa(nome: str, subgenero: str) -> Dict[str, str]:
    # Parte 1: Saudação
    saudacao = greet(nome)
    
    # Parte 2: Letra
    partes = {
        "intro": gerar_estrofe(subgenero, "intro", 4),
        "verso": gerar_estrofe(subgenero, "verso", 4),
        "refrao": gerar_estrofe(subgenero, "refrao", 6),
        "ponte": gerar_estrofe(subgenero, "ponte", 4)
    }
    
    # Parte 3: Elementos técnicos
    banda_ref = random.choice(BANDAS_ICONICAS.get(subgenero, ["Artista Desconhecido"]))
    acordes = " | ".join(PROGRESSOES.get(subgenero, ["I-IV-V"]))
    
    return {
        "Saudação": saudacao,
        "Banda Referência": banda_ref,
        "Progressão": acordes,
        "Letra": f"""INTRO:\n{"\n".join(partes['intro'])}\n\n
VERSO:\n{"\n".join(partes['verso'])}\n\n
REFRAO:\n{"\n".join(partes['refrao'])}\n\n
PONTE:\n{"\n".join(partes['ponte'])}"""
    }

# ========== INTERFACE ==========
with gr.Blocks(theme=gr.themes.Soft(primary_hue="red")) as app:
    gr.Markdown("# 🤖🎸 **Assistente de Composição Musical**")
    
    with gr.Row():
        nome = gr.Textbox(label="Seu Nome", value="Raquel")
        subgenero = gr.Dropdown(
            label="Estilo Musical",
            choices=[
                "Metal/Death Metal",
                "Metal/Power Metal",
                "Punk/Hardcore",
                "Shoegaze",
                "Dream Rock"
            ],
            value="Metal/Power Metal"
        )
    
    btn = gr.Button("Criar Música", variant="primary")
    
    with gr.Column():
        saudacao = gr.Textbox(label="Mensagem")
        referencia = gr.Textbox(label="Banda Referência")
        acordes = gr.Textbox(label="Progressão de Acordes")
        letra = gr.Textbox(label="Letra Completa", lines=15)
    
    btn.click(
        fn=gerar_musica_completa,
        inputs=[nome, subgenero],
        outputs=[saudacao, referencia, acordes, letra]
    )

app.launch()