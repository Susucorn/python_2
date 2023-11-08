'''
    2023.11.08
    202395016 컴퓨터공학부 박수연

    -- 심화문제 8-6 --
    : 튜플을 요소로 가지는 stident_tuple 리스트가 있다
        (학번, 이름, 전화번호)로 이루어짐
    : (학번 : 이름)의 딕셔너리를 만들어 출력하라
    : 학번으로 조회를 할 경우 학번, 이름과 전화번호가 출력되도록 하라
'''
student_tuple = [("211101", "강이안", "010-123-1111"), ("211102", "박동민", "010-123-2222"), ("211103", "김수정", "010-123-3333")]  # 리스트로 묶인 튜플

# 1. (학번 : 이름)의 딕셔너리로 만들기
student_dict = {}       # 빈 딕셔너리를 먼저 생성한다

# 반복문 활용하여 딕셔너리 형태로 만들기
for id, name, phone in student_tuple:
    student_dict[id] = [name, phone]     # 딕셔너리의 (학번 : 이름) 형태로 저장한다

# 딕셔너리 내용 출력
for key, value in student_dict.items():         # student_dict.items() -> 키와 값 모두 가지고 옴
    print(key, ":", value[0])

# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하세요 : ")

if number in student_dict:
    name, phone = student_dict[number]
    print(f"{number} 학생은 {name}이며, 전화번호는 {phone}입니다.")