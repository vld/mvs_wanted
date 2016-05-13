import json
import pymongo
import os
import configparser


from flask import Flask
app = Flask(__name__)

# Транспортні засоби у розшуку. ID - Ідентифікатор. OVD - Регіон (орган внутрішніх справ).
# NSH - Номер шасі. NOM - Державний номер. NKU - Номер кузова. MDL - Марка,модель. COLOR - Колір.

# (LATIN,CYRILLIC)
symbols = (u"ABCEHIKMOPTX", u"АВСЕНІКМОРТХ")
en_to_ru = {ord(a):ord(b) for a, b in zip(*symbols)}
ru_to_en = {ord(b):ord(a) for a, b in zip(*symbols)}


def search_nom(nom):
    number_ru = nom.translate(en_to_ru)
    number_en = nom.translate(ru_to_en)
    return autos.find({'NOM': {'$regex': '(%s|%s)' % (number_ru, number_en)}})


@app.route("/")
def hello():
    # Law Enforcement
    return "Hello World!\nAll rights for the photo reserved by Thomas Leuthard(https://www.flickr.com/photos/thomasleuthard/)"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.txt')

    mongo_client = pymongo.MongoClient(host=config['mongodb']['host'], port=int(config['mongodb']['port']))
    autos = mongo_client.mvs_wanted.autos

    app.run()