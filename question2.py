from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

bookings = []

@app.route('/booking', methods=['GET','POST'])
def booking():
    if request.method == "POST":
        bookingCheck = False #checks if booking has been done before
        booking = request.get_json()
        for i,q in enumerate(bookings):
            if q['slot'] == booking['slot']:
                bookingCheck = True 
        if bookingCheck == False:
            bookings.append(booking)
            return jsonify({"status": "confirmed"})
        error_statement  = "slot full, unable to save booking for " + booking['name'] + " in slot " + str(booking['slot'])
        return jsonify({"status": error_statement})

    else:
        return jsonify(bookings)

@app.route('/cancel', methods=['POST'])
def cancel():
    cancel_request = request.get_json()
    for i,q in enumerate(bookings):
        if q['slot'] == cancel_request['slot'] and q['name'] == cancel_request['name']:
            bookings.pop(i) # pops given booking from bookings list
            cancel_statement = "canceled booking for " + cancel_request['name'] + " in slot " + str(cancel_request['slot'])
            return jsonify({"status": cancel_statement})
    error_statement = "no booking for " + cancel_request['name'] + " in slot " + str(cancel_request['slot'])
    return jsonify({"status": error_statement})

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
