from flask import Flask
from flask import redirect, url_for, request
from flask import Flask, render_template
from API_queries.majorEarnings_API import earningsQuery
from API_queries.tuition_API import tuitionQuery
from createChart import createChart

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

    earnings = earningsQuery(college_name, college_major)
    tuition = tuitionQuery(college_name, residence)
    print(f"Input received! Earnings is: {earnings}. Tuition is: {tuition}")


    #Make a bar graph of earnings and tuition
    createChart(tuition, earnings, college_name, college_major, residence)

    return render_template("chartDisplay.html")

@app.route('/schoolsList')
def schoolsList():
    return render_template("schoolList.html")

@app.route('/majorsList')
def majorsList():
    return render_template("majorList.html")

if __name__ == "__main__":
    app.run(debug=True)