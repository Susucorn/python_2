'''
    2023.11.1
    202395016 컴퓨터공학부 박수연

    -- 도시의 이름과 인구를 튜플로 묶어보자 --
'''
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]    # 리스트 생성

# 비교를 하기 위해 기준을 정함
max_population = city_info[0][1]        # 최대값이 0의 1번지가 기준이 된다 (첫번째 항목이 기준)
min_population = city_info[0][1]        # 최소값이 0의 1번지가 기준이 된다 (첫번쨰 항목이 기준)
total_pop = 0                           # 0으로 초기화

max_city = city_info[0][0]        # 최대값의 기준이 0의 0번지 (첫번쨰 항목이 기준)
min_city = city_info[0][0]        # 최소값의 기준이 0의 0번지

for city, pop in city_info:      # 두 개의 항목을 각각 가져올 수 있음   (도시명, 인구수) 
    total_pop += pop             # city 안에 있는 두번째 요소를 total_pop에 저장함 -> (부산, 3441)
    if pop > max_population:     # 만약 city의 두번째 요소가 max_population 보다 크다면 (max_population = 0)
        max_pop = pop            # max_pop에 city의 두번째 요소를 담기 - 최대인구
        max_city = city          # city의 값을 max_city에 담기 - 최대 인구 도시명

    if pop < min_population:     # 만약 city의 두번째 요소가 min_population보다 작다면 (min_population = 999999999999999999)
        min_pop = pop            # min_pop에 city의 두번째 요소를 담기 - 최소인구
        min_city = city          # city의 값을 min_city에 담기 - 최소 인구 도시명

print('최대인구 : {0}, 인구 : {1} 천명'.format(max_city, max_population))
print('최소인구 : {0}, 인구 : {1} 천명'.format(min_city, min_population))
print('리스트 도시 평균 인구 : {0} 천명'.format(total_pop, len(city_info)))