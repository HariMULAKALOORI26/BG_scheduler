#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:18:46 2026

@author: mulakal
"""

from datetime import datetime
from zoneinfo import ZoneInfo


REFERENCE_DATE = {
    "Saturday": "2026-06-27",
    "Sunday": "2026-06-28",
}

people = {
    "Hari": "Europe/Paris",
    "Bala": "Asia/Kolkata",
    "Dheeraj": "America/Chicago",
    "Poojitha": "America/Detroit",
}

availability = {
    "Hari": ["Saturday 18:00", "Sunday 18:00", "Sunday 19:00"],
    "Bala": ["Saturday 02:00", "Sunday 10:45", "Sunday 23:55"],
    "Dheeraj": ["Saturday 06:00", "Sunday 19:45", "Sunday 18:00"],
    "Poojitha": ["Saturday 10:00", "Sunday 06:00", "Sunday 20:00"],
}


def local_slot_to_utc(day_time, timezone_name):
    day, time_str = day_time.split()
    #print("The day is", day)
    #print("The mentionned time is", time_str)
    date_str = REFERENCE_DATE[day]

    #print("The mentionned date is", date_str)
    local_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    #print("The details of date, time is given as", local_dt)
    local_dt = local_dt.replace(tzinfo=ZoneInfo(timezone_name))
    #print("The local dt is given as", local_dt)

    return local_dt.astimezone(ZoneInfo("UTC"))


def convert_all_availability_to_utc():
    utc_availability = {}

    for person, slots in availability.items():
        timezone_name = people[person]
        utc_slots = []

        for slot in slots:
            utc_time = local_slot_to_utc(slot, timezone_name)
            #print("The utc time of each slot is", utc_time)
            utc_slots.append(utc_time)

        utc_availability[person] = set(utc_slots)
        #print("The UTC availability is given as",utc_availability)

    return utc_availability


def find_common_slots(utc_availability):
    all_people_slots = list(utc_availability.values())
    common_slots = set.union(*all_people_slots)
    #print("The sorted of all common slots is", sorted(common_slots))
    available_people = []
    unavailable_people = []
    
    return common_slots



def display_common_slots(common_slots):
    if not common_slots:
        print("No common slots found.")
        return

    print("\nCommon Bhagavad Gita meeting slots:\n")

    for utc_slot in common_slots:
        #print("UTC:", utc_slot.strftime("%A %H:%M"))

        for person, timezone_name in people.items():
            local_time = utc_slot.astimezone(ZoneInfo(timezone_name))
            print(f"  {person}: {local_time.strftime('%A %H:%M')}")

        print()


def main():
    utc_availability = convert_all_availability_to_utc()
    common_slots = find_common_slots(utc_availability)
    display_common_slots(common_slots)


if __name__ == "__main__":
    main()