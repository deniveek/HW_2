my_list = input("введите список разделяя элементы пробелами\n").split()
print(my_list)
i = 0
while i + 1 < len(my_list):
    aux = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = aux
    i += 2
print(my_list)
