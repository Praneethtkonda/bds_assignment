import json
import pprint

from pymongo import MongoClient

file_name = './dataset.txt'
url_map = set()


def transformer(data):
    """
    Custom transformer code that does the following on the data
    1. Delete duplicates
    2. Remove URL field
    3. zipcode = outcode + postcode
    4. _id.$oid => id
    """
    if data['URL'] in url_map:
        #In Case of duplicate
        return None
    url_map.add(data['URL'])
    trans_obj = {}
    trans_obj['address'] = data['address']
    trans_obj['address_2'] = data['address line 2']
    trans_obj['name'] = data['name']
    trans_obj['zipcode'] = data['outcode'] + data['postcode']
    trans_obj['rating'] = data['rating']
    trans_obj['type_of_food'] = data['type_of_food']
    return trans_obj

if __name__=="__main__":
    try:
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client['bds']
        restaurants = db['restaurants']

        final_list = []
        file = open(file_name, "r")
        restaurants_list = file.readlines()

        for restaurant in restaurants_list:
            obj = json.loads(restaurant)
            trans_obj = transformer(obj)
            if trans_obj:
                print(f"Inserting record {trans_obj['name']}")
                restaurants.insert_one(trans_obj)
        # pprint.pprint(restaurants.find_one())

    except Exception as e:
        print("Error occured: ", e)

