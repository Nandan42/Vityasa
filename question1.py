from flask import Flask
from flask import jsonify
from flask import request
from statistics import mean


app = Flask(__name__)


@app.route('/items', methods=['POST'])
def addOne():
    numbers = [] # array to to get the JSON input, accepts input array. JSON request in the form ("items" : [1,"hello",....])
    output = [] # array to filter output
    invalid_instance = 0
    valid_instance = 0
    new_array = request.get_json() # JSON input
    for i in range(len(new_array['items'])):
        numbers.append(new_array['items'][i])
    for i in range(len(numbers)):
        if (isinstance(numbers[i], int) == False) or numbers[i] < 1 : # checks if list item is valid
            invalid_instance = invalid_instance + 1
        else:
            valid_instance  = valid_instance + 1
            output.append(numbers[i])
    return jsonify({'invalid_instance' : invalid_instance}, # returns operations done on the valid input
                    {'valid_instance' : valid_instance},
                    {'min': min(output)},
                    {'max': max(output)},
                    {'average': mean(output)})

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)