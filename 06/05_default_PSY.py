'''
    2023.10.11
    202395016 컴퓨터공학부 박수연
    -- 함수의 디폴트 인자 --
'''
def order(num, pickel, onion) :
    print('햄버거{}개 - 피클{}, 양파{}' .format(num, pickel,onion))
    
# order(1) # 오류발생. 인자는 1개인데 매개변수는 3개이다.

# 인자가 부족한 경우 기본값을 넣어 주는 것 => 디폴트 인자
def order2(num, pickel='기본', onion='기본') :
    print('햄버거{}개 - 피클{}, 양파{}' .format(num, pickel,onion))
    
order2(2)
order2(1, pickel='뺌', onion='기본')