import psycopg2

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
