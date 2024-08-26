#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.expanduser("~/.caltrack.json")

# Functions to store and load datas
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'protein': 0, 'calorie': 0, 'last_updated': datetime.now().isoformat()}


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


# Function to reset data at midnight
def reset_data(data):
    last_updated = datetime.fromisoformat(data['last_updated'])
    if last_updated.date() < datetime.now().date():
        data['protein'] = 0
        data['calorie'] = 0
    data['last_updated'] = datetime.now().isoformat()

# Function to track protein and calories intakes
def track_intake(nutrient, amount=None):
    data = load_data()
    reset_data(data)

    if amount is not None:
        data[nutrient] += amount
        print(f"Added {amount}g to {nutrient}. Total: {data[nutrient]}g")
    else:
        print(f"Current {nutrient} intake: {data[nutrient]}g")

    save_data(data)

# main function
def main():
    parser = argparse.ArgumentParser(description="Track your protein and calorie intake.")
    parser.add_argument('nutrient', choices=['protein', 'calorie'], help="The nutrient to track (protein or calorie)")
    parser.add_argument('amount', type=float, nargs='?', help="The amount of the nutrient")

    args = parser.parse_args()

    track_intake(args.nutrient, args.amount)

if __name__ == "__main__":
    main()

