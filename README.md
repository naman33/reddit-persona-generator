# Reddit Persona Generator

This is a command-line tool that scrapes a Reddit user's posts and comments, then uses a language model to generate a detailed persona profile.

---

## 🚀 Features

- Scrapes latest Reddit posts & comments from a user
- Uses LLMs via OpenRouter to generate personality summaries
- Outputs a persona report with psychological and interest-based insights
- Simple CLI interface

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
```
2. **Install Required Packages**
Make sure Python 3.8+ is installed, then run:
pip install -r requirements.txt

3. **Set Up OpenRouter API Key**
Create a .env file in the root directory:
OPENROUTER_API_KEY=your_openrouter_api_key_here

▶️ Run the Script
Example usage:
python main.py https://www.reddit.com/user/kojied/

•This will scrape the given user's recent posts and comments
•It then generates a persona and saves it to:
