from pymongo import MongoClient
import datetime
import random
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    db = client['csci2963']
    collection = db['definitions']

    colSize = db.command('collStats', 'definitions')['count']

    rand = random.randrange(0,colSize-1)

    # text = collection.find().limit(-1).skip(rand).next()
    text = collection.find_one({'word': 'Blarm'})

    if 'dates' not in text.keys():
        text['dates'] = [str(datetime.datetime.now())]
    else:
        text['dates'].append(str(datetime.datetime.now()))

    collection.update_one({'word' : text['word']}, {'$set' : {'dates' : text['dates']}})

    print(collection.find_one({'word': text['word']}))

    return text['word'] + text['definition']


if __name__ == '__main__':
    print(random_word_requester())
