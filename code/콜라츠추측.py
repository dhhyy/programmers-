def solution(num):
    
    answer = 0
    
    while num != 1:
        
        if num % 2 == 0:
            num = int(num / 2)
            answer += 1
            
        else:
            num = (num * 3) + 1
            answer += 1
        
        if answer >= 500:
            answer = -1
            break
        
    return answer

print(solution(6))
print(solution(100))
print(solution(325161))

# 조건을 따로 생각할 필요가 없었다.
# 숫자가 하나 나오면, 그 숫자를 판별해 주면 된다.

# 1
# while count < 500 : 말이 안되는 코드

# def solution(num):
#     count = 0
#     # 1일때까지 반복한다
#     while num == 1:
        
#         # 만약에, num % 2 할 때 0이면 짝수라면,
#         # num은 그냥 나누기 2로 나눈다
#         # 그리고 count += 1을 한다
#         if num % 2 == 0:
#             num = num / 2
#             count += 1

#         else:
#             num = num * 3 + 1
#             count += 1
            
#             return count
        
#         return -1
    
# print(solution(6))
# print(solution(7))
# print(solution(16))
# print(solution(626331))

# print('****************')

# data  = 4
# count = 0

# while data == 1 or data == 0:

#     if data % 2 == 0:
#         data = data / 2
#         count += 1
    
#     else:
#         data = (data * 3) + 1
#         count += 1
        
#     print(count


# data = 4

# data //= 2

# print(data))