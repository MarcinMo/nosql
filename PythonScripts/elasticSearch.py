
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['nosql']
collection = db.reddit2
 # aggreation - wypisz wszystko subreddity, z ktorych byly zebrane dane.
# x = collection.aggregate(
#    [
#      { "$group" : { "_id" : "$subreddit"} }
#    ]
# )
#
# print(list(x))

x = collection.aggregate(
   [
      { "$unwind" : "$subreddit"}, { "$sortByCount": "$subreddit" }
   ]
)

print(list(x))