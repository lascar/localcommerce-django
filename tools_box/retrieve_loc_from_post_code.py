# https://www.daniweb.com/programming/software-development/code/490561/postal-code-zips-and-location-python
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# retrieve_loc_from_post_code.py
# import retrieve_loc_from_post_code as retrieve_loc_from_post_code
# from importlib import reload
# retrieve_loc_from_post_code.MakePickleES()
# a = retrieve_loc_from_post_code.RetrieveLocPostCodeFromPickle(postal_code='04002')
import pdb
import pickle
from math import sin, cos, sqrt, atan2, radians

def MakePickleES():
    fname = "./postal_code_localization/ES.txt"
    with open(fname) as fin:
        data_str = fin.read()

    data_list = []
    for line in data_str.split('\n'):
        mylist = line.split('\t')
        if len(mylist) > 11:
            data_list.append(mylist)
    new_list = []
    for sublist in data_list:
        postal_code = sublist[1]
        # pdb.set_trace()
        latitude = float(sublist[9])
        longitude = float(sublist[10])
        data = {'latitude': latitude, 'longitude': longitude,
                'postal_code': postal_code,}
        new_list.append(data)

    with open("postal_code_localization/post_code_ES.pickle", "wb") as outfile:
        pickle.dump(new_list, outfile)
        outfile.close()

def RetrieveLocPostCodeFromPickle(postal_code):
    with open("postal_code_localization/post_code_ES.pickle", "rb") as outfile:
        code_postal_list = pickle.load(outfile)
    return SearchCode(code_postal_list, postal_code)

def SearchCode(code_postal_list, postal_code):
    for code in code_postal_list:
        if code['postal_code'] == postal_code:
            return code

def CalculDistance(pointA, pointB):
    latA = radians(pointA['latitude'])
    lonA = radians(pointA['longitude'])
    latB = radians(pointB['latitude'])
    lonB = radians(pointB['longitude'])

    dlat = latA - latB
    dlon = lonA - lonB

    a = sin(dlat / 2)**2 + cos(latA) * cos(latB) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
