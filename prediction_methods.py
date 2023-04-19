import cv2
import urllib.request
import numpy as np

import json
from flask import request
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_image():
    source = request.args.get('src')
    print(source)

    # with urllib.request.urlopen(source) as url:
    #     arr = np.asarray(bytearray(url.read()), dtype=np.uint8)
    #     img = cv2.imdecode(arr, -1)  # 'Load it as it is'
    #
    # cv2.imshow('lalala', img)
    # if cv2.waitKey() & 0xff == 27: quit()

    return "OK"


# source_url = 'https://x5t6u6x4.rocketcdn.me/wp-content/uploads/2022/02/image-1.png.webp'
# get_image(source_url)

if __name__ == '__main__':
    app.run(port=5000)
