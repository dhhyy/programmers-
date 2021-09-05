def solution(arr):
    
# 성공 케이스
    if(len(arr)==1):
        
        return [-1]
    
    else:
        
        arr.remove(min(arr))

    answer = arr
    return answer

# 실패 케이스 1 = 테스트케이스 1번 실패
#     if len(arr) > 1:
#         return [i for i in arr if i > min(arr)]
    
#     else:
#         return [-1]

#               ***********************
    
# 실패 케이스 2 = 테스트케이스 1번 실패
#     result = []
    
#     for i in arr:
#         if i > min(arr):
#             result.append(i)
#         if len(arr) == 1:
#             return [-1]
#     return result