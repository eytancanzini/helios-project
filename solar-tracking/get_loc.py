import geocoder
from pvlib import solarposition
import pandas as pd

def get_latlong(g):
    ll = g.latlng
    return ll[0], ll[1]

def get_solar_pos(lat, long):
    t = pd.to_datetime('now')
    sp = solarposition.get_solarposition(t, lat, long)
    el = sp['elevation']
    azi = sp['azimuth']
    return el, azi, sp

tz = 'Europe/London'
g = geocoder.ip('me')

lat, long  = get_latlong(g)
print(f'lat = {lat}, long = {long}')
elevation, azimuth, solarpos = get_solar_pos(lat, long)
print(solarpos)