# Ensure the virtual environment (venv) is set up before running the Makefile. 
# Manually create the virtual environment using the following commands in your terminal:
# python -m venv venv
# Then activate. => source venv/bin/activate . When done, deactivate.

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt &&\
	pip install Flask &&\
	pip install beautifulsoup4 requests

lint:
	pylint --disable=R,C,W1203,W0702 app.py

test:
	pip install pytest pytest-cov &&\
	python -m pytest -vv --cov=app test_app.py

format:
	black *.py

all: install lint test format
