from azure.eventhub import EventHubProducerClient, EventData

connection_str = 'Endpoint=sb://przemek-eventhub.servicebus.windows.net/;SharedAccessKeyName=SendHubEvents;SharedAccessKey=4uy4lmvMNKuqT99N0WUnDo0RbRa/7jVIIHwQ14FdP5M=;EntityPath=przemek-hub'
consumer_group = '$Default'
eventhub_name = 'przemek-hub'


def send_once():
    client = EventHubProducerClient.from_connection_string(
        connection_str,
        eventhub_name=eventhub_name
    )

    with client:
        event_data = client.create_batch()
        event_data.add(EventData('{"film":"Avengers", "rank": "3"}'))
        client.send_batch(event_data)


if __name__ == '__main__':
    send_once()
    print('Event published!')
