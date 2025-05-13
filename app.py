import gradio as gr # type: ignore
import random
from typing import Dict, List, Tuple
from dicionario_rimas import DICIONARIO_RIMAS
from temas_detalhados import TEMAS_DETALHADOS
from instrucoes_estilisticas import INSTRUCOES_ESTILISTICAS

from lyricsgenius import Genius
import lyricsgenius.types.song  # type: ignore
import lyricsgenius.types.album  # type: ignore

# Adicione sua API Key do Genius aqui
GENIUS_API_KEY = "BXgdS_8Op2OWqlp1_KBo9knbI2pYzGyvn2fd4hJLbJwz8_gX55Tt4mltrymG6nBh"

# Inicializa o cliente Genius
genius = lyricsgenius.Genius("BXgdS_8Op2OWqlp1_KBo9knbI2pYzGyvn2fd4hJLbJwz8_gX55Tt4mltrymG6nBh")

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
    "Metal/Death Metal": [
        {"progressao": "i-VII-VI", "emocoes": "sombrio, intenso", "caracteristicas": "riffs pesados, atmosfera obscura"},
        {"progressao": "i-VIIb-V", "emocoes": "agressivo, caótico", "caracteristicas": "ritmos rápidos, dissonância"},
        {"progressao": "i-VI-iv-V", "emocoes": "melancólico, épico", "caracteristicas": "melodias lentas, tensão crescente"},
        {"progressao": "Phrygian Dominant", "emocoes": "exótico, ameaçador", "caracteristicas": "escalas orientais, intensidade"},
        {"progressao": "i-bII-i", "emocoes": "opressor, sombrio", "caracteristicas": "mudanças abruptas, peso"},
        {"progressao": "i-VI-VII-V", "emocoes": "épico, grandioso", "caracteristicas": "dinâmica crescente, solos técnicos"}
    ],
    "Metal/Power Metal": [
        {"progressao": "I-V-vi-IV", "emocoes": "heróico, otimista", "caracteristicas": "melodias épicas, coros"},
        {"progressao": "IV-V-I", "emocoes": "triunfante, energético", "caracteristicas": "ritmos rápidos, refrões marcantes"},
        {"progressao": "I-iii-IV-V", "emocoes": "emocionante, aventureiro", "caracteristicas": "harmonias ricas, solos"},
        {"progressao": "vi-IV-I-V", "emocoes": "esperançoso, inspirador", "caracteristicas": "progressão fluida, melodia"},
        {"progressao": "I-VI-IV-V", "emocoes": "épico, grandioso", "caracteristicas": "crescendos, coros"},
        {"progressao": "I-IV-V-vi", "emocoes": "dinâmico, vibrante", "caracteristicas": "mudanças rápidas, energia"}
    ],
    "Punk/Hardcore": [
        {"progressao": "I-IV-V", "emocoes": "rebelde, direto", "caracteristicas": "riffs simples, energia crua"},
        {"progressao": "I-V-vi-IV", "emocoes": "intenso, emocional", "caracteristicas": "ritmos rápidos, letras diretas"},
        {"progressao": "IV-V-I-IV", "emocoes": "agressivo, energético", "caracteristicas": "power chords, refrões"},
        {"progressao": "Power chords", "emocoes": "cru, explosivo", "caracteristicas": "simples, impacto imediato"},
        {"progressao": "I-V-IV", "emocoes": "urgente, intenso", "caracteristicas": "ritmos rápidos, simplicidade"},
        {"progressao": "I-IV-I-V", "emocoes": "protesto, direto", "caracteristicas": "energia constante, repetição"}
    ],
    "Shoegaze": [
        {"progressao": "I-iii-IV", "emocoes": "sonhador, introspectivo", "caracteristicas": "camadas de som, reverb"},
        {"progressao": "I-V-vi-iii", "emocoes": "melancólico, etéreo", "caracteristicas": "harmonias suaves, atmosfera"},
        {"progressao": "IV-vi-I-V", "emocoes": "calmo, reflexivo", "caracteristicas": "texturas densas, melodia"},
        {"progressao": "Maj7/add9", "emocoes": "etéreo, flutuante", "caracteristicas": "acordes ricos, reverb"},
        {"progressao": "I-V-IV-iii", "emocoes": "nostálgico, suave", "caracteristicas": "melodias lentas, harmonia"},
        {"progressao": "ii-IV-I-V", "emocoes": "tranquilo, expansivo", "caracteristicas": "progressão fluida, atmosfera"}
    ],
    "Dream Rock": [
        {"progressao": "ii-V-I", "emocoes": "suave, relaxante", "caracteristicas": "melodias limpas, harmonia"},
        {"progressao": "IV-I-V-vi", "emocoes": "sonhador, introspectivo", "caracteristicas": "texturas suaves, melodia"},
        {"progressao": "I-vi-IV-V", "emocoes": "esperançoso, emocional", "caracteristicas": "progressão fluida, harmonia"},
        {"progressao": "ii-IV-I-V", "emocoes": "calmo, expansivo", "caracteristicas": "melodias suaves, atmosfera"},
        {"progressao": "I-V-vi-IV", "emocoes": "nostálgico, inspirador", "caracteristicas": "harmonias ricas, melodia"},
        {"progressao": "IV-ii-I-V", "emocoes": "etéreo, introspectivo", "caracteristicas": "texturas densas, reverb"}
    ],
    "Alternative Rock": [
        {"progressao": "I-IV-V", "emocoes": "energético, cativante", "caracteristicas": "riffs marcantes, refrões"},
        {"progressao": "I-vi-IV-V", "emocoes": "emocional, dinâmico", "caracteristicas": "mudanças de tom, melodia"},
        {"progressao": "IV-I-V-vi", "emocoes": "introspectivo, vibrante", "caracteristicas": "harmonias ricas, energia"},
        {"progressao": "I-V-vi-IV", "emocoes": "esperançoso, emocional", "caracteristicas": "progressão fluida, melodia"},
        {"progressao": "ii-V-I", "emocoes": "suave, reflexivo", "caracteristicas": "melodias limpas, harmonia"},
        {"progressao": "I-IV-ii-V", "emocoes": "dinâmico, cativante", "caracteristicas": "mudanças rápidas, energia"}
    ],
    "Indie Rock": [
        {"progressao": "I-IV-V", "emocoes": "nostálgico, cativante", "caracteristicas": "riffs simples, melodia"},
        {"progressao": "I-vi-IV-V", "emocoes": "emocional, introspectivo", "caracteristicas": "harmonias suaves, melodia"},
        {"progressao": "IV-I-V-vi", "emocoes": "sonhador, suave", "caracteristicas": "texturas limpas, reverb"},
        {"progressao": "I-V-vi-IV", "emocoes": "esperançoso, vibrante", "caracteristicas": "progressão fluida, energia"},
        {"progressao": "ii-IV-I-V", "emocoes": "calmo, introspectivo", "caracteristicas": "melodias suaves, harmonia"},
        {"progressao": "I-V-IV-vi", "emocoes": "etéreo, reflexivo", "caracteristicas": "texturas densas, melodia"}
    ],
    "Post-Rock": [
        {"progressao": "I-IV-V", "emocoes": "épico, expansivo", "caracteristicas": "crescendo lento, camadas"},
        {"progressao": "I-vi-IV-V", "emocoes": "melancólico, introspectivo", "caracteristicas": "texturas densas, melodia"},
        {"progressao": "IV-I-V-vi", "emocoes": "sonhador, etéreo", "caracteristicas": "harmonias suaves, reverb"},
        {"progressao": "I-V-vi-IV", "emocoes": "esperançoso, emocional", "caracteristicas": "progressão fluida, melodia"},
        {"progressao": "ii-V-I", "emocoes": "calmo, reflexivo", "caracteristicas": "melodias limpas, harmonia"},
        {"progressao": "I-IV-ii-V", "emocoes": "dinâmico, expansivo", "caracteristicas": "crescendo, texturas"}
    ]
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

