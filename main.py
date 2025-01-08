import code_functions as functions
import Important

url = "http://programmer100.pythonanywhere.com/tours/"

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
     if extraction not in existing_tours:

        functions.store(extraction)
        functions.send_email(message)