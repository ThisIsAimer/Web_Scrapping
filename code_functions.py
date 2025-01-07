import requests
import selectorlib


def scrape(url):
    """uses python to scrape page source from url"""
    request = requests.get(url)
    source = request.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value

def read_file():
    with open("data.txt","r") as file:
        listed_items = file.readlines()

    return listed_items


def store(new_items):
    edited_item = new_items+"\n"

    with open("data.txt","a") as file:
        file.write(edited_item)



def send_email():
    print("email sent")
