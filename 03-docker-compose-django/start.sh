#!/bin/bash

sleep 25
python manage.py migrate
python init.py
python manage.py runserver 0.0.0.0:8000
