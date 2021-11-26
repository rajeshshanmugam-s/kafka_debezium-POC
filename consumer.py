from kafka import KafkaConsumer
import json

try:
    print('Welcome to parse engine')
    consumer = KafkaConsumer('postgres.public.shipments', bootstrap_servers='localhost:9092')
    for message in consumer:
        print(message)
except Exception as e:
    print(e)
    # Logs the error appropriately. 
    pass

# docker run --tty --network kafka_tutorial_default confluentinc/cp-kafkacat kafkacat -b kafka:9092 -C -s key=s -s value=avro -r http://schema-registry:8081 -t postgres.public.shipments

# from kafka import KafkaConsumer

# from confluent_avro import AvroKeyValueSerde, SchemaRegistry
# from confluent_avro.schema_registry import HTTPBasicAuth

# KAFKA_TOPIC = "postgres.public.shipments"

# registry_client = SchemaRegistry(
#     "http://schema-registry:8081",
#     headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
# )
# avroSerde = AvroKeyValueSerde(registry_client, KAFKA_TOPIC)

# consumer = KafkaConsumer(
#     KAFKA_TOPIC,
#     bootstrap_servers=["localhost:9092",]
# )

# for msg in consumer:
#     v = avroSerde.value.deserialize(msg.value)
#     k = avroSerde.key.deserialize(msg.key)
#     print(msg.offset, msg.partition, k, v)