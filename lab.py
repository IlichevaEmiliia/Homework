documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def poisk_doc(num): #найти владельца документа по номеру
    for el in documents:
        if num == el['number']:
            return el['name']


def search_shelf(num): #найти на какой полке документ
    for k, v in directories.items():
        if num in v:
            return k


def p(num):
    if poisk_doc(num):
        return f"Владелец документа: {poisk_doc(num)}"
    else:
        return 'Документ не найден в базе'


def s(num):
    if search_shelf(num):
        return f"Документ хранится на полке: {search_shelf(num)}"
    else:
        return 'Документ не найден в базе'


def full_information():  # распечатать полную информацию о документах
    for el in documents:
        print(f"№: {el['number']}, тип: {el['type']}, владелец: {el['name']}, полка хранения: {s(el['number'])}")


def ads(num):  # добавить полку
    if num in directories.keys():
        return f"Такая полка уже существует. Текущий перечень полок: {', '.join(list(directories.keys()))}."
    else:
        directories[num] = []
        return f"Полка добавлена. Текущий перечень полок: {', '.join(list(directories.keys()))}."


def ds(num):  # удалить полку
    if num in directories.keys():
        if len(directories[num]) == 0:
            del directories[num]
            return f"Полка удалена. Текущий перечень полок: {', '.join(list(directories.keys()))}."
        else:
            return f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {', '.join(list(directories.keys()))}."
    else:
        return f"Такой полки не существует. Текущий перечень полок: {', '.join(list(directories.keys()))}."


def ad():  # добавить документ
    new_doc = {'number': input('Введите номер документа: \n'), 'type': input('Введите тип документа: \n'),
               'name': input('Введите владельца документа: \n')}
    shelf = input('Введите полку для хранения: \n')
    if shelf in directories.keys():
        documents.append(new_doc)
        directories[shelf].append(new_doc['number'])
        print(f'Документ добавлен. Текущий список документов:')
        full_information()
    else:
        print('Такой полки не существует. Вы можете добавить новую полку командой ads. \nТекущий список документов:')
        full_information()


def d(num):  # удалить документ
    for i in range(len(documents)):
        if documents[i]["number"] == num:
            documents.pop(i)
            return 'Документ удалён. \nТекщий список документов:'
    return 'Документ не найден в базе. \nТекущий список документов:'


def m():  # переместить документ с полки на полку
    num = input('Введите номер документа: \n')
    shelf = input('Введите номер полки: \n')
    for i in range(len(documents)):
        if documents[i]["number"] == num:
            if shelf in directories.keys():
                directories[search_shelf(num)].remove(num)
                directories[shelf].append(num)
                return 'Документ перемещен. \nТекущий список документов:'
            else:
                return f"Такой полки не существует. Текущий перечень полок: {', '.join(list(directories.keys()))}"
    return 'Документ не найден в базе. \nТекущий список документов:'


while True:
    c = input('Введите команду: ')
    if c == 'q':
        break
    elif c == 'p':
        print(p(input('Введите номер документа: ')))
    elif c == 's':
        print(s(input('Введите номер документа: ')))
    elif c == 'l':
        full_information()
    elif c == 'ads':
        print(ads(input('Введите номер полки: ')))
    elif c == 'ds':
        print(ds(input('Введите номер полки: ')))
    elif c == 'ad':
        ad()
    elif c == 'd':
        print(d(input('Введите номер документа: ')))
        full_information()
    elif c == 'm':
        print(m())
        full_information()
