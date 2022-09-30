# RU-app

Como faço para inicializar o ambiente virtual?

```console
export $(cat config/.env | xargs) 
poetry install
poetry shell
```

Como faço para inicializar a aplicação?

```console
sudo docker-compose up -d
python3 -m src._test
```

Como faço para iniciar o Broker Mosquitto?

 - Primeiro você deve configurar o arquivo configure.conf e trocar o ip pelo um que faça sentido...
 - Após isso, faça os seguintes comandos:
 
```console
cd path/to/configure.conf/file
sudo fuser -k 1883/tcp
mosquitto -v -d -c configure.conf
```
