# 푸는 중

# 내 풀이는 [0] [1]만 됨. 그러니까 out of range가 된다

# zip으로 풀면 안되나?

# 1 이 문제를 풀며 행렬의 대한 이해가 부족하다는 걸 느낌
# 2 또한 이중 포문에 대한 이해가 부족하다고 느낌
# 이 부분을 복습하면 된다! 

# zip 배열의 길이가 아무리 길어지더라도 상관 없음

# zip 정리!

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

result = []

for i, j in zip(arr1, arr2):
    temp = []
    print("i, j :", i, j)
    for x, y in zip(i, j):
        print("x + y :", x+y)
        temp.append(x+y)
        print("temp :", temp)
    result.append(temp)
print(result)


# for i in range(len(arr1)):
#     for j in range(len(arr1[i])):
#         arr1[i][j] += arr2[i][j]
# print(arr1)


# 코드 설명

# for i in range(len(arr1)):
# # 프린트 찍어보면 0 1 나옴. 0번 1번 반복을 하는 것, 그러니까 그 리스트의 길이만큼 반복을 시킬 때 반복을 하는 것
# # print(len(arr1))
# # print(range(len(arr1)))
# # print(i) 0, 1이 반복됨. 가장 위의 코드는 단순 반복 범위를 설정
#     for j in range(len(arr1[i])):
# # print(j) 0 1 0 1 나옴 위에 반복 범위가 2번이니까 당연하게 0 1 0 1이 나온다
#         # print(arr1[i])
#         # print("*************")
#         print(arr1[j])
#         #print("*************")
#         #print(arr1[i][j])
#         arr1[i][j] += arr2[i][j]
# print(arr1)