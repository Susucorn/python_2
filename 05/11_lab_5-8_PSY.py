'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복문 while로 터틀 그래픽을 이용하여 별 그리기 --
'''
import turtle as t  # 터틀 불러오기, 별명은 t
t.shape("turtle")   # 펜 모양이 아닌 거북이 모양으로 바꿈
i = 1               # 변수 초기화

while i <=5:        # i가 5가 될 때까지 반복
    t.forward(200)   # 200픽셀 길이의 선분을 그림
    t.right(144)    # 144도 만큼 회전시킴
    i += 1          # i를 1씩 증가시킴