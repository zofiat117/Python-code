import csv
#import pandas
import statistics

tottemp=0
recct=0
# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline='')
csv_reader = csv.reader(csvfile)
header = next(csv_reader, None)

line = csvfile.readline()
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print(line)

line = csvfile.readline()
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print(line)

line = csvfile.readline()
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print(line)

line = csvfile.readline()
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print(line)

print("Tottemp\n",tottemp," ",recct)
print(tottemp/recct)