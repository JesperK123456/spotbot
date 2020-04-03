@echo off

SET PYTHONPATH=..\..\src;%PYTHONPATH%

python3 -m templatey.clients.restful.flask.webchat.client --config ..\..\config\windows\config.webchat.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml

