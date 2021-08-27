def solution(phone_number):
    
    x = phone_number.replace(phone_number[:-4], "*" * len(phone_number[:-4]))
    
    return x