# 📝 EXERCÍCIO GUIADO
# Objetivo: Criar uma função que permite trocar de modelo dinamicamente durante uma conversa, mantendo o histórico.
## Passo 1: Estrutura básica
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# Passo 2: Criar um dicionário com 3 modelos disponíveis
MODELOS_DISPONIVEIS = {
    "1": {
        "nome": "Qwen3-32b (Groq)", 
        "string": "groq:qwen/qwen3-32b"
    },
    "2": {
        "nome": "Llama-3.1-8b (Groq)",
        "string": "groq:llama-3.1-8b-instant"
    },
    "3": {
        "nome": "Llama-3.3-70b (Groq)",
        "string": "groq:llama-3.3-70b-versatile"
    }
}

# Passo 3: Criar função que inicializa modelo baseado em escolha
def get_model(escolha):
    # configurar um modelo default
    if escolha not in MODELOS_DISPONIVEIS:
        escolha == "1"  

    modelo_string = MODELOS_DISPONIVEIS[escolha]["string"]
    return init_chat_model(modelo_string), escolha

# Passo 4: Implementar função de troca de modelo
def trocar_modelo():
    """Mostra menu e retorna novo modelo"""
    print("\n🔄 Escolha um modelo:")
    # 4.1. listar modelos do dicionário MODELOS_DISPONIVEIS
    for key, value in MODELOS_DISPONIVEIS.items():
        print(f" {key}. {value['nome']}")

    # 4.2. ler a escolha do usuário
    escolha = input("\nEscolha (1-3): ").strip()

    # 4.3. validar a escolha
    if escolha in MODELOS_DISPONIVEIS:
        # 4.4. Inicializar novo modelo
        model, escolha = get_model(escolha)
        print(f"✅ Trocado para: {MODELOS_DISPONIVEIS[escolha]['nome']}\n")
        # 4.5. Retornar a escolha e o novo modelo inicializado
        return model, escolha
    else:
        print("❌ Escolha inválida. Mantendo o modelo atual.\n")
        return None, None
    
# Passo 5: Loop com histórico persistente
def chat_com_troca():
    """Chat principal com suporte a troca de modelo"""
    
    print("💬 Chat Multi-Mod# 5.1. Mensagens de direcionamentoelo Langchain v1.0")
    print("Comandos: /trocar | /sair\n")

    # 5.2. Inicializar o modelo padrão
    model, escolha_atual = get_model("1")
    # 5.3. Mensagens de direcionamento
    print(f"Modelo ativo: {MODELOS_DISPONIVEIS[escolha_atual]['nome']}\n")

    # 5.4. Histórico (compartilhado entre modelos!)
    messages = []

    # 5.5. loop troca de modelos
    while True:
        # Input usuário
        user_input = input("Você: ").strip()

        # Opção de manter modelo
        if not user_input:
            continue

        # Opção de sair
        if user_input == "/sair":
            print("\n👋 Até logo!")
            break

        # Comando de troca de modelo
        if user_input == "/trocar":
            novo_model, nova_escolha = trocar_modelo()
            if novo_model:
                model = novo_model
                escolha_atual = nova_escolha
            continue
        
        # Adicionar mensagem do usuário
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Invocar modelo ATUAL com histórico COMPLETO
        response = model.invoke(messages)

        # Adicionar resposta ao histórico
        messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

        # Mostrar informações do modelo e conteúdo da resposta
        print(f"\n🤖 [{MODELOS_DISPONIVEIS[escolha_atual]['nome']}]:")
        print(response.content)
        print()

# Passo 6: Executar
if __name__ == "__main__":
    chat_com_troca()
