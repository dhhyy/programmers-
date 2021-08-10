dict1 = [1,2,3,4,5]
dict2 = ["one", "two", "three", "four", "five"]

dict_zip      = zip(dict1, dict2)
dict_dict_zip = dict(zip(dict1, dict2))

print(dict_zip) # <zip object at 0x7f90101f0100> 이렇게 나온다. 객체로 나온다.
print(dict_dict_zip) # 이 결과값은 딕셔너리로 나온다. dict1 = key, dict2 = value


# (1, 'one') (2, 'two') (3, 'three') (4, 'four') (5, 'five')
 #이런 형태의 결과값이 나온다. 딕셔너리 형태가 아니라, 튜플 자료형으로 나온다.
for i in dict_zip: 
    print(i, end=" ")

# 아래 코드를 실행하면 출력이 되지 않는다. 
# TypeError: cannot unpack non-iterable int object 이러한 이유로 실행이 되질 않았다. 
# 딕셔너리를 그냥 지정하면 반복 가능한 형태가 아니기 때문이다.
for key, value in dict_dict_zip:
    print(key)
    print(value)

# 그래서 이렇게 풀었다.
# 아래 결과는 1 one 2 two 3 three 4 four 5 five 이렇게 나온다.
# 요소들이 리스트도 아니고 튜플의 형태도 아니게끔 출력이 된다. 
for key, value in dict_dict_zip.items():
    print(key, end=" ")
    print(value, end=" ")

# 튜플 언패킹을 이용한 풀이
def solution(absolutes, signs):
    answer = 0
    
    for key, value in zip(absolutes, signs):
        
        if value == True: 
            answer += key
        else:
            answer -= key
            
    return answer
        
print(solution([4,7,12], [True,False,True]))