'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 심화문제 5-2 --
        1~ 100까지의 정수 중 두 수를 입력 받아 
            두 수 사이의 합계 출력하기
            두 수 사이의 짝수의 합계 출력하기
'''
sum1 = 0    # 두 수 사이의 합계를 저장할 변수
sum2 = 0    # 두 수 사이의 짝수의 합계를 저장할 변수
num1 = int(input("첫 번째 정수를 입력하세요 : "))   # 입력받는 값은 정수, num1에 저장
num2 = int(input("두 번째 정수를 입력하세요 : "))   # 입력받는 값은 정수, num2에 저장


for i in range(num1, num2+1):                   # 범위는 num1부터 num2까지
    sum1 = sum1+i                                    # 짝수의 합계 저장
print("두 수 사이의 합계는 : ", sum1)

if num1 > num2:              # num1 이 num2 보다 작으면
    num1, num2 = num2, num1  # 두 수를 작은 수가 num1에 오도록 교체
    
for i in range(num1, num2+1):          # 범위는 num2부터 num1까지 2씩 증가
    if i % 2 == 0:
        sum2 = sum2+i  
print("두 수 사이의 짝수 합은 : ", sum2)