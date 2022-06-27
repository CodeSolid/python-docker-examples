docker container run --rm -it \
    -p 8888:8888 \
    -u $(id -u ${USER}):$(id -g ${USER}) \
     -v $(pwd)/data:/data \
     sage /bin/bash
