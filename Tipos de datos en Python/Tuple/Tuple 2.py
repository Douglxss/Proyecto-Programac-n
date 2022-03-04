lst = [20,"C#","Pedro",48]
lst_tuple = [x for x in zip(*[iter(lst)]*2)]

print(lst_tuple)