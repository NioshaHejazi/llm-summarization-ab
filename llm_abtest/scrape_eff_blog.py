import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.eff.org/deeplinks"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_blog_links(limit=10):
    res = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    
    articles = soup.select("h3.node__title a")
    links = ["https://www.eff.org" + a["href"] for a in articles if a.has_attr("href")]
    print(f"✅ Found {len(links)} article links")
    return links[:limit]

def extract_article_content(url):
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    
    title_tag = soup.find("h1", id="page-title")
    content_tags = soup.select("div.field--name-body p")

    title = title_tag.text.strip() if title_tag else "Untitled"
    text = "\n".join(p.text.strip() for p in content_tags)

    return title, text

def scrape_and_save(limit=10, output_file="eff_blogs.json"):
    links = get_blog_links(limit)
    data = []

    for idx, url in enumerate(links, 1):
        print(f"🔍 Scraping ({idx}/{limit}): {url}")
        try:
            title, text = extract_article_content(url)
            if len(text) > 200:
                data.append({
                    "id": idx,
                    "title": title,
                    "url": url,
                    "text": text
                })
            else:
                print(f"⚠️ Skipped (too short): {title}")
        except Exception as e:
            print(f"❌ Failed to process {url}: {e}")
        time.sleep(1.0)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved {len(data)} articles to {output_file}")

if __name__ == "__main__":
    scrape_and_save()
