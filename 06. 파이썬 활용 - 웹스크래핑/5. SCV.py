import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
filename = "시가총액 {}.csv".format(datetime.today().strftime("%Y%m%d"))
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)
for i in range(1, 5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page={}".format(i)
    res =requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows=soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns=row.find_all("td")
        if len(columns) <=1:
            continue
        data = [column.get_text().strip() for column in columns] #strip() 불필요 항목 제거
        #print(data)

        writer.writerow(data)


    