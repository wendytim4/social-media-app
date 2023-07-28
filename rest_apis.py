from flask import Flask

app = Flask(__name__)

# 1. Create a Student
@app.route('/voters', methods=['POST'])
#def create_student():