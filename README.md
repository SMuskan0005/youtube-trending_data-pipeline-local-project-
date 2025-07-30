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

---

Directory Structure
af project 
   |- yt_pipeline - contains the frtch_trending.py
   |-airflow_home(automatically created) contained Dags and logs 
        |dags -> youtube_trending_dag   
  
   
