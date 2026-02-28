from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def main():
    # 1. Configuração do Modelo
    llm = OllamaLLM(
        model="llama3.1:latest", 
        base_url="http://localhost:11434"
    )

    # 2. Template do Sistema
    template = """
    Você é um assistente de IA especializado em Python e Machine Learning.
    Pergunta do usuário: {pergunta}
    Resposta técnica e concisa:
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    print("--- Assistente de IA Iniciado (Digite 'sair' para encerrar) ---")

    # 3. Loop de Interação
    while True:
        # Captura a pergunta do usuário no terminal
        pergunta_usuario = input("\nVocê: ")

        # Verifica se o usuário deseja sair
        if pergunta_usuario.lower() in ["sair", "exit", "quit", "parar"]:
            print("Encerrando assistente... Até logo!")
            break

        if not pergunta_usuario.strip():
            continue

        print("IA pensando...\n")

        try:
            # Invoca a cadeia e exibe a resposta
            resposta = chain.invoke({"pergunta": pergunta_usuario})
            print(f"--- RESPOSTA DA IA ---\n{resposta}")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")

if __name__ == "__main__":
    main()