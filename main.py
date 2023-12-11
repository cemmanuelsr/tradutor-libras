import base64
import cv2
from flask_socketio import SocketIO, emit

from app import app
from utils.opencv_transformations import *

socketio = SocketIO(app, async_mode="eventlet")


@socketio.on("connect")
def test_connect():
    print("Connected")
    emit("my response", {"data": "Connected"})


@socketio.on("image")
def receive_image(image):
    image = base64_to_image(image)
    gray = hand_sign_recognition(image)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    frame_resized = cv2.resize(gray, (640, 360))
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    _, frame_encoded = cv2.imencode(".jpg", frame_resized, encode_param)
    processed_img_data = base64.b64encode(frame_encoded).decode()
    b64_src = "data:image/jpg;base64,"
    processed_img_data = b64_src + processed_img_data
    
    emit("processed_image", processed_img_data)


if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000, host='0.0.0.0')
