// MSD P22835
// Themed Entertainment Model Display
// File    : DisplayDriver.c
// Author  : Harrison Barnes
// Data    : 05/03/2022
// Purpose : Driver program for the entire display

//----- Includes -----//
#include "Scheduler.c"
#include <time.h>
#include <stdio.h>
#include <unistd.h>


int main(int argc, char *argv[]) {

    // Variable declarations
    
    // validation code for Scheduler
    int validationCode = -1;


    //////////////////////////////////////////////////////
    //      SCHEDULER BLOCK BEGIN
    //////////////////////////////////////////////////////

    printf("Entering scheduler...\n");

    while(validationCode < 0) {

        printf("Fetch and validate...\n");   

        // Wait for scheduled time#include<unistd.h>
        sleep(TEST_FECTH_TIMESTAMP_DELAY_MS);

        // Fetch and validate from scheduler 
        validationCode = Scheduler();
    }

    printf("Exiting scheduler...\n");

    //////////////////////////////////////////////////////
    //      SCHEDULER BLOCK END
    //////////////////////////////////////////////////////

}