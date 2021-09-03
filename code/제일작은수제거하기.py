# def solution(arr):
    
#     return [i for i in arr if i > min(arr)]
    
# print(solution([4,3,2,1]))
# print(solution([10]))

arr = [4,3,2,1]

result = []

for i in arr:
    if i > min(arr):
        result.append(i)
print(result)


# def solution(arr):
    
#     if(len(arr)==1):
#         return [-1]
#     else:
#         arr.remove(min(arr))

#     answer = arr
#     return answer