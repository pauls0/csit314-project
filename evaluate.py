from api import api

# function to check a string with a mathemtical operation matches a known answer
# input: queryString - mathemtical operation as string
# input: answerExpected - known answer as float 
# return: a bool that represents if queryString is equal to answerExpected
def evaluate(queryString,answerExpected):
    
    answerAPI = api(queryString)            # get answer to query from api
    
    if (answerAPI == answerExpected):       # set return bool based on if answers match
        isCorrect = True
    else:
        isCorrect = False
    
    return isCorrect