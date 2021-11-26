from kafka import KafkaProducer
"""
Connect to the localhost kafka and send message to the topic named `sample`
Flush will wait for all the messages in the producer queue to be delivered. 
"""
print("Start producing")
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('postgres.public.shipments', b'Hello, World!')
producer.send('postgres.public.shipments', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
print("End")