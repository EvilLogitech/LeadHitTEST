PORT ?= 8000

install:
		poetry install

dev:
		poetry run flask --app form_data_handler:app run --port $(PORT) --debug

lint:
		poetry run flake8 form_data_handler
		poetry run flake8 tests

test:
		poetry run pytest --cov

test-coverage:
		poetry run pytest --cov=form_data_handler tests/ --cov-report xml

start:
		poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) form_data_handler:app

show:
		poetry run presentation