def plus_minus(intle):
    if intle < (float(127)/2):
        ret =  -(float(1)/(float(127)/2)) * ((float(127)/2) - intle)
    elif intle == (float(127)/2):
        ret =  0
    elif intle > (float(127)/2):
        ret =  (float(1)/(float(127)/2)) * (intle - (float(127)/2))
    return int(100 * ret)
