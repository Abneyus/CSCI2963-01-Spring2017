from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()

def main():
    db = client['csci2963']
    collection = db['definitions']

    # Find all
    print('**** FIND ALL ****')
    cursor = collection.find()
    for word in collection.find():
        print(word)

    # Find one
    print('**** FIND ONE ****')
    print(collection.find_one()['word'])
    print(collection.find_one({"word": "Blarm"})['word'])

    # Specific
    print('**** FIND SPECIFIC ****')
    print(collection.find({"word" : "Blarm"}).next()['word'])

    # ID
    print('**** FIND BY ID ****')
    print(collection.find({"_id" : ObjectId('56fe9e22bad6b23cde07b8d1')}).next()['word'])

    # Insert a new record
    print('**** INSERT RECORD ****')
    collection.insert_one({"word" : "memes", "definition" : "a mistake"})

    print(collection.find_one({ "word" : "memes"}))

if __name__ == '__main__':
    main()
