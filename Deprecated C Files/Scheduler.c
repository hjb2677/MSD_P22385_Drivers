// MSD P22835
// Themed Entertainment Model Display
// File    : Scheduler.c
// Author  : Harrison Barnes
// Data    : 05/03/2022
// Purpose : Driver program for the scheduler


//----- Includes -----//
#include "Scheduler.h"
#include <time.h>
#include <stdio.h>


//----- Function Declarations -----//


// Function : Scheduler
// Inputs   : none
// Outputs  : integer code denoting state of schedule
//
// Fetches, validates, and returns
int Scheduler(void);


// Function : FetchTime
// Inputs   : none
// Outputs  : timeOfDay - time stored in time_t
//
// Fetches current time based on time.h's library
time_t FetchTime(void);


// Function : PrintTimeOfDay
// Inputs   : timeOfDay - time stored in time_t
// Outputs  : none
//
// Prints the time of day based on the parameter currentTime
// Follows the format:
//          YYYY-MM-DD HR:MIN:SEC
void PrintTimeOfDay(time_t timeOfDay);


// Function : ValidateTime
// Inputs   : timeOfDay - time stored in time_t to be validated
// Outputs  : int - return code designating if the time is within the schedule
//
// Checks if the given time lies within the user-defined schedule. Returns accordingly
int ValidateTime(time_t timeOfDay);


//----- Function Implementations -----//


// Function : Scheduler
// Inputs   : none
// Outputs  : integer code denoting state of schedule
//
// Fetches, validates, and returns
int Scheduler(void) {
    // Var holds time of day fetched from internet
    time_t timeOfDay = FetchTime();

    // Validate time
    int validCode = ValidateTime(timeOfDay);

    return validCode; // Return validation code
}


// Function : FetchTime
// Inputs   : none
// Outputs  : timeOfDay - time stored in time_t
//
// Fetches current time based on time.h's library
time_t FetchTime(void) {
    return time(NULL); // returns the time_t created from time(NULL)
}


// Function : PrintTimeOfDay
// Inputs   : timeOfDay - time stored in time_t
// Outputs  : none
//
// Prints the time of day based on the parameter currentTime
// Follows the format:
//          YYYY-MM-DD HR:MIN:SEC
void PrintTimeOfDay(time_t timeOfDay) {
    // Convert time to usable form
    struct tm currentTime = *localtime(&timeOfDay);

    // Print the time of day, following the specified format
    // Adjusts values based on the struct's zero declarations (ex: year + 1900)
    printf("time: %d-%02d-%02d %02d:%02d:%02d\n", currentTime.tm_year + 1900, currentTime.tm_mon + 1, currentTime.tm_mday, currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec);
}


// Function : ValidateTime
// Inputs   : timeOfDay - time stored in time_t to be validated
// Outputs  : int - return code designating if the time is within the schedule
//
// Checks if the given time lies within the user-defined schedule. Returns accordingly
// Specifically checks if date is valid. If valid, checks if day of week is valid. 
// If valid, continue to check the time
int ValidateTime(time_t timeOfDay) {
    // Convert time to usable form
    struct tm currentTime = *localtime(&timeOfDay);

    // Extract date, AKA day of year, 0-365 (365 denotes leap year)
    int date = currentTime.tm_yday;

    // Extract day of week, 0-6
    int day = currentTime.tm_wday;

    // Extract hour
    int hour = currentTime.tm_hour;

    // Extract minute
    int min = currentTime.tm_min;

    // Validate dates. Check if date exists in an invalid date array
    for(int dateIdx = 0; dateIdx < sizeof(invalid_dates) / sizeof(int); dateIdx++) {
        // Check every date in invalid array
        if(date == invalid_dates[dateIdx]) {
            // Date matches invalid date in array. Return invalid date code
            return INVALID_DATE;
        }
    }

    // Validate day. Checks if day is not allowed
    for(int dayIdx = 0; dayIdx < sizeof(invalid_days) / sizeof(int); dayIdx++) {
        // Check every date in invalid array
        if(day == invalid_days[dayIdx]) {
            // Date matches invalid day in array. Return invalid day of week code
            return INVALID_DOW;
        }
    }

    // Validate time of day
    if(TOD_BEGIN_HR <= hour && hour <= TOD_CLOSE_HR) {
        // Time is within hours, check minute
        if (TOD_BEGIN_MIN <= min && min <= TOD_CLOSE_MIN) {
            // Time is within minutes, valid time
            return VALID_TIME;
        } else {
            // Time is not within valid operating minutes, but is within hours
            return INVALID_MINUTE;
        }
    } else {
        // Time is not within valid operating hours
        return INVALID_HOUR;
    }
}
