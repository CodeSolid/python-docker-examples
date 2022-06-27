docker build \
    --build-arg ARG_UID=$(id -u) \
    --build-arg ARG_GID=$(id -g) \
    -t sage:latest .
