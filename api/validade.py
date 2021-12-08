from math import cos, sqrt

def qick_distance(Lat1, Long1, Lat2, Long2):
    x = Lat2 - Lat1
    y = (Long2 - Long1)*cos((Lat2 + Lat1)*0.00872664626)  
    return 111.138*sqrt(x*x+y*y)