def odd_gen(num_in):
    for num in range(1,num_in+1,2):
        yield num


print(list(odd_gen(15)))  