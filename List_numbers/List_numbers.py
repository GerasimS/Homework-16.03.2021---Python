list1 = [1, 2, 8, 16]
list2 = [0, 0, 0, 0]


for id in list1:
    list2[id - 1] = list1[id - 1]**2

print(list2)
