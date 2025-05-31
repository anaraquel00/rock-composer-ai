"""
Rock Composer AI - Aplicação principal integrada com bibliotecas aprimoradas
Versão atualizada que aproveita todas as novas funcionalidades
"""

import gradio as gr  
import random
import os
from typing import Dict, List, Tuple, Any, Optional

# Importação das bibliotecas aprimoradas
from dicionario_rimas import DICIONARIO_RIMAS
from temas_detalhados import TEMAS_DETALHADOS
from instrucoes_estilisticas import INSTRUCOES_ESTILISTICAS, obter_caracteristicas_genero, obter_instrucoes_estilisticas

# lyricsgenius: importar apenas se instalado, não instalar em tempo de execução
try:
    from lyricsgenius import Genius
except ImportError:
    Genius = None

GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
if Genius and not GENIUS_API_KEY:
    raise ValueError("A variável de ambiente GENIUS_API_KEY não está definida. Defina antes de rodar o app.")

# Inicializa o cliente Genius apenas se possível
genius = Genius(GENIUS_API_KEY) if Genius and GENIUS_API_KEY else None

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

PROGRESSOES = {genero: instrucoes for genero, instrucoes in INSTRUCOES_ESTILISTICAS.items()}
TEMAS_LETRA = {genero: temas for genero, temas in TEMAS_DETALHADOS.items()}

# Função para gerar um tema completo para um subgênero
def gerar_tema_completo(subgenero: str) -> dict:
    """
    Gera um tema completo (nucleos, acoes, elementos, personagens, emocoes) para o subgênero fornecido.
    """
    tema_base = TEMAS_DETALHADOS.get(subgenero, TEMAS_DETALHADOS.get("Metal/Power Metal", {}))
    tema = {}
    for chave in ["nucleos", "acoes", "elementos", "personagens", "emocoes"]:
        if chave in tema_base and tema_base[chave]:
            tema[chave] = random.choice(tema_base[chave])
    return tema

# Função para buscar letras de músicas
def buscar_letra(banda: str) -> str:
    """
    Busca letras de músicas de uma banda específica usando a API do Genius.
    """
    if not genius:
        return "lyricsgenius não está instalado ou GENIUS_API_KEY não definida."
    try:
        print(f"Buscando letras para a banda: {banda}")
        artist = genius.search_artist(banda, max_songs=1, sort="popularity")
        if artist is not None and hasattr(artist, "songs") and artist.songs:
            song = artist.songs[0]
            return f"{song.title}\n\n{song.lyrics}"
        else:
            return "Não foi possível encontrar letras para esta banda."
    except Exception as e:
        print(f"Erro ao buscar letras: {e}")
        return "Não foi possível encontrar letras para esta banda."

# Função auxiliar para gerar linha poética aprimorada
def gerar_linha_poetica(tema: Dict[str, Any]) -> str:
    elementos_basicos = ["nucleos", "acoes", "elementos"]
    for elemento in elementos_basicos:
        if elemento not in tema:
            if elemento == "nucleos" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["nucleos"])
            elif elemento == "acoes" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["acoes"])
            elif elemento == "elementos" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["elementos"])
    linha = f"{tema['nucleos']} {tema['acoes']} {tema['elementos']}"
    if "personagens" in tema:
        linha += f", {tema['personagens']}"
    if "emocoes" in tema:
        linha += f" com {tema['emocoes']}"
    return linha.capitalize()

def validar_linha(nova_linha: str, linhas_existentes: List[str]) -> bool:
    palavras = nova_linha.split()
    return not any(
        palavras.count(palavra) > 2 for palavra in palavras
    ) and nova_linha not in linhas_existentes

def gerar_estrofe(subgenero: str, tipo: str, linhas: int) -> Tuple[List[str], str]:
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    instrucoes = obter_instrucoes_estilisticas(subgenero, tipo) if tipo in ["intro", "verso", "refrao", "ponte"] else {}
    estrofe = []
    for _ in range(linhas):
        while True:
            tema = gerar_tema_completo(subgenero)
            linha = gerar_linha_poetica(tema).capitalize()
            if validar_linha(linha, estrofe):
                estrofe.append(linha)
                break
    return estrofe, tipo

