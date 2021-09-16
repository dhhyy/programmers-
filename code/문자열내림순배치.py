# s는 영문 대소문자로만 구성되어 있으며, 
# 대문자는 소문자보다 작은 것으로 간주합니다.

# 람다로 조건을 설정해서 정렬하는 것이 가능하겠다.

def solution(s):
    
    answer = ''
    
    return answer

print(solution("Zbcdefg"))
# return "gfedcbZ"

def solution(s):
    upper_list = []
    lower_list = []
    for word in list(s):
        upper_list.append(word) if word.isupper() else lower_list.append(word)
    upper_list.sort(reverse=True)
    lower_list.sort(reverse=True)
    answer = ''.join(lower_list + upper_list)
    return answer
