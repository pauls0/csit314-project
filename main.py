import sys
from test_predefined import test_predefined
from test_random import test_random

def main():
    a = test_predefined()
    b = test_random()
    
    if (a and b):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()