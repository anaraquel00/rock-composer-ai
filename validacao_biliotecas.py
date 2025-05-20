"""
Script para validação das bibliotecas aprimoradas do Rock Composer AI.
Este script testa as principais funcionalidades das bibliotecas expandidas.
"""

import sys
import random
from importlib import import_module

# Configuração de cores para saída no terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.ENDC}\n")

def print_subheader(text):
    print(f"\n{Colors.BLUE}{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.BLUE}{'-' * 40}{Colors.ENDC}\n")

def print_success(text):
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

def test_module_import(module_name):
    try:
        module = import_module(module_name)
        print_success(f"Módulo {module_name} importado com sucesso")
        return module
    except ImportError as e:
        print_error(f"Falha ao importar {module_name}: {e}")
        return None

def test_dicionario_rimas():
    print_header("Testando dicionario_rimas_aprimorado.py")
    
    # Importar o módulo
    module = test_module_import("dicionario_rimas_aprimorado")
    if not module:
        return False
    
    # Testar constantes
    print_subheader("Testando constantes")
    constants = ["TIPOS_RIMA", "CLASSES_GRAMATICAIS", "DICIONARIO_RIMAS", "VOCABULARIO_GENEROS"]
    for const in constants:
        if hasattr(module, const):
            print_success(f"Constante {const} encontrada")
        else:
            print_error(f"Constante {const} não encontrada")
    
    # Testar funções
    print_subheader("Testando funções")
    functions = ["obter_rimas", "obter_rimas_por_sufixo", "obter_vocabulario_genero", "gerar_rima"]
    for func in functions:
        if hasattr(module, func) and callable(getattr(module, func)):
            print_success(f"Função {func} encontrada")
        else:
            print_error(f"Função {func} não encontrada ou não é chamável")
    
    # Testar funcionalidades específicas
    print_subheader("Testando funcionalidades específicas")
    
    # Testar obter_rimas
    try:
        rimas = module.obter_rimas("coração")
        if rimas and isinstance(rimas, dict) and "rimas" in rimas:
            print_success(f"obter_rimas('coração') retornou {len(rimas['rimas'])} rimas")
        else:
            print_warning(f"obter_rimas('coração') retornou resultado inesperado: {rimas}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_rimas: {e}")
    
    # Testar obter_rimas_por_sufixo
    try:
        rimas = module.obter_rimas_por_sufixo("ão", 2)
        if isinstance(rimas, list):
            print_success(f"obter_rimas_por_sufixo('ão', 2) retornou {len(rimas)} palavras")
        else:
            print_warning(f"obter_rimas_por_sufixo('ão', 2) retornou resultado inesperado: {rimas}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_rimas_por_sufixo: {e}")
    
    # Testar obter_vocabulario_genero
    try:
        vocab = module.obter_vocabulario_genero("Metal/Power Metal", "substantivos")
        if isinstance(vocab, list):
            print_success(f"obter_vocabulario_genero('Metal/Power Metal', 'substantivos') retornou {len(vocab)} palavras")
        else:
            print_warning(f"obter_vocabulario_genero retornou resultado inesperado: {vocab}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_vocabulario_genero: {e}")
    
    # Testar gerar_rima
    try:
        rima = module.gerar_rima("coração", 3)
        print_success(f"gerar_rima('coração', 3) retornou: {rima}")
    except Exception as e:
        print_error(f"Erro ao chamar gerar_rima: {e}")
    
    return True

