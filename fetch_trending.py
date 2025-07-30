from googleapiclient.discovery import build
import datetime
from db import get_connection

# === YouTube API Setup ===
API_KEY = 'AIzaSyAz7PqnMJFPHruqsPvki3gWppp_JUYDvsQ'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

# === Insert Function ===
def insert_video(video):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO trending_videos (
                video_id, title, published_at, channel_title,
                category_id, view_count, like_count, comment_count, trending_date
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (video_id) DO NOTHING;
        """, (
            video['video_id'],
            video['title'],
            video['published_at'],
            video['channel_title'],
            video['category_id'],
            video['view_count'],
            video['like_count'],
            video['comment_count'],
            datetime.date.today()
        ))
        conn.commit()
        print(f"✅ Inserted: {video['title']}")
    except Exception as e:
        print("❌ DB Insert Error:", e)
    finally:
        cur.close()
        conn.close()

# === Fetch Trending Videos ===
def fetch_trending_videos(region_code='IN', max_results=25):
    request = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()

    for item in response['items']:
        video = {
            'video_id': item['id'],
            'title': item['snippet']['title'],
            'published_at': item['snippet']['publishedAt'],
            'channel_title': item['snippet']['channelTitle'],
            'category_id': int(item['snippet'].get('categoryId', 0)),
            'view_count': int(item['statistics'].get('viewCount', 0)),
            'like_count': int(item['statistics'].get('likeCount', 0)),
            'comment_count': int(item['statistics'].get('commentCount', 0))
        }
        insert_video(video)

# === Main Execution ===
if __name__ == "__main__":
    fetch_trending_videos()