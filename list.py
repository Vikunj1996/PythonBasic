# list consist of unordered data as well as we add string float and list inside a list

a = [1, 2, 3, 4, 5, 44.3, 'aaba', [78, 2, 3, 'akla']]

print(a.index(3))  # return the index of value 3

a += [00, 11, 111]

print(a)

print(a[7][3])

if 44.3 in a:
    print("1 in list a")
