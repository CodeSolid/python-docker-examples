.PHONY: build run connect kill


build:
	docker build -t python-cpp:latest .

run:
	docker run --name python-cpp --rm -d python-cpp:latest

connect:
	docker run -it python-cpp /bin/bash

kill:
	docker kill python-cpp
