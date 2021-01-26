rating = []
for i in range(1, 15, 2):
    rating.insert(0, i)
print(rating)
user_input = int(input("введите натуральное число\n"))
if user_input > 0:
    rating.append(0)
    for i in rating:
        if user_input > i:
            rating.insert(rating.index(i), user_input)
            break
    rating.pop(-1)
    print(rating)
else:
    print("некорретный ввод")