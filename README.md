# RU-app

Como faço para inicializar o ambiente virtual?

```console
export $(cat config/.env | xargs) 
poetry install
poetry shell
```