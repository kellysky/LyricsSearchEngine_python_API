import pandas as pd
import json
from itertools import groupby
import pymongo
import re
import sys

def convert(ind):
    outlist = [ind['word'],]
    for k, v in ind['position'].items():
        outlist.append(k)
        outlist.append(str(len(v)))
        outlist.append(str(len(v)))
        for item in v:
            outlist.append(item)

    return " ".join(outlist)

def query_mongo(query):
   myclient = pymongo.MongoClient("8.209.74.127:27017")
   mydb = myclient["reverseIndex"]
   mycol = mydb["index"]

   r = []
   query=query.split()
   for  word in query:
      for i in mycol.find({"word" : word}):
          r.append(i)

   a = ""
   for i in r:
       a += convert(i) + "\n"

   with open("D:\Intel Idea\lyrics_demo\Index\index1.txt", 'w',encoding='UTF-8') as f:
        f.write(a)
   f.close()