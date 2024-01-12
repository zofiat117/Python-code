import csv
import statistics

csvfile = open('myfile3.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Noise', 'Temp'])
print("Columns Created")
csvwriter.writerow([25, 10])
csvwriter.writerow([24, 12])
csvfile.close()

csvfile = open('myfile3.csv', 'r')
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
csvfile.close()


csvfile = open('myfile3.csv',"a", newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow([12, 9])
csvwriter.writerow([33, 77])
csvfile.close()
print("closed append")
