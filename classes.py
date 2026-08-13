from __future__ import annotations
from abc import ABC, abstractmethod
from helpers import clamp
from random import randint, random, choices
import typing
import logger





class Item(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        pass

    def Rot() -> None:
        pass


class Food(Item):
    def __init__(self, nutricional_value: int, size: int, name: str) -> None:
        super().__init__(name)
        self.nutricional_value = nutricional_value
        self.size = size



class Meat(Food):
    def __init__(self, nutricional_value: int, size: int, name: str, avg_size: int):
        size_modifier = round(size / avg_size)
        nutricional_value = nutricional_value * size_modifier
        self.size = randint(round(avg_size - avg_size / 2), round(avg_size + avg_size / 2))
        super().__init__(nutricional_value, size, name)

class RabbitMeat(Meat):
    def __init__(self, size: int=0, nutricional_value: int=10, name: str = "Rabbit Meat", avg_size: int = 40) -> None:
        super().__init__(nutricional_value, size, name, avg_size)

class DeerMeat(Meat):
    def __init__(self, size: int=0, nutricional_value: int=30, name: str = "Deer Meat", avg_size: int = 90) -> None:
        super().__init__(nutricional_value, size, name, avg_size)

class BoarMeat(Meat):
    def __init__(self, size: int=0, nutricional_value: int=20, name: str = "Boar Meat", avg_size: int = 75) -> None:
        super().__init__(nutricional_value, size, name, avg_size)
    


class LifeForm(ABC):
    def __init__(self, health: int, size: int, gender: str, max_hunger: int, species_name: str) -> None:
        self.species_name = species_name
        self.size = size
        self.health = health
        self.gender = gender
        self.max_hunger = max_hunger
        self.current_hunger = max_hunger
        self.max_health = health
        self.alive = True
    
    @abstractmethod
    def die(self) -> None:
        logger.Write_Logs__To_text_File(f"{self.species_name} has died!")
        self.alive = False
        pass

    def take_damage(life_form: LifeForm, damage: int) -> None:
        life_form.health = clamp(life_form.health - damage, 0, life_form.max_health)
        if life_form.health == 0:
            life_form.die()

    @abstractmethod
    def lose_hunger(self) -> None:
        pass
    
    @abstractmethod
    def eat(self, food: Food) -> None:
        logger.Write_Logs__To_text_File(f"{self.species_name} ate a {food.name}")
        self.current_hunger = clamp(self.current_hunger + food.nutricional_value, 0, self.max_hunger)
        pass



class Animal(LifeForm):
    def Eat(self, food: Food) -> None:
        pass


class Human(LifeForm):
    def __init__(self, health: int, size: int, gender: str, max_hunger: int = 100, species_name: str = "Human") -> None:
        super().__init__(health, size, gender, max_hunger, species_name)
        self.civilization: Civilization = None
    
    def hunt(self) -> tuple[bool, typing.Optional[Food]]:
        if random() < 0.5:
            reward_class = choices([food for food, _ in hunt_rewards], weights=[weight for _, weight in hunt_rewards])[0]
            reward = reward_class()
            return True, reward
        else:
            return False, None
    
    def die(self) -> None:
        super().die()
        self.civilization.remove_human(self)

    def lose_hunger(self) -> None:
        benchmark = randint(8, 12)
        size_modifier = (self.size / 170) * 1.2
        hunger_lost = round(benchmark * size_modifier)

        self.current_hunger = clamp(self.current_hunger - hunger_lost, 0, self.max_hunger)

    def eat(self, food: Food) -> None:
        super().eat(food)
        self.civilization.remove_from_inventory(food)
        
        



class Civilization:
    def __init__(self, Initial_humans: list[Human]) -> None:
        self.inventory: dict[Item, int] = {}
        self.human_list: list[Human] = []
        for human in Initial_humans:
            self.add_human(human)

    def add_human(self, human: Human) -> None:
        self.human_list.append(human)
        human.civilization = self
    
    def remove_human(self, human: Human) -> None:
        self.human_list.remove(human)
    
    def add_to_inventory(self, item: Item, quantity: int = 1) -> None:
        for inventory_item in self.inventory:
            if inventory_item.name == item.name:
                self.inventory[inventory_item] += quantity
                return

        self.inventory[item] = quantity
    
    def remove_from_inventory(self, item: Item, quantity: int = 1) -> None:
        if item not in self.inventory:
            return

        self.inventory[item] -= quantity

        if self.inventory[item] <= 0:
            del self.inventory[item]


# LOOT SETS

hunt_rewards: tuple[Food, float] = [
    (RabbitMeat, 0.60),
    (DeerMeat, 0.25),
    (BoarMeat, 0.15),
]