def solution(seoul):
    
    kim_rocation = seoul.index("Kim")
    
    return "김서방은 {}에 있다".format(kim_rocation)

print(solution(["Jane", "Kim"]))