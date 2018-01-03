#!flask/bin/python
from app import app
# to debug locally:
#app.run()
app.run(host="0.0.0.0", port=8080)
