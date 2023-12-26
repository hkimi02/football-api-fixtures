from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = 'https://api.football-data.org/v2'
API_KEY = 'e8a8543277f74feb9bd02db503fd8315'  # Replace with your actual API key
headers = {'X-Auth-Token': API_KEY}

@app.route('/get_fixtures', methods=['GET'])
def get_fixtures():
    league_id = request.args.get('league_id')
    url = f'{BASE_URL}/competitions/{league_id}/matches'
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        fixtures = data['matches']
        return jsonify({'fixtures': fixtures})
    else:
        return jsonify({'error': f"Failed to fetch data. Status code: {response.status_code}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
