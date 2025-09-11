import asyncio
from aiomqtt import Client

async def mqtt_example():
    async with Client("test.mosquitto.org") as client:
        await client.publish("temperature", payload="25.3")
        async with client.messages() as messages:
            await client.subscribe("temperature")
            async for message in messages:
                return message.payload

# run
data = asyncio.run(mqtt_example())
