import gradio as gr # type: ignore
import random
from typing import Dict, List, Tuple
from dicionario_rimas import DICIONARIO_RIMAS
from temas_detalhados import TEMAS_DETALHADOS
from instrucoes_estilisticas import INSTRUCOES_ESTILISTICAS

# ========== BANCO DE DADOS MUSICAL COMPLETO ==========
BANDAS_ICONICAS = {
    "Metal/Death Metal": ["Cannibal Corpse", "Morbid Angel", "Death"],
    "Metal/Power Metal": ["Helloween", "Blind Guardian", "DragonForce"],
    "Punk/Hardcore": ["Bad Brains", "Black Flag", "Dead Kennedys"],
    "Shoegaze": ["My Bloody Valentine", "Slowdive", "Ride"],
    "Dream Rock": ["Beach House", "Mazzy Star", "Cocteau Twins"],
    "Alternative Rock": ["Radiohead", "Nirvana", "The Smashing Pumpkins"],
    "Indie Rock": ["Arctic Monkeys", "Vampire Weekend", "Tame Impala"],
    "Post-Rock": ["Explosions in the Sky", "Godspeed You! Black Emperor", "Sigur Rós"]
}

ACORDES = {
    "Metal/Death Metal": ["E5", "C5", "G5", "D5", "A5"],
    "Metal/Power Metal": ["Cmaj", "Gmaj", "Dmaj", "Amin", "Emin"],
    "Punk/Hardcore": ["E5", "A5", "D5", "G5", "C5"],
    "Shoegaze": ["Cmaj7", "Gmaj7", "Dmaj7", "Amin7", "Emin7"],
    "Dream Rock": ["Cmaj", "Gmaj", "Dmaj", "Amin", "Emin"],
    "Alternative Rock": ["Cmaj", "Gmaj", "Dmaj", "Amin", "Emin"],
    "Indie Rock": ["Cmaj", "Gmaj", "Dmaj", "Amin", "Emin"],
    "Post-Rock": ["Cmaj", "Gmaj", "Dmaj", "Amin", "Emin"]
}

PROGRESSOES = {
    "Metal/Death Metal": ["i-VII-VI", "i-VIIb-V", "Trítonos", "i-VI-iv-V", "Phrygian Dominant"],
    "Metal/Power Metal": ["I-V-vi-IV", "IV-V-I", "Harmônicos", "I-iii-IV-V", "vi-IV-I-V"],
    "Punk/Hardcore": ["I-IV-V", "Power chords", "Palm mute", "I-V-vi-IV", "IV-V-I-IV"],
    "Shoegaze": ["I-iii-IV", "Maj7/add9", "Wall of Sound", "I-V-vi-iii", "IV-vi-I-V"],
    "Dream Rock": ["ii-V-I", "IV-I-V-vi", "Sustained chords", "I-vi-IV-V", "ii-IV-I-V"]
}

# ========== TEMAS DE LETRA ATUALIZADOS ==========
# Temas de letra para cada subgênero musical
# Adicionando temas mais específicos e variados
# para enriquecer a composição musical

TEMAS_LETRA = {
    "Metal/Death Metal": ["morte", "desespero", "sangue", "guerra"],
    "Metal/Power Metal": ["fantasia", "heróis", "batalha", "luz"],
    "Punk/Hardcore": ["rebelião", "sociedade", "protesto", "liberdade"],
    "Shoegaze": ["amor", "solidão", "memórias", "sonhos"],
    "Dream Rock": ["natureza", "mistério", "tranquilidade", "reflexão"],
    "Alternative Rock": ["rebelião", "protesto", "sociedade", "liberdade"],
    "Indie Rock": ["memórias", "sonhos", "natureza", "silêncio"],
    "Post-Rock": ["mistério", "tranquilidade", "reflexão", "sonhos"]
}

# ========== GERADOR MUSICAL CORRIGIDO ==========
# Função auxiliar para gerar linha poética
def gerar_linha_poetica(tema: Dict[str, List[str]]) -> str:
    nucleos = random.choice(tema.get("nucleos", []))
    acoes = random.choice(tema.get("acoes", []))
    elementos = random.choice(tema.get("elementos", []))
    return f"{nucleos} {acoes} {elementos}"

