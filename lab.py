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


def p(num): #узнать владельца по его номеру
    for el in documents:
        if num == el['number']:
            return el['name']


def s(num): #узнать по номеру на какой полке хранится документ
    for k, v in directories.items():
        if num in v:
            return k


def full_information(): #распечатать полную информацию о документах
    for el in documents:
        print(f"№: {el['number']}, тип: {el['type']}, владелец: {el['name']}, полка хранения: {s(el['number'])}")


def ads(num): #добавить полку
    directories[num] = []
    return f"Полка добавлена. Текущий перечень полок: {', '.join(list(directories.keys()))}."


def ds(num): #удалить полку
    if num in directories.keys():
        if len(directories[num]) == 0:
            del directories[num]
            return f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}'
        else:
            return f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))}'
    else:
        return f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}'
    
    
def ad(num): #добавить документ
    new_doc = {}
    new_doc['number'] = input('Введите номер документа: \n')
    new_doc['type'] = input('Введите тип документа: \n')
    new_doc['name'] = input('Введите владельца документа: \n')
    shelf = input('Введите полку для хранения: \n')
    if shelf in directories.keys():
        documents.append(new_doc)
        directories[shelf].append(new_doc['number'])
        print(f'Документ добавлен. Текущий список документов:')
        full_information()
    else:
        print('Такой полки не существует. Вы можете добавить новую полку командой ads. \nТекущий список документов:')
        full_information()

        
def d(num): #удалить документ
    name = p(num)
    if name:
        directories[s(num)].remove(num)
        documents.remove(i)
        print('Документ удалён. \nТекщий список документов:')
        full_information()
    else:
        print('Документ не найден в базе. \nТекущий список документов:')
        full_information()
        
        
def m(): #переместить документ с полки на полку
    num = input('Введите номер документа: \n')
    shelf = input('Введите номер полки: \n')
    if p(num):
        if shelf in directories.keys():
            directories[s(num)].remove(num)
            directories[shelf].append(num)
            print('Документ перемещен. \nТекущий список документов:')
            print_all()
        else:
            print(f'Такой полки не существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')
    else:
        print('Документ не найден в базе. \nТекущий список документов:')
        
        
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
    elif c == 'ad':
        ad()
    elif c == 'd':
        d()
    elif c == 'm':
        m()
