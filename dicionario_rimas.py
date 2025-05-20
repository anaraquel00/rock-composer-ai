"""
Biblioteca aprimorada de dicionário de rimas para o Rock Composer AI.
Inclui categorização por tipo de palavra, classificação fonética e vocabulário específico por gênero musical.
"""

# Classificação de rimas por tipo
TIPOS_RIMA = {
    "consoante": "Rima em que consoantes e vogais coincidem",
    "toante": "Rima em que apenas as vogais coincidem",
    "rica": "Rima entre palavras de classes gramaticais diferentes",
    "pobre": "Rima entre palavras da mesma classe gramatical"
}

# Classificação gramatical
CLASSES_GRAMATICAIS = [
    "substantivo",
    "verbo",
    "adjetivo",
    "advérbio"
]

# Dicionário de rimas expandido e categorizado
DICIONARIO_RIMAS = {
    # Substantivos
    "ação": {
        "rimas": ["rebelião", "emancipação", "transformação", "revolução", "canção", "coração", "solidão", "visão", "emoção", "paixão"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "dor": {
        "rimas": ["valor", "tambor", "ardor", "amor", "clamor", "fervor", "temor", "calor", "horror", "torpor"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "noite": {
        "rimas": ["açoite", "alqueire", "convite", "deite", "enfeite", "leite", "deleite", "azeite", "peito", "efeito"],
        "tipo": "toante",
        "classe": "substantivo"
    },
    "mar": {
        "rimas": ["polar", "vulgar", "altar", "lar", "lunar", "celular", "singular", "familiar", "militar", "solar"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "vida": {
        "rimas": ["ferida", "cumprida", "descida", "saída", "comida", "bebida", "medida", "perdida", "querida", "bandida"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "som": {
        "rimas": ["tom", "dom", "pavão", "bom", "bombom", "batom", "garçom", "pompom", "marrom", "rinoceronte"],
        "tipo": "toante",
        "classe": "substantivo"
    },
    "coração": {
        "rimas": ["solidão", "revolução", "ilusão", "paixão", "emoção", "canção", "visão", "tensão", "razão", "traição"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "luz": {
        "rimas": ["cruz", "fuz", "seduz", "conduz", "produz", "induz", "reduz", "traduz", "capuz", "avestruz"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "sombras": {
        "rimas": ["palavras", "camas", "tramas", "chamas", "dramas", "famas", "gramas", "lamas", "ramas", "damas"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "silêncio": {
        "rimas": ["conhecimento", "sentimento", "movimento", "momento", "pensamento", "sofrimento", "elemento", "argumento", "lamento", "tormento"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "memórias": {
        "rimas": ["histórias", "vitórias", "glórias", "notórias", "trajetórias", "acessórias", "transitórias", "preparatórias", "oratórias", "conservatórias"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "sonhos": {
        "rimas": ["caminhos", "rinhos", "vinhos", "espinhos", "anjinhos", "sozinhos", "vizinhos", "carinhos", "ninhos", "gordinhos"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "natureza": {
        "rimas": ["beleza", "certeza", "pureza", "tristeza", "realeza", "fortaleza", "riqueza", "pobreza", "dureza", "frieza"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "tranquilidade": {
        "rimas": ["felicidade", "solidão", "eternidade", "cidade", "idade", "verdade", "bondade", "maldade", "saudade", "liberdade"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "mistério": {
        "rimas": ["sério", "critério", "interesse", "império", "cemitério", "refrigério", "vitupério", "ministério", "magistério", "improperio"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    "reflexão": {
        "rimas": ["ação", "revolução", "ilusão", "canção", "coração", "paixão", "visão", "tensão", "razão", "traição"],
        "tipo": "consoante",
        "classe": "substantivo"
    },
    
    # Verbos
    "cantar": {
        "rimas": ["amar", "sonhar", "voar", "chorar", "lutar", "dançar", "gritar", "pensar", "falar", "olhar"],
        "tipo": "consoante",
        "classe": "verbo"
    },
    "viver": {
        "rimas": ["morrer", "sofrer", "correr", "perder", "crescer", "nascer", "conhecer", "esquecer", "entender", "aprender"],
        "tipo": "consoante",
        "classe": "verbo"
    },
    "sentir": {
        "rimas": ["partir", "sorrir", "seguir", "fugir", "mentir", "dormir", "existir", "dividir", "decidir", "permitir"],
        "tipo": "consoante",
        "classe": "verbo"
    },
    "gritar": {
        "rimas": ["chorar", "lutar", "sonhar", "amar", "voar", "dançar", "cantar", "pensar", "falar", "olhar"],
        "tipo": "consoante",
        "classe": "verbo"
    },
    
    # Adjetivos
    "intenso": {
        "rimas": ["imenso", "denso", "suspenso", "tenso", "extenso", "propenso", "penso", "incenso", "consenso", "senso"],
        "tipo": "consoante",
        "classe": "adjetivo"
    },
    "profundo": {
        "rimas": ["mundo", "segundo", "fundo", "imundo", "moribundo", "vagabundo", "furibundo", "oriundo", "rotundo", "infecundo"],
        "tipo": "consoante",
        "classe": "adjetivo"
    },
    "eterno": {
        "rimas": ["inverno", "inferno", "moderno", "governo", "externo", "interno", "paterno", "materno", "alterno", "superno"],
        "tipo": "consoante",
        "classe": "adjetivo"
    },
    "sombrio": {
        "rimas": ["frio", "vazio", "tardio", "arrepio", "desvio", "tio", "rio", "navio", "desafio", "estio"],
        "tipo": "consoante",
        "classe": "adjetivo"
    }
}

# Vocabulário específico por gênero musical
VOCABULARIO_GENEROS = {
    "Metal/Death Metal": {
        "substantivos": ["morte", "sangue", "guerra", "trevas", "abismo", "inferno", "caos", "demônio", "destruição", "escuridão", "ruína", "apocalipse", "fúria", "agonia", "tormento"],
        "verbos": ["destruir", "queimar", "dilacerar", "esmagar", "devorar", "aniquilar", "despedaçar", "massacrar", "exterminar", "torturar"],
        "adjetivos": ["sombrio", "sangrento", "brutal", "mortal", "infernal", "demoníaco", "obscuro", "macabro", "tenebroso", "sinistro"]
    },
    "Metal/Power Metal": {
        "substantivos": ["glória", "honra", "espada", "dragão", "herói", "batalha", "vitória", "lenda", "guerreiro", "destino", "magia", "reino", "poder", "chama", "liberdade"],
        "verbos": ["conquistar", "lutar", "vencer", "cavalgar", "empunhar", "triunfar", "defender", "proteger", "governar", "reinar"],
        "adjetivos": ["épico", "glorioso", "poderoso", "lendário", "heróico", "mágico", "valente", "nobre", "eterno", "invencível"]
    },
    "Punk/Hardcore": {
        "substantivos": ["revolta", "sistema", "caos", "anarquia", "protesto", "rua", "luta", "opressão", "liberdade", "rebelião", "resistência", "revolução", "injustiça", "sociedade", "controle"],
        "verbos": ["lutar", "resistir", "gritar", "quebrar", "protestar", "rebelar", "confrontar", "desafiar", "destruir", "libertar"],
        "adjetivos": ["rebelde", "furioso", "anárquico", "cru", "direto", "intenso", "revoltado", "livre", "inconformado", "subversivo"]
    },
    "Shoegaze": {
        "substantivos": ["sonho", "névoa", "onda", "eco", "distância", "véu", "sussurro", "nuvem", "oceano", "horizonte", "reflexo", "espelho", "vazio", "silêncio", "etéreo"],
        "verbos": ["flutuar", "desvanecer", "ecoar", "dissipar", "envolver", "sussurrar", "embalar", "deslizar", "mergulhar", "contemplar"],
        "adjetivos": ["etéreo", "nebuloso", "distante", "onírico", "flutuante", "vaporoso", "difuso", "reverberante", "translúcido", "hipnótico"]
    },
    "Dream Rock": {
        "substantivos": ["sonho", "lua", "estrela", "céu", "nuvem", "mar", "vento", "noite", "sussurro", "mistério", "sombra", "luz", "reflexo", "espelho", "alma"],
        "verbos": ["sonhar", "flutuar", "brilhar", "sussurrar", "embalar", "envolver", "acariciar", "deslizar", "contemplar", "adormecer"],
        "adjetivos": ["onírico", "suave", "etéreo", "celestial", "sereno", "calmo", "misterioso", "delicado", "luminoso", "translúcido"]
    },
    "Alternative Rock": {
        "substantivos": ["mente", "dúvida", "caminho", "verdade", "mentira", "mundo", "realidade", "ilusão", "confusão", "contradição", "angústia", "desespero", "esperança", "mudança", "tempo"],
        "verbos": ["questionar", "procurar", "encontrar", "perder", "mudar", "transformar", "enfrentar", "desafiar", "descobrir", "entender"],
        "adjetivos": ["confuso", "perdido", "contraditório", "intenso", "reflexivo", "introspectivo", "complexo", "profundo", "angustiado", "esperançoso"]
    },
    "Indie Rock": {
        "substantivos": ["coração", "amor", "cidade", "rua", "café", "livro", "filme", "viagem", "memória", "nostalgia", "amizade", "solidão", "juventude", "outono", "inverno"],
        "verbos": ["sentir", "lembrar", "viajar", "encontrar", "perder", "amar", "sonhar", "observar", "escrever", "cantar"],
        "adjetivos": ["nostálgico", "melancólico", "introspectivo", "sensível", "urbano", "vintage", "indie", "alternativo", "intimista", "autêntico"]
    },
    "Post-Rock": {
        "substantivos": ["horizonte", "oceano", "montanha", "céu", "tempestade", "silêncio", "vastidão", "infinito", "cosmos", "abismo", "jornada", "paisagem", "natureza", "universo", "transcendência"],
        "verbos": ["expandir", "transcender", "elevar", "construir", "crescer", "explorar", "viajar", "contemplar", "imergir", "transformar"],
        "adjetivos": ["vasto", "expansivo", "atmosférico", "cinemático", "épico", "transcendental", "contemplativo", "crescente", "dinâmico", "imersivo"]
    }
}

# Função para obter rimas por palavra
def obter_rimas(palavra):
    """
    Retorna as rimas disponíveis para uma palavra específica.
    
    Args:
        palavra (str): A palavra para a qual se deseja encontrar rimas.
        
    Returns:
        dict: Dicionário contendo as rimas, tipo e classe gramatical da palavra.
    """
    palavra = palavra.lower()
    if palavra in DICIONARIO_RIMAS:
        return DICIONARIO_RIMAS[palavra]
    return None

# Função para obter rimas por sufixo
def obter_rimas_por_sufixo(sufixo, tamanho=2):
    """
    Retorna palavras que rimam com base em um sufixo.
    
    Args:
        sufixo (str): O sufixo para buscar rimas.
        tamanho (int): Tamanho mínimo do sufixo para considerar como rima.
        
    Returns:
        list: Lista de palavras que rimam com o sufixo fornecido.
    """
    if len(sufixo) < tamanho:
        return []
    
    sufixo = sufixo.lower()
    rimas = []
    
    for palavra, info in DICIONARIO_RIMAS.items():
        if palavra.endswith(sufixo):
            rimas.append(palavra)
        for rima in info["rimas"]:
            if rima.endswith(sufixo) and rima not in rimas:
                rimas.append(rima)
    
    return rimas

# Função para obter vocabulário específico por gênero
def obter_vocabulario_genero(genero, classe=None):
    """
    Retorna vocabulário específico para um gênero musical.
    
    Args:
        genero (str): O gênero musical.
        classe (str, optional): Classe gramatical específica (substantivos, verbos, adjetivos).
        
    Returns:
        dict ou list: Dicionário com todas as classes ou lista de palavras da classe especificada.
    """
    if genero not in VOCABULARIO_GENEROS:
        return {}
    
    if classe and classe in VOCABULARIO_GENEROS[genero]:
        return VOCABULARIO_GENEROS[genero][classe]
    
    return VOCABULARIO_GENEROS[genero]

# Função para gerar rima com validação de comprimento
def gerar_rima(palavra, silabas=3):
    """
    Versão aprimorada da função gerar_rima original.
    Gera uma rima para a palavra fornecida, respeitando o número de sílabas.
    
    Args:
        palavra (str): A palavra para a qual se deseja gerar uma rima.
        silabas (int): Número mínimo de sílabas para considerar.
        
    Returns:
        str: Uma palavra que rima com a entrada.
    """
    import random
    
    # Se a palavra for muito curta, retorna ela mesma
    if len(palavra) < silabas:
        return palavra
    
    # Tenta encontrar no dicionário primeiro
    if palavra.lower() in DICIONARIO_RIMAS:
        rimas_disponiveis = DICIONARIO_RIMAS[palavra.lower()]["rimas"]
        return random.choice(rimas_disponiveis)
    
    # Se não encontrar, tenta pelo sufixo
    sufixos = {
        2: palavra[-2:],
        3: palavra[-3:],
        4: palavra[-4:]
    }
    
    # Tenta com sufixos de diferentes tamanhos
    for tamanho in [4, 3, 2]:
        if len(palavra) >= tamanho:
            rimas = obter_rimas_por_sufixo(sufixos[tamanho], tamanho)
            if rimas and palavra.lower() in rimas:
                rimas.remove(palavra.lower())
            if rimas:
                return random.choice(rimas)
    
    # Se não encontrar nada, retorna a própria palavra
    return palavra
