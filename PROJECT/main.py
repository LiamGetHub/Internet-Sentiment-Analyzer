from crawler import crawl_site
from analyzer import get_page_text, analyze_sentiment
from logger import log_sweep_result

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

def run_sweep():
    site_sentiments = {}
    all_scores = []

    for site in seed_sites:
        pages = crawl_site(site, max_pages=10)
        print(f"Crawled {len(pages)} relevant pages from {site}")
        scores = []
        for url in pages:
            text = get_page_text(url)
            if text:
                score = analyze_sentiment(text)
                scores.append(score)
                all_scores.append(score)
        if scores:
            site_sentiments[site] = sum(scores) / len(scores)
        else:
            site_sentiments[site] = None

    overall_avg = sum(all_scores) / len(all_scores) if all_scores else 0
    print("Site Scores:", site_sentiments)
    print("Overall Avg Sentiment:", overall_avg)
    log_sweep_result(site_sentiments, overall_avg)

if __name__ == "__main__":
    run_sweep()
