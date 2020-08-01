from flask import Flask, render_template, request, jsonify

import config

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/process/', methods=['GET'])
def process_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    format = request.content_type

    # start_date = request.form('start_date')
    # end_date = request.form('end-date')
    if start_date is None or end_date is None:
        return "Please choose both dates"
    if start_date > end_date:
        return "Start date should be less or equal end date"

    return jsonify({"res": start_date + " " + end_date})


if __name__ == '__main__':
    app.run(config.address, port=config.port, debug=config.debug)