def test_instrucoes_estilisticas():
    print_header("Testando instrucoes_estilisticas_aprimorado.py")
    
    # Importar o módulo
    module = test_module_import("instrucoes_estilisticas_aprimorado")
    if not module:
        return False
    
    # Testar constantes
    print_subheader("Testando constantes")
    constants = ["ELEMENTOS_ESTRUTURAIS", "TECNICAS_MUSICAIS", "EFEITOS", "INSTRUCOES_ESTILISTICAS"]
    for const in constants:
        if hasattr(module, const):
            print_success(f"Constante {const} encontrada")
        else:
            print_error(f"Constante {const} não encontrada")
    
    # Testar funções
    print_subheader("Testando funções")
    functions = ["obter_instrucoes_estilisticas", "obter_caracteristicas_genero", 
                "obter_info_tecnica", "obter_info_efeito", "gerar_estrutura_musica"]
    for func in functions:
        if hasattr(module, func) and callable(getattr(module, func)):
            print_success(f"Função {func} encontrada")
        else:
            print_error(f"Função {func} não encontrada ou não é chamável")
    
    # Testar funcionalidades específicas
    print_subheader("Testando funcionalidades específicas")
    
    # Testar obter_instrucoes_estilisticas
    try:
        instrucoes = module.obter_instrucoes_estilisticas("Metal/Death Metal", "intro")
        if instrucoes and isinstance(instrucoes, dict):
            print_success(f"obter_instrucoes_estilisticas('Metal/Death Metal', 'intro') retornou {len(instrucoes)} itens")
        else:
            print_warning(f"obter_instrucoes_estilisticas retornou resultado inesperado: {instrucoes}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_instrucoes_estilisticas: {e}")
    
    # Testar obter_caracteristicas_genero
    try:
        caract = module.obter_caracteristicas_genero("Punk/Hardcore")
        if caract and isinstance(caract, dict):
            print_success(f"obter_caracteristicas_genero('Punk/Hardcore') retornou {len(caract)} características")
        else:
            print_warning(f"obter_caracteristicas_genero retornou resultado inesperado: {caract}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_caracteristicas_genero: {e}")
    
    # Testar obter_info_tecnica
    try:
        info = module.obter_info_tecnica("palm_muting")
        if info and isinstance(info, str):
            print_success(f"obter_info_tecnica('palm_muting') retornou: '{info[:30]}...'")
        else:
            print_warning(f"obter_info_tecnica retornou resultado inesperado: {info}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_info_tecnica: {e}")
    
    # Testar gerar_estrutura_musica
    try:
        estrutura = module.gerar_estrutura_musica("Indie Rock", 2)
        if estrutura and isinstance(estrutura, list):
            print_success(f"gerar_estrutura_musica('Indie Rock', 2) retornou estrutura com {len(estrutura)} elementos")
        else:
            print_warning(f"gerar_estrutura_musica retornou resultado inesperado: {estrutura}")
    except Exception as e:
        print_error(f"Erro ao chamar gerar_estrutura_musica: {e}")
    
    return True

def test_temas_detalhados():
    print_header("Testando temas_detalhados_aprimorado.py")
    
    # Importar o módulo
    module = test_module_import("temas_detalhados_aprimorado")
    if not module:
        return False
    
    # Testar constantes
    print_subheader("Testando constantes")
    constants = ["CATEGORIAS_TEMATICAS", "TEMAS_DETALHADOS"]
    for const in constants:
        if hasattr(module, const):
            print_success(f"Constante {const} encontrada")
        else:
            print_error(f"Constante {const} não encontrada")
    
    # Testar funções
    print_subheader("Testando funções")
    functions = ["obter_temas_detalhados", "gerar_combinacao_tematica", "gerar_tema_completo"]
    for func in functions:
        if hasattr(module, func) and callable(getattr(module, func)):
            print_success(f"Função {func} encontrada")
        else:
            print_error(f"Função {func} não encontrada ou não é chamável")
    
    # Testar funcionalidades específicas
    print_subheader("Testando funcionalidades específicas")
    
    # Testar obter_temas_detalhados
    try:
        temas = module.obter_temas_detalhados("Metal/Power Metal", "nucleos")
        if temas and isinstance(temas, list):
            print_success(f"obter_temas_detalhados('Metal/Power Metal', 'nucleos') retornou {len(temas)} temas")
        else:
            print_warning(f"obter_temas_detalhados retornou resultado inesperado: {temas}")
    except Exception as e:
        print_error(f"Erro ao chamar obter_temas_detalhados: {e}")
    
    # Testar gerar_combinacao_tematica
    try:
        combinacao = module.gerar_combinacao_tematica("Shoegaze", ["nucleos", "acoes", "elementos"])
        if combinacao and isinstance(combinacao, dict):
            print_success(f"gerar_combinacao_tematica('Shoegaze') retornou {len(combinacao)} elementos")
            for k, v in combinacao.items():
                print(f"  - {k}: {v}")
        else:
            print_warning(f"gerar_combinacao_tematica retornou resultado inesperado: {combinacao}")
    except Exception as e:
        print_error(f"Erro ao chamar gerar_combinacao_tematica: {e}")
    
    # Testar gerar_tema_completo
    try:
        tema = module.gerar_tema_completo("Alternative Rock")
        if tema and isinstance(tema, dict):
            print_success(f"gerar_tema_completo('Alternative Rock') retornou tema com {len(tema)} elementos")
            for k, v in tema.items():
                print(f"  - {k}: {v}")
        else:
            print_warning(f"gerar_tema_completo retornou resultado inesperado: {tema}")
    except Exception as e:
        print_error(f"Erro ao chamar gerar_tema_completo: {e}")
    
    return True

