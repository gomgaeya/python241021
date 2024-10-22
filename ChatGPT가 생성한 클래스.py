# Person 클래스 정의
class Person:
    def __init__(self, id, name):
        # 생성자: id와 name 멤버 변수를 초기화
        self.id = id
        self.name = name

    def printInfo(self):
        # Person 클래스의 정보를 출력하는 메서드
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 정의 (Person 클래스 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        # 부모 클래스(Person)의 생성자 호출
        super().__init__(id, name)
        # title 멤버 변수 추가
        self.title = title

    def printInfo(self):
        # Manager 클래스의 정보를 출력하는 메서드
        # 부모 클래스의 printInfo()와 달리 title 정보도 출력
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# Employee 클래스 정의 (Person 클래스 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        # 부모 클래스(Person)의 생성자 호출
        super().__init__(id, name)
        # skill 멤버 변수 추가
        self.skill = skill

    def printInfo(self):
        # Employee 클래스의 정보를 출력하는 메서드
        # 부모 클래스의 printInfo()와 달리 skill 정보도 출력
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # 1. Person 클래스 인스턴스 생성 및 정보 출력 테스트
    # person1 객체를 생성하고, printInfo() 메서드 호출
    person1 = Person(1, "Alice")
    person1.printInfo()  # 출력: ID: 1, Name: Alice

    # 2. Person 클래스 다른 인스턴스 생성
    # person2 객체를 생성하고, printInfo() 메서드 호출
    person2 = Person(2, "Bob")
    person2.printInfo()  # 출력: ID: 2, Name: Bob

    # 3. Manager 클래스 인스턴스 생성 및 정보 출력 테스트
    # manager1 객체를 생성하고, printInfo() 메서드 호출
    manager1 = Manager(3, "Charlie", "CTO")
    manager1.printInfo()  # 출력: ID: 3, Name: Charlie, Title: CTO

    # 4. Manager 클래스 다른 인스턴스 생성
    # manager2 객체를 생성하고, printInfo() 메서드 호출
    manager2 = Manager(4, "David", "CFO")
    manager2.printInfo()  # 출력: ID: 4, Name: David, Title: CFO

    # 5. Employee 클래스 인스턴스 생성 및 정보 출력 테스트
    # employee1 객체를 생성하고, printInfo() 메서드 호출
    employee1 = Employee(5, "Eve", "Python")
    employee1.printInfo()  # 출력: ID: 5, Name: Eve, Skill: Python

    # 6. Employee 클래스 다른 인스턴스 생성
    # employee2 객체를 생성하고, printInfo() 메서드 호출
    employee2 = Employee(6, "Frank", "Java")
    employee2.printInfo()  # 출력: ID: 6, Name: Frank, Skill: Java

    # 7. Manager 클래스의 title 변경 후 출력
    # manager1 객체의 title을 변경하고, printInfo() 메서드 호출
    manager1.title = "CEO"
    manager1.printInfo()  # 출력: ID: 3, Name: Charlie, Title: CEO

    # 8. Employee 클래스의 skill 변경 후 출력
    # employee1 객체의 skill을 변경하고, printInfo() 메서드 호출
    employee1.skill = "JavaScript"
    employee1.printInfo()  # 출력: ID: 5, Name: Eve, Skill: JavaScript

    # 9. Person 인스턴스에서 id 변경 후 출력
    # person1 객체의 id를 변경하고, printInfo() 메서드 호출
    person1.id = 10
    person1.printInfo()  # 출력: ID: 10, Name: Alice

    # 10. Manager 인스턴스의 name 변경 후 출력
    # manager2 객체의 name을 변경하고, printInfo() 메서드 호출
    manager2.name = "Daniel"
    manager2.printInfo()  # 출력: ID: 4, Name: Daniel, Title: CFO

# 테스트 실행
test_classes()
