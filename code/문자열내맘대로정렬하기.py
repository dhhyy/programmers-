def solution(strings, n):
    
    strings.sort()
    
    answer = sorted(strings, key = lambda x : x[n])
    
    return answer

print(solution(["sun", "bed", "car"], 1))