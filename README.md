# simple-server-client-application
<img width="483" alt="Screenshot 2021-01-07 at 5 06 10 AM" src="https://user-images.githubusercontent.com/25201552/103833139-3b9efb00-50a6-11eb-90c0-eb9abe553dd5.png">

This application can be mainly divided into 2 parts -
## Client Side
Client which requests the server.</br>
I have created this application using `socket programming in python`. A socket is one endpoint of a two way communication link between two programs running on the network.
So the socket programming steps followed on the client side are - </br>
* Creating the socket with `s=socket.socket()`
* Connection to the server `s.connect((host,port))`
* Sending and receiving the data to and from the server `s.recv() & s.send()` </br>
In this application a service on the client side is continously monitoring SSH logins. SSH related logs are stored in `/var/log/auth.log`. So the client service is monitoring or
fetching these logs and sending them to the server. To run client service run `python3 client.py`. </br>
Or there is one more way i.e `Docker Container`. In the client folder, there is a Dockerfile along with the python script. Either build the image with the help of given Dockerfile 
`docker build . -t name_of_image` or
pull the image from docker hub. </br>
Just run the command to download the image `docker pull amanpreet9391/client-side:latest` and then to run the container `docker run --name client amanpreet9391/client-side`

## Server Side
Server serves the requests of the clients. </br>
The socket programming steps followed on the server side are as follows -
* Creating the socket
* Socket binding and listening to the new connections
* If gets a connection request from client, accepting that request.
* Server is designed in such a way that it can establish connections with multiple clients.
* By `list` command one can see all the clients which are successfully connected to the server.
* By `select id`client can be selected whose metrics we want to see.
* Multi threading is being used in this program so that server can connect to multiple clients.
* To run server service run `python3 server.py` </br>
Or to run docker container either build the image or pull from docker hub. </br>
Run command `docker pull amanpreet9391/server-side:latest` followed by `docker run -p 12345:12345 --name client amanpreet9391/server-side`

## Deployment
There are 3 ways through which one can create their instances as client or server. </br>
(1) Running the python scripts `server.py` and `client.py` </br>
(2) Running the above mentioned docker commands which will spin up client or server containers. </br>
(3) Ansible Playbook</br>
If one wants to configure their client or server machines from scratch, this is the best option. This given playbook will install docker, python etc and then will run client
or server docker container, according to the requirement. 

