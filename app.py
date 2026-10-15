from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="calculation_system"
    )

def add_numbers(n1, n2):
    return n1 + n2
def subtract_numbers(n1, n2):
    return n1 - n2
def multiply_numbers(n1, n2):
    return n1 * n2
def average_numbers(n1, n2):
    return (n1 + n2) / 2

def divide_numbers(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2

def percentage_numbers(n1, n2):
    if n2 == 0:
        return "Cannot calculate percentage with zero"
    return (n1 / n2) * 100

def clean_result(result):
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM calculations ORDER BY id ASC")
    calculations = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("calculate.html", calculations=calculations)

@app.route("/calculate/ajax", methods=["POST"])
def calculate_ajax():
    try:
        number1 = float(request.form["number1"])
        number2 = float(request.form["number2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add_numbers(number1, number2)
        elif operation == "subtract":
            result = subtract_numbers(number1, number2)
        elif operation == "multiply":
            result = multiply_numbers(number1, number2)
        elif operation == "divide":
            result = divide_numbers(number1, number2)
        elif operation == "percentage":
            result = percentage_numbers(number1, number2)
        elif operation == "average":
            result = average_numbers(number1, number2)
        else:
            return jsonify({"success": False, "message": "Invalid operation"})

        if isinstance(result, str):
            return jsonify({"success": False, "message": result})

        result = clean_result(result)

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO calculations (number1, number2, operation, result) VALUES (%s, %s, %s, %s)",
            (number1, number2, operation, str(result))
        )
        db.commit()
        new_id = cursor.lastrowid

        cursor.execute("SELECT * FROM calculations WHERE id = %s", (new_id,))
        new_row = cursor.fetchone()
        cursor.close()
        db.close()

        return jsonify({
            "success": True,
            "result": result,
            "row": {
                "id": new_row["id"],
                "number1": new_row["number1"],
                "number2": new_row["number2"],
                "operation": new_row["operation"],
                "result": new_row["result"],
                "created_at": str(new_row["created_at"])
            }
        })

    except ValueError:
        return jsonify({"success": False, "message": "Please enter valid numbers"})

@app.route("/delete/<int:id>", methods=["POST"])
def delete_calculation(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM calculations WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"success": True, "message": "Deleted successfully"})

@app.route("/edit/<int:id>", methods=["POST"])
def edit_calculation(id):
    try:
        number1   = float(request.form["number1"])
        number2   = float(request.form["number2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add_numbers(number1, number2)
        elif operation == "subtract":
            result = subtract_numbers(number1, number2)
        elif operation == "multiply":
            result = multiply_numbers(number1, number2)
        elif operation == "divide":
            result = divide_numbers(number1, number2)
        elif operation == "percentage":
            result = percentage_numbers(number1, number2)
        elif operation == "average":
            result = average_numbers(number1, number2)

        if isinstance(result, str):
            return jsonify({"success": False, "message": result})

        result = clean_result(result)

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE calculations SET number1=%s, number2=%s, operation=%s, result=%s WHERE id=%s",
            (number1, number2, operation, str(result), id)
        )
        db.commit()
        cursor.close()
        db.close()

        return jsonify({
            "success": True,
            "number1": number1,
            "number2": number2,
            "operation": operation,
            "result": result
        })

    except ValueError:
        return jsonify({"success": False, "message": "Please enter valid numbers"})

if __name__ == "__main__":
    print("✅ Calculation System Starting...")
    app.run(debug=True)