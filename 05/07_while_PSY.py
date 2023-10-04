'''
    2023.10.04
    202395016 컴퓨터공학부 박수연

    -- 반복문 while --
        조건에 따라 반복

    while 조건식:       => 콜론 (:) 반드시 사용
        들여쓰기로 반복하면서 동작 작성

    ** 반복문에서는 반드시 종료 조건이 존재하여야 함 **
'''
under_construction = True               # 공사중 (변수에 불린 값 넣을 수 있음)

while under_construction:               # True일 동안 계속 반복, while True랑 똑같음
    response = input("공사가 완료되었습니까?")
    if response == "예":                # 변수에 "예" 값이 들어온다면 - 종료조건
        under_construction = False      # 변수에 False 값을 넣어 종료시킴, True 일때만 무한반복하는 조건

print("루프 탈출")