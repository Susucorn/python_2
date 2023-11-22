'''
    2023.11.01
    컴퓨터공학부 202395016 박수연

    - 온도를 입력받아 섭씨온도는 화씨온도로, 화씨온도는 섭씨온도로 변환하는 프로그램

    섭씨온도 = (화씨온도 - 32) * (5/9)
    화씨온도 = ((섭씨온도) * (9/5)) + 32

    섭씨온도 함수 : Cel_학번
    화씨온도 함수 : Fahl_학번
'''
# 섭씨온도를 구하는 함수
def cel_202395016(C):       
    c = (C - 32) * (5/9)
    return c

# 화씨온도를 구하는 함수
def Fahl_202395016(C):      
    f = (C * (9/5)) + 32
    return f

# 온도 입력받기
CelFahl = input("섭씨 또는 화씨온도를 입력하세요(27C 또는 27F) : ")  # 키보드로 입력받음

# 문자열 추출, 실수형으로 변환하기
CF = CelFahl[-1]                # 문자열 맨 뒷부분을 추출한다
temper = float(CelFahl[:-1])    # 문자열 맨 뒷부분을 제외한 나머지 숫자부분을 실수형으로 변환한다

# 섭씨온도인지 화씨온도인지 판단하기
if CF == 'C':                       # 만약 맨 뒷부분의 문자열이 C라면
    Fahl = Fahl_202395016(temper)   # 함수 호출
    print(f"화씨온도 {CelFahl}은 화씨온도 {Fahl:.2f}F 입니다.")

elif CF == 'F':                     # 만약 맨 뒷부분의 문자열이 F라면
    cel = cel_202395016(temper)     # 함수 호출
    print(f"섭씨온도 {CelFahl}은 화씨온도 {cel:.2f}C 입니다.")

else:
    print("온도를 잘못 입력하셨습니다.")