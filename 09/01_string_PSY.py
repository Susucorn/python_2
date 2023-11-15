'''
    2023.11.15
    202395016 컴퓨터공학부 박수연

    -- 텍스트 (문자열) --
'''
# 문자열도 슬라이싱이 가능하다
s = 'Happy Day!'
print(s[0])         # 변수명[주소]
print(s[6:10])      # 6번지부터 9번지까지 출력한다
print(s[:-2])       # 0번지부터 뒤에서 두번째 앞 번지까지 출력한다

# 문자열 분리 : .split() 메소드 활용
s = 'Welcome to Python!'
print(s.split())        # 괄호 안에 공백이면, 공백을 기준으로 분리한다 - 괄호 안에는 무엇을 기준으로 분리할지 적어주면 됨

print()

s = '2023.11.15'
print(s.split('.'))     # . 을 기준으로 분리한다

print()

s = 'Helld, world!'
print('< 쉼표를 기준으로 분리 >')
print(s.split(','))     # 쉼표를 기준으로 분리한다
# 공백도 문자이기 때문에 world 앞에 공백도 출력이 된다

# 쉼표랑 공백을 기준으로 분리하자
print('< 쉼표와 공백을 기준으로 분리 >')
print(s.split(', '))

# 공백 제거 : .strip() 메소드 활용
s = 'Welcome, to, Python, and , bla, bla'
print(s.strip())        
print([x.strip() for x in s.split(',')])    # 쉼표를 기준으로 분리한다, 분리한 것을 x에 저장한다, 공백도 없앤다
# 단어들만 추출하고 싶다면? - 쉼표들을 기준으로 잘라낸다, 공백도 제거한다
# 값을 담을 변수명.strip() for x in 문자열 담겨진 변수명.split(분리할 기준)

print()

# 문자열을 리스트로 바꾸기
print(list('Hello, World!'))    # 문장을 리스트로 형 변환 하라

print()

# 문자열 연결 : .join() 메소드 활용
print(','.join(['apple', 'grape', 'banana']))   # 쉼표로 붙여서 연결하라
#print('-'.join(['010.1234.5678'.split('.')]))  # .으로 구분된 번호를 - 기호로 바꾼다

# .을 -로 바꾸기
print('< .replace() 메소드 활용 >')
print('010.1234.5678'.replace('.', '-'))        #.replace(기호, 바꾸고 싶은 기호)

print()

s = 'Hello World!'
print(s)
slist = list(s)     # s에 담겨진 문자열을 리스트로 형 변환하여 slist에 저장함
print(slist)        # 리스트로 문자열 분리된다

# 분리된 문자를 다시 합치자
print(''.join(slist))   # slist를 합친다

print()

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = 'Today as well, \n\t Have a Happy Day.'
print(a_string)
# 문자열 자르고 wordlist에 저장하기
wordlist = a_string.split()             # 문자열 자르기
print(wordlist)
# 다시 합치기
refined_string = " ".join(wordlist)     # 공백과 join 하라
print(refined_string)                   # 줄바꿈과 탭이 삭제된다

# ** 문자 단어들을 잘라내고, 다시 합치면 문자열만 뽑아낼 수 있다 **

print()

# 대소문자 변환과 문자열 삭제하기
s = 'Hello, World!'
print(s)
print(s.lower())    # 변수명.lower()    --> 모두 소문자로 바꾼다
print(s.upper())    # 변수명.upper()    --> 모두 대문자로 바꾼다

# 공백 제거하기 strip()
s = '       Hello, World!       '
print(s.strip())    # 모든 공백 제거한다 (왼쪽, 오른쪽)
print(s.lstrip())   # 왼쪽 공백을 제거한다
print(s.rstrip())   # 오른쪽 공백을 제거한다

s = '#######Hello, World!#######'
print(s)
print(s.strip('#'))    # 기호를 제거한다
print(s.lstrip('#'))   # 왼쪽 기호를 제거한다
print(s.rstrip('#'))   # 오른쪽 기호를 제거한다

print()

# 문자열 찾기   : .find() 메소드 활용
s = 'www.silla.ac.kr'
print(s.find('.kr'))        # 몇 번지에 있는지 출력한다 - 12번지
print(s.find('x'))          # -1 이 출력됨 (x라는 문자열은 없다)

# .이 몇 개일까? : .count() 메소드 활용
print(s.count('.'))