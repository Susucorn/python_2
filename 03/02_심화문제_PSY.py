'''
    2023.09.13
    컴퓨터공학부 202395016 박수연

    -- 90p 문제 3.9
        평균 시속과 이동시간을 입력받아
            이동시간은 시, 분, 초 단위로 출력하고,
                이동한 거리를 계산하여 출력하시오 --
'''

speed = float(input("평균 시속(km/h)을 입력하세요 : "))     # 평균 시속 실수로 입력받기
total_hours = float(input("이동 시간(h)를 입력하세요 : "))         # 시간 실수로 입력받기

print("평균 시속 : ", speed, "(km/h)")       # 평균 시속
hours = int(total_hours)                    # 시
total_minutes = ((total_hours-hours)*60)     # 분 - 초를 계산할 수 있도록
seconds = int((total_minutes-int(total_minutes))*60)           # 초
print("이동 시간 : {} 시간 {} 분 {} 초".format(hours, int(total_minutes), seconds))    # 이동 시간
print("이동 거리 : ", speed*total_hours, "km" )     # 이동 거리
