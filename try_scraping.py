import requests

from src.scraping import HTMLPageParser

response = requests.get("https://news.ycombinator.com/", timeout=10)

parser = HTMLPageParser()
soup = parser.parse(response.text)

titles = parser.find_all_items(soup, "span", "titleline")
for i, item in enumerate(titles[:5], 1):
    link = item.find("a")
    if link:
        print(f"{i}. {link.text}")
