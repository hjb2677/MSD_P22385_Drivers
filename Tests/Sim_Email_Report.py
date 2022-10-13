import ErrorReporter
import ErrorReport
import ErrorCodes
import Scheduler

def SimEmailReport():
    print("Simulating error")
    timestamp = Scheduler.GetTimestamp()
    ErrorReporter.EmailErrorToClient(ErrorReport.EMAIL_REPORTER_TEST_ERROR, timestamp)
    print("Simulation done")


if __name__ == "__main__":
    SimEmailReport()

