import requests

resp = requests.get("https://uvu.edu")
print(resp)
print(resp.text)