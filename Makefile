dev-setup:
	docker-compose up -d postgres redis
	pip install -U -r requirements.txt

dev-setup-down:
	docker-compose down

lint-check:
	ruff check backend_essentials --fix

format:
	ruff format backend_essentials

run-makemigrations:
	python3 backend_essentials/manage.py makemigrations

run-migrations:
	python3 backend_essentials/manager.py migrate
