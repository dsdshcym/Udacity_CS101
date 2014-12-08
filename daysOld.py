# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def add(a, b):
    return a + b

def isLeap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def monthDays(year, month):
    if month == 2:
        if isLeap(year):
            return 29
        else:
            return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def yearDays(year):
    if isLeap(year):
        return 366
    else:
        return 365

def monthDaysFactory(year):
    def monthDays(month):
        if month == 2:
            if isLeap(year):
                return 29
            else:
                return 28
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30
    return monthDays

def dayDays(year, month, day):
    f = monthDaysFactory(year)
    if month>1:
        sum = reduce(add, map(f, range(1, month)))
    else:
        sum = 0
    return sum + day

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    # print year1, month1, day1, year2, month2, day2
    sum = 0
    for i in range(year1, year2):
        sum += yearDays(i)
    days1 = dayDays(year1, month1, day1)
    days2 = dayDays(year2, month2, day2)
    return sum - days1 + days2


# Test routine
def test_isLeap():
    if isLeap(2000):
        print '400x leap year passed'
    else:
        print '400x leap year failed'
    if isLeap(1900):
        print '100x leap year failed'
    else:
        print '100x leap year passed'
    if isLeap(2004):
        print 'normal leap year passed'
    else:
        print 'normal leap year failed'
    if isLeap(2003):
        print 'normal year failed'
    else:
        print 'normal year passed'

def test_monthDays():
    f = True
    bigMonth = [1, 3, 5, 7, 8, 10, 12]
    smallMonth = [4, 6, 9, 11]
    for year in range(1800, 2001):
        for month in range(1, 13):
            testResult = monthDays(year, month)
            if month in bigMonth:
                if testResult != 31:
                    print 'normal year bigMonth ' + str(month) + ' is *WRONG*: ' + str(testResult)
                    f = False
            elif month in smallMonth:
                if testResult != 30:
                    print 'normal year smallMonth ' + str(month) + ' is *WRONG*: ' + str(testResult)
                    f = False
            else:
                if isLeap(year):
                    FebDays = 29
                else:
                    FebDays = 28
                if testResult != FebDays:
                    print 'normal year Feburary is *WRONG*: ' + str(year) + ' ' + str(testResult)
                    f = False
    if f:
        print 'monthDays test passed'
    else:
        print 'something is *WRONG* in monthDays'

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
# print daysBetweenDates(2012,1,1,2012,3,1)
# test_isLeap()
# test_monthDays()
# print dayDays(2000, 2, 1)
