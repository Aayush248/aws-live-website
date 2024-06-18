from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection details
db_config = {
    'user': 'admin',
    'password': 'admin12345',
    'host': 'my-db-test.crezjbu8x9vl.us-east-1.rds.amazonaws.com',
    'database': 'company'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    hire_date = request.form['hire_date']
    job_title = request.form['job_title']
    salary = request.form['salary']

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert the data into the employee table
    cursor.execute('''
        INSERT INTO employee (first_name, last_name, email, hire_date, job_title, salary)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (first_name, last_name, email, hire_date, job_title, salary))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
