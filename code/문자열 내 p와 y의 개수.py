def solution(s):
    
    p_count    = 0
    y_count    = 0

    for i in s:
        if i == 'p' or i == 'P':
            p_count += 1
        if i == 'y' or i == 'Y':
            y_count += 1
    
    if p_count == y_count:
        return True
    else:
        return False

print(solution("pPoooyY"))
print(solution("Pyy"))