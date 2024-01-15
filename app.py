from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('options.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def index():
    current_node = data['start']
    return render_template('index.html', current_node = current_node )

@app.route('/get_next_node', methods=['POST'])
def get_next_node():
    user_choice = request.form['choice']
    return render_template('flowchart.html', user_choice=user_choice)

if __name__ == '__main__':
    app.run(debug=True)