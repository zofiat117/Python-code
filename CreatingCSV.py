import csv
print("complete")
csvfile = open('myfile.csv', 'x')
print("File Created")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Fname', 'Sname', 'Age', 'City'])
print("Columns Created")

csvwriter.writerow(['Mary', 'Smith', '17', 'Dublin'])
print("Data Added")

csvfile.close()
print("closed")