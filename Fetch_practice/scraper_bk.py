#from import 套件 
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config_bk import BASE_URL

#網頁下載
#儲存伺服器回傳的回應物件。
def get_news():
    response =requests.get(
        BASE_URL,
        timeout=15
    )
#回傳 HTTP 錯誤狀態
    response.raise_for_status()

#你可以把 soup 想成一份可以用 Python 搜尋的 HTML 結構，而不是單純的一大段文字。
    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    article = []
#找出書籍：select() 使用 CSS 選擇器尋找所有符合條件的 HTML 元素。
# select_one()
    for item in soup.select("article.product_pod"):
        #表示在h3 字體裡面找尋a連結標籤的
        link_tag = item.select_one("h3 a")

        if link_tag is None:
            continue
#整理資料：字典與 append()
        title = link_tag.get("title","").strip()

        article_url= urljoin(
            BASE_URL,
            link_tag.get("href","")
        )
#每本書的標題和網址存入字典，再加入 articles 列表。
        if title:
            article.append({
                "title":title,
                "url":article_url
            })
    return article

#真正抓取前，可以先用python3 -c "from scraper import get_news; print(get_news()[:3])"測試