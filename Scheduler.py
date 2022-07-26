"""
MSD P22385
Themed Entertainment Model Display
File    : Scheduler.py
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
Function : GetTimestamp
Inputs   : none
Outputs  : timestamp - a string representation of the current time & date

Fetches time and dates, creates a string timestamp, and returns it
"""
def GetTimestamp():
    return FetchTime().isoformat() + FetchDate().strftime(" %y-%m-%d\n")


"""
Function : ValidateTime
Inputs   : timeOfDay - current time of day
Outputs  : return code based on validity of time within the ride schedule

Checks if the given time lies within the user-defined schedule. Returns accordingly
Specifically checks if date is valid. If valid, checks if day of week is valid.
If valid, continue to check the time
"""
def ValidateTime(timeOfDay, todaysDate):
    # Extract day of week and current week and year using ISO calendar format
    currentDOW = todaysDate.isocalendar()[2]
    currentWeek = todaysDate.isocalendar()[1]
    currentYear = todaysDate.isocalendar()[0]

    # Extract current date (ISO format) and month
    currentDate = datetime.date.isoformat(todaysDate)
    currentMonth = todaysDate.month

    # Extract hour and minute for evaluation
    currentMin = timeOfDay.minute
    currentHour = timeOfDay.hour

    # If the current day is set as a valid override, all other date-based invalidate checks are skipped.
    # Useful for things like Imagine RIT that fall on weekends, without having to remove the weekend restriction
    validOverrideFlag = False
    for overrideDate in Schedule.VALID_OVERRIDE_DATE_ARRAY:
        if currentDate == overrideDate:  # Override date detected, set flag high to skip date validation
            validOverrideFlag = True
    # Validate the date ONLY if the current date is not an override date
    if not validOverrideFlag:
        # Validate date
        for date in Schedule.INVALID_DATE_ARRAY:
            if currentDate == date:  # If date is invalid, return invalid code
                return Schedule.INVALID_DATE

        # Validate day of week (DOW)
        for day in Schedule.INVALID_DOW_ARRAY:
            if currentDOW == day:  # If DOW is invalid, return invalid code
                return Schedule.INVALID_DOW

        # Validate week number
        for weekYearTuple in Schedule.INVALID_WEEK_ARRAY:
            # If week is invalid, return invalid code
            # Checks year too for insurance that the week is correct
            if currentYear == weekYearTuple[0] and currentWeek == weekYearTuple[1]:
                return Schedule.INVALID_WEEK

        # Validate month number
        for month in Schedule.INVALID_MONTH_ARRAY:
            if currentMonth == month:  # If month is invalid, return invalid code
                return Schedule.INVALID_MONTH

    # Validate time of day (TOD)
    if Schedule.OPEN_HR < currentHour < Schedule.CLOSE_HR:
        # TOD is within valid hours, no need to check minutes
        return Schedule.VALID_RUN_TIME
    elif Schedule.OPEN_HR == currentHour:
        # If hour matches opening hour, check minutes
        if Schedule.OPEN_MN <= currentMin:
            # Time is past opening, valid
            return Schedule.VALID_RUN_TIME
        else:
            # Time is not at opening, invalid
            return Schedule.INVALID_MINUTE
    elif Schedule.CLOSE_HR == currentHour:
        # If hour matches closing hour, check minutes
        if Schedule.CLOSE_MN >= currentMin:
            # Time is prior to closing, valid
            return Schedule.VALID_RUN_TIME
        else:
            # Time is after closing, invalid
            return Schedule.INVALID_MINUTE
    else:
        # Hour is not within correct timeframe (hours)
        return Schedule.INVALID_HOUR

