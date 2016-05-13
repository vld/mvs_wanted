import json
import pymongo
import os
import configparser


from flask import Flask
app = Flask(__name__)

# Транспортні засоби у розшуку. ID - Ідентифікатор. OVD - Регіон (орган внутрішніх справ).
# NSH - Номер шасі. NOM - Державний номер. NKU - Номер кузова. MDL - Марка,модель. COLOR - Колір.

symbols = (u"ABCEHIKMOPTX", u"АВСЕНІКМОРТХ")
tr = {ord(a):ord(b) for a, b in zip(*symbols)}


def search_nom(nom):
    number = nom.translate(tr)
    autos.find({'NOM': {'$regex': number}})


@app.route("/")
def hello():
    return "Hello World!\nAll rights for the photo reserved by Thomas Leuthard(https://www.flickr.com/photos/thomasleuthard/)"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.txt')

    mongo_client = pymongo.MongoClient(host=config['mongodb']['host'], port=int(config['mongodb']['port']))
    autos = mongo_client.mvs_wanted.autos

    app.run()