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