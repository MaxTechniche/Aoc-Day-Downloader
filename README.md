# Advent Of Code

Solutions and attempts by MaxTechniche

The three files under tools can be used to make a days folder structure and request information from the site to fill in the question/input
## Setup

### Requirements

`pip install -r requirements.txt` or similar

### Environment Variables

`SESSION_ID=<id gathered from cookie from aoc>`

#### Instuctions on how to get the session id

- Go to https://adventofcode.com/
- Log in if you haven't already
- Open the `developer tools` (F12) or right click and `inspect`
- Go to the network tab
- Refresh the page
- Look for a request to `adventofcode.com` (or the page you are on) (it should be the first one)
- Look for the request header called `Cookie`
- Copy the `session` value
- Set the environment variable `SESSION_ID` to the value of the session OR pass it as an argument to the script via `-s / --session-id`
- Run the script

## Usage

```shell help

usage: get_all_days.py [-h] [-y YEARS [YEARS ...]] [-d DAYS [DAYS ...]] [-s SESSION_ID] [-i] [-q]
                                     [-p PARTS] [-r] [-o OUTPUT]

Download selected `Advent of Code` days for a given year or given years.

optional arguments:
  -h, --help            show this help message and exit
  -y YEARS [YEARS ...], --year YEARS [YEARS ...], --years YEARS [YEARS ...]
                        The year(s) to get the days for. Can be a single year, a range of years, or a list of years
                        separated by commas or spaces. Defaults to all years. (0)
  -d DAYS [DAYS ...], --days DAYS [DAYS ...]
                        Days to get. Can be a single day, a range of days, or a list of days separated by commas and/or
                        spaces. Defaults to all days. (0)
  -s SESSION_ID, --session-id SESSION_ID
                        Your session ID from `adventofcode.com`. Needed to get input and part 2 question if you have
                        solved part 1. Default is to use the SESSION_ID environment variable.
  -i, --input, --get-input
                        Will attempt to get the input for the day (must have a valid session id).
  -q, --question, --get-question
                        Will get the question for the day.
  -p PARTS, --parts PARTS
                        Will attempt to get the question for the day up to the given part. Defaults to 1
  -r, --reset-solution  Will reset the solution file for the day (if 'solution.py' exists in day).
  -o OUTPUT, --output OUTPUT
                        The directory to output the files to.
```
