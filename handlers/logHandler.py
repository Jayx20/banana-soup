from enum import Enum
from io import IOBase


class LogHandler():
    file: IOBase
    # Base log class, containing logLevels (1 Logs to Console and File, 2 logs to just console. Anything else will be ignored)
    @staticmethod
    def log(log: str, logLevel: int):
        log = str(log) + "\n"
        if logLevel == 1:
            LogHandler.file.write(log)
            print(log)
        if logLevel == 2:
            print(log)
    # Start File Stream so we can read/write from it
    @staticmethod  
    def init():
        LogHandler.file = open("log.txt", "w")
        return LogHandler.file
    # Close file (So you can see it's content)
    @staticmethod 
    def close():
        LogHandler.file.close()