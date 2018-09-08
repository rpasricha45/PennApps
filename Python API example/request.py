import requests
response = requests.get('https://swapi.co/api/people/1').json() # first put in the link for the api, and also how  you want to view the data
name = response['name']
print(name)

# new request

binUrl = 'https://requestb.in/1083ut61'

p = requests.post(binUrl,data['name': 'nemo']






