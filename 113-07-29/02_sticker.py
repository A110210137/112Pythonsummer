import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Authorization'] = 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'
P['message'] = '貼圖測試'
P['stickerPackageId'] = 6136
P['stickerId'] =10551376
response = requests.post(URL, headers=H, params=P)

print(response.status_code)
print(response.text)