.PHONY: build run clean_images connect_db

echo:
	echo $(PWD)
run:
	docker run --env-file ../../private/secrets.txt \
		--mount 'type=volume,src=pgdata,target=/var/lib/postgresql/data/pgdata' \
		--name postgres  \
		--rm -d \
		-p 5432:5432 \
		postgres:latest 


build:
	docker build . -t postgres:latest 

connect:
	docker-compose run  client /bin/bash

connect_db:
	docker-compose run  backend /bin/bash

# Caution, cleans all images, including non-related
clean_images:
	$(shell docker rmi `docker images -a -q` --force)

