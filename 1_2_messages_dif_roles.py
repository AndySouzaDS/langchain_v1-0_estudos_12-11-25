from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# configurando o llm
model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# messages com diferentes roles
messages = [
    # system: instrui o comportamento do llm
    {
        "role": "system",
        "content": "Você é um professor paciente que explica conceitos técnicos de forma simples."
    },
    # user: a pergunta do usuário
    {
        "role": "user",
        "content": "O que é um agent?"   
    },
    # assistant: resposta da ia
    {
        "role": "assistant",
        "content": "Um agent é um sistema que usa IA para tomar decisões."
    },
    # user: continuação da conversa
    {
        "role": "user",
        "content": "E o que são tools?"
    }

]

response = model.invoke(messages)
print(response.content)
