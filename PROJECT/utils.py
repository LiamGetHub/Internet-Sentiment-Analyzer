def is_relevant_url(url):
    keywords = ["business", "politics", "economy", "world", "news"]
    return any(k in url.lower() for k in keywords)
