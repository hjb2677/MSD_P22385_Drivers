// MSD P22835
// Themed Entertainment Model Display
// File    : POST.h
// Author  : Harrison Barnes
// Data    : 04/05/2022
// Purpose : Contains defines for the POST (Power On Self Test)

//----- Return Codes -----//

// POST Pass - POST finds no issues
#define POST_PASS (600)

// POST Fail - Return a SEVERITY code from below

// Severity = NOTE
#ifndef SEV_NOTE
#define SEV_NOTE (601)
#endif

// Severity = WARNING
#ifndef SEV_WARN
#define SEV_WARN (602)
#endif

// Severity = ERROR
#ifndef SEV_ERROR
#define SEV_ERROR (603)
#endif

// Severity = FAILURE
#ifndef SEV_FAIL
#define SEV_FAIL (604)
#endif

//----- Acceptabilities -----//

// Acceptable - error allows continuation
#ifndef ERR_ACCEPTABLE
#define ERR_ACCEPTABLE (100)
#endif

// Unacceptable - error prevents continuation
#ifndef ERR_UNACCEPTABLE
#define ERR_UNACCEPTABLE (-100)
#endif

