import code_functions as functions
import Important
import time

from code_functions import WebScrape

url = "http://programmer100.pythonanywhere.com/tours/"

while True:
    web = functions.WebScrape()
    file = functions.Files()
    email = functions.Email()


    html_data = web.scrape(url)
    extraction = web.extract(html_data)
    print(extraction)

    existing_tours = file.read()

    #making the message
    message = f"""\
subject: new event found
    
From: {Important.get_mail()}
new tour found {extraction}
"""

    if extraction != "No upcoming tours":
         if extraction+"\n" not in existing_tours:

            file.store(extraction)
            email.send(message)
