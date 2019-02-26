import numpy as np

# This script tranforms XZY coordinates to ENU

def xyz2enu(xyz_data):

    X = [item[0] for item in xyz_data]
    Y = [item[1] for item in xyz_data]
    Z = [item[2] for item in xyz_data]

    Xm = np.mean(X)
    Ym = np.mean(Y)
    Zm = np.mean(Z)

    phi = np.arctan2(Zm, np.sqrt(Xm**2 + Ym**2))
    lam = np.arctan2(Ym, Xm)

    e = -np.sin(lam) * (X-Xm) + np.cos(lam) * (Y-Ym)
    n = -np.sin(phi) * np.cos(lam) * (X-Xm) - np.sin(phi) * np.sin(lam) * (Y-Ym) + np.cos(phi) * (Z-Zm)
    u = np.cos(phi) * np.cos(lam) * (X-Xm) + np.cos(phi) * np.sin(lam) * (Y-Ym) + np.sin(phi) * (Z-Zm)

    enu = np.array([e, n, u])

    return np.transpose(enu)
