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

## To remove all the containers and networks created
docker compose down

# Assignment #4

## Start minikube

minikube start

## Stop
minikube stop


## Create kubernets deployment objects

kubectl create deployment mongo-pod --image=mongo --port=27017

kubectl create deployment backend-pod --image=tapadinhas/iacd-backend:Assignment3-no-env-var --port=80 --replicas=2

kubectl create deployment frontend-pod --image=tapadinhas/iacd-frontend:Assignment1-and-2 --port=3000 --replicas=3

## To delete any type of kubernets object

kubectl delete <object-type> <object-name>

## To expose the pods

kubectl expose deployment mongo-pod --type=ClusterIP --port=27017
kubectl expose deployment backend-pod --type=LoadBalancer --port=80
kubectl expose deployment frontend-pod --type=LoadBalancer --port=3000

## To apply the configurations files for the deployment and services

kubectl apply -f=<config.yaml>




# To get the public address to access the service

minikube service frontend-service
minikube service backend-service





# Kubernets - Notes from class

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

