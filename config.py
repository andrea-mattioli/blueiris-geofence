import yaml

class BlueConfig:
    def __init__(self, raw):
        self.__dict__.update(raw)
        self.proto = raw['proto']
        self.host = raw['host']
        self.username = raw['username']
        self.password = raw['password']
        self.home_latitude = raw['home_latitude']
        self.home_longitude = raw['home_longitude']
        self.distance = raw['distance']

class LifeConfig:
    def __init__(self, raw):
        self.token = raw['token']
        self.username = raw['username']
        self.password = raw['password']

class Binside:
    def __init__(self, raw):
        self.set_profile = raw['set_profile']
        self.set_schedule = raw['set_schedule']
        self.set_signal = raw['set_signal']
        self.trigger = raw['trigger']

class Boutside:
    def __init__(self, raw):
        self.set_profile = raw['set_profile']
        self.set_schedule = raw['set_schedule']
        self.set_signal = raw['set_signal']
        self.trigger = raw['trigger']

class Config:
    def __init__(self, raw):
        self.blueiris = BlueConfig(raw['blueiris'])
        self.blueiris.inside = Binside(raw['blueiris']['inside'])
        self.blueiris.outside = Boutside(raw['blueiris']['outside'])
        self.life360 = LifeConfig(raw['life360'])
