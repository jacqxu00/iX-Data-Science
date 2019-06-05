# -*- coding: utf-8 -*-
"""
Jacqueline Xu
iXperience Tel Aviv
26 May 2019
Introduction to Python Assignment
"""

#%%

"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data 
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a
script with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information

Given a neighbourhood, the tool will provide the following information to the user:
- Total number of available listings in the neighbourhood
- Number of rooms broken down per listing type
- Average Room Price
- Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belem"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.

This functionality will help the user to find an appropriate listing. It will
ask the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesn't specifiy any of the requirements (pressing enter without
typing anything), we will consider that the user is indifferent

It will also ask the user if he/she prefers the results sorted by price, by
average score or by number of reviews.

Finally the script will print out the top 10 results matching the desired
requirements and sorted by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user
that no listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out
the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the
data source.
"""

import pandas as pd
import argparse

# loads the dataset
def load_data():
    fname = "data/airbnb.csv"
    data = pd.read_csv(fname, index_col = 0)
    return data

# functionality 1 (neighborhood listings)
def information(neighborhood, data):
    
    # data for new neighborhood
    data = data[data["neighborhood"] == neighborhood]
    
    # print total number of available listings
    print("\nTotal # of Available Rooms: {}".format(len(data.index)))
    
    # print total number of rooms per listing type
    for each in data["room_type"].unique():
        rooms = data[data["room_type"] == each]
        print("  Total # of Available {}s: {}".format(each,len(rooms.index)))
              
    # print average room price
    print("Average Room Price: $%.2f" %data["price"].mean())
    
    # print price quartiles
    quartiles = data["price"].quantile([0, 0.25, 0.5, 0.75, 1])
    for each in quartiles.index:
        percent = each * 100
        print("  %dth Percentile Room Price: $%.2f" %(percent, quartiles[each]))
    print()

# checks if the range is valid input
def check_range(values):
    if (not (len(values) == 2)):
        print("incorrect number of commands")
        return False
    else:
        lo = values[0]
        hi = values[1]
        if (not (lo.isdigit() and hi.isdigit())):
            print("numbers are not positive integers")
            return False
        elif (lo > hi):
            print("low end is greater than high end")
            return False
        return True
        

# functionality 2 (apartment search)
def search(data):
    
    # check for listings in desired price range
    while (True):
        command = input('Enter Desired Price Range as "lo hi": ')
        # FIX when the input is only one 
        if (not (command == "")): # user would like to input range
            values = command.split()
            if check_range(values):
                lo = int(values[0])
                hi = int(values[1])
                print("... checking for listings with price range: [${}, ${}]\n".format(lo, hi))
                data = data[(data["price"] >= int(lo)) & (data["price"] <= int(hi))]
                break
        else: # user is indifferent
            print("... no preference for price range\n")
            break
    
    # check for listings in desired bedroom range
    while (True):
        command = input('Enter Desired Number of Bedrooms as "lo hi": ')
        if (not (command == "")): # user would like to input range
            values = command.split() 
            if check_range(values):
                lo = int(values[0])
                hi = int(values[1])
                print("... checking for listings with bedroom range: [{}, {}]\n".format(lo, hi))
                data = data[(data["bedrooms"] >= int(lo)) & (data["bedrooms"] <= int(hi))]
                break
        else: # user is indifferent
            print("... no preference for # of bedrooms\n")
            break

    # check for listings in list of desired neighborhoods 
    while (True):
        command = input('Enter List of Desired Neighborhoods (spaces in between): ')
        if (not (command == '')):
            values = command.split()
            neighborhoods = data["neighborhood"].unique()
            valid = []
            for each in values:
                if each in neighborhoods:
                    valid.append(each)
            if (len(valid) > 0):
                print("... checking for listings in neighborhoods: {}\n".format(valid))
                data = data[data["neighborhood"].isin(valid)]
                break
            else:
                print("neighborhoods are invalid (to print all, press enter)\n")
        else:
            print("... no preference for neighborhoods\n")
            break
    
    # check if user would like to have the information ordered
    while (True):
        command = input('''Enter Order Preference of Results (valid inputs are "reviews" for
number of reviews, "score" for overall satisfaction, or "price" for price): ''')
        if (not (command == "")):
            if (command == "reviews"):
                data = data.sort_values(by=['reviews'], axis=0, ascending=False)
                print("ordering listings in terms of descending # of reviews\n")
                break
            elif (command == "score"):
                data = data.sort_values(by=['overall_satisfaction'], axis=0, ascending=False)
                print("ordering listings in terms of descending overall satisfaction\n")
                break
            elif (command == "price"):
                data = data.sort_values(by=['price'], axis=0, ascending=False)
                print("ordering listings in terms of descending price\n")
                break
            else:
                print("invalid input")
        else:
            print("... no order preference\n")
            break
        
    # print data
    if (len(data.index) == 0):
        print("there are no listings under current criteria\n")
    else:
        print("... printing top 10 results")
        print(data.head(10))
        print()
    
# parses the command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Script Description")

    '''
    parser.add_argument("method", help="""
                        Indicates the functionality to perform
                        Valid methods are "information" or "search"
                        """, choices=["information", "search"])
    '''
						
    subparsers = parser.add_subparsers(help='information on neighborhood',dest='method')
    create_parser = subparsers.add_parser('information')
    create_parser.add_argument("neighborhood", help="""
                        Indicates the neighborhood that the user wants
                        information on""")
    subparsers.add_parser('search')
    
    arguments = parser.parse_args()
    return arguments

# main functionality
def main(arguments):
    data = load_data()
    method = arguments.method
    if (method == "information"):
        information(arguments.neighborhood, data)
    elif (method == "search"):
        search(data)

if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)