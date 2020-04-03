FROM python:3.7-alpine
LABEL maintainer sohail21400

ENV PYTHONUNBUFFER 1

# this copies the requirements.txt file and save it inside the image with requirements.txt
COPY ./requirements.txt/ requiremenets.txt 
#
RUN pip install -r /requiremenets.txt

# we need a directory to save our application source code
RUN mkdir /app
# this is like cd
WORKDIR /app
# this copies our projects app folder and puts it inside the image file
COPY ./app /app

# we are creating a user named 'user'
# -D says creating user for running the app only.
# otherwise it will run in root account

# RUN chown user -R /app

# switching the user to 'user'

# USER user

# # Create Windows user in the container
# RUN net user /add user
# # Set it for subsequent commands
# USER user