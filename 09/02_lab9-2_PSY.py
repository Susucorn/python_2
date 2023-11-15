'''
    2023.11.15
    202395016 컴퓨터공학부 박수연
'''
text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color.  \
    It’s because when we show up, things change."

# 띄어쓰기로 문자열 분리하고, 단어의 갯수 찾기
print(text.split())      # 띄어쓰기로 문자열 분리 --> 변수명.split()    : 리스트 형태로 출력되는지 확인
tlist = text.split()     # tlist 에 저장하고 길이를 출력해보기
print('tlist의 길이(개수)? : ', len(tlist))        # len() --> 길이(개수)  --> 리스트의 항목 개수 찾음

print()
print()

# 도전문제 9-1
# 회사 이름은 ** 로 표시한다
# KT, Sansung, LG, SKT
print("------ 도전문제 9-1 ------")
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
        Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'

# 먼저 문장을 소문자로 바꾼다
text = text.lower()
print('소문자 변환 : \n', text)
print()

# 문자열을 공백으로 분리하여 리스트 변수에 저장
tlist = text.split() 
print('문자열 공백으로 분리 : \n', tlist)
print()

# 리스트에 저장된 단어를 검사하기 --> 단어가 회사명인가?
for i in range(len(tlist)):                         # tlist 안에 있는 문자열을 반복하여 i에 저장한다
    if tlist[i] in ['kt', 'skt', 'lg', 'samsung']:  # tlist 안에 회사명이 있다면
        tlist[i] = '**'                             # ** 로 바꾼다

# 공백 제거하기
text2 = " ".join(tlist)     # 공백과 join 하라
print('공백 제거 : \n', text2)
print()

# 결과 출력하기
print("================= 최종 결과 ===================")
print(text2)