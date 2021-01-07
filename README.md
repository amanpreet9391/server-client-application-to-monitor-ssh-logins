# simple-server-client-application
<img width="483" alt="Screenshot 2021-01-07 at 5 06 10 AM" src="https://user-images.githubusercontent.com/25201552/103833139-3b9efb00-50a6-11eb-90c0-eb9abe553dd5.png">

This application can be mainly divided into 2 parts -
## Client Side
Client which requests the server.</br>
This application is being created using `socket programming in python`. A socket is one endpoint of a two way communication link between two programs running on the network.
The socket programming steps followed on the client side are - </br>
* Creating the socket with `s=socket.socket()`
* Connecting to the server `s.connect((host,port))`
* Sending and receiving the data to and from the server `s.recv() & s.send()` </br>
In this application a service on the client side is continously monitoring SSH logins. SSH related logs are stored in `/var/log/auth.log`. So the client service is monitoring or
fetching these logs and sending them to the server. Run this command to run the client service --> `python3 client.py`. </br>
Or there is one more way i.e using `Docker Container`. In the client folder, there is a Dockerfile along with the python script. Either build the image with the help of given Dockerfile 
`docker build . -t name_of_image` or
pull the image from docker hub. </br>
Just run this command to download the image `docker pull amanpreet9391/client-side:latest` and then to run the container `docker run --name client amanpreet9391/client-side`

## Server Side
Server serves the requests of the clients. </br>
The socket programming steps followed on the server side are as follows -
* Creating the socket `s=socket.socket()`
* Socket binding and listening to the new connections `s.bind((host,port))`,`s.listen(5)`
* If it gets a connection request from client, accepting the request. `session,address =  s.accept()`
* Server is designed in such a way that it can establish connections with multiple clients.
</br>
<img width="1232" alt="Screenshot 2021-01-07 at 5 56 29 AM" src="https://user-images.githubusercontent.com/25201552/103835832-49a44a00-50ad-11eb-8637-6b99eef9e5c6.png">
</br>

* By `list` command one can see all the clients which are successfully connected to the server.
</br>

<img width="1424" alt="Screenshot 2021-01-07 at 5 56 43 AM" src="https://user-images.githubusercontent.com/25201552/103835866-604aa100-50ad-11eb-8a69-a315e27a70fd.png">
</br>

* By `select id`client can be selected whose metrics we want to see.
</br>
<img width="1436" alt="Screenshot 2021-01-07 at 5 57 06 AM" src="https://user-images.githubusercontent.com/25201552/103835883-70fb1700-50ad-11eb-83d9-b26b869a0c01.png">
</br>

* Multi threading is being used in this program so that server can connect to multiple clients.
* To run server service run `python3 server.py` </br>
Or to run docker container either build the image or pull from docker hub. </br>
Run command `docker pull amanpreet9391/server-side:latest` followed by `docker run -p 12345:12345 --name client amanpreet9391/server-side`

## Deployment
There are 3 ways through which one can configure their instances as client or server. </br>
(1) Running the python scripts `server.py` and `client.py` </br>
(2) Running the above mentioned docker commands which will spin up client or server containers. </br>
(3) Ansible Playbook</br>
If one wants to configure their client or server machines from scratch, this is the best option. The given playbook will install docker, python etc and then will run client
or server docker container, according to the requirement. 

