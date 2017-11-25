# Must import LightCtrl
from app import app


@app.route('/api/strip')
def test():
    return "Test"
