import urllib.request
import json
import pymongo
import os
import configparser

def load_data():
    description = urllib.request.urlopen('http://data.gov.ua/view-dataset/dataset-file/2334').read()
    dc = json.loads(description.decode('utf-8'))
    filename = dc['url'].split('/')[-1]
    filepath = 'data/%s' % (filename)
    if (not os.path.exists(filepath)) | (not os.path.isfile(filepath)):
        os.system('wget %s -P data' % dc['url'])
        if 'autos' in mongo_client.mvs_wanted.collection_names():
            mongo_client.mvs_wanted.autos.drop()
        os.system('mongoimport --db mvs_wanted --collection autos --file %s' % filepath)
        mongo_client.mvs_wanted.autos.create_index([("NKU", pymongo.ASCENDING)], background=True)
        mongo_client.mvs_wanted.autos.create_index([("NSH", pymongo.ASCENDING)], background=True)
        mongo_client.mvs_wanted.autos.create_index([("NOM", pymongo.ASCENDING)], background=True)

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.txt')

    mongo_client = pymongo.MongoClient(host=config['mongodb']['host'], port=int(config['mongodb']['port']))

    load_data()