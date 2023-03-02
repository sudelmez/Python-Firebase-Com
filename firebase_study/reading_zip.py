import json  
import zipfile 

d = None  
data = None  

with zipfile.ZipFile("/Users/sudeolmez/Downloads/foodai_firebase_backend.zip", "r") as z:
    for filename in z.namelist():
        print(filename)
        with z.open(filename) as f:
            data = f.read()
            print(data)
