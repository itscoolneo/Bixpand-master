import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getAppUrl():
        url = config.get('common data', 'baseurl')
        return url

    def getEmail():
        email=config.get('common data', 'useremail')
        return email

    def getPassword():
        password = config.read('common data','userpass')
        return password
