def solution(n):
    answer = []
    
    for i in str(n):
        answer.append(i)

    return sum(map(int, answer))

print(solution(123))
print(solution(987))

def solution(n):
    
    return sum(map(int, [i for i in str(n)]))

print(solution(123))
print(solution(987))