# ISS Tracker
# Kieran Hobden
# 05-Aug-18

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('Current Astronauts in Space: ', result['number'])
for i in result['people']:
    print(i['name'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon), float(lat))

# Space Centre, Houston
sclat = 29.5502
sclon = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(sclon, sclat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(sclat) + '&lon=' + str(sclon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

