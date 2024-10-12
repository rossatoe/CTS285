from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer_checker')
def answer_checker():
    return render_template('answer_checker.html')

@app.route('/memory_bank', methods=['GET', 'POST'])
def memory_bank():
    if request.method == 'POST':
        # Save the equations to a database or file (we'll implement this later)
        pass
    return render_template('memory_bank.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Save the feedback to a database or file (we'll implement this later)
        pass
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run()
