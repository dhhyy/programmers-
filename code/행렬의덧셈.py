arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

result = []

for mid_arr1, mid_arr2 in zip(arr1, arr2):
    middle = []
    for i, j in zip(mid_arr1, mid_arr2):
        middle.append(i+j)
    # print(middle)
    result.append(middle)
print(result)