from flask import Flask, jsonify, request

app = Flask(__name__)

# Starting with a bit of dummy data
students = [
    {"id": 1, "name": "Zechariah", "grade": 10},
    {"id": 2, "name": "Alice", "grade": 11}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/delete-student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Search for the student by ID
    global students
    student_to_remove = next((s for s in students if s['id'] == student_id), None)

    if student_to_remove:
        # Re-create the list without the target student
        students = [s for s in students if s['id'] != student_id]
        return jsonify({
            "message": f"Student with ID {student_id} deleted successfully!",
            "deleted_student": student_to_remove
        }), 200
    
    # If the ID wasn't found
    return jsonify({"error": f"Student with ID {student_id} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
