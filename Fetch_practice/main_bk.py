from scraper_bk import get_news

def search_news(news, keyword):
    result = []

    for article in news:
        title = article["title"]

        if keyword.casefold() in title.casefold():
            result.append(article)

    return result

def main():
    print("====Web keyword serarch===")

    news = get_news()

    print(f"成功取得{len(news)}筆資料")
    keyword = input("請輸入收尋關鍵字：").strip()

    if not keyword:
        print("Ｎ／Ａ")
        return

    result = search_news(news,keyword)

    print(f"\n找到 {len(result)}結果")

    for article in result:
        print(f"- {article['title']}")
        print(f"- 網址{article['url']}")

if __name__ == "__main__":
    main()