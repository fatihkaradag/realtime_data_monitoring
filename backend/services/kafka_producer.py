from kafka import KafkaProducer

class KafkaProducerService:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def send_data(self, topic, data):
        # Convert data to bytes if necessary
        if isinstance(data, str):
            data = data.encode('utf-8')

        # Send data to Kafka topic
        self.producer.send(topic, data)
