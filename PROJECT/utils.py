from langdetect import detect

def is_relevant_url(url):
    keywords = ["business", "politics", "economy", "world", "news"]
    return any(k in url.lower() for k in keywords)


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def extract_title(text):
    lines = text.splitlines()
    for line in lines:
        if line.strip() and len(line.strip().split()) > 3:
            return line.strip()[:100]
    return "untitled"

def classify_article_type(text):
    lowered = text.lower()
    if "opinion" in lowered or "editorial" in lowered:
        return "opinion"
    elif "analysis" in lowered:
        return "analysis"
    return "news"
