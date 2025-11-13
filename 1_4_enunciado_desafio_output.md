# 💪 **EXERCÍCIO DESAFIO**

### **Desafio:** 

Crie um script que permite conversar com o LLM em múltiplos turnos, mantendo o histórico da conversa.

### **Requisitos:**

- [ ] Inicializar modelo Groq corretamente
- [ ] Criar um loop que aceita input do usuário
- [ ] Manter histórico de mensagens (user + assistant)
- [ ] Adicionar uma mensagem de system no início definindo personalidade
- [ ] Permitir sair digitando "sair"
- [ ] Mostrar contador de mensagens trocadas

### **Dicas:**

- 💡 Use `input()` para ler entrada do usuário
- 💡 Mantenha uma lista `messages = []` e vá adicionando a cada turno
- 💡 Após cada resposta do LLM, adicione ela também ao histórico
- 💡 Use `while True:` para loop infinito com `break` para sair

---

## **Explicação da solução:**

1. **System message**: Define o comportamento do LLM no início da conversa
2. **Histórico persistente**: Cada mensagem (user + assistant) é adicionada à lista
3. **Context window**: O LLM recebe TODAS as mensagens anteriores a cada turno
4. **Loop infinito**: Permite múltiplas interações até digitar "sair"
5. **Contador**: Rastreia quantas trocas aconteceram

### **Por que isso é importante:**

- Em produção, agents precisam manter contexto de conversas
- Entender como o histórico funciona é fundamental para debugging
- Este padrão é a base para sistemas mais complexos com memória


---

## **Saída do Mini Sistema de Mensagens**

(.venv) andysouza@andysouzadell:~/langchain_v1-0_estudos_12-11-25$ python 1_4_desafio_primeiro_chat.py 
💬 Chat com LangChain v1.0
Digite 'sair' para encerrar

Você: O que é um agent?

🤖 Assistente: No contexto da LangChain, um agente (em inglês, "agent") é um componente fundamental que executa tarefas específicas em uma aplicação ou sistema. Em resumo, um agente é um programa ou script que pode realizar ações em nome de um usuário ou outro programa.

Nos sistemas de LangChain, os agentes são projetados para interagir com os modelos de linguagem e outros componentes do sistema para realizar tarefas como:

* Processamento de texto
* Resposta a perguntas
* Geração de conteúdo
* Classificação de texto
* Extração de informações

Os agentes podem ser classificados em diferentes categorias, dependendo de suas funções e capacidades. Alguns exemplos incluem:

* **Agentes de interface**: interagem com os usuários para coletar input e fornecer output.
* **Agentes de processamento**: realizam tarefas de processamento de texto, como tokenização, stemização, etc.
* **Agentes de conhecimento**: acessam e manipulam conhecimento armazenado em bancos de dados ou modelos de linguagem.

Os agentes são uma peça fundamental na arquitetura da LangChain, pois permitem que os sistemas de processamento de linguagem natural sejam mais flexíveis, escaláveis e personalizáveis. Eles podem ser facilmente integrados a outros componentes do sistema, permitindo que os desenvolvedores criem aplicações mais complexas e poderosas.

Espero que isso tenha ajudado a esclarecer o conceito de agente no contexto da LangChain! Se tiver mais alguma pergunta, sinta-se à vontade para perguntar.

📊 Mensagens trocadas: 1
--------------------------------------------------

Você: O que é chunck?

🤖 Assistente: No contexto da LangChain, um "chunk" (ou "pedaço" em português) refere-se a uma unidade de texto que é processada ou manipulada como uma entidade única. Em outras palavras, um chunk é um segmento de texto que é separado de outros segmentos por meio de um processo de tokenização ou segmentação.

Os chunks podem ser usados para representar diferentes níveis de granularidade no texto, como:

* **Palavras**: cada palavra pode ser considerada um chunk individual.
* **Frases**: uma frase pode ser considerada um chunk.
* **Parágrafos**: um parágrafo pode ser considerado um chunk.
* **Seções**: uma seção de um documento pode ser considerada um chunk.

Os chunks são importantes na LangChain porque permitem que os modelos de linguagem e os agentes processem o texto de forma mais eficiente e eficaz. Alguns exemplos de como os chunks são usados incluem:

* **Processamento de texto**: os chunks são usados para tokenizar o texto e realizar operações como stemização, lematização, etc.
* **Análise de sentimento**: os chunks são usados para analisar o sentimento de uma frase ou parágrafo.
* **Extração de informações**: os chunks são usados para extrair informações específicas de um texto, como nomes de pessoas, lugares, etc.

Os chunks também podem ser usados para melhorar a performance dos modelos de linguagem, pois permitem que os modelos processem o texto em lotes menores e mais gerenciáveis.

Aqui estão alguns exemplos de como os chunks podem ser representados:

* **Chunk de palavra**: "Eu", "amo", "comer", "pizza"
* **Chunk de frase**: "Eu amo comer pizza"
* **Chunk de parágrafo**: "Eu amo comer pizza. É minha comida favorita."

Espero que isso tenha ajudado a esclarecer o conceito de chunk no contexto da LangChain! Se tiver mais alguma pergunta, sinta-se à vontade para perguntar.

📊 Mensagens trocadas: 2
--------------------------------------------------

Você: sair

👋 Conversa encerrada. Total de mensagens: 4

📜 Histórico completo da conversa:
1. 👤 user: O que é um agent?...
2. 🤖 assistant: No contexto da LangChain, um agente (em inglês, "a...
3. 👤 user: O que é chunck?...
4. 🤖 assistant: No contexto da LangChain, um "chunk" (ou "pedaço" ...