import urllib.request
import json
import pymongo
from flask import Flask
import os
app = Flask(__name__)

# Транспортні засоби у розшуку. ID - Ідентифікатор. OVD - Регіон (орган внутрішніх справ).
# NSH - Номер шасі. NOM - Державний номер. NKU - Номер кузова. MDL - Марка,модель. COLOR - Колір.

def parse:
    description = urllib.request.urlopen('http://data.gov.ua/view-dataset/dataset-file/2334').read()
    dc = json.loads(description.decode('utf-8'))
    filename = dc['url'].split('/')[-1]
    os.system('wget %s' % dc['url'])
    os.system('mongodump --db mvs_wanted --collection autos --file %s' % filename)


@app.route("/")
def hello():
    return "Hello World!\nAll rights for the photo reserved by Thomas Leuthard(https://www.flickr.com/photos/thomasleuthard/)"

if __name__ == "__main__":
    app.run()
