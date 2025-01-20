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

    existing_tours = file.reading()
    file.close_r()


    #making the message
    message = f"""\
subject: new event found
    
From: {Important.get_mail()}
new tour found {extraction}
"""

    if extraction != "No upcoming tours" and extraction not in existing_tours:

        file.store(extraction)
        file.close_w()
        email.send(message)

    time.sleep(3)