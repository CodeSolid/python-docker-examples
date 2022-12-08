.PHONY: build up connect clean_images

up:
	docker compose up -d 


build:
	docker build . -f Dockerfile.client \
		-t demo_client:latest 

connect:
	docker-compose run  client /bin/bash

connect_db:
	docker-compose run  backend /bin/bash

# Caution, cleans all images, including non-related
clean_images:
	$(shell docker rmi `docker images -a -q` --force)

