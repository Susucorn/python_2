'''
    2023.10.11
    202395016 컴퓨터공학부 박수연

    -- def 함수 호출 --
'''
print(":: def 예약어를 이용하여 함수 작성하고 호출하기 ::")
print()
# 함수 선언
def address() :                 # def 함수이름(매개변수)
    print("부산시 사상구")
    print("괘법동 산 1-1번지")
    print("신라대학교 국제교육관 552호")
    
# 함수 호출
address()   # 이름이 address인 함수를 호출함
address()   # 함수를 n번 호출한 만큼 n번 실행함

print()

'''
    함수에 값을 넘겨주고 일을 시킨다.
    인자와 매개변수
'''
print(":: 인자와 매개변수 ::")
print()
# 함수 선언
def welcome(name) :   # name은 매개변수 - 전달받은 값을 저장 할 변수.
    print(name,"님 안녕하세요.")
    print(f"{name}님 안녕하세요.")
    print("{}님 안녕하세요." .format(name))

# 함수 호출    
welcome("박수연") # 이름을 가지고 호출한다. 이름을 전달한다.
welcome("홍길동") # (name) 매개변수 자리에 값을 전달함