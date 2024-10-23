import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name="electronics.db"):
        # 데이터베이스 연결 및 테이블 생성
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # 테이블이 없으면 생성
        query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_name, price):
        # 제품을 데이터베이스에 삽입
        query = "INSERT INTO products (product_name, price) VALUES (?, ?);"
        self.conn.execute(query, (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        # 제품 정보를 업데이트
        query = "UPDATE products SET "
        params = []
        if product_name:
            query += "product_name = ?, "
            params.append(product_name)
        if price is not None:
            query += "price = ?, "
            params.append(price)
        query = query.rstrip(", ")  # 마지막 쉼표 제거
        query += " WHERE product_id = ?;"
        params.append(product_id)
        self.conn.execute(query, params)
        self.conn.commit()

    def delete_product(self, product_id):
        # 제품을 데이터베이스에서 삭제
        query = "DELETE FROM products WHERE product_id = ?;"
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        # 특정 제품을 조회
        query = "SELECT * FROM products WHERE product_id = ?;"
        cursor = self.conn.execute(query, (product_id,))
        return cursor.fetchone()

    def select_all_products(self):
        # 모든 제품을 조회
        query = "SELECT * FROM products;"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        # 데이터베이스 연결을 종료
        self.conn.close()

# 100개의 샘플 데이터 생성
def generate_sample_data(db):
    product_names = ["Smartphone", "Laptop", "Tablet", "Smartwatch", "Camera",
                     "Headphones", "Monitor", "Keyboard", "Mouse", "Printer"]
    for i in range(100):
        product_name = random.choice(product_names) + f" {i+1}"
        price = round(random.uniform(100, 2000), 2)  # 100 ~ 2000 사이의 랜덤 가격
        db.insert_product(product_name, price)

# 사용 예시
if __name__ == "__main__":
    # 데이터베이스 초기화
    db = ElectronicsDatabase()

    # 100개의 샘플 데이터 삽입
    generate_sample_data(db)

    # 모든 제품 조회
    all_products = db.select_all_products()
    for product in all_products:
        print(product)

    # 제품 업데이트 예시
    db.update_product(1, product_name="Updated Product", price=999.99)

    # 특정 제품 조회
    product = db.select_product(1)
    print("Updated Product:", product)

    # 제품 삭제 예시
    db.delete_product(2)

    # 모든 제품 조회 (삭제 후)
    all_products = db.select_all_products()
    for product in all_products:
        print(product)

    # 데이터베이스 연결 종료
    db.close()
