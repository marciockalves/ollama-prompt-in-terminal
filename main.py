import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def main():
    
    nome_modelo = os.getenv("OLLAMA_MODEL", "llama3.1")
    url_base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    print(f"--- Iniciando com o modelo: {nome_modelo} ---")
    print(f"--- Na base url: {url_base} ---")

    llm = OllamaLLM(
        model=nome_modelo, 
        base_url=url_base
    )

    template = """
    Você é um assistente de IA especializado em Python e Machine Learning.
    Pergunta do usuário: {pergunta}
    Resposta técnica e concisa:
    """

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    print("--- Assistente de IA Iniciado (Digite 'sair' para encerrar) ---")

    while True:
        pergunta_usuario = input("\nVocê: ")

        if pergunta_usuario.lower() in ["sair", "exit", "quit", "parar"]:
            break

        if not pergunta_usuario.strip():
            continue

        print("IA pensando...\n")

        try:
            resposta = chain.invoke({"pergunta": pergunta_usuario})
            print(f"--- RESPOSTA DA IA ---\n{resposta}")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")

if __name__ == "__main__":
    main()