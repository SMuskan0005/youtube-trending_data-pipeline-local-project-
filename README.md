# youtube-trending_data-pipeline-local-project-

# 🎥 YouTube Trending Data Pipeline

A local ETL pipeline that:
- Fetches trending videos using the YouTube Data API v3
- Stores raw data in a CSV file
- Loads structured data into a PostgreSQL database
- Automates the entire workflow with Apache Airflow

---

## ⚙ Tech Stack

- Python, Pandas
- YouTube Data API
- PostgreSQL, psycopg2
- Apache Airflow

---

## 🏗 Architecture

YouTube API → Python → CSV → PostgreSQL  
🌀 Orchestrated by Airflow DAG (Optional)

PS :  Get Your YouTube API Key ( for fetching data)

1. Go to: "https://console.cloud.google.com"
2. Create a project (e.g., yt-pipeline)
3. Go to “APIs & Services” → “Library”
4. Search for YouTube Data API v3 → Enable it
5. Go to “Credentials” → Create API key
6. Copy and save the key

---

Directory Structure
af project 
   |- yt_pipeline - contains the frtch_trending.py
   |-airflow_home(automatically created) contained Dags and logs 
        |dags -> youtube_trending_dag   
  
   
