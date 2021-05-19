import json
import requests
import pandas as pd
import os

target_test = "http://116.63.72.80:9200/"
show_index = "_cat/indices?v"

print("_________________________________________________________")
print("TARGET EXAMPLE : http://116.63.72.80:9200/")
target = input("Enter your target: ")
print("_________________________________________________________")

index_list = requests.get(target+show_index)

index = index_list.text

#create the text file that contains all the elasticsearch's indexes
f = open("index.txt", "w")
f.write(index)
f.close()

df = pd.read_fwf('index.txt')
df.to_csv('index.csv')

indici = df["index"].values

list = []
list = df["index"].tolist()


for i in list:
    requests.delete(target+i)
    print("Index ["+i+"] successfully deleted!")

os.remove("index.txt")
os.remove("index.csv")




























