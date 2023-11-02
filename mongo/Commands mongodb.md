# Run container mongo

docker run -d --name=mongodb_cont --network=mongo_backend_net mongo

# TODO: falta commmando sem network, só com port mapping