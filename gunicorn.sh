#!/bin/bash

#cd ~/stepik_web/web && gunicorn -b 0.0.0.0:8080 hello:wsgi_app
#cd ~/web && gunicorn -b 0.0.0.0:8080 hello:wsgi_app
cd ~/web/ask && gunicorn -b 0.0.0.0:8000 ask.wsgi
