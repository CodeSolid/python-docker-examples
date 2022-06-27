docker container run --rm -it \
    -p 8888:8888 \
    -u $(id -u ${USER}):$(id -g ${USER}) \
     -v $(pwd)/sage:/sage \
     sage /bin/bash
