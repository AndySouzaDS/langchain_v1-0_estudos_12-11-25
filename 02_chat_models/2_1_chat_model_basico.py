from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# init_chat_model() - A interface unificada da v1.0
# Formato> "provider:model-name"
# Provider poder: openai, anthropic, groq, google, cohere, etc.

model = init_chat_model("groq:llama-3.3-70b-versatile")

# Messages: sempre uma lista de dicionários
# Cada dict TEM QUE TER 'role' e 'content'
messages = [
    {
        "role": "user",
        "content": "Qual a capital da França?"
    }
]

# invoke() - faz a requisição e espera resposta completa
response = model.invoke(messages)

# responde - é um objeto AIMessage (não dict!)
print(f"Tipo: {type(response)}")                  # <class 'langchain_core.message.ai.AIMessage>
print(f"Role: {response.type}")                   # 'ai' (equivalente a 'assistant')
print(f"Conteúdo: {response.content}")            # "A capital da França é Paris."

# Acessar apenas o texto da resposta:
print(response.content)

# response também tem outros atributos úteis:
print(f"ID: {response.id}")                       # ID único da mensagem
print(f"Metadata: {response.response_metadata}")  # Informações do provider


# Tipo: <class 'langchain_core.messages.ai.AIMessage'>
# Role: ai
# Conteúdo: A capital da França é Paris.
# A capital da França é Paris.
# ID: lc_run--99f4bb64-78ef-4631-8bd2-fe3406336a79-0
# Metadata: {'token_usage': {'completion_tokens': 9, 'prompt_tokens': 42, 'total_tokens': 51, 'completion_time': 0.012176637, 'prompt_time': 0.00114907, 'queue_time': 0.152740037, 'total_time': 0.013325707}, 'model_name': 'llama-3.3-70b-versatile', 'system_fingerprint': 'fp_767ba3debd', 'service_tier': 'on_demand', 'finish_reason': 'stop', 'logprobs': None, 'model_provider': 'groq'}