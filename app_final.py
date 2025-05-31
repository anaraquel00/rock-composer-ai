"""
Rock Composer AI - Aplicação principal integrada com bibliotecas aprimoradas
Versão atualizada que aproveita todas as novas funcionalidades
Correção de repetição e melhoria na geração de letras
"""

import gradio as gr  # type: ignore
import random
from typing import Dict, List, Tuple, Any, Optional

# Importação das bibliotecas aprimoradas
from dicionario_rimas_aprimorado import (
    DICIONARIO_RIMAS, 
    obter_rimas, 
    obter_vocabulario_genero, 
    gerar_rima,
    obter_rimas_por_sufixo
)
from temas_detalhados_aprimorado import (
    TEMAS_DETALHADOS, 
    obter_temas_detalhados, 
    gerar_combinacao_tematica, 
    gerar_tema_completo
)
from instrucoes_estilisticas_aprimorado import (
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

# Adicione sua API Key do Genius aqui
GENIUS_API_KEY = "sSa-NaHFpfLFcIbKSTICM0z2GVutBfEWURsiwuogtMjaWH0rmBGHLUP56yPUYXnG"

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
        song = genius.search_artist(banda, max_songs=1, sort="popularity").songs[0]
        return f"{song.title}\n\n{song.lyrics}"
    except Exception as e:
        print(f"Erro ao buscar letras: {e}")
        return "Não foi possível encontrar letras para esta banda."

# Função para extrair palavras-chave de um tema
def extrair_palavras_chave(tema: Dict[str, Any]) -> List[str]:
    """
    Extrai palavras-chave de um tema para uso em geração de variações.
    
    Args:
        tema (dict): Dicionário contendo elementos temáticos.
        
    Returns:
        list: Lista de palavras-chave extraídas.
    """
    palavras = []
    
    # Extrair palavras de cada elemento do tema
    for categoria, conteudo in tema.items():
        if isinstance(conteudo, str):
            palavras.extend([p for p in conteudo.split() if len(p) > 3])
    
    # Remover duplicatas e retornar
    return list(set(palavras))

# Função auxiliar para gerar linha poética aprimorada
def gerar_linha_poetica(tema: Dict[str, Any], palavras_evitar: List[str] = None, palavras_incluir: List[str] = None) -> str:
    """
    Versão aprimorada da função para gerar linha poética.
    Utiliza o tema completo com múltiplos elementos e evita palavras específicas.
    
    Args:
        tema (dict): Dicionário contendo elementos temáticos.
        palavras_evitar (list, optional): Lista de palavras a evitar.
        palavras_incluir (list, optional): Lista de palavras a incluir.
        
    Returns:
        str: Linha poética gerada.
    """
    if palavras_evitar is None:
        palavras_evitar = []
    
    if palavras_incluir is None:
        palavras_incluir = []
    
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
    
    # Verificar se algum elemento contém palavras a evitar
    for elemento in elementos_basicos:
        palavras = tema[elemento].split()
        if any(palavra in palavras_evitar for palavra in palavras):
            # Tentar substituir o elemento
            if elemento == "nucleos" and "Metal/Power Metal" in TEMAS_DETALHADOS:
                for _ in range(5):  # Tentar até 5 vezes
                    novo_elemento = random.choice(TEMAS_DETALHADOS["Metal/Power Metal"][elemento])
                    if not any(palavra in palavras_evitar for palavra in novo_elemento.split()):
                        tema[elemento] = novo_elemento
                        break
            
    # Tentar incluir palavras específicas
    if palavras_incluir and random.random() < 0.7:  # 70% de chance de incluir
        palavra_incluir = random.choice(palavras_incluir)
        # Decidir onde incluir a palavra
        elemento_alvo = random.choice(elementos_basicos)
        palavras = tema[elemento_alvo].split()
        if len(palavras) > 1:
            indice = random.randint(0, len(palavras) - 1)
            palavras[indice] = palavra_incluir
            tema[elemento_alvo] = " ".join(palavras)
    
    # Construir a linha poética
    linha = f"{tema['nucleos']} {tema['acoes']} {tema['elementos']}"
    
    # Adicionar elementos adicionais se disponíveis
    elementos_adicionais = ["personagens", "emocoes", "simbolos", "conflitos"]
    elementos_disponiveis = [e for e in elementos_adicionais if e in tema]
    
    if elementos_disponiveis:
        # Escolher aleatoriamente 1 ou 2 elementos adicionais
        num_elementos = min(len(elementos_disponiveis), random.randint(1, 2))
        elementos_escolhidos = random.sample(elementos_disponiveis, num_elementos)
        
        for elemento in elementos_escolhidos:
            if elemento == "personagens":
                linha += f", {tema[elemento]}"
            elif elemento == "emocoes":
                linha += f" com {tema[elemento]}"
            elif elemento == "simbolos":
                linha += f" como {tema[elemento]}"
            elif elemento == "conflitos":
                linha += f" em {tema[elemento]}"
    
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
    
    # Verificar se há palavras repetidas na mesma linha
    if any(palavras.count(palavra) > 2 for palavra in palavras):
        return False
    
    # Verificar se a linha é muito similar a alguma existente
    for linha in linhas_existentes:
        palavras_existentes = set(linha.lower().split())
        palavras_novas = set(nova_linha.lower().split())
        
        # Calcular similaridade (interseção / união)
        if len(palavras_existentes) > 0 and len(palavras_novas) > 0:
            similaridade = len(palavras_existentes.intersection(palavras_novas)) / len(palavras_existentes.union(palavras_novas))
            if similaridade > 0.7:  # Se mais de 70% das palavras são iguais
                return False
    
    return True

# Função para gerar estrofe aprimorada
def gerar_estrofe(subgenero: str, tipo: str, linhas: int, tema_base: Dict[str, Any] = None) -> Tuple[List[str], str]:
    """
    Versão aprimorada da função para gerar estrofe.
    Utiliza as novas funções de geração de temas e combinações.
    
    Args:
        subgenero (str): Subgênero musical.
        tipo (str): Tipo de estrofe (verso, refrão, etc).
        linhas (int): Número de linhas na estrofe.
        tema_base (dict, optional): Tema base para manter coerência.
        
    Returns:
        tuple: Lista de linhas da estrofe e tipo da estrofe.
    """
    # Usar tema padrão caso o subgênero não seja encontrado
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    
    # Obter características do estilo para o tipo de estrofe
    instrucoes = obter_instrucoes_estilisticas(subgenero, tipo) if tipo in ["intro", "verso", "refrao", "ponte"] else {}
    
    # Gerar tema base se não fornecido
    if tema_base is None:
        tema_base = gerar_tema_completo(subgenero)
    
    # Extrair palavras-chave do tema base para manter coerência
    palavras_chave = extrair_palavras_chave(tema_base)
    
    estrofe = []
    palavras_usadas = set()
    
    # Gerar linhas únicas para a estrofe
    for _ in range(linhas):
        tentativas = 0
        while tentativas < 10:  # Limitar tentativas para evitar loops infinitos
            # Gerar variação do tema base
            tema_variacao = gerar_tema_completo(subgenero)
            
            # Incluir algumas palavras-chave do tema base para manter coerência
            palavras_incluir = random.sample(palavras_chave, min(2, len(palavras_chave))) if palavras_chave else []
            
            # Evitar palavras já muito usadas
            palavras_evitar = list(palavras_usadas)
            
            linha = gerar_linha_poetica(tema_variacao, palavras_evitar, palavras_incluir).capitalize()
            
            if validar_linha(linha, estrofe):
                estrofe.append(linha)
                # Adicionar palavras à lista de usadas
                for palavra in linha.split():
                    if len(palavra) > 3:
                        palavras_usadas.add(palavra.lower())
                break
            
            tentativas += 1
        
        # Se não conseguiu gerar uma linha válida após várias tentativas
        if tentativas >= 10 and len(estrofe) < linhas:
            # Gerar uma linha simples como fallback
            linha = f"{random.choice(tema_base.get('nucleos', '').split())} {random.choice(tema_base.get('acoes', '').split())}"
            estrofe.append(linha.capitalize())
    
    return estrofe, tipo

# Função para gerar refrão com rimas
def gerar_refrao(subgenero: str, linhas: int, tema_base: Dict[str, Any] = None) -> Tuple[List[str], str]:
    """
    Função especializada para gerar refrão com sistema de rimas.
    
    Args:
        subgenero (str): Subgênero musical.
        linhas (int): Número de linhas no refrão.
        tema_base (dict, optional): Tema base para manter coerência.
        
    Returns:
        tuple: Lista de linhas do refrão e esquema de rimas.
    """
    # Usar tema padrão caso o subgênero não seja encontrado
    if subgenero not in TEMAS_DETALHADOS:
        subgenero = "Metal/Power Metal"
    
    # Gerar tema base se não fornecido
    if tema_base is None:
        tema_base = gerar_tema_completo(subgenero)
    
    # Escolher esquema de rima
    esquemas = ["AABB", "ABAB", "AAAA", "ABBA"]
    esquema = random.choice(esquemas)
    
    # Criar dicionário para armazenar as linhas por padrão de rima
    linhas_por_padrao = {}
    
    # Gerar primeira linha para cada padrão único no esquema
    padroes_unicos = set(esquema)
    for padrao in padroes_unicos:
        # Gerar tema variação
        tema_variacao = gerar_tema_completo(subgenero)
        
        # Gerar linha base
        linha_base = gerar_linha_poetica(tema_variacao)
        
        # Extrair última palavra para rima
        palavras = linha_base.split()
        if palavras:
            ultima_palavra = palavras[-1]
            
            # Gerar algumas rimas para esta palavra
            rimas = []
            for _ in range(5):
                rima = gerar_rima(ultima_palavra)
                if rima and rima != ultima_palavra and rima not in rimas:
                    rimas.append(rima)
            
            # Armazenar linha e rimas disponíveis
            linhas_por_padrao[padrao] = {
                "linha_base": linha_base.capitalize(),
                "ultima_palavra": ultima_palavra,
                "rimas": rimas,
                "linhas_geradas": [linha_base.capitalize()]
            }
        else:
            # Fallback se não conseguir extrair palavra
            linhas_por_padrao[padrao] = {
                "linha_base": linha_base.capitalize(),
                "ultima_palavra": "",
                "rimas": [],
                "linhas_geradas": [linha_base.capitalize()]
            }
    
    # Gerar o refrão seguindo o esquema
    refrao = []
    for i in range(linhas):
        if i >= len(esquema):
            # Se tivermos mais linhas que o esquema, repetir o esquema
            padrao_atual = esquema[i % len(esquema)]
        else:
            padrao_atual = esquema[i]
        
        info_padrao = linhas_por_padrao[padrao_atual]
        
        # Se já temos linhas suficientes para este padrão
        if len(info_padrao["linhas_geradas"]) > i // len(esquema):
            linha = info_padrao["linhas_geradas"][i // len(esquema)]
        else:
            # Gerar nova variação da linha base
            tema_variacao = gerar_tema_completo(subgenero)
            linha_base = gerar_linha_poetica(tema_variacao)
            palavras = linha_base.split()
            
            # Substituir última palavra por uma rima
            if palavras and info_padrao["rimas"]:
                rima = info_padrao["rimas"][0]
                info_padrao["rimas"].remove(rima)
                # Se não temos mais rimas, reciclar a última palavra
                if not info_padrao["rimas"]:
                    info_padrao["rimas"] = [info_padrao["ultima_palavra"]]
                
                linha = " ".join(palavras[:-1] + [rima]).capitalize()
            else:
                linha = linha_base.capitalize()
            
            info_padrao["linhas_geradas"].append(linha)
        
        refrao.append(linha)
    
    # Garantir que não temos linhas idênticas consecutivas
    for i in range(1, len(refrao)):
        if refrao[i] == refrao[i-1]:
            # Modificar levemente a linha
            palavras = refrao[i].split()
            if len(palavras) > 3:
                # Trocar uma palavra do meio
                indice_meio = len(palavras) // 2
                palavras_alternativas = obter_vocabulario_genero(subgenero, "substantivos")
                if palavras_alternativas:
                    palavras[indice_meio] = random.choice(palavras_alternativas)
                    refrao[i] = " ".join(palavras).capitalize()
    
    return refrao, esquema

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
    
    # Gerar tema base para toda a música
    tema_base = gerar_tema_completo(subgenero)
    print(f"Tema base gerado: {tema_base}")
    
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
            linhas = 8
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
        
        # Usar função especializada para refrão, estrofe normal para o resto
        if parte == "refrao":
            frases, esquema = gerar_refrao(subgenero, linhas, tema_base)
        else:
            frases, esquema = gerar_estrofe(subgenero, parte, linhas, tema_base)
        
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
                    progressoes_disponiveis.append(p["progressao"])
            
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
    
    # Formatar a letra - Corrigido o problema com f-strings e barras invertidas
    intro_text = "INTRO:" + "\n" + "\n".join(partes["intro"]) + "\n\n"
    letra_formatada = intro_text
    
    # Adicionar as partes na ordem da estrutura
    for parte in estrutura:
        if parte == "intro":
            continue  # Já adicionado
        
        parte_nome = parte.upper()
        if parte == "verso":
            parte_nome = "VERSO"
        elif parte == "refrao":
            parte_nome = "REFRÃO"
        elif parte == "ponte":
            parte_nome = "PONTE"
        elif parte == "pre_refrao":
            parte_nome = "PRÉ-REFRÃO"
        elif parte == "outro":
            parte_nome = "OUTRO"
        
        parte_text = parte_nome + ":" + "\n" + "\n".join(partes[parte]) + "\n\n"
        letra_formatada += parte_text
    
    # Buscar letra de uma música da banda referência
    letra_banda = buscar_letra(banda_ref)
    
    # Retornar os valores
    return banda_ref, acordes, letra_formatada, letra_banda

# Interface Gradio
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as app:
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
