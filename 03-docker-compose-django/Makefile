.PHONY: build run connect browse kill up

up:
	docker compose --env-file ../secrets/secrets.txt up --force-recreate 

down:
	docker-compose down


build:
	docker build -t django-example:latest .

clean: 
	docker kill ```docker ps -q``` || true
	docker rm -f ```docker ps -a -q``` || true
	docker rm ```docker ps -a -q``` || true
	# docker image prune -a -f || true
	# docker image rm -f * || true
	rm -rf data
	
	
# -p 80:8080
run:
	docker run --name django --env-file ../secrets/secrets.txt  --rm django-example:latest

connect:
	docker compose run frontend /bin/bash
	# docker run -it --env-file ../secrets/secrets.txt --rm django-example /bin/bash

browse:
	# curl http://localhost
	open http://localhost

kill:
	docker kill flask	
