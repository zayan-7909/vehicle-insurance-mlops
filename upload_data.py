import os
import pandas as pd
from pymongo import MongoClient

MONGODB_URL = os.environ["MONGODB_URL"]

client = MongoClient(MONGODB_URL)

db = client["Proj1"]
collection = db["Proj1-Data"]

df = pd.read_csv("notebook/data.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))

records = df.to_dict("records")

print("Uploading data...")

collection.insert_many(records, ordered=False)

print("Upload complete!")

print("Documents in collection:", collection.count_documents({}))

client.close()