# 푸는 중

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

result = []

if range(len(arr1)) == range(len(arr2)):
    for in_arr1, in_arr2 in zip(arr1, arr2):
        print([(in_arr1[0] + in_arr2[0]), (in_arr1[1] + in_arr2[1])])