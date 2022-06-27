# Sage Dockerfile 
FROM python:3.10.4-slim-bullseye

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y sagemath
RUN pip install jupyter jupyterlab

WORKDIR /sage

ARG ARG_GID
ARG ARG_UID
ENV GID=$ARG_GID
ENV UID=$ARG_UID
RUN adduser -q --uid $UID --gid $GID sageuser
USER sageuser

EXPOSE 8888
