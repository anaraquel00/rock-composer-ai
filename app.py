import gradio as gr # type: ignore
import random
from typing import Dict, List, Tuple

# ========== SISTEMA DE SAUDAÇÃO ATUALIZADO ==========
def greet(name: str) -> str:
    saudacoes = ["🎸 Olá", "🤘 Saudações", "🎤 Bem-vindo"]
    return f"{random.choice(saudacoes)} {name}! Vamos compor algo épico hoje?"

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
}

PROGRESSOES = {
    "Metal/Death Metal": ["i-VII-VI", "i-VIIb-V", "Trítonos", "i-VI-iv-V", "Phrygian Dominant"],
    "Metal/Power Metal": ["I-V-vi-IV", "IV-V-I", "Harmônicos", "I-iii-IV-V", "vi-IV-I-V"],
    "Punk/Hardcore": ["I-IV-V", "Power chords", "Palm mute", "I-V-vi-IV", "IV-V-I-IV"],
    "Shoegaze": ["I-iii-IV", "Maj7/add9", "Wall of Sound", "I-V-vi-iii", "IV-vi-I-V"],
    "Dream Rock": ["ii-V-I", "IV-I-V-vi", "Sustained chords", "I-vi-IV-V", "ii-IV-I-V"]
}

DICIONARIO_RIMAS = {
    "ação": ["rebelião", "emancipação", "transformação"],
    "dor": ["valor", "tambor", "ardor"],
    "noite": ["desconforto", "apogeu", "redemoinho"],
    "mar": ["polar", "vulgar", "altar"],
    "vida": ["ferida", "cumprida", "descida"],
    "som": ["tom", "dom", "pavão"],
    "coração": ["solidão", "revolução", "ilusão"],
    "luz": ["cruz", "fuz", "seduz"],
    "sombras": ["palavras", "camas", "tramas"],
    "silêncio": ["conhecimento", "sentimento", "movimento"],
    "memórias": ["histórias", "vitórias", "glórias"],
    "sonhos": ["caminhos", "rinhos", "vinhos"],
    "natureza": ["beleza", "certeza", "pureza"],
    "tranquilidade": ["felicidade", "solidão", "eternidade"],
    "mistério": ["sério", "critério", "interesse"],
    "reflexão": ["ação", "revolução", "ilusão"],
    "rebelião": ["ação", "transformação", "emancipação"],
    "protesto": ["manifesto", "pretexto", "contexto"],
    "sociedade": ["realidade", "solidão", "liberdade"],
    "liberdade": ["idade", "verdade", "felicidade"],
    "fantasia": ["melodia", "sinfonia", "harmonia"],
    "heróis": ["você", "nós", "pelo"],
    "batalha": ["morte", "alma", "caminhada"],
    "sangue": ["sangue", "luz", "som"],
    "guerra": ["terra", "era", "espera"],
    "desespero": ["zero", "espero", "mero"],
}

TEMAS_DETALHADOS = {
    "Metal/Power Metal": {
        "nucleos": ["Cavaleiro", "Dragão", "Espada", "Profecia"],
        "verbos": ["ergue", "cruza", "desafia", "convoca"],
        "complementos": ["estelar", "cósmico", "ancestral", "eterno"]
    },
    "Punk/Hardcore": {
        "nucleos": ["rebelião", "protesto", "sociedade", "liberdade"],
        "verbos": ["grita", "desafia", "rompe", "constrói"],
        "complementos": ["sistema", "corrupção", "opressão", "futuro"]
    },
    "Shoegaze": {
        "nucleos": ["memórias", "sonhos", "natureza", "silêncio"],
        "verbos": ["flutua", "desvanece", "abraça", "perde"],
        "complementos": ["eterno", "infinito", "transcendente", "etéreo"]
    },
    "Dream Rock": {
        "nucleos": ["mistério", "tranquilidade", "reflexão", "sonhos"],
        "verbos": ["dança", "sussurra", "abraça", "persegue"],
        "complementos": ["luz", "sombras", "universo", "tempo"] 
    },
    "Alternative Rock": {
        "nucleos": ["rebelião", "protesto", "sociedade", "liberdade"],
        "verbos": ["grita", "desafia", "rompe", "constrói"],
        "complementos": ["sistema", "corrupção", "opressão", "futuro"]
    },
    "Indie Rock": {
        "nucleos": ["memórias", "sonhos", "natureza", "silêncio"],
        "verbos": ["flutua", "desvanece", "abraça", "perde"],
        "complementos": ["eterno", "infinito", "transcendente", "etéreo"]
    },
    "Post-Rock": {
        "nucleos": ["mistério", "tranquilidade", "reflexão", "sonhos"],
        "verbos": ["dança", "sussurra", "abraça", "persegue"],
        "complementos": ["luz", "sombras", "universo", "tempo"]
    }


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
def gerar_rima(palavra: str, silabas: int = 2) -> str:
    sufixo = palavra.lower()[-silabas:]
    return random.choice(DICIONARIO_RIMAS.get(sufixo, [f"{palavra}..."]))

def gerar_estrofe(subgenero: str, tipo: str, linhas: int) -> Tuple[List[str], str]:
    temas = TEMAS_LETRA.get(subgenero, ["abstrato"])
    esquema = random.choice(["ABAB", "AABB", "ABCB"])
    
    frases = []
    for i in range(linhas):
        base = random.choice(temas)
        if i > 0 and esquema in ["ABAB", "AABB"]:
            if (esquema == "ABAB" and i % 2 == 1) or (esquema == "AABB" and i % 2 == 0):
                frases.append(gerar_rima(frases[-1]))
                continue
        frases.append(f"{base} {random.choice(['sombrio', 'épico', 'etéreo'])}")
    
    return frases, esquema

def gerar_musica_completa(nome: str, subgenero: str) -> Tuple[str, str, str, str]:
    # Parte 1: Elementos estruturais
    partes = {}
    estruturas = ["intro", "verso", "refrao", "ponte"]
    
    for parte in estruturas:
        linhas = 4 if parte != "refrao" else 6
        frases, esquema = gerar_estrofe(subgenero, parte, linhas)
        partes[parte] = "\n".join(frases)
    
    # Parte 2: Elementos técnicos
    banda_ref = random.choice(BANDAS_ICONICAS[subgenero])
    acordes = " | ".join(random.sample(PROGRESSOES[subgenero], 3))
    bpm = str(random.randint(80, 200)) + " BPM"
    
    # Parte 3: Montagem da letra
    letra_formatada = f"""INTRO ({esquema}):\n{partes['intro']}\n\n
VERSO:\n{partes['verso']}\n\n
REFRAO:\n{partes['refrao']}\n\n
PONTE:\n{partes['ponte']}"""
    
    return greet(nome), banda_ref, acordes, letra_formatada

# ========== INTERFACE ATUALIZADA ==========
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