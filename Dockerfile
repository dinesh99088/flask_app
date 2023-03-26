FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y procps net-tools

EXPOSE 80

CMD ["python", "app.py"]
