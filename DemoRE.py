import re

# 이메일 주소를 검사하는 함수
def is_valid_email(email):
    # 정규표현식으로 이메일 주소의 규칙을 정의해요.
    # ^: 문자열의 시작을 의미해요.
    # [a-zA-Z0-9_.+-]: 이메일 앞부분에는 알파벳 대소문자, 숫자, 점(.), 밑줄(_), 더하기(+), 빼기(-)가 나올 수 있어요.
    # +: 위의 글자들이 여러 번 반복될 수 있어요.
    # @: 이메일 주소에는 꼭 골뱅이(@)가 들어가야 해요.
    # [a-zA-Z0-9-]: 골뱅이 뒤에는 알파벳 대소문자, 숫자, 빼기(-)가 들어가요.
    # +: 위의 글자들이 여러 번 반복될 수 있어요.
    # \.: 점(.)은 반드시 하나가 있어야 해요. 점은 특수문자라서 \를 앞에 붙여줘야 해요.
    # [a-zA-Z0-9-.]: 점 뒤에는 알파벳 대소문자, 숫자, 점(.), 빼기(-)가 나올 수 있어요.
    # $: 문자열이 여기서 끝나야 해요.
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.match 함수로 이메일이 위의 패턴에 맞는지 확인해요.
    return re.match(pattern, email) is not None

# 이메일 주소의 샘플을 10개 준비했어요.
emails = [
    "example1@gmail.com",           # 정상적인 이메일
    "valid.email+alias@domain.com", # + 기호와 별명 사용한 이메일
    "user_name@sub.domain.org",     # 밑줄과 서브 도메인을 사용한 이메일
    "invalid-email@domain",         # .(점)이 빠져서 잘못된 이메일
    "noatsign.com",                 # @이 빠져서 잘못된 이메일
    "wrong@domain..com",            # 점(.)이 두 번 연속 사용되어 잘못된 이메일
    "good.email@domain.co.kr",      # 한국 도메인을 사용하는 정상적인 이메일
    "user@domain-with-dash.com",    # 빼기(-)를 포함한 정상적인 이메일
    "name@domain123.com",           # 숫자를 포함한 정상적인 이메일
    "user@domain@domain.com"        # @이 두 번 들어간 잘못된 이메일
]

# 각 이메일을 검사하고 결과를 출력해요.
for email in emails:
    # 이메일이 유효하면(True) "유효한 이메일입니다"라고 출력하고, 아니면(False) "유효하지 않은 이메일입니다"라고 출력해요.
    if is_valid_email(email):
        print(f"'{email}'은(는) 유효한 이메일 주소입니다.")
    else:
        print(f"'{email}'은(는) 유효하지 않은 이메일 주소입니다.")
