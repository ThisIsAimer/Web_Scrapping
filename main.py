import code_functions as functions
import Important
import time

url = "http://programmer100.pythonanywhere.com/tours/"

while True:
    html_data = functions.scrape(url)
    extraction = functions.extract(html_data)
    print(extraction)

    existing_tours = functions.read_file()

    #making the message
    message = f"""\
subject: new event found
    
From: {Important.get_mail()}
new tour found {extraction}
"""

    if extraction != "No upcoming tours":
         if extraction+"\n" not in existing_tours:

            functions.store(extraction)
            functions.send_email(message)
    time.sleep(3)