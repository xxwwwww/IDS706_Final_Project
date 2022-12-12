install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=W,R,C --ignore-patterns=test_.*?py *.py

build:

deploy:

all:
