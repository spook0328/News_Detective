#練習使用GUI 創建介面
import tkinter as tk
#建立視窗 Tk()是一個class 做obb用的
window = tk.Tk()
# Title
window.title("GUI UI practice ")
# 設定視窗大小
window.geometry("600x400")


#Label：在視窗中顯示提示文字。, 下面的window是在說明label在哪一個視窗上。

label = tk.Label(
    window,
    text="Enter the key words you want to search"
)
#將文字標籤放進Window
label.pack(pady=10)

#建立輸入匡 Entry：讓使用者輸入文字。
entry = tk.Entry(
    window
)
#將收尋匡標籤放進Window
entry.pack()

#定義搜尋, config()=設定的意思
def search():
    keyword = entry.get()
    result_labbel.config(text=f"輸入的關鍵字是{keyword}")

#Button
button = tk.Button(
    window,
    text="subbmit",
    command=search
)
button.pack(pady=10)

#result
result_labbel = tk.Label(
    window,
    text = "輸入的keywords顯示"
)
result_labbel.pack(pady=10)
#顯示視窗並等待使用者操作
window.mainloop()