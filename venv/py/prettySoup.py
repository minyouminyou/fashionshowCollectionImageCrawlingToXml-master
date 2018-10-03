from bs4 import BeautifulSoup
import requests

req = requests.get("http://runway.vogue.co.kr/2018/02/21/ready-to-wear-2018-fw-gucci/#0")

html = req.text

header = req.headers

status = req.status_code

is_ok = req.ok

soup = BeautifulSoup(html,'html.parser')

for a in soup.select("img"):
    print(a)