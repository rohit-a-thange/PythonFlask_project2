from flask import Flask, render_template, request
obj = Flask(__name__)

@obj.route("/")
def welcome():
    return "Welcome!"

@obj.route("/cal", methods = ["GET"])
def math_operator():
    operation = request.json["operation"] #we use request.json to interact using POSTMAN and not html file(for html we use request.form)
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation == "add":
        result = number1+number2
    elif operation == "multiply":
        result = number1*number2
    elif operation == "division":
        result = number1/number2
    else:
        result = number1-number2      
    return result





if __name__ == "__main__":
    obj.run(debug=True)