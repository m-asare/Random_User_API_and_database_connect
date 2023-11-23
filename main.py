"""
Create and connect to a database called Staff.db. Create two tables for teaching and non teaching staff.
Populate both tables using the RandomUser API and save the information to the Staff database. Run queries
to view all entries, view only their last names and print all staff from Ohio State.
"""

import sqlite3
import pandas as pd
from randomuser import RandomUser

# Create and connect to the staff database
conn = sqlite3.connect('Staff.db')

# Create two tables
tableOne = 'Teaching_Staff'
tableTwo = 'Non_Teaching_Staff'


# Function to generate info about the staff
def generate_staff(number):
    """Generate a table with information about the staff"""
    total_people = []
    for people in RandomUser.generate_users(number):
        total_people.append({'Name': people.get_full_name(),
                             'Gender': people.get_gender(),
                             'Age': people.get_age(),
                             'City': people.get_city(),
                             'State': people.get_state(),
                             'Email': people.get_email(),
                             'DOB': people.get_dob(),
                             'Zipcode': people.get_zipcode()})
    return pd.DataFrame(total_people)


# Generate info for tableOne and tableTwo
tbOne = generate_staff(1500)
tbTwo = generate_staff(800)

# Saving both tables to the database
tbOne.to_sql(tableOne, conn, if_exists='replace', index='False')
tbTwo.to_sql(tableTwo, conn, if_exists='replace', index='False')

# Querying the database to view all entries
query_statement = f"SELECT * FROM {tableOne}"
print(query_statement)
query_output = pd.read_sql(query_statement, conn)
print(query_output)
