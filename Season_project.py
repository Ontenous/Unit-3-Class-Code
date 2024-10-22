"""
Name: William Nathan
Date: 10/22/24
Description: Season project for unit 2 and 3
"""

month = input("Enter the name of the month: ")
day = int(input("Enter the day (1-31): "))
cap_month = month.title()

if cap_month == "January" or cap_month == "February":
    print(f"{cap_month} {day} is in Winter")
if cap_month == "December" and 21<=day<=31:
    print(f"{cap_month} {day} is in Winter")
if cap_month == "March" and 1<=day<20:
    print(f"{cap_month} {day} is in Winter")

if cap_month == "March" and 20<=day<=31:
    print(f"{cap_month} {day} is in Spring")
if cap_month == "April" or cap_month == "May":
    print(f"{cap_month} {day} is in Spring")
if cap_month == "June" and 1<=day<21:
    print(f"{cap_month} {day} is in Spring")

if cap_month == "June" and 21<=day<=30:
    print(f"{cap_month} {day} is in Summer")
if cap_month == "July" or cap_month == "August":
    print(f"{cap_month} {day} is in Summer")
if cap_month == "September" and 1<=day<22:
    print(f"{cap_month} {day} is in Summer")

if cap_month == "September" and 22<=day<=30:
    print(f"{cap_month} {day} is in Fall")
