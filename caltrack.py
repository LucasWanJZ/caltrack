#!/usr/bin/env python3

import argparse
import json
import os
import ast
import operator
from datetime import datetime

DATA_FILE = os.path.expanduser("~/.caltrack.json")

# Function to load the stored data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'breakfast': {'protein': 0, 'calorie': 0},
        'lunch': {'protein': 0, 'calorie': 0},
        'dinner': {'protein': 0, 'calorie': 0},
        'protein'
        'last_updated': datetime.now().isoformat()
    }

# Function to save the data
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Function to reset data at midnight
def reset_data(data):
    last_updated = datetime.fromisoformat(data['last_updated'])
    if last_updated.date() < datetime.now().date():
        data['breakfast']['protein'] = 0
        data['lunch']['protein'] = 0
        data['dinner']['protein'] = 0
        data['breakfast']['calorie'] = 0
        data['lunch']['calorie'] = 0
        data['dinner']['calorie'] = 0
        data['last_updated'] = datetime.now().isoformat()
    	
# Calculation
def evaluate_expression(expression):
    try:
        tree = ast.parse(expression, mode='eval')
        return eval(compile(tree, filename="", mode="eval"), {"__builtins__": None}, {
            'x': operator.mul, '*': operator.mul, '/': operator.truediv, '+': operator.add, '-': operator.sub
        })
    except Exception as e:
        raise ValueError(f"Invalid expression: {expression}. Error: {e}")

# Function to reset the protein and calorie intake
def reset_nutrient(nutrient=None):
    data = load_data()
    
    if nutrient:
        comfirmation = input(f"Are you sure you want to reset {nutrient}? (y/n) ")
        if comfirmation.lower() == 'y':
            data['breakfast'][nutrient] = 0
            data['lunch'][nutrient] = 0
            data['dinner'][nutrient] = 0
            print(f"{nutrient.capitalize()} intake has been reset.")
        else:
            print("Cancelled.")
    else:
        comfirmation = input("Are you sure you want to reset all data? (y/n) ")
        if comfirmation.lower() == 'y':
            data['breakfast']['protein'] = 0
            data['lunch']['protein'] = 0
            data['dinner']['protein'] = 0
            data['breakfast']['calorie'] = 0
            data['lunch']['calorie'] = 0
            data['dinner']['calorie'] = 0
            print("All data has been reset.")
        else:
            print("Cancelled.")
    save_data(data)

# Function to track the protein and calorie intake
def track_intake(command, meal=None, amount=None):
    data = load_data()
    reset_data(data)

    unit = 'g' if command == 'protein' else 'kcal'

    if not amount:
        if not meal:
            print(f"Breakfast: {data['breakfast'][command]}{unit}")
            print(f"Lunch: {data['lunch'][command]}{unit}")
            print(f"Dinner: {data['dinner'][command]}{unit}")
            print(f"Total: {data['breakfast'][command] + data['lunch'][command] + data['dinner'][command]}{unit}")
        else:
            print(f"{meal.capitalize()} Protein: {data[meal]['protein']}g")
            print(f"{meal.capitalize()} Calorie: {data[meal]['calorie']}kcal")
    else:
        data[meal][command] += amount
        print(f"{amount}{unit} of {command} has been added to {meal}.")

    save_data(data)

def main():
    parser = argparse.ArgumentParser(description="Track your protein and calorie intake.")
    parser.add_argument('command', choices=['protein','calorie','meals','reset'], help="Choose a command to execute")
    parser.add_argument('amount', type=str, nargs='?', help="The amount of protein or calorie to add")
    parser.add_argument('--m', choices=['breakfast','lunch','dinner'], help="The meal to add or show the protein or calorie")
    parser.add_argument('--n', choices=['protein','calorie'], help="The nutrient to reset")

    args = parser.parse_args()

    if args.command == 'meals' and not args.m:
        parser.error("--m option is required for the 'meals' command")
    
    if args.amount and not args.m:
        parser.error("--m option is required when adding protein or calorie")

    if args.command == 'reset':
        reset_nutrient(args.n)
    elif args.amount is None:
        track_intake(args.command, args.m)
    else:
        try:
            calculated_amount = round(evaluate_expression(args.amount),2)
            track_intake(args.command, args.m, calculated_amount)
            
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
