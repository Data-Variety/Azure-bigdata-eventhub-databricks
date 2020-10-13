from azure.eventhub import EventHubProducerClient, EventData

connection_str = 'Endpoint=sb://'
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
