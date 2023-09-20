'''
    2023.09.20
    컴퓨터공학부 202395016 박수연
    
    -- 선택문 if ~ else --
        1. random 함수를 이용한 가위바위보 게임
            random 함수로 생성된 정수로 게임을 진행
            0 => 가위 | 1 => 바위 | 2 => 보
'''
import random

print("--- 가위 바위 보 게임을 시작합니다. ---")

num = random.randrange(3)      # range - 범위  range(3) -> 0, 1, 2를 랜덤으로 생성하여 num 변수에 저장함

user = int(input("가위(0) 바위(1) 보(2)를 입력하세요 : "))
if num ==1:
    print("가위")
if num == 2:
    print("바위")
if num == 3:
    print("보")