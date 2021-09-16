def solution(s):
    # 홀수라면
    if len(s) % 2 != 0:
        return s[len(s)//2]
    else:
        return s[(len(s)//2)-1]+s[len(s)//2]

print(solution("abcde"))
print(solution("qwer"))