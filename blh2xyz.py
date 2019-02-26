from math import *
import numpy as np

# This script tranforms BLH coordinates to XYZ

def blh2xyz(dataset):

    B = dataset['B']
    L = dataset['L']
    H = dataset['H']

    func_b = lambda B: B*pi/180
    func_l = lambda L: L*pi/180
    func_h = lambda H: H*pi/180

    b = list(map(func_b, B))
    l = list(map(func_l, L))
    h = list(map(func_h, H))

    # Elipsoid parameters

    a_wgs84 = 6378137.0
    e_wgs84 = 0.00669437999014

    # Transformation BLH2XYZ

    func_r = lambda b: (a_wgs84/(1-e_wgs84*sin(b)**2))
    r = list(map(func_r, b))
    B_ = np.asarray(b)
    L_ = np.asarray(l)
    H_ = np.asarray(h)
    R = np.asarray(r)

    blh = np.array([B_, L_, H_])

    X = (R + H_) * np.cos(B_) * np.cos(L_)
    Y = (R + H_) * np.cos(B_) * np.sin(L_)
    Z = (R * (1 - e_wgs84) + H_) * np.sin(B_)
    xyz = np.array([X, Y, Z])

    return np.transpose(xyz)
