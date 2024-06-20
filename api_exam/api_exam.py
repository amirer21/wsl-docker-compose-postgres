import psycopg2
from psycopg2 import sql

# PostgreSQL 서버 접속 정보
host = "172.0.0.4"
port = 5432
database = "testdb"
user = "hong"
password = "1111"

# 데이터베이스에 접속
try:
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    # 테이블 생성
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        position VARCHAR(100),
        salary NUMERIC
    )
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully")

    # 데이터 삽입
    insert_data_query = '''
    INSERT INTO employees (name, position, salary) VALUES
    (%s, %s, %s)
    '''
    data_to_insert = [
        ('John Doe', 'Manager', 62200),
        ('Jane Smith', 'Developer', 55000),
        ('Sam Johnson', 'Designer', 50000)
    ]
    cursor.executemany(insert_data_query, data_to_insert)
    connection.commit()
    print("Data inserted successfully")

    # 데이터 조회
    select_query = 'SELECT * FROM employees'
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("Data retrieved successfully")
    for record in records:
        print(record)

except Exception as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
