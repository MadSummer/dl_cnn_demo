import os
import sys
import urllib
import urllib.request
import ssl
import flask



app = flask.Flask(__name__)

@app.route('/demo')
def phone_loc():
    """get phone_loc"""

    return flask.render_template("index.html")


def get_result(img):
    """get result of input image"""
    return None



if __name__ == "__main__":
    app.run()

