from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# validando as variáveis de ambiente
load_dotenv()

# inicializando o modelo
model = init_chat_model("groq:llama-3.3-70b-versatile")

# histórico de mensagens (começa com system message)
messages = [
    {
        "role": "system",
        "content": "Você é um assistente prestativo e amigável especializado em LangChain."
    }
]

# contador de interações
contador = 0

print("💬 Chat com LangChain v1.0")
print("Digite 'sair' para encerrar\n")

while True:
    # ler a entrada do usuário
    user_input = input("Você: ")

    # verificar se o usuário gostaria de sair do chat
    if user_input == "sair":
        print(f"\n👋 Conversa encerrada. Total de mensagens: {contador * 2}")  # (system e user)
        break

    # adicionar a mensagem do usuário ao histórico
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    ) 

    # invocar o modelo com todo o histórico
    response = model.invoke(messages)

    # adicionar a resposta do assistente ao histórico
    messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    # incrementar o contador de mensagens
    contador += 1

    # Mostrar resposta
    print(f"\n🤖 Assistente: {response.content}\n")
    print(f"📊 Mensagens trocadas: {contador}")
    print("-" * 50 + "\n")

# EXTRA: Mostrar histórico completo ao final
print("\n📜 Histórico completo da conversa:")
for i, msg in enumerate(messages[1:], 1):  # pula a system message
    role_emoji = "👤" if msg["role"] == "user" else "🤖"
    print(f"{i}. {role_emoji} {msg['role']}: {msg['content'][:50]}...")
