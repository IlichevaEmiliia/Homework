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


def p(num):
    for el in documents:
        if num == el['number']:
            return el['name']


def s(num):
    for k, v in directories.items():
        if num in v:
            return k


def full_information():
    for el in documents:
        print(f"№: {el['number']}, тип: {el['type']}, владелец: {el['name']}, полка хранения: {s(el['number'])}")


def ads(num):
    directories[num] = []
    return f"Полка добавлена. Текущий перечень полок: {', '.join(list(directories.keys()))}."


def ds(num):
    if s(num):
        if len(directories[num]) == 0:
            del directories[num]
            return f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}'
        else:
            return f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))}'
    else:
        return f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}'


while True:
    c = input('Введите команду: ')
    if c == 'q':
        break
    elif c == 'p':
        print(p(input('Введите номер документа: ')))
    elif c == 's':
        print(f"Документ хранится на полке: {s(input('Введите номер документа: '))}")
    elif c == 'l':
        full_information()
    elif c == 'ads':
        print(ads(input('Введите номер полки: ')))
    elif c == 'ds':
        print(ds(input('Введите номер полки: ')))
