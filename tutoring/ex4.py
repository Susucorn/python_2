'''
    사용자로부터 어떤 문자열을 입력받고, 입력된 문자열을 역순으로 출력하는 함수를 정의한 후
        함수를 호출하여 결과를 출력하는 프로그램

    1. 함수 정의
    2. 문자열 입력받기
    3. 함수 호출
'''   
def rev_str(input_string):
    re_str = input_string[::-1]
    return re_str

user_input = input("문자열을 입력하세요: ")     # 입력받는 값은 문자열

rev_input = rev_str(user_input)
print("문자열 역순 출력 : ", rev_input)         # 함수 호출하여 문자열 역순 출력
