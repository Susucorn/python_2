'''
    2023.11.08
    202395016 컴퓨터공학부 박수연

    -- 심화문제 8-3 --
    
    : 3명의 학생의 학번, 이름, 전화번호의 3쌍의 요소를 가지는 student_tuple이 존재한다
    : 이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로 이루어진 딕셔너리를 만들어 출력
    : 이 정보를 이용하여 학생의 학번을 입력 받아 이름과 전화번호를 출력하는 학사정보 프로그램을 작성
    : student_tuple의 마지막 항목으로 학점을 추가한다, 이 정보를 바탕으로 딕셔너리를 만들어 출력
    : 학생의 학점 평균을 출력하기
'''
student_tuple = [('211101', '조성훈', '010-1234-4500'), ('211102', '김은지', '010-1223-4455'), ('211103', '윤소정', '010-3344-4567')]     # 튜플로 정보를 저장하여 리스트로 묶는다

student_dict = {}       # 빈 딕셔너리 생성

# 딕셔너리에 추가
for idNum, name, phone in student_tuple:        # 세 개의 항목들을 student_tuple 안에 있는 요소를 차례대로 저장하라
    student_dict[idNum] = [name, phone]         # key는 학번, value는 이름과 전화번호가 들어간다

# 딕셔너리 내용 출력
for key, value in student_dict.items():         # student_dict.items() -> 키와 값 모두 가지고 옴
    print(key, ":", value)

# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하세요 : ")
print("이름 : ", student_dict[number][0])           # number 에 0번지와 (이름)
print("연락처 : ", student_dict[number][1])         # number 에 1번지를 출력 (연락처)

# 학점 추가
student_dict["211101"].append(4.5)
student_dict["211102"].append(3.5)
student_dict["211103"].append(2.5)


# 학점 출력
print("전체 학생의 학점 평균")

sum = 0
for key, value in student_dict.items():
    sum = sum + value[2]
print(f"평균 : {(sum/3):.2f}")