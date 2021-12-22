def solution(a, b):
    
    a.sort()
    b.sort(reverse=True)
    
    return sum([a * b for a, b in zip(a, b)])
