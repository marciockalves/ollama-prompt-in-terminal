# Variáveis para facilitar a manutenção
CONTAINER_NAME=ollama
MODEL_DEEPSEEK=deepseek-r1:8b
MODEL_LLAMA=llama3.1

.PHONY: setup pull-all pull-deepseek pull-llama status

# Comando principal: Sobe o docker e baixa tudo
setup:
	docker compose up -d
	@echo "Aguardando o Ollama iniciar..."
	@sleep 5
	$(MAKE) pull-all

stop-setup:
	docker compose down

# Baixa todos os modelos de uma vez
pull-all:
	docker exec -it $(CONTAINER_NAME) ollama pull $(MODEL_DEEPSEEK)
	docker exec -it $(CONTAINER_NAME) ollama pull $(MODEL_LLAMA)
	@echo "Todos os modelos foram baixados com sucesso!"

# Baixa apenas o DeepSeek
pull-deepseek:
	docker exec -it $(CONTAINER_NAME) ollama pull $(MODEL_DEEPSEEK)

# Baixa apenas o Llama
pull-llama:
	docker exec -it $(CONTAINER_NAME) ollama pull $(MODEL_LLAMA)

# Verifica o status dos modelos baixados
status:
	docker exec -it $(CONTAINER_NAME) ollama list

run:
	uv run main.py