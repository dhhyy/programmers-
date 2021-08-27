data = int(input())
for i in range(1, data + 1, 2):
    print((' ' * (data-i-1)) + ('*' * i))

# def solution(clothes):
#     dct    = {}
#     answer = 1
    
#     for wear,category in clothes:
#         if category not in dct:
#             dct[category] = []
#         dct[category].append(wear)
#     print(dct)
        
# #         print(dct)

#     for i in dct.keys():
#         answer *= len(dct[i]) + 1
#         # print(dct.keys())
#         # print(len(dct[i]))
#         # print(dct[i])
#         # print(answer)
#     return answer - 1

# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))


# 없음이라는 경우를 생각한다. 2 + 1 / 1 + 1
# 없음이라는 것

# 까다롭게 느껴지는 조건 때문에 간단해진다?

# 딕셔너리로 숫자를 박아 놓고 풀 수 있겠다


#   *
#  ***
# *****