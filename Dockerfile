FROM python:3.8-alpine

RUN apk --no-cache add git
RUN git clone https://github.com/santilc25/end-to-end-ml-project.git /app

WORKDIR /app

RUN apt update -y && apt install awscli -y
RUN pip install -r requirements

CMD ["python", "app.py"]
