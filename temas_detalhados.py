"""
Biblioteca aprimorada de temas detalhados para o Rock Composer AI.
Inclui temas mais ricos e variados, categorias adicionais, contexto histórico,
temas contemporâneos e sistema de combinação dinâmica para cada gênero musical.
"""

# Constantes para categorias temáticas
CATEGORIAS_TEMATICAS = [
    "nucleos",
    "acoes",
    "elementos",
    "cenarios",
    "personagens",
    "conflitos",
    "emocoes",
    "simbolos",
    "periodos_historicos",
    "temas_contemporaneos"
]

# Temas detalhados expandidos para cada subgênero musical
TEMAS_DETALHADOS = {
    "Metal/Death Metal": {
        "nucleos": [
            "morte iminente", "sangue ancestral", "ritual profano", "trevas eternas", 
            "abismo infernal", "caos primordial", "demônio interior", "destruição total",
            "escuridão absoluta", "ruína da humanidade", "apocalipse final", "fúria demoníaca",
            "agonia perpétua", "tormento infinito", "maldição antiga", "pesadelo vívido"
        ],
        "acoes": [
            "devora almas", "rasga a carne", "invoca demônios", "amaldiçoa vidas", 
            "destrói mundos", "queima igrejas", "dilacera corpos", "espalha terror",
            "corrompe inocentes", "sacrifica virgens", "profana túmulos", "invoca o caos",
            "liberta monstros", "perfura corações", "derrama sangue", "extingue a luz"
        ],
        "elementos": [
            "sob luar sangrento", "entre chamas infernais", "no abismo profundo", "sob céu vermelho", 
            "entre ossos antigos", "no altar profano", "sob pentagrama", "entre sombras dançantes",
            "no vale da morte", "sob névoa pútrida", "entre ruínas malditas", "no portal dimensional",
            "sob eclipse eterno", "entre espíritos atormentados", "no reino das trevas", "sob tempestade demoníaca"
        ],
        "cenarios": [
            "cemitério abandonado", "catacumbas antigas", "floresta amaldiçoada", "templo profanado", 
            "cidade em ruínas", "campo de batalha", "inferno na terra", "dimensão demoníaca",
            "masmorra subterrânea", "altar de sacrifício", "montanha de crânios", "vale dos mortos",
            "mansão assombrada", "laboratório macabro", "abismo sem fim", "portal interdimensional"
        ],
        "personagens": [
            "demônio ancestral", "sacerdote profano", "guerreiro sangrento", "entidade cósmica", 
            "serial killer", "besta interior", "deus caído", "profeta do apocalipse",
            "ceifador de almas", "monstro abissal", "bruxa demoníaca", "carrasco impiedoso",
            "criatura mutante", "cientista louco", "espírito vingativo", "avatar da morte"
        ],
        "conflitos": [
            "batalha final", "guerra eterna", "confronto interno", "luta pela sobrevivência", 
            "resistência ao controle", "desafio aos deuses", "fuga do inferno", "busca por vingança",
            "pacto demoníaco", "ritual de sacrifício", "possessão espiritual", "transformação monstruosa",
            "queda na loucura", "despertar da besta", "julgamento divino", "apocalipse iminente"
        ],
        "emocoes": [
            "ódio visceral", "fúria incontrolável", "desespero absoluto", "terror paralisante", 
            "angústia sufocante", "loucura crescente", "paranoia constante", "obsessão doentia",
            "melancolia profunda", "resignação sombria", "êxtase sádico", "prazer na dor",
            "frieza calculista", "indiferença cruel", "fascinação mórbida", "repulsa existencial"
        ],
        "simbolos": [
            "sangue ritual", "crânio humano", "foice da morte", "chamas eternas", 
            "corvo negro", "pentagrama invertido", "serpente devoradora", "lua vermelha",
            "espada amaldiçoada", "livro proibido", "ampulheta vazia", "máscara demoníaca",
            "espelho quebrado", "rosa murcha", "correntes enferrujadas", "olho que tudo vê"
        ],
        "periodos_historicos": [
            "idade média", "inquisição", "guerras mundiais", "peste negra", 
            "queda de impérios", "era viking", "civilizações antigas", "apocalipse futuro",
            "era pós-apocalíptica", "tempos pré-históricos", "era industrial", "idade das trevas",
            "fim dos tempos", "era glacial", "colapso da civilização", "era dos deuses antigos"
        ],
        "temas_contemporaneos": [
            "colapso ambiental", "controle mental", "vigilância total", "manipulação genética", 
            "inteligência artificial", "guerra nuclear", "pandemia global", "experimentos humanos",
            "realidade virtual", "transumanismo", "conspiração global", "colapso social",
            "extinção em massa", "lavagem cerebral", "distopia tecnológica", "isolamento digital"
        ]
    },
    
    "Metal/Power Metal": {
        "nucleos": [
            "cavaleiro das estrelas", "dragão de ébano", "espada ancestral", "profecia celestial", 
            "reino perdido", "guardião do fogo eterno", "legião dos imortais", "chama da redenção",
            "guerreiro da luz", "portador da verdade", "herdeiro do trono", "protetor dos reinos",
            "campeão imortal", "senhor das tempestades", "caçador de dragões", "filho do trovão"
        ],
        "acoes": [
            "ergue o lábaro", "cruza o horizonte", "desafia o crepúsculo", "convoca os eleitos", 
            "domina as trevas", "ilumina o caminho", "vence a batalha final", "desperta o poder oculto",
            "empunha a espada", "cavalga através do fogo", "conquista reinos", "derrota o mal ancestral",
            "lidera exércitos", "forja alianças", "quebra maldições", "restaura a ordem"
        ],
        "elementos": [
            "sob a lua rubra", "entre relâmpagos cósmicos", "no altar dos deuses antigos", "pelas veredas do destino", 
            "no abismo do infinito", "sob o céu flamejante", "entre as montanhas sagradas", "no coração da tempestade",
            "sob as estrelas eternas", "entre portais dimensionais", "no vale dos heróis", "pelas terras místicas",
            "sob o sol dourado", "entre ruínas ancestrais", "no castelo nas nuvens", "pelas florestas encantadas"
        ],
        "cenarios": [
            "castelo nas nuvens", "campo de batalha épico", "floresta encantada", "montanha sagrada", 
            "cidade flutuante", "templo dos deuses", "vale dos dragões", "fortaleza inexpugnável",
            "reino subterrâneo", "ilha mística", "portal dimensional", "arena dos campeões",
            "palácio de cristal", "biblioteca arcana", "torre do mago", "santuário celestial"
        ],
        "personagens": [
            "rei guerreiro", "mago ancestral", "princesa guerreira", "oráculo divino", 
            "cavaleiro rúnico", "dragão sábio", "elfo imortal", "anão ferreiro",
            "paladino sagrado", "bardo profético", "guardião do tempo", "arqueiro élfico",
            "valquíria celestial", "lobo gigante", "grifo leal", "titã ancestral"
        ],
        "conflitos": [
            "batalha pelo reino", "busca pelo artefato", "resgate da princesa", "derrota do dragão", 
            "quebra da maldição", "restauração da ordem", "cumprimento da profecia", "retorno do rei",
            "união dos reinos", "defesa da fortaleza", "jornada ao desconhecido", "prova de valor",
            "confronto com o mal", "recuperação do trono", "proteção do inocente", "sacrifício heroico"
        ],
        "emocoes": [
            "coragem inabalável", "honra inquestionável", "glória eterna", "esperança renovada", 
            "determinação férrea", "lealdade absoluta", "fé inabalável", "orgulho nobre",
            "compaixão verdadeira", "amor eterno", "amizade forjada em batalha", "respeito mútuo",
            "admiração profunda", "gratidão sincera", "devoção completa", "confiança cega"
        ],
        "simbolos": [
            "espada lendária", "escudo mágico", "amuleto protetor", "coroa real", 
            "anel de poder", "armadura encantada", "estandarte do reino", "pergaminho antigo",
            "cálice sagrado", "cristal mágico", "árvore da vida", "chave dimensional",
            "cetro do poder", "manto celestial", "elmo do dragão", "medalhão profético"
        ],
        "periodos_historicos": [
            "era medieval", "tempos arthurianos", "era viking", "império romano", 
            "renascimento", "era dos descobrimentos", "cruzadas", "idade do bronze",
            "civilizações antigas", "era dos samurais", "tempos bíblicos", "era mitológica",
            "era dos cavaleiros", "idade de ouro", "era dos conquistadores", "tempos lendários"
        ],
        "temas_contemporaneos": [
            "jornada interior", "superação pessoal", "união na diversidade", "preservação da natureza", 
            "resistência pacífica", "sabedoria ancestral", "equilíbrio universal", "harmonia cósmica",
            "legado para o futuro", "conhecimento como poder", "tradição e modernidade", "identidade cultural",
            "cooperação global", "respeito às diferenças", "justiça verdadeira", "liberdade responsável"
        ]
    },
    
    "Punk/Hardcore": {
        "nucleos": [
            "rebelião urbana", "gritos de liberdade", "ruas em chamas", "sombras da opressão", 
            "protesto nas ruas", "revolução iminente", "caos organizado", "esperança na resistência",
            "juventude alienada", "sistema falido", "anarquia controlada", "voz dos oprimidos",
            "revolta popular", "colapso social", "contracultura viva", "movimento underground"
        ],
        "acoes": [
            "grita contra a injustiça", "desafia o sistema", "rompe as correntes", "constrói um novo amanhã", 
            "rompe as barreiras", "incendeia a opressão", "destrói as mentiras", "clama por igualdade",
            "levanta o punho", "ocupa as ruas", "questiona autoridades", "une os marginalizados",
            "confronta o poder", "expõe a hipocrisia", "recusa conformidade", "vive autenticamente"
        ],
        "elementos": [
            "sistema opressor", "corrupção governamental", "luta pela verdade", "opressão social", 
            "futuro incerto", "solidão na multidão", "esperança perdida", "gritos abafados",
            "ruas sujas", "becos escuros", "muros pichados", "sirenes distantes",
            "fábricas abandonadas", "subúrbios esquecidos", "centros urbanos", "escolas falidas"
        ],
        "cenarios": [
            "show underground", "manifestação de rua", "ocupação urbana", "fábrica abandonada", 
            "subúrbio decadente", "centro da cidade", "sala de aula opressiva", "delegacia de polícia",
            "casa de shows", "beco grafitado", "prédio ocupado", "estacionamento vazio",
            "skate park", "ponte abandonada", "estúdio improvisado", "porão sujo"
        ],
        "personagens": [
            "jovem rebelde", "ativista incansável", "punk de moicano", "anarquista convicto", 
            "trabalhador explorado", "estudante revolucionário", "artista marginal", "músico underground",
            "skatista urbano", "grafiteiro noturno", "fotógrafo de protestos", "poeta das ruas",
            "ex-presidiário", "sem-teto filosófico", "professor radical", "jornalista independente"
        ],
        "conflitos": [
            "luta contra o sistema", "resistência à opressão", "batalha pela autenticidade", "fuga da alienação", 
            "busca por liberdade", "confronto com autoridades", "rejeição de normas", "sobrevivência urbana",
            "dilema ético", "contradição interna", "pressão social", "repressão policial",
            "censura cultural", "manipulação midiática", "exploração econômica", "conformismo forçado"
        ],
        "emocoes": [
            "raiva justificada", "frustração intensa", "desprezo pelo sistema", "solidariedade genuína", 
            "desconfiança institucional", "esperança revolucionária", "alienação social", "indignação moral",
            "desespero existencial", "determinação inabalável", "ceticismo saudável", "empatia pelos oprimidos",
            "nojo da hipocrisia", "orgulho da autenticidade", "ansiedade constante", "satisfação na resistência"
        ],
        "simbolos": [
            "punho erguido", "símbolo anarquista", "moicano colorido", "botas militares", 
            "patches costurados", "bandeira rasgada", "correntes quebradas", "spray de grafite",
            "fanzine underground", "guitarra distorcida", "coquetel molotov", "câmera de vigilância",
            "distintivo policial", "máscara antigás", "crachá corporativo", "dinheiro queimando"
        ],
        "periodos_historicos": [
            "anos 70 e 80", "era Reagan/Thatcher", "guerra fria", "crise econômica", 
            "movimentos sociais", "contracultura", "era punk original", "pós-industrialismo",
            "maio de 68", "guerra do vietnã", "queda do muro", "revolução digital",
            "crise dos mísseis", "era nuclear", "revolução sexual", "movimento pelos direitos civis"
        ],
        "temas_contemporaneos": [
            "vigilância digital", "precarização do trabalho", "crise climática", "polarização política", 
            "fake news", "consumismo excessivo", "gentrificação urbana", "desigualdade crescente",
            "algoritmos de controle", "cultura do cancelamento", "capitalismo de plataforma", "crise habitacional",
            "dependência tecnológica", "fast fashion", "saúde mental", "individualismo tóxico"
        ]
    },
    
    "Shoegaze": {
        "nucleos": [
            "memórias vivas", "sonhos perdidos", "natureza efêmera", "silêncio profundo", 
            "ecos do passado", "visões distantes", "corações partidos", "neblina dos sentimentos",
            "reflexos distorcidos", "sussurros inaudíveis", "ondas de emoção", "véu translúcido",
            "fragmentos de memória", "paisagem interior", "conexão invisível", "presença ausente"
        ],
        "acoes": [
            "flutua em lágrimas", "desvanece em mente", "abraça-me forte", "perde a consciência", 
            "dança no vazio", "desaparece no horizonte", "sussurra ao vento", "cai em devaneios",
            "dissolve-se lentamente", "contempla o infinito", "afunda em pensamentos", "atravessa dimensões",
            "derrete-se em cores", "respira profundamente", "escapa da realidade", "mergulha em sensações"
        ],
        "elementos": [
            "eterno amor", "infinito ao voar", "transcendente em brilho", "etéreo em luz", 
            "sombras suaves", "luz difusa", "céu nebuloso", "mar de emoções",
            "névoa matinal", "chuva silenciosa", "reflexos na água", "raios filtrados",
            "ondas sonoras", "reverberação infinita", "eco distante", "distorção harmônica"
        ],
        "cenarios": [
            "praia deserta", "quarto iluminado", "rua sob neblina", "floresta ao amanhecer", 
            "cidade vazia", "janela embaçada", "campo de flores", "lago refletivo",
            "trem em movimento", "sala vazia", "corredor infinito", "escada em espiral",
            "jardim abandonado", "biblioteca silenciosa", "galeria de arte", "estúdio fotográfico"
        ],
        "personagens": [
            "amante distante", "poeta introspectivo", "sonhador eterno", "observador silencioso", 
            "artista solitário", "viajante perdido", "fantasma do passado", "estranho familiar",
            "fotógrafo de memórias", "dançarino invisível", "pintor de emoções", "colecionador de momentos",
            "guardião de segredos", "mensageiro onírico", "espírito errante", "amigo imaginário"
        ],
        "conflitos": [
            "separação inevitável", "conexão impossível", "memória versus realidade", "desejo inalcançável", 
            "passado persistente", "futuro incerto", "identidade fragmentada", "comunicação falha",
            "solidão na multidão", "beleza na tristeza", "despertar do sonho", "retorno indesejado",
            "perda da inocência", "busca por significado", "aceitação da efemeridade", "reconciliação interior"
        ],
        "emocoes": [
            "melancolia doce", "nostalgia profunda", "contemplação serena", "vulnerabilidade exposta", 
            "admiração silenciosa", "desejo contido", "tristeza bela", "alegria distante",
            "conforto na solidão", "aceitação pacífica", "anseio persistente", "esperança tímida",
            "resignação tranquila", "fascínio hipnótico", "confusão agradável", "paz inquieta"
        ],
        "simbolos": [
            "polaroid desbotada", "fita cassete", "flor prensada", "carta não enviada", 
            "espelho embaçado", "janela na chuva", "luz através de cortinas", "ondas de rádio",
            "câmera analógica", "disco de vinil", "diário antigo", "bilhete de trem",
            "colar guardado", "perfume familiar", "gravação em VHS", "telefone desconectado"
        ],
        "periodos_historicos": [
            "anos 80 e 90", "era pré-internet", "pós-punk", "fim da guerra fria", 
            "boom econômico", "era analógica", "cultura college rock", "cena indie britânica",
            "geração X", "era MTV", "movimento new wave", "pós-modernismo",
            "cultura zine", "cena de clubes", "movimento DIY", "era pré-celular"
        ],
        "temas_contemporaneos": [
            "desconexão digital", "autenticidade versus filtros", "nostalgia analógica", "slow living", 
            "mindfulness", "vulnerabilidade emocional", "intimidade genuína", "experiências sensoriais",
            "memória coletiva", "cultura lo-fi", "estética vintage", "simplicidade voluntária",
            "conexões humanas", "presença consciente", "valorização do momento", "beleza na imperfeição"
        ]
    },
    
    "Dream Rock": {
        "nucleos": [
            "mistério da noite", "tranquilidade ao luar", "reflexão silenciosa", "sonhos profundos", 
            "paisagens oníricas", "caminhos ocultos", "segredos do universo", "harmonia do infinito",
            "portal dimensional", "jardim secreto", "rio de estrelas", "templo interior",
            "caverna cristalina", "montanha etérea", "ilha flutuante", "floresta luminosa"
        ],
        "acoes": [
            "dança nas estrelas", "sussurra alto", "me abraça", "persegue meu ego", 
            "navega no desconhecido", "explora o infinito", "desvenda os segredos", "se perde no tempo",
            "flutua no éter", "atravessa dimensões", "tece sonhos", "dissolve fronteiras",
            "cria universos", "acende constelações", "desperta consciências", "transforma realidades"
        ],
        "elementos": [
            "luz em minha cor", "sombras escuras", "universo paralelo", "tempo perdido", 
            "brilho das galáxias", "vento do além", "aurora boreal", "silêncio do cosmos",
            "ondas etéreas", "poeira estelar", "névoa onírica", "cristais vibrantes",
            "portais dimensionais", "fractais infinitos", "espirais cósmicas", "geometria sagrada"
        ],
        "cenarios": [
            "praia sob luar", "deserto estrelado", "floresta encantada", "caverna de cristais", 
            "templo antigo", "jardim noturno", "lago refletivo", "montanha nebulosa",
            "ilha flutuante", "biblioteca infinita", "observatório abandonado", "teatro vazio",
            "casa de espelhos", "labirinto de luz", "torre de marfim", "vale dos sonhos"
        ],
        "personagens": [
            "viajante astral", "guardião dos sonhos", "oráculo silencioso", "artista cósmico", 
            "xamã urbano", "poeta das estrelas", "dançarino etéreo", "músico interdimensional",
            "alquimista da alma", "tecelão de realidades", "explorador do inconsciente", "mensageiro onírico",
            "colecionador de memórias", "arquiteto de sonhos", "navegador do tempo", "observador silencioso"
        ],
        "conflitos": [
            "realidade versus sonho", "despertar ou continuar", "memória versus imaginação", "tempo versus eternidade", 
            "luz versus sombra", "ordem versus caos", "individual versus universal", "material versus etéreo",
            "consciente versus inconsciente", "passado versus futuro", "ilusão versus verdade", "finito versus infinito",
            "forma versus essência", "razão versus intuição", "separação versus união", "ego versus totalidade"
        ],
        "emocoes": [
            "serenidade profunda", "admiração cósmica", "nostalgia inexplicável", "êxtase contemplativo", 
            "melancolia doce", "curiosidade infinita", "paz transcendental", "alegria silenciosa",
            "amor universal", "aceitação completa", "gratidão expansiva", "esperança luminosa",
            "compaixão abrangente", "fascínio hipnótico", "reverência sagrada", "pertencimento cósmico"
        ],
        "simbolos": [
            "lua cheia", "constelação", "cristal transparente", "espelho d'água", 
            "porta entreaberta", "chave antiga", "relógio parado", "bússola mágica",
            "mapa estelar", "livro em branco", "pena de escrever", "ampulheta flutuante",
            "lanterna acesa", "máscara teatral", "escada em espiral", "véu translúcido"
        ],
        "periodos_historicos": [
            "anos 80 e 90", "era psicodélica", "romantismo", "renascimento", 
            "era vitoriana", "belle époque", "idade de ouro", "era espacial",
            "antiguidade clássica", "era medieval", "período barroco", "modernismo",
            "era do jazz", "anos dourados", "era do cinema noir", "pós-modernismo"
        ],
        "temas_contemporaneos": [
            "consciência expandida", "realidade virtual", "estados alterados", "inteligência artificial", 
            "exploração espacial", "física quântica", "neurociência", "meditação mindfulness",
            "terapia psicodélica", "sonhos lúcidos", "biohacking", "sincronicidade",
            "conexão universal", "estados de flow", "experiências transcendentais", "design sensorial"
        ]
    },
    
    "Alternative Rock": {
        "nucleos": [
            "rebelião desenfreada", "protesto sem graça", "sociedade corrompida", "liberdade de escolhas", 
            "gritos abafados", "esperança quebrada", "caminhos tortuosos", "verdades ocultas",
            "alienação urbana", "desconforto existencial", "contradição interna", "identidade fragmentada",
            "desencanto moderno", "ansiedade coletiva", "isolamento social", "autenticidade perdida"
        ],
        "acoes": [
            "grita alto", "desafia o sistema", "rompe barreiras", "constrói pontes", 
            "questiona a realidade", "destrói ilusões", "enfrenta o caos", "procura redenção",
            "expõe mentiras", "abraça contradições", "rejeita rótulos", "transforma dor",
            "cria significado", "transcende limites", "confronta demônios", "celebra imperfeições"
        ],
        "elementos": [
            "sistema sitiado", "corrupção generalizada", "opressão controlada", "futuro sombrio", 
            "mentiras expostas", "cicatrizes do passado", "ecos da revolução", "sombras do presente",
            "muros invisíveis", "pontes quebradas", "janelas embaçadas", "portas trancadas",
            "ruas desertas", "céu poluído", "terra infértil", "água contaminada"
        ],
        "cenarios": [
            "cidade industrial", "subúrbio americano", "apartamento vazio", "estrada abandonada", 
            "bar na esquina", "escola decadente", "hospital psiquiátrico", "estúdio improvisado",
            "quarto adolescente", "escritório corporativo", "motel de beira de estrada", "estação de metrô",
            "shopping center", "parque de diversões", "estacionamento vazio", "sala de estar suburbana"
        ],
        "personagens": [
            "adolescente alienado", "artista torturado", "trabalhador desiludido", "rebelde sem causa", 
            "intelectual cínico", "viciado em recuperação", "veterano traumatizado", "professor idealista",
            "músico fracassado", "ativista cansado", "amante abandonado", "sonhador pragmático",
            "outsider observador", "crítico cultural", "viajante sem destino", "profeta ignorado"
        ],
        "conflitos": [
            "autenticidade versus sucesso", "individualidade versus conformidade", "arte versus comércio", "idealismo versus realidade", 
            "liberdade versus segurança", "conexão versus isolamento", "esperança versus cinismo", "amor versus independência",
            "talento versus reconhecimento", "integridade versus sobrevivência", "paixão versus apatia", "memória versus esquecimento",
            "verdade versus conforto", "mudança versus estabilidade", "significado versus vazio", "compromisso versus liberdade"
        ],
        "emocoes": [
            "desencanto lúcido", "raiva controlada", "melancolia reflexiva", "esperança relutante", 
            "alienação confortável", "ansiedade criativa", "tédio existencial", "nostalgia crítica",
            "vulnerabilidade corajosa", "frustração produtiva", "cinismo protetor", "empatia dolorosa",
            "resignação rebelde", "confusão inspiradora", "solidão conectada", "amor ambivalente"
        ],
        "simbolos": [
            "rádio quebrado", "televisão estática", "cigarro aceso", "garrafa vazia", 
            "guitarra desgastada", "caderno de anotações", "pôster rasgado", "fotografia desbotada",
            "carro abandonado", "telefone desconectado", "bilhete de suicídio", "pílulas prescritas",
            "tatuagem significativa", "roupas de brechó", "fita cassete", "câmera polaroid"
        ],
        "periodos_historicos": [
            "anos 80 e 90", "pós-guerra fria", "era grunge", "geração X", 
            "boom econômico", "era Clinton/Bush", "pós-modernismo", "era MTV",
            "revolução digital inicial", "cultura college rock", "movimento indie", "era pré-internet",
            "contracultura tardia", "era do CD", "cena underground", "cultura zine"
        ],
        "temas_contemporaneos": [
            "alienação digital", "ansiedade social", "crise de identidade", "cultura de celebridades", 
            "superficialidade midiática", "pressão por autenticidade", "nostalgia como escape", "burnout criativo",
            "saúde mental", "relacionamentos líquidos", "capitalismo tardio", "colapso de instituições",
            "hiperconectividade solitária", "cultura de cancelamento", "autoimagem versus realidade", "busca por significado"
        ]
    },
           
    "Post-Rock": {
        "nucleos": [
            "mistério do tempo", "tranquilidade duvidada", "reflexão às avessas", "sonhos loucos", 
            "paisagens infinitas", "caminhos esquecidos", "ecos do universo", "harmonia do caos",
            "vastidão contemplativa", "silêncio eloquente", "jornada interior", "horizontes expandidos",
            "profundidade oceânica", "altura vertiginosa", "ciclos eternos", "transformação constante"
        ],
        "acoes": [
            "dança pra mim", "sussurra devagar", "abraça meu ar", "persegue meu ser", 
            "caminha no vazio", "desvenda o silêncio", "se perde no infinito", "explora o desconhecido",
            "transcende limites", "constrói catedral sonora", "dissolve fronteiras", "eleva consciência",
            "navega profundezas", "escala montanhas", "atravessa desertos", "mergulha no abismo"
        ],
        "elementos": [
            "luz nas sombras", "silêncio ensurdecedor", "caos ordenado", "beleza desolada", 
            "horizonte distante", "oceano de som", "montanha de emoção", "deserto de pensamentos",
            "floresta de memórias", "rio de consciência", "céu de possibilidades", "abismo de contemplação",
            "névoa persistente", "tempestade silenciosa", "aurora eterna", "crepúsculo infinito"
        ],
        "cenarios": [
            "paisagem desolada", "montanha imponente", "oceano infinito", "floresta densa", 
            "deserto vasto", "cidade abandonada", "ruínas antigas", "espaço sideral",
            "caverna profunda", "ilha remota", "geleira derretendo", "vulcão adormecido",
            "cânion profundo", "planície sem fim", "céu estrelado", "tempestade distante"
        ],
        "personagens": [
            "viajante solitário", "observador silencioso", "explorador do desconhecido", "guardião da memória", 
            "testemunha do tempo", "navegador de emoções", "arquiteto de sons", "pintor de paisagens sonoras",
            "mensageiro sem palavras", "peregrino sem destino", "colecionador de momentos", "cartógrafo de territórios inexplorados",
            "geólogo emocional", "astrônomo interior", "oceanógrafo da consciência", "arqueólogo do silêncio"
        ],
        "conflitos": [
            "finitude versus infinito", "silêncio versus expressão", "indivíduo versus cosmos", "movimento versus estase", 
            "construção versus destruição", "ordem versus caos", "simplicidade versus complexidade", "presença versus ausência",
            "memória versus esquecimento", "permanência versus impermanência", "controle versus rendição", "forma versus abstração",
            "humano versus natural", "fragmento versus totalidade", "conhecido versus desconhecido", "palavra versus música"
        ],
        "emocoes": [
            "admiração cósmica", "melancolia transcendental", "esperança cautelosa", "resignação serena", 
            "nostalgia universal", "êxtase contemplativo", "tristeza bela", "alegria profunda",
            "solidão conectada", "paz inquieta", "temor reverencial", "aceitação expansiva",
            "curiosidade infinita", "gratidão silenciosa", "vulnerabilidade corajosa", "amor impessoal"
        ],
        "simbolos": [
            "horizonte infinito", "montanha distante", "onda quebrando", "árvore solitária", 
            "estrela cadente", "ruína antiga", "ponte abandonada", "caminho sinuoso",
            "farol na tempestade", "navio à deriva", "bússola quebrada", "mapa incompleto",
            "ampulheta eterna", "escada em espiral", "porta entreaberta", "janela para o infinito"
        ],
        "periodos_historicos": [
            "pós-modernidade", "virada do milênio", "era pós-industrial", "antropoceno", 
            "era espacial", "guerra fria", "período entre guerras", "era nuclear",
            "revolução digital", "era da informação", "globalização", "colapso soviético",
            "fim da história", "era da ansiedade", "pós-humanismo", "era da incerteza"
        ],
        "temas_contemporaneos": [
            "antropoceno", "colapso ambiental", "pós-humanismo", "solidão digital", 
            "sobrecarga informacional", "contemplação na era da pressa", "sublime tecnológico", "nostalgia do futuro",
            "memória coletiva", "identidade fragmentada", "espaços liminares", "não-lugares",
            "consciência ecológica", "tempo geológico", "escala cósmica", "pequenez humana"
        ]
    }
}

