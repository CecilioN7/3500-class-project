# course: cmps3500
# CLASS Project
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# date: 04/19/24
# Student 1: Cecilio Navarro
# Student 2: Oscar Rocha
# Student 3: Isaac Mendez
# Student 4: Francisco Serrato
# description: Implementation Basic Data Analysis Routines

import time
import pandas as pd

program_start_time = time.time()

# question 3 method
def get_state_with_most_severity_2_accidents():
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv('US_Accidents_data.csv')

        # Filter the DataFrame to include only severity 2 accidents
        severity_2_accidents = df[df['Severity'] == 2]

        # Group by state and count the number of severity 2 accidents in each state
        state_accident_counts = severity_2_accidents['State'].value_counts()

        # Get the state with the maximum number of severity 2 accidents
        state_with_most_accidents = state_accident_counts.idxmax()

        return state_with_most_accidents

    except FileNotFoundError:
        print("Error: File not found.")

# question 4 method
def get_most_common_severity_for_states(states):
    try:
        df = pd.read_csv('US_Accidents_data.csv')
        states_data = df[df['State'].isin(states)]
        most_common_severity = states_data.groupby('State')['Severity'].agg(pd.Series.mode)
        return most_common_severity
    except FileNotFoundError:
        print("Error: File not found.")

# question 8 method
def NH_data(data):
    try:
        #only loads data from New Hampshire
        NH_data = data[data['State'] == 'NH']
    
        #collects data from New Hampshire accidents with a severity of 2
        NH_severity2 = NH_data[NH_data['Severity'] == 2]
    
        #print info
        print("8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?\n")
        print("Max visibility of accidents in New Hampshire with a severity of 2: ")
        print(NH_severity2[Visibility(mi).max())
        print("\n")
    
    except FileNotFoundError:
        print("Error: File not found.")

# question 9 method
def accident_severity_annually(data):
    try:
        #start time
        start_time = time.time()
    
        #collect only bakersfield data
        bakersfield_accidents = data[data['City'] == 'Bakersfield'].copy()
    
        #years
        severity_by_year = bakersfield_accidents.groupby(['Severity', 'Year']).size().unstack(fill_value = 0)
    
        #end time
        end_time = time.time()
    
        #total time
        total_time = end_time - start_time
    
        #display info
        print("9. How many accidents of each severity were recorded in Bakersfield? Display the data per year.\n")
    
        print(severity_by_year)
        print("\nTime to execute: ", total_time, "seconds\n")

    except FileNotFoundError:
        print("Error: File not found.")

# question 10 method    
def longest_accident_time(data):
    try:
        #start time
        start_time = time.time()
    
        #collect only las vegas data between march, april, and may
        LV_data = data[data['City'] == 'Las Vegas']
        spring_szn = LV_data[LV_data['Start_Time'].dt.month.isin([3, 4, 5])]
    
        #how long the accident lasted
        spring_szn ['Accident_Time'] = spring_szn['End_Time'] - spring_szn['Start_Time'].dt.total_seconds() / 3600
    
        #by year
        by_year = spring_szn.groupby(spring_szn['Start_Time'].dt.year)
        longest_accident_yearly = by_year['Accident_Time'].max()
    
        print("10. What was the longest accident (in hours) recorded in Las Vegas in the Spring (March, April, and May)? Display the data per year.\n")
        print("Longest accident per year: ")
        for year, duration in longest_accident_yearly.items():
            print(f"Year {year}: {duration:.2f} hours")
        print("\n")
    
    except FileNotFoundError:
        print("Error: File not found.")
        
def option1():
    print()
    print("Loading and cleaning input data set:")
    print("************************************")
    print(f"[{time.strftime('%H:%M:%S')}] Starting Script")
    print(f"[{time.strftime('%H:%M:%S')}] Loading US_Accidents_data.csv")

    start_time = time.time()  # Record start time
    
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv('US_Accidents_data.csv')
        
        # Get total columns and rows
        total_columns = df.shape[1]
        total_rows = df.shape[0]

        print(f"[{time.strftime('%H:%M:%S')}] Total Columns Read: {total_columns}")
        print(f"[{time.strftime('%H:%M:%S')}] Total Rows Read: {total_rows}")

    except FileNotFoundError:
        print("Error: File not found.")

    end_time = time.time()  # Record end time
    time_to_load = end_time - start_time  # Calculate time taken
    print(f"\nTime to load is:  {time_to_load:.2f} seconds")
    
def option2():
    print()
    print("Processing input data set:")
    print("**************************")
    print(f"[{time.strftime('%H:%M:%S')}] Performing Data Clean Up")

    start_time = time.time()
    
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv('US_Accidents_data.csv')
        
        # Drop rows with missing values in specified columns
        df.dropna(subset=['ID', 'Severity', 'Zipcode', 'Start_Time', 'End_Time', 'Visibility(mi)', 'Weather_Condition', 'Country'], inplace=True)
        
        # Drop rows with empty values in 3 or more columns
        df.dropna(thresh=5, inplace=True)
        
        # Consider only the first 5 digits of the zip code
        df['Zipcode'] = df['Zipcode'].astype(str).str[:5]
        
        # Drop rows with distance equal to zero
        df = df[df['Distance(mi)'] != 0]
        
        # Drop rows where the duration of the accident is zero
        df = df[df['End_Time'] != df['Start_Time']]
        
        total_rows_after_cleaning = len(df)
        print(f"[{time.strftime('%H:%M:%S')}] Total Rows Read after cleaning is: {total_rows_after_cleaning}")
        
    except FileNotFoundError:
        print("Error: File not found.")

    end_time = time.time()
    time_to_process = end_time - start_time
    print(f"\nTime to process is:  {time_to_process:.2f} seconds")

def option3():
    print()
    print("Answering questions:")
    print("********************")
    print(f"[{time.strftime('%H:%M:%S')}] 3) What is the state that had the most accidents of severity 2?")
    
    start_time = time.time()
    
    state_with_most_accidents = get_state_with_most_severity_2_accidents()
    if state_with_most_accidents:
        print(f"[{time.strftime('%H:%M:%S')}] {state_with_most_accidents}")

    end_time = time.time()
    time_to_answer = end_time - start_time
    print(f"\nTime to answer is:  {time_to_answer:.2f} seconds")

    print()
    print(f"[{time.strftime('%H:%M:%S')}] 4) What severity is the most common in Virginia, California, and Florida?")
    
    start_time = time.time()
    
    states = ['VA', 'CA', 'FL']
    most_common_severity = get_most_common_severity_for_states(states)
    if most_common_severity is not None:
        for state, severity in most_common_severity.items():
            print(f"[{time.strftime('%H:%M:%S')}] {state}: {severity}")

    end_time = time.time()
    time_to_answer = end_time - start_time
    print(f"\nTime to answer is:  {time_to_answer:.2f} seconds")

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
