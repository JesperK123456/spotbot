import xml.etree.ElementTree as ET

from programy.oob.callmom.oob import OutOfBandProcessor
from programy.utils.logging.ylogger import YLogger


class SpotifyOutOfBandProcessor(OutOfBandProcessor):
    def __init__(self):
        print("init lol")
        file = open('lol.txt', 'w')
        file.write('init lol')
        file.close()
        OutOfBandProcessor.__init__(self)
    
    def parse_oob_xml(self, oob: ET.Element):
        print("parsing lol")
        for child in oob:
            if child.tag == "child":
                print(child.text)
        return True

    def execute_oob_command(self, bot, clientid):
        print("executing lol")
        return "success"

    def process_out_of_band(self, bot, clientid, oob):
        if self.parse_oob_xml(oob) is True:
            return self.execute_oob_command(bot, clientid)
        else:
            return "fail"