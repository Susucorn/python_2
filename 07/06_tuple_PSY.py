'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 한 번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플 (불변속성 자료형) --
'''
color = ("red", "yellow", "green", "blue")      # 튜플 생성
color_list = ["red", "yellow", "green", "blue"] # 리스트 생성

print(f"color : {color}")

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append' : 튜플 개체에 append 속성이 없다는 뜻
# 튜플은 추가, 삭제 불가
# color.append("black")

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작함
print("color 튜플 : ", color)
print("color 튜플 중 2, 3, 4번은? : ", color[1:4])
print("color 튜플 중 1, 2, 3번은? : ", color[:3])  # [0:3]
print("color 튜플 중 3번~ 끝은? : ", color[2:])    # [2:4]
print("color 튜플 중 1, 3, 5번은? : ", color[::2]) # 2씩 증가, 시작부터 끝까지, 5번은 없으므로 출력안함
print("color 튜플을 반대로 출력? : ", color[::-1])  # 거꾸로 출력

# 튜플끼리도 결합이 가능하다 => + 연산자 | 반복도 가능하다 => * 연산자
colors = color+color
print("colors 튜플 : ", colors)
print("color 튜플을 10번 반복하여 출력? : ", color*10)