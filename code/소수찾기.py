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