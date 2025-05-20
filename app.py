"""
Rock Composer AI - Aplicação principal integrada com bibliotecas aprimoradas
Versão atualizada que aproveita todas as novas funcionalidades
"""

import gradio as gr  
import random
from typing import Dict, List, Tuple, Any, Optional

# Importação das bibliotecas aprimoradas
from dicionario_rimas import (
    DICIONARIO_RIMAS, 
    obter_rimas, 
    obter_vocabulario_genero, 
    gerar_rima,
    obter_rimas_por_sufixo
)
from temas_detalhados import (
    TEMAS_DETALHADOS, 
    obter_temas_detalhados, 
    gerar_combinacao_tematica, 
    gerar_tema_completo
)
from instrucoes_estilisticas import (
    INSTRUCOES_ESTILISTICAS, 
    obter_instrucoes_estilisticas, 
    obter_caracteristicas_genero, 
    gerar_estrutura_musica
)

# Instalação do lyricsgenius se necessário
try:
    from lyricsgenius import Genius 
    import lyricsgenius.types.song  # type: ignore
    import lyricsgenius.types.album  # type: ignore
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "lyricsgenius"])
    from lyricsgenius import Genius
    import lyricsgenius.types.song  # type: ignore
    import lyricsgenius.types.album  # type: ignore

import os
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")
if not GENIUS_API_KEY:
    raise ValueError("A variável de ambiente GENIUS_API_KEY não está definida. Defina antes de rodar o app.")

# Inicializa o cliente Genius
genius = Genius(GENIUS_API_KEY)

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

# Utilizamos a constante PROGRESSOES diretamente das instruções estilísticas aprimoradas
PROGRESSOES = {genero: instrucoes for genero, instrucoes in INSTRUCOES_ESTILISTICAS.items()}

# ========== TEMAS DE LETRA ATUALIZADOS ==========
# Utilizamos os temas detalhados aprimorados
TEMAS_LETRA = {genero: temas for genero, temas in TEMAS_DETALHADOS.items()}

# Função para buscar letras de músicas
def buscar_letra(banda: str) -> str:
    """
    Busca letras de músicas de uma banda específica usando a API do Genius.
    
    Args:
        banda (str): Nome da banda para buscar letras.
        
    Returns:
        str: Letra da música encontrada ou mensagem de erro.
    """
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
    """
    Versão aprimorada da função para gerar linha poética.
    Utiliza o tema completo com múltiplos elementos.
    
    Args:
        tema (dict): Dicionário contendo elementos temáticos.
        
    Returns:
        str: Linha poética gerada.
    """
    # Verificar se temos os elementos básicos
    elementos_basicos = ["nucleos", "acoes", "elementos"]
    for elemento in elementos_basicos:
        if elemento not in tema:
            # Gerar elemento faltante
            if elemento == "nucleos" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["nucleos"])
            elif elemento == "acoes" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["acoes"])
            elif elemento == "elementos" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                tema[elemento] = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"]["elementos"])
    
    # Construir a linha poética
    linha = f"{tema['nucleos']} {tema['acoes']} {tema['elementos']}"
    
    # Adicionar elementos adicionais se disponíveis
    if "personagens" in tema:
        linha += f", {tema['personagens']}"
    if "emocoes" in tema:
        linha += f" com {tema['emocoes']}"
    
    return linha.capitalize()

# Função para validar linha
def validar_linha(nova_linha: str, linhas_existentes: List[str]) -> bool:
    """
    Verifica se uma nova linha é válida e não duplicada.
    
    Args:
        nova_linha (str): Linha a ser validada.
        linhas_existentes (list): Lista de linhas existentes.
        
    Returns:
        bool: True se a linha for válida, False caso contrário.
    """
    palavras = nova_linha.split()
    
    # Verifica se há palavras repetidas na mesma linha
    return not any(
        palavras.count(palavra) > 2 for palavra in palavras
    ) and nova_linha not in linhas_existentes

# Função para gerar estrofe aprimorada
def gerar_estrofe(subgenero: str, tipo: str, linhas: int) -> Tuple[List[str], str]:
    """
    Versão aprimorada da função para gerar estrofe.
    Utiliza as novas funções de geração de temas e combinações.
    
    Args:
        subgenero (str): Subgênero musical.
        tipo (str): Tipo de estrofe (verso, refrão, etc).
        linhas (int): Número de linhas na estrofe.
        
    Returns:
        tuple: Lista de linhas da estrofe e tipo da estrofe.
    """
    # Usar tema padrão caso o subgênero não seja encontrado
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    
    # Obter características do estilo para o tipo de estrofe
    instrucoes = obter_instrucoes_estilisticas(subgenero, tipo) if tipo in ["intro", "verso", "refrao", "ponte"] else {}
    
    estrofe = []
    
    # Gerar linhas únicas para a estrofe
    for _ in range(linhas):
        while True:
            # Gerar tema completo para linha mais rica
            tema = gerar_tema_completo(subgenero)
            linha = gerar_linha_poetica(tema).capitalize()
            
            if validar_linha(linha, estrofe):
                estrofe.append(linha)
                break
    
    return estrofe, tipo

