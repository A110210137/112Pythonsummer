import requests

IMG = 'https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2024/07/31/realtime/30174960.jpg'
URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'
P['message'] = '網路圖片'
F['imageFile'] = requests.get(IMG).content
requests.post(URL, headers=H, params=P, files=F)