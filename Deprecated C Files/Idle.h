// MSD P22835
// Themed Entertainment Model Display
// File    : Idle.h
// Author  : Harrison Barnes
// Data    : 04/05/2022
// Purpose : Contains defines for the display's Idle state and user input

// Check Period - The maximum time (ms) the Idler waits for user input. If no input
//      is provided within Check Period, the Idler returns to the scheduler
//      Check period currently set to 5 min = 300,000 ms
#define CHECK_PERIOD_MS (300000)

//----- Return Codes -----//

// Check Period suprassed - Returns if the check period suprasses without any input
#define CHECK_PERIOD_SURPASSED (0)

// User Input Found - Returns if the Idle polling finds user input
#define USER_INPUT_FOUND (1)

