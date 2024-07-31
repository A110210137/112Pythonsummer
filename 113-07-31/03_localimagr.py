import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'
P['message'] = '本機圖片'
#F['imageFile'] = open(r'C:\Users\m303\Pictures\33.jpg', 'rb')
#F['imageFile'] = open('./pictures/vans.jpg', 'rb')
F['imageFile'] = open('fsd.jpg', 'rb')
requests.post(URL, headers=H, params=P, files=F)