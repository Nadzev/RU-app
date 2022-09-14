FROM python:^3.9-slim
WORKDIR /app

COPY . .

RUN poetry install

CMD ["python3", "./server.py"]