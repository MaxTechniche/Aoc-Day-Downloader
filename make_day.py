import os


def day_valid(day):
    pass


while True:
    year = input("Year [2020]: ") or 2020
    try:
        int(year)
        break
    except ValueError:
        print("Unable to convert year to integer. Try again.")

print(f"Year: {year}")

while True:
    day = input("Day number: ")
    try:
        if int(day) > 25 or int(day) < 1:
            print("Number is not in range (1-25)")
            continue
        if day_valid(day):
            break
    except ValueError:
        print("Unable to convert day to integer. Try again.")

    # do = input(f"Day {day}? [y]/n/q :") or "y"
    # if do == "q":
    #     print("Exiting...")
    #     exit()
    # elif do == "n":
    #     continue
    # elif do == "y" or do == "":
    #     print(f"Creating day {day}...")
    #     break

print(f"Day: {day}")
