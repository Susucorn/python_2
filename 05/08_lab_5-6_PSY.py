'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복문 while --
        사용자로부터 암호를 입력받아 로그인 하는 프로그램
        - 사용자로부터 계속해서 암호를 입력 받음
        - 암호가 맞다면 "로그인 성공" 메세지 출력, 암호가 맞을 때까지 반복하기 (암호는 1234)
'''

pw = ""

while pw != "1234":                         # pw 변수가 1234가 아니면 계속 반복
    pw = input("암호를 입력하세요 : ")       # pw 변수에 사용자로부터 무한으로 입력받음, pw가 1234가 될때까지

print("로그인 성공")                        # pw == "1234" 가 되면 출력됨