from pymongo import MongoClient

#  Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]  # database
collection = db["users"]  # collection (like a table)

# Insert one document
collection.insert_one({"name": "jeshwanth", "email": "jeshwanth@gmail.com"})

# Insert many
collection.insert_many([
    {"name": "sai", "email": "SAi@gmail.com"},
    {"name": "charna", "email": "charn@gmail.com"}
])

#Find all
for user in collection.find():
    print(user)

#Find with filter
print(collection.find_one({"name": "jeshwanth"}))

#Update
collection.update_one({"name": "sai"}, {"$set": {"email": "sai@gmail.com"}})
print("This is new updated databases")
for user in collection.find():
    print(user)

#Delete
collection.delete_one({"name": "charna"})

#Count documents
print("Total users:", collection.count_documents({}))
