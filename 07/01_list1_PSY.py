'''
    2023.10.18
    202395016 컴퓨터공학부 박수연

    -- 리스트 만들기 --
'''
# 과일 리스트 만들기
fruits = ['멜론', '참외', '수박']
print("과일 목록 : ", fruits)

# 과일 추가 => append() 메소드 사용 (마지막에 추가)
fruits.append('바나나')
print("과일 목록(바나나 추가) : ", fruits)
fruits.append('파인애플')
print("과일 목록(파인애플 추가) : ", fruits)

# 과일 추가 => + 연산자 사용 (연결 연산자)
fruits = fruits + ['포도']  # 포도를 더해서 fruits에 저장함, num = num+1 과 같은 의미
print("과일 목록(포도 추가)", fruits)
print()

# 연결 연산자
num = [1, 2, 3] + [4, 5, 6]     # 리스트에서 + 연산자는 연결을 의미함
print("숫자 리스트 : ", num)
# 결과 예상 - [1, 2, 3, 4, 5, 6]
print()

# * 연산자 => 리스트를 n번 반복함
num1 = [1, 2, 3] * 3
print("숫자 리스트 * 3 : ", num1)
print()

# in 연산자 => 포함되어 있는가?
print("과일 목록에 망고가 있는가? -> ", '망고' in fruits)
print()

'''
    -- 인덱스를 사용하여 리스트의 항목에 접근하기 --
'''
print(":: 인덱스 활용 ::")
print("과일 리스트에 있는 과일의 갯수? : ", len(fruits))    # 과일 갯수

# 과일 리스트 주소
print("과일 중 첫번째 과일은? : ", fruits[0])
print("과일 중 마지막 과일은? : ", fruits[-1])             # 음수 인덱스로 마지막 원소를 쉽게 접근 가능함

# 과일 중 가장 큰 과일?
print("과일 중 가장 큰 과일은? : ", max(fruits))           # 문자열은 사전식 순서로 큰 값 찾음 (ㄱ, ㄴ, ㄷ, ....)
print("과일 중 가장 작은 과일은? : ", min(fruits))          # 문자열은 사전식 순서로 작은 값 찾음
print()

# 정렬
print(":: 정렬 ::")
fruits.sort()                       # 오름차순으로 정렬함
print("오름차순 정렬 : ", fruits)    # 작은 것부터 
fruits.sort(reverse=True)           # 내림차순으로 정렬함
print("내림차순 정렬 : ", fruits)    # 큰 것부터
print()

'''
    리스트를 원하는 모양으로 자르는 슬라이싱
'''
print(":: 슬라이싱 ::")
print("과일 목록 : ", fruits)
print("과일 리스트 중 2번째, 3번째, 4번째 과일은? : ", fruits[1:4])     # 리스트는 0번째부터 시작(2,3,4 => 1,2,3)
print("과일 리스트 중 1번째, 2번째, 3번째 과일은? : ", fruits[0:3])     # 리스트는 0번째부터 시작(1,2,3 => 0,1,2)
print("과일 리스트 중 1번째, 2번째, 3번째 과일은? : ", fruits[:3])      # 처음부터 2번째까지, [0:3]와 같다
print("과일 리스트 중 3번째 과일부터 마지막까지 과일은? : ", fruits[2:]) # 2번째부터 마지막까지
print("과일 리스트 중 1번째, 3번째, 5번째 과일은? : ", fruits[::2])     # 처음부터 끝까지 2씩 증가
print("과일 리스트 거꾸로 출력 : ", fruits[::-1])                      # 리스트를 거꾸로 출력
print()

'''
    리스트의 원소 값을 자유롭게 조작하기
'''
print(":: 리스트 요소 변경 ::")
print("과일 목록 : ", fruits)

# 원하는 위치에 '두리안' 추가 => insert() 메소드
fruits.insert(3, '두리안')
print("과일 목록 : ", fruits)   # 4번째에 '두리안' 추가됨

# 위치찾기 => index() 메소드
print("수박의 위치는? : ", fruits.index('수박'))    # 원하는 요소의 위치를 찾음

# 수박을 마지막에 추가
fruits.append('수박')
print("과일 목록(마지막에 수박 추가) : ", fruits)

# 수박의 개수 => count() 메소드
print("수박의 개수는? : ", fruits.count('수박'))    # '수박' 요소는 2개
print()

'''
    리스트의 항목 삭제
'''
# '수박' 요소 삭제 => remove() 메소드
print(":: 요소 삭제 ::")
fruits.remove('수박')
print("과일 목록(수박 삭제 후) : ", fruits)         # 리스트의 맨 먼저 오는 '수박' 요소를 삭제
print()
# 항목 삭제 => pop() 메소드
fruits.pop()                                       # 마지막 항목을 삭제함
print("과일 목록(마지막 요소 삭제) : ", fruits)
print()

# del() 키워드 => 포도 삭제
del fruits[0]   # 0번째 항목 삭제
print("과일 목록(첫번째 요소 삭제) : ", fruits)

'''
    # remove() - 괄호 안에 삭제할 항목을 지정함
    # pop() - 괄호 안에 X, 마지막 항목을 삭제함
    # del[] - [] 안에 위치를 지정하여 지정 위치 항목을 삭제함
''' 