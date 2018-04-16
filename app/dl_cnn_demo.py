import os
import sys
import urllib
import urllib.request
import urllib.parse
import ssl
import requests
import time
import json
from flask import request,Response,Flask,render_template
from PIL import Image
app = Flask(__name__)
current_milli_time = lambda: int(round(time.time() * 1000))
@app.route('/')
def index():
    """ index """
    return render_template("index.html")

@app.route('/getImage', methods=['POST'])
def get_image():
    image_url = request.values.get('url', 0)
    """ get image,use urllib """
    res = download_image(image_url)
    orginal_path = res[0] + res[1]
    """ handle the image """
    processed_path = get_result(res[0],res[1])
    """  return the status code and image url """
    return Response(json.dumps({
      'status':200,
      'orginal_path':orginal_path.replace('./app',''),
      'processed_path':processed_path.replace('./app','')
    }), mimetype='application/json')

def get_result(path,ext):
    """ get result of input image """
    processed_path = path + '_processed_' + ext

    """ 下面是处理过程，保存路径为processed_path即可 """
    original_image = Image.open(path + ext)
    processed_image = original_image.convert('L')
    with open(processed_path, 'w') as f:
        processed_image.save(processed_path)
    return processed_path

def download_image(url):
    r = requests.get(url,stream=True)
    file_ext = urllib.parse.unquote(url).split('/')[-1]
    file_path = './app/static/images/' + str(current_milli_time()) + '__'
    with open(file_path + file_ext, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    return file_path,file_ext
if __name__ == "__main__":
    app.run()

