from flask import Flask

# Sets a flask instance equal to 'app'
app = Flask(__name__)

jinja_options = app.jinja_options.copy()

jinja_options.update(dict(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='%%',
    variable_end_string='%%',
    comment_start_string='<#',
    comment_end_string='#>'
))
app.jinja_options = jinja_options



# Imports 'views' from a package 'app'
from app import views

# Import the RESTapi functionality
from app import restapi
