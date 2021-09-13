# def solution(s):
    
#     int(s)
    
#     return int(s)


# print(solution("-1234"))


def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        print(idx, number)
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));