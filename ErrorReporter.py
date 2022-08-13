"""
MSD P22385
Themed Entertainment Model Display
File    : ErrorReported.py
Author  : Harrison Barnes
Date    : 07/26/2022
Purpose : Driver program for the Error Reporting system
"""

# Includes
import ErrorCodes
import ErrorReport
import smtplib
from email.message import EmailMessage

def ErrorReporterDriver():
    errorCode = ErrorReport.EMAIL_REPORTER_TEST_ERROR
    EmailErrorToClient(errorCode)
    return ErrorReport.ERROR_REPORTER_CONTINUE_DRIVER


"""
Function : EmailErrorToClient
Inputs   : errorCode - the driver-determined error code associated with the identified error
Outputs  : none

Sends a formatted error notification email to the client. accompanied with other potentially
useful information
"""
def EmailErrorToClient(errorCode):
    pass

