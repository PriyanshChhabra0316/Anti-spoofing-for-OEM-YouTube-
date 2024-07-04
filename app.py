from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('services.html')

@app.route('/run_python_program')
def run_python_program():
    try:
        
        result = subprocess.check_output(['python', 'WebPage/sample.py'], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

if __name__ == '__main__':
    app.run(debug=True)
