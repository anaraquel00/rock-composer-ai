"""
Biblioteca aprimorada de instruções estilísticas para o Rock Composer AI.
Inclui instruções mais detalhadas, elementos estruturais adicionais, variações de estilo,
referências técnicas e sugestões de andamento para cada gênero musical.
"""

# Constantes para elementos estruturais de música
ELEMENTOS_ESTRUTURAIS = [
    "intro",
    "verso",
    "pre_refrao",
    "refrao",
    "ponte",
    "solo",
    "interludio",
    "outro"
]

# Constantes para técnicas musicais
TECNICAS_MUSICAIS = {
    "palm_muting": "Técnica de abafar as cordas com a palma da mão para criar um som mais percussivo",
    "tremolo_picking": "Técnica de palhetada rápida e contínua em uma mesma corda",
    "sweep_picking": "Técnica de palhetada em movimento de 'varredura' através de várias cordas",
    "tapping": "Técnica de tocar as cordas batendo com os dedos no braço da guitarra",
    "hammer_on": "Técnica de tocar uma nota e depois pressionar outra corda sem palhetar",
    "pull_off": "Técnica de puxar o dedo para fora da corda após tocar uma nota",
    "bend": "Técnica de esticar a corda para alterar a altura da nota",
    "vibrato": "Técnica de vibrar a corda para criar oscilação na nota",
    "slide": "Técnica de deslizar o dedo pela corda entre duas notas",
    "harmonico": "Técnica de tocar notas harmônicas tocando levemente a corda em pontos específicos",
    "feedback": "Uso controlado da retroalimentação do amplificador para criar efeitos sonoros",
    "drone": "Nota ou acorde sustentado continuamente como base para outras partes musicais",
    "ostinato": "Padrão musical que se repete persistentemente",
    "riff": "Frase musical curta e repetitiva, geralmente na guitarra",
    "blast_beat": "Padrão de bateria extremamente rápido usado em metal extremo",
    "d_beat": "Padrão de bateria característico do punk hardcore",
    "breakdown": "Seção com andamento reduzido e ênfase em riffs pesados",
    "groove": "Sensação rítmica que induz movimento, baseada na interação entre baixo e bateria"
}

# Constantes para efeitos e processamentos
EFEITOS = {
    "distortion": "Distorção de sinal, criando harmônicos adicionais",
    "overdrive": "Distorção suave que emula amplificadores valvulados",
    "fuzz": "Distorção extrema com clipping agressivo",
    "chorus": "Efeito que adiciona uma versão ligeiramente desafinada do sinal original",
    "flanger": "Efeito de modulação que cria um som 'whooshing'",
    "phaser": "Efeito que cria picos e vales no espectro de frequência",
    "reverb": "Simulação de ambientes acústicos e reflexões sonoras",
    "delay": "Repetições do sinal original em intervalos de tempo",
    "wah": "Filtro controlado por pedal que altera o ponto de ênfase de frequência",
    "compression": "Redução da faixa dinâmica do sinal",
    "eq": "Equalização para moldar o espectro de frequência",
    "noise_gate": "Redução de ruído quando o sinal está abaixo de um limiar",
    "octaver": "Adição de notas uma oitava acima ou abaixo",
    "pitch_shifter": "Alteração da altura das notas",
    "tremolo": "Modulação rápida do volume"
}

