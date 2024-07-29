import requests

URL = 'https://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Aothorizaion'] = 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'
P['message'] = '圖片'
F['imageFile'] = open('fsd.jpg','rb')
requests.post(URL, headers=H, params=P, files=F)
