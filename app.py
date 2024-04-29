import psycopg2

dbname = 'Saifertek'
user = 'postgres'
password = '2003'
host = 'localhost'
port = '5432'

connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = connection.cursor()

query_with_join = """
SELECT loc.location_id, loc.street_address, loc.city, loc.state_province, co.country_name
FROM locations loc
JOIN countries co ON loc.country_id = co.country_id
WHERE co.country_name = 'Canada'
"""

cursor.execute(query_with_join)

print("Query with JOIN:")
for row in cursor.fetchall():
    print(row)

query_without_join = """
SELECT location_id, street_address, city, state_province, 
    (SELECT country_name FROM countries WHERE countries.country_id = locations.country_id) AS country_name
FROM locations
WHERE country_id = 'CA';
"""

cursor.execute(query_without_join)

print("\nQuery without JOIN:")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
