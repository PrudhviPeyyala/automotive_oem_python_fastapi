import MySQLdb

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': 'test'
}


def get_database_connection():
    print(' ==== creating database connection ====')
    conn = MySQLdb.connect(**db_config)
    print(' ==== database connection created ====')
    return conn
