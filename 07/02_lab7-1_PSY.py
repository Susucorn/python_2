'''
    2023.10.18
    202395016 컴퓨터공학부 박수연

    -- 입력을 받아 맛있는 과일의 리스트 만들기 --
        좋아하는 과일 5개를 입력받아 리스트에 저장함
        과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단함

        추가 = append() 메소드
        찾기 = in 연산자
'''
fruits = []     # 빈 리스트 생성

for count in range(5):
    fru = input(str(count+1) + ". 좋아하는 과일을 5개 입력하세요 : ")   # 문자열 + 문자열 이여야 가능, 정수 + 문자열은 에러
    fruits.append(fru)                                                # 입력 받은 변수의 값을 리스트에 추가

print(fruits)
print()
# 찾기
fav_fruit = input("과일 하나를 입력하세요 : ")
# 사용자가 입력한 과일이 리스트 안에 있는지 판단
if fav_fruit in fruits:
    print(fav_fruit + "은(는) 당신이 좋아하는 과일입니다.")
else:
    print(fav_fruit + "은(는) 당신이 좋아하는 과일이 아닙니다.")