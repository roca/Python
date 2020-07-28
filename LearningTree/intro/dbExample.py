import psycopg2

conn = psycopg2.connect(host="db", dbname="python", user="postgres", password="password")

cur = conn.cursor()
command = " CREATE TABLE vendors ( vendor_id SERIAL PRIMARY KEY, vendor_name VARCHAR(255) NOT NULL); "
try:
    cur.execute(command)
    conn.commit()
except:
    print("Table already exists")
    conn.rollback()

cur.execute("INSERT INTO vendors (vendor_name) VALUES ('ACME2');")
conn.commit()
cur.close()