install: 
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -v test_hello.py

format:
	black *.py

link:
	pylint --disable=R,C hello.py

all: install lint test
