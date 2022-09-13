import ErrorReporter
import ErrorReport
import ErrorCodes

def SimEmailReport():
    print("Simulating error")
    ErrorReporter.EmailErrorToClient(ErrorReport.EMAIL_REPORTER_TEST_ERROR)
    print("Simulation done")


if __name__ == "__main__":
    SimEmailReport()

