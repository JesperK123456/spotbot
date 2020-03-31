from programy.utils.logging.ylogger import YLogger
from programy.extensions.base import Extension

class SpotifyExtension(Extension):
    def __init__(self):
        print("SpotifyExtension initialized.")

    def execute(self, bot, clientid, data):
        params = [x.strip().upper() for x in data.split()]
        print(params)