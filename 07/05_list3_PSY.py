'''
    2023.10.18
    202395016 컴퓨터공학부 박수연

    -- 리스트의 객체 생성과 참조 --
'''
fru1 = ['딸기', '바나나', '수박']

fru2 = fru1

print("fru1 : ", fru1)
print("fru2 : ", fru2)      # 같은 리스트가 나옴

# 실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사됨
fru2[1] = '망고'            # fru2의 2번째 요소를 망고로 바꾸면

print("fru1 : ", fru1)      # fru1에 '바나나' 요소도 '망고'로 바뀐다
print("fru2 : ", fru2)      # 이유? - 주소를 참조하기 때문(같은 주소)

# 주소 확인 => 메모리 위치 정보 알아보기 -->  id()함수
print("fru1 의 id : ", id(fru1))
print("fru2 의 id : ", id(fru1))    # 두 리스트의 id정보(주소)가 같음
print()

'''
    리스트 내용 복제하기 list()함수
'''
print(":: 리스트 내용 복제 ::")
fru2 = list(fru1)   # 내용 복제(배정)
print("fru1 : ", fru1)
print("fru2 : ", fru2)
print("fru1 의 id : ", id(fru1))
print("fru2 의 id : ", id(fru1))
print()

# 내용 복제2
print(":: 리스트 내용 복제2 ::")
fru3 = fru1[:]
fru2 = list(fru1)   # 내용 복제(배정)
print("fru1 : ", fru1)
print("fru3 : ", fru3)
print("fru1 의 id : ", id(fru1))
print("fru3 의 id : ", id(fru3))    # id 정보가 다름
print()

print(":: fru3의 0번째를 '수박'으로 바꾼 후 ::")
fru3[0] = '수박'    # 0번째 요소를 '수박'으로 바꿈
print("fru1 : ", fru1)
print("fru3 : ", fru3)
print("fru1 의 id : ", id(fru1))
print("fru3 의 id : ", id(fru3))