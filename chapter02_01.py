# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
## 보통 작은따옴표를 많이 사용함
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
## => 분리가 무엇으로 되어있는지?
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-') ## 파라미터 결합을 '-'으로 시켜준다.
print('python', 'google.com', sep='@')

print()

# end 옵션
## => 끝부분을 어떻게 처리할 것인지?
## print()문은 자동으로 줄바꿈을 해 주지만 end 옵션에 들어간 문자로 다음 print문으로 이어질 수 있다.
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
## 외부 특정한 파일에 내용 작성
import sys ## import => 예약어

print('Learn Python', file=sys.stdout) ## sys.stdout => console out

print()

# format 사용(d, s, f)
## d => 정수(digit)
## s => 문자열(string)
## f => 실수(float)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2)) ## 좀 더 유연하게 사용 가능
print('{1} {0}'.format('one', 'two')) ## 순서 지정해서 사용 가능

print()

# %s
print('%10s' % ('nice')) ## 총 10개의 자릿수, 왼쪽부터 공백 처리
print('{:>10}'.format('nice'))

print('%-10s' % ('nice')) ## 총 10개의 자릿수, 오른쪽부터 공백 처리
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) ## 왼쪽 공백을 _로 채운다
print('{:^10}'.format('nice')) ## 중앙 정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) ## 5글자만 절삭(슬라이싱, 반올림)
print('%5s' % ('pythonstudy')) ## 다 출력됨
print('{:10.5}'.format('pythonstudy')) ## 총 10글자의 자리를 확보하는데 5개만 나와라

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.14343434343434))
print('%1.8f' % (3.14343434343434)) ## 정수부 1자리, 소수부 8자리
print('{:f}'.format(3.14343434343434))

print('%06.2f' % (3.141592653589793)) ## 총 6자리인데 정수부는 하나이기 때문에 나머지를 0으로 채움, 소수부는 둘째 자리까지
print('{:06.2f}'.format(3.141592653589793))
