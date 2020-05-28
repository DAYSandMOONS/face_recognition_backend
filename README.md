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
(Ignore the water print plz)
# About License
MIT License

Copyright (c) 2020 Nothing.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.