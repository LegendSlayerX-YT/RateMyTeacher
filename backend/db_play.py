import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="rate_my_teacher_db",
    user="postgres",
    password="abc123",
    host="localhost",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT 1; ")

# Fetch and print the results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()