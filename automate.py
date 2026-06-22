import requests
import urllib.parse
from datetime import datetime

NEWS_API_KEY = "3d9d1ca3fdd94186a02a173fa4b0793b"
BUFFER_TOKEN = "8Yau2zZcwB1uROnn-gRyP7LTziXVjzpqqGhnPAgTrO_"
BUFFER_PROFILE_ID = "6a39918a5ab6d2f1065e1f21"
NICHE_KEYWORD = "artificial intelligence"

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q={NICHE_KEYWORD}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    return requests.get(url).json().get("articles", [])

def generate_image_url(prompt):
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}?width=1080&height=1080&nologo=true"

def generate_post(title):
    hashtags = "#AI #Tech #News #MachineLearning #Innovation"
    return f"🚀 {title}\n\n{hashtags}"

def post_to_buffer(text, image_url):
    headers = {"Authorization": f"Bearer {BUFFER_TOKEN}", "Content-Type": "application/json"}
    data = {"text": text, "media": {"link": image_url}, "profile_ids": [BUFFER_PROFILE_ID], "now": True}
    try:
        r = requests.post("https://api.bufferapp.com/1/updates/create.json", headers=headers, json=data)
        print(f"Buffer Status: {r.status_code}")
        print(f"Buffer Response: {r.text}")
        return r.status_code == 200
    except Exception as e:
        print(f"Buffer Error: {e}")
        return False

def run():
    print("🔍 Fetching news...")
    articles = fetch_news()
    if not articles:
        print("No articles found")
        return
    article = articles[0]
    title = article['title'][:100]
    print(f"📰 Story: {title}")
    post = generate_post(title)
    image_url = generate_image_url(title)
    print(f"\n🖼 Image: {image_url}")
    print(f"\n📝 Post:\n{post}")
    print("\n📤 Posting to Instagram via Buffer...")
    if post_to_buffer(post, image_url):
        print("✅ Successfully posted!")
    else:
        print("❌ Failed to post")
    print(f"\n✅ Generated at {datetime.now()}")

if __name__ == "__main__":
    run()
