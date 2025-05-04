import json

filename = './student.json'
listObj = []

# Read the JSON file and load it into a list
with open(filename, 'r') as file:
    listObj = json.load(file)

# Print the list
#print(listObj)
#print(type(listObj))

# Function to print student details in the specified format
def print_student_details(listObj):
    for student in listObj:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

# Call the function to print the details
print('These are the orginial student details:')
print_student_details(listObj)
print('')

listObj.append({
    "F_Name": "Adam",
    "L_Name": "Bench",
    "Student_ID": 369189,
    "Email": "abench@my365.bellevue.edu"
})

print('The Student List has been updated:')
print_student_details(listObj)
print('')

# Write the updated list back to the JSON file
with open(filename, 'w') as file:
    json.dump(listObj, file, indent=4)

print('The .json file was updated with the new student list.')