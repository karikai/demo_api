import pymongo

myclient = pymongo.MongoClient("mongodb://ec2-18-116-42-212.us-east-2.compute.amazonaws.com:27017/")

def createCRUD(collectionName, data):
   try:
      db = myclient['test']
      currentCollection = db[collectionName]
      currentCollection.insert(data)
      return True
   except:
      print("Unexpected error")
      return False

def readCRUD(collectionName, query):
   try:
      db = myclient['test']
      currentCollection = db[collectionName]
      results = []

      for doc in currentCollection.find(query, {'_id': False}):
         print(doc)
         results.append(doc)
      return results
   except:
      print("Unexpected error")
      return False

def updateCRUD(collectionName, query, data):
   try:
      db = myclient['test']
      currentCollection = db[collectionName]
      newData = { "$set": data }
      currentCollection.update_one(query, newData)
      return True
   except:
      print("Unexpected error")
      return False

def deleteCRUD(collectionName, query):
   try:
      db = myclient['test']
      currentCollection = db[collectionName]
      currentCollection.delete_many(query)
      return True
   except:
      print("Unexpected error")
      return False