# 抓取PTT八卦版的網頁原始碼（HTML）
import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 建立一個request物件，附加Request Headers的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "cookie": "over18=1"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析原始碼，取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)
