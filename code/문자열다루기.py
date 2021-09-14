def solution(s):
    
    answer = ''
    
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    else:
        answer = False
    
    return answer
        
print(solution("a33443"))
print(solution("a234"))
print(solution("1234"))