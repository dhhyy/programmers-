# 내 풀이

def solution(x):
    
    sum_x = sum(map(int, str(x)))
    
    if x % sum_x == 0:
        return True
    else:
        return False
    
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))

# 다른 분의 풀이 1
# a = 0을 만들어 for loop를 돌며 더하려는 생각은 하지 못했다
def Harshad(n):
    # n은 하샤드 수 인가요?
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n%a == 0 else False

print(Harshad(18))

# 다른 분의 풀이 2
# 스트링으로 바꿔주고, 뽑히는 문자열을 다시 int로 저장
def Harshad(n):
    return not( n % sum([int(x) for x in str(n)]))