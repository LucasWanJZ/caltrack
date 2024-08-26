# caltrack

caltrack is a simple command-line tool to help you track your daily intake of protein and calories. It automatically resets your intake data at midnight, ensuring that you always have an accurate record of your daily consumption.

## Features
- Track protein and calorie intake easily through the command line.
- Automatically resets daily intake at midnight.
- Lightweight and minimal dependencies.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/LucasWanJZ/caltrack.git
   cd caltrack
   ```
2. Ensure that you have Python 3 installed
3. Make the script executable
   ```
   chomod +x caltrack.py
   ```
4. Optionally, add the script to your PATH for easier access:
   ```
   sudo mv caltrack.py /usr/local/bin/caltrack
   ```
   
## Usage 
You can use Caltrack to track your protein and calorie intake throughout the day 

### Track Protein Intake
To add a specific amount of protein (in grams) to your daily total
```
caltrack protein 25
```

If you want to check your current protein intake:
```
caltrack protein
```

### Track Calorie Intake 
to add a specific amount of calories:
```
caltrack calorie 355
```
if you want to check your current calorie intake:
```
caltrack calorie
```

### Future Works
1. Reset Calorie and Protein Intake
2. Export to a file
3. Able to see breakfast, lunch and dinner's intakes

