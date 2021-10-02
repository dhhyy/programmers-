# 1
# for loop를 두 번 사용하는 방법

# def solution(arr):
    
#     answer = []
    
#     for i in range(len(arr)):
#         print("1 : ", arr[i])
#         for j in range(len(arr)):
#             print("2 : ", arr[j])
#             print("---------------------")
#             if arr[i] != arr[j]:
#                 answer.append(arr[i])
#             else:
#                 break
#     return answer

# print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))

# 2
# 연속되는 숫자가 없을 때까지 반복하는 방법



# arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7] 
# result = [] # 중복 제거된 값들이 들어갈 리스트 
# for value in arr: 
#     if value not in result: 
#         result.append(value) 
# print(result)

# test_arr = [1,1,1,4,4,6,6,8,9,10,10]
# result   = []

# for i in test_arr:
#     if i not in result:
#         result.append(i)
# print(result)

# def solution(arr):
    
#     answer = []
#     answer.append(arr[0])
    
#     for i in range(1, len(arr)):
#         if arr[i-1] != arr[i]:
#             answer.append(arr[i])
            
#     return answer

# print(solution([1,1,3,3,0,1,1]))

# 다른 풀이들 더 공부하자... 계속 공부하자... 

# 코드를 뭐 어떻게 하기 보다는 자료형부터 생각하고,
# 인덱스를 이용할 생각을 하자.. 

# def solution(arr):
    
#     result = []
#     result.append(arr[0])
    
#     for i in arr:
#         if result[-1] != i:
#             result.append(i)
#         else:
#             continue
        
#     return result

# print(solution([1,1,3,3,0,1,1]))

a = [1,2,3,4,5,6,7]

print(a[-1:])
print(type(a[-1:]))
print(a[-1])
print(type(a[-1]))




def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1,1,3,3,0,1,1]))