#!/usr/bin/env python

import os
import time


def make_year(year):
    if year not in os.listdir():
        print(f"Year {year} not found.")
        while True:
            create = input(
                f"Would you like to create year {year}? [y]/n: ") or "y"
            if create == "y":
                print("Creating year {year}...")
                os.mkdir(year)
                print("Done")
                break
            elif create == "n":
                print("Exiting...")
                exit()
            else:
                print(f"{create} not a valid command")



def make_day(day, year):
    day = "Day_" + day.zfill(2)

    if day not in os.listdir():
        print(f"Creating {day}")
        os.mkdir(day)
        print(f"Done")
        os.chdir(day)

    else:
        print(f"{day} already in {year}")
        print("Exiting...")
        return

    day = "Day_" + str(day).zfill(2)

    open("question", "w")
    open("input", "w")
    open("sample_input", "w")
    with open("solution.py", "w") as solution:
        solution.write(f"""
            from time import perf_counter 
            def main():
                t1 = perf_counter()

                with open("{year}/{day}/input") as f:
                    lines = f.read().splitlines()
                    
                print("Time:", time() - t1)
                
            main()
            """
    )



def get_year(current_year):
    while True:
        year = input("Year [{current_year}]: ".format(current_year=current_year)) or current_year
        try:
            if 2015 > int(year) or int(year) > int(current_year):
                print("Year not in range (2015 - {current_year})".format(current_year=current_year))
            else:
                return str(year)
        except ValueError:
            print("Unable to convert year to integer. Try again.")

def get_day():
    while True:
        day = input("Day number: ")
        try:
            if int(day) > 25 or int(day) < 1:
                print("Number is not in range (1-25)")
                continue
            return str(day)
        except ValueError:
            print("Unable to convert day to integer. Try again.")
    
def main():
    current_year = int(time.strftime("%Y")) - 1
    current_month = time.strftime("%m")

    if current_month in ("11", "12"):
        current_year += 1

    year = get_year(current_year)
    day = get_day()

    make_year(year)
    print(f"Entering year {year}")
    os.chdir(year)

    make_day(day, year)

if __name__ == "__main__":
    main()
