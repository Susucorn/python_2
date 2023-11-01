'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 함수는 튜플을 돌려줄 수 있다 --

        : 반지름을 입력받아 원의 넓이와 둘레를 계산하는 프로그램
            1) 넓이와 둘레를 계산하는 함수를 작성
            2) 함수는 넓이와 둘레를 함께 리턴한다 (두 개의 결과값을 동시에 돌려준다 - 튜플형식)

        [함수]
            3. 반지름을 받아서 매개변수에 저장한다
            4. 넓이와 둘레를 계산한다
            5. 넓이와 둘레를 돌려준다 (함수를 호출한 곳으로 돌려줌)
                -> return 넓이, 둘레

        [메인]
            1. 키보드로부터 반지름을 입력받기
            2. 함수를 호출하기 -> 반지름을 가지고 호출하기
            6. 돌려받은 넓이와 둘레를 튜플형태로 저장하기
                (넓이, 둘레)
            7. 출력
'''
def circle(r):
    area = r * r *  3.14        # 원의 넓이
    circum = r * 2 * 3.14       # 원의 둘레
    return (area, circum)       # 튜플을 반환함

radius = float(input("원의 반지름을 입력하세요 : "))        # 실수로 입력받기
(a, c) = circle(radius)                                   # 함수를 호출하기 : (a, c)는 전역변수 (area, circum)은 지역변수
print(f"반지름이 {radius}인 원의 넓이는 {a:.2f}이고, 원의 둘레는 {c:.2f} 입니다.")  # 소수 둘째자리까지 표시함

# 변수 두 개를 한 번에 저장하기
circle = circle(radius)     # circle 이라는 변수에 넓이와 둘레가 튜플 형태로 담겨져 있다
print(f"반지름이 {radius}인 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f} 입니다.")