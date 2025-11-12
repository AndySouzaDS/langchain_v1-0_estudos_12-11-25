# 🚀 Estudos LangChain v1.0

Repositório de estudos e projetos práticos com LangChain v1.0

## 📚 Estrutura do Projeto

```
langchain-v1-estudos/
├── topico_01_fundamentos/      # Instalação, setup, conceitos básicos
├── topico_02_chat_models/       # init_chat_model, messages, roles
├── topico_03_tools_basicas/     # TavilySearch e tools built-in
├── topico_04_tools_customizadas/# Criar tools com @tool decorator
├── topico_05_primeiro_agent/    # create_react_agent
├── projetos_integrados/         # Mini-projetos completos
├── notas_estudo/                # Anotações e resumos
├── venv/                        # Ambiente virtual (não commitado)
├── .env                         # API keys (não commitado)
├── .gitignore                   # Arquivos ignorados pelo git
└── requirements.txt             # Dependências Python
```

## 🔧 Setup Inicial

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/langchain-v1-estudos.git
cd langchain-v1-estudos
```

### 2. Criar ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar API keys
Copie `.env.example` para `.env` e adicione suas chaves:
```bash
cp .env.example .env
nano .env  # Edite e adicione suas keys
```

### 5. Obter API Keys

- **Groq** (Gratuito): https://console.groq.com
- **Tavily** (Gratuito): https://tavily.com
- **OpenAI** (Pago): https://platform.openai.com
- **Anthropic** (Pago): https://console.anthropic.com

## 🎯 Roadmap de Estudos

### 🟢 Básico (Tópicos 1-8)
- [x] Fundamentos
- [x] Chat Models
- [ ] Tools Básicas
- [ ] Tools Customizadas
- [ ] Primeiro Agent
- [ ] Executando Agents
- [ ] Streaming
- [ ] Memória Básica

### 🟡 Intermediário (Tópicos 9-20)
- [ ] create_agent v1.0
- [ ] Middleware
- [ ] Structured Output
- [ ] ...

### 🔴 Avançado (Tópicos 21-33)
- [ ] Custom Middleware
- [ ] LangGraph
- [ ] Multi-Agent Systems
- [ ] ...

## 🧪 Testando Instalação

```python
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model("groq:llama-3.3-70b-versatile")
response = model.invoke([{"role": "user", "content": "Olá!"}])
print(response.content)
```

## 📖 Recursos

- [LangChain Docs](https://docs.langchain.com)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Groq Console](https://console.groq.com)

## 🤝 Contribuindo

Este é um repositório pessoal de estudos, mas sugestões são bem-vindas!

## 📝 Licença

MIT License - Livre para usar e modificar
# langchain_v1-0_estudos_12-11-25
