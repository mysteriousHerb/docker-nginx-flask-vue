# use python container image
From python:3.6-stretch

# set the working directory of the image filesystem 
WORKDIR /backend

# copy current directory to the working directory 
ADD . /backend

# run the following command on host, if there is any libray changes
# pipenv run pip freeze > requirements.txt

# Install the python dependencies on container
RUN pip install -r requirements.txt

EXPOSE 8000

# start the uWSGI
CMD ["uwsgi", "app.ini"]
