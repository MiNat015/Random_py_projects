import requests

API_KEY = 'c09c0311325b2ffe5928449b3497f792'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

run = True

while run:

    city = input('Enter a city name: ')
    request_url = f'{BASE_URL}?q={city}&appid={API_KEY}'
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        main = data['main']
        temp = round(main['temp'] - 273.15, 2)
        print('Weather: ', weather)
        print('Temperature: ', temp, 'celsius')

    else:
        print('An error occurred')

    run_again = input('Would you like to run the program again? Y/n: ')
    if run_again != 'Y':
        run = False
