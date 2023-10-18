'''
    2023.10.18
    202395016 컴퓨터공학부 박수연

    -- 도시의 인구 자료에 대한 슬라이싱하기 --
'''
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

print("서울 인구 : ", population[1])     # 리스트의 두 번째 요소 출력
print("인천 인구 : ", population[-1])    # 리스트의 마지막 요소 출력, 음수 인덱스 활용
print("도시 리스트 : ", population[::2]) # 도시 이름만 있는 리스트 출력, step값 이용

people = population[1::2]                # 도시 인구만 있는 리스트 출력, step값 이용, 두번째 요소부터 마지막까지 2씩 증가                            
print("인구의 합 : ", sum(people))        # sum함수를 활용하여 인구의 합 출력