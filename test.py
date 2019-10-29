import os
import requests

# url = 'http://127.0.0.1:8000/api/v1/1/'
url = "http://127.0.0.1:8000"
resp = requests.get(url)
# assert resp.status_code == 403

# api_key = 'xbgLK0wM.NE4gL4BLFBRX7ZUkhCH0ziMT1lK6R3m5'
# auth = f"Api-Key {api_key}"
api_key = "02d9ffbb74331650d2f57503704fe43d21762132"
auth = f"Token {api_key}"

resp = requests.get(url, headers={"Authorization": auth})
# assert resp.status_code == 200

print(resp.json())
# print(resp)

# curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
