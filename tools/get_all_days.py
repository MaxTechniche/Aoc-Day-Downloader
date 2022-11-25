#!/usr/bin/env python3

import make_day
import os
import sys
import time
import argparse

from requests import get
from dotenv import load_dotenv

load_dotenv()


def parse(value):
    raise NotImplementedError


def get_day_info(year, day, options):
    """ This will send GET requests to the AoC website.
    If you look at the response of the website,
    you'll see that the creator has put a notice
    as to ask to reduce the amount of automated request.
    Please respect this notice,
    and use this script sparingly."""
    overwrite = options.get("overwrite", False)
    auto = options.get(["auto"], True)
    get_input = options["get_input"]
    get_question = options["get_question"]
    parts = options["parts"]
    session_id = options["session_id"]
    cookie = dict()

    if get_input is True or parts == 2:
        cookie["session"] = session_id

    make_day.make_year(year, overwrite=overwrite, auto=auto)
    make_day.make_day(day, year, overwrite=overwrite, auto=auto)

    # Get the input for the day
    question_url = f"https://adventofcode.com/{year}/day/{day}"
    input_url = question_url + "/input"

    if get_input is True:
        response = get(input_url, cookie=cookie)
        if response.status_code == 200:
            with open(f"{year}/Day_{day}/input", "w") as f:
                f.write(response.text)
        else:
            print(f"Failed to get input for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")

    # Get the question for the day
    if parts == 2:
        response = get(question_url, cookie=cookie)
        if response.status_code == 200:
            with open(f"{year}/Day_{day}/question", "w") as f:
                f.write(response.text)
        else:
            print(f"Failed to get question for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")
    elif get_question is True:
        response = get(question_url)
        if response.status_code == 200:
            with open(f"{year}/Day_{day}/question", "w") as f:
                f.write(response.text)
        else:
            print(f"Failed to get question for day {day}, year {year}")
            print(f"Status code: {response.status_code}")
            print(f"Reason: {response.reason}")


def get_all_days_from_year(year):
    pass


def main(args):
    args["base_url"] = "https://adventofcode.com"
    years = parse(args["years"])
    days = parse(args["days"])

    for year in years:
        for day in days:
            get_day_info(year, day, args)

    print("Finished getting info for all days")


if __name__ == "__main__":
    cur_year = time.strftime("%Y")
    if time.strftime("%m") != "12":
        cur_year -= 1
        cur_day = 25

    parser = argparse.ArgumentParser(
        prog="`Advent of Code` Year Grabber",
        description="Download selected `Advent of Code` days for a given year\
             or given years.",
        epilog="Example: python get_all_days.py 2020\
                    (gets all days in 2020) \n\
                Example: python get_all_days.py -a \
                    (gets all years from 2015 to current year)\n\
                Example: python get_all_days.py 2017, 2021 \
                    (gets all days from 2015 and 2021)\n\
                Example: python get_all_days.py 2017-2019 \
                    (gets all years from 2017 to 2019)",
        argument_default="-a",
    )
    parser.add_argument(
        "year",
        "-y",
        "--year",
        "--years",
        nargs="+",
        action="extend",
        dest="years",
        required=False,
        default="2015-{cur_year}".format(cur_year=cur_year),
    )
    parser.add_argument(
        "-a",
        "--all",
        default=False,
        dest="all_years",
    )
    parser.add_argument(
        "-d",
        "--days",
        nargs="+",
        action="extend",
        dest="days",
        default="1-25",
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
        default=1,
    )

    args = parser.parse_args(sys.argv)

    main(args)