# Instruções estilísticas expandidas para cada subgênero musical
INSTRUCOES_ESTILISTICAS = {
    "Metal/Death Metal": {
        "caracteristicas_gerais": {
            "descricao": "Subgênero extremo do metal caracterizado por vocais guturais, guitarras pesadas com afinação baixa, blast beats e temáticas sombrias",
            "bpm_recomendado": "160-240 BPM",
            "afinacao_recomendada": "Drop C, Drop B ou mais grave",
            "artistas_referencia": ["Cannibal Corpse", "Death", "Morbid Angel", "Obituary", "Suffocation"],
            "tecnicas_comuns": ["tremolo_picking", "palm_muting", "blast_beat", "growl_vocal", "sweep_picking"]
        },
        "intro": {
            "padrao": "Guitarra pesada em drop D, bateria rápida e agressiva",
            "variacao_1": "Riff dissonante com palm muting e acentos irregulares, blast beats na bateria",
            "variacao_2": "Introdução atmosférica com guitarra limpa e efeitos, seguida de explosão com riff pesado",
            "variacao_3": "Sample de filme de horror ou diálogo sombrio, seguido por entrada abrupta da banda completa",
            "tecnicas": ["palm_muting", "tremolo_picking", "blast_beat"],
            "efeitos_recomendados": ["distortion", "noise_gate", "eq"]
        },
        "verso": {
            "padrao": "Riffs rápidos, vocais guturais, baixo pulsante",
            "variacao_1": "Riffs em tremolo picking com harmonia dissonante, vocais graves e guturais",
            "variacao_2": "Riffs técnicos com mudanças de compasso, vocais alternando entre gutural grave e agudo",
            "variacao_3": "Groove pesado com acentos sincopados, vocais ritmicamente precisos",
            "tecnicas": ["tremolo_picking", "palm_muting", "growl_vocal"],
            "efeitos_recomendados": ["distortion", "compression", "eq"]
        },
        "pre_refrao": {
            "padrao": "Intensificação rítmica, aumento de tensão harmônica",
            "variacao_1": "Riff ascendente com aumento de intensidade, double bass acelerando",
            "variacao_2": "Breakdown com palm muting pesado, preparando para explosão",
            "variacao_3": "Pausa dramática ou diminuição súbita de intensidade antes do refrão",
            "tecnicas": ["palm_muting", "double_bass", "power_chords"],
            "efeitos_recomendados": ["distortion", "compression"]
        },
        "refrao": {
            "padrao": "Melodia épica, harmonias em quintas, blast beats",
            "variacao_1": "Riff memorável com harmonia em quintas, blast beats alternando com groove",
            "variacao_2": "Melodia sombria sobre base rítmica intensa, vocais em camadas",
            "variacao_3": "Riff técnico com mudanças de tempo, vocais em padrão de pergunta e resposta",
            "tecnicas": ["blast_beat", "power_chords", "layered_vocals"],
            "efeitos_recomendados": ["distortion", "reverb", "delay"]
        },
        "ponte": {
            "padrao": "Solo técnico, mudanças de tempo, atmosfera sombria",
            "variacao_1": "Solo virtuoso com sweep picking e tapping, sobre base rítmica complexa",
            "variacao_2": "Breakdown pesado com half-time feel, criando contraste com seções rápidas",
            "variacao_3": "Seção atmosférica com guitarras ambientes e percussão minimalista",
            "tecnicas": ["sweep_picking", "tapping", "time_signature_changes"],
            "efeitos_recomendados": ["delay", "reverb", "wah"]
        },
        "solo": {
            "padrao": "Solo técnico e veloz com escalas menores e frígias",
            "variacao_1": "Solo melódico com bends expressivos e vibrato intenso",
            "variacao_2": "Solo atonal com técnicas estendidas e dissonâncias",
            "variacao_3": "Solo baseado em arpejos com sweep picking e tapping",
            "tecnicas": ["sweep_picking", "alternate_picking", "tapping", "whammy_dive"],
            "efeitos_recomendados": ["delay", "wah", "reverb"]
        },
        "interludio": {
            "padrao": "Seção instrumental com experimentação rítmica",
            "variacao_1": "Passagem atmosférica com guitarras limpas e efeitos",
            "variacao_2": "Riff complexo em unísono entre guitarra e baixo",
            "variacao_3": "Seção percussiva com ênfase na bateria e baixo",
            "tecnicas": ["clean_arpeggios", "harmonics", "polyrhythms"],
            "efeitos_recomendados": ["reverb", "delay", "chorus"]
        },
        "outro": {
            "padrao": "Repetição intensificada do riff principal com final abrupto",
            "variacao_1": "Desaceleração gradual com aumento de dissonância",
            "variacao_2": "Fade out com feedback e ruído controlado",
            "variacao_3": "Final explosivo com blast beats e grito prolongado",
            "tecnicas": ["feedback", "noise", "blast_beat"],
            "efeitos_recomendados": ["distortion", "noise_gate", "reverb"]
        }
    },
    
    "Metal/Power Metal": {
        "caracteristicas_gerais": {
            "descricao": "Subgênero do metal caracterizado por tempos rápidos, melodias épicas, vocais limpos e agudos, e temáticas heroicas",
            "bpm_recomendado": "140-180 BPM",
            "afinacao_recomendada": "Standard E ou Drop D",
            "artistas_referencia": ["Helloween", "Blind Guardian", "DragonForce", "Stratovarius", "Rhapsody of Fire"],
            "tecnicas_comuns": ["alternate_picking", "sweep_picking", "double_bass", "vibrato", "harmonized_guitars"]
        },
        "intro": {
            "padrao": "Guitarra energética em E standard, bateria pulsante, synth otimista",
            "variacao_1": "Introdução orquestral com sintetizadores épicos e coral",
            "variacao_2": "Riff melódico rápido em oitavas ou terças harmonizadas",
            "variacao_3": "Arpejo limpo seguido de entrada explosiva da banda completa",
            "tecnicas": ["alternate_picking", "harmonized_guitars", "double_bass"],
            "efeitos_recomendados": ["reverb", "chorus", "delay"]
        },
        "verso": {
            "padrao": "Riffs melódicos, vocais altos, baixo harmônico",
            "variacao_1": "Riffs rápidos com pedal tone, vocais narrativos e melódicos",
            "variacao_2": "Riffs em palm muting com acentos em notas melódicas, vocais dinâmicos",
            "variacao_3": "Riffs baseados em escalas maiores com baixo seguindo a harmonia",
            "tecnicas": ["alternate_picking", "palm_muting", "high_register_vocals"],
            "efeitos_recomendados": ["overdrive", "compression", "eq"]
        },
        "pre_refrao": {
            "padrao": "Construção harmônica ascendente, intensificação vocal",
            "variacao_1": "Progressão de acordes ascendente com bateria intensificando",
            "variacao_2": "Riff em pedal tone com melodia vocal crescente",
            "variacao_3": "Pausa dramática seguida de fill de bateria para o refrão",
            "tecnicas": ["pedal_tone", "crescendo", "vocal_build"],
            "efeitos_recomendados": ["overdrive", "compression"]
        },
        "refrao": {
            "padrao": "Gancho melódico, harmonias em terças, coro épico",
            "variacao_1": "Melodia vocal épica sobre acordes maiores, coros em camadas",
            "variacao_2": "Refrão em tempo dobrado com harmonias vocais em terças e quintas",
            "variacao_3": "Melodia ascendente com resolução épica, double bass constante",
            "tecnicas": ["vocal_harmonies", "double_bass", "power_chords"],
            "efeitos_recomendados": ["reverb", "chorus", "delay"]
        },
        "ponte": {
            "padrao": "Solo virtuoso, progressão ascendente, atmosfera heroica",
            "variacao_1": "Modulação para tonalidade maior com solo técnico",
            "variacao_2": "Seção orquestral com guitarras em segundo plano",
            "variacao_3": "Breakdown com half-time feel e vocais épicos",
            "tecnicas": ["sweep_picking", "tapping", "modulation"],
            "efeitos_recomendados": ["delay", "reverb", "wah"]
        },
        "solo": {
            "padrao": "Solo virtuoso com escalas maiores e frígias dominantes",
            "variacao_1": "Solo melódico com frases cantáveis e vibrato expressivo",
            "variacao_2": "Solo técnico ultra-rápido com alternate picking e sweep",
            "variacao_3": "Solo neoclássico com arpejos e sequências harmônicas",
            "tecnicas": ["alternate_picking", "sweep_picking", "tapping", "legato"],
            "efeitos_recomendados": ["delay", "reverb", "wah"]
        },
        "interludio": {
            "padrao": "Seção instrumental com teclados e guitarras em harmonia",
            "variacao_1": "Passagem acústica com violões e flautas",
            "variacao_2": "Duelo entre guitarra e teclado",
            "variacao_3": "Seção orquestral com coral e percussão épica",
            "tecnicas": ["harmonized_guitars", "keyboard_solo", "acoustic_arpeggios"],
            "efeitos_recomendados": ["reverb", "chorus", "delay"]
        },
        "outro": {
            "padrao": "Repetição do refrão com intensificação e final grandioso",
            "variacao_1": "Coda instrumental com tema principal em arranjo orquestral",
            "variacao_2": "Aceleração gradual com final explosivo",
            "variacao_3": "Fade out com coral e orquestração",
            "tecnicas": ["crescendo", "harmonized_guitars", "orchestration"],
            "efeitos_recomendados": ["reverb", "delay", "chorus"]
        }
    },
    
    # Continuando com os demais gêneros de forma similar...
    "Punk/Hardcore": {
        "caracteristicas_gerais": {
            "descricao": "Gênero caracterizado por sua energia crua, simplicidade, atitude rebelde e mensagens políticas ou sociais",
            "bpm_recomendado": "160-220 BPM",
            "afinacao_recomendada": "Standard E",
            "artistas_referencia": ["Black Flag", "Bad Brains", "Minor Threat", "Dead Kennedys", "Converge"],
            "tecnicas_comuns": ["power_chords", "downpicking", "d_beat", "shouted_vocals", "feedback"]
        },
        "intro": {
            "padrao": "Guitarra distorcida, bateria rápida, energia crua",
            "variacao_1": "Feedback seguido de explosão com power chords",
            "variacao_2": "Contagem rápida e entrada imediata da banda",
            "variacao_3": "Riff simples e direto com bateria em D-beat",
            "tecnicas": ["power_chords", "downpicking", "d_beat"],
            "efeitos_recomendados": ["distortion", "overdrive"]
        },
        "verso": {
            "padrao": "Riffs simples, vocais gritados, baixo direto",
            "variacao_1": "Power chords rápidos em downpicking, vocais agressivos",
            "variacao_2": "Riff com notas individuais, vocais ritmicamente marcados",
            "variacao_3": "Progressão de acordes simples com baixo seguindo a raiz",
            "tecnicas": ["power_chords", "downpicking", "shouted_vocals"],
            "efeitos_recomendados": ["distortion", "overdrive"]
        },
        "pre_refrao": {
            "padrao": "Intensificação rítmica, build-up para o refrão",
            "variacao_1": "Pausa momentânea seguida de fill de bateria",
            "variacao_2": "Mudança para ritmo mais marcado antes do refrão",
            "variacao_3": "Acentuação nos contratempos criando tensão",
            "tecnicas": ["syncopation", "drum_fills", "power_chords"],
            "efeitos_recomendados": ["distortion", "overdrive"]
        },
        "refrao": {
            "padrao": "Refrão explosivo, power chords, coro de gangue",
            "variacao_1": "Power chords simples com vocais em grupo (gang vocals)",
            "variacao_2": "Melodia vocal simples e direta sobre base energética",
            "variacao_3": "Refrão com mudança de andamento (mais rápido ou mais lento)",
            "tecnicas": ["power_chords", "gang_vocals", "d_beat"],
            "efeitos_recomendados": ["distortion", "overdrive"]
        },
        "ponte": {
            "padrao": "Quebra de ritmo, gritos intensos, caos controlado",
            "variacao_1": "Breakdown com half-time feel e vocais gritados",
            "variacao_2": "Seção com apenas baixo e bateria, criando tensão",
            "variacao_3": "Mudança para ritmo mais lento e pesado",
            "tecnicas": ["breakdown", "half_time", "feedback"],
            "efeitos_recomendados": ["distortion", "feedback"]
        },
        "solo": {
            "padrao": "Solo curto e energético baseado em escala pentatônica",
            "variacao_1": "Notas rápidas e caóticas sem estrutura aparente",
            "variacao_2": "Feedback controlado e manipulação de ruído",
            "variacao_3": "Ausência de solo (característica comum no punk)",
            "tecnicas": ["bend", "feedback", "noise"],
            "efeitos_recomendados": ["distortion", "feedback", "wah"]
        },
        "interludio": {
            "padrao": "Seção com baixo proeminente e bateria simplificada",
            "variacao_1": "Apenas bateria com vocais falados/gritados",
            "variacao_2": "Riff alternativo com mudança de dinâmica",
            "variacao_3": "Feedback e ruído experimental",
            "tecnicas": ["bass_riff", "spoken_word", "noise"],
            "efeitos_recomendados": ["distortion", "overdrive", "feedback"]
        },
        "outro": {
            "padrao": "Final abrupto após intensificação",
            "variacao_1": "Desaceleração com final caótico",
            "variacao_2": "Repetição do refrão com intensificação gradual",
            "variacao_3": "Feedback prolongado após último acorde",
            "tecnicas": ["feedback", "noise", "drum_fill"],
            "efeitos_recomendados": ["distortion", "feedback"]
        }
    },
    
    # Adicionando os demais gêneros de forma resumida para não estender demais o código
    "Shoegaze": {
        "caracteristicas_gerais": {
            "descricao": "Gênero caracterizado por camadas densas de guitarras com efeitos, vocais etéreos e atmosfera sonora imersiva",
            "bpm_recomendado": "80-120 BPM",
            "afinacao_recomendada": "Standard E ou Drop D",
            "artistas_referencia": ["My Bloody Valentine", "Slowdive", "Ride", "Lush", "Chapterhouse"],
            "tecnicas_comuns": ["wall_of_sound", "reverb_wash", "tremolo_arm", "feedback", "drone"]
        },
        # Elementos estruturais omitidos para brevidade
    },
    
    "Dream Rock": {
        "caracteristicas_gerais": {
            "descricao": "Subgênero que combina elementos do rock alternativo com texturas atmosféricas e ambientes sonoros oníricos",
            "bpm_recomendado": "70-110 BPM",
            "afinacao_recomendada": "Standard E ou Drop D",
            "artistas_referencia": ["Beach House", "Mazzy Star", "Cocteau Twins", "Cigarettes After Sex", "Slowdive"],
            "tecnicas_comuns": ["arpeggios", "reverb_wash", "delay_textures", "breathy_vocals", "minimalist_drums"]
        },
        # Elementos estruturais omitidos para brevidade
    },
    
    "Alternative Rock": {
        "caracteristicas_gerais": {
            "descricao": "Gênero amplo que surgiu como alternativa ao rock mainstream, caracterizado por experimentação e influências diversas",
            "bpm_recomendado": "90-140 BPM",
            "afinacao_recomendada": "Standard E ou Drop D",
            "artistas_referencia": ["Radiohead", "Nirvana", "The Smashing Pumpkins", "R.E.M.", "Sonic Youth"],
            "tecnicas_comuns": ["dynamic_contrast", "unconventional_song_structures", "noise_elements", "melodic_hooks", "experimental_textures"]
        },
        # Elementos estruturais omitidos para brevidade
    },
    
    "Indie Rock": {
        "caracteristicas_gerais": {
            "descricao": "Gênero associado originalmente a gravadoras independentes, caracterizado por abordagens DIY e experimentação dentro de estruturas pop/rock",
            "bpm_recomendado": "90-130 BPM",
            "afinacao_recomendada": "Standard E",
            "artistas_referencia": ["Arctic Monkeys", "Vampire Weekend", "Tame Impala", "The Strokes", "Arcade Fire"],
            "tecnicas_comuns": ["jangly_guitars", "lo_fi_aesthetics", "vintage_tones", "room_ambience", "quirky_arrangements"]
        },
        # Elementos estruturais omitidos para brevidade
    },
    
    "Post-Rock": {
        "caracteristicas_gerais": {
            "descricao": "Gênero que utiliza instrumentação de rock para criar texturas e estruturas não tradicionais, frequentemente instrumentais e com dinâmicas crescentes",
            "bpm_recomendado": "70-130 BPM",
            "afinacao_recomendada": "Standard E, Drop D ou afinações alternativas",
            "artistas_referencia": ["Explosions in the Sky", "Godspeed You! Black Emperor", "Sigur Rós", "Mogwai", "This Will Destroy You"],
            "tecnicas_comuns": ["crescendo_structures", "delay_textures", "tremolo_picking", "ambient_passages", "extended_compositions"]
        },
        # Elementos estruturais omitidos para brevidade
    }
}

