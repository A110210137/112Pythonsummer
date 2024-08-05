import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-A7E3C0DC-2B4A-4968-88E1-95265C6C6092'
r = requests.get(URL, params=P)     
t = r.json()
print(t)
