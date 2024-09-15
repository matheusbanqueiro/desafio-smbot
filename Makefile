# Para os comandos funcionar você precisa estar no seu ambiente virtual venv 

.PHONY: help run migrations tests up down ps

# Define a variável BACK_END_LOCAL_URL
BACK_END_LOCAL_URL=localhost:8000

help:
	@echo "**Para os comandos funcionar você precisa estar no seu ambiente virtual venv**"
	@echo "Comandos disponíveis:"
	@echo "  make run        - Inicia o servidor Django na URL especificada pela variável BACK_END_LOCAL_URL."
	@echo "  make migrations - Cria e aplica migrações no banco de dados Django."
	@echo "  make tests      - Executa os testes do Django."
	@echo "  make up         - Inicia os containers Docker definidos no docker-compose.yml."
	@echo "  make down       - Para e remove os containers Docker."
	@echo "  make ps         - Lista os containers Docker em execução."

run:
	python manage.py runserver $(BACK_END_LOCAL_URL)

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

tests:
	python3 manage.py test

up:
	docker-compose up -d

down:
	docker-compose down

ps:
	docker-compose ps
