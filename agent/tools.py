from duckduckgo_search import DDGS
import re


TRUSTED_KEYWORDS = [
    "aws", "amazon", "ec2", "lambda", "s3",
    "gcp", "google cloud", "compute engine",
    "cloud storage", "free tier", "pricing"
]

def is_english(text: str) -> bool:
    try:
        text.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def normalize_query(query: str) -> str:
    query = query.replace('"', "")
    keywords = [k for k in TRUSTED_KEYWORDS if k in query.lower()]
    return " ".join(keywords) if len(keywords) >= 3 else query[:100]


def web_search(query: str, max_results=5):
    results = []
    clean_query = normalize_query(query)

    with DDGS() as ddgs:
        for r in ddgs.text(clean_query, max_results=max_results):
            body = r.get("body", "")
            if not body:
                continue

            
            if not is_english(body[:80]):
                continue

        
            if not any(k in body.lower() for k in TRUSTED_KEYWORDS):
                continue

            results.append(body)

    return results
