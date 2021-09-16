def solution(s):
    
    answer = ''
    s_split = s.split(" ")

    
    for str_part in s_split:
        
        for i, c in enumerate(str_part):

            if i % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        else:
            answer += ' '

    return answer[:-1]
    
print(solution("try hello python"))