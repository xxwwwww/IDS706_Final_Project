FROM python:3.8.13-slim-buster

RUN mkdir -p /app
COPY app.py requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "app.py" ]
ENTRYPOINT [ "python" ]