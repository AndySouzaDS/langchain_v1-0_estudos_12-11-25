from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# Configurar múltiplos providers
# IMPORTANTE: Você precisa ter as API Keys configuradas
providers = {
    "Groq Llama 3.3": "groq:llama-3.3-70b-versatile",
    "Groq Mixtral": "groq:llama-3.1-8b-instant"
}

# mesma pergunta para todos
messages = [
    {
        "role": "user",
        "content": "Explique LangChain em uma frase."
    }
]

print("🔬 Comparando respostas de diferentes modelos:\n")

# iterando o conjunto de providers
for name, model_string in providers.items():
    try:
        # inicializar o modelo
        model = init_chat_model(model_string)

        # invocar o modelo
        response = model.invoke(messages)

        # mostrar resultado
        print(f"📍 {name}")
        print(f"    Resposta: {response.content}")
        print(f"    Tokens: {response.response_metadata.get('token_usage', 'N/A')}")
        print()

    except Exception as e:
        print(f"{name}: {str(e)}\n")

# Análise: Podemos observar como diferentes modelos respondem de forma diferente, más o CÓDIGO é idêntico! Apenas a string do modelo muda (string notation).

# Output:
# 🔬 Comparando respostas de diferentes modelos:

# 📍 Groq Llama 3.3
#     Resposta: LangChain é uma biblioteca de código aberto que permite aos desenvolvedores criar aplicativos de inteligência artificial (IA) baseados em linguagem natural, utilizando modelos de linguagem como o LLaMA e outros, para construir chatbots, assistentes virtuais e outros tipos de aplicações de processamento de linguagem natural.
#     Tokens: {'completion_tokens': 72, 'prompt_tokens': 43, 'total_tokens': 115, 'completion_time': 0.217275513, 'prompt_time': 0.00288009, 'queue_time': 0.149114918, 'total_time': 0.220155603}

# 📍 Groq Mixtral
#     Resposta: LangChain é uma biblioteca de código aberto que permite criar modelos de linguagem para aplicativos de negócio e de produto, utilizando técnicas de aprendizado de máquina e de processamento de linguagem natural.
#     Tokens: {'completion_tokens': 47, 'prompt_tokens': 43, 'total_tokens': 90, 'completion_time': 0.075632186, 'prompt_time': 0.002021624, 'queue_time': 0.147855835, 'total_time': 0.07765381}
