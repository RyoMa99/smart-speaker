import json
import requests
from bs4 import BeautifulSoup

# 都営浅草線のURL
URL = "https://transit.yahoo.co.jp/diainfo/128/0"

# HTMLの取得
res = requests.get(URL)

# BeautifulSoupオブジェクトの生成
soup = BeautifulSoup(res.text,"html.parser")

message = {
  "title": "",
  "content": "",
}

if soup.find("dd",class_="trouble"):
  title = soup.find("dd",class_="trouble").previous_sibling
  title.find("span").extract()
  message["title"] = title.get_text()

  message["content"] = soup.find("dd",class_="trouble").get_text()

elif soup.find("dd",class_="normal"):
  title = soup.find("dd",class_="normal").previous_sibling
  title.find("span").extract()
  message["title"] = title.get_text()
  
  message["content"] = soup.find("dd",class_="normal").get_text()
else:
  message["title"] = "問題が発生しました"

print(json.dumps(message,ensure_ascii=False))