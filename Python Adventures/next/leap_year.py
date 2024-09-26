months = [1, 2, 32, 23, 5, 15, 26, 3]


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def next(year, month):
    if month < 1 or month > 12:
        return "Invalid month! "
    elif month == 2 and leap_year(year):
        return 29
    else:
        return months[month]


print(leap_year(2017))
print(leap_year(2020))
print(next(2017, 2))
print(next(2020, 2))



