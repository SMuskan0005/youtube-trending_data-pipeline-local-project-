from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add yt_pipeline path
sys.path.append(os.path.expanduser('~/af_project/yt_pipeline_project'))

from fetch_trending import fetch_trending_videos, insert_video

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fetch_and_store():
    df = get_trending_videos()
    for _, row in df.iterrows():
        video = {
            'video_id': row['video_id'],
            'title': row['title'],
            'published_at': row['publishedAt'],
            'channel_title': row['channel'],
            'category_id': int(row['categoryId']),
            'view_count': int(row['views']),
            'like_count': int(row['likes']),
            'comment_count': int(row['comments']),
        }
        insert_video(video)

with DAG(
    dag_id='youtube_trending_pipeline',
    default_args=default_args,
    description='Fetch trending YouTube videos and store in PostgreSQL daily',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    run_pipeline = PythonOperator(
        task_id='fetch_and_store_videos',
        python_callable=fetch_and_store
    )