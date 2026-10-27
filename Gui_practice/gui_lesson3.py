# tk.Listbox：顯示可選取的項目清單。
# .curselection()：取得使用者目前選取的項目索引。
# .bind("<Double-Button-1>", show_title)：使用滑鼠雙擊事件觸發函式。

import tkinter as tk
from tkinter import messagebox

#News data
news = [
    "2026,10,26",
    "Toronto election",
    "TPL",
    "TPL card renew"
]

# Window GUI setup
window = tk.Tk()
window.title ("Gui Lesson3")
window.geometry("550x420")

#Search bar
label = tk.Label(window, text="請輸入搜尋關鍵字：")
label.pack(pady=5)

entry = tk.Entry(window, width="40")
entry.pack(pady=5)

#Search bar status
status_label = tk.Label(window, text="請輸入關鍵字並搜尋")
status_label.pack(pady=5)

#News listbox
result_listbox = tk.Listbox(window, width=65, height=12)
result_listbox.pack(pady=5)

#Search method
def search():
    keyword = entry.get().strip()
    #清除之前的紀錄
    result_listbox.delete(0, tk.END)

    if keyword == "":
        status_label.config(text="請輸入想查詢內容")
        return

    result = []

    for title in news:
        if keyword.lower() in title.lower():
            result.append(title)

    if len(result) ==0:
        status_label.config(text="查無此資料")
    else:
        status_label.config(text=f"一共找到{len(result)}筆資料")   

        for title in result:
            result_listbox.insert(tk.END, title)

#雙擊新聞標題時執行
def show_title(event):
    selected = result_listbox.curselection()

    if selected:
        title = result_listbox.get(selected[0])
        messagebox.showinfo("新聞標題",title)

#btn
button = tk.Button(window, text="submit", command=search)
button.pack(pady=5)

#綁定雙擊事件
result_listbox.bind("<Double-Button-1>",show_title)

window.mainloop()