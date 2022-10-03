FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["python3", "-m", "src.main"]