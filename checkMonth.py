__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

'''
Problem:
Given Two Dates,
Deterimine whether they are exactly 1 month apart, more than 1 month or less than 1 month.
'''

def checkMonths(input1, input2):
    date1 = input1
    date2 = input2

    (month1, day1, year1) = [int(e) for e in date1.split(" ")]
    (month2, day2, year2) = [int(e) for e in date2.split(" ")]

    if abs(year1 - year2) >= 2:
        return "More than 1 month"
    elif year1 != year2 and ((month1 == 12 and month2 == 1) or (month1 == 1 and month2 == 12)) and day1 == day2:
        return "Exactly 1 month"
    elif month1 == month2:
        return "Less than 1 month"
    elif abs(month1 - month2) == 1 and day1 == day2:
        return "Exactly 1 month"
    else:
        return "More than 1 month"

print("Resulted: " + checkMonths("12 15 2014", "1 15 2015")) # Rollover case
print("Expected: Exactly 1 month")

print("Resulted: " + checkMonths("1 15 2015", "12 15 2014")) # Reverse Rollover case
print("Expected: Exactly 1 month")

print("Resulted: " + checkMonths("1 15 2014", "1 15 2016")) # Two Years
print("Expected: More than 1 month")

print("Resulted: " + checkMonths("1 15 2014", "1 30 2014")) # Same month
print("Expected: Less than 1 month")

print("Resulted: " + checkMonths("1 15 2015", "3 15 2015")) # More than 1 month
print("Expected: More than 1 month")

print("Resulted: " + checkMonths("1 15 2015", "2 15 2015")) # Exactly 1 month
print("Expected: Exactly 1 month")

print("Resulted: " + checkMonths("2 15 2015", "1 15 2015")) # Reverse Exactly 1 month
print("Expected: Exactly 1 month")
