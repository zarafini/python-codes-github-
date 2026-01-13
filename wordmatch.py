def wordmatch(words):
    ctr= 0
    lst= []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            lst.append(i)

    print("List of words with first and last character same\n", lst)
    return ctr

count= wordmatch(['dhg', 'hrg', 'rhr', 'rggr', 'evene'])
print("Number of words having first and last character the same:", count)