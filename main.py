import code_functions as functions
import Important
import time

from code_functions import WebScrape

url = "http://programmer100.pythonanywhere.com/tours/"

while True:
    web = functions.WebScrape()
    file = functions.Files()
    html_data = web.scrape(url)
    extraction = web.extract(html_data)
    print(extraction)

    existing_tours = file.read_file()

    #making the message
    message = f"""\
subject: new event found
    
From: {Important.get_mail()}
new tour found {extraction}
"""

    if extraction != "No upcoming tours":
         if extraction+"\n" not in existing_tours:

            file.store(extraction)
            functions.send_email(message)
    time.sleep(3)