'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복문 while --
        단을 입력받아 해당 단의 구구단을 출력하는 프로그램

    문제 분석 - 조건식이 되는 변수는 1로 초기화, 단을 입력받아 변수에 저장함
                조건식이 되는 변수가 9가 될 때까지 반복하여 구구단 출력

    필요한 변수 - 입력받을 단 (dan), 조건식 변수 i
'''
i = 1      # 변수 초기화
dan = int(input("원하는 단을 입력하세요 : "))       # 정수로 입력받기

while i<=9:
    print(f"{dan} * {i} = {dan*i}")
    i += 1