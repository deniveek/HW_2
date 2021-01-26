wares = []
wares_count = 0
while True:
    user_input = input("Чтобы добавить товар в список, введите 1\n"
                       "Чтобы изменить данные о товаре, введите 2\n"
                       "чтобы показать список товаров, введите 3\n"
                       "чтобы показать аналитику, введите 4\n"
                       "введите пустую строку, чтобы завершить работу ")
    if not user_input:
        break
    if user_input == "1":
        wares_count += 1
        user_input = input("введите название ")
        ware_info = {"название": user_input}
        user_input = input("введите цену товара ")
        ware_info["цена"] = user_input
        user_input = input("введите количество товара ")
        ware_info["количество"] = user_input
        user_input = input("введите еденицу измерения товара ")
        ware_info["ед"] = user_input
        wares.append((str(wares_count), ware_info))
    elif user_input == "2":
        user_input = input(
            "Введите номер товара, данные о котором необходимо изменить, или введите ничего, чтобы отменить ")
        if user_input in wares[(0)]:
            ware_info = wares[int(user_input) - 1][1]
            while user_input:
                user_input = input(
                    "введите название категории, данные в которой нужно исправить, или введите ничего, чтобы завершить ")
                while user_input:
                    if not ware_info.get(user_input):
                        user_input = input(
                            "Вы неправильно ввели название категории, введите его првильно,или введите ничего, чтобы завершить ")
                    else:
                        ware_info[user_input] = input("Введите исправленые данные о товаре ")
                        break
    elif user_input == "3":
        print("Список товаров:")
        for ware in wares:
            print(ware)
    elif user_input == "4":
        analytics = {}
        for ware in wares:
            for key in ware[1].keys():
                if key not in analytics.keys():
                    analytics[key] = []
                analytics[key].append(ware[1][key])
        print(analytics)
    else:
        print("некорректный ввод")
