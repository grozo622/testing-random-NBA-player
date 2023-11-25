install:
	pip install --upgrade pip &&\
	    pip install -r requirements.txt &&\
	    pip install Flask

lint:
	pylint --disable=R,C,W1203,W0702 app.py

test:
	pip install pytest pytest-cov &&\
	    python -m pytest -vv --cov=app test_app.py

format:
	black *.py

all: install lint test format
