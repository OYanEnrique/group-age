# group-age
A Python script that analyzes data from a group of 4 people to calculate the average age, find the oldest man, and count how many women are under 20.

# 📊 People Group Analyzer

This is a command-line Python program that collects and analyzes data from a group of four people. At the end, it provides three statistical insights about the group.

The script asks for the name, age, and sex of each person. During the iterations, it calculates the group's average age, identifies the name of the oldest man, and counts the number of women under 20 years old. This project demonstrates the ability to process multiple data points within a loop and apply complex conditional logic.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `group_age.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python group_age.py
    ```
5.  The program will ask for the name, age, and sex (M/F) of 4 people. Enter the data for each person when prompted.
6.  After entering the data for the fourth person, the program will display the calculated statistics.

## Program Logic

* **Data Collection:** A `for` loop with `range(0, 4)` is used to ensure data from exactly four people is collected. The `.strip()` function is used to remove any unnecessary whitespace from the beginning or end of the text inputs.
* **Average Age Calculation:** A `sum_age` variable accumulates the age of each person. After the loop, the average is calculated by dividing `sum_age` by 4.
* **Finding the Oldest Man:**
    * Inside the loop, the program checks if the sex is 'M'.
    * If it is, it compares the current person's age with the value stored in `age_older_man`.
    * If the current age is greater, the `age_older_man` and `name_older_man` variables are updated with the current person's data.
* **Counting Young Women:**
    * The program checks if the sex is 'F' **and** if the age is less than 20.
    * If both conditions are true, the `total_young_woman` counter is incremented.
* **Final Results:** At the end of the four iterations, the program prints the three calculated results.
