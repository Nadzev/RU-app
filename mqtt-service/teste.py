from mqtt import Mqtt
import asyncio

m = Mqtt()
loop = asyncio.get_event_loop()

def teste_publish():
    print('enviando')
    m.client.publish("topico_teste","enviando")

if __name__ == "__main__":
    loop.run_until_complete(m.main())
    teste_publish()
    loop.run_forever()
    
    