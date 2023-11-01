'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 키와 값을 가지는 딕셔너리 --

    :: 튜플 (), 리스트 [], 딕셔너리 {} ::
'''
phone_book1 = {}    # 빈 딕셔너리 생성

# 딕셔너리에 값 저장하기_1 key, value
phone_book1['박수연'] = '010-5156-3383'  # [key] = value 의 형태로 값을 저장한다
print('phone_book1 : ', phone_book1)    # {'박수연': '010-5156-3383'} => 콜론을 중심으로 왼쪽이 key, 오른쪽이 value

# 딕셔너리에 값 저장하기_2 {key : value}
phone_book2 = {'홍길동' : '010-1234-5678', '박수연' : '010-5156-3383'}   # 직접 콜론을 적어 키와 값을 구분지어 저장할 수 있다 | 쉼표로 구분하여 첫번쨰값, 두번째값을 넣을 수 있다
print('phone_book2 : ', phone_book2)        # {'홍길동': '010-1234-5678'}

# 5명의 이름과 전화번호를 저장하여 출력하기
phone_book3 = {}
phone_book3['박수연'] =  '010-5156-3383'
phone_book3['박수진'] =  '010-5157-3384'
phone_book3['박수현'] =  '010-5158-3385'
phone_book3['박수이'] =  '010-5159-3386'
phone_book3['박수은'] =  '010-5150-3387'
print('phone_book3 : ', phone_book3)
print()

# key 값만 출력하기
print('------ phone_book3 이름 ------')
print(phone_book3.keys())       # 이름만 출력됨
print()
# value 값만 출력하기
print('------ phone_book3 전화번호 ------')
print(phone_book3.values())     # 전화번호만 출력됨
print()
# 모든 key, value 출력하기
print('------ phone_book3 출력 ------')
print(phone_book3.items())      # 이름만 출력됨
print()

print("----- 전화번호 phone_book3 items()출력 -----")
for name, phone_num in phone_book3.items(): # phone_book3.items 에 들어있는 값을 반복하여 각각 name(key), phone_num(value)로 저장함
    print(name, ':', phone_num)

print()

print("----- 전화번호 phone_book3[keys]로 접근하여 출력 -----")
for key in phone_book3.keys():
    print(key, ':', phone_book3[key])       # key에 대한 value 값이 나온다

print()

print("딕셔너리 작성 시 : (콜론)을 기준으로 key:value 로 작성")
person_dict = {'name':'박수연', 'age':'21', 'class':'1학년'}
print('name : ', person_dict['name'])   # 이름이 출력된다, person_dict에 있는 'name' 키로 값을 초회하여 출력함
print('age : ', person_dict['age'])     # 나이가 출력된다, person_dict에 있는 'age' 키로 값을 초회하여 출력함
print('class : ', person_dict['class']) # 학년이 출력된다, person_dict에 있는 'class' 키로 값을 초회하여 출력함

print()

print('----- 딕셔너리 정렬 -----')
print(sorted(phone_book3))          # phone_book3가 정렬된다, key를 기준으로 정렬하여 리스트로 반환됨

print()

# 키 정렬
print('----- 키를 기준으로 전체 정렬 -----')
sort_phone_book3 = sorted(phone_book3.items(), key = lambda x : x[0])   # lamda() 함수(이름없는 일회용), x의 0번지(이름) 기준으로 정렬을 하라
print(sort_phone_book3)

print()

# 값 정렬
print('----- 값을 기준으로 전체 정렬 -----')
sort_phone_book3 = sorted(phone_book3.items(), key = lambda x : x[1])   # lamda() 함수(이름없는 일회용), x의 1번지 (전화번호) 기준으로 정렬을 하라
print(sort_phone_book3)

# lamda 함수?
# 이름이 없는 함수, 간단한 1회용 작업에 유용한 함수 (복잡한 작업은 def 써야함)

print()

# 항목 삭제하기
print('----- 항목 삭제 -----')
del phone_book3['박수연']       # 삭제할 key를 입력하면 key에 대한 값도 삭제된다
print(phone_book3)

print()

# 전체 삭제하기
print('----- 전체 삭제 -----')
phone_book3.clear       # .clear
print(phone_book3)