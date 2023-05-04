import secrets
import requests
from flask import Flask, request, jsonify, render_template

api_key = secrets.API_KEY
app = Flask(__name__)

name = "Ringo Pan"
server = "Cerberus"
#Make a request to retrieve char data
#40117682
#Parse the JSON Response
#data = json.loads(response.text)
#data = response.json()

#print(f"Character ID for {name} on {server} is {character_id}")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_character():
    name = request.form['name']
    server = request.form['server']
    response = requests.get(f"https://xivapi.com/character/search?name={name}&server={server}&private_key={api_key}")
    data = response.json()
    # check if the request was successful
    if response.status_code == 200 and data['Pagination']['Results'] > 0:
        # extract the character id from the response data
        character_id = data['Results'][0]['ID']

        # use the character id to get the character data
        url = f'https://xivapi.com/character/{character_id}?private_key={api_key}'
        response = requests.get(url)
        data = response.json()
        class_jobs = []
        jobs = data['Character']['ClassJobs']
        for job in data['Character']['ClassJobs']:
            class_jobs.append(job['Name'])
            print(job)
        # return the character data as JSON
        return jsonify(response.json())
    else:
         # return an error message
         return jsonify({'error': 'Failed to retrieve character data'})
    return 'Hello, ' + name + '! You play on the ' + server + ' server.'

@app.route('/<char_id>')
def character_profile(char_id):
    url = f'https://xivapi.com/character/{char_id}?private_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template('character.html', data=data)
    else:
        return f'Error: {response.status_code}'
    

if __name__ == '__main__':
    app.run()