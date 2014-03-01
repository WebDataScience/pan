import math
from itertools import izip
import numpy as np

def dotProduct(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

def cosineMeasure(v1, v2):
    prod = dotProduct(v1, v2)
    len1 = math.sqrt(dotProduct(v1, v1))
    len2 = math.sqrt(dotProduct(v2, v2))
    return prod / (len1 * len2)

def kl(p, q):
    p = np.asarray(p, dtype=np.float)
    q = np.asarray(q, dtype=np.float)
    return np.sum(np.where(p != 0,(p-q) * np.log10(p / q), 0))

