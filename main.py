# import secretskeys
# import requests
# from flask import Flask, request, jsonify, render_template, redirect, url_for

# api_key = secretskeys.API_KEY
# app = Flask(__name__)

#name = "Ringo Pan"
#server = "Midgardsormr"
# #Make a request to retrieve char data
#character_id=40117682
# #Parse the JSON Response
# #data = json.loads(response.text)
# #data = response.json()

# #print(f"Character ID for {name} on {server} is {character_id}")
# @app.route('/', methods=['GET','POST'])
# def get_character():
#     if request.method == 'POST':
#         name = request.form['name']
#         server = request.form['server']
#         response = requests.get(f"https://xivapi.com/character/search?name={name}&server={server}&private_key={api_key}")
#         data = response.json()
#         if response.status_code == 200 and data['Pagination']['Results'] > 0:
#             character_id = data['Results'][0]['ID']
#             return redirect(url_for('character_profile', character_id=character_id))
#     return render_template('index.html')

#     #     # use the character id to get the character data
#     #     url = f'https://xivapi.com/character/{character_id}?private_key={api_key}'
#     #     response = requests.get(url)
#     #     data = response.json()
#     #     class_jobs = []
#     #     jobs = data['Character']['ClassJobs']
#     #     for job in data['Character']['ClassJobs']:
#     #         class_jobs.append(job['Name'])
#     #         print(job)
#     #     # return the character data as JSON
#     #     return jsonify(response.json())
#     # else:
#     #      # return an error message
#     #      return jsonify({'error': 'Failed to retrieve character data'})
#     # return 'Hello, ' + name + '! You play on the ' + server + ' server.'
 

# if __name__ == '__main__':
#     app.run()

import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for

load_dotenv()
API_KEY = os.getenv('API_KEY')
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_character():
    if request.method == 'POST':
        name = request.form['name']
        server = request.form['server']
        response = requests.get(f"https://xivapi.com/character/search?name={name}&server={server}&private_key={API_KEY}")
        #response = requests.get(f"https://xivapi.com/character/search?name=Ringo+Pan&server=Midgardsormr")
        data = response.json()
        print(data)
        if response.status_code == 200 and data['Pagination']['Results'] > 0:
            character_id = data['Results'][0]['ID']
            return redirect(url_for('character_profile', character_id=character_id))
    return render_template('index.html')


@app.route('/profile/<int:character_id>')
def character_profile(character_id):
    url = f'https://xivapi.com/character/{character_id}?private_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)
    character_name = data['Character']['Name']
    server = data['Character']['Server']
    return render_template('profile.html', character_name=character_name, server=server, character_id=character_id)

if __name__ == '__main__':
    #currently runs on localhost | change it later??
    app.run(host='0.0.0.0')