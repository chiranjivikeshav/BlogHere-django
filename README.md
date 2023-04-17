# Blog here
# website link :-https://ckeshav.pythonanywhere.com/
# Setup
The first thing to do is to clone the repository:<br>
$ git clone https://github.com/chiranjivikeshav/BlogHere-django.git<br>
$ cd blog<br>
# Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env<br>
$ source env/bin/activate<br>
# Then install the dependencies:<br>

(env)$ pip install -r requirements.txt<br>
### Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.<br>

Once pip has finished downloading the dependencies:<br>

(env)$ cd project<br>
(env)$ python manage.py runserver<br>
# navigate to http://127.0.0.1:8000.<br>
