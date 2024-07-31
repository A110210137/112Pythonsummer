import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# 固定的Token和Message
TOKEN = '你的 LINE Notify Token'
MESSAGE = '這是自動發送的訊息'

def send_line_notify(sticker_package_id=None, sticker_id=None, image_file=None):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {TOKEN}'}
    payload = {'message': MESSAGE}
    files = {}

    if sticker_package_id and sticker_id:
        payload['stickerPackageId'] = sticker_package_id
        payload['stickerId'] = sticker_id
    elif image_file:
        files = {'imageFile': image_file}
    
    response = requests.post(url, headers=headers, data=payload, files=files)
    return response

def on_send():
    choice = option_var.get()
    if choice == "Line Sticker":
        sticker_package_id = sticker_package_id_entry.get().strip()
        sticker_id = sticker_id_entry.get().strip()
        if not sticker_package_id or not sticker_id:
            messagebox.showerror("錯誤", "請輸入Sticker Package ID和Sticker ID")
            return
        response = send_line_notify(sticker_package_id, sticker_id)
    elif choice == "Local Image File":
        file_path = file_path_entry.get().strip()
        if not file_path:
            messagebox.showerror("錯誤", "請輸入本機圖片檔案路徑")
            return
        try:
            with open(file_path, 'rb') as f:
                response = send_line_notify(image_file=f)
        except FileNotFoundError:
            messagebox.showerror("錯誤", "找不到指定的檔案")
            return
    elif choice == "Web Image File":
        img_url = img_url_entry.get().strip()
        if not img_url:
            messagebox.showerror("錯誤", "請輸入網路圖片URL")
            return
        image_data = requests.get(img_url).content
        image_file = ('image.jpg', image_data, 'image/jpeg')
        response = send_line_notify(image_file=image_file)
    
    messagebox.showinfo("結果", f"狀態碼: {response.status_code}\n回應: {response.text}")

def on_option_change(*args):
    choice = option_var.get()
    sticker_frame.pack_forget()
    file_frame.pack_forget()
    url_frame.pack_forget()
    if choice == "Line Sticker":
        sticker_frame.pack()
    elif choice == "Local Image File":
        file_frame.pack()
    elif choice == "Web Image File":
        url_frame.pack()

app = tk.Tk()
app.title("LINE Notify 發送器")

# Token和Message已經固定，不需要再讓用戶輸入
tk.Label(app, text=f"Token: {TOKEN}").pack()
tk.Label(app, text=f"Message: {MESSAGE}").pack()

option_var = tk.StringVar(app)
option_var.set("Line Sticker")  # 設置預設值
option_var.trace("w", on_option_change)

options = ["Line Sticker", "Local Image File", "Web Image File"]
option_menu = tk.OptionMenu(app, option_var, *options)
option_menu.pack()

sticker_frame = tk.Frame(app)
tk.Label(sticker_frame, text="Sticker Package ID:").pack()
sticker_package_id_entry = tk.Entry(sticker_frame, width=50)
sticker_package_id_entry.pack()

tk.Label(sticker_frame, text="Sticker ID:").pack()
sticker_id_entry = tk.Entry(sticker_frame, width=50)
sticker_id_entry.pack()

file_frame = tk.Frame(app)
tk.Label(file_frame, text="本機圖片檔案路徑:").pack()
file_path_entry = tk.Entry(file_frame, width=50)
file_path_entry.pack()
tk.Button(file_frame, text="選擇檔案", command=lambda: file_path_entry.insert(0, filedialog.askopenfilename())).pack()

url_frame = tk.Frame(app)
tk.Label(url_frame, text="網路圖片URL:").pack()
img_url_entry = tk.Entry(url_frame, width=50)
img_url_entry.pack()

tk.Button(app, text="確定", command=on_send).pack()

app.mainloop()
