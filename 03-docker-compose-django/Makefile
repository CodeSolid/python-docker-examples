.PHONY: build run connect connect_db browse kill up

up:
	docker compose --env-file ../secrets/secrets.txt up --force-recreate 

down:
	docker-compose down

build:
	docker build -t django-example:latest .

run:
	docker run --name django --env-file ../secrets/secrets.txt  --rm django-example:latest

connect:
	docker compose run frontend /bin/bash	

# CAUTION: This target will remove all your docker containers and images, 
# and the data directory.  Use with caution.
clean: 
	docker kill ```docker ps -q``` || true
	docker rm -f ```docker ps -a -q``` || true
	docker rm ```docker ps -a -q``` || true
	docker image prune -a -f || true
	docker image rm -f * || true
	rm -rf data
	
	


connect_db:
	docker compose run backend /bin/sh

browse:	
	open http://localhost

kill:
	docker kill flask	
