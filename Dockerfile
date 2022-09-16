FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["python3", "src/main.py"]