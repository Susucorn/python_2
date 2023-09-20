'''
    2023.09.20
    컴퓨터공학부 202395016 박수연

        -- 선택문 if ~ else --
        1. random 함수를 이용한 가위바위보 게임
            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임 진행
'''
import random

print("--- 가위 바위 보 게임을 시작합니다. ---")

player1 = input("player1의 이름을 입력하세요 : ")
player2 = input("player2의 이름을 입력하세요 : ")

num1 = random.randrange(3)      # player1의 랜덤 수
num2 = random.randrange(3)      # player2의 랜덤 수    

# player1의 가위바위보 출력
print(player1, " : ", end='')
if num1 ==0:
    print("가위")
if num1 == 1:
    print("바위")
if num1 == 2:
    print("보")

# player2의 가위바위보 출력
print(player2, " : ", end='')
if num2 ==0:
    print("가위")
if num2 == 1:
    print("바위")
if num2 == 2:
    print("보")

# player1이 가위 라면
if num1 == 0 :
    if num2 == 0:
        print("비겼습니다.")
    elif num2 == 1:
        print(player2, "이 이겼습니다.")
    else:
        print(player1, "이 이겼습니다.")

# player1이 바위 라면
if num1 == 1 :
    if num2 == 0:
        print(player1, "이 이겼습니다.")
    elif num2 == 1:
        print("비겼습니다.")
    else:
        print(player2, "이 이겼습니다.")

# player1이 보 라면
if num1 == 2 :
    if num2 == 0:
        print(player2, "이 이겼습니다.")
    elif num2 == 1:
        print(player1, "이 이겼습니다.")
    else:
        print("비겼습니다.")