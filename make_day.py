import os


def vac_year(year):
    if str(year) not in os.listdir():
        print(f"Year {year} not found.")
        while True:
            create = input(f"Would you like to create year {year}? [y]/n") or "y"
            if create == "y":
                print("Creating year {year}...")
                os.mkdir(str(year))
                print("Done")
                break
            elif create == "n":
                print("Exiting...")
                exit()
            else:
                print(f"{create} not a valid command")

    print(f"Entering year {year}")
    os.chdir(str(year))


def vac_day(day, year):
    day = "Day_" + str(day).zfill(2)

    if day not in os.listdir():
        print(f"Creating {day}")
        os.mkdir(day)
        print(f"Done")
        os.chdir(day)

    else:
        print(f"{day} already in {year}")
        print("Exiting...")
        exit()


while True:
    year = input("Year [2021]: ") or 2021
    try:
        int(year)
        vac_year(year)
        break
    except ValueError:
        print("Unable to convert year to integer. Try again.")


while True:
    day = input("Day number: ")
    try:
        if int(day) > 25 or int(day) < 1:
            print("Number is not in range (1-25)")
            continue
        vac_day(day, year)
        break
    except ValueError:
        print("Unable to convert day to integer. Try again.")

day = "Day_" + str(day).zfill(2)

open("question", "w")
open("input", "w")
with open("solution.py", "w") as solution:
    solution.write(
        f"""from time import time

t1 = time()

with open("{year}/{day}/input") as f:
    lines = f.read().splitlines()
    
print("Time:", time() - t1)
"""
    )
