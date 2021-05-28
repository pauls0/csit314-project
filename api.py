import requests     # used to make a http request
import urllib       # used to do URL percent-encoding

# function to return an answer from an api
# input is a string containing a mathemtical operation
# returns a float of the answer evaluated by the api
def api(queryString):
    
    encodedQuery = urllib.request.pathname2url(queryString)     # convert UTF-8 query to URL percent-encoding
    apiURL = "http://api.mathjs.org/v4/?expr="                  # api endpoint url
    requestURL = apiURL + encodedQuery                          # make api url for the query
    apiResponse = requests.get(requestURL)                      # make http request to api
    answer = apiResponse.text                                   # get the answer element of the response
    answerFloat = float(answer)                                 # cast answer String to float

    return answerFloat 