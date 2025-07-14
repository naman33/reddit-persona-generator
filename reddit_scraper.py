# reddit_scraper.py

import praw
from dotenv import load_dotenv
import os

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def scrape_user_content(username):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    for submission in user.submissions.new(limit=50):
        posts.append(f"[POST] Title: {submission.title}\nText: {submission.selftext}\nSubreddit: r/{submission.subreddit}")

    comments = []
    for comment in user.comments.new(limit=50):
        comments.append(f"[COMMENT] {comment.body}\nSubreddit: r/{comment.subreddit}")

    return posts, comments
