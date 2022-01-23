lst = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

#1
lst = sorted(lst, key=lambda x: x[1], reverse=False)
print(lst)

#2 [[4, 0, 1, 7], [2, 1, 3, 5], [5, 2, 1, 0], [1, 3, 3, 4], [0, 4, 8, 3]]
dict = {}
count = 0

for i in lst:
    el = lst[count]
    key = el[1]
    del el[1]
    dict.setdefault(key, el)
    count += 1

print(dict)

#3 {0: [4, 1, 7], 1: [2, 3, 5], 2: [5, 1, 0], 3: [1, 3, 4], 4: [0, 8, 3]}
sort_dict = {}

for i in dict:
    sort_lst = dict[i]
    sort_lst = sorted(sort_lst, reverse=True)
    sort_dict.setdefault(i, sort_lst)
print(sort_dict)

#4 {0: [7, 4, 1], 1: [5, 3, 2], 2: [5, 1, 0], 3: [4, 3, 1], 4: [8, 3, 0]}
lst2 = []
for i in sort_dict:
    lst1 = (sort_dict[i])
    for n in lst1:
        lst2.append(n)
x = set(lst2)
print(x)

#5 {0, 1, 2, 3, 4, 5, 7, 8}
st = str(x)
print("String =" + st)
# String ={0, 1, 2, 3, 4, 5, 7, 8}