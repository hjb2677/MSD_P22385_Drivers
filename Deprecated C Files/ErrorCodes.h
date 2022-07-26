// MSD P22835
// Themed Entertainment Model Display
// File    : ErrorCodes.h
// Author  : Harrison Barnes
// Data    : 04/05/2022
// Purpose : Contains defines for Error codes and their error messages

//----- Generic Information -----//

// Error codes are 5-digit numbers - #####
//      - MSB (Bit 4) is the sys ID
//      - Bit 3,2 are the sub sys ID
//      - LSBs (bit 1, 0) is the error ID

// Ending message output - Shut down manually
#define FORCED_RETURN (0)
const char* exit_str_forced = "Program shutting down (manual) - Exiting with error code 0";

// Ending message output - safety shutdown of entire system
#define SAFE_RETURN (-42)
const char* exit_str_safe = "Critical safety error detected that requires shut down of entire system - Exiting with error code -42";

// Ending message output - fatal error
#define FATAL_RETURN (-420)
const char* exit_str_fatal = "Fatal error detected, could not recover program - Exiting with error code -420";

// Ending message output - unknown error caused fatal crash
#define UNKNOWN_RETURN (-96)
const char* exit_str_unknown = "Fatal error occurred but could not be identified, cause is unknown - Exiting with error code -96";

// Unknown error is used when an error is caught but not identified
#define UNKNOWN_ERROR (00000)
const char* error_str_unknown = "Error: unknown error - error caught but not identified";


//----- Acceptabilities -----//

// Acceptable - error allows continuation
#define ERR_ACCEPTABLE (100)

// Unacceptable - error prevents continuation
#define ERR_UNACCEPTABLE (-100)


//----- Severities -----//

// Severity = NOTE
#define SEV_NOTE (601)

// Severity = WARNING
#define SEV_WARN (602)

// Severity = ERROR
#define SEV_ERROR (603)

// Severity = FAILURE
#define SEV_FAIL (604)

//----- System 1 - Ride System -----//

// Error 1022# - Hall Sensor did not trigger when expected
#define E10200 (10200)
const char* error_str_E10200 = "Error 10200: Hall sensor at location XXXXXXX did not trigger when expected.";
#define E10201 (10201)
const char* error_str_E10201 = "Error 10201: Hall sensor at location XXXXXXX did not trigger when expected.";
#define E10202 (10202)
const char* error_str_E10202 = "Error 10202: Hall sensor at location XXXXXXX did not trigger when expected.";
#define E10203 (10203)
const char* error_str_E10203 = "Error 10203: Hall sensor at location XXXXXXX did not trigger when expected.";

//----- System 2 - Show System -----//


//----- System 3 - Interactive System -----//


//----- System 4 - Power System -----//


//----- System 5 - Control System -----//

// Error 50000 - Connection to show controller lost
#define E5000 (50000)
const char* error_str_E50000 = "Error 50000: Connection to show controller lost.";

// Error 50100 - Failed to fetch current time
#define E50100 (50100)
const char* error_str_E50100 = "Error 50100: Failed to fetch current local time.";


//----- System 6 - Error Reporting System -----//

// Error 60000 - Email failed
#define E6000 (60000)
const char* error_str_E60000 = "Error 60000: Failed to send email.";

