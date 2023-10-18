'''
    2023.10.18
    202395016 컴퓨터공학부 박수연

    -- 리스트에서 사용 가능한 함수 --
'''

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # 리스트를 변수에 저장

print("num_list : ", num_list)
print("num_list 길이 : ", len(num_list))
print("num_list 최대값 : ", max(num_list))
print("num_list 최소값 : ", min(num_list))
print("num_list 항목의 합계 : ", sum(num_list))
print("num_list 항목의 평균 : ", sum(num_list)/len(num_list))
print("num_list 항목 중 0이 아닌 원소가 있는가? : ", any(num_list))