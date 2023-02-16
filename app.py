import base64
import io
import numpy as np
from flask import Flask
from flask import request
from PIL import Image
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(message)s') 

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    image_np = request_to_img_array(request)
    logger.info(image_np.size)
    return {'result': 'ok'}


def request_to_img_array(request):
    json_data = request.get_json()
    image_bytes = json_data['image_bytes']
    base64_decoded = base64.b64decode(image_bytes)
    image = Image.open(io.BytesIO(base64_decoded))
    return np.array(image)

if __name__ == "__main__":
    logger.info("Starting IWF starter...")
    app.run(host="0.0.0.0")
