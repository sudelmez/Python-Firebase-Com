import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred =credentials.Certificate("/Users/sudeolmez/Downloads/working-with-pyth-firebase-adminsdk-amg1a-b66e2daef9.json")
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()

doc_first = firestore_client.collection('laptops').document("1")

doc = doc_first.get() #we get a snapshot data in order to read
print(f"The document is {doc.to_dict()}") #showing as maps

#how to get laptops whose brand is Apple?
show_ref= firestore_client.collection("laptops")
find_ref= show_ref.where("brand", "==", "Apple")

for doc in find_ref.stream(): #stream is more useful than get
    print(f"{doc.id} => {doc.to_dict()}")

#query_ref = coll_ref.where("brand", "in", ["HP", "Lenovo"]) #this method is used as 'or'

#query_ref = coll_ref.where("tags", "array_contains", "Popular")  #this is used as 'whatever includes'

doc_ref = firestore_client.collection("laptops").document("2")
doc_ref.update({"order.quantity": 5}) #with 'update', we can change a value

#witf ..doc_name...delete() , we can delete the folder that exists.

    