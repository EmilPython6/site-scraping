import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
page = response.text

texts = []
links = []
upvotes = []

soup = BeautifulSoup(page, "html.parser")
article_text = soup.find_all(name="a", class_="storylink")
for article in article_text:
    texts.append(article.text)
    article_link = article.get("href")
    links.append(article_link)

for vote in soup.find_all(class_="score"):
    upvotes.append(int(vote.text.split()[0]))

max_upvotes_index = upvotes.index(max(upvotes))
print(texts[max_upvotes_index])
print(links[max_upvotes_index])
print(upvotes[max_upvotes_index])
