import csv
import os
import re
os.system('cls')

def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,

filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)

# Step 1

fields = ['Roll', 'Name', 'Email'] 

# Extracting CB_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchcb = re.compile(r'2001CB*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchcb, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("CB_STRENGTH", 'w')as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)    

# Extracting CE_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchcb = re.compile(r'2001CE*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchcb, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("CE_STRENGTH", 'w') as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)    

# Extracting CS_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchcs = re.compile(r'2001CS*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchcs, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("CS_STRENGTH", 'w') as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)  

# Extracting EE_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchee = re.compile(r'2001EE*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchee, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("EE_STRENGTH", 'w') as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)      

# Extracting ME_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchme = re.compile(r'2001ME*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchme, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("ME_STRENGTH", 'w') as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)  

# Extracting MM_STRENGTH.csv from Btech_2020_master_data.csv
rows = []
searchmm = re.compile(r'2001MM*')
STRENGTH = 0
with open("Btech_2020_master_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if re.search(searchmm, row):
            print(row)
            rows.append(row)
            STRENGTH+=1
 
 with open("MM_STRENGTH", 'w') as f:
    write = writer.csv(f)
    write.writerow(fields) 
    write.writerows(rows)  

    # Step 1 Ends