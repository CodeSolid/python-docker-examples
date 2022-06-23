.PHONY: build run connect browse kill

# Needs to be run once
makevol:
	docker volume create sage

build:
	docker build -t sage:latest .

# run:
# 	docker run --name flask --rm -d -p 80:8080 sage:latest

connect:
	docker run -it  -p 8888:8888 --mount source=sage,target=/app sage /bin/bash 

#
# kill:
# 	docker kill flask	
