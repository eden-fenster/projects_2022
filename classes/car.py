#!/usr/bin/env python3
class Car:

    def __init__(self, comp: str, model: str, ide: str, price: float, owners: int):
        self._comp = comp
        self._model = model
        self._id = ide
        self._price = price
        self._owners = owners

    def get_price(self) -> float:
        return self._price

    def get_owners(self) -> int:
        return self._owners

    def set_price(self, x: float):
        self._price = x

    def sell_car(self):
        self._owners += 1

    def car_details(self) -> str:
        return f'company: {self._comp} \n' \
               f'model: {self._model} \n' \
               f'id: {self._id} \n' \
               f'price: {self._price} \n' \
               f'owners: {self._owners}'


car = Car(comp='Toyota', model='Corolla', ide='12t386w', price=10000, owners=6)
car.sell_car()
print(car.car_details())
