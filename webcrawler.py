import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# ---------------------------
# Web Crawler
# ---------------------------

def crawl_site(seed_url, max_pages=10):
    visited = set()
    to_visit = [seed_url]
    collected_urls = []

    while to_visit and len(collected_urls) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            visited.add(url)
            collected_urls.append(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if full_url.startswith(seed_url):  # stay within domain
                    to_visit.append(full_url)

        except Exception:
            continue

    return collected_urls

def filter_news_urls(urls):
    keywords = ["news", "article", "world", "politics", "business"]
    return [url for url in urls if any(k in url.lower() for k in keywords)]

if __name__ == "__main__":
    seed_url = "https://www.bbc.com"
    print(f"Crawling: {seed_url}")
    
    collected = crawl_site(seed_url, max_pages=20)
    print(f"\nCollected {len(collected)} URLs:")
    for url in collected:
        print(" -", url)

    filtered = filter_news_urls(collected)
    print(f"\nFiltered {len(filtered)} news-related URLs:")
    for url in filtered:
        print(" ->", url)
