import pandas as pd
from FunctionLibrary import ReadFormatFiles as RFF
from FunctionLibrary import TabulatePrint as TP
#File path and file name
path = "/Users/satyajeetpradhan/ESFutures/".replace("//","////")
file = "ES-Futureswith VIX.xlsx"

# Extract file details
readFile= pd.ExcelFile(path+file)
sheetList = readFile.sheet_names
del readFile


df = RFF.readDataframes(sheetList = sheetList, path = path,file = file)

df1 =[]
df1.append(df[0][df[0]['Day'] != 6])
df1.append(df[1][df[1]['Day'] != 6])

print("-------------------\n")
TP.tabulatePrint(df1[0].head(10))
print("-------------------\n")
TP.tabulatePrint(df1[1].head(10))
