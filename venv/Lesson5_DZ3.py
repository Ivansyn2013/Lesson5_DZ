
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#result = [12, 44, 4, 10, 78, 123]
result_list =[]
for i, j in zip(src, src[1::]):
    if j>i: result_list.append(j)


print(result_list)