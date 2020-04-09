from pymongo import MongoClient

#connect to the database
client = MongoClient("mongodb://localhost/fao")
db = client.get_database()
coll = db["fao"]

def givenYear(country,year,product):
    anio = str(year)
    vista = {"_id":0,"Area":1,"Item":1,"Element":1,f"{anio}":1}
    q = {"$and":[{"Item":f"{product}"},{"Area":f"{country}"},]}
    info = list(coll.find(q,vista))
    return info

