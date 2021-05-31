import sys
from test_predefined import test_predefined
from test_random import test_random

def main():
    
    print("\nExecuting Random-tests")
    a = test_random()
    
    print("\nExecuting Predefined-tests")
    b = test_predefined()
    
    print("\n\n--FINAL TEST RESULT--")
    if a:
        print("Test Result Random-tests: ALL PASSED")
    else:
        print("Test Result Random-tests: TEST RETURNED ERROR")

    if b:
        print("Test Result Predefined-tests: ALL PASSED")
    else:
        print("Test Result Predefined-tests: TEST RETURNED ERROR")

    if (a and b):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()