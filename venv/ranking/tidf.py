import pymongo
import mysql.connector


client = pymongo.MongoClient('mongodb://8.209.74.127:27017/')

db=client.reverseIndex

collection=db.index


total_number=collection.count()
doc_number=collection.find({'words_id':'00'}).count()

mydb = mysql.connector.connect(
  host="8.209.74.127",
  user="root",
  db='lyrics',
  passwd="password",
  port='3306'
)

mycursor=mydb.cursor();

mycursor.execute("select content from Song where id =1")

myresult=mycursor.fetchall()





