from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from datetime import datetime
import json
from quotefunction import prepare_sentiment_quote_stash, gimme_a_quote

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})



@app.route('/')
def hello():
    utc_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', utc_time=utc_time)

@app.route('/quotes')
# @cross_origin(origins=['http://localhost:5173'])
def all_quotes():
    quote_path = 'quotes.csv'
    quotes = prepare_sentiment_quote_stash(quote_path)
    return quotes


@app.route('/quotes', methods=['POST'])
# @cross_origin(origins=['http://localhost:5173'])
def get_quote():
    data = request.get_json()
    direction = data.get('direction')
    current_index = data.get('current_index')
    quote_id = gimme_a_quote(direction, current_index)
    print('this is the quote id', quote_id)
    return str(quote_id)

if __name__ == '__main__':
    app.run(debug=True)