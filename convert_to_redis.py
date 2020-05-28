import face_recognition
import os
import redis
import struct
import gc


def toRedis(r, key, array): 
    # r for redis
    # check whether array shape is 128
    if array.shape != (128,):
        raise Exception("Shape Error!")
    else:
        pass
    encoded = array.tobytes()
    r.set(key, encoded)
    # better than not
    del encoded, key, array
    gc.collect()
    return


# base setting
image_dir = './face_image'
face_names = os.listdir(image_dir)

# connet to redis
r = redis.Redis(host='localhost', port=6379, db=0)
# store into redis
for face_name in face_names:
    try:
        toRedis(r, face_name.split('.')[0], face_recognition.face_encodings(
            face_recognition.load_image_file(image_dir+'/'+face_name))[0])
    except:
        print('no face in %s' % face_name)
    del face_name
    gc.collect()

del face_names
gc.collect()

# print(face_data.keys())
# print(face_data['Cook'])
