year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
sunday = 0
for year_num in range(1900, 2001):  # calculates whether the year is a leap year
    if year_num % 4 == 0:
        year[1] = 29
        if year_num % 100 == 0:
            year[1] = 28
            if year_num % 400 == 0:
                year[1] = 29
    else:
        year[1] = 28

    for month in year:              # calculates what day it is on the first day of each month
        r = month % 7
        day += r
        if day > 7:
            day = day % 7
        if day == 7 and year_num > 1900:
            sunday += 1

print("there are", sunday, "sundays")
