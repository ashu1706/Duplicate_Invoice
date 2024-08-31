import pandas as pd

masterList=[]
duplicateIDs=[]
dataFrames=[]
data=""


#reading csv file

try:
    data= pd.read_csv("data/joined_dataset_final.csv")
except:
    print("Error opening file. Please check the filename and try again. Existing... ")
    exit()

data["unique_id"] = (data["WRBTR"].astype("str")+ data["BUKRS"].astype("str")+data["BLDAT"]+ data["XBLNR"] ) #creating unique id 

#iterating through data

for i, row in data.iterrows():
    if row["unique_id"] not in masterList:
        masterList.append(row["unique_id"])    #if unique id not present add in masterList
    else:
        duplicateIDs.append(row["unique_id"])  #if already present add into duplicateIds


for i in duplicateIDs:
    dataFrames.append(data.loc[data["unique_id"]==i])


dataFrames= pd.concat(dataFrames)
dataFrames.to_csv("data/duplicates.csv")
