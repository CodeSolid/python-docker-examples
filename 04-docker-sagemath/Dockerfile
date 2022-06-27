# Sage Dockerfile 
FROM python:3.10.4-slim-bullseye
WORKDIR /data

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y sagemath
RUN pip install jupyter jupyterlab

ARG ARG_GID
ARG ARG_UID
ENV GID=$ARG_GID
ENV UID=$ARG_UID
RUN adduser -q --uid $UID --gid $GID sageuser
USER sageuser

EXPOSE 8888




# run sage -i jupyterlab_widgets


# RUN useradd -m myuser
# USER myuser
# WORKDIR /home/myuser

# COPY --chown=myuser:myuser requirements.txt requirements.txt
# COPY --chown=myuser:myuser flaskapp.py flaskapp.py
# RUN pip install --user -r requirements.txt

# ENV PATH="/home/myuser/.local/bin:${PATH}"
# ENV FLASK_APP=flaskapp
# ENV FLASK_RUN_PORT=8080
# ENV FLASK_RUN_HOST=0.0.0.0

# CMD ["flask", "run"]
