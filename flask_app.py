#!/usr/bin/python3

from flask import Flask
from string import Template

app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello ${name}!</h1>
<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")

@app.route('/')
def homepage():
    return"""<h1>Hello World!</h1>"""

@app.route('/<place>')
def place_page(place):
    return(HTML_TEMPLATE.substitute(place_name=place))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
