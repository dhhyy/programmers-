# 정수  = x
# 자연수 = n
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야한다. 

# 입력받은 n개의 숫자만큼의 반복 수를 설정
# n = 5, 1,2,3,4,5 이런 식으로 반복이 될 것
# 그러면 어차피 x만큼 증가를 하니까, 구구단처럼 처리
# x = 2가 들어오면 2x1 2x2 이런 식으로 될 것

def solution(x, n):
    answer = []
    
    [answer.append(x*i) for i in range(1, n + 1)]
    
    return answer