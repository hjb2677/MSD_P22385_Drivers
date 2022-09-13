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
import Scheduler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def ErrorReporterDriver():
    errorCode = ErrorReport.EMAIL_REPORTER_TEST_ERROR
    timestamp = Scheduler.GetTimestamp()
    EmailErrorToClient(errorCode, timestamp)
    return ErrorReport.ERROR_REPORTER_CONTINUE_DRIVER


"""
Function : EmailErrorToClient
Inputs   : errorCode - the driver-determined error code associated with the identified error
Outputs  : none

Sends a formatted error notification email to the client. accompanied with other potentially
useful information
"""
def EmailErrorToClient(errorCode, timestamp):
    # Obtain display email address and gmail app password for authentication
    smtp_user = ErrorReport.EMAIL_ORIGIN_ADDRESS
    smtp_password = ErrorReport.APP_PASSWORD

    # Set up smtp server and port number. Used for sending the email
    server = "smtp.gmail.com"
    port = 587

    # Fill out message parts. Subject, From, To, and MSG
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Error Occurred - CODE : " + str(errorCode) + " at " + timestamp
    msg["From"] = smtp_user
    msg["To"] = ErrorReport.EMAIL_DESTINATION_ADDRESS

    # Actual message goes here
    msg.attach(MIMEText("\nThe Raspberry Pi in the TPE Display has detected an error." +
                        "\nERROR CODE - " + str(errorCode) + " at " + timestamp +
                        "\nRefer to reference manual for causes, debugging, etc.", "plain"))

    # Initialize smtp server
    emailServer = smtplib.SMTP(server, port)
    emailServer.ehlo()
    emailServer.starttls()

    # Use gmail account and app password to login to the display email
    emailServer.login(smtp_user, smtp_password)

    # Notify customer of the issue
    emailServer.sendmail(smtp_user, "hjb2677@g.rit.edu", msg.as_string())

    # Close the smtp server connection
    emailServer.quit()

