# Kafka Debezium POC (Change Data Capture)

* Clone the Repo

* In [docker-compose.yml](docker-compose.yml) change the line number 28 `KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://127.0.0.1:9092` to your Public IP. 

* Run `docker-compose up -d`

* Check all the five services are running. 

* There is a SQL script under [scripts](scripts/) folder, It will be executed when the containers are starting. 

* Enter the postgres container and check for the Table `shipments` if it is not there create the table based on the [script](scripts/) 
     - To enter into the container `docker exec -it <<containerid>> bash` then `psql -U postgresuser -d shipment_db`

     - Alternate solution (Remove the postgres volume and build again)

* Enter into the Debezium Connect container and the run the below command
       
        curl -H 'Content-Type: application/json' debezium:8083/connectors --data '
        {
        "name": "shipments-connector",  
        "config": {
            "connector.class": "io.debezium.connector.postgresql.PostgresConnector", 
            "plugin.name": "pgoutput",
            "database.hostname": "postgres", 
            "database.port": "5432", 
            "database.user": "postgresuser", 
            "database.password": "postgrespw", 
            "database.dbname" : "shipment_db", 
            "database.server.name": "postgres", 
            "table.include.list": "public.shipments" }
        }'

* Now Postgres DB is connected to the Kafka Via Debezium connect. 

* For Kcat Monioring: 

    * Run in a new Terminal: 

`docker run --tty --network kafka_debezium-poc_default confluentinc/cp-kafkacat kafkacat -b kafka:9092 -C -s key=s -s value=avro -r http://schema-registry:8081 -t postgres.public.shipments`

* To see the docker networks `docker volume ls`
* It is using the avro format 
* And finally the topic name that is postgres.public.shipments

* For Python clients: 
    - Create a virtualenv 
    - Install the Requirements from requirements.txt  `pip install -r requirements.txt`

* For Python consumer:

#### TODO: In python consumer output is in Avro format, need to deserialize using Avro schema. 
    
    python consumer.py    

To run the consumer from a different host. Change the argument bootstrap_servers to the public IP of the kafka host in line no:6 of consumer.py 

* To Update the PostgresDB:

`python pg_update.py`

Reference: 
- https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html
- https://medium.com/event-driven-utopia/a-visual-introduction-to-debezium-32563e23c6b8
- https://medium.com/event-driven-utopia/configuring-debezium-to-capture-postgresql-changes-with-docker-compose-224742ca5372

