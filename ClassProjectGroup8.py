# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 04/19/24
# Student 1: Cecilio Navarro
# Student 2: Oscar Rocha
# Student 3: Isaac Mendez
# Student 4: 
# description: Implementation Basic Data Analysis Routines

import time

program_start_time = time.time()

def option1():
    print()
    print("Loading and cleaning input data set:")
    print("************************************")
    print(f"[{time.strftime('%H:%M:%S')}] Starting Script")
    print(f"[{time.strftime('%H:%M:%S')}] Loading US_Accidents_data.csv")
    total_columns = "<Your Answer>"
    total_rows = "<Your Answer>"
    print(f"[{time.strftime('%H:%M:%S')}] Total Columns Read: {total_columns}")
    print(f"[{time.strftime('%H:%M:%S')}] Total Rows Read: {total_rows}")

    start_time = time.time()
    end_time = time.time()
    time_to_load = end_time - start_time
    print(f"\nTime to load is:  {time_to_load:.2f} seconds")

def option2():
    print()
    print("Processing input data set:")
    print("**************************")
    print(f"[{time.strftime('%H:%M:%S')}] Performing Data Clean Up")
    print(f"[{time.strftime('%H:%M:%S')}] Total Rows Read after cleaning is: <Your Answer>")

    start_time = time.time()
    end_time = time.time()
    time_to_process = end_time - start_time
    print(f"\nTime to process is:  {time_to_process:.2f} seconds")

def option3():
    print()
    print("Answering questions:")
    print("********************")
    print(f"[{time.strftime('%H:%M:%S')}] In what month were there more accidents reported?")
    print(f"[{time.strftime('%H:%M:%S')}] <Your Answer>")
    print(".\n.\n.")
    print(f"[{time.strftime('%H:%M:%S')}] What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?")
    print(f"[{time.strftime('%H:%M:%S')}] <Your Answer>")

def option4():
    print()
    print("Search Accidents:")
    print("*****************")
    print("Enter a State name: <User Input>")
    print("Enter a City name: <User Input>")
    print("Enter a ZIP Code: <User Input>")
    print("\nThere where <User Input> accidents.")

    start_time = time.time()
    end_time = time.time()
    time_to_search = end_time - start_time
    print(f"\nTime to perform search is:  {time_to_search:.2f} seconds")

def option5():
    print()
    print("Search Accidents:")
    print("*****************")
    print("Enter a Year: <User Input>")
    print("Enter a Month name: <User Input>")
    print("Enter a Day: <User Input>")
    print("\nThere where <User Input> accidents.")

    start_time = time.time()
    end_time = time.time()
    time_to_search = end_time - start_time
    print(f"\nTime to perform search is:  {time_to_search:.2f} seconds")

def option6():
    print()
    print("Search Accidents:")
    print("*****************")
    print("Enter a Minimum Temperature (F): <User Input>")
    print("Enter a Maximum Temperature (F): <User Input>")
    print("Enter a Minimum Visibility (mi): <User Input>")
    print("Enter a Maximum Visibility (mi): <User Input>")
    print("\nThere where <User Input> accidents.")

    start_time = time.time()
    end_time = time.time()
    time_to_search = end_time - start_time
    print(f"\nTime to perform search is:  {time_to_search:.2f} seconds")

def exit_menu():
    end_time = time.time()
    total_time = (end_time - program_start_time) / 60
    print()
    print(f"Total Running Time (In Minutes): {total_time:.2f}")
    exit()

menu_options = {
    "1": option1,
    "2": option2,
    "3": option3,
    "4": option4,
    "5": option5,
    "6": option6,
    "q": exit_menu
}

def display_menu():
    print("-------------------------------------------------------------")
    print("(1) Load data")
    print("(2) Process data")
    print("(3) Print Answers")
    print("(4) Search Accidents (Use City, State, and Zip Code)")
    print("(5) Search Accidents (Year, Month and Day)")
    print("(6) Search Accidents (Temperature Range and Visibility Range)")
    print("(Q) Quit")

def main():
    while True:
        display_menu()
        print()
        choice = input("Select an option: ").lower()
        if choice in menu_options:
            menu_options[choice]()
        else:
            print()
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()