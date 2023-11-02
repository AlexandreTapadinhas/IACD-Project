# Commands for the backend container

docker run -d --name=backend_cont -p 40:80 -v backend_vol:/backend_vol --network=mongo_backend_net backend

cmd inputs
docker run -d --name=<container-name> -p <host-port>:<container-port> -v <volume-name>:<volume-path> --network=<network-name> <image-name>

## To run containerized I had to change the port of the backend server to port 40, since my computer had port 80 being used by another service


## mongo db path to environment variable

  'mongodb://${process.env.DB_ADDRESS:27017}/course-goals',
