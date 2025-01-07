import code_functions as functions

temp_string = """
              <h1 class="animated fadeIn mb-4">“For the things we have to learn before we can do them, we learn by doing them”- Aristotle</h1>
              <h1 align="right">Next Tour:</h1>
              <h1 align="right " id="displaytimer">Lions of the IDE, Clone City, 6.5.2088</h1>
              <p class="animated fadeIn text-muted">PythnoHow Team</p>
              """

url = "http://programmer100.pythonanywhere.com/tours/"

html_data = functions.scrape(url)
extraction = functions.extract(html_data)
print(extraction)

if extraction != "No upcoming tours":
    functions.send_email()