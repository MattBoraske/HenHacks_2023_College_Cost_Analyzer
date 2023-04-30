from flask import Flask
from flask import redirect, url_for, request
from flask import Flask, render_template
from API_queries.newEarnings import earningsQuery

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/process_input', methods=['POST'])
def process_input():
    college_name = request.form['college-name']
    college_major = request.form['college-major']
    residence = request.form['residence']
    print(f"College: {college_name}")
    print(f"Major: {college_major}")
    print(f"Residence: {residence}")
    print("\n")

    earnings = earningsQuery(college_name)

    return f"Input received! Earnings is: {earnings}"

if __name__ == "__main__":
    app.run(debug=True)