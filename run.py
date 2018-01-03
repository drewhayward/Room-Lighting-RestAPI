#!flask/bin/python
from app import app
# TODO Turn off debug when testing with real Serial
app.run(debug=True)
