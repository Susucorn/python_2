'''
    두 정수를 입력으로 받아 두 숫자를 더하는 함수를 정의한 후,
        그 함수를 호출하여 두 숫자를 더한 결과를 출력하는 프로그램

    1. 함수 정의 - 매개변수로부터 입력받은 값으로 식을 수행한다
    2. 사용자로부터 정수 입력받기
    3. 함수 호출
'''
def addition(a, b):                        # 이름이 addition 이라는 함수를 정의함, (a, b)는 매개변수이며 각각 num1, num2 값이 들어감
    result = a + b                         # result 변수에 매개변수로 입력받은 값을 덧셈한 후 저장
    return result                          # 결과 값을 리턴한다

num1 = int(input("첫번째 정수 입력 : "))    # 첫번째 정수 입력받기
num2 = int(input("두번째 정수 입력 : "))    # 두번째 정수 입력받기

plus = addition(num1, num2)                # 매개변수 num1, num2 (입력받은 값을 addition 함수를 호출하여 각각 매개변수(a, b)에 넘겨준다)
print(f"{num1} + {num2} = {plus} 입니다.")  # 결과 출력