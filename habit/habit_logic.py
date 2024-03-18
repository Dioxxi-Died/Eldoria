#imports

import json
import os
from prettytable import PrettyTable

# Json Logic
def write_to_json(file_name, data):
    """
    Write data to a JSON file. If the file exists, it will be opened in write mode
    to clear previous content. If it doesn't exist, a new file will be created.

    Parameters:
        file_name (str): The name of the JSON file.
        data (dict): The data to be written to the file.
    """
    # Check if the file exists
    if os.path.exists(file_name):
        # File exists, open it in write mode to clear previous content
        with open(file_name, "w") as file:
            pass  # Opening the file in write mode clears previous content
        print(f"Opened existing file '{file_name}'")
    else:
        # File doesn't exist, create it
        with open(file_name, "w") as file:
            pass  # Creating an empty file
        print(f"Created new file '{file_name}'")

    # Write data to the file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print("Data written to the file successfully.")

# Sample data to write to the file
sample_data = {
    "habits": [
        {"name": "Exercise", "category": "Health", "completed": False},
        {"name": "Read", "category": "Personal Development", "completed": True},
        {"name": "Drink water", "category": "Health", "completed": False}
    ]
}

# File name
file_name = "habits.json"

# Greeting the user
# Give a little info on what is available

def greeting_traveler():
    print("""
    Hello Traveler! Welcome to your tavern!
    There are so many quests you can go to!
    I know that sometimes the quests on the board aren't what we want,
    so we've added a "Go on your own journey board too!
    """)
    traveler_name = input("""
    Oh dear! I have forgotten to ask your name!
    Silly me. What do you like being called?
    --> """)
    return traveler_name

# Building the quest board

def habit_choice():
    choice_check = False
    print("""
    Do you want to look at the quest board, or do you want to venture to better things?""")
    while choice_check == False:
        choice = input("""
        1. Look at the quest board
        2. Venture out
        --> """)
        if choice == "1":
            view_quest_board()
            choice_check = True
            break
        elif choice == "2":
            structure_habit()
            choice_check = True
            break
        else:
            print("I'm sorry. Could you please choose either option 1 or option 2.")

    return choice

def view_quest_board():
    print("Quest board")

def structure_habit():
    print("""
    Oh! Do you mind sharing?""")
    habit = input("""
    Please type your habit:
    --> """)
    print(habit)

def start_habit():
    # Call the function with the file name and data
    write_to_json(file_name, sample_data)
    traveler_name = greeting_traveler()
    habit_choice()

if __name__== '__main__':
    start_habit()
