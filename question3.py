from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

coordinates = []

@app.route('/plot', methods=['POST'])
def plot():
    coordinate_point = request.get_json()
    coordinate_point_arr = [coordinate_point['x'],coordinate_point['y']]
    coordinates.append(coordinate_point_arr)
    if len(coordinates) >= 4:
        x = check_square(coordinates)
        if x is False:
            return jsonify({"status":"accepted"})
        else:
            success_statement = "Success " + str(x)
            return jsonify({"status": success_statement})       
    return jsonify({"status":"accepted"})

def square(a, b, c, d):
        #sort points so they can easily be compared
        points = sorted([a, b, c, d])
        w = abs(points[0][0] - points[1][0])
        x = abs(points[0][1] - points[2][1])
        y = abs(points[2][0] - points[3][0])
        z = abs(points[1][1] - points[3][1])
        #check if lenghts are equal
        if w == x and x == y and y == z and z == w:
            #check if corners line up
            if points[0][0] == points[1][0] and\
                points[0][1] == points[2][1] and\
                points[2][0] == points[3][0] and\
                points[1][1] == points[3][1]:
                    return True
        return False

#loop over all sets of 4 points
def check_square(lst_points):
    for i in range(len(lst_points)):
        for j in range(i+1, len(lst_points)):
                for k in range(j+1, len(lst_points)):
                        for l in range(k+1, len(lst_points)):
                              #check if square   
                              if square(lst_points[i],
                                             lst_points[j],
                                             lst_points[k],
                                             lst_points[l]):
                                        return [lst_points[i], lst_points[j], lst_points[k], lst_points[l]]
    return False

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)