# Função para obter temas detalhados por gênero
def obter_temas_detalhados(genero, categoria=None):
    """
    Retorna temas detalhados para um gênero musical específico.
    
    Args:
        genero (str): O gênero musical.
        categoria (str, optional): Categoria temática específica (nucleos, acoes, elementos, etc).
        
    Returns:
        dict ou list: Dicionário com todas as categorias ou lista de temas da categoria especificada.
    """
    if genero not in TEMAS_DETALHADOS:
        return {}
    
    if categoria and categoria in TEMAS_DETALHADOS[genero]:
        return TEMAS_DETALHADOS[genero][categoria]
    
    return TEMAS_DETALHADOS[genero]

# Função para gerar combinação temática aleatória
def gerar_combinacao_tematica(genero, categorias=None):
    """
    Gera uma combinação temática aleatória para um gênero musical.
    
    Args:
        genero (str): O gênero musical.
        categorias (list, optional): Lista de categorias temáticas a incluir.
        
    Returns:
        dict: Dicionário com elementos temáticos selecionados aleatoriamente.
    """
    import random
    
    if genero not in TEMAS_DETALHADOS:
        return {}
    
    if not categorias:
        categorias = ["nucleos", "acoes", "elementos"]
    
    combinacao = {}
    
    for categoria in categorias:
        if categoria in TEMAS_DETALHADOS[genero]:
            combinacao[categoria] = random.choice(TEMAS_DETALHADOS[genero][categoria])
    
    return combinacao

