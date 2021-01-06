FROM ubuntu:latest
RUN apt-get update 
RUN apt-get install python3 -y
COPY . /app
EXPOSE 12345
CMD python3 /app/client.py


##docker cp /var/log/auth.log client:/app/test