import configparser


config=configparser.RawConfigParser()
#reads the data from ini file
config.read(".\\configfiles\\config.ini")

class Readconfig:
    @staticmethod #we can access methods directly without creating objects
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        user =config.get('common info', 'user')
        return user

    @staticmethod
    def getPassword():
        password =config.get('common info','pwd')
        return password

    @staticmethod
    def getfname():
        firstname = config.get('checkout info', 'firstname')
        return firstname

    @staticmethod
    def getlname():
        lastname = config.get('checkout info', 'lastname')
        return lastname

    @staticmethod
    def getpcode():
        postalcode = config.get('checkout info', 'postalcode')
        return postalcode
