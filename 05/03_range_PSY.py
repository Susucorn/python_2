'''
    2023.09.27
    202395016 컴퓨터공학부 박수연
    
    -- range() 함수 --
    range(시작값, 숫자 앞까지, 증가값/감소값)
    C언어 -> for(초깃값; 조건식; 증감식)
'''
for i in range(3):          # 0~2까지의 값이 i 변수에 저장됨
    print(i, end='. ')      # end='' --> 줄 바꿈 하지 않고 옆으로 연결, ' ' 안에 있는 것으로 연결함
    print("안녕하세요.")
    print("   박수연 입니다.")

print()

# 1부터 5까지 출력하기
for i in range(1,6):        # 기본으로 1씩 증가하기 때문에 증가값 1은 생략가능
    print(i, end=' ')

print()                 

# 10 ~ 1 까지 출력하기
for i in range(10, 0, -1):  # 감소값은 적어줘야 함
    print(i, end=' ')