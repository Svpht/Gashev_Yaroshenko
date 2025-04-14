import psycopg2
from psycopg2 import sql
DB_HOST = '79.174.88.238'
DB_PORT = 15221
DB_NAME = 'school_db'
DB_USER = 'school'
DB_PASSWORD = 'School1234*'

connect = psycopg2.connect(
    dbname=DB_NAME,
    host = DB_HOST,
    port = DB_PORT,
    user = DB_USER,
    password = DB_PASSWORD
)