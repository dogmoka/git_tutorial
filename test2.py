import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=1310046")
print(res.status_code)
print(res.text)
