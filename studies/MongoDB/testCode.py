import pymongo

## Connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

## Select/Create db (nb: it won't be created untill data will be insert)
mydb = myclient["mydatabase"]
## Collection (in relational db is a table)
mycol = mydb["customers"] 



def checkCollectionExists():
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")


##### INSERT
def insertMultipleCustomer():

    mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)
    ## list of id values of inserted documents
    #print(x.inserted_ids)


def insertSingleCustomerSpecificID():
    ##whatch out, if the _id already exists, will throw and exception
    customer = { "_id": 17, "name": "Alby", "address": "VittVeneto"} ##with a specific id 
    ## In other records, where not specified there will be the object id (inserted_ids)
    x = mycol.insert_one(customer)


##### FIND/SELECT

def findOne():

    x = mycol.find_one()

    print(x)
    #print(myclient.list_database_names())

# is like a SELECT * in MySQL
def findAll():
    mycol = mydb["customers"]
    for x in mycol.find():
        print(x) 

    ## or just some field
    for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
      #print(x)
      pass
    ##To exlude a field, like address just -> "address": 0
    ####################################################
    ## LIMIT
    #mycol.find().limit(5)
    ## SORT
    #mycol.find().sort("name",-1)
    #########################à


##### QUERY

def queryFind():
    myquery = { "address": "Park Lane 38" }
    
    #myquery = { "address": {"$gt":"S"} } #started with S (gt=greater than)
    #myquery = { "address": {"$regex":"^S"} } #or w/ Regular Expression

    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


##### UPDATE

def updateSingle():
    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }

    mycol.update_one(myquery, newvalues)
    #print costumer after update
    for x in mycol.find():
        print(x)

def updateMany():
    myquery = { "address": { "$regex": "^S" } }
    newvalues = { "$set": { "name": "Minnie" } }

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count, "documents updated.")



##### DELETE/DROP

def deleteElement():

    myquery = { "address": "Mountain 21" }
    mycol.delete_one(myquery)

def deleteManyElem():
    myquery = { "address": {"$regex": "^S"} }
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

    ## OR delete all from collection with:
    #x = mycol.delete_many({})
    #print(x.deleted_count," documents deleted.")

def dropCollection():
    mycol.drop()


def main():
    insertMultipleCustomer()
    try:
        insertSingleCustomerSpecificID()
    except:
        print("Customer with that ID already exists")
        

    #findOne()
    findAll()

main()
#missing: update, delete/drop, query