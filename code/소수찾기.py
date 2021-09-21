# def solution(n):
    
#     result = []
#     # 2나 3으로 나눠지지 않으면서 1과 자기 자신만으로 나뉘어지는 수
#     for i in range(1, n+1):
#         if i % i == 0 and i % 1 == 0:
#             result.append(i)
#     return result

# print(solution(10))
# print(solution(5))


# def solution(n):
#     answer = 0
#     result = []
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             result.append(i)
#         if i % 3 == 0:
#             result.append(i)
        
#     return result

# print(solution(10))
# print(solution(5))

def solution(n):
    
    num_set = set(range(2, n+1))
    print('1 - num_set_1 : ', num_set)
    
    for i in range(2, n+1):
        print('2 - i_for : ', i)
        if i in num_set:
            print('3 - i_if : ', i)
            num_set -= set(range(i*2, n+1, i))
            print('4 - num_set_2 : ', num_set)
            
    answer = len(num_set)
    print('5 - num_set_3 : ', num_set)
    
    return answer

print(solution(10))
# print(solution(5))