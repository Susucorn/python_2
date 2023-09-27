'''
    2023.09.27
    202395016 컴퓨터공학부 박수연

    -- 반복문 for --
'''
# 본인 이름 5개 출력
print(":: for 반복문으로 이름 5개 출력 ::")
for i in range(5):
    print(i, " : 박수연")

print()

print(":: 리스트로 이름 5개 출력 ::")
for i in [1,2,3,4,5]:   # 리스트
    print(i, " : 박수연")

print()

print(":: 리스트로 구구단의 19단 출력 ::")
for num in [1,2,3,4,5,6,7,8,9]:     # range(1,10)
    print(f"19 * {num} = {num*19}")

print()

print(":: 문자열 내용 출력 ::")
for i in "Hello" :                  # 문자열을 하나씩 i 변수에 담아서 차례대로 출력함
    print("i = ", i)

print()

# 도전 문제 5.3
print(":: BTS 멤버 명단 출력 ::")
bts = ["뷔", "제이홉", "알엠", "정국", "진", "지민", "슈가"]

for i in bts:
    print(i)