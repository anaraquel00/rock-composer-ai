# 🎸 Rock Composer AI 
**Gerador de letras de rock alimentado por IA**  

[![Open in Hugging Face](https://img.shields.io/badge/🤗_Open_in_Spaces-FFD700?logo=huggingface)](https://huggingface.co/spaces/ana99/rock-composer-ai)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🌟 Visão Geral
Projeto que combina:
- Modelos de linguagem (GPT-2 fine-tuned)
- Engenharia de prompts musical
- Regras estilísticas baseadas em rock alternativo/grunge

🔗 **Demo online:** [Acesse o Space](https://huggingface.co/spaces/ana99/rock-composer-ai)

---

## 🛠️ Tecnologias
```mermaid
flowchart TB
    A[Python] --> B[Gradio]
    A --> C[Transformers]
    D[Prompts estruturados] --> E[Letras personalizadas]
```    


# 📦 Estrutura do Projeto

```bash
rock-composer-ai/
├── src/              # Código-fonte
│   ├── app.py
│   ├── dicionario_rimas.py
│   ├── instrucoes_estilisticas.py
│   └── temas_detalhados.py
├── docs/             # Documentação
│   ├── setup.md
│   └── prompt-guide.md
├── assets/           # Mídias
└── requirements.txt  # Dependências
```

# 🚀 Começando

```bash
git clone https://huggingface.co/spaces/ana99/rock-composer-ai
cd rock-composer-ai
pip install -r requirements.txt
python src/app.py
```
# 📚 Documentação Técnica

Fluxo de Geração

```mermaid
sequenceDiagram
    Usuário->>+app.py: Envia prompt JSON
    app.py->>+dicionario_rimas.py: Solicita padrão de rima
    app.py->>+temas_detalhados.py: Busca temas relacionados
    app.py-->>-Usuário: Retorna letra completa
```    
Arquivos Principais

Arquivo	Função
app.py	Interface Gradio e lógica principal
dicionario_rimas.py	Gerencia padrões ABAB, AABB, etc.
temas_detalhados.py	Banco de temas pré-definidos

# 🎨 Guia de Prompts

Exemplo mínimo:
```json
{
  "tema": "revolta",
  "estilo": "grunge",
  "estrutura": "verso-refrão"
}
```
Dicas:

Use contrastes ("doce amargura")

Inclua verbos de ação ("esmagar", "gritar")

Referencie objetos concretos ("garrafa quebrada")

# ⚖️ Direitos Autorais

Letras geradas são de domínio público

Atribua o projeto se usar comercialmente

# 🤝 Como Contribuir

Faça um fork do projeto

Crie uma branch (git checkout -b feature/novo-recurso)

Commit suas mudanças (git commit -m 'Add novo recurso')

Push para a branch (git push origin feature/novo-recurso)

Abra um Pull Request

# 📬 Contato

Ana Raquel - @anaraquel00
Projeto no Hugging Face: Rock Composer AI