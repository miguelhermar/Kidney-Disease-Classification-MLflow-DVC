#it first downloads python interpreter
FROM python:3.8-slim-buster  

# updates every package manager and installs awscli (terminal) for the deployment in AWS
RUN apt update -y && apt install awscli -y
# creates one app directory
WORKDIR /app

# it copies all the code and puts it inside it
COPY . /app
# installs requirements
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]