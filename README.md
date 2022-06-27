# Using Docker With Python: Companion Source

This is the companion source for the article [How To Use Docker With Python](https://codesolid.com/how-to-use-docker-with-python/).  The article goes into the source and what's available in more depth, but if you have Gnu make, you can follow these steps:

## Part 1. A Simple Flask Server in a Container.

Source:  01-docker-flask

Usage:

See the commands in the article, or use the Makefile

```
cd 01-docker-flask
make build
make run
make browse
```
## Bonus, Alpine example:

Source: 02-docker-flask-alpine

Usage:

```
cd 02-docker-flask-alpine
make build
make run
make browse
```

## Docker-Compose Example With Django and flask:

Source: 03-docker-compose-django

Usage:

```
cd 03-docker-compose-django
make up
# Wait for stack (esp Postgres) to come up, about 25 seconds
make browse
```

See the article for more details on the commands that are available or running without Gnu make.

## Running SageMath in a Container:

For more on this source, see the article [Python Docker Examples: SageMath in a Container](https://codesolid.com/python-docker-examples-sagemath-in-a-container/).

Source: 04-docker-sagemath

Usage:

```
cd 04-docker-sagemath
# Building 
./build.sh
# Running the container
./run.sh
# Inside the container, use ./run_lab.sh to launch Jupyter Lab with Sage enabled.
```




