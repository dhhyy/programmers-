def solution(s):
    # 홀수라면
    if len(s) % 2 != 0:
        # 
        return s[len(s)//2]
    else:
        return s[(len(s)//2)-1]+s[len(s)//2]

print(solution("abcde"))
print(solution("qwer"))

s1 = "abcde"
s2 = "qwer"

print(len(s1)/2)
print(len(s2)/2)
print(len(s1)//2)
print(len(s2)//2)
print(s1[len(s1)//2])
print(s2[len(s2)//2])
print(s1[len(s1)//2])
print(s2[len(s2)//2-1]+s2[len(s2)//2])