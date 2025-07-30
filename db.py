import psycopg2
def get_connection():
    return psycopg2.connect(
        dbname='yt_data',
        user="yt_user or whatever suits you",
        password="yt_pass or whatever suits you",
        host="localhost",
        port="5432"
    )
