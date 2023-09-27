'''
    2023.09.27
    202395016 컴퓨터공학부 박수연

    -- 터틀 그래픽으로 여러 개의 원 그리기 --
'''
import turtle as t

'''
# 원 하나 그리기
t.circle(100)   # 반지름이 100인 원

t.mainloop()    # 종료, t.done()
'''

for count in range(10):
    t.circle(100)       # 반지름이 100인 원을 5번 그림
    t.left(360/10)       # 회전하는 각도

t.mainloop()            # 종료