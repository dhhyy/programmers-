# s는 영문 대소문자로만 구성되어 있으며, 
# 대문자는 소문자보다 작은 것으로 간주합니다.

# 람다로 조건을 설정해서 정렬하는 것이 가능하겠다.

def solution(s):
    
    answer = ''
    
    return answer

print(solution("Zbcdefg"))
# return "gfedcbZ"


testing_str = "Zbcdefg"

data1 = sorted(testing_str, reverse=True)
print(data1)
print(sorted(testing_str))

# 해당 문자열의 문자들을 내림차순으로 정렬해야 하므로 문자열이 가진 문자열을 하나씩 잘라 리스트에 젖아한 뒤정렬하고 다시
# 다시 문자열로 변경하는 것 이때 대문자는 아스키코드 값이 소문자보다 작기 때문에 대문자가 더 작다는 조건은 
# 자동적으로 성립된다고 한다

def solution(s):
    upper_list = []
    lower_list = []
    for word in list(s):
        upper_list.append(word) if word.isupper() else lower_list.append(word)
    upper_list.sort(reverse=True)
    lower_list.sort(reverse=True)
    answer = ''.join(lower_list + upper_list)
    return answer
