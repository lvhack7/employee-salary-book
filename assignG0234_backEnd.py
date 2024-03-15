import pandas as pd
import re
import os

def add_entry():
    while True:
        # Collect user input
        name = input("Enter employee name: ")
        dept = input("Enter department name: ")
        y_of_exp_str = input("Enter years of experience: ")
        salary_str = input("Enter annual salary (USD): ")

        # Validate inputs using regular expressions
        if not re.match("^[a-zA-Z\s]+$", name):
            print("Error: Name must not contain digits.")
            return
        if not re.match("^[a-zA-Z\s]+$", dept):
            print("Error: Department name must not contain digits.")
            return
        try:
            y_of_exp = int(y_of_exp_str)
            salary = float(salary_str)
            if y_of_exp < 0 or salary < 0:
                raise ValueError
        except ValueError:
            print("Error: Years of experience and salary should be positive numerical values.")
            return

        # Creating a dictionary for the entry with all corresponding keys
        data = {
            'Name': [name], 
            'Years of Exp': [y_of_exp], 
            'Department Name': [dept], 
            'Annual Salary': [salary]
        }
        
        # Add entry to DataFrame
        df = pd.DataFrame(data)

        # Check if CSV file exists
        if os.path.isfile('salary_book.csv'):
            try:
                existing_df = pd.read_csv('salary_book.csv')

                # Creating a List with existing Dataframe and new Entry
                updated_df_list = [existing_df]

                # Appending new data to the list
                updated_df_list.append(df)

                # Concatenating the dataframe with new entry
                updated_df = pd.concat(updated_df_list, ignore_index=True)
            except pd.errors.EmptyDataError:
                updated_df = df
        else:
            updated_df = df

        # Write updated DataFrame to CSV
        updated_df.to_csv('salary_book.csv', index=False)
        print("Message: Entry added successfully.")
        return

def view_entries():
    # Checking if file exists
    if os.path.isfile('salary_book.csv'):
        # Wrapping try except to ensure error prevention 
        try:
            df = pd.read_csv('salary_book.csv')
            if df.empty:
                print("Message: Salary book is empty.")
            else:
                print(df)
        except pd.errors.EmptyDataError:
            print('Message: Salary book file is empty')
        
    else:
        print("Message: Salary book is empty.")

def delete_entries():
    if os.path.isfile('salary_book.csv'):
        try:
            df = pd.read_csv('salary_book.csv')
            if df.empty:
                print("Message: Salary book is already empty.")
            else:
                # Truncating the file using file read/write functionality
                f = open("salary_book.csv", "w")
                f.truncate()
                f.close()
                print("Message: Deleted all entries successfully.")
        except pd.errors.EmptyDataError:
            print('Message: Salary book file is already empty')
    else:
        print("Message: Salary book is already empty.")

