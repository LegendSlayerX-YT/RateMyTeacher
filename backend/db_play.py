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

name = "Cottonwood Creek TK-8"
# Execute a query
cur.execute(f'''
                SELECT id, name, country, state, city, zip_code, address, grade_level 
                FROM teacher_sch.schools 
                WHERE name = %s; 
            ''',
            [name])

# Fetch and print the results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()