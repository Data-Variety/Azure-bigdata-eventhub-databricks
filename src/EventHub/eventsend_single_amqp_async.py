import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

connection_str = 'Endpoint=sb://przemek-eventhub.servicebus.windows.net/;SharedAccessKeyName=SendHubEvents;SharedAccessKey=4uy4lmvMNKuqT99N0WUnDo0RbRa/7jVIIHwQ14FdP5M=;EntityPath=przemek-hub'
consumer_group = '$Default'
eventhub_name = 'przemek-hub'


async def send_once():
    client = EventHubProducerClient.from_connection_string(
        connection_str,
        eventhub_name=eventhub_name
    )

    async with client:
        event_data = await client.create_batch()
        event_data.add(EventData('{"film":"Witcher", "rank": "5"}'))
        event_data.add(EventData('{"film":"Witcher", "rank": "6"}'))
        event_data.add(EventData('{"film":"Ponies", "rank": "5"}'))
        event_data.add(EventData('{"film":"Capo", "rank": "4"}'))
        event_data.add(EventData('{"film":"Witcher", "rank": "5"}'))
        await client.send_batch(event_data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_once())
    print('Event published!')
