import json
import csv
from datetime import datetime

json_file = "E:\DAIICT\Sem 2\Deep Learning\Sentiment\RawData\Baby_Products.jsonl"  
csv_file = "output.csv"

fields = ["timestamp","rating","title","text","parent_asin","verified_purchase"]

with open(json_file, "r", encoding="utf-8") as infile, open(csv_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fields)
    writer.writeheader() 
    
    for line in infile:
        data = json.loads(line.strip()) 
        
        timestamp_sec = data["timestamp"] / 1000
        data["timestamp"] = datetime.utcfromtimestamp(timestamp_sec).strftime("%Y-%m-%d %H:%M:%S")
        
        writer.writerow({field: data[field] for field in fields})

print(f"CSV file '{csv_file}' created successfully!")

