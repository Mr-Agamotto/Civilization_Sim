#!/usr/bin/env python3

import sys
from helpers import clamp
from classes import Human, Civilization, Item, Food
from random import random, choice
from logger import Write_Logs__To_text_File, error_message, reset_logs

DEFAULT_DAYS = 100

def generate_day(civilization: Civilization, day_count: int) -> int:
    day_count += 1
    for human in civilization.human_list:
        human_day(human)
    return day_count


def human_day(human: Human) -> None:
    #Hunger tick
    human.lose_hunger()

    #Human eating event
    if human.current_hunger < human.max_hunger:
        food_list: list[Food] = [key for key in human.civilization.inventory.keys() if isinstance(key, Food)]
        if food_list:
            human.eat(choice(food_list))
        Write_Logs__To_text_File(f"{human.species_name}'s currect hunger is {human.current_hunger}")
        

    #Low hunger damage tick
    if human.current_hunger < 30:
        Write_Logs__To_text_File(f"{human.species_name} is starving! health lowers")
        human.take_damage(10)

    if not human.alive:
        return
    
    #Hunting event
    if random() < 0.5:
        hunt_bool, reward = human.hunt()
        if hunt_bool:
            Write_Logs__To_text_File(f"Hunt by {human.species_name} was a success! gained one {reward.name}")
            human.civilization.add_to_inventory(reward)
        else: 
            Write_Logs__To_text_File(f"Hunt by {human.species_name} was a failure, gained nothing")



def get_max_days(argv: list[str]) -> int:
    number_of_days_to_simulate: int
    if len(argv) > 2:
        error_message(
            "Error: The program accepts only one argument.\n"
            "Usage: ./simulator.py <number_of_days>"
        )
    if len(argv) == 1:
        return DEFAULT_DAYS
    try:
        number_of_days_to_simulate = int(argv[1])
    except ValueError:
        error_message("Error: Please provide a valid integer for the number of days to simulate, or omit the argument to use the default value.")
    return number_of_days_to_simulate



def main() -> None:
    reset_logs()

    initial_humans: list[Human] = []
    initial_humans.append(Human(100, 180, "M"))
    civilization = Civilization(initial_humans)

    day_count: int = 0
    number_of_days_to_simulate: int = get_max_days(sys.argv)

    Write_Logs__To_text_File(f"--------------------Day: {str(day_count)}--------------------" + '\n')
    day_count = generate_day(civilization, day_count)
    
    civ_dict: dict[str, int] = {item.name: quantity for item, quantity in civilization.inventory.items()}
    Write_Logs__To_text_File(f"{civ_dict}")

    for i in range(0, number_of_days_to_simulate - 1):
        Write_Logs__To_text_File('\n' + f"--------------------Day: {str(day_count)}--------------------" + '\n')

        day_count = generate_day(civilization, day_count)

        civ_dict: dict[str, int] = {item.name: quantity for item, quantity in civilization.inventory.items()}
        Write_Logs__To_text_File(f"{civ_dict}")

if __name__ == "__main__":
    main()
