#!/usr/bin/env python3
import copy
from dataclasses import dataclass


class Date:

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def copy(cls, instance):
        return cls(instance.get_day(), instance.get_month(), instance.get_year())

    def get_year(self) -> int:
        return self._year

    def get_month(self) -> int:
        return self._month

    def get_day(self) -> int:
        return self._day

    def equals(self, instance) -> bool:
        return self.equals(instance)

    def before(self, instance) -> bool:
        if self._year > instance.get_year:
            return False
        if self._year < instance.get_year:
            return True
        if self._month > instance.get_month:
            return False
        if self._month < instance.get_month:
            return True
        if self._day > instance.get_day:
            return False
        if self._day < instance.get_day:
            return True
        return False

    def after(self, instance) -> bool:
        if equals(instance):
            return False
        return not before(instance)

    def compute_days(self, date: Date) -> int:
        # If it is a leap year.
        if date.get_year % 4 == 0 and date.get_year % 100 != 0:
            if date.get_month == 1:
                return (31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 2:
                return (29 + 31 + (date.get_year * 365)) - (29 - date.get_day)
            if date.get_month == 3:
                return (31 + 29 + 31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 4:
                return (30 + 31 + 29 + 31 + (date.get_year * 365)) - (30 - date.get_day)
            if date.get_month == 5:
                return (31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 6:
                return (30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (30 - date.get_day)
            if date.get_month == 7:
                return (31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 8:
                return (31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 9:
                return (30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (30 - date.get_day)
            if date.get_month == 10:
                return (31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) - (31 - date.get_day)
            if date.get_month == 11:
                return (30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) \
                       - (30 - date.get_day)
            if date.get_month == 12:
                return (31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 29 + 31 + (date.get_year * 365)) \
                       - (31 - date.get_day)

        if date.get_month == 1:
            return (31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 2:
            return (28 + 31 + (date.get_year * 365)) - (28 - date.get_day)
        if date.get_month == 3:
            return (31 + 28 + 31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 4:
            return (30 + 31 + 28 + 31 + (date.get_year * 365)) - (30 - date.get_day)
        if date.get_month == 5:
            return (31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 6:
            return (30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (30 - date.get_day)
        if date.get_month == 7:
            return (31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 8:
            return (31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 9:
            return (30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (30 - date.get_day)
        if date.get_month == 10:
            return (31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (31 - date.get_day)
        if date.get_month == 11:
            return (30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) - (30 - date.get_day)
        if date.get_month == 12:
            return (31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31 + (date.get_year * 365)) \
                   - (31 - date.get_day)

    def difference(self, instance) -> int:
        if equals(instance):
            return 0
        return abs(compute_days(self) - compute_days(instance))

    def print_date(self) -> str:
        return '(' + f'{self._day}' + '/' + f'{self._month}' + '/' + f'{self._year}' + ')'


class Student(Date):
    def __init__(self, name: str, day: int, month: int, year: int):
        super().__init__(day, month, year)
        self._name = name

    def get_birthday(self) -> Date:
        return self._date

    def get_name(self) -> str:
        return self._name

    def equals(self, instance) -> bool:
        return self.equals(instance)

    def print_student(self) -> str:
        return self._name + '\n' + self.print_date()


class Group(Student):
    def __init__(self, max_students: int, stud: List[Student], no_of_students: int):
        self._max_students = max_students
        self._stud = stud
        self._no_of_students = no_of_students

    def get_students(self) -> List[str]:
        return self._stud

    def get_no_of_students(self) -> int:
        return self._no_of_students

    def add_student(self, student: Student):
        if self._no_of_students + 1 <= self._max_students:
            self._stud.appened(student)
            self._no_of_students += 1

    def remove_student(self, name: str, d: int, m: int, y: int):
        date: Date = Date(d, m, y)
        for student in self._stud:
            if not student.get_name.equals(name):
                continue
            if not student.get_birthday.equals(date):
                continue
            self._stud.remove(student)

    def print_group(self) -> str:
        s: str = ''
        for student in self._stud:
            s += student.print_student() + '\n'
        return s

    def sort(self) -> List[Student]:
        sorted_list: List[Student] = sorted(self._stud, key=lambda student: Student.get_birthday.get_year)
        return sorted_list

    def how_many_months(self) -> int:
        counter: int = 12
        list_of_months: List[int] = []
        for student in self._stud:
            if student.get_birthday.get_month in list_of_months:
                continue
            list_of_months.append(student.get_birthday.get_month)
        for i in range(1, 13):
            if i in list_of_months:
                continue
            counter += 1
        return counter

    def bigger_than(self, num: int) -> bool:
        for j in range(0, len(self._stud) - 1):
            for i in range(1, len(self._stud)):
                if not self._stud[j].difference(self._stud[i]) >= num:
                    continue
                return True
        return False

# d = Date(1, 2, 3)
# c = Date.copy(d)
# print(d, c)
# print(c.print_date())
