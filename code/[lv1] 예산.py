def solution(d, budget):
    sorted_d = sorted(d)
    answer   = 0
    
    for i in range(len(sorted_d)):
        
        if budget >= sorted_d[i]:
            budget -= sorted_d[i]
            answer += 1
            
        else:
            break
    
    return answer


print(solution([2,2,3,3], 10))
