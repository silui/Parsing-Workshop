from bs4 import BeautifulSoup
import requests
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
all_article = soup.find_all('article')
for article in all_article:
    print(article.h2.get_text())