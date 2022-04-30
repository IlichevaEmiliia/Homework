class Hotel:
    _prices = {"SGL": 1000, "DBL": 1500, "Junior Suite": 3000, "Suite": 7000}
    _roomsTypes = list(_prices.keys())
    _rooms = dict()

    def __init__(self, num_rooms):
        for i in range(len(num_rooms)):
            self._rooms[self._roomsTypes[i]] = [True for _ in range(num_rooms[i])]

    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, tupe, room_id):
        if self._rooms[tupe][room_id]:
            self._rooms[tupe][room_id] = False  # бронируем номер
        else:
            raise RuntimeError("Номер занят")

    # метод для освобождения номера по уникальному значению в списке
    def free(self, tupe,  room_id):
        self._rooms[tupe][room_id] = True  # освобождаем номер

    def __str__(self):
        a = ''
        for i in self._rooms:
            for j in range(len(self._rooms[i])):
                if self._rooms[i][j] == 0:
                    a += i + ' номер ' + str(j + 1) + " свободен\n"
                else:
                    a += i + ' номер ' + str(j + 1) + " занят\n"
            return a

    def all_occypy(self):
        for i in self._roomsTypes:
            for j in range(len(self._rooms[i])):
                self._rooms[i][j] = False

    def occupy_percentage(self):
        text = "Процент занятых номеров: \n"
        for i in self._roomsTypes:
            text += f"Тип {i}: {round(self._rooms[i].count(0) / len(self._rooms[i]) * 100, 2)}% \n"
        return text

    def all_free(self):
        for i in self._roomsTypes:
            for j in range(len(self._rooms[i])):
                self._rooms[i][j] = True

    def income(self):
        income = 0
        for i in self._roomsTypes:
            income += (self._rooms[i].count(1)) * self._prices[i]
        return income


hotel = Hotel((2, 4, 2, 3))
hotel.occypy("SGL", 1)
hotel.occypy("Junior Suite", 1)
hotel.occypy("Suite", 2)
print(hotel)
print(hotel.occupy_percentage())
print(hotel.income())
hotel.all_occypy()
print(hotel.occupy_percentage())
hotel.all_free()
print(hotel.occupy_percentage())
