@echo off

CLS

del spotbot.log
python -m programy.clients.restful.flask.google.client --config ../../config/windows/config.google.yaml --cformat yaml --logging ../../config/windows/logging.yaml --bot_root ..\..\