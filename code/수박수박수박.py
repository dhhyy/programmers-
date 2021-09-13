def solution(n):
    
    answer = ''
    
    str1 = '수'
    str2 = '박'
    
    answer = ((str1 + str2) * n)[:n]
    
    return answer

print(solution(3))
print(solution(4))