import psycopg2
import os
from typing import Optional

from db.vocab import SchoolEntity, SchoolQueryCondition


def add_school(school_condition : SchoolQueryCondition) -> Optional[int]:
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
                school_condition.name,
                school_condition.country,
                school_condition.state,
                school_condition.city,
                school_condition.zip_code,
                school_condition.address,
                school_condition.grade_level
            ]
            )

            # Fetch and print the results
            rows = cur.fetchall()

            if len(rows) == 0:
                return None

            school_id = rows[0]
            return school_id[0]



def find_school(school_condition : SchoolQueryCondition) -> list[SchoolEntity]:
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
            sql = '''
                SELECT id, name, country, state, city, zip_code, address, grade_level 
                FROM teacher_sch.schools 
                WHERE true
            '''
            bind = []

            if school_condition.id is not None:
                sql += 'AND id = %s '
                bind.append(school_condition.id)

            if school_condition.name is not None:
                sql += 'AND name = %s '
                bind.append(school_condition.name)

            if school_condition.address is not None:
                sql += 'AND address = %s '
                bind.append(school_condition.address)

            if school_condition.city is not None:
                sql += 'AND city = %s '
                bind.append(school_condition.city)

            if school_condition.state is not None:
                sql += 'AND state = %s '
                bind.append(school_condition.state)


            if school_condition.country is not None:
                sql += 'AND country = %s '
                bind.append(school_condition.country)

            if school_condition.grade_level is not None:
                sql += 'AND grade_level = %s '
                bind.append(school_condition.grade_level)

            if school_condition.zip_code is not None:
                sql += 'AND zip_code = %s '
                bind.append(school_condition.zip_code)


            cur.execute(sql, bind)

            # Fetch and print the results
            rows = cur.fetchall()

            result = []

            for row in rows:
                result.append(SchoolEntity(
                    id = row[0],
                    name = row[1],
                    country = row[2],
                    state = row[3],
                    city = row[4],
                    zip_code = row[5],
                    address = row[6],
                    grade_level = row[7]
                ))
            return result


def remove_school(id : int) -> Optional[int]:
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
                DELETE 
                FROM teacher_sch.schools
                WHERE id = %s
                RETURNING *;
            ''',
            [id])
            
            # Fetch and print the results
            rows = cur.fetchall()
            
            return len(rows)
