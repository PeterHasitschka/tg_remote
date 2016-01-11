import configparser
import os

class CommandSwitcher:

    def __init__(self, msg):
        self.config_file = "config.cfg"
        self.msg = msg

    def execute(self):

        print("Finding command for '" + self.msg + "'")
        cmd = self.getcommand()
        print("Executing:'" + cmd + "'")
        os.system(cmd)

    def getcommand(self):
        config = configparser.RawConfigParser()
        config.read(self.config_file)

        try:
            cmd = config.get("Commands", self.msg)
        except configparser.NoOptionError as exc:
            print("Could not find command for '" + self.msg + "'. Gently exiting.")
            exit()

        return cmd

