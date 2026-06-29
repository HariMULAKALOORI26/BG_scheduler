#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:10:25 2026

@author: mulakal
"""

from datetime import datetime
from zoneinfo import ZoneInfo

## understanding strptime ##

#example = "Fri, 26 Jun 2026 13:10:46"

#parsed = datetime.strptime(example, "%a, %d %b %Y %H:%M:%S")
# parsed = datetime.strptime(
#     "Fri, 26 Jun 2026 13:10:46",
#     "%a, %d %b %Y %H:%M:%S"
# )
#print(parsed)
#formatted_again = f"{parsed:%a, %d %b %Y %H:%M:%S}"
#print(formatted_again)
#print(datetime.strptime(example, "%a, %d %b %y %H:%m:%S"))
#print(datetime.strptime(example, "%a, %d %b %Y %H:%M:%S"))

#print(parsed.strftime("%d"))
#print(parsed.second)

#print(datetime.now())
#print(parsed)

## understanding zoneinfo ##

# when = dt.datetime(2026, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
# print(when)


# when.tzname()

# from zoneinfo import ZoneInfo
# import datetime as dt

#user_date_time = datetime.now()
# when = dt.datetime(dt.now(), tzinfo=ZoneInfo("America/Los_Angeles"))
# print(when)


#when.tzname()

print(datetime.now(ZoneInfo("America/Los_Angeles")))