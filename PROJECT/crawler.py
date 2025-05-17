import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import is_relevant_url

def crawl_site(seed_url, max_pages=10):
    visited = set()
    to_visit = [seed_url]
    collected = []

    while to_visit and len(collected) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            visited.add(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if full_url.startswith(seed_url) and full_url not in visited:
                    to_visit.append(full_url)
                    if is_relevant_url(full_url):
                        collected.append(full_url)

        except Exception:
            continue
    return collected
