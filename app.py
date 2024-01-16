from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('options.json', 'r') as emigrate_file:
    emigrate_flowdata = json.load(emigrate_file)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/first_node')
def first_node():
    current_node = get_node_by_id("node1")
    return render_template('flowchart.html', node=current_node)

@app.route('/get_next_node', methods=['POST'])
def get_next_node():
    user_choice = request.form['choice']
    current_node = get_node_by_id(user_choice)
    if current_node['id'] == 'within_of_scope':
        return render_template('within_of_scope.html', node=current_node)
    elif current_node['id'] == 'out_of_scope':
        return render_template('out_of_scope.html', node=current_node)
    elif current_node['id'] == 'within_of_employ_scope':
        return render_template('qualified_subsidy.html', node=current_node)
    elif current_node['id'] == 'out_of_employ_scope':
        return render_template('out_of_employ_scope.html', node=current_node)
    elif current_node['id'] == 'within_of_found_scope':
        return render_template('qualified_subsidy.html', node=current_node)
    elif current_node['id'] == 'out_of_found_scope':
        return render_template('out_of_found_scope.html', node=current_node)
    return render_template('flowchart.html', node=current_node)

def get_node_by_id(node_id):
    for node in emigrate_flowdata['nodes']:
        if node['id'] == node_id:
            return node
    return None

@app.route('/employment_first')
def employment_first():
    current_node = get_node_by_id("node21")
    return render_template('flowchart.html', node=current_node)

@app.route('/foundation_first')
def foundation_first():
    current_node = get_node_by_id("node31")
    return render_template('flowchart.html', node=current_node)


@app.route('/foundation')
def foundation():
    return render_template('foundation_chart.html')



if __name__ == '__main__':
    app.run(debug=True)