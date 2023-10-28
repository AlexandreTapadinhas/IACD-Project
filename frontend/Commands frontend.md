# Commands for the frontend container

docker run -d --name=frontend_cont -p 3000:3000 -v frontend_vol:/front_end_vol frontend

## To run containerized I had to change the port of the backend server to port 40, since my computer had port 80 being used by another service

In the frontend source code, change address from "localhost" to "localhost:40"