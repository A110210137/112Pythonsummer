import tkinter as tk
from tkinter import messagebox
import requests

# 发送消息的函数
def send_message():
    message = message_entry.get()
    if not message:
        messagebox.showwarning("警告", "请输入要发送的消息")
        return

    URL = 'https://notify-api.line.me/api/notify'
    H = {'Authorization': 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'}
    P = {'message': message}

    try:
        response = requests.post(URL, headers=H, params=P)
        if response.status_code == 200:
            messagebox.showinfo("成功", "消息发送成功")
        else:
            messagebox.showerror("错误", f"发送失败: {response.text}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("错误", f"发生错误: {e}")

# 创建主窗口
root = tk.Tk()
root.title("LINE Notify 消息发送器")

# 创建标签和文本输入框
tk.Label(root, text="请输入要发送的消息:").pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=10)

# 创建发送按钮
send_button = tk.Button(root, text="发送", command=send_message)
send_button.pack(pady=10)

# 运行主循环
root.mainloop()