def gerar_estrofe_modernizada(subgenero: str, linhas: int) -> Tuple[List[str], str]:
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    esquemas = ["ABAB", "AABA", "ABCD"]
    esquema = random.choice(esquemas)
    frases = []
    ultimas_rimas = {}
    for i in range(linhas):
        padrao_atual = esquema[i % len(esquema)]
        tema_linha = gerar_tema_completo(subgenero)
        nova_linha = gerar_linha_poetica(tema_linha)
        palavras = nova_linha.split()
        if padrao_atual in ultimas_rimas and palavras:
            rima_alvo = ultimas_rimas[padrao_atual]
            # Aqui você pode implementar gerar_rima se desejar rimas reais
            # rima = gerar_rima(rima_alvo, silabas=3)
            # nova_linha = " ".join(palavras[:-1] + [rima])
        if palavras:
            ultimas_rimas[padrao_atual] = palavras[-1]
        frases.append(nova_linha.capitalize())
    return frases, esquema

def gerar_musica_completa(nome: str, subgenero: str) -> Tuple[str, str, str, str]:
    print(f"Gerando música para o subgênero: {subgenero}")
    caracteristicas = obter_caracteristicas_genero(subgenero)
    print(f"Características estilísticas carregadas: {caracteristicas}")
    # Função para gerar uma estrutura musical padrão
    def gerar_estrutura_musica(subgenero: str, complexidade: int = 2) -> List[str]:
        """
        Gera uma estrutura musical baseada no subgênero e complexidade.
        """
        if complexidade == 1:
            return ["intro", "verso", "refrao", "outro"]
        elif complexidade == 2:
            return ["intro", "verso", "refrao", "verso", "refrao", "ponte", "refrao", "outro"]
        else:
            return ["intro", "verso", "pre_refrao", "refrao", "verso", "pre_refrao", "refrao", "ponte", "solo", "refrao", "outro"]

    estrutura = gerar_estrutura_musica(subgenero, complexidade=2)
    print(f"Estrutura musical gerada: {estrutura}")
    partes = {}
    esquemas = {}
    instrucoes = obter_instrucoes_estilisticas(subgenero)
    print(f"Instruções estilísticas carregadas: {len(instrucoes) if instrucoes else 0} itens")
    for parte in estrutura:
        if parte == "intro":
            linhas = 4
        elif parte == "verso":
            linhas = 4
        elif parte == "refrao":
            linhas = 4
        elif parte == "ponte":
            linhas = 4
        elif parte == "solo":
            linhas = 0
        elif parte == "outro":
            linhas = 2
        else:
            linhas = 4
        if linhas == 0:
            partes[parte] = ["[Instrumental]"]
            esquemas[parte] = "Instrumental"
            continue
        if parte == "refrao":
            frases, esquema = gerar_estrofe_modernizada(subgenero, linhas)
        else:
            frases, esquema = gerar_estrofe(subgenero, parte, linhas)
        partes[parte] = frases
        esquemas[parte] = esquema
    if subgenero in BANDAS_ICONICAS:
        banda_ref = random.choice(BANDAS_ICONICAS[subgenero])
    else:
        banda_ref = "Banda Desconhecida"
    print(f"Banda referência: {banda_ref}")
    acordes = " | "
    if subgenero in ACORDES:
        acordes_disponiveis = ACORDES[subgenero]
        if subgenero in PROGRESSOES:
            progressoes_disponiveis = []
            for p in PROGRESSOES[subgenero]:
                if isinstance(p, dict) and "progressao" in p:
                    progressoes_disponiveis.append(p.get("progressao"))
            if progressoes_disponiveis:
                acordes += " | ".join([
                    random.choice(progressoes_disponiveis) 
                    for _ in range(3)
                ])
            else:
                acordes += " | ".join([
                    random.choice(acordes_disponiveis) 
                    for _ in range(3)
                ])
        else:
            acordes += " | ".join([
                random.choice(acordes_disponiveis) 
                for _ in range(3)
            ])
    bpm = str(random.randint(80, 200)) + " BPM"
    if (
        isinstance(instrucoes, dict)
        and "caracteristicas_gerais" in instrucoes
        and isinstance(instrucoes["caracteristicas_gerais"], dict)
        and "bpm_recomendado" in instrucoes["caracteristicas_gerais"]
    ):
        bpm_range = instrucoes["caracteristicas_gerais"]["bpm_recomendado"]
        bpm = bpm_range
    letra_formatada = ""
    for idx, parte in enumerate(estrutura):
        parte_nome = parte.upper()
        if parte == "intro":
            parte_nome = "INTRO"
        elif parte == "verso":
            parte_nome = f"VERSO{idx+1}"
        elif parte == "refrao":
            parte_nome = "REFRÃO"
        elif parte == "ponte":
            parte_nome = "PONTE"
        elif parte == "pre_refrao":
            parte_nome = "PRÉ-REFRÃO"
        elif parte == "outro":
            parte_nome = "OUTRO"
        instrucao = ""
        if (
            isinstance(instrucoes, dict)
            and parte in instrucoes
            and instrucoes[parte]
        ):
            valor = instrucoes[parte]
            if isinstance(valor, list):
                if valor and isinstance(valor[0], dict):
                    if "descricao" in valor[0]:
                        instrucao = f"[{parte_nome}: {valor[0]['descricao']}]\n"
                    elif "padrao" in valor[0]:
                        instrucao = f"[{parte_nome}: {valor[0]['padrao']}]\n"
                    else:
                        instrucao = f"[{parte_nome}]\n"
                elif valor and isinstance(valor[0], str):
                    instrucao = f"[{parte_nome}: {valor[0]}]\n"
                else:
                    instrucao = f"[{parte_nome}]\n"
            elif isinstance(valor, dict):
                if "descricao" in valor:
                    instrucao = f"[{parte_nome}: {valor['descricao']}]\n"
                elif "padrao" in valor:
                    instrucao = f"[{parte_nome}: {valor['padrao']}]\n"
                else:
                    instrucao = f"[{parte_nome}]\n"
            elif isinstance(valor, str):
                instrucao = f"[{parte_nome}: {valor}]\n"
            else:
                instrucao = f"[{parte_nome}]\n"
        else:
            instrucao = f"[{parte_nome}]\n"
        parte_text = instrucao + "\n".join(partes[parte]) + "\n\n"
        letra_formatada += parte_text
    letra_banda = buscar_letra(banda_ref)
    return banda_ref, acordes, letra_formatada, letra_banda

