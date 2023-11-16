install:
		poetry install

dev:
		poetry run flask --app form_data_handler/app:app run --debug

lint:
		poetry run flake8 form_data_handler
		poetry run flake8 tests

test:
		poetry run pytest --cov

test-coverage:
		poetry run pytest --cov=form_data_handler tests/ --cov-report xml

PORT ?= 5000
start:
		poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) form_data_handler:app