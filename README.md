# Project Information
This is a project using face_recognition package to identify people by photo.(No front end so far)
## Involved Component
* flask
* redis
* face_recognition package
## How to deploy (Linux/WSL Only)
1. Install Dlib
    - u will need to install gcc g++ cmake build-essential
2. Install face_recognition
    - through pip to install
3. Install other packages
    - the requirements.txt has given other packages used install this project, just install them by 'pip install -r requirements.txt'
## More about the detail
* convert_to_redis.py is used to convert all given people image to numpy array, and store in redis
* reach_back.py shows how those data should been taken back
* app.py is a flask application, provide a web server to recive images from the front end
## About the front end
![咕咕咕](https://p.pstatp.com/origin/ffca0000da8fe40c246c)

Above is a famous Chinese Meme meaning something will (definitely not) come.