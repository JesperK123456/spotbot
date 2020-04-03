@echo off

CLS

start %appdata%\Spotify\Spotify.exe

del spotbot.log
python -m programy.clients.events.console.client --config ..\..\config\windows\config.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml --bot_root ..\..\