def responder_chat(mensagem, estado):
    """
    Função para responder ao chat do usuário.
    O usuário deve digitar o tema desejado, e a IA gera a música.
    """
    nome = "Usuário"
    tema_usuario = mensagem.strip()
    # Tenta identificar subgênero pelo tema, senão usa padrão
    subgenero = None
    for key in BANDAS_ICONICAS.keys():
        if key.lower() in tema_usuario.lower():
            subgenero = key
            break
    if not subgenero:
        subgenero = "Metal/Power Metal"
    banda_ref, acordes, letra, letra_banda = gerar_musica_completa(nome, subgenero)
    resposta = (
        f"**Banda Referência:** {banda_ref}\n"
        f"**Progressão de Acordes:** {acordes}\n\n"
        f"**Letra:**\n{letra}\n"        
    )
    estado.append((mensagem, resposta))
    return "", estado

with gr.Blocks() as app:
    gr.Markdown("# 🎸 **Jo Cyborg - IA Compositora**")
    gr.Markdown("Digite no chat o tema ou estilo da música que deseja gerar (ex: 'faça um rock sobre liberdade').")
    chatbot = gr.Chatbot(label="Jo Cyborg Chat")
    estado = gr.State([])

    with gr.Row():
        chat_input = gr.Textbox(
            show_label=False,
            placeholder="Digite o tema ou estilo da música...",
            container=False
        )
        send_btn = gr.Button("Enviar", variant="primary")

    def atualizar_chat(mensagem, estado):
        return responder_chat(mensagem, estado)

    send_btn.click(
        atualizar_chat,
        inputs=[chat_input, estado],
        outputs=[chat_input, chatbot]
    )
    chat_input.submit(
        atualizar_chat,
        inputs=[chat_input, estado],
        outputs=[chat_input, chatbot]
    )

    gr.Markdown("Projeto no Hugging Face: [Rock Composer AI](https://huggingface.co/spaces/ana99/rock-composer-ai)")

    app.launch()