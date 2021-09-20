from pymongo import MongoClient
import pprint

from pymongo.aggregation import _DatabaseAggregationCommand

client = MongoClient("mongodb://root:example@localhost:27017/")
db = client['bds']
restaurants = db['restaurants']

question= input("enter 1 for for first question , 2 for second question, 3 and 4  for 3rd and 4th question respectively\n")

##1.    User provides a choice of cuisine and zipcode, the query 
##returns a list of top 5 restaurant names with full address and rating with results sorted descending order based on rating.
##query1

if question=='1':
    cuisine = input('What cuisine ?\n').strip().lower().capitalize()
    zipcode = input('Which zipcode ?\n').strip().upper()
    print(cuisine,zipcode)

    query1={'$and':[{'type_of_food':cuisine},{'zipcode':zipcode}]}
    
    projection1={"name":1,'address':1,'rating':1}

    docs=restaurants.find(query1,projection1).sort("rating",-1).limit(5)
    print("Below are the top 5 restraunts int he zip code as per rating")
    for doc in docs:
        print(f'{doc["name"]} - {doc["address"]} - {doc["rating"]}')


#query 2
# 2.    User provides a string to be searched in the address field and a minimum rating. The query returns all restaurant names 
# and cuisine that match the inputs provided along with the match score. Sort output by descending score.
elif question=='2':
    search_string = input('Enter the search string for address.\n').strip()
    minimum_rating = float(input('Rnter the minimum rating.\n').strip())
    search_string = f'""{search_string}""'
    query2 = [{'$match':{ '$text': { '$search': search_string,  '$caseSensitive': False } }},{'$match':{'rating':{'$gte':minimum_rating}}},\
    { '$sort': { 'score': { '$meta': "textScore" } } },\
    { '$project': { '_id': 0,'name':1,'type_of_food':1,'score': { '$meta': "textScore" } } },\
        {'$sort':{'score':-1}}]
    
    docs = restaurants.aggregate(query2)
    for doc in docs:
        print(doc)

# 3.Give a cuisine, output how many (i.e. count) matching restaurants are there per zip code.
#  Sort descending the 2 column output (zipcode, count) by the count.

elif question=='3':
    cuisine = input("Which cuisine ?\n").strip().lower().capitalize()
    query3=[{'$match':{"type_of_food":cuisine}},{'$group':{'_id':'$zipcode', 'count': {'$count':{}}}},{'$sort':{'count':-1,'_id':-1}}]
    docs = restaurants.aggregate(query3)
    for doc in docs:
        print(doc)



# 4.    Show the average rating per type of food and provide an ascending sorted output (type of food, rating) by rating. 
elif question=='4':
    query4=[{'$group':{'_id':'$type_of_food','average_rating':{'$avg':"$rating"}}},{'$sort':{'average_rating':-1}},\
        {'$project':{'food':"$_id","average_rating":1,"_id":0}}]
    docs = restaurants.aggregate(query4)
    for doc in docs:
        print(doc)

else:
    print("select option 1 2 3 or 4")
