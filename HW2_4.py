user_input = input("введите строку\n").split()
i = 0
for word in user_input:
    i += 1
    print(f"{i}. {word[:10]}")
