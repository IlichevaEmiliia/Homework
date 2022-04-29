class Hotel:
    def __init__(self, num_rooms):
        self._rooms = [0 for _ in range(num_rooms)] # информация о статусе номеров
    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, room_id):
        self._rooms[room_id] = 1  # бронируем номер
    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_id):
        self._rooms[room_id] = 0  # освобождаем номер
    
hotel = Hotel(5) # в нашем отеле, например, 5 номеров
print(hotel._rooms) # смотрим номера через атрибут self.rooms
hotel.occypy(3)
print(hotel._rooms)
hotel.free(3)
print(hotel._rooms)
