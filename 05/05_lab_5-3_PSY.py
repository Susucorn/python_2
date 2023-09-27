'''
    2023.09.27
    202395016 컴퓨터공학부 박수연

    -- 터틀 그래픽으로 n각형 도형 그리기 --
        사용자로부터 그려보고 싶은 도형의 변의 수를 입력받아 도형을 그리는 프로그램
'''
import turtle as t

t.shape("turtle")   # 거북이 모양

# 펜 이동   - 펜 자국이 남지 않도록 들어서 이동한 후 그림을 그림
t.penup()           # 펜을 든다
t.goto(-50, -150)    # x, y 좌표만큼 이동한 후
t.pendown()         # 펜을 내려 놓음


# 5번 반복
for count in range(5):
    # 원하는 도형을 입력 받기
    num = int(t.textinput("도형 그리기", "몇 각형의 도형을 그릴까요?"))
    # 도형 그리기
    for i in range(num):
        t.forward(100)  # 선 그리기, 길이는 100(앞으로)
        t.left(360/num) # 외각만큼 회전

t.done()        # 종료