from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# TODO: Carregar variáveis de ambiente
load_dotenv()

# TODO: Inicializar o modelo Groq
model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# TODO: Criar uma lista de mensagens com role "user"
messages = [
    # system: contexto para o sistema
    {
        "role": "system",
        "content": "Você é um excelente professor de conteúdo de IA, explica tudo com simplicidade e objetividade."
    },
    # user: dúvida técnica
    # Pergunta sugerida: "O que é o LangChain em 2 frases?"
    {
        "role": "user",
        "content": "O que é Lanchain em 2 frases?"
    }

]

# TODO: Invocar o modelo e imprimir a resposta
response = model.invoke(messages)
print(response.content)
