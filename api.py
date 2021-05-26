from bs4 import BeautifulSoup
import requests
import urllib

def api(queryString):
    queryEncoded = urllib.request.pathname2url(queryString)
    queryURL = "https://www.google.com/search?q=" + queryEncoded

    headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}
    html = requests.get(queryURL, headers=headers).text
    answer = BeautifulSoup(html, 'html.parser').select_one('.qv3Wpe').text
    
    return float(answer)