from flask import Flask, render_template, request, abort, make_response, Response, jsonify
from util import file_reader

import config

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


def get_start_end_dates():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if start_date is None or start_date == '':
        # Is smaller than any number char
        start_date = '0'
    if end_date is None or end_date == '':
        # Is larger than any number char
        end_date = 'INF'
    if start_date > end_date:
        # TODO normal aborts
        abort(400)
        abort(Response('Start date should be less or equal end date'))
    return start_date, end_date


@app.route('/process/', methods=['GET'])
def process_data():
    start_date, end_date = get_start_end_dates()
    format = request.args.get('format')
    # TODO choose file depending on Google/iOS
    format_getter = None
    # start_date = request.form('start_date')
    # end_date = request.form('end-date')
    # TODO format in header?
    if format == 'CSV':
        format_getter = file_reader.get_csv
    elif format == 'JSON':
        format_getter = file_reader.get_json
    else:
        abort(400, Response('No such format'))
    res = format_getter(start_date, end_date)
    output = make_response(res)
    if format == 'CSV':
        output.headers["Content-Disposition"] = "attachment; filename=reviews_" + \
                                                start_date + "_to_" + end_date + ".csv"
        output.headers["Content-type"] = "text/csv"
    elif format == 'JSON':
        # output.headers["Content-Disposition"] = "attachment; filename=export.csv"
        output.headers["Content-type"] = "application/json"
    return output


@app.route('/type-counts/', methods=['GET'])
def show_chart():
    start_date, end_date = get_start_end_dates()
    type_counts = file_reader.get_type_counts(start_date, end_date)
    return jsonify(type_counts)

if __name__ == '__main__':
    app.run(config.address, port=config.port, debug=config.debug)
