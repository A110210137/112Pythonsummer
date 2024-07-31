import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer wJILf24pASjz8QSzoVAmf3nGngrgYCOf4joauiUaz0h'
P['message'] = '群組網路圖片'
#F['imageFile'] = open(r'C:\Users\m303\Pictures\33.jpg', 'rb')
#F['imageFile'] = open('./pictures/vans.jpg', 'rb')
F['imageFile'] = open('fsd.jpg', 'rb')
requests.post(URL, headers=H, params=P, files=F)