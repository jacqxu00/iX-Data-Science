# -*- coding: utf-8 -*-
"""
Jacqueline Xu
iXperience Tel Aviv
27 May 2019
Exercise 2: Baby Names
"""

#%%
"""
In this example we are going to build an application that reads the most
popular names in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains
the most popular baby names for boys and girls for a certain year (the year is
in the filename)
- For the name provided as an argument, print out how many years it's been
among the most popular among boys and girls
"""

import argparse # for parsing through args
import os # for finding directory

# used to parse arguments in main
def parse_arguments_advanced():
    parser = argparse.ArgumentParser(description="Script Description")
    
    parser.add_argument("name", help="""
                        Indicates the name of the input
                        """)
    
    arguments = parser.parse_args()
    return arguments

# finds how mnay years the name has been among the most popular
# assuming first column is for guys' names and second column is for girls'
# assuming that each name shows up at most once per column per file
# (if name X placed 4th for girls' names it will not place again later)
def main(args):
    name = args.name.capitalize()
    boys = 0
    girls = 0
    
    # parse through all files
    for filename in os.listdir("data"):
        f = open("data/" + filename)
        lines = f.read().split()
        parsed = []
        for line in lines:
            names = line.split('|')
            parsed.append(names)
        
        # check file if the name is inside
        for line in parsed:
            if len(line) == 3:
                if line[1] == name:
                    boys += 1
                    continue
                if line[2] == name:
                    girls += 1
                    continue
            
    print("boys couunt: ", boys)
    print("girls count: ", girls)
    

# allow program to run main
if __name__ == "__main__":
    args = parse_arguments_advanced()
    print("Arguments passed to the script: ", args)
    main(args)