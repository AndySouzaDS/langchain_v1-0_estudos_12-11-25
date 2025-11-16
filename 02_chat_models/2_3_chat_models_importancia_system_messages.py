from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("groq:llama-3.3-70b-versatile")

# Teste 1: SEM System Message
messages_sem_system = [
    {
        "role": "user",
        "content": "Explique o que é RAG, no contexto de IA Generativa em uma frase."
    }
]

response1 = model.invoke(messages_sem_system)
print("💬 SEM system message:")
print(response1.content)
print("\n" + "="*50 + "\n")

# Teste 2: COM System Message definindo a personalidade
messages_com_system = [
    {
        "role": "system",
        "content": "Você é um professor especialista, em criar analogias simples para leigos compreenderem conceitos técnicos sobre IA Generativa."
    },
    {
        "role": "user",
        "content": "Explique o que é RAG, no contexto de IA Generativa em uma frase."
    }
]

response2 = model.invoke(messages_com_system)
print("👨🏿‍🏫 COM system message (professor):")
print(response2.content)
print("\n" + "="*50 + "\n")

# Teste 3: System Messages para formato estruturado
messages_estruturado = [
    {
        "role": "system",
        "content": "Responda SEMPRE no formato: RESPOSTA: [sua resposta] | CONFIANÇA: [baixa/média/alta]"
    },
    {
        "role": "user",
        "content": "Explique o que é RAG, no contexto de IA Generativa em uma frase."
    }
]

response3 = model.invoke(messages_estruturado)
print("📋 COM system message (formato estruturado):")
print(response3.content)

# LIÇÃO: System Message é PODEROSO para controlar comportamento!

# ........................................................................................

# Output:
# 💬 SEM system message:
# RAG (Retrieval-Augmented Generation) é uma técnica de IA generativa que combina modelos de recuperação de informações com modelos de geração de texto para produzir respostas mais precisas e informadas.

# ==================================================

# 👨🏿‍🏫 COM system message (professor):
# O RAG (Retrieval-Augmented Generation) é como um bibliotecário inteligente que, ao gerar texto, procura em uma vasta biblioteca de informações para encontrar fatos e dados relevantes e, em seguida, os combina de forma criativa para produzir respostas mais precisas e informadas.

# ==================================================

# 📋 COM system message (formato estruturado):
# RESPOSTA: RAG (Retrieval-Augmented Generation) é uma abordagem de IA generativa que combina a recuperação de informações de uma base de conhecimento com a geração de texto, permitindo que os modelos produzam respostas mais precisas e informadas. | CONFIANÇA: Alta