install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=W,R,C *.py

build:

deploy: