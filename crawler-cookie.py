# 抓取PTT八卦版的網頁原始碼（HTML）
import bs4
import urllib.request as req

# 用一個函式來包裝


def getData(url):
    # 建立一個request物件，附加Request Headers的資訊
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "cookie": "over18=1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章的標題
    root = bs4.BeautifulSoup(data, "html.parser")
    # 抓取每一頁的標題
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    # 抓取上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是‹ 上頁的a標籤
    return nextLink["href"]  # 用return讓這個網址回傳出來


# 呼叫函示
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    # getData(pageURL)會回傳nextLink["href"]，讓他去覆蓋原本的pageURL
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1  # 這樣它會去跑三頁
