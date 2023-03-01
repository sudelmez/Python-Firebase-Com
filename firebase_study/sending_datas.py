import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred =credentials.Certificate("/Users/sudeolmez/Downloads/working-with-pyth-firebase-adminsdk-amg1a-b66e2daef9.json")
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()


doc_first = firestore_client.collection("laptops").document("1") #do not need to specify explicitly to create a document. we can set them all here.
doc_first.set(
    {
        "name": "MacBook Air",
        "brand": "Apple",
    }
)

doc_first = firestore_client.collection("laptops").document("2")
doc_first.set(
    {
        "name" : "ideapad 3",
        "brand" : "lenovo",
        "year" : "2020"
    }
)

coll_ref = firestore_client.collection("laptops") #adds the end of the datas without needing an ID, with a random ID
create_time, doc_first = coll_ref.add(
    {
        "name": "Apple macbook air",
        "brand": "Apple",
    }
)
#how to create a subcollection?
laptop_ref = firestore_client.collection("laptops").document("4")
laptop_ref.set( 
    {
        "name": "Apple Macbook Pro",
        "brand": "Apple",
    }
)
attr_coll = laptop_ref.collection("attributes") #defining a subcollection here

attr_ref = attr_coll.document("storage") #defining a subcollection here

attr_ref.set({"name": "Storage", "value": "1", "unit": "TB"}) #uploading values
#attributes, created a kind of a list of maps. it can also be created with list method:
# ..."name": "Apple Macbook Pro",
#        "brand": "Apple",
#        "attributes": [
#            {"name": "Storage", "value": "1", "unit": "TB"},
#            {"name": "ram", "value": "16", "unit": "GB"},
#        ],...
