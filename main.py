import secrets
import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for

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
@app.route('/', methods=['GET','POST'])
def get_character():
    if request.method == 'POST':
        name = request.form['name']
        server = request.form['server']
        response = requests.get(f"https://xivapi.com/character/search?name={name}&server={server}&private_key={api_key}")
        data = response.json()
        # check if the request was successful
        #if response.status_code == 200:
            # extract the character id from the response data
        character_id = data['Results'][0]['ID']
        print(character_id)
        return redirect(url_for('character_profile', character_id=character_id))
    return render_template('index.html')

    #     # use the character id to get the character data
    #     url = f'https://xivapi.com/character/{character_id}?private_key={api_key}'
    #     response = requests.get(url)
    #     data = response.json()
    #     class_jobs = []
    #     jobs = data['Character']['ClassJobs']
    #     for job in data['Character']['ClassJobs']:
    #         class_jobs.append(job['Name'])
    #         print(job)
    #     # return the character data as JSON
    #     return jsonify(response.json())
    # else:
    #      # return an error message
    #      return jsonify({'error': 'Failed to retrieve character data'})
    # return 'Hello, ' + name + '! You play on the ' + server + ' server.'
@app.route('/character')
@app.route('/character/<int:character_id>')
def character_profile(character_id):
    url = f'https://xivapi.com/character/{character_id}?private_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        character_name = data['Character']['Name']
        server = data['Character']['Server']
        return render_template('character.html', character_name=character_name, server=server, character_id=character_id)
    else:
        return f'Error: {response.status_code}'
    

if __name__ == '__main__':
    app.run()