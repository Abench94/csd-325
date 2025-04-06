import csv
import sys
from datetime import datetime
from pathlib import Path
# I was having trouble getting the working file path to work with the csv file, so I used the pathlib library to get the path of the current script and then append the filename to it.
# This way, the script can be run from any directory without needing to specify the full path to the csv file.

from matplotlib import pyplot as plt

def plot_temperatures(dates, temperatures, color, title):
    """Helper function to plot temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Dynamically construct the file path
base_dir = Path(__file__).parent  # Get the directory of the current script
filename = base_dir / 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

print("This program plots the high and low temperatures in Sitka, Alaska for 2018.\n" \
        "You can choose to see either the high or low temperatures.\n" \
        "Please enter 'h' to see high temperatures, 'l' for lows, or 'e' to exit.")

while True:
    choice = input("Would you like to see the high or low temperature? (h/l/e): ").strip().lower()
    if choice == 'h':
        plot_temperatures(dates, highs, 'red', "Daily High Temperatures - 2018")
    elif choice == 'l':
        plot_temperatures(dates, lows, 'blue', "Daily Low Temperatures - 2018")
    elif choice == 'e':
        print("Thank you for using the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid input. Please enter 'h', 'l', or 'e'.")