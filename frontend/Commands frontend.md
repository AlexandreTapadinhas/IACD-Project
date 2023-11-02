# Commands for the frontend container

docker run -d --name=frontend_cont -p 3000:3000 -v frontend_vol:/front_end_vol frontend


In the frontend source code, change address from "localhost" to "localhost:40"