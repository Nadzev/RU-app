from mqtt import Mqtt
import asyncio

m = Mqtt()
loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(m.main())
    loop.run_forever()
    