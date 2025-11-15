🟢 TÓPICO 1: FUNDAMENTOS

## 📖 TEORIA

### O que é LangChain v1.0?

LangChain é um framework para desenvolvimento de aplicações alimentadas por modelos de linguagem (LLMs). A versão 1.0, lançada em outubro de 2025, trouxe mudanças significativas que tornam o framework mais estável, modular e pronto para produção.

### **Conceitos fundamentais que você precisa entender:**

**Agents**: São sistemas autônomos que usam LLMs para decidir quais ações tomar. Eles podem chamar ferramentas (tools), processar informações e responder dinamicamente. Pense em um agent como um assistente que pode usar calculadoras, fazer buscas na web, consultar bancos de dados - tudo decidido por conta própria o que precisa fazer.

**Tools**: São funções que os agents podem executar. Uma tool pode fazer diversas coisas: buscar informações na web, consultar um banco de dados, fazer cálculos, enviar emails, etc. As tools são o "corpo" do agent - sem elas, ele só pode conversar.

**Messages**: São as unidades de comunicação. Cada mensagem tem um `role` (quem está falando) e `content` (o que está sendo dito). Os roles principais são: `user` (você), `assistant` (o LLM), `system` (instruções para o LLM) e `tool` (resultados de ferramentas).

### Por que LangChain v1.0 é importante?

A v1.0 trouxe **breaking changes** significativas, removendo código legado e estabelecendo padrões mais claros. Isso significa que muitos tutoriais antigos **não funcionam mais**. Dominar a v1.0 agora te coloca à frente, pois a maioria dos desenvolvedores ainda usa v0.x ou está migrando.

### Quando usar LangChain?

✅ **Use quando:** Você precisa construir aplicações com LLMs que tomam decisões, usam ferramentas, mantêm contexto de conversação, ou integram múltiplas fontes de dados.

❌ **Não use quando:** Você só precisa fazer uma chamada simples para um LLM sem lógica complexa. Nesse caso, a API direta do provedor é mais simples.