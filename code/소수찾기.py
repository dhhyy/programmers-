# def solution(n):
#     answer = 0
#     result = []
#     for i in range(1, n+1):
#         if i % i == 0 and i % 1 == 0:
#             result.append(i)
#     return result

# print(solution(10))
# # print(solution(5))

def solution(n):
    answer = 0
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(i)
            if i % 3 == 0:
                result.append(i)
        
    return result

print(solution(10))
# print(solution(5))