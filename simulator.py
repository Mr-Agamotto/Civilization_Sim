#!/usr/bin/env python3

import math
from abc import ABC
from typing import Iterator
from classes import Human, Civilization
from random import random, randint, choice



def generate_day() -> Iterator[int]:
    Day_Count: int = 0
    civilization = yield
    while True:
        Day_Count += 1
        civilization = yield Day_Count
        for human in civilization.Humans:
            human_day(human)

def human_day(human: Human) -> None:
    if random() < 0.5:
        hunt_bool, reward = human.hunt()
        if hunt_bool:
            Write_Logs__To_text_File(f"Hunt by {human.species_name} was a success! gained one {reward.name}\n")
        else: 
            Write_Logs__To_text_File(f"Hunt by {human.species_name} was a failure, gained nothing\n")

def reset_logs():
    open("Logs.txt", "w").close()


def Write_Logs__To_text_File(content: str) -> None:
    """Write a line to the Logs.txt file"""
    File_Object = open("Logs.txt", "a")
    File_Object.write(content)
    File_Object.close()


def main() -> None:
    reset_logs()
    initial_humans: list[Human] = []
    initial_humans.append(Human(100, 180, "M"))
    civilization = Civilization(initial_humans)
    Day_count: int = 0
    day = generate_day()
    next(day)
    Day_count = day.send(civilization)
    Write_Logs__To_text_File(f"Day: {str(Day_count)}" + '\n')
    for i in range(0, 10):
        Day_count = day.send(civilization) 
        Write_Logs__To_text_File(f"Day: {str(Day_count)}" + '\n')

if __name__ == "__main__":
    main()
