import openpyxl
import random
import string

# 워크북 및 워크시트 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "제품 판매 데이터"

# 헤더 작성
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 제품명 예시 리스트
product_names = [
    "노트북", "스마트폰", "태블릿", "헤드폰", "스피커",
    "키보드", "마우스", "모니터", "프린터", "웹캠"
]

for i in range(1, 101):
    # 제품ID 생성 (예: P0001 ~ P0100)
    product_id = f"P{str(i).zfill(4)}"
    
    # 제품명 랜덤 선택
    product_name = random.choice(product_names)
    
    # 수량 랜덤 선택 (1~100)
    quantity = random.randint(1, 100)
    
    # 가격 랜덤 선택 (10,000 ~ 100,000)
    price = random.randint(10000, 100000)
    
    # 데이터 추가
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")