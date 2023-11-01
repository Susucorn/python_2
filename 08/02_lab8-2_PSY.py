'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 편의점 재고 관리 프로그램 --
'''
items = {'커피음료':7, '펜':3, '종이컵':2, '우유':1, '콜라':4, '책':5}      # 딕셔너리 생성

# 물건의 목록을 출력

# 물건의 입력을 입력받아 재고를 출력
print("제품 목록 : ", end=' ')
for key in items.keys():
    print(key, end=', ')
name = input("물건의 이름을 입력하세요 : ")

if name == '커피음료':
    print(items['커피음료'])
elif name == '펜':
    print(items['펜'])
elif name == '종이컵':
    print(items['종이컵'])
elif name == '우유':
    print(items['우유'])
elif name == '책':
    print(items['책'])