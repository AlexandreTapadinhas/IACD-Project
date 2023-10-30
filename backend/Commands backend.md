# Commands for the backend container

docker run -d --name=backend_cont -p 40:80 -v backend_vol:/backend_vol --network=mongo_backend_net backend




## mongo db path to environment variable

  'mongodb://${process.env.DB_ADDRESS:27017}/course-goals',
