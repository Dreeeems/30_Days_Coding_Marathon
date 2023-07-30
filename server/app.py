from flask import Flask, jsonify
from flask_cors import CORS
from fetch import get_movie_details

app = Flask(__name__)
CORS(app)

@app.route('/movie/<terms>', methods=["GET"])
def get_movie(terms):
    # Use the 'terms' parameter to do something related to the movie search
    # For example, return a response with the search results
    data = get_movie_details(terms)
    if data is not None:
        return jsonify(data)  # Automatically converts 'data' to a JSON response
    else:
        return jsonify({'error': 'Error fetching movie details'}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'key1': 'value1',
        'key2': 'value2',
    }
    return jsonify(data)  # Automatically converts 'data' to a JSON response

if __name__ == '__main__':
    app.run(debug=True)
