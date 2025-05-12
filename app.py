import gradio as gr
import random
from typing import Dict

# ========== BANCO DE DADOS ATUALIZADO ==========
FRASES_POR_ESTILO = {
    "Punk": {
        "intro": [
            "Acordes distorcidos ecoam na escuridão",
            "Batidas aceleradas invadem as ruas",
            "A revolução começa agora!",
            "Sangue, suor e amplificadores"
        ],
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
            "REVOLTA É A SOLUÇÃO!"
        ],
        "ponte": [
            "Guitarras rugem como feras",
            "O caos é nossa linguagem",
            "Pichações na parede do tempo"
        ],
        "outro": [
            "O último acorde ainda ecoa",
            "Marcas permanecem no asfalto",
            "A rebeldia nunca morre"
        ]
    },
    "Shoegaze": {
        "intro": [
            "Névoa sonora envolve os sentidos",
            "Sintetizadores sussurram segredos",
            "O universo em camadas de feedback"
        ],
        "verso": [
            "Nuvens de algodão cobrem o sol da tarde",
            "Seu nome ecoa em câmera lenta",
            "O ar cheira a chuva e transistor",
            "Todos os relógios pararam às 4h"
        ],
        "refrao": [
            "Perdido em reverberação",
            "O abismo me chama em do sustenido",
            "Flutuar é a única opção"
        ],
        "ponte": [
            "O verão dissolveu em químicos",
            "Seus olhos são dois eclipses",
            "Respire fundo antes de mergulhar"
        ],
        "outro": [
            "Ecos permanecem na névoa",
            "O último acorde se dissolve",
            "Silêncio em 360 graus"
        ]
    }
}

# ========== GERADOR DE PARTES CORRIGIDO ==========
def gerar_partes(tipo: str, estilo: str, num_frases: int) -> str:
    """Gera uma parte da música com número exato de frases"""
    try:
        base = FRASES_POR_ESTILO[estilo][tipo]
    except KeyError:
        base = [f"[SEÇÃO {tipo.upper()} INDISPONÍVEL PARA {estilo.upper()}]"]
    
    # Garante que não repetirá frases na mesma seção
    selected = random.sample(base, min(num_frases, len(base)))
    
    # Preenche com fallback se necessário
    while len(selected) < num_frases:
        selected.append(f"[{tipo.upper()} {len(selected)+1} DO {estilo.upper()}]")
    
    return "\n".join(selected)

# ========== GERADOR COMPLETO ATUALIZADO ==========
def gerar_letra_estruturada(tema: str, estilo: str) -> tuple:
    estrutura = {
        "intro": 4,
        "verso1": 4,
        "refrao": 4,
        "verso2": 4,
        "ponte": 4,
        "outro": 4
    }
    
    partes = {}
    for parte, quantidade in estrutura.items():
        tipo = parte.rstrip('12')  # Remove numeração dos versos
        partes[parte] = gerar_partes(tipo, estilo, quantidade)
    
    letra_formatada = f"""INTRO:\n{partes['intro']}\n\n
VERSO 1:\n{partes['verso1']}\n\n
REFRAO:\n{partes['refrao']}\n\n
VERSO 2:\n{partes['verso2']}\n\n
PONTE:\n{partes['ponte']}\n\n
OUTRO:\n{partes['outro']}"""
    
    return f"{tema} ({estilo})", letra_formatada

# ========== INTERFACE CORRIGIDA ==========
with gr.Blocks(title="Gerador de Letras Profissional") as app:
    gr.Markdown("# 🎤 **Gerador de Letras Estruturadas**")
    
    with gr.Row():
        tema = gr.Textbox(label="Tema Principal", value="amor em tempos de caos")
        estilo = gr.Dropdown(
            label="Estilo Musical", 
            choices=list(FRASES_POR_ESTILO.keys()),  # Usa apenas estilos com dados
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