# Função para gerar estrofe modernizada
def gerar_estrofe_modernizada(subgenero: str, linhas: int) -> Tuple[List[str], str]:
    """
    Versão aprimorada da função para gerar estrofe modernizada.
    Utiliza esquemas de rima mais sofisticados.
    
    Args:
        subgenero (str): Subgênero musical.
        linhas (int): Número de linhas na estrofe.
        
    Returns:
        tuple: Lista de frases da estrofe e esquema utilizado.
    """
    # Usar tema padrão caso o subgênero não seja encontrado
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    
    # Escolher esquema de rima
    esquemas = ["ABAB", "AABA", "ABCD"]
    esquema = random.choice(esquemas)
    
    frases = []
    ultimas_rimas = {}
    
    for i in range(linhas):
        padrao_atual = esquema[i % len(esquema)]
        
        # Gere um novo tema para cada linha para garantir variedade
        tema_linha = gerar_tema_completo(subgenero)
        nova_linha = gerar_linha_poetica(tema_linha)
        
        # Se este padrão já tem uma rima estabelecida, tentar usar
        if padrao_atual in ultimas_rimas:
            rima_alvo = ultimas_rimas[padrao_atual]
            palavras = nova_linha.split()
            if palavras:
                rima = gerar_rima(rima_alvo, silabas=3)
                nova_linha = " ".join(palavras[:-1] + [rima])
        
        palavras = nova_linha.split()
        if palavras:
            ultimas_rimas[padrao_atual] = palavras[-1]
        
        frases.append(nova_linha.capitalize())
    
    return frases, esquema
# Função para gerar música completa aprimorada
def gerar_musica_completa(nome: str, subgenero: str) -> Tuple[str, str, str, str]:
    """
    Versão aprimorada da função para gerar música completa.
    Utiliza estrutura musical dinâmica e todas as novas funcionalidades.
    
    Args:
        nome (str): Nome para a música.
        subgenero (str): Subgênero musical.
        
    Returns:
        tuple: Banda de referência, acordes, letra formatada e letra da banda de referência.
    """
    print(f"Gerando música para o subgênero: {subgenero}")
    
    # Obter características do gênero
    caracteristicas = obter_caracteristicas_genero(subgenero)
    print(f"Características estilísticas carregadas: {caracteristicas}")
    
    # Gerar estrutura musical com complexidade média
    estrutura = gerar_estrutura_musica(subgenero, complexidade=2)
    print(f"Estrutura musical gerada: {estrutura}")
    
    # Preparar partes da música
    partes = {}
    esquemas = {}
    
    # Obter instruções estilísticas específicas
    instrucoes = obter_instrucoes_estilisticas(subgenero)
    print(f"Instruções estilísticas carregadas: {len(instrucoes) if instrucoes else 0} itens")
    
    # Gerar cada parte da estrutura
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
            linhas = 0  # Instrumental
        elif parte == "outro":
            linhas = 2
        else:
            linhas = 4
        
        # Pular partes instrumentais
        if linhas == 0:
            partes[parte] = ["[Instrumental]"]
            esquemas[parte] = "Instrumental"
            continue
        
        # Usar estrofe modernizada para refrão, estrofe normal para o resto
        if parte == "refrao":
            frases, esquema = gerar_estrofe_modernizada(subgenero, linhas)
        else:
            frases, esquema = gerar_estrofe(subgenero, parte, linhas)
        
        partes[parte] = frases
        esquemas[parte] = esquema
    
    # Escolher banda de referência
    if subgenero in BANDAS_ICONICAS:
        banda_ref = random.choice(BANDAS_ICONICAS[subgenero])
    else:
        banda_ref = "Banda Desconhecida"
    
    print(f"Banda referência: {banda_ref}")
    
    # Gerar progressão de acordes
    acordes = " | "
    if subgenero in ACORDES:
        acordes_disponiveis = ACORDES[subgenero]
        # Selecionar progressão de acordes baseada nas características do gênero
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
    
    # Gerar BPM baseado nas características do gênero
    bpm = str(random.randint(80, 200)) + " BPM"
    if "caracteristicas_gerais" in instrucoes and "bpm_recomendado" in instrucoes["caracteristicas_gerais"]:
        bpm_range = instrucoes["caracteristicas_gerais"]["bpm_recomendado"]
        bpm = bpm_range  # Usar o range recomendado diretamente
    
        
    # Formatar a letra - Adicionando descrição estilística antes de cada parte
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

        
         # Obter instrução estilística para a parte (se existir)
        instrucao = ""
        if (
            isinstance(instrucoes, dict)
            and parte in instrucoes
            and instrucoes[parte]
        ):
            valor = instrucoes[parte]
            if isinstance(valor, list):
                # Se for lista, pega o primeiro elemento (se for string ou dict)
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
                # Se for dict, tenta pegar a descrição ou o padrão
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

        # Montar bloco da parte
        parte_text = instrucao + "\n".join(partes[parte]) + "\n\n"
        letra_formatada += parte_text
    
    # Buscar letra de uma música da banda referência
    letra_banda = buscar_letra(banda_ref)
    
    # Retornar os valores
    return banda_ref, acordes, letra_formatada, letra_banda

# Interface Gradio
with gr.Blocks() as app:
    gr.Markdown("# 🎸 **Jo Cyborg - IA Compositora**")
    
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
