from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Passo 1: Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Passo 2: Inicializar modelo usando string notation (novidade v1.0!)
# *** Nota: essa notação do llm também funciona: "groq:llama-3.3-70b-versatile"
model = init_chat_model("groq:llama-3.3-70b-versatile")

# Passo 3: Criar mensagens
# Messages é sempre uma lista de dicionários
messages = [
    {
        "role": "user",  # role: é quem está falando (user, assistant, system)
        "content": "O que é LangChain em 2 frases?"  # content: o que está sendo dito
    }
]

# Passo 4: Invocar modelo (fazer a requisição)
response = model.invoke(messages)

# Passo 5: Exibir resposta
print("🤖 Resposta do LLM:")
print(response.content)

# Passo 6 (EXTRA): Ver estrutura completa da resposta
print("\n📊 Estrutura completa:")
print(f"Tipo: {type(response)}")
print(f"Role: {response.type}")  # Será 'ai' (assistant)
print(f"Conteúdo: {response.content}")
