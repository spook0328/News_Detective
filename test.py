#測試邏輯部分，跟熟習python 判斷 if, if-else, for, function, print
news = [
    "AI 技術正在改變科技產業",
    "台灣股市今日上漲",
    "人工智慧應用進入醫療領域",
    "全球氣候變遷成為關注焦點",
    "科技公司推出新的 AI 模型"
]

keyword = input("請輸入新聞關鍵字：")

results = [
    item for item in news
    if keyword.lower() in item.lower()
]

if results:
    print(f"\n find {len(results)} news: ")
    for item in results:
        print("-", item)
else:
    print("Not found")