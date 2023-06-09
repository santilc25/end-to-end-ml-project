FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/santilc25/end-to-end-ml-project.git /app

WORKDIR /app

RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
