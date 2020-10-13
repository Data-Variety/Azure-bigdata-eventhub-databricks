import asyncio
from random import randint
from time import sleep

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

connection_str = 'Endpoint=sb://'
consumer_group = '$Default'
eventhub_name = 'przemek-hub'


async def send_once():
    client = EventHubProducerClient.from_connection_string(
        connection_str,
        eventhub_name=eventhub_name
    )

    async with client:
        event_data = await client.create_batch()

        can_add = True
        while can_add:
            try:
                event_data.add(EventData('{"film":"Witcher", "rank": "5"}'))
            except ValueError:
                can_add = False

        await client.send_batch(event_data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    i = 1
    while i <= 10:
        loop.run_until_complete(send_once())
        print('Event published! {} time'.format(str(i)))
        i += 1
        sleep(randint(1,10))
