'''
    2023.10.11
    202395016 컴퓨터공학부 박수연

    -- LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수 --
    
    리스트에 10개의 값을 랜덤으로 생성,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.
    
    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.   max(), min()
            7) 값을 돌려준다.
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려 받은 최대값 또는 최소값을 출력한다.
'''
import random

def getMinMax(my_list, method='max'):
    if method == 'max' :                # method는 input_result 자리에 값을 넘겨줌, 만약 입력받은 값이 max라면
        maxValue = max(my_list)         # 리스트 요소 중에 최댓값을 maxValue 변수에 저장함
        return '최대값 : ' , maxValue   # 최대값을 리턴함
    elif method == 'min' :              # 입력받은 값이 min이라면
        minValue = min(my_list)         # 리스트 요소 중에 최솟값을 minValue 변수에 저장함
        return '최소값 : ' , minValue   # 최솟값을 리턴함
    else :
       print('illegal method')          # max 또는 min을 입력하지 않을 시에 출력됨
       
while(True):                
    # "_" 변수의 이름을 특별히 지정하지 않고, 단순히 반복 횟수를 나타내는 용도로 사용
    list_data = [random.randint(10, 99) for _ in range(10)]  # 범위가 10~99 인 10개의 랜덤 숫자를 가진 리스트 생성함
    print('생성된 리스트 : ', list_data)                      # 생성된 리스트 출력
    
    input_result = input('최대값을 원하면 max, 최소값을 원하면 min을 입력하시오: ')
    print(getMinMax(list_data, input_result))