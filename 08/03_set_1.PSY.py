'''
    2023.11.08
    202395016 컴퓨터공학부 박수연

    -- 집합 set() --
'''
number = set()              # 빈 집합 생성, 변수에 저장
number1 = {2, 1, 3}         # 숫자 3개로 이루어진 집합
print("집합 : ", number1)   # 나열한 순서대로 출력되지 않는다

# 비어있는 집합을 만들려면 set() 이라고 명명하고, 중괄호 안에 원소를 나열한다
# 딕셔너리는 중괄호 안에 key : value
print()

# 리스트로부터 집합 생성하기
number2 = set([1, 2, 3, 1, 2])  # 이 리스트를 집합으로 바꿔서 변수에 저장
print("집합 : ", number2)       # 중복을 허용하지 않는다

print()

# 문자열을 집합으로 생성하기
text1 = set("asdfasdf") 
print("text1 : ", text1)

print()

numbers = {2, 4, 5, 1, 2}
if 1 in numbers:                    # 만약 1이 numbers 안에 있다면
    print("집합에 1이 존재합니다.")   # 이 문장을 출력한다

# 집합은 순서가 없기 때문에 index로 접근이 불가능함

print()

# 반복문으로 접근하여 출력 가능
numbers1 = {9, 1, 5, 2, 4, 7, 6, 3, 4, 9, 1}
for num in numbers1:
    print(num, end=' ')

# 정렬 후 출력하기
for num in sorted(numbers1):        # num 변수 안에 numbers1을 정렬하고 반복하여 값을 저장한다
    print(num, end=' ')             # sorted()를 써야 정렬되어 출력된다

print()

for num in sorted(text1):
    print(num, end=' ')

print()

# 추가하기
numbers1.add(100)               # add - 추가 | append - 마지막에 추가
print(numbers1)                 # 그냥 출력
for num in sorted(numbers1):  
    print(num, end=' ')         # 정렬되어 출력

print()

# 삭제하기
numbers1.remove(100)
print(numbers1)