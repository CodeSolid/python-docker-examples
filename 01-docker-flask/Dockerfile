# Dockerfile
FROM python:3.10.4-slim-buster
RUN pip install --upgrade pip

RUN useradd -m myuser
USER myuser
WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
COPY --chown=myuser:myuser flaskapp.py flaskapp.py
RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"
ENV FLASK_APP=flaskapp
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
