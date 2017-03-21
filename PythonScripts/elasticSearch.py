
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
keys = []
lista = []
#print(list(x))
for i in list(x):
   a = {i[u"_id"].encode('utf-8'): i[u"count"]}
   print a
   lista.append(a)
   keys.append(i[u"_id"].encode('utf-8'))



with open('redditData.csv', 'wb') as output_file:
   count = 100
   for item in lista:
      output_file.write("%s\n" % item)
      count -= 1
      if not count: break
