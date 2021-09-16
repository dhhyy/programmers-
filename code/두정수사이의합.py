def solution(a, b):
    
    answer = 0
    
    for i in range(a, b+1):
        answer += i
    
    if a > b:
        for i in range(b, a+1):
            answer += i
    
    return answer
        
        
print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

def solution(a, b):
    
    return sum(range(min(a,b), max(a,b)+1))

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))