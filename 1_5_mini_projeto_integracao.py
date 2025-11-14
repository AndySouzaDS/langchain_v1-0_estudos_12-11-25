from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import time

# carregar api keys
load_dotenv()

# configurações personalizadas
PERSONALIDADES = {
    "1": {
        "nome": "Professor Paciente",
        "prompt": "Você é um professor paciente que explica conceitos de LangChain de forma didática, com exemplos e analogias."
    },
    "2": {
        "nome": "Dev Sênior",
        "prompt": "Você é um desenvolvedor sênior experiente. Respostas diretas, código limpo, sem enrolação."
    },
    "3": {
        "nome": "Documentação Viva",
        "prompt": "Você responde no estilo da documentação oficial: estruturado, com parâmetros, exemplos e links quando relevante."
    }
}

def setup_model():
    """Inicializa o modelo Groq"""
    return init_chat_model("groq:llama-3.3-70b-versatile")

def get_system_prompt(escolha):
    """Retorna o system prompt baseado na personalidade escolhida."""
    return {
        "role": "system",
        "content": PERSONALIDADES[escolha]["prompt"]
    }

def print_menu():
    """Mostra o menu de personalidades."""
    print("\n🎭 Escolha a personalidade do assistente:")
    for key, value in PERSONALIDADES.items():
        print(f"{key}. {value['nome']}")
    print()

def handle_command(comando, messages, stats):
    """Processa comandos especiais."""
    if comando == "/trocar":
        print_menu()  # mostrará novamente as opções de personalidades
        nova_escolha = input("Escolha (1-3): ")
        if nova_escolha in PERSONALIDADES:
            # substituição system message
            messages[0] = get_system_prompt(nova_escolha)
            print(f"✅ Personalidade trocada para: {PERSONALIDADES[nova_escolha]['nome']}\n")
        return True
    
    elif comando == "/historico":
        print("\n📜 Últimas 5 mensagens:")
        for msg in messages[-10:]:  # últimas 5 trocas (10 msgs)
            if msg["role"] != "system":
                role_emoji = "👤" if msg["role"] == "user" else "🤖"
                print(f"{role_emoji} {msg['content'][:80]}...")
        print()
        return True
    
    elif comando == "/limpar":
        # mantém apenas system message
        system_msg = messages[0]
        messages.clear()
        messages.append(system_msg)
        stats["mensagens"] = 0
        print("✅ Conversa resetada!\n")
        return True
    
    elif comando == "/sair":
        return False
    
    return True

def display_stats(stats, tempo_resposta):
    """Mostra estatísticas da conversa."""
    stats["tempo_total"] += tempo_resposta
    print(f"\n📊 Mensagens: {stats['mensagens']} | Tempo resposta: {tempo_resposta:.2f}s | Total: {stats['tempo_total']:.2f}s")
    print("-" * 70 + "\n")

def chat_loop():
    """Loop principal do chat."""
    # setup
    model = setup_model()

    # escolher personalidade inicial
    print("🚀 Assistente Técnico LangChain v1.0")
    print_menu()
    escolha = input("Escolha inicial (1-3): ")

    if escolha not in PERSONALIDADES:
        escolha = "1"

    # inicializar histórico com system prompt
    messages = [get_system_prompt(escolha)]
   
    # estatísticas
    stats = {"mensagens": 0, "tempo_total": 0}

    print(f"\n✅ Assistente ativo: {PERSONALIDADES[escolha]['nome']}")
    print("\nComandos: /trocar | /historico | /limpar | /sair\n")

    # loop principal
    while True:
        # input do usuário
        user_input = input("Você: ").strip()
    
        if not user_input:
            continue
        
        # verificar se é comando
        if user_input.startswith("/"):
            continuar = handle_command(user_input, messages, stats)
            if not continuar:
                print(f"\n👋 Encerrando. Total de mensagens: {stats['mensagens']}")
                break
            continue
        
        # adicionar mensagem do usuário
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
    
        # invocar modelo e medir tempo
        inicio = time.time()
        response = model.invoke(messages)
        tempo_resposta = time.time() - inicio
    
        # adicionar resposta ao histórico
        messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )
    
        # atualizar stats
        stats["mensagens"] += 1
    
        # mostrar resposta
        print(f"\n🤖 {PERSONALIDADES[escolha]['nome']}:")
        print(response.content)
    
        # mostrar stats
        display_stats(stats, tempo_resposta)

# executar
if __name__ == "__main__":
    chat_loop()
    
