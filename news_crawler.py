import requests
from bs4 import BeautifulSoup
import feedparser
from urllib.parse import quote_plus

def get_google_news(keyword):
    encoded_keyword = quote_plus(keyword)
    url = f"https://news.google.com/rss/search?q={encoded_keyword}+when:3d&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries[:10]]

def get_macro_news():
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        res = requests.get('https://www.cnbc.com/world/?region=world', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        return [tag.text.strip() for tag in soup.select('a.Card-title')][:10]
    except Exception as e:
        print(f"❌ Fail to get macro news: {e}")
        return []

def get_finviz_news(ticker):
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find('table', class_='fullview-news-outer')
        rows = table.find_all('tr') if table else []
        return [row.find_all('td')[1].text.strip() for row in rows[:10]]
    except Exception as e:
        print(f"❌ Fail to get news from Finviz: {e}")
        return []

def get_financial_news(ticker, company_name=None):
    if company_name is None:
        company_name = ticker
    query = f"{company_name} OR {ticker} stock"
    company_news = get_google_news(query)
    company_news += get_finviz_news(ticker)
    macro_news = get_macro_news()
    print(f"Fetched {len(company_news)} pieces of [{ticker} company news] and {len(macro_news)} pieces of [macro news]")
    return "\n".join(company_news + macro_news)