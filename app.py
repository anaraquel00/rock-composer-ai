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
        "nucleos": [
            "Cavaleiro das estrelas",
            "Dragão de ébano",
            "Espada ancestral",
            "Profecia celestial"
        ],
        "acoes": [
            "ergue o lábaro",
            "cruza o horizonte",
            "desafia o crepúsculo",
            "convoca os eleitos"
        ],
        "elementos": [
            "sob a lua rubra",
            "entre relâmpagos cósmicos",
            "no altar dos deuses antigos",
            "pelas veredas do destino"
        ]
    },
    "Punk/Hardcore": {
        "nucleos": [
            "rebelião urbana",
            "gritos de liberdade",
            "ruas em chamas",
            "sombras da opressão"
        ],
        "verbos": [
            "grita contra a injustiça",
            "desafia o sistema",
            "rompe as correntes",
            "constrói um novo amanhã",
            "rompe as barreiras",
            "constrói um novo amanhã"
        ],
        "complementos": [
            "sistema opressor",
            "corrupção governamental",
            "luta pela verdade",
            "opressão social",
            "futuro incerto",
            "solidão na multidão"
        ]
    },
    "Shoegaze": {
        "nucleos": ["memórias vivas", "sonhos perdidos", "natureza efêmera", "silêncio profundo"],
        "verbos": ["flutua em lagrimas", "desvanece em mente", "abraça me forte", "perde a consciência"],
        "complementos": ["eterno amor", "infinito ao voar", "transcendente em brilho", "etéreo em luz"]
    },
    "Dream Rock": {
        "nucleos": ["mistério da noite", "tranquilidade ao luar", "reflexão silenciosa", "sonhos profundos"],
        "verbos": ["dança nas estrelas", "sussurra alto", "me abraça", "persegue meu ego"],
        "complementos": ["luz em minha cor", "sombras escuras", "universo paralelo", "tempo perdido"] 
    },
    "Alternative Rock": {
        "nucleos": ["rebelião desenfreada", "protesto sem graça", "sociedade corrompida", "liberdade de escolhas"],
        "verbos": ["grita alto", "desafia o sistema", "rompe barreiras", "constrói pontes"],
        "complementos": ["sistema sitiado", "corrupção generalizada", "opressão controlada", "futuro sombrio"]
    },
    "Indie Rock": {
        "nucleos": ["memórias vivas", "sonhos sem nexo", "natureza morta", "silêncio abafado"],
        "verbos": ["flutua alto", "desvanece devagar", "abraça meus contos", "perde consciência"],
        "complementos": ["eterno viver", "infinito calmo", "transcendente luar", "etéreo em cruz"]
    },
    "Post-Rock": {
        "nucleos": ["mistério do tempo", "tranquilidade duvidada", "reflexão às avessas", "sonhos loucos"],
        "verbos": ["dança pra mim", "sussurra devagar", "abraça meu ar", "persegue meu ser"],
        "complementos": ["luz nas sombras", "sombras vazias", "universo cosmico", "tempo passado"]
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
  
def gerar_rima(palavra: str, silabas: int = 3) -> str:
    """Gera rima baseada na última palavra do verso"""
    ultima_palavra = palavra.split()[-1].lower()
    for chave, rimas in DICIONARIO_RIMAS.items():
        if chave in ultima_palavra:
            return random.choice(rimas)
    return f"{palavra}..."

def validar_linha(nova_linha: str, linhas_existentes: list) -> bool:
    """Valida linha evitando repetições excessivas"""
    palavras = nova_linha.split()
    # Verifica repetição de palavras e linhas idênticas
    return (
        all(palavras.count(p) < 2 for p in palavras) and 
        nova_linha not in linhas_existentes
    )

def gerar_estrofe_modernizada(subgenero: str, tipo: str, linhas: int) -> Tuple[List[str], str]:
    """Gera estrofe com estrutura coerente"""
    tema = TEMAS_DETALHADOS.get(subgenero)
    esquema = random.choice(["ABAB", "AABA", "ABCB"])
    
    frases = []
    rimas = {}
    
    for i in range(linhas):
        while True:
            # Gera linha base combinando elementos temáticos
            sujeito = random.choice(tema['nucleos'])
            verbo = random.choice(tema['verbos'])
            complemento = random.choice(tema['elementos'])
            nova_linha = f"{sujeito} {verbo} {complemento}"
            
            # Aplica esquema de rimas
            if esquema == "ABAB" and i % 2 == 0:
                if i > 1:
                    nova_linha += f" {gerar_rima(rimas[i%2])}"
            elif esquema == "AABA" and i == 3:
                nova_linha += f" {gerar_rima(rimas[0])}"
            
            if validar_linha(nova_linha, frases):
                break
                
        frases.append(nova_linha.capitalize())
        rimas[i] = nova_linha.split()[-1]
    
    return frases, esquema

def gerar_musica_completa(nome: str, subgenero: str) -> Tuple[str, str, str, str]:
    """Gera música completa com estrutura coerente"""
    partes = {}
    esquema_geral = ""
    
    # Gera cada parte da música
    for parte in ["intro", "verso", "refrao", "ponte"]:
        linhas = 6 if parte == "refrao" else 4
        frases, esquema = gerar_estrofe_modernizada(subgenero, parte, linhas)
        partes[parte] = "\n".join(frases)
        esquema_geral = esquema  # Mantém último esquema para referência
    
    # Montagem final da letra
    letra_formatada = (
        f"INTRO ({esquema_geral}):\n{partes['intro']}\n\n"
        f"VERSO:\n{partes['verso']}\n\n"
        f"REFRAO:\n{partes['refrao']}\n\n"
        f"PONTE:\n{partes['ponte']}"
    )
    
    # Elementos técnicos
    return (
        greet(nome),
        random.choice(BANDAS_ICONICAS[subgenero]),
        " | ".join(random.sample(PROGRESSOES[subgenero], 3)),
        letra_formatada
    )
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