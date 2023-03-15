def count(input1):
    dic ={}
    for i in input1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

print(count(['a', 'b', 'c', 'a', 'c', 'a', 'x']))
