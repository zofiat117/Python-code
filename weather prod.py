import csv

#Writing the CSV file
try:
    with open('weatherprod.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Day', 'Brightness', 'Temperature', 'Rain'])
        print("Columns Created")

        # Writing rows of data
        csvwriter.writerow(['1', 'Yes', 'High', 'No'])
        csvwriter.writerow(['2', 'No', 'High', 'Yes'])
        csvwriter.writerow(['3', 'Yes', 'Mild', 'No'])
        csvwriter.writerow(['4', 'Yes', 'Mild', 'Yes'])
        csvwriter.writerow(['5', 'Yes', 'Cold', 'No'])
        csvwriter.writerow(['6', 'No', 'Mild', 'No'])
        csvwriter.writerow(['7', 'No', 'Cold', 'Yes'])
        print("Data added successfully.")

except Exception as e:
    print(f"Error while writing CSV: {e}")

# Step 2: Reading and processing the CSV file
try:
    with open('weatherprod.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Check if the file is empty
        header = next(csvreader, None)
        if header:
            print("Line:", header)
        else:
            print("The CSV file is empty.")
            raise SystemExit

        # Process rows
        for row in csvreader:
            # Skip empty rows or rows with insufficient columns
            if len(row) < 4:
                print("Skipping invalid or empty row:", row)
                continue  # Skip this row if it doesn't have enough columns
            
            print("Row:", row)  # Print each valid row for debugging

            # Check the value in the Brightness column (index 1)
            if row[1] == "No":
                print("Low Productivity")
            elif row[1] == "Yes":
                if row[2] == "High" :
                    print("Low Productivity")
                elif row[2] == "Mild" or "Cold":
                    if row[3] == "Yes":
                        print("Low Productivity")
                    elif row[3] == "No":
                        print("High Productivity")
                        
                
                
except Exception as e:
    print(f"Error while reading CSV: {e}")