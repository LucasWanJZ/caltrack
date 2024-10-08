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
   chmod +x caltrack.py
   ```
4. Optionally, add the script to your PATH for easier access:
   ```
   sudo mv caltrack.py /usr/local/bin/caltrack
   ```

## Command Usage

Command allows you to track your protein and calorie intake across different meals (breakfast, lunch, and dinner).
You can add new amounts, view current totals, and reset data as needed.

### Basic Usage

```
caltrack <command> [amount] [--m <meal>] [--n <nutrient>]
```

### Commands

- `protein`: track or display protein intake
- `calorie`: track or display calorie intake
- `meals`: show the current intake of protein and calorie of a specific meal
- `reset`: reset nutrient data (either `protein`, `calorie` or both)

### Options

- `amount`: The amount of protein (in grams) or calorie (in kcal) to add.
- `--m`: specify the meal to add or show data for. REQUIRED FOR ALL COMMANDS EXCEPT `reset`. {`breakfast`, `lunch`, `dinner`}
- `--n`: specify the nutrient to reset. {`protein`, `calorie`}

## Example

### Add Protein Intake to a Meal

```
caltrack protein 30 --m breakfast
```

Added 30g of protein to your breakfast

```
caltrack protein 2.4*2.5 --m lunch
```

2.4\*2.5g of protein will be calculated first, then add to your lunch.

### Add Calorie Intake to a Meal

```
caltrack calorie 400 --m dinner
```

Added 400kcal to your dinner

### View total protein intake

```
caltrack protein
```

### View total calorie intake

```
caltrack calorie
```

### View Nutrient Intake of a specific Meal

```
caltrack meals --m breakfast
```

view breakfast's nutrient data

### Reset Nutrient Data

```
caltrack reset --n protein
```

reset protein data

```
caltrack reset
```

reset all data

### Future Works

1. Reset Calorie and Protein Intake ✅
2. Able to show breakfast, lunch and dinner's intakes ✅
3. Able to use mathematic expressions as amount input ✅
4. Export to a file
