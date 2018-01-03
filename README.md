Rest API
===

#Installation

Use virtualenv to install Python 2 as /flask/

    python -m virtualenv flask

Then install pyserial, flask and flask-cors

    pip install flask pyserial flask-cors

#/api/ Endpoints

##/strip/
**Methods: POST**
The /strip/ endpoint changes the color of the strip. It accepts json data in the following format. Colors are set with RGB

    {
	    "color":"000000",
	    "strip":"bedStrip"
	}

##/light/
**Methods: POST**
The /light/ endpoint changes the state of the light given.

##/state/
