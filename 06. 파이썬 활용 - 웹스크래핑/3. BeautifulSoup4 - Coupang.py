import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
for i in range(1, 6):
    print("||||||||{} page정보|||||||||| \n".format(i))
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("dl", attrs={"class": re.compile("^search-product")})
    for item in items:
        name = item.find("div", attrs={"class": "name"})
        if name:
            pass
            # print(name.get_text())

    for item in items:

        ad_remove=item.find("span", attrs={"class":"ad-badge-text"})
        if ad_remove:
            # print(" <광고 상품은 제외합니다> \n ====================================================")
            continue
        

        name = item.find("div", attrs={"class":"name"}).get_text() #이름 
        #MSI 제외
        if "MSI" in name:
            # print(" <MSI 상품은 제외합니다> \n ====================================================")
            continue

        price = item.find("strong", attrs={"class":"price-value"}) #가격
        if price: 
            price=price.get_text()
        else:
            continue
        rate = item.find("em", attrs={"class":"rating"}) #평점
        if rate: #평점이 없는 제품이 있을 수 있음
            rate=rate.get_text()
        else:
            # print(" <평점 없는 상품은 제외합니다>\n ====================================================")
            continue
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count: # 리뷰가 없는 제품이 있을 수 있음
            rate_count=rate_count.get_text()
            rate_count = rate_count[1:-1] #괄호가 출력되기 때문에 괄호를 제거해줌
        else:
            # print(" <리뷰 없는 상품은 제외합니다> \n ====================================================")
            continue

        
        #name_element = item.find("a", attrs={"class":"search-product-link"})["href"]
        #if name_element:
        #    name = name_element.get_text()
        #    link = "https://www.coupang.com{}".format(name)
        #else:
        #    continue -- # 링크따오는 거지만 오류로 못따옴


        if float(rate) >= float(4.5) and int(rate_count) > 50:
            print("이름: ", name, "\n 가격: ", price, "\n 평점: ", rate, "\n 리뷰 수: ", rate_count, "\n ====================================================")
            