# 📊 Group Data Analyzer

This is a command-line Python program that continuously collects and analyzes data from a group of people. The user can enter data for as many people as they wish and then see the final statistical results.

The script repeatedly asks for the name, age, and gender of each person. After the user decides to stop, the program calculates the group's average age, the total number of adults (18+), the total number of men, and the total number of women aged 20 or younger.

## Features

* **Flexible Data Entry**: Unlike the previous version, there is no limit to the number of people you can add.
* **User-Controlled Loop**: The program will ask if you want to continue after each entry, giving you full control.
* **Multiple Statistics**: Provides a summary of the group's demographics upon completion.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `group_analyzer.py`).
3.  Run the script from your terminal:
    ```sh
    python group_analyzer.py
    ```
4.  The program will ask for the name, age, and gender of the first person.
5.  After each person's data is entered, you will be asked `Continue? [Y or N]`.
6.  Enter `Y` to add another person or `N` to stop and see the results.
7.  Once you enter `N`, the program will display the final calculated statistics.

## Program Logic

* **Data Collection**: A `while True` loop is used for continuous data entry.
* **Loop Control**: The loop breaks when the user inputs 'N' to the "Continue?" prompt.
* **Calculations**:
    * Counters are used to track the number of adults (`age >= 18`), men (`gender == 'M'`), and young women (`gender == 'F' and age <= 20`).
    * The total age and total number of people are summed up with each iteration to calculate the average age at the end.
* **Final Results**: After the loop terminates, the program prints a formatted string containing all the calculated results.
