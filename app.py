
# Flask Library
from flask import Flask, jsonify, request


# Create App Object
app = Flask(__name__)


# List of Students
students = [
    {
        "id": 1,
        "name": 'tom'
    },
    {
        "id": 2,
        "name": "Jerry"
    },
    {
        "id": 3,
        "name": "Bugs Bunny"
    }
]

# Example endpoint
@app.route('/example')
def home():
    return "Welcome to the Flask API!"

#### ASSIGNMENT STARTS HERE ####

#Get names
@app.route('/get')
def getNames():
    names = []
    for student in students:
        names.append(student['name'])
    return(jsonify(names))
        
#Get student by ID
@app.route('/get', methods=['POST'])
def getByID():
    data = request.get_json()
    studentID = int(data["id"])
    for student in students:
        if student["id"] == studentID:            
            return(student)

#Post new student
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    studentName = data["name"]
    studentID = len(students)+1
    student = {"id" : studentID, "name" : studentName}
    students.append(student)
    return(students)

#Edit student name
@app.route('/edit', methods=['POST'])
def edit():
    data = request.get_json()
    studentName = data["name"]
    studentID = int(data["id"])
    for student in students:
        if student["id"] == studentID:
            student["name"] = studentName
    return(students)

#Delete student
@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    studentID = int(data["id"])
    index = 0
    for student in students:
        if student["id"] == studentID:
            del students[index]
        else:
            index += 1
    return(students)
            

    
    
#### ASSIGNMENT ENDS HERE ####

if __name__ == '__main__':
    app.run(debug=True)
