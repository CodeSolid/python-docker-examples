# Docker Python Examples

## 1. A simple Flask Server in a container.

See the article section, Running Python Flask in a Docker Container.

Usage:

```
```


## Other Docker commands

```

docker run -it python:3.10.4-alpine3.15 /sh
docker run -it python:3.10.4-slim-buster /bin/bash
docker build -t flask-example:latest .
docker build -f Dockerfile.alpine -t flask-example:latest .
docker run -it python:3.10.4-slim-buster /bin/bash

docker run -d -p 80:8080 flask-example:latest

docker run -d -p 80:8080 --name flask flask-example:latest
```
