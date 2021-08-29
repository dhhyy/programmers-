# 원래 리스트를 약수를 구하는 리스트를 따로 만들어서 공약수를 찾아서 그 안에서 가장 작은 것을 구하려고 했다. 하지만 실패


# def solution(n, m):
    
#     min_n   = []
#     min_m   = []
#     max_n_m = []
#     result  = []
    
#     # 최대공약수 구하기
    
#     for i in range(1, n+1):
#         if n % i == 0:
#             min_n.append(i)
            
#     for i in range(1, m+1):
#         if m % i == 0:
#             min_m.append(i)
            
#     gcf_num = max(min_n)
    
#     if gcf_num in min_m:
        
#         result.append(gcf_num)
    
#     for i in range(m, (n * m) + 1):
#         if i % n == 0 and i % m == 0:
#             max_n_m.append(i)
            
#             print(max_n_m)
    
#             lcm_num = min(max_n_m)
            
#             print(lcm_num)
#             print(result)
            
#             return result.append(lcm_num)

# print(solution(3, 12))



# num1 = 3
# num2 = 12

# for i in range(num2, (num1*num2)+1):
#     if i % num1 == 0 and i % num2 == 0:
#         print(i)



def solution(n, m):
    
    min_n   = []
    min_m   = []
    max_n_m = []
    result  = []
    
    # 최대공약수 구하기
    
    for i in range(1, n+1):
        if n % i == 0:
            min_n.append(i)
    print(min_n)
            
    for i in range(1, m+1):
        if m % i == 0:
            min_m.append(i)
    print(min_m)
            
    gcf_num = max(min_n)
    
    if gcf_num in min_m:
        
        result.append(gcf_num)
    
    for i in range(m, (n * m) + 1):
        if i % n == 0 and i % m == 0:
            max_n_m.append(i)
    
            lcm_num = min(max_n_m)
            
            if lcm_num in max_n_m:
            
                result.append(lcm_num)
                
        return result

print(solution(3, 12))
# print(solution(2, 5))

# 리스트에 있는 것들 중에서 공통되는 것은 또 따로 담기