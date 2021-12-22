def solution(arr):

    result = []
    result.append(arr[0])
    
    for i in arr:
        if result[-1] != i:
            result.append(i)
        else:
            continue
        
    return result

print(solution([1,1,3,3,0,1,1]))