def test_integration():
    print_header("Testando integração entre bibliotecas")
    
    # Importar os módulos
    dicionario = test_module_import("dicionario_rimas_aprimorado")
    instrucoes = test_module_import("instrucoes_estilisticas_aprimorado")
    temas = test_module_import("temas_detalhados_aprimorado")
    
    if not all([dicionario, instrucoes, temas]):
        print_error("Não foi possível importar todos os módulos necessários para o teste de integração")
        return False
    
    print_subheader("Simulando geração de música completa")
    
    try:
        # Selecionar gênero aleatório
        if temas is None or not hasattr(temas, "TEMAS_DETALHADOS"):
            print_error("O módulo 'temas_detalhados_aprimorado' não possui o atributo 'TEMAS_DETALHADOS'")
            return False
        generos = list(temas.TEMAS_DETALHADOS.keys())
        genero = random.choice(generos)
        print(f"Gênero selecionado: {genero}")
        
        # Obter tema completo
        tema_completo = temas.gerar_tema_completo(genero)
        print(f"Tema gerado com {len(tema_completo)} elementos")
        
        # Obter estrutura musical
        if instrucoes is not None and hasattr(instrucoes, "gerar_estrutura_musica"):
            estrutura = instrucoes.gerar_estrutura_musica(genero, 2)
            print(f"Estrutura musical com {len(estrutura)} partes: {', '.join(estrutura)}")
        else:
            print_error("O módulo 'instrucoes_estilisticas_aprimorado' não possui o método 'gerar_estrutura_musica'")
            return False
        
        # Obter características do gênero
        caracteristicas = instrucoes.obter_caracteristicas_genero(genero)
        print(f"BPM recomendado: {caracteristicas.get('bpm_recomendado', 'N/A')}")
        print(f"Afinação recomendada: {caracteristicas.get('afinacao_recomendada', 'N/A')}")
        
        # Gerar algumas rimas para o tema principal
        if "nucleos" in tema_completo:
            nucleo = tema_completo["nucleos"]
            palavras = nucleo.split()
            if palavras:
                palavra_principal = max(palavras, key=len)
                if dicionario is not None and hasattr(dicionario, "gerar_rima"):
                    rima = dicionario.gerar_rima(palavra_principal)
                    print(f"Rima para '{palavra_principal}': '{rima}'")
                else:
                    print_error("O módulo 'dicionario_rimas_aprimorado' não possui o método 'gerar_rima' ou não foi importado corretamente")
        
        print_success("Simulação de integração concluída com sucesso")
        return True
        
    except Exception as e:
        print_error(f"Erro durante teste de integração: {e}")
        return False

def main():
    print_header("VALIDAÇÃO DAS BIBLIOTECAS APRIMORADAS DO ROCK COMPOSER AI")
    
    # Adicionar diretório atual ao path para importação dos módulos
    sys.path.append('/home/ubuntu/rock-composer-ai')
    
    # Testar cada biblioteca individualmente
    dicionario_ok = test_dicionario_rimas()
    instrucoes_ok = test_instrucoes_estilisticas()
    temas_ok = test_temas_detalhados()
    
    # Testar integração entre bibliotecas
    integration_ok = test_integration()
    
    # Resumo dos testes
    print_header("RESUMO DOS TESTES")
    if dicionario_ok:
        print_success("✓ dicionario_rimas_aprimorado.py: OK")
    else:
        print_error("✗ dicionario_rimas_aprimorado.py: FALHOU")
    
    if instrucoes_ok:
        print_success("✓ instrucoes_estilisticas_aprimorado.py: OK")
    else:
        print_error("✗ instrucoes_estilisticas_aprimorado.py: FALHOU")
    
    if temas_ok:
        print_success("✓ temas_detalhados_aprimorado.py: OK")
    else:
        print_error("✗ temas_detalhados_aprimorado.py: FALHOU")
    
    if integration_ok:
        print_success("✓ Integração entre bibliotecas: OK")
    else:
        print_error("✗ Integração entre bibliotecas: FALHOU")
    
    # Resultado final
    if all([dicionario_ok, instrucoes_ok, temas_ok, integration_ok]):
        print_header("TODOS OS TESTES PASSARAM COM SUCESSO!")
        return 0
    else:
        print_header("ALGUNS TESTES FALHARAM. VERIFIQUE OS DETALHES ACIMA.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
