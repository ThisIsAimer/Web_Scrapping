import requests
import selectorlib
import smtplib,ssl,Important

class WebScrape:
    def scrape(self,url):
        """uses python to scrape page source from url"""
        request = requests.get(url)
        source = request.text
        return source

    def extract(self,source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)['tours']
        return value


class Files:
    def __init__(self,filepath = "data.txt"):
        self.fileRead = open(filepath,"r")
        self.fileWrite = open(filepath,"w")


    def read(self):

        listed_items = self.fileRead.readlines()
        print(listed_items)

        return listed_items


    def store(self,new_items):
        edited_item = new_items+"\n"


        self.fileWrite.write(edited_item)


class Email:
    def send(self,message, receiver = Important.get_mail()):
        host = "smtp.gmail.com"
        post = 465
        user_name = Important.get_mail()
        password = Important.get_pass()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, post, context=context) as server:
            server.login(user_name, password)
            server.sendmail(user_name, receiver, message)