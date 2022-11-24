# Write a Python program to print the calendar of a month and year, given by user.

import calendar
y = int(input("Enter the year : "))
m = int(input("Enter the month : "))
print(calendar.month(y, m))