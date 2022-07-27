"""
MSD P22385
Themed Entertainment Model Display
File    : Scheduler.c
Author  : Harrison Barnes
Date    : 05/03/2022
Purpose : Driver program for the scheduler
"""

# Includes
import datetime
import Schedule

"""
Function : SchedulerDriver
Inputs   : None
Outputs  : integer code denoting state of schedule

Fetches time, validates the time within the schedule, and returns
a proper validation code.
"""
def SchedulerDriver():
    # Fetch time and date for the current time
    timeOfDay = FetchTime()
    todaysDate = FetchDate()

    # Validate the time and date within the schedule
    return ValidateTime(timeOfDay, todaysDate)


"""
Function : FetchTime
Inputs   : none
Outputs  : Current time of day
"""
def FetchTime():
    return datetime.datetime.now().time()


"""
Function : FetchDate
Inputs   : none
Outputs  : Current date
"""
def FetchDate():
    return datetime.date.today()


"""
Function : ConvertDayOfWeek
Inputs   : dateObj -  a datetime date object
Outputs  : Day of week (0 = mon, 6 = sun)
"""
def ConvertDayOfWeek(dateObj):
    return datetime.date.weekday(dateObj)


"""
Function : PrintTimeOfDay
Inputs   : none
Outputs  : none

#rints time of day
"""
def PrintTimeOfDay():
    print(FetchTime())


"""
Function : PrintDate
Inputs   : none
Outputs  : none

Prints current date
"""
def PrintDate():
    print(FetchDate())


"""
Function : ValidateTime
Inputs   : timeOfDay - current time of day
Outputs  : return code based on validity of time within the ride schedule

Checks if the given time lies within the user-defined schedule. Returns accordingly
Specifically checks if date is valid. If valid, checks if day of week is valid.
If valid, continue to check the time
"""
def ValidateTime(timeOfDay, todaysDate):
    # Extract Day, Month, Year for evaluation
    currentDay = todaysDate.day
    currentDOW = ConvertDayOfWeek(todaysDate)
    currentMonth = todaysDate.month
    currentYear = todaysDate.year

    # Extract Hour, Minute, Second for evaluation
    currentMin = timeOfDay.min
    currentHour = timeOfDay.hour

    # Validate day of week (DOW)
    for day in Schedule.INVALID_DATES_ARRAY:
        if currentDOW == day: # If DOW is invalid, return invalid code
            return Schedule.INVALID_DOW

    # Validate time of day (TOD)
    if Schedule.OPEN_HR < currentHour < Schedule.CLOSE_HR:
        # TOD is within valid hours, no need to check minutes
        return Schedule.VALID_TIME
    elif Schedule.OPEN_HR == currentHour:
        # If hour matches opening hour, check minutes
        if Schedule.OPEN_MN <= currentMin:
            # Time is past opening, valid
            return Schedule.VALID_TIME
        else:
            # Time is not at opening, invalid
            return Schedule.INVALID_MINUTE
    elif Schedule.CLOSE_HR == currentHour:
        # If hour matches closing hour, check minutes
        if Schedule.CLOSE_MN >= currentMin:
            # Time is prior to closing, valid
            return Schedule.VALID_TIME
        else:
            # Time is after closing, invalid
            return Schedule.INVALID_MINUTE
    else:
        # Hour is not within correct timeframe (hours)
        return Schedule.INVALID_HOUR

