lint:
	.venv/bin/ruff check src/
	.venv/bin/mypy src/

format:
	.venv/bin/ruff format src/

check: lint format

fix:
	.venv/bin/ruff check src/ --fix

test:
	.venv/bin/pytest

clean:
	@echo "Cleaning build artifacts and caches..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf dist/ build/ *.egg-info src/*.egg-info

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

dev:
	python manage.py runserver
