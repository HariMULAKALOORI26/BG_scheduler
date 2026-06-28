#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:49:58 2026

@author: mulakal
"""

from datetime import datetime
from zoneinfo import ZoneInfo

def get_user_details():
    
    #user_name = input("Enter your name: ")
    user_time_zone = input("Select your time zone: ")
    user_date = input("Enter your available dates (Ex: 01-01-2026): ")
    user_time = input("Enter your available time (Ex: 18:55): ")
    local_date_time = datetime.strptime(f"{user_date} {user_time}", "%d-%m-%Y %H:%M")
    local_date_time = local_date_time.replace(tzinfo=ZoneInfo(user_time_zone)) ## Local time and its relative difference to UTC
    print("Your time zone info is", local_date_time.tzinfo)
    #relative_UTC_diff = local_date_time.ZoneInfo(user_time_zone)
    #print("relative", relative_UTC_diff)
    print("Your time zone is relative to UTC by ", local_date_time.utcoffset(), "hrs")
    utc_time = local_date_time.astimezone(ZoneInfo("UTC"))
    print("Your time in utc is", utc_time)
    utc_time = local_date_time.replace(tzinfo=ZoneInfo("UTC"))
    print("Your replaced time zone with the same time is", utc_time)
    #time_zone_time = local_date_time.tzinfo
    #print("1 ",time_zone_time)
    
    return local_date_time


def main():
    #print("this is main")
    local_date_time = get_user_details()
    #print("Your time zone is UTC + ", local_date_time.utcoffset(), "hrs")
   # when = datetime.datetime(datetime.now(), tzinfo=ZoneInfo("America/Los_Angeles"))
    #print(when)
    
if __name__ == "__main__":
    main()