from life360 import life360
from math import sin, cos, sqrt, atan2, radians
import requests, json, hashlib, sys, argparse, yaml
from blueiris import BlueIris
from config import Config

config = Config(yaml.safe_load(open('./config.yaml')))
distance = 0

def inside():
    bi = BlueIris(config.blueiris.host, config.blueiris.username, config.blueiris.password, False)
    if config.blueiris.inside.set_profile['enable']:
       try:
          profile_id = bi.profiles_list.index(config.blueiris.inside.set_profile['profile_name'])
       except:
          pass
       bi.cmd("status", {"profile": profile_id})
    if config.blueiris.inside.set_schedule['enable']:
       bi.set_schedule(config.blueiris.inside.set_schedule['schedule_name'])
    if config.blueiris.inside.set_signal['enable']:
       bi.set_signal(config.blueiris.inside.set_signal['signal_colour'])
    if config.blueiris.inside.trigger['enable']:
       bi.cmd("trigger", {"camera": config.blueiris.inside.trigger['camera_name']})
    bi.logout()

def outside():
    bi = BlueIris(config.blueiris.host, config.blueiris.username, config.blueiris.password, False)
    if config.blueiris.outside.set_profile['enable']:
       try:
          profile_id = bi.profiles_list.index(config.blueiris.outside.set_profile['profile_name'])
       except:
          pass
       bi.cmd("status", {"profile": profile_id})
    if config.blueiris.outside.set_schedule['enable']:
       bi.set_schedule(config.blueiris.outside.set_schedule['schedule_name'])
    if config.blueiris.outside.set_signal['enable']:
       bi.set_signal(config.blueiris.outside.set_signal['signal_colour'])
    if config.blueiris.outside.trigger['enable']:
       bi.cmd("trigger", {"camera": config.blueiris.outside.trigger['camera_name']})
    bi.logout()

def geofence (lat,lon):
    global config
    # Raggio della terra in m
    R = 6356988
    #
    dlon = radians(lon) - radians(config.blueiris.home_longitude)
    dlat = radians(lat) - radians(config.blueiris.home_latitude)
    #
    a = sin(dlat / 2)**2 + cos(radians(config.blueiris.home_latitude)) * cos(radians(lat)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

if __name__ == "__main__":

    api = life360(authorization_token=config.life360.token, username=config.life360.username, password=config.life360.password)
    if api.authenticate():

        circles =  api.get_circles()
        id = circles[0]['id']
        circle = api.get_circle(id)
        inside_list=[]
        for m in circle['members']:
            lat=float(m['location']['latitude'])
            lon=float(m['location']['longitude'])
            distance=geofence(lat, lon)
            if distance <= 100:
              inside_list.append(True)
        if inside_list:
           inside()
        else:
           outside()
    else:
        print ("Error authenticating")
