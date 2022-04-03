# Dockerfile
FROM python:3.10.4-slim-buster
RUN pip install --upgrade pip

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install libpq-dev

RUN useradd myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
COPY --chown=myuser:myuser ./codesolid_demo .
copy --chown=myuser:myuser start.sh start.sh
copy --chown=myuser:myuser init.py init.py
RUN chmod 766 init.py
RUN chmod 766 start.sh
RUN pip install --user -r requirements.txt

ENV PATH=/home/myuser/.local/bin:${PATH}


CMD ["./start.sh"]