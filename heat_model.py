import numpy as np

def gaussian_heat(x, y, x0, y0, Q=1, sigma=1):
    return Q * np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))
