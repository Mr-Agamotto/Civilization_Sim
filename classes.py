import math
from abc import ABC, abstractmethod
from random import randint, random
import typing




class Items(ABC):
    def __init__(self) -> None:
        pass

    def Rot() -> None:
        pass


class Food(Items):
    def __init__(self, nutricional_value: int, size: int, name: str) -> None:
        self.nutricional_value = nutricional_value
        self.size = size
        self.name = name



class Meat(Food):
    def __init__(self, nutricional_value: int, size: int, name: str):
        super().__init__(nutricional_value, size, name)

class RabbitMeat(Meat):
    def __init__(self, nutricional_value: int, size: int, name: str = "Rabbit Meat"):
        super().__init__(nutricional_value, size, name)
    


class LifeForm(ABC):
    def __init__(self, health: int, size: int, gender: str, species_name: str) -> None:
        self.species_name = species_name
        self.size = size
        self.health = health
        self.gender = gender
    
    def Die() -> None:
        pass



class Animal(LifeForm):
    def Eat(self, food: Food) -> None:
        pass


class Human(LifeForm):
    def __init__(self, health: int, size: int, gender: str, species_name: str = "Human") -> None:
        super().__init__(health, size, species_name, gender)
    
    def hunt(self) -> tuple[bool, typing.Optional[Food]]:
        if random() < 0.5:
            reward = RabbitMeat(10, 10)
            return True, reward
        else:
            return False, None



class Civilization:
    def __init__(self, Initial_humans: list[Human]) -> None:
        self.Humans: list[Human] = Initial_humans


