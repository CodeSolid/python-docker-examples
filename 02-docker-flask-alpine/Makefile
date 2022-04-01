.PHONY: build run connect browse kill

build:
	docker build -t flask-example:latest .

run:
	docker run --name flask --rm -d -p 80:8080 flask-example:latest

connect:
	docker run -it flask-example /bin/sh

browse:
	open http://localhost

kill:
	docker kill flask	
