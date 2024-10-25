def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # 좌측 공백 출력
        print(' ' * (rows - i) * 2, end='')
        # 증가하는 숫자 출력
        for j in range(1, i + 1):
            print(f"{j} ", end=' ')
        # 감소하는 숫자 출력
        for j in range(i - 1, 0, -1):
            print(f"{j} ", end=' ')
        print()

if __name__ == "__main__":
    try:
        rows = int(input("몇 층의 피라미드를 원하시나요? "))
        print_number_pyramid(rows)
    except ValueError:
        print("유효한 숫자를 입력해주세요.")