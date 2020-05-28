import base64
from flask import request
from flask import Flask
import os
import face_recognition
import struct
import redis
import gc
import numpy as np

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)
names = r.keys()


def fromRedis(r, key):
    # r for redis
    encoded = r.get(key)
    array = np.frombuffer(encoded)
    del encoded
    gc.collect()
    return array


def compare(unknown_face_encodings, known_face_encoding):
    match_results = face_recognition.compare_faces(
        [known_face_encoding], unknown_face_encodings)
    print(match_results)
    if match_results[0]:
        return True
    else:
        return False


@app.route("/photo", methods=['POST'])
# define router
def get_frame():
    try:
        pic = request.files['pic']
    except:
        return 'image not uploaded'
    try:
        image = face_recognition.load_image_file(pic)
    except:
        return 'image format error'
    unknown_face_encodings = face_recognition.face_encodings(image)
    print(unknown_face_encodings[0])
    if len(unknown_face_encodings[0]) > 0:
        pass
    else:
        return 'no face in image!'
    print(names)
    Matched = False
    Matched_Name = ''
    for key in names:
        temp_face_data = fromRedis(r, key).tolist()
        print((key))
        match_results = face_recognition.compare_faces(
            [temp_face_data], unknown_face_encodings[0])
        # print(match_results)
        if match_results[0]:
            Matched = True
            Matched_Name = key
        else:
            pass
    if Matched:
        return 'People Matched ! You are ' + Matched_Name.decode() + '!'
    else:
        return 'No One Matched'


if __name__ == "__main__":
    app.run()
