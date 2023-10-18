'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복문 while로 사용자가 입력하는 숫자의 합을 계산하는 프로그램 --
        - yes 일때까지 무한반복하기
        - 사용자로부터 정수를 입력받음
        - 합계를 저장함
        - 반복을 멈출때 합계 출력

    필요한 변수?
        - "yes"를 담을 변수 (answer), 입력받을 변수 (num), 합계를 담을 변수 (sum)
'''
answer = "yes"          # 변수에 문자열 저장
sum = 0                 # 합계를 저장할 변수, 0으로 초기화

while answer == "yes":                                 # answer 변수가 yes일때까지 무한반복
    num = int(input("숫자를 입력하세요 : "))            # 입력받는 값은 정수형
    answer = input("계속 하시겠습니까? (yes/no) : ")    # 입력받는 값은 문자열
    sum = sum+num                                      # 합계를 저장
    # 합계를 출력할 조건
    if answer == "no":             # 사용자로부터 입력받은 값이 no 일때
        print("합계는 : ", sum)     # 합계 출력