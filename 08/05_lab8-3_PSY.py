'''
    2023.11.08
    202395016 컴퓨터공학부 박수연

    -- lab 8-3, 도전문제 --
'''
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))   # 교집합 메소드

print()

# 도전문제 
print("파티 A, B에 참석한 사람들 : ", partyA.union(partyB))                         # 합집합
print("파티 A, B에 중복없이 참석한 사람 : ", partyA.symmetric_difference(partyB))   # 대칭차집합
print("파티 A에만 참석한 사람 : ", partyA.difference(partyB))                       # 차집합