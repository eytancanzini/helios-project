import geocoder
from pvlib import solarposition
import pandas as pd
import sys
from time import sleep
import numpy as np

def get_latlong(g):
    ll = g.latlng
    return ll[0], ll[1]

def get_solar_pos(lat, long):
    t = pd.to_datetime('now')
    sp = solarposition.get_solarposition(t, lat, long)
    el = sp.iloc[0]['elevation']
    azi = sp.iloc[0]['azimuth']
    return el, azi, sp


if __name__ == "__main__":

    if len(sys.argv) > 1:
        custom_loc = True
    else:
        custom_loc = False
        tz = 'Europe/London'
        g = geocoder.ip('me')

    while True:
        if custom_loc is True:
            lat = float(sys.argv[1])
            long = float(sys.argv[2])
        else:
            lat, long  = get_latlong(g)
        # print(f'lat = {lat}, long = {long}')
        elevation, azimuth, solarpos = get_solar_pos(lat, long)
        print(f'Elevation  = {elevation} deg\nAzimuth = {azimuth} deg\n')
        sleep(2.5)