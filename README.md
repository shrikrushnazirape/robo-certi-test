# robo-certi-test

## To create Docker Image 
Run 

docker build -t <name_of_image> .

## To create Docker Container
Run

docker run --name <name_of_container> -p <host_port>:8000 Docker image tag/name for above build

## Check on localhost:<host_port> to see the app 
