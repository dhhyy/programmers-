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

3
https://ychae-leah.tistory.com/7

def solution(s):
    
    charlist = ""
    idx = 0
    for i in s:
        if i.isalpha():
            idx += 1
            if idx % 2 != 0:
                charlist += i.upper()
            else:
                charlist += i.lower()
        else:
            idx = 0
            charlist += " "
            continue
        
    return charlist

print(solution("try hello python"))