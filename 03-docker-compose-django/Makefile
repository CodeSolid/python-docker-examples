.PHONY: build run connect connect_db browse kill up

up:
	docker compose --env-file ../secrets/secrets.txt up -d

down:
	docker compose down


run:
	docker run --name django --env-file ../secrets/secrets.txt  --rm django-example:latest

connect:
	docker compose run frontend /bin/bash	

connect_db:
	docker compose run backend /bin/bash

# CAUTION: This target will remove all your docker containers and images, 
# and the data directory.  Use with caution.
clean: 
	docker kill ```docker ps -q``` || true
	docker rm -f ```docker ps -a -q``` || true

	docker image prune -a -f || true
	docker image rm -f * || true
	rm -rf data
	
	



browse:	
	open http://localhost

kill:
	docker kill flask	
