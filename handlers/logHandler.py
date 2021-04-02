from enum import Enum



class LogHandler():
    
    @staticmethod
    def log(log: str, logLevel: int):
        if logLevel == 1:
            file = open("log.txt", "a")
            file.write(log)
            file.close
            print(log)
        if logLevel == 2:
            print(log)