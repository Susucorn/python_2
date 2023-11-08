'''
    2023.11.08
    202395016 컴퓨터공학부 박수연

    -- 집합의 연산 --
'''
num1 = {1, 2, 3}    # 첫번쨰 집합
num2 = {1, 2, 3}    # 두번쨰 집합

# 비교 연산자
print("num1 == num2? : ", num1 == num2)
print("num1 != num2? : ", num1 != num2)

print()

numSet = {1, 4, 6, 3, 7, 9, 4}          # 집합 생성
print("numSet : ", numSet)              # 중복된 값을 빼서 출력
print("numSet 길이 : ", len(numSet))    # 중복 허용하지 않기 때문에 중복 제외 후 6개
print("numSet 최대값 : ", max(numSet))  # numSet 집합의 제일 큰 값 출력
print("numSet 최솟값 : ", min(numSet))  # numSet 집합의 제일 작은 값 출력
print("numSet 합계 : ", sum(numSet))    # 중복된 값 제외하고 합계를 계산한다

# ** set()는 중복을 허용하지 않는다 !

print()

num3 = {1, 2, 3}
num4 = {3, 4, 5}

print()

# 합집합
print("num3 | num4 : ", num3 | num4)                        # 합집합 연산자
print("num3.union(num4) : ", num3.union(num4))              # 합집합 메소드 .union()

print()

# 교집합
print("num3 & num4 : ", num3 & num4)                            # 교집합 연산자
print("num3.intersection(num4) : ", num3.intersection(num4))    # 교집합 메소드 .intersetion()

print()

# 차집합
print("num3 - num4 : ", num3 - num4)                         # 차집합 연산자
print("num3.difference(num4) : ", num3.difference(num4))     # 차집합 메소드 .difference()

print()

# 대칭차집합
print("num3 ^ num4 : ", num3 ^ num4)                                             # 대칭차집합 연산자
print("num3.symmetric_difference(num4) : ", num3.symmetric_difference(num4))     # 대칭차집합 메소드 .symmetric_difference()