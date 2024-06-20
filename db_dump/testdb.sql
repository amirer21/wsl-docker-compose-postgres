-- 데이터베이스 생성 (이미 존재하면 생략 가능)
CREATE DATABASE testdb;

-- 데이터베이스 선택 (이미 접속했다면 생략 가능)
\c testdb

-- 테이블 생성
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary NUMERIC
);

-- 샘플 데이터 삽입
INSERT INTO employees (name, position, salary) VALUES
('John Doe', 'Manager', 60000),
('Jane Smith', 'Developer', 55000),
('Sam Johnson', 'Designer', 50000);

-- 데이터 확인
SELECT * FROM employees;