# Função para gerar tema completo com contexto
def gerar_tema_completo(genero):
    """
    Gera um tema completo com múltiplos elementos e contexto para um gênero musical.
    
    Args:
        genero (str): O gênero musical.
        
    Returns:
        dict: Dicionário com tema completo incluindo múltiplos elementos temáticos.
    """
    import random
    
    if genero not in TEMAS_DETALHADOS:
        return {}
    
    tema = {}
    
    # Elementos principais
    categorias_principais = ["nucleos", "acoes", "elementos"]
    for categoria in categorias_principais:
        if categoria in TEMAS_DETALHADOS[genero]:
            tema[categoria] = random.choice(TEMAS_DETALHADOS[genero][categoria])
    
    # Elementos de contexto
    categorias_contexto = ["cenarios", "personagens", "conflitos"]
    for categoria in categorias_contexto:
        if categoria in TEMAS_DETALHADOS[genero]:
            tema[categoria] = random.choice(TEMAS_DETALHADOS[genero][categoria])
    
    # Elementos emocionais e simbólicos
    categorias_emocionais = ["emocoes", "simbolos"]
    for categoria in categorias_emocionais:
        if categoria in TEMAS_DETALHADOS[genero]:
            tema[categoria] = random.choice(TEMAS_DETALHADOS[genero][categoria])
    
    # Contexto histórico ou contemporâneo
    if random.choice([True, False]):
        if "periodos_historicos" in TEMAS_DETALHADOS[genero]:
            tema["contexto_temporal"] = random.choice(TEMAS_DETALHADOS[genero]["periodos_historicos"])
    else:
        if "temas_contemporaneos" in TEMAS_DETALHADOS[genero]:
            tema["contexto_temporal"] = random.choice(TEMAS_DETALHADOS[genero]["temas_contemporaneos"])
    
    return tema
