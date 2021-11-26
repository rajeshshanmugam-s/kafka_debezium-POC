import psycopg2
conn = psycopg2.connect(database="shipment_db", user="postgresuser", password="postgrespw", host="127.0.0.1", port="5432")
print("Database Connected....")
cursor = conn.cursor()
cursor.execute("update shipments set status='PTR' where order_id = 12500;")
conn.commit()
conn.close()
# cursor.execute("select * from shipments;")

# rows = cursor.fetchall()

# for row in rows:
#     print(row[3])

# from schema_registry.client import SchemaRegistryClient


# sr = SchemaRegistryClient('0.0.0.0:8081')
# my_schema = sr.get_by_id(schema_id=1)