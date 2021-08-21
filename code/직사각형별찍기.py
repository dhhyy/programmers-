n, m = map(int, input().strip().split(' '))

for i in range(m):
    print(n * '*')
    
# 풀이

# strip()
# 양 옆의 공백을 제거해준다
str = '          real python             '
print(str)
print(str.strip())

# split()
# input에 split을 사용하면 입력받은 값을 공백을 기준으로 분리하여 변수에 차례대로 저장합니다(split은 분리하다, 나누다라는 뜻입니다). 
# 여기서는 문자열 'Hello Python'을 공백을 기준으로 분리하여 'Hello'는 첫 번째 변수 a에 'Python'은 두 번째 변수 b에 저장합니다.

a, b = input('문자열을 두 개 입력해주세요:').split()


a, b = map(int, input().strip().split(' '))
print(a + b)

# map
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

data1 = input('텍스트를 입력해라: ').split()
print(data1)
# 텍스트를 입력해라:           하이             
# ['하이']

data2 = input('텍스트를 입력해라: ').strip()
print(data2)
print(type(data2))
# 텍스트를 입력해라: hi
# hi
# <class 'str'>

# 여기까지 보면 결과가 똑같은 거 아닌가? 공백을 없애준다

data3 = input('덱스트를 입력해라 :  ').strip().split(',')
print(data3)
print(type(data3))
# 덱스트를 입력해라 :  hi
# ['hi']
# <class 'list'>

data4 = map(int, input().strip().split())
print(data4)
print(type(data4))
# hi
# <map object at 0x7fadc8133460>
# <class 'map'>

b = input().split(", ")
print(b)
print(type(b))
# hello, python, hello
# ['hello', 'python', 'hello']
# <class 'list'>
# 일단 데이터가 있고, 그 데이터에 있는 부호나 뭐 그런 것들을 기준으로 자르기!

a = input().split()
print(a)
print(type(a))
# 10 20 30
# ['10', '20', '30']
# <class 'list'>

b = map(int, input().split())
for i in b:
    print(b)
# 10 20 30
# <map object at 0x7fda201139a0>
# <map object at 0x7fda201139a0>
# <map object at 0x7fda201139a0>