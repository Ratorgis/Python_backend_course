# ustin lambda function
b = [1, 2, 3, 4, 5]
s = list(map(lambda x: x ** 2, b))
print(s)

# Class
class Student:
    def __init__(self, name: str, age: int = 18) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'name: {self.name} and age: {self.age}'

class Graduated_student(Student):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.__diploma_mark = 0
    
    def __str__(self):
        return f'name: {self.name} and graduated year {self.age}'
    
    def set_mark(self, mark: int) -> None:
        self.__diploma_mark = mark
    
    def get_mark(self) -> int:
        return f'{self.name} mark is {self.__diploma_mark}'

def print_name(person):
    return print(person.name)

Max = Student('Max')
print_name(Max)

# dataclass
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
    balance: int

    def has_money(self) -> bool:
        return self.balance > 0

# Декораторы






