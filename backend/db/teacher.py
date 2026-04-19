import psycopg2
import os
from typing import Optional

from db.vocab import TeacherEntity, TeacherQueryCondition

def add_teacher(teacher_condition : TeacherQueryCondition) -> int:
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
                INSERT INTO teacher_sch.teachers (school_id, name, email) 
                VALUES (%s, %s, %s) RETURNING id; 
            ''', 
            [
                teacher_condition.school_id,
                teacher_condition.name,
                teacher_condition.email
            ]
            )

            # Fetch and print the results
            rows = cur.fetchall()

            if len(rows) == 0:
                return None

            teacher_id = rows[0]
            return teacher_id[0]


def find_teacher(teacher_condition : TeacherQueryCondition) -> list[TeacherEntity]:
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
                SELECT id, school_id, name, email
                FROM teacher_sch.teachers 
                WHERE true
            '''
            bind = []

            if teacher_condition.id:
                sql += 'AND id = %s '
                bind.append(teacher_condition.id)

            if teacher_condition.school_id:
                sql += 'AND school_id = %s '
                bind.append(teacher_condition.school_id)

            if teacher_condition.name:
                sql += 'AND name = %s '
                bind.append(teacher_condition.name)

            if teacher_condition.email:
                sql += 'AND email = %s '
                bind.append(teacher_condition.email)

            cur.execute(sql, bind)

            # Fetch and print the results
            rows = cur.fetchall()

            result = []

            for row in rows:
                result.append(TeacherEntity(
                    id = row[0],
                    school_id = row[1],
                    name = row[2],
                    email = row[3]
                ))
            return result

def remove_teacher(id : int) -> Optional[int]:
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
                FROM teacher_sch.teachers
                WHERE id = %s
                RETURNING *;
            ''',
            [id])
            
            # Fetch and print the results
            rows = cur.fetchall()
            
            return len(rows)