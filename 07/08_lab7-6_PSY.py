'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 도시의 이름과 인구를 튜플로 묶어보자 --
'''
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]    # 리스트 생성

# 비교를 하기 위해 기준을 정함
max_population = 0                      # 최대값을 999~... 를 한다면 999~... 보다 많은 인구는 없음
min_population = 999999999999999999     # 최소값을 0으로 한다면 0보다 적은 인구는 없음
total_pop = 0                           # 0으로 초기화

max_city = None         # 인구가 가장 많은 도시의 값을 저장하기 위해 None으로 초기화
min_city = None         # 인구가 가장 적은 도시의 값을 저장하기 위해 None으로 초기화

for city in city_info:           # city_info 안에 있는 요소들을 반복하여 city 에 저장함
    total_pop += city[1]         # city 안에 있는 두번째 요소를 total_pop에 저장함 -> (부산, 3441)
    if city[1] > max_population: # 만약 city의 두번째 요소가 max_population 보다 크다면 (max_population = 0)
        max_pop = city[1]        # max_pop에 city의 두번째 요소를 담기 - 최대인구
        max_city = city          # city의 값을 max_city에 담기 - 최대 인구 도시

    if city[1] < min_population: # 만약 city의 두번째 요소가 min_population보다 작다면 (min_population = 999999999999999999)
        min_pop = city[1]        # min_pop에 city의 두번째 요소를 담기 - 최소인구
        min_city = city          # city의 값을 min_city에 담기 - 최소 인구 도시

print('최대인구 : {0}, 인구 : {1} 천명'.format(max_city[0], max_city[1]))
print('최소인구 : {0}, 인구 : {1} 천명'.format(min_city[0], min_city[1]))
print('리스트 도시 평균 인구 : {0} 천명'.format(total_pop, len(city_info)))