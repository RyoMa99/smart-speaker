from email import message
import requests
from bs4 import BeautifulSoup

# 都営浅草線のURL
URL = "https://transit.yahoo.co.jp/diainfo/128/0"

# HTMLの取得
res = requests.get(URL)

# BeautifulSoupでの解析
soup = BeautifulSoup(res.text,"html.parser")

if soup.find("dd",class_="trouble"):
  message = "遅延しています"
elif soup.find("dd",class_="normal"):
  message = "遅延はありません"
else:
  message = "問題が発生しました"

print(message)