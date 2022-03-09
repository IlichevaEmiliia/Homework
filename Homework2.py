user = {'Камин комплект Старый Замок': {'count': 1, 'price': 28490},
        'Полусапоги Betsy': {'count': 2, 'price': 2399},
        'Семь навыков высокоэффективных людей': {'count': 1, 'price': 437}}
total = 0
for el in user.values():
    total += el['count'] * el['price']
print(total)
