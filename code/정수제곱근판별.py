def solution(n):
    
    answer = 0
    
    for i in range(1, n):
        if n % i == 0:
            answer = (i+1)*(i+1)
        else:
            answer = -1
            
    return answer

print(solution(121))