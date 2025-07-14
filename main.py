import sys
import os
from urllib.parse import urlparse

from reddit_scraper import scrape_user_content
from persona_builder import generate_persona


def extract_username(profile_url):
    return urlparse(profile_url).path.split('/')[-2]


def save_persona(username, persona_text):
    os.makedirs("personas", exist_ok=True)
    with open(f"personas/{username}.txt", "w", encoding="utf-8") as f:
        f.write(persona_text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_user_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username(profile_url)
    print(f"[INFO] Scraping data for: {username}")

    posts, comments = scrape_user_content(username)
    print(f"[INFO] Scraped {len(posts)} posts and {len(comments)} comments.")

    persona = generate_persona(posts, comments)
    save_persona(username, persona)
    print(f"[SUCCESS] Persona saved to personas/{username}.txt")


if __name__ == "__main__":
    main()
