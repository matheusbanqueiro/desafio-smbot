# Para os comandos funcionarem, você precisa estar no seu ambiente virtual venv.

.PHONY: help run migrations tests up down ps

BACK_END_LOCAL_URL=localhost:8000

help:
	@echo "===================================="
	@echo "  ClientConnect - Comandos Makefile"
	@echo "===================================="
	@echo "Comandos disponíveis:"
	@echo "  make run        - Inicia o servidor Django na URL especificada."
	@echo "  make migrations - Cria e aplica migrações no banco de dados."
	@echo "  make tests      - Executa os testes automatizados."
	@echo "  make up         - Inicia os containers Docker definidos."
	@echo "  make down       - Para e remove os containers Docker."
	@echo "  make ps         - Lista os containers Docker em execução."
	@echo "===================================="
	@echo "Lembre-se de estar no ambiente virutal"
	@echo "===================================="
run:
	@echo "Iniciando o servidor Django em $(BACK_END_LOCAL_URL)..."
	python manage.py runserver $(BACK_END_LOCAL_URL)

migrations:
	@echo "Criando e aplicando migrações..."
	python3 manage.py makemigrations
	python3 manage.py migrate

tests:
	@echo "Executando testes..."
	python3 manage.py test

up:
	@echo "Subindo containers Docker..."
	docker-compose up -d

down:
	@echo "Parando e removendo containers Docker..."
	docker-compose down

ps:
	@echo "Listando containers Docker em execução..."
	docker-compose ps
