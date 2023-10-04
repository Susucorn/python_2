'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복을 제어하는 break, continue --

    Test word : programming
'''
word = input("단어를 입력하세요 : ")        # 키보드로부터 입력받는 문자형

print(" -- break 1 --")

for i in word:                            # word 변수 안에 있는 값만큼 반복
    if i == "a" or i == "i" or i == "u" or i == "e" or i == "o":    # i가 a,e,i,o,u 중에 하나가 있다면
        break                                                       # 반복 빠져나감
    else:
        print(i, end='')                                            # 그렇지 않으면 i를 옆으로 연결하여 출력

# 결과 예상 : pr

print()

print(" -- break 2 --")
for i in word:                            # word 변수 안에 있는 값만큼 반복
    if i in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:      # i 안에 리스트 값이 있다면
        break                                                       # 반복 빠져나감
    else:
        print(i, end='')                                            # 그렇지 않으면 i를 옆으로 연결하여 출력

print()

print(" -- continue --")
for i in word:                            # word 변수 안에 있는 값만큼 반복
    if i in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:      
        continue                          # 반복문으로 다시 돌아감, print문을 만날 수 없다
    print(i, end='')                      # 리스트 요소들을 뺀 값이 나옴

# 결과 예상 : prgrmmng