import requests

URL = 'https://notify-api.line.me/api/notify'
H, P = {}, {}
H['Aothorizaion'] = 'Bearer JMcCEGDAdAa6I3WqcK8e3Xj8Ev9QtzFeBr9hHtc6aAv'
P['message'] = '今天是星期五晚上'
requests.post(URL, headers=H, params=P)

