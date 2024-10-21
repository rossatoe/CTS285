from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def query_db(query, args=(), one=False):
    conn = get_db_connection()
    cur = conn.execute(query, args)
    rv = [dict(row) for row in cur.fetchall()]
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer_checker', methods=['GET', 'POST'])
def answer_checker():
    result = ""
    if request.method == 'POST':
        try:
            user_input = request.form['equation']
            equation, user_answer = user_input.split('=')
            correct_answer = eval(equation)
            if correct_answer == int(correct_answer):
                correct_answer = int(correct_answer)
            if str(correct_answer) == user_answer.strip():
                result = f"Correct! The answer is {correct_answer}"
            else:
                result = f"Incorrect! The answer is {correct_answer}"
        except Exception as e:
            result = 'Error: ' + str(e)
    return render_template('answer_checker.html', result=result)

@app.route('/memory_bank', methods=['GET', 'POST'])
def memory_bank():
    if request.method == 'POST':
        equation = request.form['equation']
        if 'save' in request.form:
            conn = get_db_connection()
            conn.execute('INSERT INTO equations (equation) VALUES (?)', (equation,))
            conn.commit()
            conn.close()
        elif 'remove' in request.form:
            conn = get_db_connection()
            conn.execute('DELETE FROM equations WHERE equation = ?', (equation,))
            conn.commit()
            conn.close()
        return redirect(url_for('memory_bank'))
    
    equations = query_db('SELECT * FROM equations')
    return render_template('memory_bank.html', equations=equations)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback_text = request.form['feedback']
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (feedback) VALUES (?)', (feedback_text,))
        conn.commit()
        conn.close()
        return redirect(url_for('feedback'))
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
