import gradio as gr
import random
from typing import Dict, List

# ========== BANCO DE DADOS ==========
FRASES_POR_ESTILO = {
    "Punk": {
        "verso": [
            "A cidade está podre e ninguém se importa!",
            "Gritos ecoam mas ninguém escuta",
            "Quebramos as regras só por existir",
            "O sistema caiu e ninguém viu"
        ],
        "refrao": [
            "ISSO NÃO É UMA FASE! (x3)",
            "Queimem tudo até o chão!",
            "Não somos sua diversão!",
            "O futuro é nosso também!",
            "Nada vai nos calar!",
            "REVOLTA É A SOLUÇÃO!"
        ]
    },
    "Shoegaze": {
        "verso": [
            "Nuvens de algodão cobrem o sol da tarde",
            "Seu nome ecoa em câmera lenta",
            "O ar cheira a chuva e transistor",
            "Todos os relógios pararam às 4h"
        ],
        "ponte": [
            "O verão dissolveu em químicos",
            "Seus olhos são dois eclipses",
            "Respire fundo antes de mergulhar",
            "O vazio tem um som tão doce"
        ]
    }
}

# ========== GERADOR DE PARTES ==========
def gerar_partes(tipo: str, estilo: str, num_frases: int) -> str:
    """Gera uma parte da música com número exato de frases"""
    frases = []
    base = FRASES_POR_ESTILO.get(estilo, {}).get(tipo, [])
    
    for _ in range(num_frases):
        if base:
            frases.append(random.choice(base))
        else:
            # Fallback criativo
            frases.append(f"[FRASE {tipo.upper()} DO {estilo.upper()}]")
    
    return "\n".join(frases)

# ========== GERADOR COMPLETO ==========
def gerar_letra_estruturada(tema: str, estilo: str) -> Dict[str, str]:
    part_names = ["intro", "verso1", "refrao", "ponte", "outro"]
    
    partes = {
        "intro": gerar_partes("intro", estilo, 4),
        "verso1": gerar_partes("verso", estilo, 4),
        "refrao": gerar_partes("refrao", estilo, 6),
        "verso2": gerar_partes("verso", estilo, 4),
        "ponte": gerar_partes("ponte", estilo, 4),
        "outro": gerar_partes("outro", estilo, 4)
    }
    
    return {
        "Título": f"{tema} ({estilo})",
        "Letra": f"""INTRO:\n{partes['intro']}\n\n
VERSO 1:\n{partes['verso1']}\n\n
REFRAO:\n{partes['refrao']}\n\n
VERSO 2:\n{partes['verso2']}\n\n
PONTE:\n{partes['ponte']}\n\n
OUTRO:\n{partes['outro']}"""
    }

# ========== INTERFACE ==========
with gr.Blocks(title="Gerador de Letras Profissional") as app:
    gr.Markdown("# 🎤 **Gerador de Letras Estruturadas**")
    
    with gr.Row():
        tema = gr.Textbox(label="Tema Principal", value="amor em tempos de caos")
        estilo = gr.Dropdown(
            label="Estilo Musical", 
            choices=["Punk", "Metal", "Grunge", "Shoegaze", "Dream Rock"],
            value="Punk"
        )
    
    btn = gr.Button("Gerar Letra", variant="primary")
    
    with gr.Row():
        titulo = gr.Textbox(label="Título")
        letra = gr.Textbox(label="Letra Completa", lines=20)
    
    btn.click(
        fn=gerar_letra_estruturada,
        inputs=[tema, estilo],
        outputs=[titulo, letra]
    )

app.launch()