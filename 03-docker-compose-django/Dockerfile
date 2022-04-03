# Dockerfile
FROM python:3.10.4-slim-buster
RUN pip install --upgrade pip

RUN useradd myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
COPY --chown=myuser:myuser ./codesolid_demo .
copy --chown=myuser:myuser --chmod=744 start.sh start.sh
RUN pip install --user -r requirements.txt

ENV PATH=/home/myuser/.local/bin:${PATH}
ENV POSTGRES_USER=${POSTGRES_USER}


# CMD [flask, run]
CMD [./start.sh]