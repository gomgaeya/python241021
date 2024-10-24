import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path


class DBManager:
    def __init__(self, db_name="ProductList.db"):
        # DB 연결
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        # DB가 없을 경우 테이블 생성
        if not os.path.exists(db_name):
            self.create_table()

    def create_table(self):
        # 테이블 생성 쿼리
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )

    def add_product(self, name, price):
        # 제품 추가 쿼리
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        # 제품 수정 쿼리
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        # 제품 삭제 쿼리
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def get_all_products(self):
        # 모든 제품 조회 쿼리
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

    def close(self):
        # DB 연결 종료
        self.con.close()


# 디자인 파일 로드
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]


class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # DBManager 인스턴스 생성
        self.db_manager = DBManager()

        # QTableWidget 초기 설정
        self.setup_table()

        # 엔터키 이벤트 설정
        self.setup_signals()

        # UI 버튼 클릭 시그널 연결
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2.clicked.connect(self.updateProduct)
        self.pushButton_3.clicked.connect(self.removeProduct)
        self.pushButton_4.clicked.connect(self.getProduct)

    def setup_table(self):
        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

    def setup_signals(self):
        # 엔터키로 다음 입력 필드로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        # 테이블 더블 클릭 시 제품 정보 불러오기
        self.tableWidget.doubleClicked.connect(self.fill_form_with_selected_row)

    def addProduct(self):
        # 제품 추가
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db_manager.add_product(name, price)
        self.get_products()

    def updateProduct(self):
        # 제품 수정
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db_manager.update_product(prod_id, name, price)
        self.get_products()

    def removeProduct(self):
        # 제품 삭제
        prod_id = self.prodID.text()
        self.db_manager.remove_product(prod_id)
        self.get_products()

    def getProduct(self):
        # 모든 제품 조회
        self.tableWidget.clearContents()
        products = self.db_manager.get_all_products()

        # 테이블에 데이터 삽입
        for row, item in enumerate(products):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))

    def fill_form_with_selected_row(self):
        # 테이블에서 선택된 행의 데이터를 입력 폼에 채움
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

    def closeEvent(self, event):
        # 윈도우 닫을 때 DB 연결 종료
        self.db_manager.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
