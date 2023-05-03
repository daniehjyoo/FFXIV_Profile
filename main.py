import secrets
import requests, json

api_key = secrets.API_KEY


name = "Ringo Pan"
server = "Cerberus"
#Make a request to retrieve char data
response = requests.get(f"https://xivapi.com/character/search?name={name}&server={server}")
#40117682
#Parse the JSON Response
#data = json.loads(response.text)
data = response.json()

#print(f"Character ID for {name} on {server} is {character_id}")


# check if the request was successful
if response.status_code == 200:
    # extract the character id from the response data
    character_id = response.json()['Results'][0]['ID']

    # use the character id to get the character data
    url = f'https://xivapi.com/character/{character_id}'
    response = requests.get(url)

    print(response.json())
else:
    print('Error:', response.status_code)

