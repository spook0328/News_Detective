import tkinter as tk

news = [
    "Boom Cafe",
    "Weak Wifi",
    "Testing",
    "Practice python GUI"
]


window = tk.Tk()
window.title("Python 資料串接到GUI")
window.geometry("600x400")

label = tk.Label(
    window,
    text=("串接資料使用")
)
label.pack(pady=10)

entry = tk.Entry(
    window,
    text=("Enter")
)

entry.pack(pady=10)

#.strip()：去掉文字前後多餘的空白。
def search():
    keyword = entry.get().strip()
    result = []

    for title in news:
        if keyword.lower() in title.lower():
            result.append(title)

    #delete()：刪除指定範圍的文字。, "1.0"：從第 1 行、第 0 個字元開始。, tk.END直到文字區域的結尾。
    result_box.delete("1.0", tk.END)

    if keyword == "":
        result_box.insert(tk.END, "請輸入關鍵字")

    elif len(result) ==0:
        result_box.insert(tk.END, "N/A")
        print(f"{keyword}")  

    else:
        result_box.insert(tk.END, f"一共找到{len(result)}條新聞：\n")
        print(f"{keyword}")    

    for title in result:
        result_box.insert(tk.END,f"---{title}")
        

#btn
button = tk.Button(
    window,
    text=("Enter"),
    command=search
)
button.pack(pady=5)

#result_box
result_box = tk.Text(window, width=55, height=12)
result_box.pack(pady=10)


window.mainloop()