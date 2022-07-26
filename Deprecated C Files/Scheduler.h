// MSD P22835
// Themed Entertainment Model Display
// File    : Scheduler.h
// Author  : Harrison Barnes
// Data    : 04/05/2022
// Purpose : Contains defines for the scheduling of the display


//----- Validation Arrays -----//

// Invalid Dates - dates of the year in which the display will not run.
//      Stored from 0-365, where 365 is a leap year max value, 364 is
//      a normal year max value
const int invalid_dates[] = {0};


// Invalid Days - days of the weekin which the display will not run.
//      Stored from 0-6, where 0 is sunday, 1 is monday, etc.
const int invalid_days[] = {0,6};


//----- Defines -----//

// Fetch Period - time (ms) between fetching timestamp in Scheduler
//      Currently set to 5 min = 300,000 ms
#define FECTH_TIMESTAMP_DELAY_MS (300000)

// Fetch Period TEST - time (s) between fetching timestamp in scheduler
//      when performing the scheduler test
//      Set to 5 seconds (5 s)
#define TEST_FECTH_TIMESTAMP_DELAY_MS (5)

// TOD Begin - Time of day in which the display should begin running
//      Split amongst HR and MIN, which designates the hour and minute, respectively
//      HR - 0-23; MIN - 0-59
#define TOD_BEGIN_HR (19)
#define TOD_BEGIN_MIN (10)

// TOD Close - Time of day in which the display should stop running
//      Split amongst HR and MIN, which designates the hour and minute, respectively
//      HR - 0-23; MIN - 0-59
#define TOD_CLOSE_HR (20)
#define TOD_CLOSE_MIN (30)

// Valid Time - given time of day is within operating time
#define VALID_TIME (0)

// Valid Time - Coaster should be running at this time, as scheduled by TPE
#define VALID_RUN_TIME (1)

// Invalid Minutes - hour is an operating hour, minutes are not
#define INVALID_MINUTE (-1)

// Invalid Hours - hour is not an operating hour.
#define INVALID_HOUR (-2)

// Invalid DOW - Day of Week is scheduled to have no operations. Overrides hour and minute validations
#define INVALID_DOW (-3)

// Invalid Date - Specific date is specified as a non-operating date. Overrides all other validations
#define INVALID_DATE (-4)

