from evaluate import evaluate
import random

def executeTest(queryString,answerExpected):
    
    result = evaluate(queryString,answerExpected)                                           # bool: does query = ans
    print('Test: ["' + queryString + '" == ' + str(answerExpected) + '] ' + str(result))    # print of the test running
    return result
    
def test_random():
    
    print("\nRandom Tests Executing:")
    
    test_list = []      # list to store test results
    
    # Random test of addition
    r1 = random.randint(1, 100)                                     # generate a random int [1-100]
    r2 = random.randint(1, 100)                                     # generate a random int [1-100]
    equationString = str(r1) + "+" + str(r2)                        # create equatiion string to send to api
    answer = r1 + r2                                                # calc ans in python
    test_list.append(executeTest(equationString, float(answer)))    # add to list a bool for if the two answers equal
    
    # Random test of subtraction
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    equationString = str(r1) + "-" + str(r2)
    answer = r1 - r2
    test_list.append(executeTest(equationString, float(answer)))
    
    # Random test of division
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    equationString = str(r1) + "/" + str(r2)
    answer = r1 / r2
    test_list.append(executeTest(equationString, float(answer)))
    
    # Random test of multiplication
    r1 = random.randint(1, 100)
    r2 = random.randint(1, 100)
    equationString = str(r1) + "*" + str(r2)
    answer = r1 * r2
    test_list.append(executeTest(equationString, float(answer)))
    
    # loop through list of test results and set function return
    allPassed = True
    for test in test_list:
        if (test == False):
            allPassed = False
   
    # print overall Random Testing Result
    if allPassed:
        print("Random Tests Result: ALL PASSED")
    else:
        print("Random Tests Result: ALL TESTS DID NOT PASS")
        
    return allPassed