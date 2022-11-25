#!/usr/bin/env python3

import make_day
import os
import sys
import time
import argparse

from itertools import chain
from requests import get
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()


def parse(value, t=None):
    if value == 0:
        if t == 'year':
            value = range(2015, time.localtime().tm_year + 1)
        elif t == 'day':
            value = range(1, 26)
        return value
    for i, v in enumerate(value):
        if "-" in v:
            start, end = v.split("-")
            value[i] = list(range(int(start), int(end) + 1))
        if "," in v:
            value[i] = list(map(int, v.strip(",").split(",")))
        if isinstance(value[i], str):
            value[i] = [int(value[i])]
    value = set(chain.from_iterable(value))
    return value
    


def get_day_info(year, day, options):
    """ This will send GET requests to the AoC website.
    If you look at the response of the website,
    you'll see that the creator has put a notice
    as to ask to reduce the amount of automated request.
    Please respect this notice,
    and use this script sparingly."""
    # overwrite = options.get("overwrite", False)
    overwrite = False
    reset_solution = options["reset_solution"]
    # auto = options.get(["auto"], True)
    auto = True
    get_input = options["get_input"]
    get_question = options["get_question"]
    parts = options["parts"]
    session_id = options["session_id"]
    cookies = dict()

    if get_input is True or parts == 2:
        cookies["session"] = session_id

    __location__ = os.getcwd()
    os.chdir(__location__)
    make_day.make_year(year, overwrite=overwrite, auto=auto)
    os.chdir(str(year))
    make_day.make_day(day, year, overwrite=overwrite, auto=auto, reset_solution=reset_solution)
    # Get the input for the day
    question_url = f"https://adventofcode.com/{year}/day/{day}"
    input_url = question_url + "/input"

    if get_input is True:
        response = get(input_url, cookies=cookies)
        if response.status_code == 200:
            with open("input", "w") as f:
                f.write(response.text)
        else:
            print(f"Failed to get input for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")

    # Get the question for the day
    if get_question is True:
        if parts == 2:
            response = get(question_url, cookies=cookies)
        else:
            response = get(question_url)
        if response.status_code == 200:
            with open("question", "w") as f:
                soup = BeautifulSoup(response.text, "html.parser")
                f.write(str(soup.main))
        else:
            print(f"Failed to get question for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")
    print("Done")
    os.chdir(__location__)

def get_days_from_year(year, days, args):
    for day in days:
        print(year, day)
        get_day_info(year, day, args)
    

def main(args):
    args = vars(args)
    print(args)
    args["base_url"] = "https://adventofcode.com"
    years = parse(args["years"], t="year")
    days = parse(args["days"], t="day")

    for year in years:
        get_days_from_year(year, days, args)

    print("Finished getting info for all days")


if __name__ == "__main__":
    cur_year = time.strftime("%Y")
    if time.strftime("%m") != "12":
        cur_year = str(int(cur_year) - 1)

    parser = argparse.ArgumentParser(
        prog="`Advent of Code` Year Grabber",
        description="Download selected `Advent of Code` days for a given year\
             or given years."
    )
    parser.add_argument(
        "-y",
        "--year",
        "--years",
        nargs="+",
        dest="years",
        default=0,
    )
    parser.add_argument(
        "-a",
        "--all",
        default=True,
        dest="all_years",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--days",
        nargs="+",
        dest="days",
        default=0,
    )
    parser.add_argument(
        "-s",
        "--session-id",
        dest="session_id",
        default=os.getenv("SESSION_ID"),
    )
    parser.add_argument(
        "-i",
        "--input",
        "--get-input",
        dest="get_input",
        action="store_true",
    )
    parser.add_argument(
        "-q",
        "--question",
        "--get-question",
        dest="get_question",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        "--parts",
        dest="parts",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-r",
        "--reset-solution",
        dest="reset_solution",
        action="store_true",
    )

    args = parser.parse_args()

    main(args)
