import streamlit as st
import time
from datetime import datetime
from pytz import timezone
from pprint import pprint
import locale
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="refresher")
current_time = datetime.now(timezone('US/Eastern'))
current_time = datetime(2019, 12, 10, 0, 0, 0, 0, timezone('US/Eastern'))


values = dict()
year_max = current_time.year
if current_time.month == 12:
    year_max += 1
selectable_years = range(2015, year_max)
containers = dict()

for year in selectable_years:
    values[str(year)] = dict()
    values[str(year)]["num"] = year

st.write("# [`Advent of Code`](https://adventofcode.com) Day Downloader")
st.write("##### Retrieve question and/or input for selected day(s) from selected year(s).")
st.write(f"###### Current time: {current_time.strftime('%c')} (US/Eastern) (your locale: {locale.getlocale()})")


def check_available(year, day=None):
    if year < current_time.year:
        return True

    if year > current_time.year:
        return False

    if current_time.month < 12:
        return False

    if day is None:
        return True

    if current_time.day >= day:
        return True

    return False
    

def check_day_checkboxes(year, container):
    checked = st.session_state[f"{year}"]
    for day in range(1, 26):
        available = check_available(year, day)
        st.session_state[f"{year}-{day}"] = checked and available


def get_num_days_available(year):
    if current_time.year > year:
        return 25
    num_days_available = 0
    for day in range(1, 26):
            if check_available(year, day):
                num_days_available += 1
    return num_days_available

def sidebar_years(years, container=st.sidebar):
    for year in years:
        available = check_available(year)
        num_days_available = get_num_days_available(year)
        
        try:
            if not all([st.session_state[f"{year}-{day}"] for day in range(1, num_days_available + 1)]):
                st.session_state[year] = False
            else:
                st.session_state[year] = True
        except KeyError:
            st.session_state[year] = False
        checked = st.session_state[year]
        year_checkbox = container.checkbox(f"{year}", key=f"{year}", disabled=(not available), value=checked, on_change=check_day_checkboxes, args=(year, container))
        if available:
            containers[year] = container.expander(f"{year}")


def sidebar_days(year, container):
    for day in range(1, 26):
        available = check_available(year, day)
        if available:
            container.checkbox(f"Day {day}", key=f"{year}-{day}")

def update_sidebar():
    sidebar_years(selectable_years, container=st.sidebar)
    for year in selectable_years:
        if st.session_state[year]:
            sidebar_days(year, containers[year])

sidebar = st.sidebar
sidebar.write("#### Select year(s) and day(s) to download.")


sidebar_years(selectable_years)
for year, container in containers.items():
    sidebar_days(year, container)

day_cols = st.columns([2] + [1] * 25)
for year in selectable_years:
    day_cols[0].write(f"##### *{year}:*")
    for day in range(1, 26):
        try:
            if st.session_state[f"{year}-{day}"]:
                day_cols[day].write(f"##### {day}")
            else:
                if check_available(year, day):
                    day_cols[day].write("##### -")
        except KeyError:
            pass

st.text_input("session_id:", key="session_id")
st.button("Retrieve")