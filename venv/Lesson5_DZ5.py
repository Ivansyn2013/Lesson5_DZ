src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]

unique_src = set()
result_list =[]
for el in src:
    if el not in unique_src:
        unique_src.add(el)
    else: unique_src.discard(el)
print([el for el in src if el  in unique_src])
