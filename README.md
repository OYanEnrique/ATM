# ATM
A Python script that simulates an ATM, calculating the optimal number of banknotes for a given withdrawal amount.

# 🏧 ATM Banknote Calculator

A simple command-line Python script that simulates an ATM withdrawal by calculating the minimum number of banknotes required for a specific amount.

This program asks the user for a monetary value to withdraw and, based on the available banknotes ($50, $20, $10, and $1), it calculates and displays how many of each note should be dispensed.

## Features

* **Withdrawal Simulation**: A straightforward interface to enter any withdrawal amount.
* **Optimal Banknote Calculation**: Uses a greedy algorithm to provide the fewest possible banknotes, prioritizing higher denominations.
* **Simple Command-Line Interface**: Easy to run and use directly from any terminal.

## How to Use

1.  Ensure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `ATM.py`).
3.  Run the script from your terminal:
    ```sh
    python ATM.py
    ```
4.  When prompted, enter the total amount of money you wish to withdraw.
5.  The script will print out the number of each banknote you will receive.

## Program Logic

The script determines the number of banknotes using a "greedy" approach:

1.  It starts with the largest banknote denomination ($50).
2.  It uses integer division (`//`) to find out how many of that banknote fit into the total amount.
3.  It then uses the modulo operator (`%`) to calculate the remaining amount.
4.  This remaining amount is then passed down to the next smaller banknote denomination ($20), and the process repeats until it reaches the $1 banknote.
