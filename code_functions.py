import requests
import selectorlib

url = "http://programmer100.pythonanywhere.com/tours/"

def scrape():
    """uses python to scrape page source from url"""
    request = requests.get(url)
    source = request.text
    return source