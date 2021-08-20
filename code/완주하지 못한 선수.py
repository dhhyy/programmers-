def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for par, com in zip(participant, completion):
        if par != com:
            return par
        
    return participant[-1]
    
 
# 풀이

# 1. participant에는 있고, completion에는 없는 리스트 요소 하나를 return 한다.
# 2. completion의 길이는 participant의 길이보다 1 작습니다. -> 즉 한 명만 떨어진다. 
# 3. 참가자 중에는 동명이인이 있을 수 있다? -> 일단 무시
# 4. 이중 포문으로 participant 다 돌고 completion 돌고 일치하지 않은 값만 리턴
# 5. 질문하기 보니까 이중 포문 돌리면 효율성에서 안좋다고 한다..

# sort 묶어서 키, 밸류 값으로 만든 다음에 계속 비교
# 정렬을 한 후에 묶으면 된다. 

# list1 = ["leo", "kiki", "eden"]
# list1.sort()
# print(list1)

# def myFunc(e):
#     return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)
# print(cars)

# print("******************")

# list2 = ["leo", "kiki", "eden"]
# list2.sort()
# list3 = ["eden", "kiki"]
# list3.sort()

# list4 = ["marina", "josipa", "nikola", "vinko", "filipa"]
# list4.sort()
# list5 = ["josipa", "filipa", "marina", "nikola"]
# list5.sort()

# list6 = ["mislav", "stanko", "mislav", "ana"]
# list6.sort()
# list7 = ["stanko", "ana", "mislav"]
# list7.sort()

# print(list2)
# print(list3)
# print(list4)
# print(list5)
# print(list6)
# print(list7)

# ['eden', 'kiki', 'leo']
# ['eden', 'kiki']
# ['filipa', 'josipa', 'marina', 'nikola', 'vinko']
# ['filipa', 'josipa', 'marina', 'nikola']
# ['ana', 'mislav', 'mislav', 'stanko']
# ['ana', 'mislav', 'stanko']

x = 0
list_1 = [1,2,3,4,5]
list_2 = [5,4,3,2,1]

list_3 = dict(zip(list_1, list_2))

for i, j in list_3.items():
    x += i + j
print(list_3)