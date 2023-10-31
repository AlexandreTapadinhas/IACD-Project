Project cmds

# Push images to docker hub

docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname

# Docker build 
docker build . # with Dockerfile
docker build 

# Run container with volume

docker run [-p container_port:host_port] [-v volume_name:path_to_local_volume] image_name


# Network for communication for MongoDB and Backend 
## Create network
docker network create my-bridge-network

# Assignment 3
## To build and run everything
docker compose up

## To delete everything
docker compose down


# kubernets

kubectl get pod

## Create kubernets pod on terminal

kubectl create deployment [name] --image=username/image_id

## deployment.yaml file

config file for kubernet pod

## Deploy do pod deployment e service
kubectl apply -f=deployment.yaml

kubectl apply -f=service.yaml


# Service types on kubernetes

## Service of ClusterIP type
Used for inside the Cluster Communication

## Service of LoadBalancer or NodePort type
For being accessible to outside of the Cluster

# Auto generated environment variable
## [service_name]_SERVICE_HOST

## Types of services for the project

Service of Mongodb pod is ClusterIP type

Service of Backend pod is LoadBalancer type (because it is accessed by the client browser)

Service of Frontend pod is LoadBalancer type
