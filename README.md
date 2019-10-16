# docker-project-template

This is a simple Docker template used to quickly create a new dockerized application.

This example creates an example Python web application (using Flask), and a Redis cache service.

## Prerequisites

* Docker
* Docker Compose (optional)

The following commands describe how to install these prerequisites under Ubuntu.

Install Docker:
```sh
$ apt-get update && apt-get install -y docker.io
$ update-rc.d docker defaults

# usermod change requires new shell
$ usermod -aG docker vagrant
```

Install Docker Compose (assumes Python and PIP are already installed):
```sh
$ pip install docker-compose
```

## Docker Usage

If using Docker Compose, skip to that section.  Docker Compose simplifies the process and creates many resources (images, containers, networks, volumes, etc) through Docker for you.

Build the image:
```sh
$ cd /path/to/docker-project-template/app
$ docker build --tag app:latest .
```

Start the containers (and networks and volumes):
```sh
$ docker network create app-network

$ docker volume create --name redis-data
$ docker run -d --name redis --network app-network -v redis-data:/data redis:alpine

$ docker run -d --name app --network app-network --mount type=bind,source=${PWD}/app.py,target=/app/app.py -p 5000:5000 -e FLASK_DEBUG=1 app:latest
```

Access the containers:
```sh
$ docker ps | grep app
$ docker exec -it <container id> /bin/sh
```

View the logs:
```sh
$ docker ps | grep app
$ docker logs <container id>
```

Monitor the container stats:
```sh
$ docker stats
```

Stop the containers (and remove containers, networks, and volumes):
```sh
$ docker ps | grep app
$ docker stop <container id>

$ docker ps | grep redis
$ docker stop <container id>

$ docker ps | grep app
$ docker rm <container id>

$ docker ps | grep redis
$ docker rm <container id>

$ docker network prune
$ docker volume prune
```

## Docker Compose Usage

Build and start the containers (and networks and volumes):
```sh
$ cd /path/to/docker-project-template
$ docker-compose up -d
```

Re-build and deploy changes to the images/containers:
```sh
$ docker-compose up --build --force-recreate -d
```

Access the containers:
```sh
$ docker-compose exec app /bin/sh
```

View the logs:
```sh
$ docker-compose logs app
```

Stop the containers (and remove containers, networks, and volumes):
```sh
$ docker-compose down --volumes
```

## Access the Web Application

The web application can be accessed from your host (localhost or the IP of the VM it is running in):
```
http://localhost:5000/
http://localhost:5000/count
```

The root API serves static content, while the count API returns a cached value from Redis.  Any changes to the `app.py` file will be immediately reflected in the container as the file is bind mounted.

## Further Modifications

It is expected that the example applications and services in this project template would be updated or replaced with the desired applications and services.  Additional applications or services can be added under their own directory and included in the `docker-compose.yaml` file.

Environment-specific Docker settings can be put in an `.env` file, and environment-specific Docker Compose overrides can be put in a `docker-compose.overrides.yaml` file.

Use the Docker Compose `scale` option (during `docker-compose up` or as a standalone command) to scale the number of nodes for a given application or service.  An load balancer can then be placed in front of the given application or service.

## License

Copyright (c) 2019 Jeremy Parr-Pearson

The MIT License (MIT)
