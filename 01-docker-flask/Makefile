.PHONY: build run connect browse

build:
	docker build -t flask-example:latest .

run:
	docker run -d -p 80:8080 flask-example:latest

connect:
	docker run -it flask-example /bin/bash

browse:
	# curl http://localhost
	open http://localhost