# Função para buscar letras de músicas
def buscar_letra(banda: str) -> str:
    try:
        print(f"Buscando letras para a banda: {banda}")
        song = genius.search_artist(banda, max_songs=1, sort="popularity").songs[0]
        return f"{song.title}\n\n{song.lyrics}"
    except Exception as e:
        print(f"Erro ao buscar letras: {e}")
        return "Não foi possível encontrar letras para esta banda."

# ========== GERADOR MUSICAL CORRIGIDO ==========
# Função auxiliar para gerar linha poética
def gerar_linha_poetica(tema: Dict[str, List[str]]) -> str:
    # Certifique-se de que as listas não estão vazias antes de escolher
    nucleos = random.choice(tema.get("nucleos", ["tema padrão"]))
    acoes = random.choice(tema.get("acoes", ["ação padrão"]))
    elementos = random.choice(tema.get("elementos", ["elemento padrão"]))
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
    # Use um tema padrão caso o subgênero não seja encontrado
    tema = TEMAS_DETALHADOS.get(subgenero, TEMAS_DETALHADOS["Metal/Power Metal"])
    
    # Verifique se o tema possui as chaves necessárias
    if not all(key in tema for key in ["nucleos", "acoes", "elementos"]):
        tema = TEMAS_DETALHADOS["Metal/Power Metal"]  # Fallback para tema padrão
    
    estrofe = []
    for _ in range(linhas):
        while True:
            linha = gerar_linha_poetica(tema).capitalize()
            if validar_linha(linha, estrofe):  # Verifica se a linha é única
                estrofe.append(linha)
                break
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
    print(f"Gerando música para o subgênero: {subgenero}")
    partes = {}
    esquemas = {}
    instrucoes = INSTRUCOES_ESTILISTICAS.get(subgenero, {})
    print(f"Instruções estilísticas carregadas: {instrucoes}")
    estruturas = ["intro", "verso", "refrao", "ponte"]
    for parte in estruturas:
        linhas = 4 if parte != "refrao" else 6
        frases, esquema = gerar_estrofe(subgenero, parte, linhas)
        descricao = instrucoes.get(parte, "Descrição não disponível")
        partes[parte] = f"[{descricao}]\n" + "\n".join(frases)
        esquemas[parte] = esquema
    banda_ref = random.choice(BANDAS_ICONICAS.get(subgenero, ["Banda Desconhecida"]))
    print(f"Banda referência: {banda_ref}")
    acordes = " | ".join(random.sample(
        [p["progressao"] for p in PROGRESSOES.get(subgenero, PROGRESSOES["Metal/Power Metal"])],
        3
    ))
    bpm = str(random.randint(80, 200)) + " BPM"
    letra_formatada = f"""INTRO:\n{partes['intro']}\n\n
VERSO:\n{partes['verso']}\n\n
REFRAO:\n{partes['refrao']}\n\n
PONTE:\n{partes['ponte']}"""
    
    # Busca a letra de uma música da banda referência
    letra_banda = buscar_letra(banda_ref)

    # Retorna os valores
    return banda_ref, acordes, letra_formatada, letra_banda


# Interface Gradio
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as app:
    gr.Markdown("# 🤖🎸 **Jo Cyborg - IA Compositora**")
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
        letra_banda = gr.Textbox(label="Letra da Banda Referência", lines=15)
    btn.click(
        fn=gerar_musica_completa,
        inputs=[nome, subgenero],
        outputs=[referencia, acordes, letra, letra_banda]
    )
    
    app.launch()

