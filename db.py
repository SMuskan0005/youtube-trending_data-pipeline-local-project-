import psycopg2
def get_connection():
    return psycopg2.connect(
        dbname='yt_data',
        user="yt_user",
        password="yt_password",
        host="localhost",
        port="5432"
    )