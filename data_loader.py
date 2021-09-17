import json
import pprint
from pymongo import MongoClient, errors

file_name = './dataset.txt'

def transformer(data):
    """
    Custom transformer code that does the following on the data
    1. Delete duplicates
    2. Remove URL field
    3. zipcode = outcode + postcode
    4. _id.$oid => id
    """
    trans_obj = {}
    trans_obj['address'] = str(data['address'])
    trans_obj['address_2'] = str(data['address line 2'])
    trans_obj['name'] = str(data['name'])
    trans_obj['zipcode'] = data['outcode'] + data['postcode']
    trans_obj['rating'] = data['rating']
    trans_obj['type_of_food'] = data['type_of_food']
    return trans_obj

if __name__=="__main__":
    try:
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client['bds']
        restaurants = db['restaurants']
        # Creating index on name and zipcode
        res = restaurants.create_index([('name', 1), ('zipcode', 1)], unique = True)
        print(f"Created Index: {res}")

        file = open(file_name, "r")
        restaurants_list = file.readlines()

        for restaurant in restaurants_list:
            obj = json.loads(restaurant)
            trans_obj = transformer(obj)
            print(f"Inserting record {trans_obj['name']}")
            try:
                restaurants.insert_one(trans_obj)
            except errors.DuplicateKeyError:
                print(f"Duplicate key found for {trans_obj['name']}")
            finally:
                continue
        # pprint.pprint(restaurants.find_one())

    except Exception as e:
        print("Error occured: ", e)

