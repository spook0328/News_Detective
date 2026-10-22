#串聯全部模組
from scraper import get_news
# import requests
# from bs4 import BeautifulSoup
# import jieba
# import nltk
# from collections import Counter

news = get_news()

keyword = input("你要查詢什麼資料:")

result = []

for title in news:
    if keyword.lower() in title.lower():
        result.append(title)
    

print(f"\n 一共找到{len(result)}則新聞")

for title in result:
    print(f"---", title)