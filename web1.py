#web1.py
#웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#웹페이지를 파싱: "상수값을 지정"
soup = BeautifulSoup(page, "html.parser")

#원하는 데이터 추출
#print(soup.prettify())

#<p> 태그를 전부 추출: <P>태그 中 <>를 안 붙여줘도 인식한다!!
#print(soup.find_all("p"))
#첫번째 <P> 태그 검색
#print(soup.find("p"))

#조건검색: <p class="outer-text"> 태그 추출
#print(soup.find_all("p", class_="outer-text"))
#attrs: 속성 추출: attributes 속성
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#태그 내부 문자열 추출: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

#id로 검색
print(soup.find_all(id="first"))

