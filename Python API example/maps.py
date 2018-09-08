import requests
key = 'AIzaSyCKxGvck0ftgmF46nLupByrChK_MS1Ur4o'
url = 'https://www.googleapis.com/geolocation/v1/geolocate?key='+key

data = requests.get(url)

print(data.status())


