data = [{"Name": "Pip", "Age": 26, "Hair": "None", "Python-Score": 0.69,"Active": True},
{"Name": "Leia", "Age": 25, "Hair": "Purple", "Python-Score": 0.78,"Active": True},
{"Name": "Prof. Turtle", "Age": 134, "Hair": "Gray", "Python-Score": 0.99, "Active": False}]

#text file section
with open("textfile.txt", "w+") as file:

    #write to textfile
    file.writelines(str(x) + "\n" for x in data)

    #read from textfile
    file.seek(0)
    new_data = [eval(file.readline().replace("\n", "")) for i in range(len(data))]
    file.close()

#compare
print(str(new_data) == str(data))


#csv section
import csv
import ast
fields = ["Name", "Age", "Hair", "Python-Score", "Active"]

with open("csvfile.csv", "w+", newline="") as file:
    
    #write to cvs
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()
    writer.writerows(data)

    #read from csv
    file.seek(0)
    reader = csv.DictReader(file)
    new_data = [dict(row) for row in reader]
    file.close()

# Convert values to appropriate types (because csv.DictReader reads values as strings)
for item in new_data:
    for key, value in item.items():
        if key == "Age":
            item[key] = int(value)
        elif key == "Python-Score":
            item[key] = float(value)
        elif key == "Active":
            item[key] = value.lower() == 'true'

#compare
print(str(new_data) == str(data))


#json section
import json

with open('jsonfile.json', 'w+') as file:

    # Save to json
    json.dump(data, file)

    # Read from json
    file.seek(0)
    new_data = json.load(file)

# Compare
print(str(new_data) == str(data))