# Função para gerar rima com validação de comprimento
def gerar_rima(palavra: str, silabas: int = 3) -> str:
    if len(palavra) < silabas:
        return palavra
    sufixos = {
        2: palavra[-2:],
        3: palavra[-3:],
        4: palavra[-4:]
    }
    return random.choice(DICIONARIO_RIMAS.get(sufixos[silabas], [palavra]))

# Função para validar linha
def validar_linha(nova_linha: str, linhas_existentes: list) -> bool:
    palavras = nova_linha.split()
    return not any(
        palavras.count(palavra) > 2 for palavra in palavras
    ) and nova_linha not in linhas_existentes

# Função para gerar estrofe
def gerar_estrofe(subgenero: str, tipo: str, linhas: int) -> Tuple[List[str], str]:
    tema = TEMAS_DETALHADOS.get(subgenero, TEMAS_DETALHADOS["Metal/Power Metal"])
    estrofe = []
    for _ in range(linhas):
        linha = gerar_linha_poetica(tema)
        estrofe.append(linha)
    return estrofe, tipo

# Função para gerar estrofe modernizada
def gerar_estrofe_modernizada(subgenero: str, linhas: int) -> Tuple[List[str], str]:
    tema = TEMAS_DETALHADOS.get(subgenero, TEMAS_DETALHADOS["Metal/Power Metal"])
    esquema = random.choice(["ABAB", "AABA", "ABCD"])
    frases = []
    ultimas_rimas = {}
    for i in range(linhas):
        nova_linha = gerar_linha_poetica(tema)
        if esquema in ["ABAB", "AABA"]:
            if i in [0, 2] and esquema == "ABAB":
                rima_alvo = ultimas_rimas.get(0, nova_linha.split()[-1])
                nova_linha = gerar_rima(rima_alvo, silabas=3) + " " + nova_linha
            elif i == 3 and esquema == "AABA":
                nova_linha = gerar_rima(ultimas_rimas[0], silabas=3) + " " + nova_linha
        frases.append(nova_linha.capitalize())
        ultimas_rimas[i] = nova_linha.split()[-1]
    return frases, esquema

# Função para gerar música completa
def gerar_musica_completa(nome: str, subgenero: str) -> Tuple[str, str, str, str]:
    partes = {}
    esquemas = {}
    instrucoes = INSTRUCOES_ESTILISTICAS.get(subgenero, {})
    estruturas = ["intro", "verso", "refrao", "ponte"]
    for parte in estruturas:
        linhas = 4 if parte != "refrao" else 6
        frases, esquema = gerar_estrofe(subgenero, parte, linhas)
        descricao = instrucoes.get(parte, "Descrição não disponível")
        partes[parte] = f"[{parte.upper()}: {descricao}]\n" + "\n".join(frases)
        esquemas[parte] = esquema
    banda_ref = random.choice(BANDAS_ICONICAS.get(subgenero, ["Banda Desconhecida"]))
    acordes = " | ".join(random.sample(PROGRESSOES.get(subgenero, ["I-IV-V"]), 3))
    bpm = str(random.randint(80, 200)) + " BPM"
    letra_formatada = f"""INTRO ({esquemas['intro']}):\n{partes['intro']}\n\n
VERSO ({esquemas['verso']}):\n{partes['verso']}\n\n
REFRAO ({esquemas['refrao']}):\n{partes['refrao']}\n\n
PONTE ({esquemas['ponte']}):\n{partes['ponte']}"""
    return banda_ref, acordes, letra_formatada, bpm

# Interface Gradio
with gr.Blocks(theme=gr.themes.Soft(primary_hue="red")) as app:
    gr.Markdown("# 🤖🎸 **Assistente de Composição Musical**")
    with gr.Row():
        nome = gr.Textbox(label="Seu Nome", value="Raquel")
        subgenero = gr.Dropdown(
            label="Estilo Musical",
            choices=list(BANDAS_ICONICAS.keys()),
            value="Metal/Power Metal"
        )
    btn = gr.Button("Criar Música", variant="primary")
    with gr.Column():
        referencia = gr.Textbox(label="Banda Referência")
        acordes = gr.Textbox(label="Progressão de Acordes")
        letra = gr.Textbox(label="Letra Completa", lines=15)
    btn.click(
        fn=gerar_musica_completa,
        inputs=[nome, subgenero],
        outputs=[referencia, acordes, letra]
    )
app.launch()