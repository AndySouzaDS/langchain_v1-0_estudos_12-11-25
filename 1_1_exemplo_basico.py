# configurações de API Keys
import os
from dotenv import load_dotenv

load_dotenv()

# primeira interação
from langchain.chat_models import init_chat_model

# inicialização do modelo (string notation é novo na v1.0!)
model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# criando uma mensagem simples
messages = [
    {"role": "user", "content": "Explique o que são agents em uma frase."}
]

# invocar o modelo
response = model.invoke(messages)

# visualizando a resposta
print(response.content)

