import time
import csv
from datetime import datetime
from crawler import crawl_site
from analyzer import get_page_text, analyze_sentiment
from logger import log_sweep_result
from utils import detect_language, extract_title, classify_article_type

seed_sites = [
    "https://www.bbc.com/news",
    "https://www.cnn.com",
    "https://www.nytimes.com",
    "https://www.foxnews.com",
    "https://www.nbcnews.com",
    "https://www.washingtonpost.com",
    "https://www.cbsnews.com",
    "https://www.economist.com",
]

def run_enhanced_sweep():
    all_scores = []
    site_sentiments = {}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("detailed_results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "site", "url", "title", "type", "length", "language", "score"])

        for site in seed_sites:
            start = time.time()
            pages = crawl_site(site, max_pages=10)
            scores = []

            for url in pages:
                text = get_page_text(url)
                if not text:
                    continue

                title = extract_title(text)
                article_type = classify_article_type(title + " " + text[:300])
                content_length = len(text.split())
                language = detect_language(text)
                score = analyze_sentiment(text)

                scores.append(score)
                all_scores.append(score)

                writer.writerow([timestamp, site, url, title, article_type, content_length, language, score])

            avg_score = sum(scores) / len(scores) if scores else None
            site_sentiments[site] = avg_score
            duration = time.time() - start
            print(f"{site} — {len(pages)} articles in {duration:.2f}s, avg score: {avg_score}")

    overall_avg = sum(all_scores) / len(all_scores) if all_scores else 0
    log_sweep_result(site_sentiments, overall_avg)
    print("Overall sentiment average:", overall_avg)

if __name__ == "__main__":
    run_enhanced_sweep()
