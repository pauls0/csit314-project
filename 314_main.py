import requests
import random

# waiting for user to choose amount to test, if error occurs 5 test will run
try:
    testAmount = int(input())
except (IOError, TypeError, ValueError) as e:
    testAmount = 5

ranStrList = []
pyCalcAns = []

# creating a list of strings containing the multiplication of 2 ints between 0 and 201
i = 0
while i < testAmount:
  ranIntString = str(random.randint(1, 200)) + "*" + str(random.randint(1, 200))
  ranStrList.append(ranIntString)
  i += 1

# counter for test cases
counter = 1

# function to evalute either the equation string
def evaluateEquation(string):
    ans = eval(string)
    return ans

# looping through the equation string, returning pythons calculator answer and adding to list
for item in ranStrList:
    ans1 = evaluateEquation(item)
    pyCalcAns.append(ans1)


# using pythons request library to call the mathjs api to evaluate and compare
def requestsFunction(arg, pyAnswer):
    global counter
    req = requests.get('http://api.mathjs.org/v4/?expr='+arg)
    reqInt = int(req.text)
    if reqInt == pyAnswer:
        print("Test " + str(counter) + " = Success\nAPI calculator    " + arg + " = " + req.text + "\nPython calculator " + arg + " = " + str(pyAnswer) + "\n")
        counter += 1
    else:
        print("Test " + str(counter) + " = Fail\nAPI calculator " + arg + " = " + req.text + "\nPython calculator " + arg + " = " + str(pyAnswer) + "\n")
        counter += 1


counter1 = 0
while counter1 < testAmount:
   requestsFunction(ranStrList[counter1], pyCalcAns[counter1])
   counter1 += 1


