import requests
'''
open weather project
'''

key = 'c4d51c0453758b3c64515ce293808319' # this is my api key

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=c4d51c0453758b3c64515ce293808319&q=' # url with the key 


cityName = input('enter in the city name ') #this is the city name 

url = api_adress +cityName # add the city name to the program
try:
    
   data = requests.get(url).json() # entire JSON data

   info = data['weather'][0]['main'] # getting the specfic data

   print(info)
except KeyError:
    print('Pleas enter in a valid city ')# do 7 week

def weekely ():
    import requests

    url = 'http://api.openweathermap.org/data/2.5/forecast?q='
    city = input('please enter in the city name :')
    countryCode = 'us&mode=xml'
    url = url + countryCode + city

    data = requests.get(url)
    print(data)



def url ():
    ''' this module is is an example for youtube api'''
    import json
    import requests
    data = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
    json = json.loads(data.text)
    print(json)
    
#url()



def other():
    import requests
    import json
    data = requests.get("http://espn.com")
    data = json.loads(data)
    print(data)

    