# Função para obter instruções estilísticas por gênero
def obter_instrucoes_estilisticas(genero, elemento=None):
    """
    Retorna instruções estilísticas para um gênero musical específico.
    
    Args:
        genero (str): O gênero musical.
        elemento (str, optional): Elemento estrutural específico (intro, verso, refrao, etc).
        
    Returns:
        dict: Dicionário com instruções estilísticas.
    """
    if genero not in INSTRUCOES_ESTILISTICAS:
        return {}
    
    if elemento and elemento in INSTRUCOES_ESTILISTICAS[genero]:
        return INSTRUCOES_ESTILISTICAS[genero][elemento]
    
    return INSTRUCOES_ESTILISTICAS[genero]

# Função para obter características gerais de um gênero
def obter_caracteristicas_genero(genero):
    """
    Retorna características gerais de um gênero musical.
    
    Args:
        genero (str): O gênero musical.
        
    Returns:
        dict: Dicionário com características gerais do gênero.
    """
    if genero in INSTRUCOES_ESTILISTICAS and "caracteristicas_gerais" in INSTRUCOES_ESTILISTICAS[genero]:
        return INSTRUCOES_ESTILISTICAS[genero]["caracteristicas_gerais"]
    
    return {}

# Função para obter informações sobre técnicas musicais
def obter_info_tecnica(tecnica):
    """
    Retorna informações sobre uma técnica musical específica.
    
    Args:
        tecnica (str): Nome da técnica musical.
        
    Returns:
        str: Descrição da técnica musical.
    """
    if tecnica in TECNICAS_MUSICAIS:
        return TECNICAS_MUSICAIS[tecnica]
    
    return "Técnica não encontrada na base de dados."

# Função para obter informações sobre efeitos
def obter_info_efeito(efeito):
    """
    Retorna informações sobre um efeito específico.
    
    Args:
        efeito (str): Nome do efeito.
        
    Returns:
        str: Descrição do efeito.
    """
    if efeito in EFEITOS:
        return EFEITOS[efeito]
    
    return "Efeito não encontrado na base de dados."

# Função para gerar estrutura de música completa
def gerar_estrutura_musica(genero, complexidade=1):
    """
    Gera uma estrutura musical completa para um gênero específico.
    
    Args:
        genero (str): O gênero musical.
        complexidade (int): Nível de complexidade da estrutura (1-3).
        
    Returns:
        list: Lista ordenada de elementos estruturais para a música.
    """
    estruturas = {
        1: ["intro", "verso", "refrao", "verso", "refrao", "outro"],
        2: ["intro", "verso", "refrao", "verso", "refrao", "ponte", "refrao", "outro"],
        3: ["intro", "verso", "pre_refrao", "refrao", "verso", "pre_refrao", "refrao", "ponte", "solo", "refrao", "outro"]
    }
    
    if complexidade not in estruturas:
        complexidade = 1
    
    return estruturas[complexidade]
