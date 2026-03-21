import psycopg2
from db.vocab import SchoolEntity
import os
from typing import Optional

def add_school(schoolentity : SchoolEntity) -> Optional[int]:
    # Connect to your PostgreSQL database
    with psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
    ) as conn:
        # Create a cursor object
        with conn.cursor() as cur:
            # Execute a query
            cur.execute('''
                INSERT INTO teacher_sch.schools (name, country, state, city, zip_code, address, grade_level) 
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id; 
            ''', 
            [
                schoolentity.name,
                schoolentity.country,
                schoolentity.state,
                schoolentity.city,
                schoolentity.zip_code,
                schoolentity.address,
                schoolentity.grade_level
            ]
            )

            # Fetch and print the results
            rows = cur.fetchall()

            if len(rows) == 0:
                return None

            school = rows[0]
            return school[0]



def find_school(id : int) -> Optional[SchoolEntity]:
    # Connect to your PostgreSQL database
    with psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
    ) as conn:
        # Create a cursor object
        with conn.cursor() as cur:
            # Execute a query
            cur.execute('''
                SELECT id, name, country, state, city, zip_code, address, grade_level 
                FROM teacher_sch.schools 
                WHERE id = %s; 
            ''', 
            [id])

            # Fetch and print the results
            rows = cur.fetchall()

            if len(rows) == 0:
                return None

            school = rows[0]
            return SchoolEntity(
                id=school[0],
                name=school[1],
                country=school[2],
                state=school[3],
                city=school[4],
                zip_code=school[5],
                address=school[6],
                grade_level=school[7],
            )